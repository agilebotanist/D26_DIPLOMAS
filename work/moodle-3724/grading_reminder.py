#!/usr/bin/env python3
"""Build the "grading reminder for supervisors" page of course 3724 from two exports. Code only: the exports hold student data and stay outside every repository.

  innomood quiz-results 153168 --mode responses --out <data>/stage1-responses.csv      (Stage 1 form: supervisor, thesis title)
  innomood assign-worksheet 153169 --out <data>/fall-submission-worksheet.csv           (who has submitted, who has a grade)
  python -I -X pycache_prefix=$HOME/tmp/_code/_pycache grading_reminder.py --quiz ... --worksheet ... --out <data>/grading-reminder.html
  add --review to print only supervisor names and counts (no student data) and write nothing.

Students pick a supervisor from a list or, under "Other", type the name in a free-text comment, and they type their own thesis title, so entries can be
wrong or spelled differently. Names are matched by their tokens (spelling variants, order, Cyrillic) and the page says so politely."""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import html
import re
import sys
from collections import Counter, defaultdict

CYR = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts",
                                                       "ch", "sh", "shch", "", "y", "", "e", "yu", "ya"]))
NOISE = {"supervisor", "superviser", "supervisors", "is", "my", "would", "be", "name", "prof", "professor", "dr", "at", "innopolis", "university", "scientific",
         "advisor", "adviser", "the", "mr", "mrs", "ms", "ph", "d", "and", "i", "want", "have", "will", "by"}
TOKEN_SIM = 0.8


def translit(word: str) -> str:
    return "".join(CYR.get(ch, ch) for ch in word.lower())


def tokens(text: str) -> list[str]:
    """Name-like tokens of a free-text entry: no emails or handles, no filler words, Cyrillic transliterated."""
    text = re.sub(r"\S+@\S+|@\w+", " ", text)
    out = []
    for w in re.findall(r"[A-Za-zА-Яа-яЁё]+", text):
        t = translit(w)
        if t and t not in NOISE and len(t) > 1:
            out.append(t)
    return out


def tok_match(a: str, b: str) -> bool:
    return a == b or difflib.SequenceMatcher(None, a, b).ratio() >= TOKEN_SIM


def same_person(a: list[str], b: list[str]) -> bool:
    """Every token of the shorter name (at least two) matches some token of the longer: surname first or last, spelling variants, a patronymic."""
    short, long_ = (a, b) if len(a) <= len(b) else (b, a)
    return len(short) >= 2 and all(any(tok_match(s, l) for l in long_) for s in short)


def name_in_text(canon: list[str], text_tokens: list[str]) -> bool:
    return len(canon) >= 2 and all(any(tok_match(c, t) for t in text_tokens) for c in canon)


def plain_name(text: str) -> str:
    """The name of a short free-text entry such as 'Supervisor: A B' or 'A B is my supervisor', or '' when the entry is a sentence or has no two-or-three-word name."""
    first_line = re.split(r"[.\n;,]", re.sub(r"\S+@\S+|@\w+|\([^)]*\)", " ", text))[0]
    words = [w for w in re.findall(r"[A-Za-zА-Яа-яЁё]+", first_line) if translit(w) not in NOISE and len(w) > 1]
    return " ".join(words) if 2 <= len(words) <= 3 and len(first_line) <= 60 else ""


def latest_attempts(path: str) -> dict[str, dict]:
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig", newline="")))
    best: dict[str, tuple] = {}
    for n, r in enumerate(rows):
        email = r["Email address"].strip().lower()
        if not email or not r["Status"].lower().startswith("finished"):
            continue
        try:
            when = dt.datetime.strptime(re.sub(r"\s+", " ", r["Completed"]).strip(), "%d %B %Y %I:%M %p")
        except ValueError:
            when = dt.datetime.min
        if email not in best or (when, n) > best[email][0]:
            best[email] = ((when, n), r)
    return {e: v[1] for e, v in best.items()}


def resolve_supervisors(attempts: dict[str, dict]) -> tuple[dict[str, str], dict[str, Counter]]:
    """({email: supervisor display name or ''}, {display name: Counter of the spellings merged into it}).
    The pick-list is authoritative. Free text is handled in two passes, so the result does not depend on the order of the answers:
    first plain names ('Supervisor: A B', 'B A') form or join clusters, then longer sentences are assigned only if they contain a known name."""
    listed = Counter()
    for r in attempts.values():
        v = r["Response 1"].strip()
        if v and not v.startswith("Other") and v != "-":
            listed[v] += 1
    clusters = [{"tokens": tokens(name), "plain": Counter({name: listed[name]}), "raw": Counter({name: listed[name]}), "listed": name} for name in listed]
    who_cluster: dict[str, dict | None] = {}
    pending = []
    for email, r in attempts.items():
        picked = r["Response 1"].strip()
        if picked in listed:
            who_cluster[email] = next(c for c in clusters if c["listed"] == picked)
            continue
        comment = r["Response 8"].strip()
        plain = plain_name(comment)
        if not plain:
            pending.append((email, comment))
            continue
        toks = tokens(plain)
        target = next((c for c in clusters if c["listed"] and name_in_text(c["tokens"], toks)), None) or next((c for c in clusters if same_person(c["tokens"], toks)), None)
        if target is None:
            target = {"tokens": toks, "plain": Counter(), "raw": Counter(), "listed": None}
            clusters.append(target)
        target["plain"][plain] += 1
        target["raw"][plain] += 1                                     # the review shows cleaned names only, never free text
        who_cluster[email] = target
    for email, comment in pending:                                  # sentences: only a known name inside them counts
        text_tokens = tokens(comment)
        target = next((c for c in clusters if name_in_text(c["tokens"], text_tokens)), None)
        if target is not None:
            target["raw"]["(longer sentence)"] += 1
        who_cluster[email] = target
    def display(c) -> str:
        if c["listed"]:
            return c["listed"]
        latin = [(n, k) for k, n in c["plain"].items() if re.fullmatch(r"[A-Za-z' -]+", k)]
        return max(latin or [(n, k) for k, n in c["plain"].items()])[1].title() if c["plain"] else ""
    who = {e: (display(c) if c else "") for e, c in who_cluster.items()}
    variants: dict[str, Counter] = defaultdict(Counter)
    for c in clusters:
        variants[display(c)].update(c["raw"])
    return who, variants


def build_page(waiting: list[dict], asof: str) -> str:
    by_prof: dict[str, list[dict]] = defaultdict(list)
    for w in waiting:
        by_prof[w["supervisor"] or ""].append(w)
    known = sorted((p for p in by_prof if p), key=lambda p: p.split()[-1].lower())
    e = lambda s: html.escape(s, quote=True)
    out = ['<div class="alert alert-info" style="border-left: 5px solid #5bc0de;">',
           "  <p>Dear colleagues, a friendly reminder. The list below shows students who have submitted chapters 1 and 2 (Fall submission) and are still waiting for a grade, "
           "grouped by the supervisor they named in the Stage 1 form. Thank you for taking a look when you have a moment.</p>",
           f'  <p class="mb-0">State on {e(asof)}: {len(waiting)} students are waiting, spread over {len(known)} supervisors'
           + (f", plus {len(by_prof.get('', []))} where no supervisor could be identified." if by_prof.get("") else ".") + "</p>", "</div>", "",
           '<div class="alert alert-warning" style="border-left: 5px solid #f0ad4e;">',
           "  <p><strong>How this list was made.</strong> The supervisor and the thesis title come from the Stage 1 form. Students picked their supervisor from a list or, under \"Other\", typed the name themselves, "
           "and they typed their own thesis title. For each student the latest answer was used and matched to the status of the Fall submission on " + e(asof) + " (submitted, no grade yet). "
           "Different spellings of one supervisor's name (transliteration, word order, Cyrillic) were merged automatically.</p>",
           "  <p class=\"mb-0\"><strong>Please check it, it may be incorrect.</strong> The matching was done by a program, so a student can appear under the wrong supervisor or with a wrong title, "
           "two supervisors may have been merged by mistake, and a grade entered after " + e(asof) + " is not shown. If you notice a mistake, please report it to the course team and ignore the entry in the meantime. Thank you.</p>",
           "</div>", "",
           "<h4>Overview</h4>", '<table class="table table-sm table-striped" style="max-width: 32em;">',
           "  <thead><tr><th>Supervisor</th><th>Waiting for a grade</th></tr></thead>", "  <tbody>"]
    for p in known:
        out.append(f"    <tr><td>{e(p)}</td><td>{len(by_prof[p])}</td></tr>")
    if by_prof.get(""):
        out.append(f"    <tr><td>Supervisor not identified</td><td>{len(by_prof[''])}</td></tr>")
    out += ["  </tbody>", "</table>", "", "<h4>Students by supervisor</h4>"]
    for p in known:
        out += [f"<h5>{e(p)}</h5>", '<table class="table table-sm table-striped" style="max-width: 52em;">',
                "  <thead><tr><th>Student</th><th>Thesis title (as entered by the student)</th></tr></thead>", "  <tbody>"]
        for w in sorted(by_prof[p], key=lambda x: x["name"].lower()):
            out.append(f"    <tr><td>{e(w['name'])}</td><td>{e(w['title'])}</td></tr>")
        out += ["  </tbody>", "</table>"]
    if by_prof.get(""):
        out += ["<h5>Supervisor not identified</h5>",
                "<p>For these students the Stage 1 form gave no supervisor, or a name that could not be matched. If one of them works with you, we would be grateful for a quick note.</p>",
                '<table class="table table-sm table-striped" style="max-width: 52em;">',
                "  <thead><tr><th>Student</th><th>Thesis title (as entered by the student)</th></tr></thead>", "  <tbody>"]
        for w in sorted(by_prof[""], key=lambda x: x["name"].lower()):
            out.append(f"    <tr><td>{e(w['name'])}</td><td>{e(w['title'])}</td></tr>")
        out += ["  </tbody>", "</table>"]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--quiz", required=True); ap.add_argument("--worksheet", required=True)
    ap.add_argument("--out"); ap.add_argument("--review", action="store_true", help="print supervisor names and counts only; write nothing")
    ap.add_argument("--asof", default=dt.date.today().strftime("%d %b %Y"))
    a = ap.parse_args()
    attempts = latest_attempts(a.quiz)
    who, variants = resolve_supervisors(attempts)
    sheet = list(csv.DictReader(open(a.worksheet, encoding="utf-8", newline="")))
    waiting, no_sub, graded = [], 0, 0
    for r in sheet:
        if r["grade"].strip():
            graded += 1
        elif r["status"].lower().startswith("submitted"):
            email = r["email"].strip().lower()
            att = attempts.get(email)
            waiting.append({"name": r["name"].strip(), "supervisor": who.get(email, ""), "title": re.sub(r"\s+", " ", att["Response 2"]).strip() if att else "(no Stage 1 form found)"})
        else:
            no_sub += 1
    if a.review:
        per = Counter(w["supervisor"] or "(not identified)" for w in waiting)
        print(f"students on the sheet {len(sheet)} | graded {graded} | waiting (submitted, no grade) {len(waiting)} | not submitted, no grade {no_sub} | with a Stage 1 form {len(attempts)}")
        print(f"supervisors with waiting students: {len([k for k in per if k != '(not identified)'])}")
        for k, n in sorted(per.items(), key=lambda kv: (-kv[1], kv[0])):
            merged = {s: c for s, c in variants.get(k, {}).items()}
            print(f"  {n:3d}  {k}   <- {len(merged)} spelling(s) merged" if len(merged) > 1 else f"  {n:3d}  {k}")
        print("\nall supervisor clusters (display name, total students in the Stage 1 form, spellings merged):")
        for k, c in sorted(variants.items(), key=lambda kv: -sum(kv[1].values())):
            if len(c) > 1:
                print(f"  {sum(c.values()):3d}  {k}: " + " | ".join(f"{s!r} x{n}" for s, n in c.most_common(6)))
        return 0
    if not a.out:
        print("give --out (or --review)", file=sys.stderr)
        return 2
    page = build_page(waiting, a.asof)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote {a.out}: {len(waiting)} students, {len(page)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())

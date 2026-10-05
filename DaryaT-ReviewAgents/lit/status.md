# Paper inventory — Darya Tolmeneva

Two sources. The first is her 2026-08-31 review (`_raw/review.md`), written for the
multi-agent platform framing she later dropped. The second is her Obsidian vault
(`_raw/Diploma/`), which is the live one: 11 papers with PDFs, 25 atomic notes and 13
question notes, built between 20 September and 5 October.

Updated: 2026-10-05

## Current reading — the Obsidian vault

PDFs are in `_raw/Diploma/статьи/<paper>/`, each beside her own note on it. Not copied into
`lit/pdfs/` to avoid holding 11 MB twice; the vault is the authoritative copy.

| # | Key (provisional) | Title | Section | PDF | Her note | BibTeX | Relevance |
|---|---|---|---|---|---|---|---|
| 1 | `gilb_inspection` | Inspection Manual (one-page inspection, Malotaux 2008) | 2.1 | yes | yes | no | CRITICAL — the backbone of her best thinking. HB4, HB9, HB11, HB12, HB13, HB16, HB17 each generated a question or a metric |
| 2 | `cohen2006peer` | Peer Review Best Practices (Cohen 2006) | 2.1, 2.6 | yes | yes | no | CRITICAL — review goals as measurable outcomes; external vs internal metrics; checklist construction and availability |
| 3 | `cohen2006effective` | Effective Code Review (Cohen 2006) | 2.1 | yes | yes | no | HIGH — the "Why Code Review?" functions: communication, trust, mentoring, knowledge spread |
| 4 | `cihan2024practice` | Automated Code Review In Practice | 2.4 | yes | yes | yes | CRITICAL — industrial study, 4335 PRs. 73.8% of automated comments resolved, but PR closure went from 5h52m to 8h20m. This is the evidence behind her "AI review does not guarantee time savings" |
| 5 | `tufano2025codereview` | Automating Code Review: A Systematic Literature Review | 2.4 | no | yes | yes | HIGH — already in her bib from the August review |
| 6 | `aicodechanges` | Does AI Code Review Lead to Code Changes? A Case Study of GitHub Actions | 2.4, 2.5 | yes | yes | no | HIGH — §V.D recommends defining AI's role and limits explicitly, which is the source of her boundaries question |
| 7 | `repo_reviewer` | RepoReviewer: A Local-First Multi-Agent Architecture for Repository-Level Code Review | 2.3 | yes | stub | no | HIGH — the closest architectural precedent; her note is still a stub |
| 8 | `swe_review` | SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review | 2.3 | yes | stub | no | HIGH — agentic review in the issue-resolution loop; note is a stub |
| 9 | `review_conversation` | Code Review is a Conversation: Toward Conversational AI Review Assistants | 2.2, 2.3 | yes | yes | no | CRITICAL — the source of her two-level orchestration idea |
| 10 | `agents_change_dev` | Does Working with AI Agents Change How Developers Code, Test, and Review? | 2.5 | yes | yes | no | HIGH — behaviour change, which is where her "people review less attentively" observation can be grounded |
| 11 | `evaluating_agentsmd` | Evaluating AGENTS.md | 2.3 | yes | yes | no | MED — context files did not reduce steps to working code, and generated ones cost more without confirmed benefit |

## Verified

| Key | Source |
|---|---|
| `cihan2024practice` | arXiv:2412.18531, Cihan, Haratian, İçöz, Gül, Devran, Bayendur, Uçar, Tüzün, 2024 |
| `tufano2025codereview` | arXiv:2503.09510, verified earlier |
| `he2025lmasurvey`, `cai2025masdesign`, `koech2026phoenix`, `guo2023falsepositives`, `chomatek2025cicd`, `kuliamin2024dynamic` | From the August review, verified on 2026-09-21 |

The remaining nine from the vault are recorded as she filed them and need checking. Her
folder names are not citations: `gilb_inspection` and the two Cohen items in particular need
real bibliographic records, since the Inspection Manual is doing the most work in her thesis
and currently has no verifiable reference at all.

## Two notes that are already experiment designs

Worth saying out loud, because they are better than the checklist comparison agreed at the
meeting:

**Unique findings per agent.** Merge duplicate reports, then per agent measure confirmed
defects found only by that agent, and the overlap with others. High overlap with little
unique contribution is grounds to question whether the role earns its cost. Derived from
HB12 and HB13. This is a testable design, not an idea.

**Confirmed defects per unit cost.** Her own metric, close to the classic Defect Rate, and
the thing that makes "is this agent worth running" answerable.

She also has the classic internal metrics written down with units: inspection rate
(kLOC/person-hour), defect rate (defects/person-hour), defect density (defects/kLOC), and
the external-versus-internal distinction from Cohen.

## Earlier reading, August review

Seven verified entries from `_raw/review.md` are in `references.bib`. That review argued for
the multi-agent platform framing she dropped on 21 September, so the references stand but
the argument around them does not. Two of them had wrong author attributions, corrected in
the bib.

## Gaps

| Missing | Why it matters |
|---|---|
| A real citation for the Inspection Manual and both Cohen items | They carry her strongest material and currently have none |
| Notes for RepoReviewer, SWE-Review and the code review SLR | All three are stubs under 300 bytes, and the first two are the closest architectural precedents to what she wants to build |
| Own commentary | "Мои мысли" is empty in 16 of the 25 atomic notes, and that is the section worth the most |
| Anything on defect seeding or residual defect estimation | Raised on 28 September as an evaluation route, nothing read |
| Anything on the intern and junior role | A11, raised 5 October, nothing read |

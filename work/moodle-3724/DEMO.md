# Demo script: working on a Moodle course with `innomood` and Claude Code

About fifteen minutes. Replace `<course>` with a course id, `<section>` with a section id and `<cmid>` with an activity id (the `id=` in an activity's URL). Every command that writes is a dry run until `--live`, and each dry run is shown before the live run.

## 0. Before the demo

Open Moodle in Chrome through the university network or VPN and sign in with SSO, then run `innomood login` once and `innomood doctor`. The skill reuses your own signed-in session: nothing is stored in the repository and nothing bypasses a refusal from the server.

## 1. Look at a course (read only, nothing can change)

```bash
innomood course <course>            # sections, hidden or visible, number of activities
innomood assignments <course>       # dates, team settings, grade maximum, and anything that looks wrong
innomood quizzes <course>           # settings and how many attempts exist
innomood grades <course>            # the gradebook tree
innomood summary <section>          # the text a section shows, saved locally
```

Point out what a first look finds without opening a browser: dates a year away, duplicated hidden items with identical names, a one-line task description, plain-text schedules.

## 2. Show the improved version next to the original

```bash
innomood section-add <course> --after <section> --name "Topic: improved layout (DEMO, hidden)"          # dry run: where it would go
innomood section-add <course> --after <section> --name "Topic: improved layout (DEMO, hidden)" --live    # inserted, hidden at once, named, everything else checked
innomood update-summary <new-section> improved.html            # dry run: word differences and links
innomood update-summary <new-section> improved.html --live     # backup first, then saved and verified
innomood compare <new-section> improved.html                   # the live text equals the file
innomood page-create <course> --section <n> --name "General feedback" --content page.html --visibility show   # a longer text as a page of its own, dry run then --live
```

What to say: Moodle creates a new section visible, so the skill hides it in the very next request and then proves that every other section and summary is unchanged. The improved page links to the real activities instead of copying them, so no grades or attempts are duplicated.

## 3. Use the course data

```bash
innomood quiz-results <cmid> --out answers.csv                 # every attempt of a quiz as a CSV
innomood assign-worksheet <cmid> --out sheet.csv               # who submitted, who has a grade, status per student
```

Then ask Claude for a page built from them, for example a polite reminder to supervisors listing the students who still wait for a grade, grouped by supervisor. Show the `--review` step: it prints names and counts only, so the matching of free-text names can be checked before any page exists. Student data stays outside the repository.

## 4. Change things safely

```bash
innomood assign-edit <cmid> --due "YYYY-MM-DD HH:MM" --cutoff "YYYY-MM-DD HH:MM"   # dry run, then --live
innomood assign-grade <cmid> --email a@x.org --grade 6.5 --feedback "..."          # one correction; refuses a visible assignment
innomood feedback-create <course> --section <n> --name "Team data" --text intro.html   # hidden and named
innomood feedback-item-add <cmid> --type text --name "Team name" --required
innomood quiz-create <course> --section <n> --name "Check 1" --time-limit 10 --attempts 1
```

## 5. What to stress

| Rule | Why it matters |
|---|---|
| Dry run first, live second, in two commands | You see exactly what changes before it does |
| Backup before each write, read back after | A wrong save is found at once and can be restored |
| Only the intended fields change | The whole form is sent back as it was |
| Hidden by default for anything new | Students never see a half-built item |
| No user is ever deleted or unenrolled, deletes are guarded | Only empty, hidden, exactly named items can go |
| Student data never goes into a repository or a chat | Exports live in a work folder outside the repo |
| A refusal from the server is never bypassed | The skill uses your own login, not a workaround |

## 6. After the demo

The demo topic is removed with the guarded `page-delete` and `section-delete` (hidden, empty, exact name), or by hand in Moodle. The commands, the rules learned from the real course and the limits (for example: removing or editing a question of a quiz is left to Moodle) are in `~/_code/_skills/innomood/SKILL.md`.

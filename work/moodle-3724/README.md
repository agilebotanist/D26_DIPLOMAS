# Course 3724 on Moodle: working folder

Course `https://moodle.innopolis.university/course/view.php?id=3724`, [F26] Thesis Project, Moodle 5.1. Everything here was done with the `innomood` skill (`~/_code/_skills/innomood`). The check itself is in [audit-2026-11-08.md](audit-2026-11-08.md), the step-by-step script for colleagues in [DEMO.md](DEMO.md).

## What was added to the course (2026-11-08)

One new topic, hidden, right after the visible "Fall 2026" and before "Topic 2", holding two Pages. No original section, activity or summary was changed (checked by comparing section names, visibility, activity counts and summary hashes before and after).

| Item | Id | What it is | Source |
|---|---|---|---|
| Topic "Fall 2026: improved layout (DEMO, hidden)" | section 35010 | The same information students see now, restructured: where you are, and one table of sessions and materials (the lecture schedule joined with the four workshop topics). A link points to the feedback page. | `fall-2026-improved.html` |
| Page "General feedback on chapters 1 and 2" | cm 160184 | The summary for the whole group: what worked well, what most drafts still need (a table), and a checklist for the next draft. Visible, inside the hidden topic. | `general-feedback-page.html` |
| Page "Grading reminder for supervisors: chapters 1 and 2" | cm 160185 | A polite reminder for supervisors: students who have submitted chapters 1 and 2 and have no grade yet, grouped by the supervisor they named, with their thesis title as entered. **Hidden at the activity level as well**, inside the hidden topic. | generated, see below |

The feedback text comes from `../stage-ch1-2-feedback-to-thesis-group-EN.md`. Every sentence is kept as written, only regrouped. The "Written for" line of the source is left out.

The reminder page contains student names. Two locks protect it: the topic is hidden and the page itself is hidden. Never show that page to students, and do not unhide it when the topic is shown. (A first version had its own top-level topic; it was emptied and deleted.)

## The supervisors page

`grading_reminder.py` builds it from two exports. The exports and the page hold student data, so they live outside every repository, in `~/tmp/_code/_skills/innomood/data3724/` (excluded from Time Machine).

```bash
D=~/tmp/_code/_skills/innomood/data3724
innomood quiz-results 153168 --mode responses --out $D/stage1-responses.csv          # Stage 1 form: supervisor, thesis title
innomood assign-worksheet 153169 --out $D/fall-submission-worksheet.csv               # who has submitted, who has a grade
python3 -I -X pycache_prefix=$HOME/tmp/_code/_pycache grading_reminder.py --quiz $D/stage1-responses.csv --worksheet $D/fall-submission-worksheet.csv --review
python3 -I -X pycache_prefix=$HOME/tmp/_code/_pycache grading_reminder.py --quiz $D/stage1-responses.csv --worksheet $D/fall-submission-worksheet.csv --out $D/grading-reminder.html --asof "<date>"
innomood page-edit 160185 --content $D/grading-reminder.html      # dry run, then add --live
```

`--review` prints only supervisor names, cleaned spellings and counts, no students, so the matching can be checked first. How it works: each student's latest finished attempt is used; the supervisor is the pick-list choice, or for "Other" the name found in the free-text comment (spelling variants, word order, Cyrillic and "Supervisor: ..." prefixes are merged, and a sentence counts only if it contains a known name); a student is listed when the Fall submission has been submitted and has no grade. Students with no supervisor found go under "Supervisor not identified". Refresh the page after grading progresses by running the same commands again.

## Undoing

Delete the two Pages (`innomood page-delete 3724 <cmid> --name "..."` after hiding them), then the topic (`innomood section-delete 3724 35010 --name "..."` after emptying its text and its activities). Backups of every pushed text are in `~/tmp/_code/_skills/innomood/backups/`.

## Open

The reminder follows the Fall submission (chapters 1 and 2). If the Stage 1 quiz grade (264 of 272 attempts still "Not yet graded") should count too, the script needs one more input. The lecture video in the Introduction block comes from a personal draft area: check it as a student.

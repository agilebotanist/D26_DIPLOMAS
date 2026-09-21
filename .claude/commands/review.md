---
description: Review a draft with a reviewer profile, or spec a section before writing
argument-hint: "<file> [--profile thesis-committee|se-researcher|industry-practitioner|consistency-checker] [--spec]"
---

Review: $ARGUMENTS

Follow `.claude/skills/reviewers/SKILL.md`. Default profile is `thesis-committee` for a
diploma chapter and `se-researcher` for a paper. `--spec` means pre-draft mode: produce
what the section must contain instead of reviewing what it says.

Load the student's `lit/topic.md` for the research questions, and their
`feedback/call-context/` if this targets a venue. Write the output to
`<Student>/feedback/reviews/`.

Never modify the draft.

---
name: reviewers
description: Simulate expert reviewers on a thesis chapter or paper draft, or produce a pre-draft spec of what a section must contain. Use when asked to review, critique, or assess a student's draft, to check a paper against a venue's criteria, or to say what a section needs before it is written.
---

# Reviewers

Structured feedback on a draft, in the voice of the person who will actually judge it.
Two modes:

- **Pre-draft, spec:** before a section is written, produce the checklist it must satisfy.
  This is the cheaper mode and the one students skip.
- **Post-draft, review:** after it is written, evaluate it and name what is missing.

Invoke: `Review <file> [§Section] using profile <name> in post-draft mode.`
or `Produce a spec for <section> using profile <name> in pre-draft mode.`

## Profiles

Generic and reusable across students. The venue-specific and thesis-specific material is
**not** in the profile; it is loaded separately.

| Profile | Use for | Judges |
|---|---|---|
| `thesis-committee` | Diploma chapters and the full thesis | Does the work clear the bar for the degree: problem, method, result, evidence |
| `se-researcher` | Papers and methodology chapters | Validity, controls, statistics, threats, related work |
| `industry-practitioner` | Industry-track submissions | Practical relevance, would a practitioner change anything |
| `consistency-checker` | Full drafts before submission | Internal coherence, formatting, claims matching evidence |

Start with `thesis-committee` for diploma work and `se-researcher` for papers. Run
`consistency-checker` last, on a complete draft, because it checks across sections.

## Context loading

Before reviewing, read in this order:

1. The profile from `profiles/`.
2. `<Student>/lit/topic.md` — the RQs and objectives the draft must serve. A review that
   does not know the RQs cannot tell whether a section earns its place.
3. `<Student>/feedback/call-context/<venue>.md`, if the target is a venue submission.
   Create it from `templates/call-context.md` when a new venue is targeted: evaluation
   criteria, paper type, length, formatting, and any prior rejection to close.
4. The draft itself.

## Output

Post-draft uses `templates/review-output.md`, pre-draft uses `templates/spec-output.md`.

Findings are graded MUST, SHOULD, CONSIDER. A MUST is something that fails the draft as it
stands. Keep the MUST list short and real: a review where everything is a MUST gets read as
noise and changes nothing.

Write to `<Student>/feedback/reviews/<target>-<mode>-<profile>-<YYYY-MM-DD>.md`.

## Rules

1. **Never modify the draft.** The reviewer reads; the student writes. A reviewer that
   silently fixes things teaches nothing and hides the finding.
2. Adopt the persona fully. Judge as that reader would, not as a helpful assistant.
3. One pass, complete output. No interactive back-and-forth mid-review.
4. Be phase-aware. Flag only what can realistically be fixed before the deadline in
   `<Student>/PROFILE.md`. A perfect review of an unfixable problem wastes the remaining time.
5. Quote the draft when making a finding. An unlocated criticism cannot be acted on.
6. Reviews are English, and follow the writing rules in the root `CLAUDE.md`.

## Feedback loop

Review, student decides on MUST items, student revises, re-run the same profile to verify.
Repeat until no MUST remains. Record what was decided and rejected in the student's
`feedback/` folder, so the same finding is not re-litigated at the next review.

---
description: Scaffold a new student folder from the shared skeleton
argument-hint: "<FirstName><LastInitial>-<TopicSlug> \"Full Name\" \"Topic\""
---

Add a student: $ARGUMENTS

1. Copy `templates/student/` to a root folder named `<FirstName><LastInitial>-<TopicSlug>`,
   matching the convention in `CLAUDE.md`, for example `DaryaT-ReviewAgents`.
2. Fill `PROFILE.md` with the name, topic, and whatever deadlines are known. Leave the rest
   as placeholders rather than inventing them.
3. Create `ACTIONS.md` from `meetings/templates/actions.md` with an empty open list.
4. Create `lit/topic.md` from `.claude/skills/lit-review/templates/topic.md` and fill what
   is known about the topic. Do not fabricate research questions; mark them as open.
5. Add the student to the board in `README.md`.

Then tell me what in `PROFILE.md` and `lit/topic.md` still needs the student to answer.

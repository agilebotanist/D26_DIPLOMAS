---
description: Roll up open actions across all students - overdue, stalled, due next
argument-hint: "[student folder name; omit for all students]"
---

Roll up open actions for: $ARGUMENTS (omit means all students).

Read every `<Student>/ACTIONS.md` and report in the order given in `meetings/CLAUDE.md`:

1. **Overdue**, most overdue first, with the number of days.
2. **Stalled**: carried over twice or more, whatever the due date.
3. **Due before the next meeting.**
4. **Blocked**, with what blocks them.

Do not list everything that is open. This roll-up exists to decide what to chase, so end
with the two or three students who need attention before the next meeting, and why.

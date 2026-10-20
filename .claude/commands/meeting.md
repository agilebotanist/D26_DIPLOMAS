---
description: Process a meeting transcript into per-student notes and update their action lists
argument-hint: "[date or transcript filename; omit to process everything in meetings/raw/]"
---

Process the meeting transcript: $ARGUMENTS

Follow `meetings/CLAUDE.md` exactly. If no argument is given, process every file in
`meetings/raw/` that has no matching `meetings/<date>/` folder yet.

Produce, per that workflow:

1. `meetings/<date>/transcript.md` — cleaned and speaker-attributed
2. `meetings/<date>/joint.md` — cross-cutting decisions only
3. `<Student>/meetings/<date>.md` — one Minto note per student discussed, in Russian,
   one screen, with their open actions listed at the bottom so it can be sent as is
4. `<Student>/FEEDBACK.md` — one Telegram-HTML message: feedback, decisions and open actions together,
   neutral register (Обсудили / Что требует доработки / Решили / Действия), never «ты»
5. `<Student>/ACTIONS.md` — reconciled: closed what was accepted, carried over what was
   not mentioned, added what was newly agreed
6. One appended line in `meetings/index.md`, and the board in `README.md` refreshed

Then report which students got notes, and tell me what is ready to send.

# Meetings workflow

Turn a supervision meeting transcript into a summary the student can be sent, and update
that student's action list.

## How it starts

The supervisor drops a transcript into `meetings/raw/`. Nothing else is needed. Any file
there without a matching processed folder is unprocessed work.

Trigger: "process the new meeting", "обработай встречу", or `/meeting [date]`.

## What it produces

```
meetings/raw/<whatever-zoom-called-it>.vtt   # input, never edited, never deleted
meetings/<YYYY-MM-DD>/
├── transcript.vtt        # the raw file, moved here on processing
├── transcript.md         # cleaned, speaker-attributed
└── joint.md              # cross-cutting decisions only, at most ten lines
<Student>/meetings/<YYYY-MM-DD>.md           # SHAREABLE: this is what goes to the student
<Student>/ACTIONS.md                         # updated in place
meetings/index.md                            # one appended line
```

The per-student note is the shareable artifact. It must stand alone when pasted into a
chat or an email: the student should need no other file to know what was decided and what
they owe. That is why their open actions are repeated at the bottom of the note.

`joint.md` and `transcript.md` are supervisor-side. Do not send them.

## Language

Notes and actions are in **Russian**, because the meetings are. The em-dash prohibition in
the root `CLAUDE.md` covers English academic prose only; in Russian the em-dash is ordinary
correct punctuation, so write Russian as a Russian speaker would.

`lit/`, thesis text and BibTeX stay English.

## The hard constraint: concision

A per-student note fits on one screen: target 25 lines, hard cap 40.

The transcript is what was said. The note is what it means. Never walk through the meeting
turn by turn. If the note does not fit on a screen, it is not summarised yet, only
transcribed.

## Minto shape

The note is decision-bearing: it answers "where does this work stand, and what happens
next?". Answer first, never chronological.

1. **Итог** — one sentence, the judgment. "Тема сузилась до сравнения агентного и
   человеческого ревью; следующий шаг - выбрать датасет" is an answer.
   "Обсудили ревью-агентов" is a topic label, and is wrong.
2. **Почему** — two to four reasons supporting the итог, all the same kind of thing,
   strongest first. Each carries its evidence from the meeting on the same line.
3. **Решения** — what was settled, so it does not get reopened next meeting.
4. **Действия** — who does what by when, with stable IDs.
5. **Открытые вопросы** — only what actually blocks something.

Drop any section that would be empty. An empty heading is noise.

## Steps

### 1. Clean the transcript

Read the raw file. Determine the meeting date from the filename or the first timestamps,
create `meetings/<date>/`, and move the raw file in as `transcript.vtt`.

**There are usually two sources, and they are good at different things. Use both.**

| Source | Gives | Lacks |
|---|---|---|
| Zoom `.vtt` | Speaker labels, per-cue timestamps | Poor word recognition: mangled words, wrong word boundaries, broken agreement |
| Whisper `.txt` (run separately by the supervisor) | Much more accurate words | No speaker labels, no timestamps |

Take the wording from the Whisper text and recover who said what, plus coarse timestamps,
by aligning it against the VTT. Neither alone is enough: the VTT alone produces notes built
on misheard words, and the Whisper text alone cannot tell two speakers apart, which matters
because a joint meeting runs student by student.

Whisper hallucinates filler on silence, typically repeated lines like "Продолжение
следует..." at the head of the file before anyone speaks. Drop them and say so.

Produce `transcript.md`: merge consecutive turns by the same speaker into paragraphs, keep
one coarse timestamp per block, and say at the top which source gave the words and which
gave the speakers.

Do not "fix" the Russian beyond obvious recognition artefacts, and never invent a sentence
that makes a garbled turn read smoothly. Where a phrase is unrecoverable, keep it and mark
it `[неразборчиво]`, with a guess only if it is worth chasing: `[неразборчиво: «джефф
лея», предположительно GLiNER]`.

If only the VTT exists, say so in the note and treat every specific term in it as suspect.

### 2. Segment by student

Attendees come from the speaker labels. A joint meeting runs student by student; find the
boundaries where the discussion moves from one to the next.

A student who attended but whose work was not discussed gets no note. Silence is
information, and a note saying "ничего не обсуждали" is noise.

Anything binding all students (process, deadlines, tooling, next meeting format) goes in
`joint.md` and is not repeated in each note.

### 3. Write the notes

Use `templates/student-note.md`, filled from the transcript only.

Where the ASR is too garbled to be sure what was agreed, write what the transcript supports
and mark the rest `[уточнить]`. Never resolve an ambiguity by guessing what a supervisor
would plausibly have said. An action the student never agreed to is worse than a missing
one, because they will be held to it.

### 4. Update the action list

Open `<Student>/ACTIONS.md` and reconcile it against the meeting:

- An action the student reported done **and** that was accepted moves to Выполнено, closed
  on the meeting date. Reported but not accepted stays open.
- An action not mentioned at all stays open, and its `Перенос` counter goes up by one.
  Two carry-overs is a signal: say so in the next note's Почему section.
- New commitments become new rows with the next free ID. IDs are per student, stable, never
  reused and never renumbered, so a note written in March can still reference `A7`.
- Every action needs an owner and an absolute date. If the meeting set none, write
  `[срок?]`; do not invent one.

Then rewrite the `Сейчас` line at the top: the single most important open action, in one
sentence. It is the first thing the student reads.

Finally copy the student's open actions into the Действия section of their note, so the
note can be sent on its own.

### 5. Index and board

Append one line to `index.md`: date, attendees, and the joint decision in one clause.
Update the `README.md` cohort board at the repo root: phase, next milestone, open action
count, last meeting date.

## Roll-up: /actions

Read every `<Student>/ACTIONS.md` and report in this order:

1. Overdue, most overdue first, with the number of days.
2. Carried over twice or more, regardless of due date. This is the D25 failure mode: six
   `todo.md` files existed and every one was empty, because nothing was ever reconciled.
3. Due before the next meeting.
4. Blocked, with what blocks them.

Do not list everything open. The roll-up exists to decide what to chase.

## Rules

1. Never edit or delete anything in `raw/`. It is the record.
2. Never write an action nobody agreed to.
3. A note over 40 lines goes back for another pass.
4. If the итог reads as a topic label, rewrite it as a judgment.
5. The per-student note must stand alone. Assume the student has nothing else.

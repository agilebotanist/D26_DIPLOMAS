# Meetings workflow

Turn a supervision meeting transcript into a summary the student can be sent, and update
that student's action list.

## How it starts

The supervisor drops a transcript into `meetings/raw/`. Nothing else is needed. Any file
there without a matching processed folder is unprocessed work.

Trigger: "process the new meeting", "обработай встречу", or `/meeting [date]`.

When nothing is waiting in `raw/`, the supervisor does not have to drop anything: "process
Friday's meetings", "обработай пятничные встречи", "process the meetings of <date>" and
`/meeting <date>` start the automated route below, which fetches the recordings itself.

## Automated intake: Zoom to notes

Student one-on-ones run back to back in one Zoom meeting, and the whole chain from recording
to notes is automated. Run it end to end without asking for confirmation between stages;
stop only at a point marked **STOP**. It runs on macOS in zsh (`myzoom`, `whisp`), and the
shell and Python lines in the root `CLAUDE.md` that mention PowerShell and Windows paths do
not apply to it. Read the `myzoom` skill first for its auth and read-only rules.

**The meeting is «DM26 Students», ID `86189981896`.** The `myzoom` default (`config`
`meeting_id`) is the lecture room `84591791997`, and with it `recordings list` returns
nothing for supervision days. Always pass `--meeting-id 86189981896`; never change the
default, the lectures need it.

1. **Find the sessions.** Resolve the day to an absolute date `D` ("Friday" is the latest
   Friday not in the future; say which date you took). Run
   `myzoom recordings list --meeting-id 86189981896 --from <D-1> --to <D+1>` and keep the
   sessions whose UTC start date is `D`. A day holds one session per student plus restarts
   after dropped connections, so expect more sessions than students. **STOP** if there are
   none (other meeting ID, recording still processing, or recording was off) and say so;
   never try other IDs. On `kind: "auth"` run `myzoom doctor`, relay its `fix`, and **STOP**:
   the user runs `! myzoom auth login`, you cannot.
2. **Fetch every session** into its own empty directory in the scratchpad, never into the
   repo: `myzoom fetch --meeting-id 86189981896 --date D --uuid '<uuid>' --into <dir>/raw
   --audio --media-dir <dir>/media`. It yields the Zoom VTT (speakers and timestamps), the
   M4A and the participants CSV.
3. **Identify the student** from the participants CSV: the one name that is not the host.
   Zoom display names are unreliable (`azizvundirov`), so match against the student folder
   names and `PROFILE.md`; **STOP** and ask if a name matches nobody. A second session of the
   same student minutes after the first is a continuation after a dropped connection: same
   note, files suffixed `-2`. A session with no speech is a test: keep its files, write
   no note.
4. **Transcribe the audio in Russian.** Always
   `whisp -l ru -m large-v3 --srt -q -o <dir>/ru <file>.m4a`: language forced, never
   auto-detected (earlier runs came out as English translations with mangled terms), SRT
   requested because the aligner needs timestamps. `whisp` runs one job at a time and takes
   about two minutes per half hour of audio on this Mac, so start all sessions as one
   background batch and wait for the `.srt` files to appear (`whisp` with no arguments lists
   running jobs); do not poll in a loop. Then read a few lines of each output: if it is not
   Russian, the run is wrong.
5. **File everything** in `meetings/<D>/`, one prefix per student (given name, lowercase
   Latin), copied from the scratch directories. Audio is kept in the repo, as for earlier
   meetings:

   ```text
   <name>-recording.m4a   <name>-transcript.vtt   <name>-participants.csv
   ru/<name>-recording.srt   ru/<name>-recording_transcript_raw.txt   <name>-transcript.md
   ```

   Build `<name>-transcript.md` with `python3 meetings/merge_transcript.py
   ru/<name>-recording.srt <name>-transcript.vtt <name>-transcript.md`. The script gives
   Whisper's words the Zoom speaker, drops silence hallucinations and subtitle credits, and
   collapses a decoding loop into `[повтор]`. Then read the whole file and mark what is still
   garbled by hand (`[неразборчиво]`, `[обрыв связи]`) as the "Clean the transcript" step
   below requires. Zoom's own VTT is never a source of words, only of speakers and time.
6. **Process the meeting** with steps 2 to 5 below: per-student notes, `FEEDBACK.md`,
   `ACTIONS.md`, `joint.md`, `index.md`, the `README.md` board. In `joint.md` say that the
   files came from Zoom and Whisper `-l ru`, give times in UTC, and record any dropped
   connection.
7. **Report**: for each student what is ready to send, every `[уточнить]` with the reason,
   dropped connections and which part of the talk they cost, actions carried over twice or
   more, and the supervisor's own actions (АС) that are overdue. Do not commit unless asked.

Zoom is read-only here: no step creates, changes or deletes anything on the account.
Participant lists are student data and stay in this private repo.

## What it produces

```
meetings/raw/<whatever-zoom-called-it>.vtt   # input, never edited, never deleted
meetings/<YYYY-MM-DD>/
├── transcript.vtt        # the raw file, moved here on processing
├── transcript.md         # cleaned, speaker-attributed
└── joint.md              # cross-cutting decisions only, at most ten lines
<Student>/meetings/<YYYY-MM-DD>.md           # SHAREABLE: this is what goes to the student
<Student>/ACTIONS.md                         # updated in place
<Student>/FEEDBACK.md                        # SHAREABLE: feedback, decisions and actions in one Telegram message
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

**There are up to three sources, good at different things. Use them together.**

| Source | Gives | Lacks |
|---|---|---|
| Zoom `.vtt` | Speaker labels, per-cue timestamps | Poor word recognition: mangled words, wrong word boundaries, broken agreement |
| Whisper `.srt` | Accurate words **and** timestamps | No speaker labels |
| Whisper `.txt` | Accurate words | No speakers, no timestamps |

When both an `.srt` and a `.vtt` exist, run the aligner instead of doing it by hand:

```bash
python meetings/merge_transcript.py <base>.srt <base>.vtt <out>.md
```

Both files run on the same recording-relative clock, so it assigns each Whisper cue the
speaker whose Zoom cue overlaps it most, merges consecutive turns, and drops Whisper's
silence hallucinations ("you", "Продолжение следует...", subtitle-credit lines).

Neither source alone is enough: the VTT alone produces notes built on misheard words, and
the Whisper text alone cannot tell speakers apart, which matters because several students
may be in one recording or one day.

**Check whether Whisper transcribed or translated.** If the output is English while the
meeting was in Russian, it was run with `--task translate`, and technical terms are
mangled through translation: SAST becomes "state elite", Qwen2.5-Coder becomes "QN5 coder",
false positive becomes "Fox positive", виртуальные потоки become "virtual flows",
литературный обзор becomes "political review". The meaning survives, the names do not.
Cross-check every specific term against the Russian VTT, say in the transcript header that
this happened, and ask for `--task transcribe` next time.

Produce `transcript.md` and say at the top which source gave the words, which gave the
speakers, and whether translation was involved.

Do not "fix" the Russian beyond obvious recognition artefacts, and never invent a sentence
that makes a garbled turn read smoothly. Where a phrase is unrecoverable, keep it and mark
it `[неразборчиво]`, with a guess only if it is worth chasing: `[неразборчиво: «джефф
лея», предположительно GLiNER]`.

If only the VTT exists, say so in the note and treat every specific term in it as suspect.

### Several meetings on one day

Back-to-back one-on-ones are the normal pattern. They share one `meetings/<date>/` folder,
and every file is prefixed with the student's given name in lowercase Latin:

```
meetings/2026-09-28/
├── ilya-transcript.vtt     ilya-whisper.srt     ilya-whisper.txt     ilya-transcript.md
├── mikhail-...
└── joint.md                # what applies to everyone, once
```

One `joint.md` per day, not per meeting. Cohort-wide decisions repeated across four
one-on-ones are recorded there once, and each student's note carries only what concerns
them.

### 2. Segment by student

Attendees come from the speaker labels. A joint meeting runs student by student; find the
boundaries where the discussion moves from one to the next.

A student who attended but whose work was not discussed gets no note. Silence is
information, and a note saying "ничего не обсуждали" is noise.

Anything binding all students (process, deadlines, tooling, next meeting format) goes in
`joint.md` and is not repeated in each note.

### 3. Write the notes

Use `templates/student-note.md`, filled from the transcript only. Then write
`<Student>/FEEDBACK.md` from `templates/feedback.md` (see step 4b).

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

### 4b. Write FEEDBACK.md

`<Student>/FEEDBACK.md` is the single message sent to the student: feedback, decisions and the
open action list together. It sits at the student root and is overwritten after each
meeting; git keeps the history.

It is written in Russian in a neutral register, as a record rather than a personal letter:
lead judgment, Обсудили, Что требует доработки, Решили, Действия. Never address the student
as «ты»: use impersonal constructions («стоит», «нужно», «тема подаётся»), and «вы» only
where a direct address cannot be avoided. The action list is a copy of the open rows of
`ACTIONS.md`, ordered by priority, one line each: ID, due date, action. Keep it under 4000 visible characters, the
Telegram message limit. Rules:

- Only what the supervisor said or demonstrably meant at the meeting, plus what the student
  sent. Praise only what was actually valued; do not add balance for its own sake.
- No new demands. Anything asked for already exists in `ACTIONS.md` and is referenced by ID.
- Shareable means shareable: candid assessment of pace, motivation or authorship of text
  stays in `PROFILE.md` and `feedback/`, never here.
- It is a draft for the supervisor to edit before sending; say so in the report.

**Format: Telegram HTML.** The file is pasted into Telegram with parse mode HTML, so it
contains no Markdown. Allowed tags: `<b>`, `<i>`, `<u>`, `<s>`, `<code>`, `<pre>`,
`<blockquote>`, `<a href>`. Not supported, so never used: `<p>`, `<br>`, `<ul>`, `<li>`,
`<h1>`, tables, `#` headings. Line breaks are real newlines, and every line that is followed
by another non-blank line ends with two trailing spaces: Telegram ignores them, but a
Markdown or HTML preview collapses single newlines without them (the preview is how the
supervisor checks the file). Lists are `•` or `1.`, the
lead judgment goes in `<blockquote>`, section titles in `<b>`. Escape `&`, `<`, `>` in text
as `&amp;`, `&lt;`, `&gt;`. No HTML comments (Telegram would show them). The same applies
to any other text meant for Telegram.

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

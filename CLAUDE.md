# D26_DIPLOMAS — cohort workspace (Innopolis, 2026-2027)

One repo for all diploma students of the 2026-2027 batch. Shared workflows live here at
the root; each student has a folder at the root for individual follow-up.

**This repo is private to the supervisor.** `feedback/` may hold candid assessment that is
not meant for the student verbatim. What goes to the student is the meeting note and the
action list, nothing else.

## Layout

```
D26_DIPLOMAS/
├── CLAUDE.md                  # this file — routing and shared rules, the only copy
├── README.md                  # cohort board: who is where, what is overdue
├── meetings/
│   ├── CLAUDE.md              # ← meeting workflow: transcript to notes and actions
│   ├── raw/                   # drop transcripts here; processing moves them out
│   ├── templates/             # note, joint, actions
│   ├── index.md               # one line per meeting
│   └── YYYY-MM-DD/
│       ├── transcript.vtt     # raw, as recorded
│       ├── transcript.md      # cleaned, speaker-attributed
│       └── joint.md           # cross-cutting decisions only
├── <Student>-<Topic>/         # one per student, see templates/student/
│   ├── PROFILE.md             # topic, RQ, objectives, deadlines, links
│   ├── ACTIONS.md             # the live action list — never let this go stale
│   ├── _raw/                  # whatever the student sent, exactly as sent
│   ├── meetings/YYYY-MM-DD.md # per-student meeting note (Minto)
│   ├── lit/                   # literature workspace, same skeleton for everyone
│   ├── feedback/              # supervisor feedback and review outputs
│   ├── work/                  # drafts, notes, thesis and paper text
│   └── code/                  # implementation and experiments
├── templates/student/         # skeleton to copy for a new student
├── work/                      # supervisor's own cross-cutting notes
└── .claude/skills|commands/   # the shared workflows
```

Student folder name: `<FirstName><LastInitial>-<TopicSlug>`, e.g. `DaryaT-ReviewAgents`.

## Taskflow routing

| Task | Command | Loads |
|---|---|---|
| Turn a meeting transcript into notes and actions | `/meeting [date]` | `meetings/CLAUDE.md` |
| See who owes what across all students | `/actions [student]` | `meetings/CLAUDE.md` |
| Literature review, any phase | `/lit <student> [phase]` | `.claude/skills/lit-review/` |
| Review a draft against a venue's criteria | `/review <file> --profile <p>` | `.claude/skills/reviewers/` |
| Add a student | `/new-student <Name> <Topic>` | `templates/student/` |

Per-student variables (RQ, lit section map, topic codes, relevance dimensions) live in
`<Student>/lit/topic.md` and `<Student>/PROFILE.md`. The workflows read them from there.
Never fork a workflow per student; parameterise it.

### `_raw/` — what the student sent

Drop student submissions into `<Student>/_raw/` exactly as received: documents, CVs, PDFs,
pasted messages, reading logs. Nothing there is edited, and nothing there is authoritative.

It is intake, not the record. Anything that matters gets read out into the right place:
references into `lit/references.bib` and `lit/status.md`, thesis text into `work/`, facts
about the student into `PROFILE.md`, commitments into `ACTIONS.md`. Then the raw file stays
as provenance.

A file sitting in `_raw/` that has not been read out is unprocessed work, the same as a
transcript in `meetings/raw/`.

## Shared rules

### Never read PDFs directly

Do not use the Read tool on `.pdf`. Convert first, then read the Markdown:

```powershell
npx -y @firecrawl/anydoc <student>\lit\pdfs\paper.pdf -o <student>\lit\converted\paper.md
```

`-o` takes a **file** path, not a directory. Passing a directory fails with `EISDIR`.

`anydoc` is the converter of choice: it reads multi-column layouts in true reading order
and raises an error naming the pages when a PDF is a scan, instead of quietly emitting
plausible nonsense. Fall back to `pdfplumber` only when geometric column control is needed.
The `/pdf2md` and `/convert-documents-to-markdown` skills wrap both.

Alternative for papers found online: the `read_*_paper` MCP tools extract text directly.

### Python

Use system Python explicitly. Bare `python` can resolve to a skill venv that lacks the
Google and PDF libraries:

```
C:\Users\asadovykh\AppData\Local\Programs\Python\Python314\python.exe
```

### Shell

PowerShell is primary; the Bash tool is available for POSIX scripts. Each takes its own
syntax, so do not mix them in one call. Use Windows paths (`C:\...`), not `/c/...`.

### Writing style — English academic prose

Applies to thesis text, papers, summaries, insights and anything a reviewer will read.
The point is that the text should not read as machine-generated:

- No em-dash (`—`) and no `---` in prose. Recast with a comma, colon, parentheses or a
  new sentence. En-dashes in ranges (`12--15`) are correct typography and stay.
- No emoji, no decorative markers.
- No horizontal rules between sections. Headings alone.
- No bullet lists where every bullet opens with a bolded phrase and a colon.
- No filler openers or closers ("In today's fast-paced world", "In conclusion").
- Avoid "not only ... but also", "delve", "leverage", "robust", "comprehensive".
- Avoid mechanical Strengths/Weaknesses/Conclusion scaffolding unless the format demands it.

**This rule does not apply to the Russian meeting notes.** In Russian typography the em-dash
is ordinary correct punctuation. Write Russian notes as a Russian speaker would.

### Language

| Artifact | Language |
|---|---|
| Meeting notes, action lists, `PROFILE.md` | Russian |
| Thesis, papers, lit summaries, insights, `references.bib` | English |
| Workflow instructions (this file, skills) | English |

Meetings are conducted in Russian; notes the student reads stay in Russian.

### Manual download lists

When a student must fetch papers by hand, always give a table with Author / Year / Title /
URL, sorted by priority. The URL column is never omitted: a DOI link where one exists,
otherwise a Google Scholar search link.

## Conventions

- BibTeX keys: `authorYYYYkeyword`, lowercase, e.g. `richardson2018microservices`.
- Paper PDFs: `<topic>_<NN>_<author><year>_<description>.pdf`, topic codes per student in
  `<Student>/lit/topic.md`.
- Books: `_book_<Author>_<Year>_<Title-Hyphenated>.pdf`. Theses: `_thes_<...>.pdf`.
- Action IDs are stable and per student: `A1`, `A2`, ... Never renumber, never reuse.
- Dates are absolute and ISO: `2026-09-21`, never "next week".
- Always read `<Student>/lit/status.md` before searching for papers.

## What D25 got wrong, and what this repo fixes

Carried forward from the 2025-2026 cohort, where every student had their own repo:

| D25 problem | D26 fix |
|---|---|
| Six copies of a 550-line lit workflow, drifting apart | One `lit-review` skill, parameterised by `topic.md` |
| All six `todo.md` files empty; actions never tracked | `ACTIONS.md` per student with stable IDs, updated by `/meeting` |
| No meeting record at all across ten repos | `meetings/` is the clock; every meeting produces a note |
| No cross-student view of who owes what | `/actions` roll-up and `README.md` board |
| `.gitignore` excluded `.claude/`, so workflows were never shared | `.claude/` is committed here on purpose |
| Folder names drifted: `converted/` vs `extracted_text/`, `pdfs/` vs `downloads/` | One skeleton in `templates/student/` |
| Reviewer skill hard-bound to one venue | Profiles are generic; venue criteria go in per-student `feedback/call-context/` |

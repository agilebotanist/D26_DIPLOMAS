---
name: lit-review
description: Literature review pipeline for a diploma student - inventory, search and download, summarise, snowball, synthesise, then feed the thesis. Use when working in any student's lit/ folder, or when asked to find, download, summarise, score or synthesise papers for a thesis chapter, or to update a download list of missing PDFs.
---

# Literature review

One pipeline, all students. Everything that differs between students lives in
`<Student>/lit/topic.md`: the thesis title, research questions, the chapter section map,
topic codes for filenames, and the relevance scoring dimensions.

**Read `<Student>/lit/topic.md` first, every time.** If it is missing or still has
placeholders, fill it with the student before searching for anything. A literature review
without a defined section map produces a pile of PDFs, not a chapter.

## Layout

```
<Student>/lit/
├── topic.md          # ← per-student parameters; read this first
├── status.md         # paper inventory and progress, the single source of truth
├── download.md       # missing PDFs to fetch by hand, priority order
├── readings.md       # prioritised reading list, Tier 1/2/3
├── snowball.md       # backward and forward reference tracking
├── references.bib    # verified BibTeX, keys match status.md exactly
├── pdfs/             # downloaded papers and books
├── converted/        # PDF to Markdown
├── summaries/        # one file per paper, <key>.md
└── insights/         # cross-paper synthesis, one file per chapter section
```

Templates are shared and live in this skill's `templates/`. Do not copy them into each
student's folder; that is how D25 ended up with six diverging copies.

## Pipeline

```
1 Inventory    → status.md
2 Search       → pdfs/ + converted/, whatever cannot be fetched → download.md
3 Summarise    → summaries/
4 Snowball     → snowball.md, loops back to 2
5 Synthesise   → insights/
6 Write        → thesis sections in work/
```

Phases are resumable. To resume, read `status.md`, then `readings.md`, then any
`insights/*.md`.

### Phase 1 — Inventory

Before searching for anything, check what is already there: `pdfs/`, `summaries/`,
`readings.md`, and any thesis draft in `work/`. Only search for what is genuinely missing.

`status.md` is one table:

| # | Key | Title | Section | PDF | Converted | Summary | BibTeX | Relevance |
|---|-----|-------|---------|-----|-----------|---------|--------|-----------|

Update it after every phase, per paper. It is the only place that knows the true state.

### Phase 2 — Search and download

Search in three tiers, narrow to broad, using the queries in the student's `topic.md`:

1. Core: the exact intersection of the thesis topic.
2. Technical: the individual techniques, patterns and tools.
3. Broad: the surrounding field, for foundations and surveys.

MCP tool priority: `search_semantic` (cross-database, citations, year filters), then
`search_arxiv` (CS preprints), then `search_crossref` (DOI and metadata validation), then
`search_google_scholar` (citation counts, coverage).

Prefer well-cited work for foundations. Citation count is the cheapest available proxy for
what the field considers settled, and it is what the supervisor will ask about.

Download with `download_arxiv` / `download_semantic` into `<Student>/lit/pdfs/`, then
rename to `<topic>_<NN>_<author><year>_<description>.pdf` using the topic codes from
`topic.md`.

#### Missing PDFs go to download.md

Anything that cannot be fetched automatically, because it is paywalled, behind a publisher
login, or has no open-access copy, is written into `<Student>/lit/download.md` instead of
being reported in chat and forgotten.

That file is the student's fetch queue, so keep it strictly to Author, Year, Title, URL:

- **Missing papers stay at the top of the page**, ordered by priority, so the list is
  actionable without scrolling. Highest priority is whatever blocks the section the student
  is writing next.
- A row moves down to "Got it" only once the PDF is actually in `pdfs/`.
- The URL column is never empty: a DOI link where one exists, otherwise the best direct
  link, otherwise a Google Scholar search link.
- No status columns, no notes, no commentary. Four columns, priority order.

Re-sort the list whenever priorities change. Update it in the same turn as the search that
found the gap, never "later".

#### Convert before reading

Never use the Read tool on a PDF:

```powershell
npx -y @firecrawl/anydoc <Student>\lit\pdfs\paper.pdf -o <Student>\lit\converted\paper.md
```

`-o` takes a file path, not a directory. Passing a directory fails with `EISDIR`.

### Phase 3 — Summarise

One file per paper in `summaries/<key>.md`, from the template matching its tier:

| Tier | Template | Depth |
|---|---|---|
| 1 Must-read | `templates/summary_full.md` | Full read: contribution, method, findings, quotes, limitations, snowball refs |
| 2 Key sections | `templates/summary_partial.md` | Abstract, method, results |
| 3 Skim | `templates/summary_skim.md` | Abstract and conclusion only |

Every summary scores relevance on the dimensions in `topic.md`, 0 to 5 each. The scoring
guide: 5 is core and directly reusable, 3 is useful background, 1 is a keyword match only.

The `/notebooklm` skill helps extract quotes, reported challenges and evaluation metrics
from a paper without rereading it whole.

### Phase 4 — Snowball

After each Tier 1 or 2 summary, harvest its references into `snowball.md`.

Backward: which works does it cite. Forward: what cites it, via Semantic Scholar or Google
Scholar "cited by". A work cited by three or more of the papers already in `status.md` is
high priority, and almost always a foundation the review cannot omit. High-priority
snowball hits that are not open access go straight into `download.md`.

Stop when the foundational gaps in `topic.md` are filled and new papers stop changing the
insight files.

### Phase 5 — Synthesise

One file per chapter section in `insights/`, from `templates/insight_topic.md`. A synthesis
needs at least three papers, and states: consensus with the papers supporting it,
contradictions with the thesis's chosen position, gaps relevant to the research questions,
and what to adopt, adapt or avoid.

The insight file ends with a draft paragraph for the chapter. That paragraph is the point
of the whole pipeline.

### Phase 6 — Write

Feed `insights/` into the thesis sections in `<Student>/work/`. Every research question
must have supporting literature, and every claim in the chapter must trace to a key in
`references.bib`.

## references.bib

Verify metadata with MCP before adding an entry. Never transcribe it from a PDF's title
page, which is where wrong years and mangled venue names come from.

```
search_crossref(query="exact title")   or   get_crossref_paper_by_doi(doi="10.xxxx/...")
```

Every entry: author, title, year, and a venue field. DOI where one exists, `eprint` for
arXiv preprints. Key format `authorYYYYkeyword`, matching `status.md` exactly. No duplicates.

## Rules

1. Read `topic.md` before anything else.
2. Never read a PDF directly. Convert first.
3. A paper that cannot be downloaded goes into `download.md` in the same turn, at the top,
   in priority order.
4. `status.md` is updated in the same turn as the work it records, not later.
5. No BibTeX entry without MCP verification.
6. Summaries and insights are English, and follow the writing rules in the root `CLAUDE.md`.
7. Never copy these templates into a student folder.

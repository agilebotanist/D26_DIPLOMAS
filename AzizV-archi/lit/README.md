# lit/

Literature workspace. The pipeline is shared: `.claude/skills/lit-review/`.

Start by filling `topic.md`. Nothing else in this folder can be done well before it exists,
because `topic.md` holds the section map that decides which papers belong here at all.

| File | Purpose |
|---|---|
| `topic.md` | Per-student parameters: RQs, section map, topic codes, scoring dimensions |
| `status.md` | Paper inventory and processing state, the source of truth |
| `download.md` | Missing PDFs to fetch by hand, priority order, missing ones at the top |
| `readings.md` | Prioritised reading list, Tier 1/2/3 |
| `snowball.md` | Backward and forward reference tracking |
| `references.bib` | Verified BibTeX, keys matching `status.md` |
| `pdfs/` | Downloaded papers |
| `converted/` | PDF to Markdown, never read a PDF directly |
| `summaries/` | One file per paper |
| `insights/` | Cross-paper synthesis, one file per chapter section |

Templates live in the skill, not here. Do not copy them in.

English, throughout.

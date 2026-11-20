# Brief: Agentic AI and the IT industry

Working title: "Surviving". Status: draft captured from the request of 2026-11-17, to be corrected by the speaker.

## The talk

A 20 to 25 minute talk on the impact of agentic AI on the IT industry. The audience is mixed: IT experts, students, a few business people. The tone may be futuristic and provocative. It gives no investment recommendations and avoids conspiracy thinking.

## Voice

The talk is personal, not academic (speaker's decision, 2026-11-17). It is one practitioner telling what he sees, does and worries about. It must not intimidate the audience with numbers, sources and reports.

What follows from this:

- The spine of the talk is the speaker's own experience and a few stories. The research stays backstage: it decides what he can say with confidence, and it sits in speaker notes, a backup section and the bibliography for questions.
- A slide carries at most one number, and only when the number is the story. Most slides carry a picture, a story or a question.
- References go in the slide footer, as in the speaker's other decks (speaker's decision, 2026-11-18): author, year and short title, small, one line. The body of a main slide still carries no citations, report names or logos. A source is named aloud only when it is part of the story ("the people who measure this stopped measuring in September").
- Stories about people and companies come before statistics. The audience should remember three or four stories and two pictures (the two curves and the five forces), not figures.
- Personal experience cannot be invented. Every first-person story on a slide comes from the speaker.

## Intent

Step back and look at the situation from above (meta-analysis), with as little hype as possible. The talk combines three kinds of evidence: what analysts say, the honest state of the technology, and the speaker's own daily practice. It ends with indicators: how to prepare, what to focus on, what to watch.

The audience should leave with questions worth arguing about, more than with predictions.

## Analytical frames

1. Porter's five forces, applied to the software and IT services industry under agentic AI.
2. The S-curve of technology performance, set against the expectations (hype) curve, to discuss where we are.

## The speaker's theses, to be tested by research

Each thesis is a hypothesis. Research must look for evidence both for and against.

| # | Thesis | What would test it |
|---|---|---|
| T1 | We live in a revolution. Agents accelerate work strongly, yet need many iterations and expert validation. | Measured productivity studies, RCTs, adoption data |
| T2 | AI has already "killed" some occupations: graphic design, copywriting, translation. | Freelance market and employment data for these occupations |
| T3 | Benchmarks are revealing and inflated. Producers over-optimise for them. Real work differs. | Benchmark contamination and gaming studies, field studies |
| T4 | Biases remain: probabilistic output, optimisation to please the user, plausible results with gaps an expert finds. | Sycophancy and reliability research |
| T5 | Generated code carries technical debt, security, architecture and maintenance problems. | Code quality and vulnerability studies |
| T6 | Frontier models grow expensive and are controlled by few actors and countries. IP rights are unclear. | Pricing trends, market concentration, court rulings |
| T7 | Vendor analytics may be inflated ahead of IPOs. | Who publishes which numbers, and their interests |
| T8 | Physical limits are coming: data centres, memory, energy, parallelisation. | Capex, energy and memory supply data |
| T9 | Signs of change: IT layoffs, security incidents (agents attack and defend), systems rebuilt cheaply by agents. | Labour data, incident reports, documented cases |
| T10 | Idea to proof of concept takes hours. Good for creators who understand customers, and anything in software can be copied at almost no cost. | Cases, SaaS market reactions |
| T11 | What cannot be copied: customer service, reliability and trust, hardware, physical presence. | Moat analysis, five forces |
| T12 | Humans stay responsible: someone pays or goes to jail. | Liability law and cases |
| T13 | Domains where validation is hard stay human longer: cyber-physical systems, multi-physics, large physical objects, health, machinery. | Evidence on where agents fail |
| T14 | Business bottlenecks: physical limits, token cost, denial of access to frontier models (sanctions). Competition still exists. | Export controls, open-weight model progress |
| T15 | How many IT specialists are needed is an open question: does the desire for innovation grow faster than agent autonomy? Shocks come before stabilisation. | Labour forecasts, Jevons-type arguments, history of earlier automation |
| T16 | The average coder disappears. Valuable: people skills, broad knowledge, deep domain expertise, understanding of human and agent biases, initiative. | Skills-demand data, hiring trends |
| T17 | Personal experience: daily use for office, admin, teaching and research work. No way back. High cognitive load, project switching, exhaustion. Talking to people remains the source of ideas. | Studies on work intensification and cognitive load |

## Source policy

Mostly analyst and institutional reports, a few arXiv papers, primary data where it exists. Every source is tagged with who published it and what interest they have. The Telegram chat export "AI Projects" (2020-11 to 2026-06) is treated as a list of leads with a likely bias towards inflating agent capabilities, never as evidence.

## Citations

One `references.bib` in this folder, in the layout of `msd_review/literature/references.bib` (speaker's decision, 2026-11-17): keys `authorYYYYkeyword` in lowercase, organisations as author for analyst reports, aligned fields `author`, `title`, `year`, `url`, `doi`, `keywords`, `note`. `keywords` carries the research strand (`1.analysts`, `2.benchmarks`, `3.labour`, `4.economics`, `5.industry`, `6.security`). `note` carries the verification level (primary page read, secondary only) and the publisher's interest. The report and the slides cite by key, written `[@key]`. A source that was not read at its primary page is marked so in `note` and is checked before it reaches a slide.

## Converted sources

Converted Markdown is kept in the project (speaker's decision, 2026-11-17): `converted/reports/` for PDFs and reports, `converted/web/` for scraped pages. The PDFs, logs and raw HTML stay in `~/tmp/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/` as regenerable material. `converted/sync.sh` copies new conversions across.

## Insights step

Between the research notes and the talk structure there is an insights step, shaped after `msd_review/review/proc/insights/README.md` (added 2026-11-17 at the speaker's request). The research notes are organised by research strand and answer "what did we find". The insight files in `insights/` are organised by theme of the talk and answer "what can be said on a slide".

Each theme file carries several insights. Each insight has:

1. a title that is a claim, usable as a slide title;
2. the number or data series that carries it, with chart-ready data points and the `[@key]`;
3. one or two verbatim quotes, each checked with `msd_review/scripts/verify_quotes.py` against the converted source in `converted/`, with the key and the speaker's role and interest. A quote that does not pass is not used;
4. one concrete example or case;
5. the counter-evidence, in proportion;
6. speaker-note material: provenance, caveats, who has an interest;
7. a confidence level, and which thesis in this brief it supports, corrects or refutes;
8. a question it raises for the audience;
9. the personal angle: where this meets the speaker's own practice, and how he could say it in one plain sentence without a number. This line is what reaches the slide. Items 2, 3, 5 and 6 are backstage material for speaker notes, backup slides and questions.

Themes: I1 where we are on the S-curve and the expectations curve; I2 benchmarks and reality; I3 the productivity paradox; I4 quality, verification and the mathematics case; I5 economics and physical limits; I6 access, geopolitics and competition; I7 industry structure under five forces; I8 security; I9 jobs; I10 skills and human factors; I11 how hype is produced and how to read claims.

## Deliverables

1. This brief.
2. Research notes and a synthesis report in `research_notes/` and `reports/`.
3. A proposed talk structure, for discussion.
4. Slides with inno-marp, with report-style charts and diagrams.

## Language

All research, reasoning, structure and slide drafts are in English. Translation happens once, at the final stage (speaker's decision, 2026-11-17).

## Open points

Target language of the final translation, date and venue, and whether the speaker's own workflow is shown live or as screenshots.

# Literature parameters — Darya Tolmeneva

Seeded from the 2026-09-21 meeting. The topic is not chosen yet, so most of this file is
deliberately empty. Fill it as the direction narrows; do not invent research questions to
make the file look complete.

## Thesis

| Field | Value |
|---|---|
| Title | Not chosen. Area: code review automation, agents and static analysis |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Where this stands

The initial idea, orchestrating agents whose outputs are reduced to comments on a diff, was
rejected by the student herself on 2026-09-21. Her reason: human review rests on
communication, discussion and decisions, and an agent that only emits findings does not
provide that. The reasoning holds, so the direction is genuinely open.

## Candidate directions

One of these is to be chosen by 2026-10-31.

| # | Direction | What an experiment might look like |
|---|---|---|
| 1 | How well existing analysers actually perform | Measure on a corpus with known defects |
| 2 | Automatic application of security playbooks | Apply to real projects, measure what is caught and what breaks |
| 3 | Embedding partly AI-based tools into the review pipeline | Compare pipeline with and without |
| 4 | Using an LLM to improve static analysis output, including where to look next | Compare raw analyser output against LLM-refined output |

The supervisor also suggested a data source that fits several of these: an open-source
project with a large number of pull requests, processed to compare which approach reaches a
better result faster.

## Research questions

OPEN. Nothing to record until a direction is chosen. Leave this section empty rather than
filling it with a plausible guess.

## Objectives

OPEN.

## Chapter 2 section map

OPEN. This is the section that decides which papers belong in this folder at all, so
searching in volume before it exists produces a pile of PDFs rather than a chapter.

## Topic codes

Provisional, covering the whole candidate area. Narrow once the direction is fixed.

| Code | Meaning |
|---|---|
| `review` | Code review practice, what makes it work, what it costs |
| `sa` | Static analysis tools, precision, recall, adoption |
| `agent` | LLM agents applied to review and defect finding |
| `sec` | Security review and playbooks |

## Relevance dimensions

Provisional.

| Dimension | What scores high |
|---|---|
| Review practice | Empirical evidence about how review actually works |
| Tooling | Evaluates concrete analysers or agents against a baseline |
| Automation | Studies what automation adds or removes from review |
| Method | Has a reusable evaluation design |

## Search queries

Tier 1, core:

```
search_semantic("modern code review empirical study effectiveness", year="2018-")
search_semantic("LLM automated code review evaluation", year="2023-")
```

Tier 2, technical:

```
search_semantic("static analysis tool comparison precision recall", year="2020-")
search_semantic("false positives static analysis developer response", year="2020-")
search_semantic("pull request review automation study", year="2020-")
```

Tier 3, broad:

```
search_semantic("code review social communication aspects", year="2018-")
```

## Inclusion and exclusion

**Include:** 2018 or later, except seminal work; peer-reviewed or a cited preprint; has a
method section; empirical evidence over opinion.

**Exclude:** non-English; vendor whitepapers; tool announcements with no evaluation.

## Known foundational gaps

| Sub-topic | Expected work | Status |
|---|---|---|
| What makes human review effective | The paper already read, which prompted the rejection. Record its citation here | need |
| Static analyser effectiveness | TBD | need |
| LLM-assisted review | TBD | need |

The paper the student read before 2026-09-21 is the one concrete source so far. Get its
citation into `references.bib` first; it is the anchor for whichever direction is chosen.

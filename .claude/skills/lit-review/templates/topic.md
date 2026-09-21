# Literature parameters — <Student Name>

Everything the lit-review pipeline needs that is specific to this thesis. The skill reads
this file before doing anything. Placeholders left unfilled block the pipeline.

## Thesis

| Field | Value |
|---|---|
| Title | <working title> |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Research questions

| # | Question |
|---|---|
| RQ1 | <question> |
| RQ2 | <question> |

## Objectives

| # | Objective | Focus |
|---|---|---|
| O1 | <what the thesis will build or establish> | <the concrete artifact or study> |
| O2 |  |  |

## Chapter 2 section map

Each section gets one file in `insights/`. This map is what turns a pile of papers into a
chapter, so define it before searching.

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | <foundations of the field> | <what this section must establish> |
| 2.2 | <the central technique or approach> |  |
| 2.3 | <alternatives and comparisons> |  |
| 2.4 | <evaluation methods and metrics> |  |

## Topic codes

Used in PDF filenames: `<topic>_<NN>_<author><year>_<description>.pdf`

| Code | Meaning |
|---|---|
| `<code>` | <what belongs under it> |

## Relevance dimensions

Each summary scores 0-5 on each dimension. Pick four or five that between them decide
whether a paper earns a place in the chapter.

| Dimension | What scores high |
|---|---|
| <Dim1> | <what a 5 looks like> |
| <Dim2> |  |

## Search queries

Tier 1, core: the exact intersection of this thesis.

```
search_semantic("<query>", year="2020-")
```

Tier 2, technical: individual techniques, tools and patterns.

```
search_semantic("<query>", year="2020-")
```

Tier 3, broad: surrounding field, foundations and surveys.

```
search_semantic("<query>", year="2018-")
```

## Inclusion and exclusion

**Include:** published 2018 or later, except seminal works; peer-reviewed or a preprint with
citations; addresses the topic directly; has a reproducible method or empirical evidence.

**Exclude:** non-English; no method section, so opinion pieces and blog posts count as grey
literature only; superseded by a newer version from the same authors; vendor whitepapers.

## Known foundational gaps

Works the review cannot omit and does not yet have. Phase 4 stops when this list is empty.

| Sub-topic | Expected work | Status |
|---|---|---|
| <sub-topic> | <author or "TBD"> | need |

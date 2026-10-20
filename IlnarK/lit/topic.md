# Literature parameters — Ilnar Khasanov

Seeded from the 2026-10-05 meeting. His own materials are not in the repo yet, so this is
thinner than it should be. Action A5 closes that.

## Thesis

| Field | Value |
|---|---|
| Title | Not named. Working area: estimating the cost of a data schema change through propagation cost |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## The problem as he states it

Large codebases have become hard to change, and schema change is among the refactoring
problems that remain unsolved. Before planning a sprint, a team cannot say what an
`extract entity` will cost: how many files it touches, how many person-hours, whether it
fits in two weeks. The only current route is to produce a draft and run static analysis
over it, which is slow and awkward to work with.

The operations he cares about: splitting a flat table into two with a one-to-many relation,
and the reverse. Fine on interactive, spreadsheet-like systems; bad through an ORM, which
is where his own work hurts.

## Where the meeting moved it

His "blast radius" already has a name. Dependencies between components are encoded in a
matrix, and the share of the system a change reaches is **propagation cost**. The quantity
of interest is then the difference in propagation cost between the state before a schema
change and the state after, which is a measure of evolvability: whether the next change
gets cheaper or dearer.

Performance is a separate axis and must not be merged into this one. Merging two tables may
win milliseconds while making the system harder to maintain, and a single number would hide
that. If latency is wanted too, the matrix cell can hold a value rather than 0 or 1.

## Where the 2026-10-19 meeting moved it

The focus shifted away from propagation cost and effort estimation. The working question is
now how much of the impact of a domain model change in ORM-based Python code (SQLAlchemy,
Django) static type checkers detect: MyPy, ty (Astral), Pyright, Pyrefly. The contribution
beyond a comparison is a tool: static blast-radius analysis over the ORM and the code base,
plus an LLM agent's estimate, explicitly covering what a type checker cannot see by
construction (dynamic attributes, raw SQL). Evaluation: large GitHub projects with synthetic
changes seeded in the mutation-testing manner (defined fault types, frequencies, proper
randomisation), comparing what MyPy finds with what the extended analysis finds.

Sources he cited, not yet in `references.bib`: a 2016 paper on ORMs not checking types; a
2022 paper on dynamic attributes being hard for MyPy but rare; a paper giving the share of
code touched by a schema change (figure uncertain in the recording); Instagram's type
coverage effort (eight months, half the code base). A paper on library dependency changes
across 35 projects was judged irrelevant.

The section map, codes and queries below still reflect the propagation-cost framing and
need revising once the topic is reworded (A3). Likely additions: type checking in Python,
ORM type safety, mutation testing and fault seeding.

## Research questions

OPEN. Nothing to record until he names the topic, which is action A3. Do not fill this with
a plausible guess.

## Objectives

OPEN.

## Chapter 2 section map

Provisional, from the meeting.

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Refactoring and its open problems | The Google paper's eight problems; which ones this thesis takes |
| 2.2 | Schema evolution and code co-evolution | Changing a schema and the code that depends on it; ORM as the hard case |
| 2.3 | Dependency structure and propagation cost | DSM, propagation cost, clustering; how change impact is quantified |
| 2.4 | Evolvability and maintainability measurement | Measuring whether the next change got cheaper |
| 2.5 | Change impact analysis | Predicting what a change touches before making it |

## Topic codes

| Code | Meaning |
|---|---|
| `refac` | Refactoring, its open problems, automation |
| `schema` | Schema evolution, ORM, data model change |
| `dsm` | Dependency structure matrices, propagation cost |
| `evolve` | Evolvability and maintainability measurement |
| `impact` | Change impact analysis and effort estimation |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Impact | Predicts the reach of a change before it is made |
| Structure | Quantifies dependency structure rather than describing it |
| Schema | Concerns data model change and the code depending on it |
| Effort | Connects structural measures to actual work or time |

## Search queries

Tier 1, core:

```
search_semantic("change impact analysis database schema evolution code", year="2015-")
search_semantic("propagation cost design structure matrix architecture", year="2006-")
```

Tier 2, technical:

```
search_semantic("schema evolution object relational mapping co-evolution", year="2012-")
search_semantic("refactoring effort estimation prediction", year="2012-")
```

Tier 3, broad:

```
search_semantic("evolvability maintainability metrics empirical validation", year="2010-")
```

## Known foundational gaps

Everything, effectively. Nothing has been read beyond the one anchor paper.

| Sub-topic | Status |
|---|---|
| The anchor paper itself, with a citation | Described at the meeting, not in the repo. See A5 |
| Which of its eight problems this thesis takes | Not decided. See A4 |
| Propagation cost and DSM | First-year course material, to be revisited. See A1 |
| Whether propagation cost actually answers his planning question | Open, and the suggestion was explicitly given as possibly wrong |

## Note

The propagation cost framing was offered with the caveat that it may not fit. His question
is about planning effort; propagation cost is about structure. The connection is plausible
but has to be argued, not assumed. If he adopts it without objection, that is worth probing
rather than taking as agreement.

# Literature parameters — Alexander Isupov

Seeded from `_raw/tg.md`, his Google Doc of sources, and the 2026-09-28 meeting.

## Thesis

| Field | Value |
|---|---|
| Title | The effect of coding agents on architecture and maintainability in native iOS projects. Not final |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Research questions

| # | Question |
|---|---|
| RQ1 | Do coding agents degrade the architecture of an iOS project in ways that compilation and tests do not reveal? |
| RQ2 | Which architectural properties degrade first: component contracts, dependency structure, or layer boundaries? |
| RQ3 | What techniques keep agents from breaking architecture on projects large enough that the context window does not cover them? |

## Objectives

| # | Objective | Focus |
|---|---|---|
| O1 | Choose a measure of architectural damage that survives a green build | DSM, propagation cost, dependency clustering |
| O2 | Run agents on real iOS projects with a varied task pool | 3-5 projects, several runs per task |
| O3 | Establish what breaks, and whether any technique prevents it | Contracts between components are the expected failure point |

## Study design as agreed

Not thirty projects: three to five real ones of around 30k lines, each given a pool of
different tasks. Thirty experiments still result, from task variety rather than project
count. Runs per task must also vary, because agent output differs between runs.

## Chapter 2 section map

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Maintainability and its measurement | Metrics, quality models, what a green build does not tell you |
| 2.2 | Dependency structure analysis | DSM, propagation cost, clustering, architectural erosion |
| 2.3 | Agents and code modification | What agents do to existing codebases; refactoring by agent |
| 2.4 | Mobile architecture | iOS layering, component contracts, and UI-layer patterns |
| 2.5 | Context limits and large codebases | Why contracts break when the project exceeds the window |

## Topic codes

| Code | Meaning |
|---|---|
| `maint` | Maintainability metrics and quality models |
| `dsm` | Dependency structure matrices, propagation cost, erosion |
| `agent` | Coding agents modifying existing code |
| `ios` | iOS and mobile architecture, UI-layer patterns |
| `ctx` | Context window limits on large codebases |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Measurement | Gives an operational measure of architectural quality |
| Agents | Studies automated modification of existing code, not generation from scratch |
| Structure | Concerns dependencies and contracts rather than surface code quality |
| Mobile | Applies to iOS or at least to comparable app architectures |

## Search queries

Tier 1, core:

```
search_semantic("LLM agent refactoring architecture degradation maintainability", year="2023-")
search_semantic("design structure matrix propagation cost architecture", year="2006-")
```

Tier 2, technical:

```
search_semantic("architectural erosion drift detection metrics", year="2015-")
search_semantic("maintainability metrics empirical validation", year="2015-")
search_semantic("mobile application architecture patterns MVVM MVI empirical", year="2018-")
```

Tier 3, broad:

```
search_semantic("technical debt code smells measurement", year="2015-")
```

## Inclusion and exclusion

**Include:** operational metrics with reported validation; empirical studies of agents on
existing codebases; DSM and propagation cost foundations regardless of age.

**Exclude:** code-generation-from-scratch benchmarks; tool announcements without evaluation;
opinion pieces on architecture.

## Known foundational gaps

| Sub-topic | Status |
|---|---|
| A measure of architectural damage beyond compilation and tests | The open question. Dependency graph alone was judged insufficient |
| DSM, propagation cost, clustering | Named, not read. Likely no ready tooling for propagation cost |
| Agent refactoring in an iOS context specifically | He searched and found almost nothing; only a Yandex Habr article on Objective-C to Swift, not research |
| Whether 3-5 real projects share architectural techniques | Not checked |

## Note on scope

He is drawn to UI-layer patterns (MVVM, MVI, MVP) for professional reasons. As a measurement
target it is weak: those patterns are hard for an agent to break, since screens are
isolated. Component contracts are what break when the context window runs out. Keep the
reading pointed at contracts and dependency structure.

## Materials promised by the supervisor

Two papers on architecture and maintainability, plus his own material on DSM and
propagation cost. Tracked as A5.

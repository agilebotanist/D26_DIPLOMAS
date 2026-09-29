# Literature parameters — Mikhail Trifonov

Seeded from the 2026-09-28 meeting.

## Thesis

| Field | Value |
|---|---|
| Title | Sizing Java virtual thread pools against database connection pools: queueing theory against measurement. Not final |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## The contradiction

Virtual threads became cheap to create, so applications create many. Database connections
did not become cheap. Sources disagree on what follows: some advise enlarging the virtual
thread pool precisely because threads are cheap, others advise shrinking it so connections
are reused, and they derive their numbers from different formulas, Erlang among them.

That disagreement is the thesis's starting point, and it is what makes it falsifiable.

## Research questions

| # | Question |
|---|---|
| RQ1 | Under what conditions do the competing pool-sizing formulas hold, and are those conditions met by a Java application talking to a database over virtual threads? |
| RQ2 | How do the formulas' predictions compare with measured behaviour on a real stand? |
| RQ3 | Does queueing theory offer properties that improve pool organisation beyond what standard tuning practice already does? |

## Objectives

| # | Objective | Focus |
|---|---|---|
| O1 | Establish the applicability conditions of each competing formula | Arrival process, service distribution, stochastic assumptions |
| O2 | Measure the real system under load | A stand, varying both pool sizes |
| O3 | Compare predictions with measurement, and both with standard pool tuning | A baseline is needed, not only formulas |

## Chapter 2 section map

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Queueing theory foundations | Kendall notation, the standard models, and the conditions under which each holds |
| 2.2 | Pool sizing in practice | Connection pools, thread pools, the formulas practitioners actually use |
| 2.3 | Virtual threads and Project Loom | What changed, and why the old sizing advice may not transfer |
| 2.4 | Performance modelling tools | JMT and similar; simulation against analytic models |
| 2.5 | Capacity planning and measurement | How to run a load experiment that supports a claim |

## Topic codes

| Code | Meaning |
|---|---|
| `queue` | Queueing theory, Kendall notation, analytic models |
| `pool` | Thread and connection pool sizing |
| `loom` | Virtual threads, Project Loom, JVM concurrency |
| `model` | Performance modelling, simulation, JMT |
| `cap` | Capacity planning, load measurement, benchmarking method |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Theory | States a model with its applicability conditions, not just a formula |
| Pools | Concerns sizing of thread or connection pools specifically |
| Virtual threads | Accounts for cheap-to-create threads |
| Measurement | Validates predictions against a measured system |

## Search queries

Tier 1, core:

```
search_semantic("virtual threads Project Loom database connection pool sizing", year="2022-")
search_semantic("thread pool sizing queueing model performance", year="2010-")
```

Tier 2, technical:

```
search_semantic("connection pool performance database throughput saturation", year="2015-")
search_semantic("queueing network model microservice resource pool", year="2015-")
```

Tier 3, broad:

```
search_semantic("capacity planning software performance model validation", year="2005-")
```

Older work is in scope: queueing theory predates the problem by decades and the
foundational results are still the ones being applied.

## Inclusion and exclusion

**Include:** states its model assumptions; empirical work that reports the load generator
and the measured quantity; classic queueing texts.

**Exclude:** blog-level tuning advice with no derivation, except as evidence of the
contradiction itself, which is a legitimate use here and should be catalogued separately.

## Known foundational gaps

| Sub-topic | Status |
|---|---|
| Kendall notation and formula applicability conditions | Not started. The main risk to the whole thesis |
| The contradicting sources themselves, with the conditions each assumed | Found informally, not catalogued |
| JMT (Java Modelling Tools) | Mentioned, not tried |
| What exactly the stand measures: throughput, latency or connection utilisation | Not decided |
| Whether the problem is already solved for microservices and other resource pools | Not checked |

## Materials promised by the supervisor

Lecture notes from the master's course and workshop, links, and books on queueing theory
and capacity planning, including a textbook of 500-plus pages. Titles came through the
transcript badly and need confirming when they arrive. Tracked as A6.

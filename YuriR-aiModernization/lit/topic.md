# Literature parameters — Yuri Rudenko

Everything the lit-review pipeline needs that is specific to this thesis. The skill reads
this file before doing anything. Placeholders left unfilled block the pipeline.

## Thesis

| Field | Value |
|---|---|
| Title | Not yet formulated. Working direction: modernising a chaotic AI-generated codebase into a maintainable one with AI agents and spec-driven development |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Research questions

Open. Not to be filled until agreed with the student. Candidate areas, not commitments:

| # | Question |
|---|---|
| RQ1 | open: how architecture-driven modernization (ADM) maps onto agent-assisted, spec-driven work |
| RQ2 | open: what the metric history over 257 commits shows, and why SonarQube ratings never moved |
| RQ3 | open: what a pre-registered protocol for the Nov–Dec 2026 core rewrite with a Claude agent team can establish |

## Objectives

| # | Objective | Focus |
|---|---|---|
| O1 | open | |

## Chapter 2 section map

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Software modernization and architecture-driven modernization (OMG ADM, KDM) | What counts as modernization, how it is evaluated |
| 2.2 | Spec-driven development and AI coding agents | What SDD is, evidence on agent-written code quality |
| 2.3 | Technical debt and maintainability measurement | Static analysers, SonarQube ratings and their known limits |
| 2.4 | Case study and single-case methodology in software engineering | Validity of n = 1, prospective protocols |

## Topic codes

| Code | Meaning |
|---|---|
| `adm` | Architecture-driven modernization, legacy modernization |
| `sdd` | Spec-driven development, agents writing code from specifications |
| `td` | Technical debt, maintainability metrics, static analysis |
| `case` | Case study methodology |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Modernization | Studies transforming an existing system, not greenfield |
| Agents | AI agents or LLMs doing the code changes |
| Measurement | Quantitative maintainability evidence over a code history |
| Method | A case-study or protocol design reusable for n = 1 |

## Search queries

Tier 1, core:

```
search_semantic("AI-assisted legacy modernization case study", year="2022-")
search_semantic("spec-driven development LLM agents", year="2024-")
```

Tier 2, technical:

```
search_semantic("architecture-driven modernization knowledge discovery metamodel", year="2010-")
search_semantic("SonarQube technical debt rating validity", year="2018-")
```

Tier 3, broad:

```
search_semantic("case study research software engineering guidelines", year="2009-")
```

## Inclusion and exclusion

**Include:** published 2018 or later, except seminal works (OMG ADM, Runeson and Höst);
peer-reviewed or a preprint with citations; addresses the topic directly; has a reproducible
method or empirical evidence.

**Exclude:** non-English; no method section; superseded by a newer version from the same
authors; vendor whitepapers.

## Known foundational gaps

| Sub-topic | Expected work | Status |
|---|---|---|
| ADM | OMG ADM / KDM specification and its surveys | need |
| Case study method | Runeson and Höst, Guidelines for conducting and reporting case study research | need |
| SDD | TBD | need |

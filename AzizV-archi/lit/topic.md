# Literature parameters — Aziz Vundirov

Read out of `_raw/Aziz Vundirov Thesis Proposal.md` and the 2026-10-02 meeting. His own
document is the fuller source; this file holds what the lit pipeline needs.

## Thesis

| Field | Value |
|---|---|
| Title | The effect of architectural representation on LLM accuracy in detecting clean architecture violations in Java projects. Not final |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Domain

Effective use of AI in detecting violations of clean architecture principles. Architecture
quality strongly affects system quality, which is what makes the area worth a thesis.

What counts as architecture, as drawn at the meeting: modularity, layers, decomposition,
and how modules talk to each other. Class-level decomposition alone does not count, and an
interaction mechanism such as push-pull is not architecture.

## Research questions

His four. Four is likely too many for one thesis; RQ4 is the first candidate to drop.

| # | Question |
|---|---|
| RQ1 | Can an LLM, given a representation of Java code (diff, dependency graph, UML diagram), detect clean architecture violations with accuracy comparable to ArchUnit as a baseline on structural violations? |
| RQ2 | Which violation types does the LLM detect better or worse, and does that distribution change with the input representation? |
| RQ3 | Which representation gives the best F1: plain dependency graph, Mermaid, or PlantUML? |
| RQ4 | Does combining representations (diff plus diagram) beat each one alone? |

## Hypotheses

Three, in his document, and flagged by him as model-generated. They need restating in his
own words before they can be defended.

1. A static analyser for deterministic dependency extraction, combined with an LLM
   constrained by an evidence-based rubric and a JSON contract, achieves high recall at
   precision above 90 percent, beating isolated prompting on recall and unstructured agents
   on precision.
2. A rubric-driven LLM audit beats ArchUnit on semantic violations (business logic leakage,
   SRP breaches, mixed responsibility), while ArchUnit stays better on purely formal import
   constraints.
3. A declarative rubric reduces the maintenance effort of architectural control as the
   system evolves, compared with ArchUnit test code, without losing auditability.

Hypothesis 2 is the strongest: it predicts a split rather than a win, and it is falsifiable.

## Why LLMs rather than existing tools

From his document, and this is the part that has to hold up:

- ArchUnit and similar analyse the AST and bytecode for forbidden package dependencies.
  Their architectural tests must be written and updated by hand at every refactoring, which
  is real maintenance debt.
- They check syntax, not meaning. A domain service containing HTML email formatting does
  not breach any import rule, so an SRP violation passes unnoticed.
- LLM answers are also simply more readable, being in natural language.

## Chapter 2 section map

Follows the structure dictated at the meeting.

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Clean architecture: definitions and conformance | What it is, how conformance is assessed, which violation types are named in the literature |
| 2.2 | Static architecture checking tools | ArchUnit, SonarQube, ArchUnitTS: how they work and where they stop |
| 2.3 | LLMs applied to architecture | What has been tried, with what validation |
| 2.4 | Code representations for LLM input | Diff, dependency graph, Mermaid, PlantUML, UML; context limits |
| 2.5 | Evaluation of violation detection | Baselines, ground truth, precision and recall on architectural defects |

## Topic codes

| Code | Meaning |
|---|---|
| `clean` | Clean architecture, conformance, violation taxonomies |
| `archtool` | ArchUnit and other static architecture checkers |
| `llmarch` | LLMs applied to architecture analysis |
| `repr` | Code and architecture representations as model input |
| `eval` | Evaluation, baselines, ground truth |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Architecture | Concerns architecture, not class-level code quality |
| Detection | Detects violations against a stated ground truth |
| Representation | Varies the input representation and measures the effect |
| Baseline | Compares against a deterministic tool rather than against nothing |

## Search queries

Tier 1, core:

```
search_semantic("LLM architectural violation detection clean architecture", year="2023-")
search_semantic("architecture conformance checking automated", year="2015-")
```

Tier 2, technical:

```
search_semantic("ArchUnit architecture test static analysis Java", year="2018-")
search_semantic("UML diagram as input large language model code analysis", year="2023-")
search_semantic("architectural decision violation detection", year="2020-")
```

Tier 3, broad:

```
search_semantic("architecture erosion drift detection", year="2015-")
search_semantic("single responsibility principle detection code smell", year="2015-")
```

## Inclusion and exclusion

**Include:** peer-reviewed work on architecture conformance, violation detection, or LLMs
applied to either; tool papers with evaluation.

**Exclude, as a basis:** Habr and similar. No result validation, not peer reviewed. Usable
for definitions, problem statements and hypotheses, which must then be confirmed against
scientific sources, but the review cannot rest on them.

## Known foundational gaps

| Sub-topic | Status |
|---|---|
| Violation taxonomy: which types are being detected at all | Referenced to his Google Doc, not yet consolidated here |
| How conformance to clean architecture is assessed in the literature | Step 1 of the required structure; not covered |
| Ground truth: where labelled architectural violations come from | Not addressed. This decides whether the experiment is possible |
| Whether four representations can realistically be compared in one thesis | Scope question, unresolved |

## Note on sources

NotebookLM deep search is usable but invents references, so everything it returns has to be
checked. Google Scholar by relevance and citation count is the primary route.

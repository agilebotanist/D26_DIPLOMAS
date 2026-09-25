# Literature parameters — Elizaveta Zagurskikh

Read out of `_raw/Диплом.md` and the 2026-09-25 meeting. Her own document is far more
detailed than this file; what is here is the part the lit pipeline needs.

## Thesis

| Field | Value |
|---|---|
| Title | Cross-artifact traceability and consistency analysis for business and systems analysis artifacts, using LLMs. Not final |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Problem and gap

In complex information systems, particularly banking, the analytical artifacts produced at
different lifecycle stages drift out of alignment. Automated checking that consistency is
preserved between linked models is the under-researched part.

The meeting of 2026-09-25 sharpened this. The point is not defect detection on its own but
traceability as a guardrail: an LLM working across linked artifacts forgets and invents, and
in a banking system that is a regulatory exposure, not an inconvenience. A compact master
(table, graph or model) holds the traceability, everything else is generated from it, and
the LLM is made to check against it.

## Research question

Her formulation: how can links between business and systems analysis artifacts be recovered
automatically, and consistency violations between them detected, using LLMs.

To be rewritten around the guardrail framing.

## Artifact layers

| Level | Artifacts |
|---|---|
| Business analysis | Business requirements, BPMN process model |
| Systems analysis | Functional requirements, system requirements, UML use case diagram |

Sequence: Business Requirements → BPMN → Use Cases → Functional Requirements → System
Requirements. Not strict: BPMN, UC and FR have feedback edges. Traceability is stored as a
graph, and matrices are views over it.

## Relation types

Her taxonomy, eight types: derivation, refinement, satisfaction, constraint,
correspondence, dependency, conflict, and a weak generic trace. Each link is core (required
for every applicable element), selective (useful but substitutable by an existing trace
path), or conditional (mandatory only under a defined semantic condition).

The layer-to-layer matrix is in `_raw/Диплом.md`. It was the one thing the supervisor asked
her to keep unchanged: it illustrates the problem better than anything else she has.

## Chapter 2 section map

Her bibliography already follows this shape, which is why it maps cleanly.

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Traceability foundations and scope | What traceability is, pre- vs post-requirements, forward and backward, normative definitions |
| 2.2 | Semantics and representation of trace links | Relation type taxonomies, layered traceability, graph representation and querying |
| 2.3 | Traceability recovery | Automated link recovery, semantic gap between artifact levels, LLM-based extraction |
| 2.4 | Cross-artifact alignment and consistency | Alignment between business requirements, processes and systems; what is checked and how |
| 2.5 | Business analysis and enterprise architecture | Domain grounding: BA practice, TOGAF and layered architecture frameworks |
| 2.6 | Evaluation of traceability and consistency methods | Datasets, ground truth construction, inter-rater agreement, metrics |

Sections 2.5 and 2.6 come from the meeting. The supervisor asked her to ground herself in
the domain first, and noted her layering maps onto enterprise architecture.

## Topic codes

| Code | Meaning |
|---|---|
| `trace` | Traceability foundations, relation semantics, recovery |
| `align` | Cross-artifact alignment and consistency checking |
| `ba` | Business analysis practice, standards, enterprise architecture |
| `llm` | LLM and NLP application to requirements and traceability |
| `eval` | Datasets, ground truth, agreement measures, metrics |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Traceability | Defines or recovers typed links between artifact levels |
| Cross-level | Spans more than one representation level, not one artifact pair |
| Consistency | Checks meaning is preserved across a link, not just that a link exists |
| Method | Gives a reusable evaluation design or a validated benchmark |

## Search queries

Tier 1, core:

```
search_semantic("requirements traceability recovery across artifact levels LLM", year="2022-")
search_semantic("consistency checking business process model requirements alignment", year="2018-")
```

Tier 2, technical:

```
search_semantic("trace link relation types semantics requirements models", year="2010-")
search_semantic("BPMN requirements traceability consistency", year="2015-")
search_semantic("zero-shot NER classification requirements linking", year="2022-")
```

Tier 3, broad:

```
search_semantic("enterprise architecture layered traceability TOGAF", year="2012-")
search_semantic("inter-rater agreement ground truth software engineering dataset", year="2015-")
```

## Inclusion and exclusion

**Include:** peer-reviewed or a standard; addresses traceability, alignment or consistency
between distinct artifact levels; empirical or formally grounded. Older work is in scope
here: the trace-relation semantics literature is largely pre-2015 and still authoritative.

**Exclude:** single artifact pair with no cross-level claim; tool papers without evaluation;
non-English.

## Known foundational gaps

Holes she marked in her own document, and which matter more than four more banking cases:

| Sub-topic | Status |
|---|---|
| The consistency model itself | Section empty in her document |
| Taxonomy of traceability defects | Empty list |
| Taxonomy of consistency defects | Empty list |
| Unified semantic representation | Section empty |
| Metrics for stage 1 (recovery) and stage 2 (consistency) | Both lists empty; only Precision/Recall/F1 named so far, plus a note to add localization accuracy and a baseline |
| Business analysis and enterprise architecture grounding | Not started; the supervisor's first assignment |
| Fast NLP classifiers as an alternative to LLM reasoning for link recovery | Raised at the meeting, nothing read yet |

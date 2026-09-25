# Paper inventory — Elizaveta Zagurskikh

Read out of the Литература section of `_raw/Диплом.md`, which is already an annotated
bibliography organised by the sections she needs.

Updated: 2026-09-25

**Not yet MCP-verified.** The paper search server was unreachable when this was compiled,
so nothing here has gone into `references.bib` yet. Metadata below is as she recorded it.
Verify before citing: that rule exists because between them the other two students had
three wrong author attributions in lists that looked fine.

| # | Key (provisional) | Title | Section | PDF | Summary | BibTeX | Relevance |
|---|---|---|---|---|---|---|---|
| 1 | `iso29148` | ISO/IEC/IEEE 29148:2018, Requirements Engineering | 2.1 | no | annotated | no | HIGH — normative terminology for requirement and requirements management, and parent/child requirement as the basis for BR to FR dependencies |
| 2 | `iiba2025standard` | IIBA, The Business Analysis Standard | 2.1, 2.5 | link | annotated | no | HIGH — traceability from stakeholder need to implemented solution, forward and backward, bidirectional tracking through matrices |
| 3 | `prereq2023slr` | A systematic literature review of pre-requirements specification traceability | 2.1 | link | annotated | no | HIGH — splits pre-RS (source to requirement) from post-RS (requirement to code or model), which fixes which part of traceability she is in. DOI 10.1007/s00766-023-00412-z |
| 4 | `reqdocrelations` | Requirements document relations: a reuse perspective on traceability through standards | 2.2 | no | annotated | no | CRITICAL — ten trace relation types collected from earlier work, layered traceability, requirement graph analysis with Neo4j and Cypher for finding inconsistencies. DOI 10.1007/s10270-021-00958-y |
| 5 | `renartefact` | Requirements Engineering: Artefact-Based Customisation | 2.1 | link | annotated | no | MED — the forward and backward traceability definition she quotes |
| 6 | `tracesemantics2011` | Semantics of trace relations in requirements models for consistency checking and inferencing | 2.2 | no | annotated | no | HIGH — formal semantics for relations between requirements. She notes it is 2011 and things may have moved |
| 7 | `archtracellm` | Enabling Architecture Traceability by LLM-based Architecture Component Name Extraction | 2.3 | link | annotated | no | CRITICAL — the closest precedent: an LLM bridges the semantic gap between artifact levels via an intermediate model. Named in her original plan as the key resource |
| 8 | `alignmentslr2019` | Alignment between Business Requirement, Business Process, and Software System: a SLR | 2.4 | no | annotated | no | CRITICAL — exactly her three artifact types. Her note: existing work mostly links models via mapping, transformation and consistency rules. DOI 10.1155/2019/6918105 |
| 9 | `modelio_hal` | Generating BPMN in Modelio from a textual description via an LLM | 2.3 | link | annotated | no | MED — the Modelio route: text, LLM, intermediate BPMN, helper library, Modelio elements. hal-05702678 |

## Duplicate in her list

One work appears twice under slightly different titles with the same DOI,
10.1007/s10270-021-00958-y. It is one entry. The second copy carries the fuller annotation,
so keep that text and drop the first.

## Her relation taxonomy against the literature

Worth a look before she settles it. Her eight types (derivation, refinement, satisfaction,
constraint, correspondence, dependency, conflict, trace) overlap but do not coincide with
the ten in `reqdocrelations` (dependency, generalization/refinement, evolution,
satisfaction, overlap, conflicting, rationalization, contribution, validation,
verification). Her own note says no single terminology exists, so the divergence is
defensible, but it has to be argued rather than left implicit.

## Not yet covered

The meeting added two areas with nothing read yet:

| Area | Why |
|---|---|
| Business analysis and enterprise architecture, TOGAF and layered frameworks | The first assignment: ground yourself in the domain before hunting a gap. The supervisor also mentioned an old paper of his own on roughly this |
| Fast NLP classifiers for link recovery, as an alternative to LLM reasoning | Raised at the meeting, possibly GLiNER, to be confirmed |

## Sources she holds outside the repo

Her PDFs are in a Google Drive folder linked from `_raw/Диплом.md`. Pull the ones that
matter into `lit/pdfs/`, since a shared Drive link is not an archive.

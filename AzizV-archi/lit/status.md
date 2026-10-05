# Paper inventory — Aziz Vundirov

Read out of the Дневничок section of `_raw/Aziz Vundirov Thesis Proposal.md`.

Updated: 2026-10-05

At the 2026-10-02 meeting this list held three entries dated 5 September, none of them about
architecture. It now holds six. The growth happened in the three days after that meeting.

| # | Key (provisional) | Title | Section | PDF | Summary | BibTeX | Relevance |
|---|---|---|---|---|---|---|---|
| 1 | `llmlayered` | Integration of Large Language Models in Layered Software Systems: A Clean Architecture and CQRS Case Study | 2.3 | no | annotated | no | HIGH — his note: one good prompt is not enough for the model to answer well |
| 2 | `evidencebased` | An Evidence-Based LLM Framework for Expert-Validated Clean Architecture Conformance Assessment in Enterprise Software Systems | 2.1, 2.3 | no | annotated | no | CRITICAL — the closest precedent. Constrain the model with rules, axioms and a knowledge base and the findings are all real, but there is no knowledge of whether all violations were found. That unknown is his candidate research gap |
| 3 | `jimenez2023swebench` | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | 2.4 | no | annotated | yes | MED — supports his point that answers degrade as the fed context grows |
| 4 | `constraintdecay` | Constraint Decay: The Fragility of LLM Agents in Backend Code Generation | 2.3, 2.4 | no | annotated | no | HIGH — models write code badly under hard structural, functional and non-functional constraints and heavy frameworks |
| 5a | `archunit_antipatterns` | Automatic Assessment of Architectural Anti-patterns and Code Smells in Student Software Projects | 2.2 | no | annotated | no | HIGH — ArchUnit in practice |
| 5b | `archunit_security` | Extending ArchUnit to support validation of security architectural constraints | 2.2 | no | annotated | no | MED — how far ArchUnit can be pushed |
| 6 | `llmadr` | Evaluating Large Language Models for Detecting Architectural Decision Violations | 2.3 | no | annotated | no | CRITICAL — closest to RQ1; violation detection by LLM, evaluated |

## Verified

Only one so far. `jimenez2023swebench` confirmed against arXiv: Jimenez, Yang, Wettig, Yao,
Pei, Press, Narasimhan, arXiv:2310.06770, 2023, 2294 problems from 12 Python repositories.

The rest are recorded as he wrote them and have not been checked. Title search on arXiv
fails for recent papers, so these need a search by DOI or by author. Verify before any of
them goes into `references.bib`.

## What his document already establishes

Usable as written, and better than most first drafts at this stage:

**ArchUnit and similar static checkers** analyse the AST and bytecode for forbidden package
dependencies. Two limitations, both cited: architectural tests must be written and updated
by hand at every refactoring, which is maintenance debt; and they check syntax, not meaning,
so a domain service that formats HTML email breaches no import rule and its SRP violation
passes unnoticed.

**Why an LLM instead**: answers in natural language, and the cost of the model is lower than
the cost of maintaining architecture tests. The second claim is an assertion and needs a
source or a measurement.

## Gaps in the list

| Missing | Why it matters |
|---|---|
| Clean architecture itself: definitions and conformance assessment | Step 1 of the structure he was given. Nothing in the list covers it |
| A violation taxonomy | RQ2 asks which types are detected better. Without a taxonomy there is nothing to group by |
| Where labelled ground truth comes from | Decides whether the experiment can be run at all |
| Representation as a variable: diff, graph, Mermaid, PlantUML | RQ3 and RQ4 rest on this, and nothing in the list addresses it |

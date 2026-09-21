# Literature parameters — Danila Kochegarov

Seeded from the 2026-09-21 meeting. Sections marked OPEN are what the student has to settle
before the search can be narrowed.

## Thesis

| Field | Value |
|---|---|
| Title | Evaluating the contribution of agent harness components on small models (working) |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Hypothesis

On small models, the harness decides the outcome, not the model. Accepted 2026-09-21 as the
basis for both the thesis and a paper.

## Research questions

OPEN. The hypothesis is agreed; the questions that operationalise it are not.

| # | Question |
|---|---|
| RQ1 | Which harness components (MCP servers, skills, instructions) account for what share of task success on small models? |
| RQ2 | How should success be measured for multi-stage agent tasks where binary pass/fail does not apply? |

Draft only. Confirm with the student.

## Objectives

| # | Objective | Focus |
|---|---|---|
| O1 | Build a harness and sandbox that holds everything constant except the component under test | Own harness, fixed models, fixed task suite |
| O2 | Define a success metric that works for multi-stage tasks | Stepwise success rate, satisfied-requirements count, LLM-as-judge |
| O3 | Measure component contribution across a task suite, with full traces | Tool calls, tokens, tool errors, success rate |

## Chapter 2 section map

Draft, to be confirmed once the scope narrows.

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Agent harnesses and their customisation surface | What a harness is, what MCP, skills and instructions do |
| 2.2 | Benchmarks for coding and general agent tasks | What exists, what they measure, what they hold constant |
| 2.3 | Evaluation metrics for agent tasks | Binary vs stepwise success, requirement satisfaction, LLM-as-judge and its validity |
| 2.4 | Tracing and observability of agent runs | Span collection, tool-call and token accounting, error taxonomies |
| 2.5 | Small models under constraint | Context window limits and what they mean for instruction and skill budgets |

## Topic codes

| Code | Meaning |
|---|---|
| `harn` | Harness architecture, components, customisation |
| `bench` | Benchmarks and task suites |
| `metric` | Success metrics, LLM-as-judge, evaluation validity |
| `trace` | Tracing, spans, observability, cost accounting |
| `small` | Small and local models, context limits |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Harness | Treats the harness, not the model, as the unit of study |
| Benchmark | Provides a reusable task suite with stated conditions |
| Metric | Defines or validates a success measure for multi-stage tasks |
| Small models | Reports results on models small enough to run locally |

## Search queries

Tier 1, core:

```
search_semantic("agent harness components evaluation tool use", year="2023-")
search_semantic("LLM agent scaffolding ablation task success", year="2023-")
```

Tier 2, technical:

```
search_semantic("coding agent benchmark multi-step task success rate", year="2023-")
search_semantic("LLM as judge evaluation validity agreement", year="2023-")
search_semantic("agent trace observability tool call metrics", year="2024-")
```

Tier 3, broad:

```
search_semantic("small language model tool use context window limits", year="2023-")
search_semantic("prompt and instruction ablation study language model", year="2022-")
```

## Inclusion and exclusion

**Include:** 2022 or later given how fast this area moves; peer-reviewed or a preprint with
citations; reports what was held constant across runs; states model versions.

**Exclude:** single-run evaluations with no variance; model comparisons that do not isolate
the scaffold; vendor benchmarks without a published method.

## Known foundational gaps

| Sub-topic | Expected work | Status |
|---|---|---|
| Harness component ablation | TBD, likely none, which is the opening | need |
| Multi-stage success metrics | TBD | need |
| Agent tracing conventions | TBD, industry practice more than papers | need |
| Skill evaluation tooling | Anthropic skill evals; Alibaba Skill Evaluator/Improver; OpenCode — mentioned in the meeting, not yet located | need |

## Non-paper sources

Named by the student on 2026-09-21 and worth locating even though they may be repos rather
than papers: Anthropic's evals-in-skills, Alibaba's Skill Evaluator or Skill Improver,
OpenCode's metric collection.

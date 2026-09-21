# Literature parameters — Danila Kochegarov

Seeded from the 2026-09-21 meeting and from the student's own proposal, `_raw/Harness
system with explainable and changing metrics (2).pdf`, sent the same day. Sections marked
OPEN are what the student has to settle before the search can be narrowed.

## Thesis

| Field | Value |
|---|---|
| Title | Evaluating the Impact of Agent Harness Components on the Reliability and Efficiency of LLM Agents (student's own title) |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Hypothesis

On small models, the harness decides the outcome, not the model. Accepted 2026-09-21 as the
basis for both the thesis and a paper.

## Subjects and components

| | |
|---|---|
| Harnesses under study | pi, opencode, hermes, openhands |
| Plus | His own harness in Go, for full control over the experiment, then compared against the open ones |
| Components varied | skills, tools, instructions, MCP, LSP |
| Held constant | sandbox, harness, models |
| Also planned | A web UI showing connected MCP/LSP/tools/skills/instructions, test-suite runs and metrics over time, so degradation after adding a component is visible |

The web UI and the self-improving-system ideas are the most likely place to lose the
October deadline. They are engineering, not evidence.

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
| Harness component ablation | "Статья 2" in his document, still uncited | need, see `download.md` |
| Agent evaluation protocols | "Статья 1" in his document, still uncited | need, see `download.md` |
| LLM-as-agent benchmarks | `liu2023agentbench` | have, BibTeX only |
| Multi-stage success metrics | TBD | need |
| Agent tracing conventions | TBD, industry practice more than papers | need |
| Skill evaluation tooling | Anthropic skill evals; Alibaba Skill Evaluator/Improver; OpenCode | need |

## Non-paper sources

Named by the student and worth locating even though they may be repos rather than papers:
Anthropic's evals-in-skills, Alibaba's Skill Evaluator or Skill Improver, OpenCode's metric
collection, and the four harnesses themselves (pi, opencode, hermes, openhands).

## Where his own reading stands

His document summarises three papers and cites none of them. One has been identified as
`liu2023agentbench` from the AgentBench repository link he included. The other two are
tracked as U1 and U2 in `status.md`. His own conclusion, that the topic is current because
every paper he found is from the last five years, does not yet rest on a citable list.

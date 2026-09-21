# Paper inventory — Danila Kochegarov

The single source of truth for what exists and how far it has been processed.

Updated: 2026-09-21

## Identified

| # | Key | Title | Section | PDF | Converted | Summary | BibTeX | Relevance |
|---|-----|-------|---------|-----|-----------|---------|--------|-----------|
| 1 | `liu2023agentbench` | AgentBench: Evaluating LLMs as Agents | 2.2, 2.5 | no | no | no | yes | HIGH — open models under 70B on real Code/Web/Game tasks, with released artifacts. Note: it studies the LLM as agent, not the harness, so it is a benchmark source and a contrast case, not a direct precedent |

## Described but not identified

Danila's document of 2026-09-21 summarises three papers without citing any of them. Two are
still unidentified. Until they have authors, a year and a venue, none of their findings can
be used in the thesis.

| # | Working name | What it reportedly does | Distinguishing details to search on |
|---|---|---|---|
| U1 | "Статья 1" | Proposes an evaluation protocol with fixed initial conditions: environment state, token budget, time limit, validator script, task statement. Adds a boolean security-bypass variable. Completion via task-specific deterministic validators or rubric-based judgment; Process scored from a reproducible trace | The failure-symptom taxonomy: output contract, tool interface errors, evidence base, missing committed artifacts, continuation state |
| U2 | "Статья 2" | Tasks ranked by difficulty and domain (SE, media and content production, office, natural science, cybersec); runs across harnesses with and without task-matched skills | Findings: AI-generated skills underperform human-curated ones; compact narrow skills beat multi-purpose ones; invocation frequency does not predict quality |

Both are in `download.md` as the first thing to resolve.

## Foundational references, BibTeX only

| # | Key | Title | Section | Notes |
|---|-----|-------|---------|-------|

<!--
Relevance is HIGH / MED / LOW followed by a reason and the RQ it serves.
Keys match references.bib exactly.
-->

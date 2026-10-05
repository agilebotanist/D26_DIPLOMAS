# Literature parameters — Darya Tolmeneva

Rewritten 2026-10-05 from her Obsidian vault (`_raw/Diploma/`). The earlier version, which
said no direction had been chosen, is superseded: the vault shows a direction and a frame.

## Thesis

| Field | Value |
|---|---|
| Title | Agentic code review: orchestration, boundaries with the human reviewer, and how to measure the agent's contribution. Not final |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

Registration on 2026-10-12 can be broad: code review, agents, effectiveness of review with
agents. Narrowing happens by May.

## The frame she found

Classic software inspection had an **inspection leader** who chose the documents, the
checklists, the rules, the participants and their roles, controlled the pace, and decided
when the inspection was finished. Modern lightweight review dropped that role.

Her question is whether an **orchestrator in an agentic system can be the modern inspection
leader**. That is a real frame, it is hers, and it turns a sprawl of ideas into one line of
enquiry. Nearly every strong note in the vault hangs off a specific clause of the Inspection
Manual:

| Inspection Manual | What she derived |
|---|---|
| HB4: removing defect causes matters more than fixing defects | Can AI review find the causes of recurring defects? |
| HB9: leader selects documents, checklists, rules, participants, roles | Can the orchestrator select checks and agent composition per review type? |
| HB11: reviewers may adjust pace to their role and situation | Can the orchestrator choose a model per check, by difficulty? |
| HB12, HB13: each reviewer should find unique serious problems | Unique findings per agent as a measure of that agent's contribution |
| HB16, HB17: exit criteria, follow-up, acceptable residual defects | What are the stopping criteria for agentic review? |

## Research questions

Not yet fixed. These are the candidates her own question notes already pose, in the order
they look defensible.

| # | Candidate | Note |
|---|---|---|
| RQ1 | Does giving an agent a checklist improve review quality over the same agent without one? | Agreed at the 2026-09-28 meeting as the first experiment |
| RQ2 | What does each agent role contribute uniquely, and does that contribution justify its cost? | Her own design: merge duplicates, then measure unique confirmed defects and overlap per agent |
| RQ3 | Where is the boundary between what an agent reviews and what a human must? How should the orchestrator make that boundary visible? | Her central question since 28 September |
| RQ4 | What are the stopping criteria for agentic review? | From HB16-HB17; distinguishes quality-based completion, waiting for a commit, and budget exhaustion |

RQ2 is the strongest candidate for the empirical core: it is measurable, it has a derivation
from the literature, and it answers a question a team would actually ask.

## Open questions in the vault

Thirteen, each sourced. Grouped here because the grouping is what she has to do next:

**Orchestration:** check and agent selection per review type; model choice per check;
orchestrator as inspection leader; stopping criteria; two levels of orchestration (managing
analysis, and managing the conversation).

**Boundaries and the human:** limits of AI review; preserving human interaction; preserving
knowledge exchange; what knowledge the system should retain.

**Measurement:** the system's goal and how we would know it was met; evaluation in hours;
whether AI lets a reviewer cover more code per hour without losing quality; what makes a
review comment useful.

**Causes:** can AI review find the causes of recurring defects.

Thirteen open questions is too many for one thesis, and that is the real work of the next
two weeks: pick the one that RQ2 serves, and park the rest as discussion.

## Chapter 2 section map

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | Code review and inspection: what the practice is | Fagan and formal inspection, roles, the inspection leader, exit criteria; why modern review dropped them |
| 2.2 | Review as conversation | Communication, mentoring, knowledge exchange as functions of review, not side effects |
| 2.3 | Agentic and multi-agent review systems | RepoReviewer, SWE-Review, orchestration architectures |
| 2.4 | Automated review in practice | Industrial evidence: what is resolved, what it costs in time |
| 2.5 | Effects on developer behaviour | Over-trust, reduced attention, the shifting bottleneck to seniors |
| 2.6 | Measuring review | External vs internal metrics, inspection rate, defect rate, defect density, defect seeding, residual defect estimation |

## Topic codes

| Code | Meaning |
|---|---|
| `insp` | Inspection, formal review process, roles, checklists |
| `agent` | Agentic and multi-agent review systems |
| `prac` | Automated review in industrial practice |
| `human` | Human factors: trust, attention, knowledge exchange, mentoring |
| `metric` | Review metrics and evaluation method |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Process | Says something about how review is organised, not just what a tool found |
| Agentic | Concerns agents or multi-agent systems doing review |
| Evidence | Reports measured outcomes from real pull requests or real teams |
| Measurement | Defines or validates a metric for review effectiveness |

## Search queries

Tier 1, core:

```
search_semantic("multi-agent LLM code review orchestration", year="2023-")
search_semantic("checklist effect code review defect detection", year="2000-")
```

Tier 2, technical:

```
search_semantic("software inspection exit criteria defect removal effectiveness", year="1990-")
search_semantic("defect seeding capture recapture residual defects inspection", year="1990-")
search_semantic("code review knowledge transfer mentoring empirical", year="2015-")
```

Tier 3, broad:

```
search_semantic("AI assistant developer behaviour trust automation bias", year="2020-")
```

Older work is in scope and necessary: the inspection literature is 1976 onwards and is
exactly what the thesis builds on.

## Inclusion and exclusion

**Include:** empirical studies of review, inspection literature of any age, agentic review
systems with evaluation, metric definitions with validation.

**Exclude:** tool announcements without evaluation; LLM review demos on single examples.

## Known foundational gaps

| Sub-topic | Status |
|---|---|
| Fagan inspection itself, and the 1970s originals | Named on 28 September, not yet in the vault |
| Defect seeding and residual defect estimation | Raised as an evaluation route, nothing read |
| Existing review checklists and agent instructions | Action A9, not started |
| The intern and junior role under agentic development | Action A11, not started |
| Real citations for the Inspection Manual and both Cohen items | They carry the most weight and have the least bibliographic grounding |

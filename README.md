# D26 — diploma cohort 2026-2027

Supervision workspace for the 2026-2027 diploma batch. One repo, shared workflows at the
root, one folder per student.

Private to the supervisor. `PROFILE.md` and `feedback/` hold candid notes. What goes to a
student is their meeting note and their action list.

## Board

| Student | Topic | Phase | Next milestone | Open | Last meeting |
|---|---|---|---|---|---|
| [AlexanderI-iosArch](AlexanderI-iosArch/) | Agents and the architecture of native iOS apps | Presented 2026-10-26 (prelim. 4/5): metric profile and A/B with rule set accepted; missing related work on agents and architecture, definition of done, task size | Related work (A8), DoD and leakage (A10); review due 2026-10-31 | 8 | 2026-10-26 |
| [AzizV-archi](AzizV-archi/) | Architectural representation and LLM detection of clean architecture violations | Direction chosen: runtime (dynamic) context of Spring apps vs static tools; no dataset or ground truth yet | Dynamic-evaluation literature and a known dataset of 30+ Java projects | 11 | 2026-10-12 |
| [DanilK-HarnessTesting](DanilK-HarnessTesting/) | Impact of agent harness components on LLM agent reliability | Presented 2026-10-26 (prelim. 4/5): components chosen (context compression, error-based instructions), Qwen3.5, scripts not judge; metrics are not numbers yet | Metrics as numbers (A5), 2026-10-31; two-experiment plan (A8) | 7 | 2026-10-26 |
| [DaryaT-ReviewAgents](DaryaT-ReviewAgents/) | Checklists for agentic code review of backend API changes | Presented 2026-10-26 (prelim. 5/5): best-prepared deck, 20 refs, experiment laid out; scope spans three sub-topics | Narrow to one line (A3), 2026-10-31; human-study design (A16) | 10 | 2026-10-26 |
| [ElizavetaZ-baTrace](ElizavetaZ-baTrace/) | Cross-artifact traceability and consistency for BA artifacts | Focus moved from traceability to consistency of linked artifacts; domain, datasets and link extraction unsettled; five actions overdue since 2026-10-09 | Narrow the domain and show related work (A8) | 9 | 2026-10-16 |
| [IlnarK](IlnarK/) | Python type checkers under domain-model changes in ORM projects, with an ORM-aware extension | Presented 2026-10-26 (prelim. 4/5, near 5): topic reworded and accepted, strong lit and design; how the approach works and the LLM role unclear | Explain approach (A8), re-check existing tools (A9), LLM role (A10) | 8 | 2026-10-26 |
| [IlyaLN-sastSLM](IlyaLN-sastSLM/) | Local CVE-trained models against and alongside SAST | Class chosen (IoT, C/C++); SAST plus LLM noise filter judged too thin, needs a durable-artifact contribution | Contribution beyond comparison (A3), at next meeting | 7 | 2026-10-16 |
| [MikhailT-qtJavaPools](MikhailT-qtJavaPools/) | Safety of virtual-thread migrations by AI agents in Java services | Topic switched from pools to migration safety and accepted; experiment must move from prompts to a deterministic migration tool, 30+ projects | Link agents with deterministic transformations (A7), term for "safety" (A8) | 4 | 2026-10-16 |
| [YuriR-aiModernization](YuriR-aiModernization/) | Modernising an AI-generated codebase with agents and SDD (working direction; frame: ADM + SDD) | New 2026-10-27: real case, 257-commit metric history, rewrite of core planned Nov–Dec; no RQ yet | First meeting; protocol before the rewrite starts | 0 | — |

**Topic registration: 2026-10-12.** It may be submitted broadly and narrowed later.

Cohort deadline, announced in the group: on 2026-10-26 (held; second session 2026-10-30 for Aziz, Mikhail, Elizaveta, Ilya-Lin) (confirmed at the 2026-10-19 meeting;
earlier given as end of October) every student presents briefly at a joint run-through. Each presentation says what problem is being solved, what
others have written about it, roughly what the solution is, and how the student rates the
usefulness of their own method. Around twenty papers read by then, roughly forty by the
defence. Results worth submitting to a conference by end of February 2027.

## Working here

| I want to | Run |
|---|---|
| Process a new transcript dropped in `meetings/raw/` | `/meeting` |
| See who owes what | `/actions` |
| Work on a student's literature | `/lit <student>` |
| Review a draft | `/review <file>` |
| Add a student | `/new-student <Name> <Topic>` |

Instructions live in [CLAUDE.md](CLAUDE.md), the meeting workflow in
[meetings/CLAUDE.md](meetings/CLAUDE.md), and the rest in `.claude/skills/`.

## Layout

```
meetings/          raw/ is the drop point; one folder per processed meeting
<Student>/         PROFILE, ACTIONS, meetings/, lit/, feedback/, work/, code/
templates/student/ skeleton for a new student
.claude/           skills and slash commands
work/              supervisor's own cross-cutting notes
```

## Why one repo

D25 gave every student their own repo. The literature workflow ended up copied six times
and drifting, every `todo.md` was empty, and in ten repos there was not one meeting record.
Nothing showed who owed what.

Here the workflow exists once, meetings drive the clock, and `ACTIONS.md` per student is
the thing that must never go stale. The full comparison is at the end of
[CLAUDE.md](CLAUDE.md).

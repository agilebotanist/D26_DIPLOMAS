# D26 — diploma cohort 2026-2027

Supervision workspace for the 2026-2027 diploma batch. One repo, shared workflows at the
root, one folder per student.

Private to the supervisor. `PROFILE.md` and `feedback/` hold candid notes. What goes to a
student is their meeting note and their action list.

## Board

| Student | Topic | Phase | Next milestone | Open | Last meeting |
|---|---|---|---|---|---|
| [AlexanderI-iosArch](AlexanderI-iosArch/) | Agents and the architecture of native iOS apps | Topic agreed; goal fixed on maintainability, but no usable measure yet (DSM, propagation cost, Sonar all insufficient) | Parameters for agent with vs without skill, then ~20 papers, 2026-10-31 | 5 | 2026-10-12 |
| [AzizV-archi](AzizV-archi/) | Architectural representation and LLM detection of clean architecture violations | Direction chosen: runtime (dynamic) context of Spring apps vs static tools; no dataset or ground truth yet | Dynamic-evaluation literature and a known dataset of 30+ Java projects | 11 | 2026-10-12 |
| [DanilK-HarnessTesting](DanilK-HarnessTesting/) | Impact of agent harness components on LLM agent reliability | Hypothesis challenged by a paper (gain peaks on mid-size models); DSL and self-improving harness set aside; first test on supervisor dataset | Name the articles (A7), narrow components (A4), 2026-10-31 | 6 | 2026-10-12 |
| [DaryaT-ReviewAgents](DaryaT-ReviewAgents/) | Code review automation | Vault in: strong frame (orchestrator as inspection leader), 13 open questions | Submit the topic, 2026-10-12 | 11 | 2026-10-05 |
| [ElizavetaZ-baTrace](ElizavetaZ-baTrace/) | Cross-artifact traceability and consistency for BA artifacts | Focus moved from traceability to consistency of linked artifacts; domain, datasets and link extraction unsettled; five actions overdue since 2026-10-09 | Narrow the domain and show related work (A8) | 9 | 2026-10-16 |
| [IlnarK](IlnarK/) | Static type checkers (MyPy, ty, Pyright) and the impact of domain model changes in ORM-based Python code | Moved from propagation cost to type checkers; contribution beyond comparison sketched (static plus agent blast radius, mutation-style fault seeding); wording not accepted; vault still not sent | Submit topic 2026-10-19, reworded topic at run-through 2026-10-26 | 6 | 2026-10-19 |
| [IlyaLN-sastSLM](IlyaLN-sastSLM/) | Local CVE-trained models against and alongside SAST | Class chosen (IoT, C/C++); SAST plus LLM noise filter judged too thin, needs a durable-artifact contribution | Contribution beyond comparison (A3), at next meeting | 7 | 2026-10-16 |
| [MikhailT-qtJavaPools](MikhailT-qtJavaPools/) | Safety of virtual-thread migrations by AI agents in Java services | Topic switched from pools to migration safety and accepted; experiment must move from prompts to a deterministic migration tool, 30+ projects | Link agents with deterministic transformations (A7), term for "safety" (A8) | 4 | 2026-10-16 |

**Topic registration: 2026-10-12.** It may be submitted broadly and narrowed later.

Cohort deadline, announced in the group: on 2026-10-26 (confirmed at the 2026-10-19 meeting;
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

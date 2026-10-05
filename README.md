# D26 — diploma cohort 2026-2027

Supervision workspace for the 2026-2027 diploma batch. One repo, shared workflows at the
root, one folder per student.

Private to the supervisor. `PROFILE.md` and `feedback/` hold candid notes. What goes to a
student is their meeting note and their action list.

## Board

| Student | Topic | Phase | Next milestone | Open | Last meeting |
|---|---|---|---|---|---|
| [AlexanderI-iosArch](AlexanderI-iosArch/) | Agents and the architecture of native iOS apps | Topic agreed; how to measure architectural damage is unsettled | ~20 papers and a draft, 2026-10-31 | 5 | 2026-09-28 |
| [AzizV-archi](AzizV-archi/) | Architectural representation and LLM detection of clean architecture violations | A month lost, then recovered fast; document rebuilt to the required structure | Lit search structure, 2026-10-09 | 4 | 2026-10-02 |
| [DanilK-HarnessTesting](DanilK-HarnessTesting/) | Impact of agent harness components on LLM agent reliability | Hypothesis accepted, proposal in, scope too broad | Draft lit review and topic, 2026-10-31 | 6 | 2026-09-21 |
| [DaryaT-ReviewAgents](DaryaT-ReviewAgents/) | Code review automation | Foundation done; first experiment is checklists | Submit the topic, 2026-10-12 | 9 | 2026-10-05 |
| [ElizavetaZ-baTrace](ElizavetaZ-baTrace/) | Cross-artifact traceability and consistency for BA artifacts | Furthest along; reframed around traceability as guardrail, validation plan parked | Domain sprint 2026-10-09 | 6 | 2026-09-25 |
| [IlnarK](IlnarK/) | Cost of a schema change via propagation cost | Topic not yet named; folder empty | Name the topic, 2026-10-12 | 6 | 2026-10-05 |
| [IlyaLN-sastSLM](IlyaLN-sastSLM/) | Local CVE-trained models against and alongside SAST | Best-organised intake; needs a contribution beyond comparison | Vulnerability class and the step beyond comparison, 2026-10-12 | 5 | 2026-09-28 |
| [MikhailT-qtJavaPools](MikhailT-qtJavaPools/) | Java virtual thread pools against DB connection pools | Topic switched and accepted; queueing-theory applicability is the risk | Queueing theory, 2026-10-12 | 6 | 2026-09-28 |

**Topic registration: 2026-10-12.** It may be submitted broadly and narrowed later.

Cohort deadline, announced in the group: by end of October 2026 every student presents
briefly at a joint run-through. Each presentation says what problem is being solved, what
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

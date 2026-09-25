# D26 — diploma cohort 2026-2027

Supervision workspace for the 2026-2027 diploma batch. One repo, shared workflows at the
root, one folder per student.

Private to the supervisor. `PROFILE.md` and `feedback/` hold candid notes. What goes to a
student is their meeting note and their action list.

## Board

| Student | Topic | Phase | Next milestone | Open | Last meeting |
|---|---|---|---|---|---|
| [DanilK-HarnessTesting](DanilK-HarnessTesting/) | Impact of agent harness components on LLM agent reliability | Hypothesis accepted, proposal in, scope too broad | Draft lit review and topic, 2026-10-31 | 6 | 2026-09-21 |
| [DaryaT-ReviewAgents](DaryaT-ReviewAgents/) | Code review automation, direction not chosen | Initial idea rejected; 7 verified references already in hand | Draft lit review and topic, 2026-10-31 | 4 | 2026-09-21 |
| [ElizavetaZ-baTrace](ElizavetaZ-baTrace/) | Cross-artifact traceability and consistency for BA artifacts | Furthest along; reframed around traceability as guardrail, validation plan parked | Domain sprint 2026-10-09, then draft 2026-10-31 | 6 | 2026-09-25 |

Cohort deadline, announced in the group: a draft literature review and the topic by end of
October 2026. It should say what problem is being solved, the domain and its definitions,
roughly what the solution is, a couple of papers that point at that solution, and how the
results will be validated. Results worth submitting to a conference by end of February 2027.

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

# D26 — diploma cohort 2026-2027

Supervision workspace for the 2026-2027 diploma batch. One repo, shared workflows at the
root, one folder per student.

Private to the supervisor. `PROFILE.md` and `feedback/` hold candid notes. What goes to a
student is their meeting note and their action list.

## Board

| Student | Topic | Phase | Next milestone | Open | Last meeting |
|---|---|---|---|---|---|
| [AlexanderI-iosArch](AlexanderI-iosArch/) | Agents and the architecture of native iOS apps | Presented 2026-10-26 (prelim. 4/5): metric profile and A/B with rule set accepted; missing related work on agents and architecture, definition of done, task size | Related work (A8), DoD and leakage (A10); review due 2026-10-31 | 8 | 2026-10-26 |
| [AzizV-archi](AzizV-archi/) | Detecting Clean Architecture violations in Java Spring with LLMs and dynamic context (Jasmine) | Presented 2026-10-30 (prelim. 4/5): gap found (CA05, static-only LLM pipelines); dynamic context unexplained, no ground truth or dataset yet | Ground truth and dataset (A11, A13); explain dynamic context (A14) | 10 | 2026-10-30 |
| [DanilK-HarnessTesting](DanilK-HarnessTesting/) | Impact of agent harness components on LLM agent reliability | Presented 2026-10-26 (prelim. 4/5): components chosen (context compression, error-based instructions), Qwen3.5, scripts not judge; metrics are not numbers yet | Metrics as numbers (A5), 2026-10-31; two-experiment plan (A8) | 7 | 2026-10-26 |
| [DaryaT-ReviewAgents](DaryaT-ReviewAgents/) | Checklists for agentic code review of backend API changes | Presented 2026-10-26 (prelim. 5/5): best-prepared deck, 20 refs, experiment laid out; scope spans three sub-topics | Narrow to one line (A3), 2026-10-31; human-study design (A16) | 10 | 2026-10-26 |
| [ElizavetaZ-baTrace](ElizavetaZ-baTrace/) | Semantic consistency of FR, UC and BPMN with LLMs | Presented 2026-10-30 (prelim. 3/5): RQs, taxonomy and B0/B1/B2 design, but no use case, no data, trace links and ground truth unsettled | Concrete use case (A11), trace links and ground truth (A13) | 8 | 2026-10-30 |
| [IlnarK](IlnarK/) | Python type checkers under domain-model changes in ORM projects, with an ORM-aware extension | Presented 2026-10-26 (prelim. 4/5, near 5): topic reworded and accepted, strong lit and design; how the approach works and the LLM role unclear | Explain approach (A8), re-check existing tools (A9), LLM role (A10) | 8 | 2026-10-26 |
| [IlyaLN-sastSLM](IlyaLN-sastSLM/) | Local CVE-trained models with SAST in embedded C/C++, persistent artifacts in CI | Presented 2026-10-30 (prelim. 4/5): contribution beyond comparison found (AVR); scope sprawls, comparison unclear, corpus small | One line, list halved (A9); prompt engineering (A10); ground truth (A11) | 8 | 2026-10-30 |
| [MikhailT-qtJavaPools](MikhailT-qtJavaPools/) | Robust migration of Java services to virtual threads by agents with deterministic transformations | Presented 2026-10-30 (prelim. 5/5): best of round 2; vtmigrate + vtcheck, load as verdict; four RQs too many | Cut to two RQs (A9); dataset (A10); iterative migration (A11) | 5 | 2026-10-30 |
| [YuriR-aiModernization](YuriR-aiModernization/) | Modernising an AI-generated codebase with agents and SDD (working direction; frame: ADM + SDD) | Presented 2026-10-30 (prelim. 2/5, started a month late): strong case, but no focus, no quality criterion, ~8 papers | Choose focus (A1), quality criterion (A2), literature (A3) | 7 | 2026-10-30 |

**Topic registration: 2026-10-12.** It may be submitted broadly and narrowed later.

Cohort deadline, announced in the group: on 2026-10-26 (held; second session held 2026-10-30; next joint run-through mid to late December 2026) (confirmed at the 2026-10-19 meeting;
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

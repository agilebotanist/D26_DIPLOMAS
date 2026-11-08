# D26 — diploma cohort 2026-2027

Supervision workspace for the 2026-2027 diploma batch. One repo, shared workflows at the
root, one folder per student.

Private to the supervisor. `PROFILE.md` and `feedback/` hold candid notes. What goes to a
student is their meeting note and their action list.

## Board

| Student | Topic | Phase | Next milestone | Open | Last meeting |
|---|---|---|---|---|---|
| [AlexanderI-iosArch](AlexanderI-iosArch/) | Agents and the architecture of native iOS apps | Presented 2026-10-26 (prelim. 4/5); 2026-11-02: plan to build the metrics collector, no justified thresholds or weights yet, mutation testing for Swift needed | Metrics tool and one end-to-end run before December (A12, A13); thresholds and weights from literature (A14) | 13 | 2026-11-02 |
| [AzizV-archi](AzizV-archi/) | Detecting Clean Architecture violations in Java Spring with LLMs and dynamic context (Jasmine) | Presented 2026-10-30 (prelim. 4/5): gap found (CA05, static-only LLM pipelines); 2026-11-06: design accepted, unit of analysis (vertical module) and dataset size still to define, synthetic mutations need a realism argument | Define "module" (A18); dataset (A13) and ground truth (A11) | 11 | 2026-11-06 |
| [DanilK-HarnessTesting](DanilK-HarnessTesting/) | Impact of agent harness components on LLM agent reliability | Presented 2026-10-26 (prelim. 4/5): components chosen (context compression, error-based instructions), Qwen3.5, scripts not judge; metrics are not numbers yet | Metrics as numbers (A5), 2026-10-31; two-experiment plan (A8) | 7 | 2026-10-26 |
| [DaryaT-ReviewAgents](DaryaT-ReviewAgents/) | Checklists for agentic code review of backend API changes | Presented 2026-10-26 (prelim. 5/5): best-prepared deck, 20 refs. Notes of 2026-11-06 narrow the topic to checklist content and whole vs step execution for backend API review (human study, checklist support, context comparison deferred); all October note fixes done (66 notes, 30 questions, 22 papers); risk: no confirmed API slice in any candidate dataset, dataset survey unverified | Accept or narrow the focus (A3, АС); API examples in ReviewBench and AACR-Bench, public dataset (A17); is the topic submitted (A8) | 6 | 2026-11-06 |
| [ElizavetaZ-baTrace](ElizavetaZ-baTrace/) | Semantic consistency of FR, UC and BPMN with LLMs | Presented 2026-10-30 (prelim. 3/5): RQs, taxonomy and B0/B1/B2 design, but no use case, no data, trace links and ground truth unsettled | Concrete use case (A11), trace links and ground truth (A13) | 8 | 2026-10-30 |
| [IlnarK](IlnarK/) | Python type checkers under domain-model changes in ORM projects, with an ORM-aware extension | Presented 2026-10-26 (prelim. 4/5, near 5): topic reworded and accepted, strong lit and design; how the approach works and the LLM role unclear | Explain approach (A8), re-check existing tools (A9), LLM role (A10) | 8 | 2026-10-26 |
| [IlyaLN-sastSLM](IlyaLN-sastSLM/) | Local CVE-trained models with SAST in embedded C/C++, persistent artifacts in CI | Presented 2026-10-30 (prelim. 4/5): contribution beyond comparison found (AVR); scope sprawls, comparison unclear, corpus small | One line, list halved (A9); prompt engineering (A10); ground truth (A11) | 8 | 2026-10-30 |
| [MikhailT-qtJavaPools](MikhailT-qtJavaPools/) | Robust migration of Java services to virtual threads by agents with deterministic transformations | Presented 2026-10-30 (prelim. 5/5): best of round 2; 2026-11-06: doubt that a deterministic tool always wins resolved, framing is LLM alone vs LLM with the tool; self-improving rule set deferred to future work | Comparison framing and survey of migration tools (A13); cut to two RQs (A9); dataset (A10) | 6 | 2026-11-06 |
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

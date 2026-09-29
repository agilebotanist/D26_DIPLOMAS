# Literature parameters — Ilya-Linh Nguyen

Seeded from `_raw/tg.md` and the 2026-09-28 meeting. His own reports are at
github.com/ilyalinhnguyen/diploma (checkpoints 1 and 2).

## Thesis

| Field | Value |
|---|---|
| Title | Local CVE-trained language models against and alongside SAST for vulnerability detection. Not final |
| Institution | Innopolis University, 2026-2027 |
| Supervisor | Andrey Sadovykh |

## Research questions

| # | Question |
|---|---|
| RQ1 | Does a security-specialised local model filter SAST noise more effectively than a general local model of comparable size? |
| RQ2 | What does combining SAST and an LLM find that neither finds alone, and what do both miss? |
| RQ3 | How does model size, from around 1B upwards, affect detection quality on the same benchmark? |

OPEN: the vulnerability class is not chosen, and it determines the dataset.

## Objectives

| # | Objective | Focus |
|---|---|---|
| O1 | Evaluate local specialised and general models on a shared benchmark | Qwen2.5-Coder as the general baseline against CVE-trained models |
| O2 | Evaluate SAST and LLM in combination, not only side by side | This is the contribution; comparison alone is not |
| O3 | Establish that the benchmarks are not in the models' training data | Otherwise the numbers mean nothing |

## Chapter 2 section map

| Section | Topic | Key concerns |
|---|---|---|
| 2.1 | SAST: taxonomy, tools, known limitations | Lexical, syntactic and semantic analysis; language-specific coupling |
| 2.2 | False positives in static analysis | The noise problem, and what has been tried against it |
| 2.3 | LLMs for vulnerability detection | What has been evaluated, on what, with what result |
| 2.4 | Local and small models | Size against quality, context window limits, sovereignty as a motivation |
| 2.5 | Benchmarks and datasets for vulnerability detection | What exists, and contamination of training data |
| 2.6 | Pipeline and CI/CD security | The origin of the topic, from his own work |

## Topic codes

| Code | Meaning |
|---|---|
| `sast` | Static analysis tools, taxonomy, precision and recall |
| `fp` | False positives and their mitigation |
| `llmvuln` | LLM-based vulnerability detection |
| `small` | Local, small and specialised models |
| `bench` | Benchmarks, datasets, contamination |
| `pipe` | Pipeline and CI/CD security |

## Relevance dimensions

| Dimension | What scores high |
|---|---|
| Detection | Measures vulnerability detection against a labelled ground truth |
| Noise | Addresses false positives directly |
| Local | Evaluates models that can run on own hardware |
| Combination | Studies tool and model working together, not just compared |

## Search queries

Tier 1, core:

```
search_semantic("large language model vulnerability detection static analysis comparison", year="2023-")
search_semantic("LLM false positive reduction static analysis warnings", year="2023-")
```

Tier 2, technical:

```
search_semantic("small language model code security CVE fine-tuning", year="2023-")
search_semantic("vulnerability detection benchmark dataset evaluation", year="2021-")
search_semantic("data contamination code benchmark language model", year="2023-")
```

Tier 3, broad:

```
search_semantic("static application security testing tool comparison", year="2019-")
search_semantic("CI/CD pipeline security misconfiguration detection", year="2020-")
```

## Inclusion and exclusion

**Include:** 2021 or later for the LLM side, older for SAST foundations; reports a labelled
dataset and a baseline; states model versions and whether weights are open.

**Exclude:** vendor benchmarks without a published method; single-example demonstrations;
papers that report detection without any false-positive accounting.

## Known foundational gaps

| Sub-topic | Status |
|---|---|
| Which vulnerability class the thesis covers | Not chosen. Blocks the dataset choice |
| The step beyond comparison: ensemble, SAST plus LLM, or false-positive filtering | Not chosen. Blocks the contribution |
| Training data of the chosen specialised models | Unknown; they are July releases with no papers yet |
| Context window as a limit on what a local model can review | Raised, not read |

## Datasets

Candidate source, his own from another course: github.com/CompSAST/CompSAST, a collection
of benchmarks across several programming languages.

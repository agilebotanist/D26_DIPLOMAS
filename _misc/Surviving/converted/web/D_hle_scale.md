Scraping: https://scale.com/leaderboard/humanitys_last_exam
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://scale.com/leaderboard/humanitys_last_exam
  Settled (dom-quiet, 1703ms)
  Extracting content...
  Extracted 11600 characters

--- Content ---

Challenging LLMs at the frontier of human knowledge

**Update September 17, 2026
**CAIS released the September 17 version of [HLE-Rolling](https://huggingface.co/datasets/cais/hle-rolling), a fork of Humanity's Last Exam that has been continually updated with feedback from the community. For the past year, it’s been cleaned up with internal checks and feedback from outside experts.

We also replaced some easy questions with harder questions from our held out set. The goal of HLE-Rolling is to provide a seamless migration path for researchers in the future once frontier models begin to hit the noise ceiling on the original HLE dataset.**

Update April 3, 2025**

HLE has been finalized to 2,500 questions. The previous version of the leaderboard is now under the “Legacy” section and will be referred to as “HLE-preview”. All current model performance on this version of HLE is similar to the previous version.

Changes

- We removed all errors correctly flagged as part of our community feedback [bug bounty](https://scale.com/blog/humanitys-last-exam-results) program. This program ended on March 21, 2025.
- Searchable questions were removed by the following procedure. A question is potentially searchable if a model with search tools answered correctly, but answered incorrectly without search. Each of these potentially searchable questions was then manually audited, removing any that were easily found via web search. We used GPT-4o mini/GPT-4o search and Perplexity Sonar models in this procedure.
- A backup pool of high quality questions was used to replace a portion of the questions removed.

## Introduction

AI capability is evaluated based on benchmarks, yet as their progress accelerates, benchmarks become quickly saturated, losing their utility as a measurement tool. Performing well on formerly frontier benchmarks such as [MMLU](https://arxiv.org/abs/2009.03300) and [GPQA](https://arxiv.org/abs/2311.12022) are no longer strong signals of progress as frontier models reach or exceed human level performance on them.

In partnership with the [Center for AI Safety](https://www.safe.ai/), we address the problem of benchmark saturation by creating Humanity’s Last Exam (HLE): **2,500 of the toughest, subject-diverse, multi-modal questions designed to be the last academic exam of its kind for AI**. HLE is designed to test for both depth of reasoning (eg. world-class mathematical problems) and breadth of knowledge across its subject domains, providing a precise measurement of model capability. Current frontier models perform poorly on HLE with low accuracies, and systematically exhibit uncalibrated overconfidence in their answers.

We **publicly release Humanity’s Last Exam** for the research community to better understand model capabilities. Evaluation is low-cost, as questions are precise and unambiguous with closed-ended answers provided – allowing for automatic evaluation. To combat the serious problem of training data contamination and benchmark hacking, we have an additional held-out private set of HLE questions to periodically measure overfitting to the public dataset. More research on overfitting can be found [here](https://scale.com/research/llm-performance-grade-school-arithmetic).

High accuracy on HLE would demonstrate AI has achieved expert-level performance on closed-ended cutting-edge scientific knowledge, but it would not alone suggest autonomous research capabilities or “artificial general intelligence.”

See the linked [full paper](https://arxiv.org/abs/2501.14249) and [dataset.](https://lastexam.ai/)

## Methodology

Leaderboard rankings are determined using **Rank (Upper Bound)**, which reflects a model’s statistical position based on confidence intervals. The ranking process follows these steps:

1. Count the number of models that are **statistically significantly better** than the target model.
2. Add **1** to this count to determine the model’s rank.

A model is considered **statistically significantly better** than another if its **lower-bound score (95% confidence interval) is higher** than the other model’s **upper-bound score**.Models receive the **same rank** when the same number of models are statistically better than each of them. This approach groups models based on statistical significance rather than raw scores, ensuring rankings reflect meaningful performance differences.

## Dataset Summary

Humanity’s Last Exam includes questions across dozens of subjects across mathematics, humanities, and the natural sciences. We provide a high level visualization of the distribution of the benchmark categories – though there are many subjects within each summarized category.

![puzzle piece graphic of HLE areas of study](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F50zba0eo%2Flabs%2Ff43f8f8af51005693e802e04fefb9b819c70fa11-2676x1166.png%3Fw%3D1200%26fit%3Dcrop%26auto%3Dformat&w=3840&q=75)

puzzle piece graphic of HLE areas of study

The benchmark is multimodal, with 14% of questions requiring comprehending a diagram or figure to answer the question. In addition, 24% of the questions are multiple choice.

## Dataset Design

Humanity’s Last Exam is a collaborative effort with questions from nearly 1000 subject expert contributors, affiliated with over 500 institutions across 50 countries – composed mostly of professors, researchers, and graduate degree holders. Participants competed for a $500,000 USD prize pool – $5,000 USD for each of the top 50 questions and $500 USD for the next 500 questions, along with the opportunity for optional co-authorship if any question is accepted in the final dataset. This structure incentives top questions from subject experts all around the world. More details can be found in our original announcement: [https://scale.com/blog/humanitys-last-exam](https://scale.com/blog/humanitys-last-exam).

![Dataset creation pipeline for HLE](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F50zba0eo%2Flabs%2F7562725f47afbde71b4e480ed9d0da5ccc68b89d-2558x714.png%3Fw%3D1200%26fit%3Dcrop%26auto%3Dformat&w=3840&q=75)

Dataset creation pipeline for HLE

Submission: Submitted questions must stump several frontier LLMs for exact match questions, or allow only up to random chance across all LLMs for multiple choice questions to be considered for human review. This ensures the questions are of a necessary difficulty bar for the current generation of models, we further verify they are sufficiently difficult with human review. In total, we received over 70,000 submissions, with 13,000 passing this difficulty bar and forwarded to human review.

Human Review: We train experts sourced from [Scale’s Outlier platform](https://scale.com/blog/new-era-outlier) to review questions. All of the human reviewers have a graduate degree in their field. Reviewers score questions against a standardized rubric, providing feedback to help question creators iterate questions. A primary round is used to shortlist the best questions. A secondary review with both organizers and expert reviewers approves or rejects questions from the final dataset – resulting in 2,700 public questions and an additional set of private questions of equal quality and difficulty. Subsequent community feedback and removal of searchable questions resulted in a finalized dataset of 2,500 questions.

## Metrics

We report both the accuracy on public questions of Humanity’s Last Exam and use the model’s own stated confidence to derive an [RMS calibration error](https://github.com/hendrycks/outlier-exposure/blob/master/utils/calibration_tools.py) using the implementation from [Hendrycks et al., 2022](https://arxiv.org/abs/2112.05135) with the default hyperparameters provided, reported in our paper for brevity. Models are ranked on the leaderboard using accuracy, however we want to emphasize calibration errors as an important metric in our paper.

A well-calibrated model should exhibit an average confidence similar to its accuracy on a benchmark - eg. 50% accuracy paired with 50% confidence. As of our initial publication, we observe systematic high calibration errors (greater than 80%) paired with low accuracy (less than 10%), which indicates strong evidence for confabulation/hallucination in all measured models.

Details on our evaluation methodology found below. At this time, we do not report any model performance metrics on the private held-out set.

## Evaluation Methodology

Evaluation is automatic. Each model on the leaderboard is evaluated on all public questions of Humanity’s Last Exam with temperature 0.0 when configurable or stated otherwise. Models are prompted to give a final answer and an estimation of confidence using the system prompts (or user prompt when not configurable), following the setup from [Wei et al., 2024](https://arxiv.org/abs/2411.04368).

As HLE uses closed-form solutions, we use o3-mini-2025-01-31 as an automatic extractor and judge to compare the model response against the ground truth answer. We employ structured decoding to extract a JSON from the following prompt. We note small differences could arise from different judge models and prompts used on edge cases (eg. acceptable precision), hence we encourage the documentation of prompts and models used for evaluation on HLE. We document ours for this evaluation below.

## Acknowledgements

Humanity’s Last Exam was a global collaborative effort developed in partnership with the [Center for AI Safety](https://www.safe.ai/). We extend our deepest gratitude to all participating question contributors and expert reviewers involved in creating and refining the Humanity’s Last Exam dataset.

Scale AI Team: Ziwen Han, Josephina Hu, † Hugh Zhang, Chen Bo Calvin Zhang, Mohamed Shaaban, John Ling, Sean Shi, Michael Choi, Anish Agrawal, Arnav Chopra, William Qian, Luis Esquivel, Caton Lu, Monica Mishra, Dean Lee, Summer Yue, Alexandr Wang

## Performance Comparison

1

54.80±1.94Calib Err: 39

2

46.50±2.00Calib Err: 20

3

46.44±1.96Calib Err: 51

4

Sonnet 5.5 (xhigh)

NEW

46.12±1.95

5

44.52±1.96Calib Err: 51

6

44.32±1.95Calib Err: 38

7

40.56±1.92Calib Err: 50

8

37.52±1.90Calib Err: 57

9

36.24±1.88Calib Err: 42

10

36.20±1.88Calib Err: 47

11

34.44±1.86Calib Err: 46

12

31.64±1.82Calib Err: 49

13

30.12±1.83

14

27.80±1.76Calib Err: 45

15

25.32±1.70Calib Err: 50

16

25.20±1.70Calib Err: 55

17

24.37±1.81Calib Err: 67

18

23.68±1.67Calib Err: 55

19

21.64±1.61Calib Err: 72

20

20.32±1.58Calib Err: 34

21

19.44±1.55Calib Err: 65

22

19.20±1.54Calib Err: 39

23

19.00±1.54Calib Err: 44

24

18.16±1.51Calib Err: 71

25

18.08±1.51Calib Err: 57

26

17.80±1.50Calib Err: 70

27

14.28±1.37Calib Err: 59

28

14.16±1.37Calib Err: 56

29

13.72±1.35Calib Err: 65

30

12.08±1.28Calib Err: 80

31

11.52±1.25Calib Err: 71

32

10.96±1.22Calib Err: 82

33

10.72±1.21Calib Err: 73

34

8.64±1.10Calib Err: 83

35

8.32±1.08Calib Err: 79

36

8.12±1.07Calib Err: 77

37

8.12±1.07Calib Err: 82

38

8.04±1.07Calib Err: 80

39

7.96±1.06Calib Err: 83

40

7.92±1.06Calib Err: 70

41

7.76±1.05Calib Err: 75

42

7.52±1.03Calib Err: 70

43

6.80±0.99Calib Err: 69

44

6.68±0.98Calib Err: 74

45

6.56±0.97Calib Err: 82

46

5.68±0.91Calib Err: 83

47

5.52±0.90Calib Err: 76

48

5.44±0.89Calib Err: 85

49

5.40±0.89Calib Err: 89

50

4.60±0.82Calib Err: 88

51

4.52±0.81Calib Err: 77

52

4.40±0.80Calib Err: 80

53

4.08±0.78Calib Err: 84

54

3.64±0.73Calib Err: 82

55

2.72±0.64Calib Err: 89

***Rank (UB):** 1 + the number of models whose lower CI bound exceeds this model’s upper CI bound.*

\-

***CE:** Calibration Error*

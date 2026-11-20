Scraping: https://gaia-benchmark-leaderboard.hf.space
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://gaia-benchmark-leaderboard.hf.space
  Settled (dom-quiet, 2251ms)
  Extracting content...
  Extracted 3603 characters

--- Content ---

## GAIA Leaderboard

GAIA is a benchmark which aims at evaluating next-generation LLMs (LLMs with augmented capabilities due to added tooling, efficient prompting, access to search, etc). (See our [paper](https://arxiv.org/abs/2311.12983) for more details.)

## Data

GAIA is made of more than 450 non-trivial question with an unambiguous answer, requiring different levels of tooling and autonomy to solve. It is therefore divided in 3 levels, where level 1 should be breakable by very good LLMs, and level 3 indicate a strong jump in model capabilities. Each level is divided into a fully public dev set for validation, and a test set with private answers and metadata.

GAIA data can be found in [this dataset](https://huggingface.co/datasets/gaia-benchmark/GAIA). Questions are contained in `metadata.jsonl`. Some questions come with an additional file, that can be found in the same folder and whose id is given in the field `file_name`.

**Please do not repost the public dev set, nor use it in training data for your models.**

## Leaderboard

Submission made by our team are labelled "GAIA authors". While we report average scores over different runs when possible in our paper, we only report the best run in the leaderboard.

See below for submissions.

Results: Test

## Submissions

Results can be submitted for the test set (we closed the validation leaderboard, as it was no longer informative). Scores are expressed as the percentage of correct answers for a given split.

Each question calls for an answer that is either a string (one or a few words), a number, or a comma separated list of strings or floats, unless specified otherwise. There is only one correct answer. Hence, evaluation is done via quasi exact match between a model’s answer and the ground truth (up to some normalization that is tied to the “type” of the ground truth).

In our evaluation, we use a system prompt to instruct the model about the required format:

```md
You are a general AI assistant. I will ask you a question. Report your thoughts, and finish your answer with the following template: FINAL ANSWER: [YOUR FINAL ANSWER]. YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings. If you are asked for a number, don't use comma to write your number neither use units such as $ or percent sign unless specified otherwise. If you are asked for a string, don't use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise. If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string.
```

We advise you to use the system prompt provided in the paper to ensure your agents answer using the correct and expected format. In practice, GPT4 level models easily follow it.

We expect submissions to be json-line files with the following format. The first two fields are mandatory, `reasoning_trace` is optional:

```md
{"task_id": "task_id_1", "model_answer": "Answer 1 from your model", "reasoning_trace": "The different steps by which your model reached answer 1"}
{"task_id": "task_id_2", "model_answer": "Answer 2 from your model", "reasoning_trace": "The different steps by which your model reached answer 2"}
```

Our scoring function can be found [here](https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/scorer.py).

![Sign in with Hugging Face icon](https://gaia-benchmark-leaderboard.hf.space/gradio_api/file=/usr/local/lib/python3.13/site-packages/gradio/icons/huggingface-logo.svg)

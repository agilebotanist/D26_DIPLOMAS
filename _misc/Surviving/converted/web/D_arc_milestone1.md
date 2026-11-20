Scraping: https://arcprize.org/blog/arc-prize-2026-milestone-1
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://arcprize.org/blog/arc-prize-2026-milestone-1
  Settled (dom-quiet, 1466ms)
  Extracting content...
  Extracted 6784 characters

--- Content ---

![ARC-AGI-3 Milestone 1 winners: Tufa Labs 'The Duck', Reki, and Md Boktiar Mahbub Murad](/media/images/arc-agi-3-milestone-1-winners.png)

The top three submissions from ARC-AGI-3 Milestone 1

[ARC-AGI-3](/arc-agi/3) is our first Interactive Reasoning Benchmark. It is a set of novel, video-game-like environments where agents must perceive, explore, plan, and act across long horizons. Due to a hidden hold-out set, these games can't be memorized. They reward on-the-fly learning, efficient exploration, and the ability to set your own goals when the objective isn't clear. Solving them is easy (and even fun) for humans, but remains hard for today's AI.

New to ARC Prize 2026, we've introduced two milestone prizes that reward the top mid-competition open-source solutions to ARC-AGI-3. They exist to inspire people to try new ideas and create incentives to push those ideas further.

We're excited to award our first **$37.5K ARC-AGI-3 milestone prize**, which ran through **June 30th**. Below are the top three submissions from our [ARC-AGI-3 Kaggle competition](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3).

---

## 1st Place - Tufa Labs, "The Duck"

A small open-source LLM that plays ARC-AGI-3 by writing and running Python in a live REPL (similar to the [Duke Harness](https://blog.alexisfox.dev/arcagi3)), treating each game like an interactive coding problem.

[Notebook](https://www.kaggle.com/code/jeroencottaar/tufa-labs-duck-harness-june-30-milestone-winner) · [Write-up](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/discussion/717133) · [Video](https://www.youtube.com/watch?v=Vg6FBKTlfOw) · [Tufa Labs](https://tufalabs.ai/)

![Tufa Labs 'The Duck' submission notebook on Kaggle](/media/images/arc-agi-3-milestone-1-tufa-labs.png)

Tufa Labs 'The Duck' submission notebook on Kaggle

This submission converts the game state into Python variables and interacts with it through a REPL. The process includes reasoning, calling helper functions, running code, taking an action, seeing the results, repeating. It perceives the board through a rendered image, the raw ASCII grid, and a segmentation tool for zooming into regions. It chooses whichever representation fits the moment.

To keep playing indefinitely without exhausting the context window, The Duck continuously pops the oldest messages ("infinite play via eviction"), keeping only the system prompt and recent history. The team's stated philosophy is to keep the harness lightweight and generic and let the model drive, and they report the gains came from multimodality and better base models, not hand-built tools.

**What's interesting:**

- This submission is the only one of the winners that has the "agent-writes-code" approach. The other two simply use "pick a JSON action."
- It is a spiritual successor to " [Stochastic Goose](https://arcprize.org/blog/arc-agi-3-preview-30-day-learnings#:~:text=Replays-,StochasticGoose,-Dries%20Smit%20%2D%20Lead)," which won the earlier [ARC-AGI-3 Agent Preview Competition](/blog/arc-agi-3-preview-30-day-learnings).
- Runs Qwen 3.6 27B FP8 locally.
- Tufa Labs noted that, counterintuitively, hand-crafted tools actually hurt the model; letting it improvise worked better.
- Featured on [Machine Learning Street Talk](https://www.youtube.com/watch?v=Vg6FBKTlfOw).
![The Tufa Labs team on Machine Learning Street Talk](/media/images/tufa-labs-mlst.jpg)

The Tufa Labs team on Machine Learning Street Talk

---

## 2nd Place - Reki

A vision-language model that looks at pictures of the game board and returns one JSON action per step.

[Notebook](https://www.kaggle.com/code/ruichardliu/milestone1-2nd-solution)

![Reki's submission notebook on Kaggle](/media/images/arc-agi-3-milestone-1-reki.png)

Reki's submission notebook on Kaggle

At its core this is a "vision-LLM-as-policy" agent: each turn it renders the recent frames as labeled images, feeds them to Gemma-4-31B locally, and asks for a single JSON object describing what changed, a short plan, and the next 1-4 actions. It also keeps a running reflection memory (refreshed every ~10 steps).

Additionally, there is a numpy click heuristic mechanism (no GPU needed). Hardcoded rules make fallback and exploratory clicks prefer small, rare-colored, button-like shapes instead of random pixels. A "Dead-signature" notices when clicking a *type* of object never changes anything and stops wasting clicks on it for the rest of the level. Both are toggle-able via environment variables.

**What's interesting:**

- Built on the official [ARC Prize GPT-OSS-120B template](https://www.kaggle.com/code/gregkamradt/arc-agi-3-gpt-oss-120b). Reki swapped the model to Gemma-4-31B.
- Designed for easy ablation: individual features or tricks can be toggled on or off using environment variables, allowing the team to directly measure the impact of each change.
- Includes JSON self-repair, legal-action constraints, a 1-4 action plan queue, reflection memory.

---

## 3rd Place - Md Boktiar Mahbub Murad, "forge"

The same "look at the board and return a JSON action" agent as Reki (2nd place), but packaged as a configurable framework.

[Notebook](https://www.kaggle.com/code/mbmmurad/arc-agi-3-lb-0-86-3rd-place-candidate-milestone)

![Md Boktiar Mahbub Murad's submission notebook on Kaggle](/media/images/arc-agi-3-milestone-1-md.png)

Md Boktiar Mahbub Murad's submission notebook on Kaggle

This submission is similar to Reki's: render frames to images, show them to a locally-served Gemma-4-31B, keep a reflection memory, and return structured JSON actions with repair and legal-action guards.

The difference is that this one is wrapped in a profile-driven framework (called "forge") with parameters that control flow. The submission has a generator for multiple candidate actions and an arbiter to score and pick between them and an optional confidence prompt that forces safe/reversible moves when the model is unsure. However, the top-scoring run of thise notebook used a profile that *turns off* all of the extra machinery.

**What's interesting:**

- Built on the official [ARC Prize GPT-OSS-120B template](https://www.kaggle.com/code/gregkamradt/arc-agi-3-gpt-oss-120b).
- Author mentioned that local public-game checks weren't a reliable leaderboard proxy.

---

Congratulations to all three teams, and thank you to everyone who submitted.

The second (and final) milestone prize will end September 30th. You can start competing right now. The fastest way in is to copy one of the [templates](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3/code) or an existing submission above, make it your own, and see how far you can push it.

Head to the [ARC-AGI-3 Kaggle competition](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3) to get started.

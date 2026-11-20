Scraping: https://os-world.github.io/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://os-world.github.io/
  Settled (dom-quiet, 2314ms)
  Extracting content...
  Extracted 30553 characters

--- Content ---

![osworld task_demonstration](static/images/task_demonstration.png)

**OSWorld** is a first-of-its-kind scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across operating systems. It can serve as a unified environment for evaluating open-ended computer tasks that involve arbitrary apps (e.g., task examples in the above Fig). We also create a benchmark of 369 real-world computer tasks in **OSWorld** with reliable, reproducible setup and evaluation scripts. *Note: 8 Google Drive tasks may require manual configuration or can be excluded (361 tasks) due to network dependencies.*

## Abstract

Autonomous agents that accomplish complex computer tasks with minimal human interventions have the potential to transform human-computer interaction, significantly enhancing accessibility and productivity. However, existing benchmarks either lack an interactive environment or are limited to environments specific to certain applications or domains, failing to reflect the diverse and complex nature of real-world computer use, thereby limiting the scope of tasks and agent scalability. To address this issue, we introduce **OSWorld**, the first-of-its-kind scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across various operating systems such as Ubuntu, Windows, and macOS. **OSWorld** can serve as a unified, integrated computer environment for assessing open-ended computer tasks that involve arbitrary applications. Building upon **OSWorld**, we create a benchmark of 369 computer tasks involving real web and desktop apps in open domains, OS file I/O, and workflows spanning multiple applications (note: 8 Google Drive tasks may require manual setup or can be excluded for a 361-task evaluation). Each task example is derived from real-world computer use cases and includes a detailed initial state setup configuration and a custom execution-based evaluation script for reliable, reproducible evaluation. Extensive evaluation of state-of-the-art LLM/VLM-based agents on **OSWorld** reveals significant deficiencies in their ability to serve as computer assistants. While humans can accomplish over 72.36% of the tasks, the best model achieves only 12.24% success, primarily struggling with GUI grounding and operational knowledge. Comprehensive analysis using **OSWorld** provides valuable insights for developing multimodal generalist agents that were not possible with previous benchmarks.

## OSWorld Environment Infrastructure

![environment infrastructure](static/images/env.png)

The **OSWorld** environment uses a configuration file for initializing tasks *(highlighted in red)*, agent interaction, post-processing upon agent completion *(highlighted in orange)*, retrieving files and information *(highlighted in yellow)*, and executing the evaluation function *(highlighted in green)*. The corresponding configuration items are highlighted in colors that match their respective components within the environment. Environments can run in parallel on a single host machine for learning or evaluation purposes. Headless operation is supported.

## Data Statistics and Comparison

Below we present an overview of the main statistics of **OSWorld**, showcasing the outline and a broad spectrum of tasks. **OSWorld** contains a total of 369 tasks (and an additional 43 tasks on Windows for analysis).

##### Key statistics of OSWorld.

The "Supp. tasks" refers to the Windows-based tasks, that could only be used after activation due to copyright restrictions.
![data-overview](static/images/statistics.png)

![data-composition](static/images/pie_chart.png)

Distribution of task instructions in **OSWorld**
based on the app domains and operation types to showcase the content intuitively.

We make a comparison of **OSWorld** against some other different benchmarks for digital agents as presented below.
**The columns indicate:** whether they provide a controllable executable environment *(Control. Exec. Env.)*, the ease of adding new tasks involving arbitrary applications in open domains *(Environment Scalability)*, support for multimodal agent evaluation *(Multimodal Support)*, support for and inclusion of cross-app tasks *(Cross-App)*, capability to start tasks from an intermediate initial state *(Intermediate Init. State)*, and the number of execution-based evaluation functions *(# Exec.-based Eval. Func.)*.

<table><thead><tr><th></th><th rowspan="1">OSWorld</th></tr></thead><tbody><tr><td># Instances<br>(# Templates)</td><td>369</td></tr><tr><td>Control.<br>Exec. Env.</td><td>Computer</td></tr><tr><td>Environment Scalability?</td><td>✔️</td></tr><tr><td>Multimodal<br>Support?</td><td>✔️</td></tr><tr><td>Cross-App?</td><td>✔️</td></tr><tr><td>Intermediate<br>Init. State?</td><td>✔️</td></tr><tr><td># Exec.-based<br>Eval. Func.</td><td>134</td></tr></tbody></table>

| [GAIA](https://huggingface.co/gaia-benchmark) | [Mind2Web](https://osu-nlp-group.github.io/Mind2Web/) | [WebLINX](https://mcgill-nlp.github.io/weblinx/) | [PixelHelp](https://github.com/google-research/google-research/tree/master/seq2act) | [MetaGUI](https://x-lance.github.io/META-GUI-Leaderboard/) | [AitW](https://github.com/google-research/google-research/tree/master/android_in_the_wild) | [OmniAct](https://huggingface.co/datasets/Writer/omniact) | [ScreenAgent](https://github.com/niuzaisheng/ScreenAgent) | [AgentBench](https://llmbench.ai/agent) | [InterCode](https://intercode-benchmark.github.io/) | [MiniWoB++](https://miniwob.farama.org/) | [WebShop](https://webshop-pnlp.github.io/) | [WebArena](https://webarena.dev/) | [VisualWebArena](https://jykoh.com/vwa) | [WorkArena](https://servicenow.github.io/WorkArena/) | [WikiHow](https://github.com/X-LANCE/Mobile-Env) | [AssistGUI](https://github.com/showlab/assistgui) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 466 | 2350 | 2337 | 187 | 1125 | 30k | 9802 | 70 | 1091 | 1350(3) | 125 | 12k(1) | 812(241) | 910(314) | 23k(29) | 150(16) | 100 |
| ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Multi-isolated | Code | Web | Web | Web | Web | Web | Mobile | ❌ |
| \- | \- | \- | \- | \- | \- | \- | \- | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |
| ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| ❌ | ✔️ | ✔️ | ❌ | ❌ | ✔️ | ✔️ | ✔️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✔️ | ❌ | ✔️ |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 3 | 125 | 1 | 5 | 6 | 7 | 16 | 2 |

## Benchmark

We adopt state-of-the-art LLM and VLM from open-source representatives such as UI-TARS, Agent-S, Qwen, Mixtral and CogAgent, and closed-source ones from Operator, GPT, Gemini, and Claude families on **OSWorld**, as LLM and VLM agent baselines. We also explore methods such as the Set-of-Marks aided approach, which has been demonstrated to improve spatial capabilities for visual reasoning. **We are actively updating the benchmark with new LLMs, VLMs and methods. Pull requests welcomed!**

#### Important Notice: Google Drive Tasks (2025-07-28)

**OSWorld contains 8 Google Drive-related tasks** that may encounter setup issues during task initialization due to IP changes or other network-related factors, even when following our configuration guidelines correctly.

**Two acceptable approaches for evaluation:**

1. **Manual Adjustment**: You can manually configure these 8 tasks to complete the full **369 tasks** evaluation
2. **Exclude Tasks**: You can exclude these 8 tasks and run **361 tasks** instead - **this is officially permitted and acceptable**

Both approaches are valid for benchmark comparison and leaderboard submission.

#### Results

These are official results evaluated by our team under unified settings and environment. All models are tested with consistent evaluation protocols to ensure fair comparison.

For self-reported results and progress trends across different modalities, [click here](#).

All verified trajectories are hosted on [Hugging Face](https://huggingface.co/datasets/xlangai/ubuntu_osworld_verified_trajs) for community analysis.

**What are the differences among General model, Specialized model, and Agentic framework?**
A General model is a model with broad, general-purpose capabilities. “Computer use” is one capability that can be elicited via prompting; the model itself can still perform other tasks such as dialogue and code generation. A Specialized model is trained specifically to serve as a computer-use agent; other capabilities are out of scope and are not emphasized in the corresponding reports. An Agentic framework organizes one or more General and Specialized models into a structured workflow—commonly, a GPT-family model acts as the planner while a proprietary or task-specific model serves as the grounder.
We will add new paradigms as they emerge.

- OSWorld-Verified Results

- Foundation E2E GUI
- All

#### Filters:

| Rank | Model & Date | Approach & Details | Success Rate (Avg±Std) |  |
| --- | --- | --- | --- | --- |
| 1 \* | **claude-fable-5\[1m\]**  Anthropic  📅 Aug 1, 2026  [Anthropic, '26](https://www.anthropic.com/claude/fable) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **86.0%** ▶ |  |
| 2 | **claude-opus-5\[1m\]**  Anthropic  📅 Aug 1, 2026  [Anthropic, '26](https://www.anthropic.com/news/claude-opus-5) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **83.4%** ▶ |  |
| 3 | **Muse Spark 1.1**  Meta Superintelligence Labs  📅 Jul 9, 2026  [Meta Superintelligence Labs](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **80.7%** ▶ |  |
| 4 | **Holo3-35B-A3B**  H Company  📅 Apr 20, 2026  [H Company](https://hcompany.ai/holo3) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 2 | **80.4±2.2%** ▶ |  |
| 5 | **MiniMax M3**  MiniMax  📅 Jun 8, 2026  [MiniMax Team](https://www.minimaxi.com/blog/minimax-m3) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **75.2%** ▶ |  |
| 6 | **Qwen 3.7 Plus**  Qwen Team, Alibaba Group  📅 May 25, 2026  [Qwen Team, Alibaba Group](https://qwen.ai/blog?id=qwen3.7) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **73.3%** ▶ |  |
| 7 | **Kimi K2.6**  Moonshot AI  📅 Apr 20, 2026  [Kimi Team](https://www.kimi.com/blog/kimi-k2-6) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **73.1%** ▶ |  |
| 8 | **claude-sonnet-4-6**  Anthropic  📅 Mar 8, 2026  [Anthropic, '26](https://www.anthropic.com/news/claude-sonnet-4-6) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **72.1%** ▶ |  |
| 9 | **Kimi K2.5**  Moonshot AI  📅 Jan 31, 2026  [Kimi Team](https://github.com/MoonshotAI/Kimi-K2.5/blob/master/tech_report.pdf) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **63.3%** ▶ |  |
| 10 | **claude-sonnet-4-5-20250929**  Anthropic  📅 Oct 31, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-sonnet-4-5) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **62.9%** ▶ |  |
| 11 | **Seed-1.8**  ByteDance Seed  📅 Dec 18, 2025  [ByteDance Seed](https://seed.bytedance.com/en/seed1_8) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **61.9%** ▶ |  |
| 12 | **claude-sonnet-4-5-20250929**  Anthropic  📅 Oct 31, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-sonnet-4-5) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **58.1%** ▶ |  |
| 13 | **EvoCUA-20260105**  Meituan LongCat Team  📅 Jan 6, 2026  [Meituan LongCat Team](https://arxiv.org/abs/2601.15876) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **56.7%** ▶ |  |
| 14 | **GUI-Owl-1.5 32B**  Tongyi Lab, Alibaba Group  📅 Mar 27, 2026  [Mobile-Agent Team](https://arxiv.org/abs/2602.16855) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 1 | **55.4%** ▶ |  |
| 15 | **DeepMiner-Mano-72B**  Mininglamp Technology  📅 Oct 31, 2025  [DeepMiner-Mano Team](https://arxiv.org/abs/2509.17336) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 1 | **53.9%** ▶ |  |
| 16 | **UI-TARS-2-2509**  ByteDance Seed  📅 Oct 14, 2025  [ByteDance Seed](https://arxiv.org/pdf/2509.02544) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 1 | **53.1%** ▶ |  |
| 17 | **EvoCUA**  Meituan LongCat Team  📅 Dec 24, 2025  [Meituan LongCat Team](https://arxiv.org/abs/2601.15876) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **50.3%** ▶ |  |
| 18 | **EvoCUA-8B-20260105**  Meituan LongCat Team  📅 Jan 13, 2026  [Meituan LongCat Team](https://arxiv.org/abs/2601.15876) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **46.1%** ▶ |  |
| 19 | **opencua-72b-preview**  The University of Hong Kong & Moonshot AI  📅 Oct 1, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 3 | **45.0±0.9%** ▶ |  |
| 20 | **opencua-72b-preview**  The University of Hong Kong & Moonshot AI  📅 Oct 1, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 1 | **44.9%** ▶ |  |
| 21 | **claude-4-sonnet-20250514**  Anthropic  📅 Jul 28, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-4) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **43.9%** ▶ |  |
| 22 | **claude-sonnet-4-5-20250929**  Anthropic  📅 Oct 31, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-sonnet-4-5) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **42.9%** ▶ |  |
| 23 | **UI-TARS-250705**  ByteDance Seed  📅 Sep 16, 2025  [ByteDance Seed](https://arxiv.org/pdf/2509.02544) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **41.8%** ▶ |  |
| 24 | **qwen3-vl-flash-2025-10-25**  Qwen Team, Alibaba Group  📅 Oct 23, 2025  [Alibaba Qwen](https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **41.6%** ▶ |  |
| 25 | **claude-4-sonnet-20250514**  Anthropic  📅 Jul 28, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-4) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **41.4%** ▶ |  |
| 26 | **DART-GUI-7B-0924**  BIGAI & BIT & DataCanvas  📅 Jan 23, 2026  [BIGAI & BIT & DataCanvas](https://arxiv.org/pdf/2509.23866) | **Type:** Specialized model  **Max Steps:** 30  **Runs:** 1 | **40.5%** ▶ |  |
| 27 | **DeepMiner-Mano-7B**  Mininglamp Technology  📅 Sep 18, 2025  [DeepMiner-Mano Team](https://arxiv.org/abs/2509.17336) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 1 | **40.1%** ▶ |  |
| 28 | **doubao-1-5-thinking-vision-pro-250717**  ByteDance Seed  📅 Jul 28, 2025  [ByteDance Seed, '25](https://arxiv.org/abs/2505.07062) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **40.0%** ▶ |  |
| 29 | **opencua-72b-preview**  The University of Hong Kong & Moonshot AI  📅 Oct 1, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 1 | **39.0%** ▶ |  |
| 30 | **claude-3-7-sonnet-20250219**  Anthropic  📅 Jul 28, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-3-7-sonnet) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **35.8%** ▶ |  |
| 31 | **claude-3-7-sonnet-20250219**  Anthropic  📅 Jul 28, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-3-7-sonnet) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **35.6%** ▶ |  |
| 32 | **opencua-32b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 3 | **34.8±0.8%** ▶ |  |
| 33 | **opencua-32b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 3 | **34.1±0.7%** ▶ |  |
| 34 | **doubao-1-5-thinking-vision-pro-250428**  ByteDance Seed  📅 Jul 28, 2025  [ByteDance Seed, '25](https://arxiv.org/abs/2505.07062) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **33.8%** ▶ |  |
| 35 | **gui-owl-7b**  Tongyi Lab, Alibaba Group  📅 Sep 3, 2025  [Ye et al., '25](https://arxiv.org/abs/2508.15144) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 1 | **32.1%** ▶ |  |
| 36 | **doubao-1-5-thinking-vision-pro-250717**  ByteDance Seed  📅 Jul 28, 2025  [ByteDance Seed, '25](https://arxiv.org/abs/2505.07062) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **31.9%** ▶ |  |
| 37 | **computer-use-preview**  OpenAI  📅 Jul 28, 2025  [OpenAI, '25](https://openai.com/index/computer-using-agent/) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 1 | **31.3%** ▶ |  |
| 38 | **claude-4-sonnet-20250514**  Anthropic  📅 Jul 28, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-4) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **31.2%** ▶ |  |
| 39 | **computer-use-preview**  OpenAI  📅 Jul 28, 2025  [OpenAI, '25](https://openai.com/index/computer-using-agent/) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 2 | **30.5±0.9%** ▶ |  |
| 40 | **TianXi-Action-7B**  Lenovo  📅 Aug 11, 2025  [Tang et al., '25](http://arxiv.org/abs/2508.04037) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 2 | **29.8±0.6%** ▶ |  |
| 41 | **opencua-32b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 3 | **29.7±1.1%** ▶ |  |
| 42 | **opencua-7b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 3 | **28.2±0.5%** ▶ |  |
| 43 | **doubao-1-5-thinking-vision-pro-250428**  ByteDance Seed  📅 Jul 28, 2025  [ByteDance Seed, '25](https://arxiv.org/abs/2505.07062) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **27.8%** ▶ |  |
| 44 | **uitars-1.5-7b**  ByteDance Seed & Tsinghua University  📅 Jul 28, 2025  [Seed-TARS, '25](https://seed-tars.com/1.5) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 2 | **27.4±2.2%** ▶ |  |
| 45 | **uitars-1.5-7b**  ByteDance Seed & Tsinghua University  📅 Jul 28, 2025  [Seed-TARS, '25](https://seed-tars.com/1.5) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 2 | **27.3±2.1%** ▶ |  |
| 46 | **claude-3-7-sonnet-20250219**  Anthropic  📅 Jul 28, 2025  [Anthropic, '25](https://www.anthropic.com/news/claude-3-7-sonnet) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **27.1%** ▶ |  |
| 47 | **uitars-72b-dpo**  ByteDance Seed & Tsinghua University  📅 Jul 28, 2025  [Qin et al., '24](https://github.com/bytedance/UI-TARS) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 1 | **27.1%** ▶ |  |
| 48 | **opencua-7b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 3 | **26.6±0.4%** ▶ |  |
| 49 | **computer-use-preview**  OpenAI  📅 Jul 28, 2025  [OpenAI, '25](https://openai.com/index/computer-using-agent/) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 1 | **26.0%** ▶ |  |
| 50 | **uitars-72b-dpo**  ByteDance Seed & Tsinghua University  📅 Jul 28, 2025  [Qin et al., '24](https://github.com/bytedance/UI-TARS) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 1 | **25.8%** ▶ |  |
| 51 | **uitars-1.5-7b**  ByteDance Seed & Tsinghua University  📅 Jul 28, 2025  [Seed-TARS, '25](https://seed-tars.com/1.5) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 2 | **24.5±1.2%** ▶ |  |
| 52 | **opencua-7b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 3 | **24.3±1.4%** ▶ |  |
| 53 | **uitars-72b-dpo**  ByteDance Seed & Tsinghua University  📅 Jul 28, 2025  [Qin et al., '24](https://github.com/bytedance/UI-TARS) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 1 | **24.0%** ▶ |  |
| 54 | **opencua-qwen2-7b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 1 | **23.1%** ▶ |  |
| 55 | **o3**  OpenAI  📅 Jul 28, 2025  [OpenAI, '25](https://openai.com/index/introducing-o3-and-o4-mini/) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **23.0%** ▶ |  |
| 56 | **opencua-qwen2-7b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 1 | **20.6%** ▶ |  |
| 57 | **opencua-a3b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 50  **Runs:** 1 | **19.9%** ▶ |  |
| 58 | **opencua-qwen2-7b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 1 | **19.9%** ▶ |  |
| 59 | **opencua-a3b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 100  **Runs:** 1 | **17.7%** ▶ |  |
| 60 | **o3**  OpenAI  📅 Jul 28, 2025  [OpenAI, '25](https://openai.com/index/introducing-o3-and-o4-mini/) | **Type:** General model  **Max Steps:** 50  **Runs:** 1 | **17.2%** ▶ |  |
| 61 | **opencua-a3b**  The University of Hong Kong & Moonshot AI  📅 Jul 28, 2025  [Wang et al., '25](https://opencua.xlang.ai/) | **Type:** Specialized model  **Max Steps:** 15  **Runs:** 1 | **16.9%** ▶ |  |
| 62 | **kimi-vl-a3b**  Moonshot AI  📅 Jul 28, 2025  [Kimi Team, '25](https://arxiv.org/abs/2504.07491) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **10.3%** ▶ |  |
| 63 | **kimi-vl-a3b**  Moonshot AI  📅 Jul 28, 2025  [Kimi Team, '25](https://arxiv.org/abs/2504.07491) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **9.7%** ▶ |  |
| 64 | **o3**  OpenAI  📅 Jul 28, 2025  [OpenAI, '25](https://openai.com/index/introducing-o3-and-o4-mini/) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **9.1%** ▶ |  |
| 65 | **qwen2.5-vl-72b-instruct**  Alibaba Cloud, Qwen Team  📅 Jul 28, 2025  [Qwen Team, '25](https://qwenlm.github.io/blog/qwen2.5-vl/) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **5.0%** ▶ |  |
| 66 | **qwen2.5-vl-72b-instruct**  Alibaba Cloud, Qwen Team  📅 Jul 28, 2025  [Qwen Team, '25](https://qwenlm.github.io/blog/qwen2.5-vl/) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **4.4%** ▶ |  |
| 67 | **qwen2.5-vl-32b-instruct**  Alibaba Cloud, Qwen Team  📅 Jul 28, 2025  [Qwen Team, '25](https://qwenlm.github.io/blog/qwen2.5-vl/) | **Type:** General model  **Max Steps:** 100  **Runs:** 1 | **3.9%** ▶ |  |
| 68 | **qwen2.5-vl-32b-instruct**  Alibaba Cloud, Qwen Team  📅 Jul 28, 2025  [Qwen Team, '25](https://qwenlm.github.io/blog/qwen2.5-vl/) | **Type:** General model  **Max Steps:** 15  **Runs:** 1 | **3.0%** ▶ |  |

## Analysis

We conduct a qualitative analysis in the aspect of models, methods, and human to find out factors influencing the performance of VLMs in digital agent tasks and their underlying behavioral logic. We investigate the impact of task attributes *(such as difficulty, feasibility, visual requirement, and GUI complexity)*, input measurements *(such as screenshot resolution, the influence of trajectory history, and the effect of UI layout)*, and explore whether there are patterns in the agent’s performance across different operating systems. Here is an overview of our analysis outcome.

## Videos

Special thanks to the following YouTubers and enthusiasts for their reports. We are delighted to see the community’s interest. If you would like a brief video introduction and their thoughts, feel free to check them out!

## Acknowledgement

We thank [Sida Wang](https://www.sidaw.xyz/), [Peter Shaw](https://www.ptshaw.com/), [Alane Suhr](https://www.alanesuhr.com/), [Luke Zettlemoyer](https://www.cs.washington.edu/people/faculty/lsz), [Haoyuan Wu](https://github.com/FredWuCZ), [Junli Wang](https://junliwang.tech/), [Chengyou Jia](https://chengyou-jia.github.io/), [Junlin Yang](https://x.com/junlin45300), [Junlei Zhang](https://github.com/leoozy), [Chen Henry Wu](https://chenwu.io/), [Pengcheng Yin](https://pengcheng.in/), [Shunyu Yao](https://ysymyth.github.io/), [Xing Han Lu](https://xinghanlu.com/), [Siva Reddy](https://sivareddy.in/), [Ruoxi Sun](https://www.linkedin.com/in/ruoxi-sun-84a85457/), [Zhiyuan Zeng](https://zhiyuan-zeng.github.io/), and [Lei Li](https://lilei-nlp.github.io/) for their helpful feedback on this work

## Acknowledgement for OSWorld-Verified

Special thanks to the following institutions that provided feedback and participated in the fixes (as well as institutions that provided feedback during the process): [MoonShot AI, a.k.a. Kimi](https://www.moonshot.ai/) ， [Human Data](https://www.hud.so/), [OpenAI](https://openai.com/), [ByteDance Seed TARS](https://seed-tars.com/), [Anthropic](https://www.anthropic.com/), [Simular](https://www.simular.ai/), [HKU Data Intelligence Lab](https://sites.google.com/view/chaoh)

Special thanks to the following students who participated in the specific fixes: [Mengqi Yuan](https://yuanmengqi.github.io/), [Danyang Zhang](https://zdy023.github.io/), [Xinzhuang Xiong](https://thisisxxz.com/), [Zhennan Shen](https://scholar.google.com/citations?user=JPwg5MwAAAAJ&hl=en), [Zilong Zhou](https://github.com/adlsdztony), Yanxu Chen, [Jiaqi Deng](https://millank0817.github.io/), [Tianbao Xie](https://tianbaoxie.com/), Junda Chen, [Jixuan Chen](https://chenjix.github.io/), [Haoyuan Wu](https://www.linkedin.com/in/haoyuan-wu-240878291/).

Special thanks to the following students who participated in running the re-evaluation: [Mengqi Yuan](https://yuanmengqi.github.io/), [Zilong Zhou](https://github.com/adlsdztony), [Xinyuan Wang](https://xinyuanwangcs.github.io/), [Bowen Wang](https://bowenbryanwang.github.io/).

## Evaluation

### Local Evaluation

Please start by reading through the [agent interface](https://github.com/xlang-ai/OSWorld/blob/main/mm_agents/README.md) and the [environment interface](https://github.com/xlang-ai/OSWorld/blob/main/desktop_env/README.md). Correctly implement the agent interface and import your customized version in the `run.py` (for single-threaded execution) or `scripts/python/run_multienv.py` / `scripts/python/run_multienv_xxx.py` (for parallel execution) file. Afterward, you can execute a command similar to the one in the previous section to run the benchmark on your agent.

### Public Evaluation

If you want your results to be verified and displayed on the verified leaderboard, you need to schedule a meeting with us (current maintainer: [tianbaoxiexxx@gmail.com](mailto:tianbaoxiexxx@gmail.com), [yuanmengqi732@gmail.com](mailto:yuanmengqi732@gmail.com)) to run your agent code on our side and have us report the results. You need to upload and allow us to disclose your agent implementation under the OSWorld framework (you may choose not to expose your model API to the public), along with a report that allows the public to understand what’s happening behind the scenes. Alternatively, if you are from a trusted institution, you can share your monitoring data and trajectories with us. Please carefully follow the [Setup Guideline - Public Evaluation Platform](https://github.com/xlang-ai/OSWorld/blob/main/SETUP_GUIDELINE.md#3-public-evaluation-platform) to get results.

## FAQ

### What is the username and password for the virtual machines?

The username and password for the virtual machines are as follows (for provider `vmware`, `virtualbox` and `docker`): we set the account credentials for Ubuntu as `user` / `password`.
For cloud service providers like `aws`, to prevent attacks due to weak passwords, we default to `osworld-public-evaluation`.
If you make further modifications, remember to set the client\_password variable and pass it to DesktopEnv and Agent (if supported) when running experiments.
Some features like setting up proxy require the environment to have the client VM password to obtain sudo privileges, and for some OSWorld tasks, the agent needs the password to obtain sudo privileges to complete them.

### How to setup the account and credentials for Google and Google Drive?

See [Setup Guideline - Google Account Setup](https://github.com/xlang-ai/OSWorld/blob/main/SETUP_GUIDELINE.md#1-google-account-setup).

### What should I do if Google Drive tasks fail to initialize properly?

**OSWorld contains 8 Google Drive-related tasks** that may encounter setup issues during initialization due to various factors:

**Common Issues:**

- IP address changes causing authentication problems
- Network restrictions or firewalls
- Google API rate limiting or access restrictions
- Regional availability limitations
**Solutions:**
**Option 1 - Manual Configuration:** Manually troubleshoot and configure these 8 tasks to complete the full 369-task evaluation.
**Option 2 - Task Exclusion:** Exclude these 8 tasks and run the remaining **361 tasks** - this is **officially permitted and acceptable** for benchmark evaluation.

**Both approaches are valid for research comparison and leaderboard submission.** Please specify which approach you used when reporting your results.

### How can I configure a proxy for the VM (if I'm behind the GFW, or I don't want some of my tasks to be identified as bot and get lower scores)?

See [Setup Guideline - Proxy Configuration](https://github.com/xlang-ai/OSWorld/blob/main/SETUP_GUIDELINE.md#2-proxy-configuration).
We also provide a pre-configured solution based on DataImpulse, please refer to [proxy setup section](https://github.com/xlang-ai/OSWorld/blob/main/SETUP_GUIDELINE.md#23-proxy-for-specific-tasks-recommended).

## BibTeX

```
@misc{OSWorld,
      title={OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments},
      author={Tianbao Xie and Danyang Zhang and Jixuan Chen and Xiaochuan Li and Siheng Zhao and Ruisheng Cao and Toh Jing Hua and Zhoujun Cheng and Dongchan Shin and Fangyu Lei and Yitao Liu and Yiheng Xu and Shuyan Zhou and Silvio Savarese and Caiming Xiong and Victor Zhong and Tao Yu},
      year={2024},
      eprint={2404.07972},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```

---

## Links

- [https://www.xlang.ai/](https://www.xlang.ai/)
- [Spider](https://yale-lily.github.io/spider)
- [UnifiedSKG](https://github.com/HKUNLP/UnifiedSKG)
- [IC-DST](https://github.com/Yushi-Hu/IC-DST)
- [Selective Annotation](https://github.com/HKUNLP/icl-selective-annotation)
- [Binder](https://lm-code-binder.github.io/)
- [DS-1000](https://ds1000-code-gen.github.io/)
- [Instructor](https://instructor-embedding.github.io/)
- [Text2Reward](https://text-to-reward.github.io/)
- [OpenAgents](https://github.com/xlang-ai/OpenAgents)
- [Lemur-70B](https://github.com/OpenLemur/lemur)
- [ARKS](https://arks-codegen.github.io/)
- [BRIGHT](https://brightbenchmark.github.io/)
- [Spider2-V](https://spider2-v.github.io/)
- [Tianbao Xie](https://tianbaoxie.com)
- [Danyang Zhang](https://zdy023.github.io/)
- [Jixuan Chen](https://chenjix.github.io/)
- [Xiaochuan Li](https://xiaochuanli.com/)
- [Siheng Zhao](https://sihengz02.github.io/)
- [Ruisheng Cao](https://scholar.google.com/citations?user=NdK881sAAAAJ&hl=zh-CN)
- [Toh Jing Hua](https://me.tjh.sg/)
- [Zhoujun Cheng](https://blankcheng.github.io/)
- [Dongchan Shin](https://www.linkedin.com/in/dongchan-shin-2a4890275/?trk=public_profile_samename-profile&originalSubdomain=hk)
- [Fangyu Lei](https://lfy79001.github.io/)
- [Yitao Liu](https://yitaoliu17.com/)
- [Yiheng Xu](https://yihengxu.com/)
- [Shuyan Zhou](https://shuyanzhou.github.io/)
- [Silvio Savarese](https://cvgl.stanford.edu/silvio/)
- [Caiming Xiong](http://cmxiong.com/)
- [Victor Zhong](https://www.victorzhong.com/)
- [Tao Yu](https://taoyds.github.io/)
- [OSWorld 2.0](https://osworld-v2.xlang.ai/)
- [OSWorld-Verified](https://xlang.ai/blog/osworld-verified)
- [community-reported examples](https://docs.google.com/spreadsheets/d/19GSOVCtYM7j3V84Zl5QiaeiEtgK_NIvqtDVXEoVb4U0/edit?gid=0#gid=0)
- [Paper](https://arxiv.org/abs/2404.07972)
- [Code](https://github.com/xlang-ai/OSWorld)
- [Doc](https://timothyxxx.github.io/OSWorld/)
- [Data](https://github.com/xlang-ai/OSWorld/tree/main/evaluation_examples)
- [Data Viewer](https://osworld-v1.xlang.ai/explorer.html)
- [Slides](https://docs.google.com/presentation/d/1-r889Nb9n7SeZqrj-ryNqJLoMzp7aGNU2ihO8nUdEcE/edit?usp=sharing)
- [Twitter](https://twitter.com/TianbaoX/status/1778781521253667267)
- [Discord](https://discord.gg/4Gnw7eTEZR)
- [GAIA](https://huggingface.co/gaia-benchmark)
- [Mind2Web](https://osu-nlp-group.github.io/Mind2Web/)
- [WebLINX](https://mcgill-nlp.github.io/weblinx/)
- [PixelHelp](https://github.com/google-research/google-research/tree/master/seq2act)
- [MetaGUI](https://x-lance.github.io/META-GUI-Leaderboard/)
- [AitW](https://github.com/google-research/google-research/tree/master/android_in_the_wild)
- [OmniAct](https://huggingface.co/datasets/Writer/omniact)
- [ScreenAgent](https://github.com/niuzaisheng/ScreenAgent)

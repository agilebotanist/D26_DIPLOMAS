Scraping: https://arxiv.org/abs/2609.20812
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://arxiv.org/abs/2609.20812
  Settled (dom-quiet, 3560ms)
  Extracting content...
  Extracted 2696 characters

--- Content ---

## Computer Science > Software Engineering

## Title:Quantifying Overclaiming Propensity in Frontier LLM Agents

[View PDF](/pdf/2609.20812) [HTML (experimental)](https://arxiv.org/html/2609.20812v3)

> Abstract:Frontier coding agents are increasingly trusted to work autonomously for long periods of time, yet what they actually did is often hard to tell from their final response. We quantify the propensity of such agents to overclaim task completion, which may mislead the user. We operationalize overclaiming as a final response that reports work that the agent's own transcript shows it did not do, for example, claiming to have read a file it never opened. This criterion requires no inference about intent and does not depend on whether the delivered work is correct; it asks only whether the reported work was done. We introduce OverclaimBench, an evaluation suite of five file-review scenarios with transcript-based coverage measurements and registered planted defects. We evaluate eight proprietary frontier models in their own production command-line interfaces and four open-weight models under a single fixed harness, and find that 1) agents fail to read every file they were asked to review in 67.9% of runs; 2) among these incomplete runs, agents are misleading 80.4% of the time (59-96% per model), either falsely claiming a complete review or leaving the gap undisclosed; 3) requiring delegation to subagents increases coverage, but a large majority of reviews that remain incomplete are still misleading; and 4) agents that falsely claim a complete review miss planted defects at about 1.8 times the rate of agents that read every file, showing that claims of completion can conceal substantive failures. Together, these results show that agents' final responses are not reliable accounts of their actions.

| Comments: |  |
| --- | --- |
| Subjects: | Software Engineering (cs.SE); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) |
| Cite as: | [arXiv:2609.20812](https://arxiv.org/abs/2609.20812) \[cs.SE\] |
|  | (or [arXiv:2609.20812v3](https://arxiv.org/abs/2609.20812v3) \[cs.SE\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2609.20812](https://doi.org/10.48550/arXiv.2609.20812) |

## Submission history

From: Pascal Junior Tikeng Notsawo \[[view email](/show-email/2d862e52/2609.20812)\]
**[\[v1\]](/abs/2609.20812v1)** Thu, 17 Sep 2026 17:59:04 UTC (3,608 KB)
**[\[v2\]](/abs/2609.20812v2)** Mon, 21 Sep 2026 17:55:11 UTC (3,657 KB)
**\[v3\]** Tue, 22 Sep 2026 17:58:40 UTC (3,685 KB)

[Which authors of this paper are endorsers?](/auth/show-endorsers/2609.20812) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))

Scraping: https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
  Settled (dom-quiet, 1658ms)
  Extracting content...
  Extracted 9031 characters

--- Content ---

## 1\. AI crossed a threshold. It is now the primary author of code.

This did not happen as a deliberate decision by most organizations. It happened as AI tool adoption scaled, acceptance rates climbed, and agent-mode tools began applying changes directly rather than waiting for a developer to approve each suggestion. In the organizations we studied, 80% of teams now exceed the 50% weekly active user threshold for AI tools. The acceptance rate of AI-generated code has risen from 20% to 60%. AI is not assisting developers. In most organizations, it is leading them.

## 2\. The business value is real. Roadmaps are finally moving.

The 2026 AI engineering impact data is not all bad news, and it is important to say that clearly. [Epics](https://www.faros.ai/blog/software-engineering-glossary#epic) completed per developer are up 66%. [Task throughput](https://www.faros.ai/blog/software-engineering-glossary#throughput) per developer is up 33.7%. [PR merge rate](https://www.faros.ai/blog/software-engineering-glossary#pr-merge-rate) per developer is up 16.2%. These numbers represent real delivery acceleration: more features shipped, more initiatives completed, more code entering the codebase than at any prior point in our dataset. AI productivity gains at the business level are real, and engineering leaders are right to want more of them.

## 3\. But the throughput numbers have an asterisk.

Code churn, the [ratio of lines deleted to lines added for merged code in a given quarter](https://www.faros.ai/blog/software-engineering-glossary#code-deletion-ratio), has increased 861% under high AI adoption. At nearly 10 times the prior rate, significantly more code is being removed relative to what is being added. There are several plausible explanations: developers accepting AI-generated code quickly and returning to replace it when it proves insufficient in practice, AI enabling teams to finally tackle large-scale refactoring that was previously too slow or costly to staff, or engineers simply moving faster to improve code they were never fully satisfied with at the time of shipping.

All three are consistent with the data, and the right explanation likely varies by organization. Every organization should determine which one applies to them. With access to Git-level line provenance data, you can determine whether deleted lines were written recently, suggesting rework of AI-generated code, or whether they represent legacy code being productively refactored. Either way, a significant increase in this ratio warrants investigation. Throughput measures what was shipped, not what survived. The 861% is the asterisk on every output number in this report.

![Illustration of key findings from the Acceleration Whiplash, the AI Engineering Report 2026.](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69d6c7504900cabccb1e6570_AI%20Engineering%20Report%202026%20-%20Acceleration%20Whiplash%20-%20Key%20Findings.webp)

Illustration of key findings from the Acceleration Whiplash, the AI Engineering Report 2026.

## 5\. Bugs are accelerating, not stabilizing.

In our 2025 AI engineering report on [the AI Productivity Paradox](https://www.faros.ai/blog/ai-software-engineering), bugs per developer were up 9% as AI adoption grew. In this dataset, that figure has risen to 54%. The relationship between AI adoption and defect rate is not flattening as organizations mature their AI programs; it’s steepening. More AI-generated code in the codebase correlates with more [bugs](https://www.faros.ai/blog/software-engineering-glossary#bug) per developer, and that relationship is strengthening as adoption deepens.

## 6\. AI made it easy to start work. It did not make it easy to finish it.

Daily PR [contexts](https://www.faros.ai/blog/software-engineering-glossary#context-switching) per developer are up 67.4%. Work restarts, [tasks](https://www.faros.ai/blog/software-engineering-glossary#task) that return to in-progress after moving to another stage, are up 13.8%. 26% more in-progress tasks show no activity for seven or more days: work that was started, claimed capacity, and then stalled. The developer productivity picture that AI tools present at the individual level is one of acceleration. The workflow data tells a more complicated story: more threads opened, more work abandoned mid-flight, and a development environment where beginning is easy and finishing is hard.

## 7\. The most experienced people in your organization are being buried. We call it the senior engineer tax.

AI-generated code presents a specific and under-appreciated challenge for reviewers. It is often superficially convincing: idiomatic, well-named, stylistically consistent with the surrounding codebase. It looks like code written by someone who knows what they are doing. The structural and logical failures, when they exist, are beneath the surface. Catching them requires a reviewer to read carefully, reason about intent, and reconstruct the problem the code was meant to solve, rather than scanning for obvious errors. That is slow, expensive cognitive work, and the data reflects it. Median time to first PR review is up 156.6%. Average time spent in [code review](https://www.faros.ai/blog/software-engineering-glossary#code-review) is up 199.6%. Median time in review is up 441.5%. The engineers with the deepest knowledge of the system are spending their most valuable hours unraveling plausible-looking code that should never have reached them in the state it did.

## 9\. Strong engineering foundations do not protect you. Two years of telemetry says so.

[DORA's 2025 State of AI-Assisted Software Development report](https://dora.dev/research/2025/dora-report/) concludes, based on survey data, that strong engineering foundations amplify AI's benefits and offer protection against its downsides. Two years of telemetry data across thousands of teams tells a different story. High-performing engineering organizations, those with mature DevOps practices, high [DORA metrics](https://www.faros.ai/blog/all-you-need-to-know-about-the-dora-metrics-and-how-to-measure-them) scores, and disciplined delivery processes, are experiencing the same downstream deterioration as everyone else. Surveys capture how developers feel about their work. Right now, developers feel more productive because, at the individual level, they are. What surveys cannot capture is what happens downstream: the review queues backing up, the incidents accumulating, the bugs reaching customers that never should have passed review. Perception lags reality. Telemetry does not.

## 10\. Every organization cutting engineering headcount on the basis of AI output gains should read this report.

The AI engineering impact data shows that output is up. It also shows that the work required to ensure that [output is safe, correct, and maintainable](https://www.faros.ai/clara) has not decreased. It has increased substantially. The engineers being considered for cuts are in many cases the ones absorbing the quality gap AI is creating. What does the data actually imply for headcount decisions, for the engineers entering the workforce, and for the organizations betting their delivery capacity on AI output alone? The report has a direct answer. We will let it speak for itself.

## The organizations that can see this clearly are already ahead.

The findings in this report are not visible to most engineering organizations. They require granular, adaptable metrics drawn from the systems where work actually happens: version control, CI/CD pipelines, incident management, work management, and IDE telemetry. Not the dashboards that organizations have been looking at for years, but [metrics that can be sliced, correlated, and interrogated](https://www.faros.ai/copilot-module) as AI changes what engineering teams produce and how they produce it.

The organizations represented in this dataset already have that visibility. They can see where throughput is real and where it is hollow. They can see where review is failing, where incidents are clustering, and where senior engineer time is being consumed. That visibility is not a small advantage. It is the prerequisite for everything that comes next: the control, the guardrails, and the ability to push quality back to where it belongs, at the point of authorship, before the code ever reaches review.

[Token Intelligence](https://www.faros.ai/platform/token-intelligence) is where that visibility starts for AI spend specifically — every token classified, every dollar attributed, every tool evaluated on what it actually produced.

The gap between knowing and acting is the only gap that matters now.

*The AI Engineering Impact Report 2026: The Acceleration Whiplash draws on two years of telemetry data from 22,000 developers and more than 4,000 teams across the Faros platform, tracking metric change between each organization's periods of lowest and highest AI adoption.* [*Download the full report.*](https://www.faros.ai/research/ai-acceleration-whiplash)

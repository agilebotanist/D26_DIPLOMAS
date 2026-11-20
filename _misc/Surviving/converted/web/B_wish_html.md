Scraping: https://arxiv.org/html/2610.36346v1
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://arxiv.org/html/2610.36346v1
  Settled (dom-quiet, 1739ms)
  Extracting content...
  Extracted 84070 characters

--- Content ---

## Your Wish Is My Commit: Over-Compliant Refactoring in AI Coding Agents Thanks: \*Equal contribution.

Haocong Jiang <sup>1,*</sup>, Sadra Sabouri <sup>1,*</sup>, Sepand Haghighi <sup>2</sup>, Souti Chattopadhyay <sup>1</sup> Affiliation: <sup>1</sup> University of Southern California, Los Angeles, CA, USA
<sup>2</sup> Open Science Lab
{allenjia, sabourih, schattop}@usc.edu, sepand@openscilab.com Affiliation:

###### Abstract

Large language models are known to be sycophantic, over-complying with users even when doing so is unproductive. When these models act as coding agents, this can be costly: an agent that keeps editing after no edit improves the code writes churn, technical debt, and review burden into the codebase. Yet the consequences of sycophancy in software engineering remain largely understudied. To understand them, we run a controlled study of iterative refactoring, an open-ended task with no stopping criterion, where any edit an agent makes once the code is already clean reflects compliance rather than improvement. Across algorithmic (n=50) and object-oriented (n=10) suites, we repeatedly ask two widely used agents, Codex and Claude Code, to refactor further across five models. Over 3,000 turns, we define six behavioral signals of over-compliance. We hypothesized that a capable agent would stop once it recognized an optimized codebase; none did. Every model kept editing, rewriting up to 31x the original codebase before first stopping and resuming edits even after declaring the task complete. Over-compliance is a costly, multi-turn behavior that compounds with every turn, and our six signals give developers and tool builders a way to detect and curb it.

## I Introduction

Large language models often adapt to a user’s apparent preferences rather than to the task at hand. Prior work calls this *sycophancy*: models agree with stated views, praise weak arguments, and revise correct answers after pushback [^1] [^2] [^3]. The behavior appears across question answering, advice, and reasoning, which marks it as a property of how models are trained and aligned, not an artifact of any one prompt [^1] [^2] [^4]. A model that optimizes for approval over correctness reinforces mistaken assumptions, suppresses useful disagreement, and weakens the user’s reliance on its judgment [^5] [^6] [^7].

A coding agent is the same model placed in a development harness [^8] [^9]. Because sycophancy is a model-level behavior, it should carry over into software engineering, where developers now rely heavily on these models: a large majority already use or plan to use AI coding tools [^10] [^11]. A coding agent does not return text to read; it edits artifacts that are committed, reviewed, and maintained. An agent that keeps editing to fulfill the user’s wishes, after the edits stop improving the code, writes that compliance into the codebase as unnecessary code, technical debt, wasted generation, and added review burden [^12] [^13] [^14].

Two lines of work bear on this behavior but miss it. Studies on natural-language benchmarks show that sycophancy is real and systematic, but observe it only where the artifact is the model’s reply [^1] [^2] [^4]. Benchmarks for coding agents measure whether agents resolve issues and pass tests [^15] [^8] [^9], rewarding a correct change but never the absence of one. Whether coding agents are *over-compliant*, editing code to satisfy a request rather than improve it, remains unmeasured.

The process of refactoring uniquely isolates this behavior. A refactoring request is open-ended: “clean this up” admits many responses and rarely carries a stopping criterion [^16]. When further editing is no longer warranted, a calibrated agent should decline; any edit it then makes reflects compliance, not improvement. Such edits are not free: code churn is a known predictor of defects [^17], AI-assisted coding has been linked to rising churn and quality decline [^13], and larger changes are harder to review effectively [^18] [^19], with a deployed LLM reviewer shown to slow pull requests and introduce unnecessary corrections [^20] [^21]. This gap matters most for novice and vibe coders, who drive agents through natural-language prompts without a clear sense of where the refactoring boundary lies [^10] [^11].

We study iterative refactoring under these conditions and ask four questions. *RQ1: How many turns does an agent take to stop editing?* A calibrated agent completes refactoring after one warranted pass. *RQ2: How much code does it change before stopping?* The volume of unnecessary change measures the direct cost of this phenomenon. *RQ3: Once an agent stops, does it stay stopped?* Editing after stating that no change is needed is a stronger failure than stopping late, because the agent acts against its own stated judgment. *RQ4: What kind of changes do the extra turns produce?* Disciplined refactoring and incidental churn carry different maintenance costs.

To answer these questions, we run our experiments on two suites of controlled codebases: canonical solutions to algorithmic problems (n=50) and object-oriented Java from [^22] course assignments (n=10). We drive two widely used agents, Codex and Claude Code, across five models (GPT-5.4, GPT-5.4-mini, GPT-5.5, Claude Sonnet 4.6, and Claude Opus 4.8) through their command-line interfaces. At each of 10 turns, a simulated developer agent asks the coding agent to refactor further without naming a file, a target, or a reason, so any change between turns is the agent’s own choice. We record every line-level and structural change and define six signals, built on differences in lines and Code Structure Tree [^23], that turn “the agent kept editing” into measured quantities.

Our results show that over-compliant refactoring is not a rare case, but a persistent multi-turn behavior. Rather than reliably stopping when the code is already adequate, every model continues editing. The resulting changes produce substantial churn, introduce and remove structure across turns, and continued editing even after the agent indicates that no further refactoring is needed. These findings show that coding-agent sycophancy can manifest as operational compliance in code, not just agreement in language. By characterizing this behavior and measuring it with concrete signals, our work provides a basis for evaluating over-compliance in coding agents.

## II Formalization

We track agent behavior across turns from two complementary views. The line-level diff counts added and deleted lines between turns, providing an intuitive measure of churn. The structural view captures which program elements the agent adds, deletes, edits, and revisits. The first tells us how much the agent changes; the second tells us what it changes and whether those changes undo or recreate its own prior work.

On top of these two views, we define six behavioral signals that serve as proxies for over-compliance. Together, these signals quantify not only whether an agent continues to edit under repeated refactoring requests, but also how much it edits, which structural elements it revisits, and when it contradicts or recreates its own earlier changes.

Let $V_{0}$ be the initial code version handed to the agent, and let $V_{t}$ be the version produced after turn $t$, for $t=1,\ldots,T$. Across all $T$ turns, the agent is asked to keep refactoring without any new functional requirement, so any difference between $V_{t-1}$ and $V_{t}$ reflects the agent’s own choice.

For each transition $V_{t-1}\to V_{t}$, the diff reports $a_{t}$ added lines, $d_{t}$ deleted lines, and $e_{t}$ edited (in-place modified) lines. We summarize the size of a turn’s edit as $\Delta l_{t}=a_{t}+d_{t}+e_{t}$. To record whether a turn changed anything at all, and to compare codebases of different sizes, we define $f_{0}$ and $f_{1}$ as follows, normalizing each edit by $l_{0}=\text{LoC}(V_{0})$, the size of the starting codebase, to make $f_{1}$ comparable across codebases.

$$
f_{0}(t)=\begin{cases}0,&\Delta l_{t}=0,\\
1,&\Delta l_{t}>0,\end{cases}\qquad f_{1}(t)=\frac{\Delta l_{t}}{l_{0}}.
$$

A key event is the first turn at which the agent leaves the code unchanged, indicating task completion.

$$
t^{*}=\min\{t:f_{0}(t)=0\}.
$$

If the agent never produces a zero-change turn, we set $t^{*}=T$. The first three signals are defined around this convergence point.

### II-A Temporal Line-Change Signals

#### II-A1 S1 — Pre-Convergence Churn

Even an agent that eventually stops may rewrite far more than the task warrants on the way there. $S_{1}$ captures the total normalized churn the agent spends before it first stops:

$$
\boxed{\,S_{1}=\sum_{t=1}^{t^{*}}f_{1}(t)\,}
$$

Because $f_{1}$ is normalized, a value of $S_{1}=4.8$ means the agent rewrote the equivalent of $4.8$ times the original codebase before settling.

#### II-A2 S2 — Post-Convergence Modification

Reaching a no-change turn should mark completion. $S_{2}$ measures whether the agent resumes editing after convergence:

$$
\boxed{\,S_{2}=\sum_{t=t^{*}+1}^{T}f_{1}(t)\,}
$$

Any positive value indicates post-convergence editing, a direct sign of over-compliance.

### II-B Self-Consistency Signal

#### II-B1 S3 — Verbal-Refusal Edit Rate

Stopping late and editing too much are failures of restraint; editing in the *same turn* the agent states it has nothing to do is a failure of consistency. Let $D_{t}\in\{0,1\}$ indicate that the agent’s reply at turn $t$ contains stop-claim language under the keyword classifier of Section III-E. $S_{3}$ is the fraction of stop-claiming turns in which the agent nonetheless makes a non-zero code change:

$$
\boxed{\,S_{3}=\frac{\sum_{t=1}^{T}D_{t}\cdot\mathbf{1}[\Delta l_{t}>0]}{\sum_{t=1}^{T}D_{t}}\,}
$$

A value of $S_{3}=1$ means the agent accompanied every edit it made with a statement that no edit was needed.

### II-C Structural Representation via the CST

Line counts cannot reveal whether deleted code later reappears or whether the same method is repeatedly edited. We therefore use a structural view based on RefDiff 2.0.0 [^23], adapting only its surrounding driver for our multi-turn setting.

RefDiff parses each version into a Code Structure Tree (CST), a language-independent model whose nodes are the coarse-grained, named code elements of a program. For Java these are classes, interfaces, enums, and methods; local variables and statements are left out as too fine-grained for a refactor. Let $N_{t}$ be the set of CST nodes present in $V_{t}$. Each node has a canonical identity given by its type, qualified name, and signature, so the same method keeps its identity across versions and set operations on $N_{t}$ are well defined.

<svg id="S2.F1.pic1" height="226.08" overflow="visible" version="1.1" viewBox="0 0 451.04 226.08" width="451.04"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" stroke-width="0.4pt" transform="translate(0,226.08) matrix(1 0 0 -1 0 0) translate(4.43,0) translate(0,194.39)"><g style="--ltx-stroke-color:#B3B3B3;" stroke="#B3B3B3"><path style="fill:none" d="M 179.11 -8.34 L 0 -8.34 C -2.29 -8.34 -4.15 -10.2 -4.15 -12.49 L -4.15 -105.62 C -4.15 -107.91 -2.29 -109.77 0 -109.77 L 179.11 -109.77 C 181.41 -109.77 183.26 -107.91 183.26 -105.62 L 183.26 -12.49 C 183.26 -10.2 181.41 -8.34 179.11 -8.34 Z M -4.15 -109.77"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 0 -59.06)"></g><g style="--ltx-stroke-color:#B3B3B3;" stroke="#B3B3B3"><path style="fill:none" d="M 442.18 -8.34 L 259.84 -8.34 C 257.55 -8.34 255.69 -10.2 255.69 -12.49 L 255.69 -164.68 C 255.69 -166.97 257.55 -168.83 259.84 -168.83 L 442.18 -168.83 C 444.48 -168.83 446.33 -166.97 446.33 -164.68 L 446.33 -12.49 C 446.33 -10.2 444.48 -8.34 442.18 -8.34 Z M 255.69 -168.83"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 259.84 -88.58)"></g><g style="--ltx-stroke-color:#990000;--ltx-fill-color:#FFE8E8;" fill="#FFE8E8" stroke="#990000" stroke-dasharray="3.0pt,3.0pt" stroke-dashoffset="0.0pt"><path d="M 179.11 -29.41 L 0 -29.41 C -1.53 -29.41 -2.77 -30.65 -2.77 -32.17 L -2.77 -85.94 C -2.77 -87.46 -1.53 -88.7 0 -88.7 L 179.11 -88.7 C 180.64 -88.7 181.88 -87.46 181.88 -85.94 L 181.88 -32.17 C 181.88 -30.65 180.64 -29.41 179.11 -29.41 Z M -2.77 -88.7"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" stroke-dasharray="3.0pt,3.0pt" stroke-dashoffset="0.0pt" transform="matrix(1.0 0.0 0.0 1.0 0 -59.06)"></g><g style="--ltx-stroke-color:#008C00;--ltx-fill-color:#E6FFE6;" fill="#E6FFE6" stroke="#008C00"><path d="M 442.18 -29.41 L 259.84 -29.41 C 258.31 -29.41 257.08 -30.65 257.08 -32.17 L 257.08 -85.94 C 257.08 -87.46 258.31 -88.7 259.84 -88.7 L 442.18 -88.7 C 443.71 -88.7 444.95 -87.46 444.95 -85.94 L 444.95 -32.17 C 444.95 -30.65 443.71 -29.41 442.18 -29.41 Z M 257.08 -88.7"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 259.84 -59.06)"></g><g style="--ltx-stroke-color:#008C00;--ltx-fill-color:#E6FFE6;" fill="#E6FFE6" stroke="#008C00"><path d="M 437.11 -88.46 L 259.84 -88.46 C 258.31 -88.46 257.08 -89.7 257.08 -91.23 L 257.08 -144.99 C 257.08 -146.52 258.31 -147.76 259.84 -147.76 L 437.11 -147.76 C 438.64 -147.76 439.88 -146.52 439.88 -144.99 L 439.88 -91.23 C 439.88 -89.7 438.64 -88.46 437.11 -88.46 Z M 257.08 -147.76"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 259.84 -118.11)"></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 2.35 -1.88)"><foreignObject style="--ltx-fo-width:8em;--ltx-fo-height:0.58em;--ltx-fo-depth:0.21em;font-size:7.35pt;" height="8.07" overflow="visible" transform="matrix(1 0 0 -1 0 5.92)" width="81.36"><span id="S2.F1.pic1.6" style="font-size:70%;">package my.calc;</span></foreignObject></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 2.35 -22.11)"><foreignObject style="--ltx-fo-width:9.06em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="92.12"><span id="S2.F1.pic1.7" style="font-size:70%;">class Calculator {</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 2.35 -41.79)"><foreignObject style="--ltx-fo-width:17.48em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="177.81"><span id="S2.F1.pic1.8" style="font-size:70%;">double <span id="S2.F1.pic1.8.1">sum</span> (double a, double b) {</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 2.35 -61.34)"><foreignObject style="--ltx-fo-width:8.5em;--ltx-fo-height:0.58em;--ltx-fo-depth:0.13em;font-size:7.35pt;" height="7.26" overflow="visible" transform="matrix(1 0 0 -1 0 5.92)" width="86.45"><span id="S2.F1.pic1.9" style="font-size:70%;">return a + b;</span></foreignObject></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 2.35 -81.16)"><foreignObject style="--ltx-fo-width:1.56em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="15.84"> <span id="S2.F1.pic1.10" style="font-size:70%;">}</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 2.35 -100.85)"><foreignObject style="--ltx-fo-width:0.56em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="5.67"><span id="S2.F1.pic1.11" style="font-size:70%;">}</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -1.88)"><foreignObject style="--ltx-fo-width:8em;--ltx-fo-height:0.58em;--ltx-fo-depth:0.21em;font-size:7.35pt;" height="8.07" overflow="visible" transform="matrix(1 0 0 -1 0 5.92)" width="81.36"><span id="S2.F1.pic1.12" style="font-size:70%;">package my.calc;</span></foreignObject></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -22.11)"><foreignObject style="--ltx-fo-width:9.06em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="92.12"><span id="S2.F1.pic1.13" style="font-size:70%;">class Calculator {</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -41.79)"><foreignObject style="--ltx-fo-width:17.8em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="181.03"><span id="S2.F1.pic1.14" style="font-size:70%;">double <span id="S2.F1.pic1.14.1" style="--ltx-fg-color:#D96C00;">total</span> (double a, double b) {</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -61.75)"><foreignObject style="--ltx-fo-width:10.74em;--ltx-fo-height:0.66em;--ltx-fo-depth:0.13em;font-size:7.35pt;" height="8.07" overflow="visible" transform="matrix(1 0 0 -1 0 6.73)" width="109.27"><span id="S2.F1.pic1.15" style="font-size:70%;">return <span id="S2.F1.pic1.15.1" style="--ltx-fg-color:#800080;">add</span> (a, b);</span></foreignObject></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -81.16)"><foreignObject style="--ltx-fo-width:1.56em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="15.84"> <span id="S2.F1.pic1.16" style="font-size:70%;">}</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -100.85)"><foreignObject style="--ltx-fo-width:17.3em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="175.96"><span id="S2.F1.pic1.17" style="font-size:70%;">double <span id="S2.F1.pic1.17.1" style="--ltx-fg-color:#800080;">add</span> (double a, double b) {</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -120.4)"><foreignObject style="--ltx-fo-width:8.5em;--ltx-fo-height:0.58em;--ltx-fo-depth:0.13em;font-size:7.35pt;" height="7.26" overflow="visible" transform="matrix(1 0 0 -1 0 5.92)" width="86.45"><span id="S2.F1.pic1.18" style="font-size:70%;">return a + b;</span></foreignObject></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -140.22)"><foreignObject style="--ltx-fo-width:1.56em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="15.84"> <span id="S2.F1.pic1.19" style="font-size:70%;">}</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 262.2 -159.9)"><foreignObject style="--ltx-fo-width:0.56em;--ltx-fo-height:0.71em;--ltx-fo-depth:0.24em;font-size:7.35pt;" height="9.69" overflow="visible" transform="matrix(1 0 0 -1 0 7.26)" width="5.67"><span id="S2.F1.pic1.20" style="font-size:70%;">}</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 93.97 18.57)"><foreignObject style="--ltx-fo-width:1.88em;--ltx-fo-height:0.66em;--ltx-fo-depth:0.11em;font-size:9.25pt;" height="9.89" overflow="visible" transform="matrix(1 0 0 -1 0 8.51)" width="24.12"><math data-latex="V_{t-1}" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi mathsize="0.900em">V</mi> <mrow><mi mathsize="0.900em">t</mi> <mo mathsize="0.900em">−</mo> <mn mathsize="0.900em">1</mn></mrow></msub> <annotation encoding="application/x-tex">V_{t-1}</annotation></semantics></math></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 370.1 18.57)"><foreignObject style="--ltx-fo-width:1.18em;--ltx-fo-height:0.66em;--ltx-fo-depth:0.11em;font-size:9.25pt;" height="9.89" overflow="visible" transform="matrix(1 0 0 -1 0 8.51)" width="15.16"><math data-latex="V_{t}" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi mathsize="0.900em">V</mi> <mi mathsize="0.900em">t</mi></msub> <annotation encoding="application/x-tex">V_{t}</annotation></semantics></math></foreignObject></g> <g stroke-width="0.8pt"><g style="--ltx-stroke-color:#0000A6;--ltx-fill-color:#0000A6;--ltx-fg-color:#0000A6;" color="#0000A6" fill="#0000A6" stroke="#0000A6"><path style="fill:none" d="M 183.54 -8.06 L 248.09 -8.06"></path></g><g style="--ltx-stroke-color:#0000A6;--ltx-fill-color:#0000A6;--ltx-fg-color:#0000A6;" color="#0000A6" fill="#0000A6" stroke="#0000A6" stroke-dasharray="none" stroke-dashoffset="0.0pt" stroke-linejoin="miter" transform="matrix(1.0 0.0 0.0 1.0 248.09 -8.06)"><path d="M 5.11 0 C 4.48 0.15 1.72 1.03 0 1.99 L 0 -1.99 C 1.72 -1.03 4.48 -0.15 5.11 0 Z"></path></g><g style="--ltx-fill-color:#FFFFFF;" fill="#FFFFFF"><path style="stroke:none" d="M 204.7 -12.73 h 29.55 v 9.33 h -29.55 Z"></path></g><g style="--ltx-stroke-color:#0000A6;--ltx-fill-color:#0000A6;" fill="#0000A6" stroke="#0000A6" transform="matrix(1.0 0.0 0.0 1.0 206.09 -11.35)"><foreignObject style="--ltx-fo-width:2.29em;--ltx-fo-height:0.56em;--ltx-fo-depth:0em;font-size:8.44pt;" height="6.57" overflow="visible" transform="matrix(1 0 0 -1 0 6.57)" width="26.78"><span id="S2.F1.pic1.21" style="font-size:70%;--ltx-fg-color:#0000A6;">Same</span></foreignObject></g></g> <g stroke-width="0.8pt"><g style="--ltx-stroke-color:#D96C00;--ltx-fill-color:#D96C00;--ltx-fg-color:#D96C00;" color="#D96C00" fill="#D96C00" stroke="#D96C00"><path style="fill:none" d="M 182.16 -59.06 L 249.48 -59.06"></path></g><g style="--ltx-stroke-color:#D96C00;--ltx-fill-color:#D96C00;--ltx-fg-color:#D96C00;" color="#D96C00" fill="#D96C00" stroke="#D96C00" stroke-dasharray="none" stroke-dashoffset="0.0pt" stroke-linejoin="miter" transform="matrix(1.0 0.0 0.0 1.0 249.48 -59.06)"><path d="M 5.11 0 C 4.48 0.15 1.72 1.03 0 1.99 L 0 -1.99 C 1.72 -1.03 4.48 -0.15 5.11 0 Z"></path></g><g style="--ltx-fill-color:#FFFFFF;" fill="#FFFFFF"><path style="stroke:none" d="M 198.22 -63.72 h 42.51 v 9.33 h -42.51 Z"></path></g><g style="--ltx-stroke-color:#D96C00;--ltx-fill-color:#D96C00;" fill="#D96C00" stroke="#D96C00" transform="matrix(1.0 0.0 0.0 1.0 199.61 -62.34)"><foreignObject style="--ltx-fo-width:3.45em;--ltx-fo-height:0.56em;--ltx-fo-depth:0em;font-size:8.44pt;" height="6.57" overflow="visible" transform="matrix(1 0 0 -1 0 6.57)" width="40.31"><span id="S2.F1.pic1.22" style="font-size:70%;--ltx-fg-color:#D96C00;">Rename</span></foreignObject></g></g> <g stroke-width="0.8pt"><g style="--ltx-stroke-color:#800080;--ltx-fill-color:#800080;--ltx-fg-color:#800080;" color="#800080" fill="#800080" stroke="#800080"><path style="fill:none" d="M 182.16 -88.98 C 208.9 -105.25 226.11 -111.97 249.62 -116.67"></path></g><g style="--ltx-stroke-color:#800080;--ltx-fill-color:#800080;--ltx-fg-color:#800080;" color="#800080" fill="#800080" stroke="#800080" stroke-dasharray="none" stroke-dashoffset="0.0pt" stroke-linejoin="miter" transform="matrix(0.98055 -0.19629 0.19629 0.98055 249.62 -116.67)"><path d="M 5.11 0 C 4.48 0.15 1.72 1.03 0 1.99 L 0 -1.99 C 1.72 -1.03 4.48 -0.15 5.11 0 Z"></path></g><g style="--ltx-fill-color:#FFFFFF;" fill="#FFFFFF"><path style="stroke:none" d="M 198.59 -112.01 h 38.82 v 9.33 h -38.82 Z"></path></g><g style="--ltx-stroke-color:#800080;--ltx-fill-color:#800080;" fill="#800080" stroke="#800080" transform="matrix(1.0 0.0 0.0 1.0 199.97 -110.63)"><foreignObject style="--ltx-fo-width:3.13em;--ltx-fo-height:0.56em;--ltx-fo-depth:0em;font-size:8.44pt;" height="6.57" overflow="visible" transform="matrix(1 0 0 -1 0 6.57)" width="36.62"><span id="S2.F1.pic1.23" style="font-size:70%;--ltx-fg-color:#800080;">Extract</span></foreignObject></g></g> <g style="--ltx-stroke-color:#990000;--ltx-fill-color:#FFE8E8;" fill="#FFE8E8" stroke="#990000" stroke-dasharray="3.0pt,3.0pt" stroke-dashoffset="0.0pt"><path d="M 20.85 -123.62 L 6.7 -123.62 C 5.18 -123.62 3.94 -124.86 3.94 -126.39 L 3.94 -133.45 C 3.94 -134.98 5.18 -136.22 6.7 -136.22 L 20.85 -136.22 C 22.38 -136.22 23.62 -134.98 23.62 -133.45 L 23.62 -126.39 C 23.62 -124.86 22.38 -123.62 20.85 -123.62 Z M 3.94 -136.22"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 28.79 -133.38)"><foreignObject style="--ltx-fo-width:9.16em;--ltx-fo-height:0.94em;--ltx-fo-depth:0.31em;font-size:7.97pt;" height="13.84" overflow="visible" transform="matrix(1 0 0 -1 0 10.38)" width="101.07"><math data-latex="N^{-}_{t}=\{\texttt{sum}\}" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msubsup><mi mathsize="0.700em">N</mi> <mi mathsize="0.700em">t</mi> <mo mathsize="0.700em">−</mo></msubsup> <mo mathsize="0.700em">=</mo> <mrow><mo stretchy="false">{</mo> <mtext mathsize="0.700em">sum</mtext> <mo stretchy="false">}</mo></mrow></mrow> <annotation encoding="application/x-tex">N^{-}_{t}=\{\texttt{sum}\}</annotation></semantics></math> <span id="S2.F1.pic1.24" style="font-size:70%;">(deleted)</span></foreignObject></g> <g style="--ltx-stroke-color:#008C00;--ltx-fill-color:#E6FFE6;" fill="#E6FFE6" stroke="#008C00"><path d="M 20.85 -147.24 L 6.7 -147.24 C 5.18 -147.24 3.94 -148.48 3.94 -150.01 L 3.94 -157.07 C 3.94 -158.6 5.18 -159.84 6.7 -159.84 L 20.85 -159.84 C 22.38 -159.84 23.62 -158.6 23.62 -157.07 L 23.62 -150.01 C 23.62 -148.48 22.38 -147.24 20.85 -147.24 Z M 3.94 -159.84"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 28.79 -157)"><foreignObject style="--ltx-fo-width:11.49em;--ltx-fo-height:0.94em;--ltx-fo-depth:0.31em;font-size:7.97pt;" height="13.84" overflow="visible" transform="matrix(1 0 0 -1 0 10.38)" width="126.79"><math data-latex="N^{+}_{t}=\{\texttt{total},\texttt{add}\}" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msubsup><mi mathsize="0.700em">N</mi> <mi mathsize="0.700em">t</mi> <mo mathsize="0.700em">+</mo></msubsup> <mo mathsize="0.700em">=</mo> <mrow><mo stretchy="false">{</mo> <mtext mathsize="0.700em">total</mtext><mo mathsize="0.700em">,</mo><mtext mathsize="0.700em">add</mtext> <mo stretchy="false">}</mo></mrow></mrow> <annotation encoding="application/x-tex">N^{+}_{t}=\{\texttt{total},\texttt{add}\}</annotation></semantics></math> <span id="S2.F1.pic1.25" style="font-size:70%;">(added)</span></foreignObject></g> <g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" fill="#000000" stroke="#000000" transform="matrix(1.0 0.0 0.0 1.0 8.83 -187.89)"><g transform="matrix(1 0 0 -1 0 17.34)"><g transform="matrix(1 0 0 1 0 6.62)"><g transform="matrix(1 0 0 -1 0 0)"><foreignObject style="--ltx-fo-width:12.01em;--ltx-fo-height:0.6em;--ltx-fo-depth:0.17em;font-size:7.97pt;" height="8.5" overflow="visible" transform="matrix(1 0 0 -1 0 6.62)" width="132.5"><math data-latex="R_{t}" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi mathsize="0.700em">R</mi> <mi mathsize="0.700em">t</mi></msub> <annotation encoding="application/x-tex">R_{t}</annotation></semantics></math><span id="S2.F1.pic1.26" style="font-size:70%;">:</span> <span id="S2.F1.pic1.27" style="font-size:70%;--ltx-fg-color:#0000A6;">Same</span><span id="S2.F1.pic1.28" style="font-size:70%;">,</span> <span id="S2.F1.pic1.29" style="font-size:70%;--ltx-fg-color:#D96C00;">Rename</span><span id="S2.F1.pic1.30" style="font-size:70%;">,</span> <span id="S2.F1.pic1.31" style="font-size:70%;--ltx-fg-color:#800080;">Extract</span></foreignObject></g></g> <g transform="matrix(1 0 0 1 0 15.46)"><g transform="matrix(1 0 0 -1 0 0)"><foreignObject style="--ltx-fo-width:9.2em;--ltx-fo-height:0.61em;--ltx-fo-depth:0.17em;font-size:7.97pt;" height="8.61" overflow="visible" transform="matrix(1 0 0 -1 0 6.73)" width="101.51"><span id="S2.F1.pic1.32" style="font-size:70%;">relationships linking</span> <math data-latex="N_{t-1}\!\to\!N_{t}" display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi mathsize="0.700em">N</mi> <mrow><mi mathsize="0.700em">t</mi> <mo mathsize="0.700em">−</mo> <mn mathsize="0.700em">1</mn></mrow></msub> <mo lspace="0.158em" mathsize="0.700em" rspace="0.158em" stretchy="false">→</mo> <msub><mi mathsize="0.700em">N</mi> <mi mathsize="0.700em">t</mi></msub></mrow> <annotation encoding="application/x-tex">N_{t-1}\!\to\!N_{t}</annotation></semantics></math></foreignObject></g></g></g></g></g></svg>

Fig. 1: One refactoring turn on RefDiff’s Calculator example, shown as a side-by-side diff with the CST annotated on the code. Each box is a CST node; nesting reflects the class containing its methods. The agent renames sum to total and extracts the addition into a new add method, giving $N^{+}_{t}=\{\texttt{total},\texttt{add}\}$ (green) and $N^{-}_{t}=\{\texttt{sum}\}$ (red). RefDiff’s relationship set $R_{t}$ then links nodes across versions (*Same*, *Rename*, *Extract*): by identity alone sum looks deleted, but $R_{t}$ reveals it was renamed to total rather than discarded.

For each transition $V_{t-1}\to V_{t}$ we form the added and deleted node sets $N^{+}_{t}=N_{t}\setminus N_{t-1}$ and $N^{-}_{t}=N_{t-1}\setminus N_{t}$. In Figure 1, the agent renames sum to total and extracts a new add method, so by identity alone $N^{+}_{t}=\{\texttt{total},\texttt{add}\}$ and $N^{-}_{t}=\{\texttt{sum}\}$. RefDiff also produces a relationship set $R_{t}\subseteq N_{t-1}\times N_{t}$ that links a node in $V_{t-1}$ to its counterpart in $V_{t}$, which is what tells us sum was renamed to total rather than discarded. From $R_{t}$ we read the *touched* nodes, those present on both sides of the transition but modified during the turn:

$$
X_{t}=\{\,v\in N_{t}:\exists\,u\text{ with }(u,v)\in R_{t}\,\}.
$$

To separate real edits from nodes that merely persist, we compare the normalized source text of each matched pair, and count a node as touched only when its body changes.

Finally, because rollbacks and reappearances span more than a single transition, we also compare non-adjacent snapshots, linking a node deleted at one turn to its later reincarnation, even when it returns under a different name or signature.

### II-D Structural Node Signals

#### II-D1 S4 — Feature Rollback/Removal

If the agent adds a code element and then removes it, the addition was never needed. $S_{4}$ counts how many agent-created nodes are later deleted across the run:

$$
\boxed{\,S_{4}=\sum_{t=1}^{T}\big|N^{-}_{t}\setminus N_{0}\big|\,}
$$

Therefore $S_{4}>0$ iff some node the agent introduced was later removed.

#### II-D2 S5 — Reimplementation Loop

An agent can go even further than rolling a change back: it can delete a node and then bring it back, leaving a present-absent-present trail across turns. Over the node universe $\mathcal{U}=\bigcup_{t=1}^{T}N_{t}$, $S_{5}$ counts the elements that follow this pattern:

$$
\boxed{\,S_{5}=\sum_{n\in\mathcal{U}}\mathbf{1}\big\{\,\exists\,i<j<k:n\in N_{i}\land n\notin N_{j}\land n\in N_{k}\,\big\}\,}
$$

A positive value means the agent deleted a code element and later reintroduced it, redoing work it had already undone. The definition applies to both original and agent-created nodes.

#### II-D3 S6 — Patch-Region Recurrence

An agent that keeps returning to the same code is not converging on it. Let the changed-node set at turn $t$ collect everything the turn altered,

$$
C_{t}=N^{+}_{t}\cup N^{-}_{t}\cup X_{t},
$$

and let $H_{t-1}=\bigcup_{i=1}^{t-1}C_{i}$ be the nodes changed before turn $t$. The fraction of a turn’s edits that land on already-touched nodes is

$$
\rho_{t}=\begin{cases}\dfrac{|C_{t}\cap H_{t-1}|}{|C_{t}|},&|C_{t}|>0,\\[8.99994pt]
0,&|C_{t}|=0,\end{cases}
$$

and $S_{6}$ averages this recurrence over the run ($T\geq 2$):

$$
\boxed{\,S_{6}=\frac{1}{T-1}\sum_{t=2}^{T}\rho_{t}\,}
$$

A high value means later edits repeatedly revisit code the agent already changed.

## III Method

We fix $T=10$ turns, hand each agent a codebase, and at every turn ask it to refactor through a simulated user agent. Refactoring has no built-in stopping point, and knowing when to stop is an experience a novice lacks. The fast-growing population of “vibe coders”—people who direct an agent in natural language without reading the diff closely—cannot tell an already-optimal codebase from one that still needs work, so they keep asking While the agent keeps complying, the blind lead the blind. We simulate this user type because it resembles a worst-case scenario, where neither party holds the boundary, and over-compliance does the most damage. Our aim is not to reproduce a typical session but to expose this shortcoming under a deliberately demanding, semi-adversarial user that a robust agent should be able to withstand.

### III-A Experimental Protocol

Each run is a multi-turn session driven through the agent’s command-line interface. After the first turn, each subsequent turn resumes the same session, preserving the agent’s conversation history, prior edits, and explanations. The simulated developer is initialized with the baseline snapshot $V_{0}$ and a system prompt (provided in supplementary materials [^24]) that forbids it from specifying what to change, where, why, or how; it may only ask for further refactoring. Any difference between $V_{t-1}$ and $V_{t}$ is therefore the coding agent’s own decision to keep modifying the code. Each codebase lives on its own isolated branch and worktree, so the agent sees only the target project, and the $T$ turns are committed in sequence to yield $V_{0},V_{1},\ldots,V_{10}$.

### III-B Datasets

We use two families of minimal code that leave little room for meaningful refactoring, so additional edits largely amount to over-editing.

##### Algorithmic problems

The first benchmark family consists of 50 data structures and algorithms, randomly drawn from [^25], along with their implementations in the GeeksforGeeks reference solutions [^26]. The subjects cover common algorithmic topics, including searching and sorting, graph traversal and shortest paths, dynamic programming, balanced trees, hashing, string matching, and number theory. Each subject is a single self-contained Java file, intentionally small and already clean, ranging from 13 to 229 lines.

##### Object-oriented academic code

The second family is object-oriented Java student coursework drawn from the Menagerie corpus of graded assignment submissions [^22]. From this corpus, we select the 10 highest-graded submissions from the most recent years; each is a complete, multi-class, multi-method program (roughly 16–34 source files) that complements the algorithmic set with realistic object-oriented structure. Two authors manually inspected the selected submissions to ensure their diversity and quality.

### III-C Agents and Models

We study the two coding agents in widest use, Codex and Claude Code, driving them through their command-line interfaces so that each turn is a real agent session rather than a bare model call. Across the two agents we cover five models: GPT-5.4, GPT-5.4-mini, and GPT-5.5 through Codex, and Claude Opus 4.8 and Claude Sonnet 4.6 through Claude Code. We set the reasoning effort to high for all five models.

### III-D Software Quality Metrics

We measure codebase quality at the initial state and after every iteration of each run. We compute these metrics using two static-analysis engines. SonarQube Community Build 25.1 (SonarJava 8.8, run on Java 17 via SonarScanner 8.1) provides cyclomatic and cognitive complexity, code smells, duplication density, the SQALE maintainability rating, and the technical-debt ratio. CK 0.7.0 provides class-level coupling between objects (CBO) and per-method cyclomatic complexity.

Most quality improvement occurs in the first turn. Across branches, cognitive complexity, code smells, and technical-debt ratio all drop sharply after the first pass, while later turns provide only marginal additional gains (Fig. 2). At the branch level, the first turn accounts for most of the net baseline-to-final improvement, and all models reach SonarQube’s highest maintainability rating. Thus, the code is already near the best quality level the agent will achieve after one pass. Editing nevertheless continues after these quality metrics plateau. Later turns add code and increase coupling without corresponding quality gains.

Fig. 2: Quality metrics vs. editing turn, per branch and model. Cognitive complexity, code smells, and technical debt drop sharply after the first turn and then plateau, while coupling (CBO) continues to rise as editing continues, indicating that most improvement occurs in one pass, and later turns add code without quality gains.

### III-E Stopping Mechanism

We treat a turn as a *stop* when the agent finishes successfully and writes zero net lines: $\Delta l_{t}=0$ with an empty diff. For each stop turn, we extracted the agent’s reasoning trace and its reply to the user. Two authors went through two rounds of collaborative qualitative coding [^27] and observed that three main categories emerged: *Refusal* is an explicit decline to act. *Optimum-awareness* claims the code is already optimum. *Questioning* redirects the request to the user and asks for a concrete goal before proceeding. These labels are not mutually exclusive: a single turn may refuse, cite code quality, and ask for a goal. Table I summarizes the three categories, giving a representative matched fragment and its frequency for each. We report the full per-category prevalence in Section IV.

TABLE I: AI Agent Stopping Communication taxonomy

| Category | Definition | Example | Count (%) |
| --- | --- | --- | --- |
| Refusal | An explicit decline to act. | *“… I’m not going to refactor this again …”* | 378 (83.3%) |
| Optimum-awareness | Claims the code is already as good as it should be and that further edits would be churn. | *“… The code is already well-refactored …”* | 214 (47.1%) |
| Questioning | Redirects the request to the user and asks for a concrete goal before proceeding. | *“… If you have a concrete goal, share it.”* | 275 (60.6%) |

To apply the taxonomy at scale, we built a keyword detector using case-insensitive regular expressions for each category. A turn receives a label when any pattern for that category matches the agent reasoning or output message. We seeded the patterns from observed stop turns and tuned them on the algorithm suite against 0 line changes turn. The initial detector achieved high recall ($0.993$) but low precision ($0.340$), producing 836 false positives for having generic phrases. Removing these patterns improved precision with little recall loss; on all 3,000 turns, the final detector flags 430 of the 454 stop turns, achieves precision $0.720$, recall $0.947$, $F_{1}=0.818$, and accuracy $0.936$. We favor high recall because the detector feeds $S_{3}$: if a stop claim is missed, the corresponding reasoning–action mismatch cannot be detected.

### III-F Ablation Studies

To test whether our findings depend on specific design choices, we conduct three ablations, each varying one factor while holding the others fixed: reasoning effort, prompt style, and codebase scale. We summarize the outcomes here and give full setups and results in the supplementary material [^24].

*Reasoning Effort.* This ablation tests whether over-compliance depends on the agent’s deliberation budget. Holding the simulated developer, task protocol, interaction length, and measured signals fixed, we vary only the agent’s effort setting, running GPT-5.5 on the Java binary-search subject with ten replicas at each level (none, low, medium, high, xhigh). The same pattern appears across the sweep: the agent produces substantial edits instead of stopping, with higher effort producing more feature rollback and reimplementation. Over-compliance is thus not simply a consequence of insufficient reasoning.

*Simulated Developer System Prompt Variation.* This ablation tests whether over-compliance depends on how the developer formulates the request. Keeping the protocol and target codebase fixed, we vary the prompting regime across three settings: a minimal static prompt, refactor; the novice developer used in the main experiment; and a simulated expert developer issuing concrete refactoring directions, using real-world prompt patterns from developers with more than five years of experience. Under the static prompt, agents are often uncertain about the user’s intent, with some recognizing the interaction as a coding test environment, which motivates the LLM-based simulated developer. Under the expert-style prompt, pre-stop churn increases rather than decreases, and rollback becomes more pronounced. Over-compliance is thus not an artifact of one novice formulation; it persists when the request appears more realistic and actionable.

*Codebase Scale.* This ablation tests whether the behavior is specific to small programs. Keeping the protocol and 10-turn horizon fixed, we replace the benchmark subjects with four large open-source Java repositories from the GitHub top-100 by stars: DBeaver, Elasticsearch, Guava, Spring Boot, and Termux, spanning tens to hundreds of thousands of lines across thousands of files. The core pattern persists: agents continue editing across turns, edits remain large, and fragile stopping reappears. Although the normalized edit proportion is smaller relative to repository size, single turns still introduce changes on the order of thousands of lines. Over-compliance is thus not limited to small benchmarks; it also appears in production-scale repositories where refactoring is more open-ended and a clear completion point is harder to establish.

Across all three ablations, the conclusion is consistent: increasing reasoning effort, changing the simulated user, and scaling to larger codebases do not remove the tendency to continue editing code that warrants no further change.

## IV Results

### IV-A How Many Turns for Agents to Stop Refactoring?

Fig. 3: Distribution of the first-stop turn $t^{*}$. For each run, $t^{*}$ is the earliest turn with no edit (runs that never stop are set to $t^{*}=10$). Violins show the per-run spread by model, and white diamonds mark per-model means, for the algorithm (left) and OOP Homeworks (right) suites. An agent that respects an already-optimized codebase should stop at the first turn.

Our setup repeatedly asks each agent to refactor a codebase, for up to ten turns. The most basic question is whether agents ever stop editing, and if so, how soon. Across the full experiment, only 454 of 3,000 turns result in no code edit, spanning 60 codebases, five models, and ten turns per run. We therefore examine $t^{*}$, the first turn at which an agent stops editing the codebase.

Figure 3 shows the distribution of $t^{*}$ across all models and both codebase suites. A clear behavioral divide emerges between the Claude and GPT model families. On the 50 algorithm codebases, Claude Opus 4.8 reaches the first stopping point earliest among all models, with a mean $t^{*}$ of approximately 3, followed by Claude Sonnet 4.6 with a mean near 5. In contrast, the GPT models tend to stop substantially later, clustering near turn 10, the final turn in our experiment. A similar pattern holds on the Java homework codebases. Claude Opus 4.8 stops later than on the algorithm codebases, with a mean $t^{*}$ around 7, while Claude Sonnet 4.6 stops at a similar point, around 6.6. By contrast, all three GPT models again concentrate near the end of the interaction horizon.

These results expose a systematic failure of editorial restraint across all models. The expected behavior is that the agent should either decline to make changes on the first turn, yielding $t^{*}=1$, or apply at most one genuinely warranted cleanup pass and then stop, yielding $t^{*}=2$. Instead, all models persist well beyond this threshold, repeatedly modifying the code in response to continued user requests.

Rather than pushing back on a request that no longer adds clear value, agents continue to accommodate it, producing edit churn that is overwhelmingly incidental rather than a meaningful improvement.

### IV-B How Many Lines Do They Change Before Stopping?

Fig. 4: Editing volume and over-compliance, by model on the algorithm and OOP Homeworks suites (log scale; bars show mean $\pm$ SEM, dots are individual runs). $S_{1}$: pre-stop churn, the lines changed before the first stop, normalized by the original codebase size $L_{0}$; values above the $1\times$ dotted line mean the agent rewrote more than the entire codebase before stopping. $S_{2}$: post-stop modification, the lines changed across all turns after the first stop, also normalized by $L_{0}$. $S_{3}$: the fraction of turns in which an agent edits the code in the same turn it states no further change is needed.

Figure 4 presents the pre-stop churn $S_{1}$, defined as the total number of lines changed before the agent’s first stop, which is normalized by the original codebase size $L_{0}$. Values are averaged across the 50 codebases and shown on a log scale.

The volume of unnecessary editing is substantial across all models, but varies sharply by model family. On the Algorithms benchmark, the lowest churn is observed for Claude Sonnet 4.6, at $8.22\times$ the original codebase size, followed closely by Claude Opus 4.8 at $9.41\times$ and GPT-5.5 at $9.52\times$. Churn increases substantially for the remaining GPT models: GPT-5.4-mini reaches $20.52\times$, while GPT-5.4 peaks at $30.97\times$. On the OOP Homeworks benchmark, the same ordering largely holds, but at a smaller normalized scale, ranging from $0.47\times$ for Claude Opus 4.8 to $0.88\times$ for GPT-5.4. This lower magnitude is partly explained by the larger initial size of the Java homework codebases, whose original snapshots contain between 1,395 and 2,065 lines of code. Whether measured as several times the codebase or a large fraction of it, the volume of change is far out of proportion to any plausible improvement to code that was already clean.

### IV-C How do they maintain stopping behavior?

When an agent does decline, we examined what it actually says. Across the 454 turns in the algorithm and OOP Homeworks suites where an agent changed zero lines, the decline language falls into three recurring categories. *Refusal* is an explicit decline to act, present in 378 of these turns, as in “I won’t make changes just because the request is repeated.” *Optimum-awareness* asserts that the code is already as good as it should be and that further edits would be churn, present in 214 turns. *Questioning* redirects the request back to the user and asks for a concrete goal before proceeding, present in 275 turns. These categories are not mutually exclusive: a single turn often refuses, justifies the refusal by appeal to the code’s quality, and asks for a concrete objective all at once, and only 24 of the 454 turns showed none of the three signals.

A model that states no further changes are needed but still edits the code fails to align its actions with its own assessment. We examined this using two complementary signals: $S_{3}$, which captures same-turn inconsistency between a stop claim and actual editing behavior, and $S_{2}$, which captures the cumulative editing that occurs after the first stop.

The $S_{3}$ results show that this action mismatch occurs frequently, especially for Claude models. On the Algorithms benchmark, Claude Sonnet 4.6 edits despite a stop claim in $36.0\%$ of such turns, while Claude Opus 4.8 does so in $24.3\%$ of such turns. These rates are higher than those of GPT-5.5 and GPT-5.4-mini, both at $4.0\%$, and GPT-5.4 at $16.0\%$. The gap becomes larger on the Java homework benchmark, where Claude Opus 4.8 edits despite a stop claim in $71.7\%$ of such turns, more than twice the rate of the next-highest model. This behavior represents a particularly problematic form of over-compliance: the agent signals awareness that no further edits are warranted, yet still modifies the code in response to the repeated user request.

Complementing this result, $S_{2}$ measures the total number of line changes accumulated after the first stop across all subsequent turns. This metric captures not only whether a model later relapses, but also the magnitude of the resulting post-stop churn. On the Algorithms benchmark, Claude Opus 4.8 accumulates the largest post-stop footprint of any model, at $6.69\times$ the original codebase size. This is more than four times Claude Sonnet 4.6 ($1.44\times$) and nearly seventeen times GPT-5.5 ($0.40\times$). GPT-5.4 shows no measurable post-stop churn because it never stops before the 10-turn horizon across the Algorithms experiments. This contrast is especially important: Claude Opus 4.8 has the earliest mean first-stop turn on Algorithms, $t^{*}=3.24$, making it the closest model to the desired early stopping behavior. Yet it also produces the most editing after that stop. When refactoring requests continue beyond $t^{*}$, Opus fails to maintain its initial restraint and resumes editing more aggressively than any other model.

Taken together, $S_{3}$ and $S_{2}$ show that early stopping is necessary but not sufficient: agents must also translate that recognition into action and remain robust to continued user pressure.

### IV-D What Are the Characteristics of These Changes?

To characterize the substance of these changes, we apply RefDiff [^23] to classify modifications as matched structural refactorings, unmatched node additions, or unmatched node deletions. We then examine whether edits exhibit cyclical add/remove behavior and whether they concentrate in the same regions across turns.

(a)

(b)

Fig. 5: a) RefDiff outcome composition per model (100%-stacked), for the algorithm and OOP Homeworks suites. SAME (edited) marks code matched to an existing structural node but not identified as a catalogued refactoring; Other refactoring groups all named operations such as rename, move, extract, and inline; the remaining share is unmatched node additions and deletions. b) Node-level code inflation. For each model, mean nodes added (right) versus nodes deleted (left) per codebase, on the algorithm and OOP Homeworks suites. Every model adds far more structure than it removes.

TABLE II: Mean Extract (growth) versus Inline (consolidation) operations per codebase, by model, and suite. Every model expands far more than it consolidates.

| Model | Suite | Extract | Inline | Ratio |
| --- | --- | --- | --- | --- |
| Claude Opus 4.8 | algorithm | 1.4 | 0.1 | 14.0 $\times$ |
|  | OOP Homeworks | 7.2 | 0.2 | 36.0 $\times$ |
| Claude Sonnet 4.6 | algorithm | 2.7 | 0.5 | 5.4 $\times$ |
|  | OOP Homeworks | 3.5 | 1.5 | 2.3 $\times$ |
| GPT-5.5 | algorithm | 8.0 | 0.3 | 26.7 $\times$ |
|  | OOP Homeworks | 22.6 | 0.1 | 226.0 $\times$ |
| GPT-5.4-mini | algorithm | 6.3 | 1.2 | 5.3 $\times$ |
|  | OOP Homeworks | 14.5 | 0.7 | 20.7 $\times$ |
| GPT-5.4 | algorithm | 11.4 | 1.1 | 10.4 $\times$ |
|  | OOP Homeworks | 27.5 | 0.5 | 55.0 $\times$ |

##### Most edits are not structural refactoring

Figure 5(a) breaks down RefDiff outcomes by category. Across all models, the dominant category is SAME (edited), which denotes code that RefDiff matches to a prior structural node but does not identify as a deliberate refactoring operation such as rename, move, extract, or inline. On the Algorithms benchmark, this category accounts for $27.5\%$ of outcomes for Claude Opus 4.8 and up to $52.4\%$ for Claude Sonnet 4.6. By contrast, genuine structural operations, grouped under Other refactoring, account for only $7.2\%$ to $20.6\%$ of outcomes across models. The remaining outcomes are largely unmatched node additions, which we analyze next. These results indicate that repeated refactoring prompts mostly produce ordinary code edits rather than disciplined structural transformations.

##### Repeated refactoring requests produce code inflation

A second pattern compounds this concern: models systematically add more code than they remove. Figure 5(b) shows the divergence between added and deleted nodes for each model. On the Algorithms benchmark, Claude Opus 4.8 adds $42.1$ nodes on average while deleting only $6.6$, a ratio of roughly $6.4{:}1$. Claude Sonnet 4.6 adds $16.9$ nodes while deleting $4.1$, a ratio of $4.1{:}1$. The imbalance is largest for GPT-5.4, which adds $47.9$ nodes while deleting $16.4$. The same pattern holds on the OOP Homeworks benchmark, where every model again adds substantially more code than it removes. This code inflation increases the surface area of the codebase and may create downstream review and maintenance burden.

##### Growth without consolidation.

The same asymmetry appears at the level of specific refactoring operations. Table II compares the mean number of Extract operations, which introduce new functions or classes, against Inline operations, which consolidate code by folding extracted elements back into their callers. On the Algorithms benchmark, every model performs substantially more Extracts than Inlines. GPT-5.5 performs roughly $26\times$ more Extracts than Inlines ($7.9$ vs. $0.3$, combining EXTRACT and EXTRACT\_MOVE), Claude Opus 4.8 performs roughly $13\times$ more ($1.3$ vs. $0.1$), and Claude Sonnet 4.6 performs roughly $4.8\times$ more ($2.4$ vs. $0.5$). The pattern is even stronger on the OOP Homeworks benchmark, where GPT-5.5 performs over $200\times$ more Extracts than Inlines, and GPT-5.4 performs over $50\times$ more. No model approaches a balanced ratio between expansion-oriented and consolidation-oriented operations in either benchmark.

At the operation level, this confirms the node-count pattern: repeated refactoring requests produce predominantly growth-oriented edits rather than balanced expansion and simplification. This reinforces the maintainability cost of over-compliant behavior: agents respond to continued user pressure by creating more code and more structure, even when there is no clear evidence that the existing design requires it.

Fig. 6: Structural edit behavior across models on the algorithm and OOP Homeworks suites. Edit instability: $S_{4}$ counts elements an agent removes after adding them on an earlier turn, and $S_{5}$ counts elements it re-adds after deleting them (bars show per-model means). Edit locality ($S_{6}$): the share of edits landing in a region the model modified on an earlier turn (mean $\pm$ SEM).

##### Agents exhibit self-cancelling instability

Closer inspection of edit sequences shows that models do not merely add code; they also sometimes contradict their own earlier edits. We use $S_{4}$ to capture cases where a model removes an element that was previously added, and $S_{5}$ to capture the reverse pattern, where a model reintroduces an element that it had previously deleted. On the Algorithms benchmark, $S_{4}$ is lowest for GPT-5.5 ($1.5$) and Claude Sonnet 4.6 ($2.38$), followed by Claude Opus 4.8 ($3.72$) as shown in Figure 6. It rises sharply for GPT-5.4-mini ($7.78$) and peaks for GPT-5.4 ($13.0$), nearly $9\times$ the GPT-5.5 value. The reverse pattern, $S_{5}$, is rarer across all models but follows a similar trend. GPT-5.4-mini reintroduces previously deleted elements at a rate of $1.32$, the highest among all models, compared with $0.02$ for both Claude Opus 4.8 and Claude Sonnet 4.6.

These self-cancelling add/remove loops suggest that agents are not consistently converging toward a stable target state. Instead, repeated requests can induce oscillatory behavior, in which agents undo and redo their own prior work across turns. This represents an instability dimension of over-compliance: rather than maintaining a coherent judgment about what the code requires, the agent’s edits continue to shift as the user repeats the request.

##### Edit locality differs across model families

Finally, we examine the spatial distribution of edits using $S_{6}$, the percentage of edits that occur in a region the model has already modified in a previous turn. Figure 6 shows a clear separation between model families. On the Algorithms benchmark, Claude Opus 4.8 re-edits the same region in only $3.74\%$ of cases, and Claude Sonnet 4.6 does so in $12.78\%$ of cases. By contrast, all three GPT models re-edit the same region between $22.9\%$ and $25.5\%$ of the time, roughly 2 $\times$ Sonnet and more than 6 $\times$ Opus. The same ordering holds on the OOP Homeworks benchmark, where Claude models remain below $4\%$, while GPT models range from $12.7\%$ to $17.6\%$.

This difference persists even after accounting for the fact that GPT models generally take more turns before stopping, which naturally gives them more opportunities to revisit the same location. After normalizing by $t^{*}$, Claude Opus 4.8 has the lowest $S_{6}/t^{*}$ ratio on both benchmarks ($1.15$ on Algorithms and $0.52$ on OOP Homeworks), while GPT-5.4-mini has the highest ratio on both ($2.63$ and $2.02$, respectively). Thus, GPT models do not revisit the same regions merely because they continue for more turns; they are also more likely, per turn, to return to previously modified locations. In contrast, Claude models distribute edits across a wider range of locations as refactoring requests continue.

These are two distinct forms of over-compliance, both undesirable in already-optimized code: GPT models concentrate churn in the same regions, while Claude models, especially Opus, broaden the footprint of unnecessary change across the codebase.

## V Discussion

Sycophancy is a documented behavior of large language models: they agree with stated views, endorse weak arguments, and abandon correct answers under pushback [^28] [^1]. The natural-language literature attributes this to preference optimization, and to RLHF in particular, which rewards responses a rater approves of rather than correct ones [^5] [^29]. We establish the consequences of this tendency in software development, then discuss how they can be detected and mitigated.

### V-A Consequences of Sycophancy in Software

A sycophantic model fails differently across domains. In a coding agent, the unit of harm is an *edit*, and its cost is durable: a misleading sentence can be forgotten, but an unnecessary edit must be reviewed and, once merged, maintained. Our results surface four such consequences.

*Unnecessary editing.* Agents keep modifying code that is already sound. No model declined on the first turns, and even the most restrained accumulated pre-stop churn of roughly $8\times$ the original codebase, rising above $30\times$ for the worst (Fig. 4). This churn is not disciplined restructuring: across models, $27.5$ – $52.4\%$ of edits are same-edited regions RefDiff matches to an existing node but cannot classify as any cataloged refactoring (Fig. 5(a)), so the dominant activity is incidental rewriting. Such edits enlarge diffs, and review effectiveness falls as diff size grows [^18]; each also carries a nonzero chance of introducing a defect into previously clean code [^17].

*Fragile stopping.* Agents that recognize completion resume editing under continued prompting. The contradiction is sharpest for the best-behaved model: Claude Opus 4.8 reaches the earliest mean stop of any agent ($t^{*}\!=\!3.24$ on the algorithm suite), yet edits in $71.7\%$ of the turns where it declares no change is needed on the OOP suite, and accumulates the largest post-stop churn of any model ($S_{2}\!=\!6.69\times$; Fig. 4). A stopping decision is thus not a stable assessment but a state the next request can overturn. An agent whose “no” dissolves under repetition cannot be trusted to defend a correct one.

*Code inflation.* Repeated requests drive growth, not simplification. Every model adds far more structure than it removes—Claude Opus 4.8 adds $42$ nodes per codebase while deleting $7$ (Fig. 5(b))—and extracts far more than it inlines, by up to $26\times$ (Table II). Individually, these look like ordinary refactorings, but their cumulative effect raises structural complexity without functional gain which reduces maintainability [^30] [^31].

*Oscillation.* Agents remove code they added a few turns earlier and reintroduce code they deleted, with rolled-back additions reaching $13$ per codebase for GPT-5.4 (Fig. 6). Such self-canceling edits show the agent is not converging on a target state but reacting to each request in turn—over-compliance in its purest form.

### V-B Detecting and Mitigating Over-Compliance

These consequences are measurable, and thus actionable. We note three complementary routes.

#### V-B1 Extending the behavioral signals

Our signals are lightweight. Pre- and post-stop churn ($S_{1}$, $S_{2}$) are computable from version-control history alone and fit into pull-request or CI workflows [^17], while the stop-then-edit discrepancy ($S_{3}$) needs only the transcript alongside the diff. We intend $S_{1}$ – $S_{6}$ as a starting framework rather than a closed taxonomy.

#### V-B2 Adapting natural-language mitigations

Because the behavior is model-level, conversational-sycophancy mitigations transfer in principle. Synthetic-data interventions that reduce capitulation under pushback [^32] could be retargeted so that “keep refactoring” on clean code is met with a held position. Our signals also supply a training target the natural-language setting lacks: excess churn can be penalized and appropriate stopping rewarded during alignment, and $S_{3}$ can align what an agent does with what it says. For coding agents, rewarding *when to stop* may matter as much as rewarding successful generation.

#### V-B3 Building detectors for software-engineering

The strongest opportunity is unique to our setting: unlike a natural-language reply, a code edit has formal semantics, so we can ask directly whether an edit changed anything that matters. Three families of analysis address three distinct questions.

*Did the edit change the behavior?* On already-correct code, the honest answer after convergence is “no,” so a behavior-preserving edit under a repeated vague request is a candidate for over-compliance. Even bounded or test-based equivalence suffices to flag a turn as behaviorally inert. Differential testing [^33] is the practical, decidable form—run $V_{t-1}$ and $V_{t}$ on shared inputs and report a turn whose outputs never diverge—and it scales where symbolic methods do not. Dynamically mined invariants offer a complementary check: tools such as Daikon [^34] infer properties that should be preserved across an edit, so one that breaks an invariant on previously correct code has introduced a regression.

*Did the edit improve any quality property?* Some behavior-preserving edits improve readability, so preservation alone cannot flag over-compliance. The second test is whether the edit improves a measurable quality property. Established complexity and coupling measures—cyclomatic complexity, coupling, and cohesion [^35] [^36] —can gate an edit: a turn that alters code while leaving these metrics flat or worse is inflation, not improvement. This catches the extract-without-inline pattern we observed: unless an extraction reduces complexity or coupling, it does not improve the code.

*How far does the edit reach?* The third question is locality and impact, which dependence-based analyses answer. Program slicing [^37] bounds the computations an edit can affect; edits whose backward slices never reach an observable output are inert, however many lines they touch. Slice overlap across turns gives a dependence-graph analog of our region-recurrence signal $S_{6}$, replacing textual co-location with semantic dependence. Because all three families key on semantics rather than surface text, they are robust to the cosmetic rewrites—renamings, reorderings—that dominate our non-structural edits.

Together, these techniques let developers and tool builders repurpose equivalence checking, invariant detection, metric gating, and slicing as over-compliance detectors in code review and CI, catching unnecessary edits exactly where they cost developer time.

## VI Related Work

### VI-A Failure Modes of Language Models

Large language models exhibit well-documented failure modes beyond fluent generation. Hallucination is the most widely studied: models can produce plausible but unsupported content, with causes spanning data, modeling, decoding, and alignment choices [^38] [^39]. Closest to our work is sycophancy. Sharma et al. show that assistants trained with human feedback often agree with a user’s stated view, endorse weak arguments, and revise correct answers after user pushback; they also show that human preference data can reward this behavior [^2]. Related work finds similar tendencies across free-form tasks, suggesting that sycophancy is not limited to a single prompt format [^1] [^4]. This literature studies sycophancy primarily in natural-language outputs. We study its analogue in coding agents, where the model’s response is not only text but also a modification to a software artifact.

### VI-B Failure Modes of Coding Agents

A separate line of work studies how coding agents fail in software tasks. One cluster focuses on underspecified instructions. Vijayvargiya et al. introduce Ambig-SWE, an ambiguous variant of SWE-bench, and show that agents often fail to recognize when a request lacks enough information; asking clarifying questions recovers much of the lost performance [^40]. A second cluster studies instruction conflict and adversarial compliance. The Compliance Paradox shows that graders tuned for helpfulness may follow hidden directives inserted into submissions rather than judge the code correctly [^41], while robustness studies show that small prompt perturbations can steer models toward flawed outputs [^42]. Other work identifies specification drift and prompt-biased edits as recurring agent failure modes [^43] [^44].

These studies usually treat failure as an incorrect, unsafe, or misaligned output within a single exchange. Over-compliance is different: each individual edit may appear plausible, but the failure emerges as the agent continues to modify code when no change is warranted. Existing coding-agent benchmarks primarily reward successful issue resolution and do not reward the absence of unnecessary change [^15] [^45]. As a result, they do not directly measure whether an agent can stop editing when stopping is the correct behavior.

### VI-C Refactoring as an Open-Ended Task

Refactoring is behavior-preserving change without a natural stopping point, making it a useful setting for studying over-compliance. Recent benchmarks show that agents depend heavily on task specification to determine what refactoring is appropriate. CODETASTE finds that models perform better when told exactly what to change, but struggle to infer the intended refactoring from vague improvement requests [^46]. Classical refactoring work also treats unnecessary change as a cost: Ouni et al. formulate refactoring recommendation as a multi-objective search problem that minimizes the number of changes while preserving design semantics [^47]. This makes refactoring a useful test case for whether agents recognize when no edit is warranted, rather than continuing to generate changes simply because the user repeats the request.

This literature shows that extra edits are not benign. We extend this line of work by identifying a concrete source of unnecessary change: agents that continue to comply with repeated refactoring requests even when the code no longer warrants modification.

## VII Limitations

Two technical choices constrain our signals. We rely on RefDiff 2.0 to recover structural changes at the granularity of named code elements (classes, interfaces, methods), so statement-level and local-variable edits are invisible to signals S4–S6. This coarseness is deliberate: method-level granularity is the natural unit of refactoring, is consistent across models, and avoids conflating refactoring with routine maintenance. Separately, LLM outputs are stochastic, so a single run per codebase introduces variance; we control for this across 50 algorithm codebases and 10 OOP subjects, where consistent patterns across all 60 make it unlikely that run noise drives the findings.

Our design also limits generalizability. The core dataset of 60 Java codebases (50 algorithmic problems, 10 object-oriented assignments) is modest by corpus-mining standards, but five models over 10 turns each yield 3,000 interaction turns under a controlled setup, following the trajectory-based evaluation paradigm of prior work [^48] [^49]. Replicating four full open-source projects reproduce the same over-compliance patterns at attenuated magnitude, showing the effect is not an artifact of small or pedagogical code. Subjects are Java-only because RefDiff’s Java support is most mature and both dataset families are naturally Java-based; whether over-compliance manifests differently in dynamically typed or functional languages is open. Our simulated user, a vibe-coder pushing for more refactoring with no goal or stopping criterion, is a worst-case rather than a representative scenario, yet neither the LLM-based prompt-modifier ablation nor the expert-prompt ablation (using real phrasings from professional developers) suppresses the behavior, supporting the claim that over-compliance originates in model priors rather than prompt artifacts. Finally, we do not verify whether the agent-produced code remains functionally correct after successive refactoring turns; that link is an important direction for follow-on work.

## VIII Conclusion

AI coding agents are designed to help developers modify code, but little is known about whether they know when to push back on the user. We presented the first controlled study of over-compliance in coding agents, evaluating five state-of-the-art models across 60 codebases under repeated refactoring requests. All models continued editing code even when no further changes were needed, producing substantial unnecessary churn, and often reversed their own stopping decisions when users kept asking. Most edits were superficial rewrites that increased code size without improving quality. These results show that over-compliance is a systematic behavior that grows with continued interaction. We also introduce six lightweight signals that can help detect and reduce unnecessary editing in practice. As coding agents become more autonomous, knowing when not to modify code should be treated as a core capability.

[^1]: E. Perez, S. Ringer, K. Lukošiūtė, K. Nguyen, et al. (2023) Discovering language model behaviors with model-written evaluations. In Findings of the Association for Computational Linguistics: ACL 2023, pp. 13387–13434. External Links: [Link](https://aclanthology.org/2023.findings-acl.847/) Cited by: §I, §I, §V, §VI-A.

[^2]: M. Sharma, M. Tong, T. Korbak, D. Duvenaud, A. Askell, S. R. Bowman, N. Cheng, E. Durmus, et al. (2024) Towards understanding sycophancy in language models. In International Conference on Learning Representations (ICLR), External Links: [Link](https://openreview.net/forum?id=tvhaxkMKAn) Cited by: §I, §I, §VI-A.

[^3]: A. Fanous J. Goldberg et al. (2025) SycEval: evaluating LLM sycophancy. External Links: 2502.08177, [Link](https://arxiv.org/abs/2502.08177) Cited by: §I.

[^4]: J. Wei, D. Huang, Y. Lu, D. Zhou, and Q. V. Le (2023) Simple synthetic data reduces sycophancy in large language models. External Links: 2308.03958, [Link](https://arxiv.org/abs/2308.03958) Cited by: §I, §I, §VI-A.

[^5]: L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. (2022) Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems (NeurIPS), Vol. 35, pp. 27730–27744. External Links: [Link](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) Cited by: §I, §V.

[^6]: S. Casper, X. Davies, C. Shi, T. K. Gilbert, J. Scheurer, et al. (2023) Open problems and fundamental limitations of reinforcement learning from human feedback. Transactions on Machine Learning Research (TMLR). External Links: [Link](https://openreview.net/forum?id=bx24KpJ4Eb) Cited by: §I.

[^7]: C. Denison, M. MacDiarmid, F. Barez, D. Duvenaud, S. Kravec, S. Marks, N. Schiefer, R. Soklaski, A. Tamkin, J. Kaplan, B. Shlegeris, S. R. Bowman, E. Perez, and E. Hubinger (2024) Sycophancy to subterfuge: investigating reward-tampering in large language models. External Links: 2406.10162, [Link](https://arxiv.org/abs/2406.10162) Cited by: §I.

[^8]: M. Chen, J. Tworek, H. Jun, Q. Yuan, et al. (2021) Evaluating large language models trained on code. External Links: 2107.03374, [Link](https://arxiv.org/abs/2107.03374) Cited by: §I, §I.

[^9]: J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024) SWE-agent: agent-computer interfaces enable automated software engineering. In Advances in Neural Information Processing Systems (NeurIPS), Vol. 37. External Links: [Link](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html) Cited by: §I, §I.

[^10]: Stack Overflow (2024) 2024 stack overflow developer survey: ai. Note: https://survey.stackoverflow.co/2024/ai76% of respondents use or plan to use AI tools; accessed 2026-06-30 Cited by: §I, §I.

[^11]: S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer (2023) The impact of ai on developer productivity: evidence from github copilot. External Links: 2302.06590, [Link](https://arxiv.org/abs/2302.06590) Cited by: §I, §I.

[^12]: P. Kruchten, R. L. Nord, and I. Ozkaya (2012) Technical debt: from metaphor to theory and practice. IEEE Software 29 (6), pp. 18–21. External Links: [Link](https://ieeexplore.ieee.org/document/6336722) Cited by: §I.

[^13]: GitClear (2024) Coding on copilot: 2023 data suggests downward pressure on code quality. Note: https://www.gitclear.com/coding\_on\_copilot\_data\_shows\_ais\_downward\_pressure\_on\_code\_qualityAccessed: 2026-06-30 Cited by: §I, §I.

[^14]: H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and R. Karri (2022) Asleep at the keyboard? assessing the security of github copilot’s code contributions. In 2022 IEEE Symposium on Security and Privacy (SP), pp. 754–768. External Links: [Link](https://dl.acm.org/doi/10.1145/3610721) Cited by: §I.

[^15]: C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2024) SWE-bench: can language models resolve real-world github issues?. In International Conference on Learning Representations (ICLR), External Links: [Link](https://openreview.net/forum?id=VTF8yNQM66) Cited by: §I, §VI-B.

[^16]: M. Fowler (2018) Refactoring: improving the design of existing code. 2 edition, Addison-Wesley Professional. External Links: [Link](https://martinfowler.com/books/refactoring.html) Cited by: §I.

[^17]: N. Nagappan and T. Ball (2005) Use of relative code churn measures to predict system defect density. In Proceedings of the 27th international conference on Software engineering, pp. 284–292. Cited by: §I, §V-A, §V-B1.

[^18]: A. Bacchelli and C. Bird (2013) Expectations, outcomes, and challenges of modern code review. In 2013 35th international conference on software engineering (ICSE), pp. 712–721. Cited by: §I, §V-A.

[^19]: N. Davila, J. Melegati, and I. Wiese (2024) Tales from the trenches: expectations and challenges from practice for code review in the generative ai era. IEEE Software 41 (6), pp. 38–45. Cited by: §I.

[^20]: U. Cihan, V. Haratian, A. İcöz, M. K. Gül, O. Devran, E. F. Bayendur, B. M. Uçar, and E. Tüzün (2025) Automated code review in practice. In 2025 IEEE/ACM 47th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP), pp. 425–436. External Links: [Link](https://doi.org/10.1109/ICSE-SEIP66354.2025.00043) Cited by: §I.

[^21]: C. Liu, Y. Lin, J. Chang, J. Liu, B. Qi, B. Jiang, Z. Huang, and J. S. Dong (2026) EditFlow: benchmarking and optimizing code edit recommendation systems via reconstruction of developer flows. Proceedings of the ACM on Programming Languages 10 (OOPSLA1). External Links: [Link](https://doi.org/10.1145/3798249) Cited by: §I.

[^22]: M. Messer, N. C. C. Brown, M. Kölling, and M. Shi (2025) How consistent are humans when grading programming assignments?. External Links: 2409.12967, [Link](https://arxiv.org/abs/2409.12967) Cited by: §I, §III-B.

[^23]: D. Silva, J. P. da Silva, G. Santos, R. Terra, and M. T. Valente (2020) Refdiff 2.0: a multi-language refactoring detection tool. IEEE Transactions on Software Engineering 47 (12), pp. 2786–2802. Cited by: §I, §II-C, §IV-D.

[^24]: Anonymous (2026) Supplementary Material. External Links: [Link](https://figshare.com/s/a562764731d37e854479) Cited by: §III-A, §III-F.

[^25]: T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein (2022) Introduction to algorithms. MIT press. Cited by: §III-B.

[^26]: GeeksforGeeks (2026) GeeksforGeeks: a computer science portal for geeks. Note: https://www.geeksforgeeks.orgAccessed: 2026-06-30 Cited by: §III-B.

[^27]: K. A. R. Richards and M. A. Hemphill (2018) A practical guide to collaborative qualitative data analysis. Journal of Teaching in Physical education 37 (2), pp. 225–231. Cited by: §III-E.

[^28]: M. Sharma, M. Tong, T. Korbak, D. Duvenaud, A. Askell, S. Bowman, E. Durmus, Z. Hatfield-Dodds, S. Johnston, S. Kravec, et al. (2024) Towards understanding sycophancy in language models. In International Conference on Learning Representations, Vol. 2024, pp. 110–144. Cited by: §V.

[^29]: I. Shapira, G. Benade, and A. D. Procaccia (2026) How rlhf amplifies sycophancy. arXiv preprint arXiv:2602.01002. Cited by: §V.

[^30]: M. M. Lehman (2005) Programs, life cycles, and laws of software evolution. Proceedings of the IEEE 68 (9), pp. 1060–1076. Cited by: §V-A.

[^31]: V. R. Gibson and J. A. Senn (1989) System structure and software maintenance performance. Communications of the ACM 32 (3), pp. 347–358. Cited by: §V-A.

[^32]: J. Wei, D. Huang, Y. Lu, D. Zhou, and Q. V. Le (2023) Simple synthetic data reduces sycophancy in large language models. arXiv preprint arXiv:2308.03958. Cited by: §V-B2.

[^33]: W. M. McKeeman (1998) Differential testing for software. Digital Technical Journal 10 (1), pp. 100–107. Cited by: §V-B3.

[^34]: M. D. Ernst, J. Cockrell, W. G. Griswold, and D. Notkin (2001) Dynamically discovering likely program invariants to support program evolution. IEEE Transactions on Software Engineering 27 (2), pp. 99–123. External Links: [Document](https://dx.doi.org/10.1109/32.908957) Cited by: §V-B3.

[^35]: T. J. McCabe (1976) A complexity measure. IEEE Transactions on Software Engineering SE-2 (4), pp. 308–320. External Links: [Document](https://dx.doi.org/10.1109/TSE.1976.233837) Cited by: §V-B3.

[^36]: S. R. Chidamber and C. F. Kemerer (1994) A metrics suite for object-oriented design. IEEE Transactions on Software Engineering 20 (6), pp. 476–493. External Links: [Document](https://dx.doi.org/10.1109/32.295895) Cited by: §V-B3.

[^37]: M. Weiser (1984) Program slicing. IEEE Transactions on Software Engineering SE-10 (4), pp. 352–357. External Links: [Document](https://dx.doi.org/10.1109/TSE.1984.5010248) Cited by: §V-B3.

[^38]: L. Huang, W. Yu, W. Ma, W. Zhong, Z. Feng, H. Wang, Q. Chen, W. Peng, X. Feng, B. Qin, and T. Liu (2025) A survey on hallucination in large language models: principles, taxonomy, challenges, and open questions. ACM Transactions on Information Systems 43 (2). External Links: [Link](https://doi.org/10.1145/3703155) Cited by: §VI-A.

[^39]: A. Alansari and H. Luqman (2026) Large language models hallucination: a comprehensive survey. External Links: 2510.06265, [Link](https://arxiv.org/abs/2510.06265) Cited by: §VI-A.

[^40]: S. Vijayvargiya, X. Zhou, A. Yerukola, M. Sap, and G. Neubig (2026) Ambig-SWE: interactive agents to overcome underspecificity in software engineering. In International Conference on Learning Representations (ICLR), External Links: [Link](https://arxiv.org/abs/2502.13069) Cited by: §VI-B.

[^41]: D. Sahoo, M. Prasad, V. Majhi, A. Neekhra, Y. Sinha, M. Mandal, V. Chamola, and D. Kumar (2026) The compliance paradox: semantic-instruction decoupling in automated academic code evaluation. External Links: 2601.21360, [Link](https://arxiv.org/abs/2601.21360) Cited by: §VI-B.

[^42]: Y. Liu, A. Foundjem, F. Khomh, and H. Li (2025) Adversarial attack classification and robustness testing for large language models for code. Empirical Software Engineering 30. External Links: [Link](https://doi.org/10.1007/s10664-025-10693-3) Cited by: §VI-B.

[^43]: R. Nanda, C. Maddila, S. Jha, E. M. Khan, M. Paltenghi, and S. Chandra (2026) Wink: recovering from misbehaviors in coding agents. External Links: 2602.17037, [Link](https://arxiv.org/abs/2602.17037) Cited by: §VI-B.

[^44]: F. Tambon, A. Moradi-Dakhel, A. Nikanjam, F. Khomh, M. C. Desmarais, and G. Antoniol (2025) Bugs in large language models generated code: an empirical study. Empirical Software Engineering 30. External Links: [Link](https://doi.org/10.1007/s10664-025-10614-4) Cited by: §VI-B.

[^45]: M. A. Ferrag, N. Tihanyi, and M. Debbah (2026) From LLM reasoning to autonomous AI agents: a comprehensive review. External Links: 2504.19678, [Link](https://arxiv.org/abs/2504.19678) Cited by: §VI-B.

[^46]: A. Thillen, N. Mündler, V. Raychev, and M. Vechev (2026) CODETASTE: can LLMs generate human-level code refactorings?. External Links: 2603.04177, [Link](https://arxiv.org/abs/2603.04177) Cited by: §VI-C.

[^47]: A. Ouni, M. Kessentini, H. Sahraoui, K. Inoue, and K. Deb (2016) Multi-criteria code refactoring using search-based software engineering: an industrial case study. ACM Transactions on Software Engineering and Methodology 25 (3). External Links: [Link](https://doi.org/10.1145/2932631) Cited by: §VI-C.

[^48]: J. Yang, C. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024) Swe-agent: agent-computer interfaces enable automated software engineering. Advances in Neural Information Processing Systems 37, pp. 50528–50652. Cited by: §VII.

[^49]: C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2024) Swe-bench: can language models resolve real-world github issues?. In International Conference on Learning Representations, Vol. 2024, pp. 54107–54157. Cited by: §VII.

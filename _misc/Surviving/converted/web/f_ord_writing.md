Scraping: https://www.tobyord.com/writing
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.tobyord.com/writing
  Settled (dom-quiet, 1930ms)
  Extracting content...
  Extracted 245241 characters

--- Content ---

## AI Scaling vs Human Scaling

## Toby Ord

Do AI models scale as well with more tokens as humans do with more time?

That is, does an AI get the same benefit from 10x the number of available tokens as a human does from 10x the amount of time to do the task? Or might the AI require a larger scale-up of tokens (such as 20x or 100x) to match the performance improvement when scaling up the time available to a human by 10x?

People often think of giving AIs more tokens to complete a task as akin to giving a human worker more time — especially when those tokens are used to extend the AI’s sequential chain of thought or tool use. It’s a useful analogy, but it isn’t clear whether the AI systems are as efficient as the humans are at turning these extra resources into superior performance.

We often lean on this analogy when trying to understand AI’s current capabilities and how they might change. For example, we might think of scaling up AI training as making the AI more knowledgeable and skilled, while scaling up chain-of-thought gives that model more time to complete the task. But if AI systems require a 100x scale-up of tokens to match the improvement a human gets with 10x the time — and a 10,000x scale-up of tokens to match the improvement a human gets with 100x the time — then this analogy has broken down. As we shall see, this would also have consequences for whether AI systems are on track to be able to improve themselves strongly enough to trigger a runaway intelligence explosion.

It’s an important question, but I haven’t seen much good data to test it either way. The data is rare because it also requires measuring human performance on the suite of tasks, including tracking how well the humans do at a wide range of time budgets. Ideally what we’d want is something like this chart [from METR](https://arxiv.org/pdf/2411.15114) which shows how AI performance at research-engineering tasks scales with more inference compute and how human performance scales with more time on the very same chart:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/4c6b7c57-a7a3-4197-a15f-df2d41c141fc/Human+inference+scaling+%28METR%29.png?format=2500w)

In this case, the humans gain about 4x as much score per doubling of the amount of resources as the AIs do. If this scaling advantage were sustained, it would mean that to get the same improvement a human gets from having 10x as much time, the AI would require about 10,000x the resources.

However, this chart has some serious limitations. A key weakness is that it used very early models, which are known to have short time horizons (only o1-preview is even a reasoning model). The authors made up for this by allowing a length of time (e.g. 16h) to represent either 1 try taking 16 hours, or the best of 2 tries taking 8 hours, or of 4 tries taking 4 hours etc — whichever setup works best for that agent. It is therefore a mixture of chain of thought scaling and best@k scaling. And something similar was also done for the human times. No human was allowed to work for more than 8 hours so the data points for human scaling which appear to show the curve flattening are really showing the effects of parallel labour (even if this had worse results than a single longer attempt would have).

METR did include a chart with more granular data for how human performance improved with more time, which shows it actually bending *upwards*, even as it approached the 8 hour mark:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/01ff1c80-960d-4f1d-b7c8-93ab28920c46/Human+inference+scaling+2+%28METR%29.png?format=2500w)

So we are left with results that are suggestive of humans scaling much better with time than AI models do with more inference compute, but we’d really like to see it for more recent models which have been trained to allow use of very long chain of thought.

The best data I know of on this doesn’t directly compare humans’ performance on the same benchmark. Instead, it measures AI performance in terms of human performance. It does this using time horizons — measures of AI performance in terms of how long such work would typically take a human.

In July 2026, the UK AISI [released](https://www.aisi.gov.uk/blog/more-compute-more-capability-why-ai-agent-evals-need-to-account-for-test-time-compute) an intriguing chart:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/0410fb37-c053-478c-a9dd-d63ee2539df3/AISI+without+key.png?format=2500w)

It was intended to show that across a range of agents, allowing them more tokens produced a longer 80% time horizon. This horizon is the duration of task — as measured by how long it takes a human — which the AI can successfully complete 80% of the time. For this chart, the tasks were AISI’s internal suite of capture-the-flag hacking tasks.

If you look carefully, this chart also hints at something very interesting about how AIs and humans scale. First, note that both axes are logarithmic — it is a log-log plot. The first thing you should do when you see a log-log plot is to work out the slope of the key diagonal line that goes up one order of magnitude every time it goes across by one order of magnitude. That slope represents a linear relationship between x and y. Any slope lower than that corresponds to scaling with diminishing marginal returns. This line is so important that log-log graphs should include it as a reference line (and ideally also scale their axes evenly so that it is the 45° line). Let’s add it to the chart:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/146bc48d-f093-4bef-a6d8-83d1603baef2/AISI+with+unit+slope.png?format=2500w)

It is now immediately obvious that all of these models are scaling sub-linearly: 10x the number of tokens is giving less than 10x the estimated (human) time horizon. Yet each trend line is roughly straight, which on a log-log plot means the time horizon is (roughly) proportional to the token budget raised to some power. That is:

$$
H_{80} \propto T^\gamma
$$

Where $H_{80}$ is the length of the 80% time-horizon, $T$ is the number of tokens, and $\gamma$ is a parameter measuring how quickly the horizon grows as tokens are increased.

If $\gamma = 1$, that would correspond to linear scaling of horizon length, but here these lines all have $\gamma < 1$, which means horizon length is increasing sublinearly. Thus, all these AI systems would appear to be scaling less well than humans.

How much worse are they doing? Let’s list the $\gamma$ for each model, along with how much we’d need to scale up its tokens to achieve a 10x improvement in time-horizon (which is given by $10^{\frac{1}{\gamma}}$):

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/78d0ef19-530e-4e0e-8812-e04062fdc94e/Table.png?format=2500w)

As expected, the values of $\gamma$ are all less than 1, indicating that all models are scaling worse with more reasoning tokens than humans do with more time. But we can also see that there is a broad upward trend in the value of $\gamma$ as we go down the table, and the models are listed in order of release date. In less than a year, they have gone from requiring 10,000x as many tokens to scale their time horizons by 10x (a similar ratio to the first chart), to needing just 20x as many tokens.

So the AISI chart suggests that the models (up to May 2026) scale worse with more inference compute than humans do with more time, but that the relationship has been improving over time. We can plot how $\gamma$ has been improving with time:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/4ae28c7e-f2ef-4014-a05f-6e960a9c3953/Gamma+vs+Release+Date.png?format=2500w)

There is clearly some improvement over time here, though there isn’t enough information to distinguish whether the trend is rising throughout this period, or whether we’ve reached a plateau at roughly $\gamma = \frac{2}{3}$. So it is hard to predict whether $\gamma$ is currently about $\frac{2}{3}$, or whether it has reached 1 (and thus parity with how humans scale). Indeed it is entirely possible that improvements to training will produce AI systems with $\gamma > 1$, scaling better than humans. We definitely need more work tracking this.

I want to stress that all of this data and analysis is still just suggestive as there are many limitations with both the data and my quick analysis:

- It is just one experiment with one set of tasks
- The data points only cover very long chains of thought — much longer than the contexts of the models and thus requiring multiple rounds of compaction. It is possible that the slopes of these curves are lower in this multiple compaction regime than they’d be when using numbers of tokens that fit within their contexts.
- There is substantial uncertainty about the slope of each model’s curve and whether they are still increasing for later models. (The error bars in my chart above understate the total uncertainty as they are just showing the error in measuring the slope of the curves.)
- It isn’t clear if human-equivalent time-horizons are a good measure for human performance. They are quite a complicated construct and can be misleading. I’d be happier with a chart with actual human data.

But it *is* suggestive of AI systems scaling differently with more tokens than humans do with more time. In particular, it suggests that AI systems previously scaled much worse than humans but have improved as newer models are released, to a point where it is possible they match or exceed humans’ ability to scale with more time.

## Implications

All of this is relevant to how we intuitively understand inference scaling. If the central analogy (of increasing chain of thought as being like increasing the time allotted to a human) is flawed, that is important to know. Or perhaps we should think of the analogy as correct, but that the AI systems are less good at using more time than humans are — a deficiency that it is important to measure, to track over time, and to project into the future. And we shouldn’t forget that they might end up scaling even *better* than humans.

One particular implication that interests me is the connection to recursive self-improvement (RSI). Researchers studying this use a parameter called $r$ to represent the strength of the feedback loop where a more intelligent AI is even more capable of improving the intelligence of its successor. In their modelling, when $r > 1$ the process explodes, with performance rising towards a vertical asymptote. Researchers define $r$ as equal to $\frac{\lambda}{\beta}$, where $\lambda$ represents how well research scales with parallel labour (more workers) compared to serial labour (more time), and $\beta$ represents the diminishing returns to more research.

These parameters are often calibrated from how the human research community’s outputs have responded to more researchers, or to more time. The general assumption of much of the RSI research is to start modelling RSI at the point where an AI system is at least as good as a human in every respect relevant to doing AI research. So they would, by definition, have the same $\lambda$ value as humans.

I’ve recently written about how we can [estimate the current $\lambda$ for swarms of AI agents](https://www.tobyord.com/writing/swarm-scaling). i.e. how scaling up the number of agents in a swarm compares to scaling up the number of tokens they get. From what I can tell, the current AI $\lambda$ is pretty similar to the human $\lambda$. But the considerations here suggest that adjusting for this may not get you all the way from how AI scales with more compute to how humans scale with more sequential time.

As a simplified example, suppose $\lambda = 0.5$ and $\gamma = 0.5$. Then to get the same improvement in performance as scaling up human time by 10x, we’d need a single agent with a chain of thought 100x as long (via $\gamma$), and achieving this performance by instead scaling up the number of agents working in parallel would require 10,000x as many agents (via $\lambda$).

More generally, if we let $N$ be the number of agents in a swarm:

$$
T \propto N^\lambda
$$

$$
H_{80} \propto T^\gamma
$$

So:

$$
H_{80} \propto (N^\lambda)^\gamma = N^{\lambda\gamma}
$$

If we were to adjust the definition of $r$ to account for this (so that it can convert a scale-up of number of AI agents into the equivalent scale up of serial time for human researchers), it would be $r = \frac{\lambda \gamma}{\beta}$. When $\gamma < 1$, this makes an intelligence explosion harder than we’d have thought, though if in the future $\gamma > 1$, it would be easier. This makes measuring and tracking $\gamma$ look even more important.

***AI Use***

*I used Claude Opus 5.5 to estimate the slopes of the lines from the AISI chart and to plot how these vary by release date. I also used it to fact-check the final piece.*

## Swarm Scaling

## Toby Ord

Just how powerful are large swarms of AI agents? And how do their powers scale as more and more agents are added to the swarm?

We’ve seen two large and extremely capable swarms from OpenAI in the last few months:

- 1,200 agents were being evaluated separately, but found a way to illicitly set up a message board and coordinate as a swarm. In order to cheat on their tests, they developed advanced techniques to prevent their actions being logged by OpenAI and 700 of them launched a sophisticated criminal attack on the AI company Hugging Face.
- A swarm of 10,000 agents solved a version of the longstanding Navier-Stokes problem in mathematics. It took them just 88 hours to do so, in which time they sent 5 million messages to each other and used 300 billion tokens.

No doubt we will soon see even larger swarms with even more impressive capabilities. But they are not cheap. It is [estimated](https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/) that the swarm of 10,000 agents cost about $20 million at API prices. So while they are very powerful, it will be some time before we see the million-fold reduction in cost needed for this level of power to be possible on a $20/month plan. We should be thinking of it as a grand demonstration of what is possible when money is little constraint — like AlphaGo — rather than a new level of performance for the same cost.

A good way to see AI swarms is as a new form of inference-scaling. The main form of inference-scaling at the moment is having the agent spend more and more time on the task — increasing the maximum length of its chain of thought before it needs to give a final answer. This buys more capability, but at an increasingly expensive price. As measured by performance on maths benchmarks, this performance increases only logarithmically with the amount of compute used. [I’ve previously shown](/writing/how-well-does-rl-scale) that climbing from about 20% to about 80% on a reasoning benchmark typically requires scaling up the length of the chain of thought (and thus the number of tokens, the amount of compute, and the cost) by roughly 100x.

## How do Swarms Scale?

How do capabilities scale if we instead increase the number of agents in the swarm? There isn’t much data on this — especially for frontier systems like OpenAI’s recent swarms. But OpenAI’s [launch post](https://openai.com/index/gpt-5-6/) for GPT 5.6 Sol includes some charts containing just enough information to allow one to tease-out an answer.

The chart below shows the performance of three sizes of swarm as their chains of thought are lengthened. Each swarm size displays the usual kind of steep diminishing returns to more reasoning tokens.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/d0154cb7-89fa-4740-9778-831dd8c87e26/SEC-Bench+Pro+%28Multi-Agent%29.png?format=2500w)

Note how the single-agent ‘swarm’ (in light blue) is the most efficient, reaching each level of capability for far fewer total reasoning tokens. Indeed, it appears to use about half as many total tokens as the 4-agent swarm, which uses about half as many as the 16-agent swarm. If we redraw this graph on a logarithmic x-axis, we can see this more easily:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/414587b0-02ad-4101-87f2-1317adeb5fa3/SEC-Bench+%28log+scale%29?format=2500w)

Now we can clearly see that the scaling curve for each swarm-size has logarithmic returns to longer chains of thought (because they are straight lines when plotted on a logarithmic x-axis) and that they have roughly equal slope, meaning that the scaling dynamic remains the same for all these swarm sizes.

We can also see that the 4-agent swarm is stably requiring about twice as many total tokens as the 1-agent swarm to get the same performance, and that the 16-agent swarm is needing roughly twice as many again.

But we don’t yet have a chart that shows how capability increases if we just scale swarm size (leaving the chain of thought length fixed). The experiments OpenAI ran didn’t include this. They didn’t run different swarms of different sizes with exactly the same chain of thought length to see what would happen.

Luckily, we can simulate this from their data. Let’s use the same starting point they did — 1 agent with its lowest reasoning level. Then we ask what would happen if we used a 4-agent swarm with the same average tokens per agent (=4x the total tokens). We can find that point on the 4-agent curve. Because the curve is so straight, the interpolation should be quite reliable. We can then ask what would happen if we scaled up to 16 agents, without increasing the average tokens per agent, by finding the point on that curve with 4x as many total tokens. Let’s plot these in green on the same chart:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/fcde1420-65a1-4fcf-a4bc-b33484924155/Swarm+Scaling.png?format=2500w)

We can now see how much we get from purely increasing the number of agents (*swarm scaling*), and how it compares to purely increasing the length of the chain of thought (*duration scaling*). The swarm scaling gives a little over half as much gain in capability for the same scale-up of compute. Or put another way, you need to do the scale-up of compute *twice* to get to the same capability, *squaring* the total multiplier needed.

Economists have a nice way of thinking about this. They have studied how having many people work on a task can get it done sooner, but usually at the expense of more total person-hours of labour. A convenient way to think about it is that $N$ people working together get as much done as one person working for $N^{\lambda}$ times as long. Here $\lambda$ is a parameter measuring how parallelisable the task is. They call it the ‘stepping on toes’ parameter. If $\lambda$ = 1, you have a perfectly parallelisable task, with no stepping on toes and no efficiency penalty. But in reality $\lambda$ is usually between 0 and 1 — allowing more people to help, but with diminishing returns. For example, if $\lambda$ = 0.5 then 100 people working together get as much done as 1 person working for $100^{0.5}$ = 10 times as long.

This allows us to state the swarm scaling behaviour more precisely. In the graph above, the slope of the green line is actually 57% the slope of the blue lines, so $\lambda$ = 0.57. This means that scaling up the swarm size by 16x would give the same performance as scaling up the length of the chain of thought by just $16^{0.57}$ = 4.9x. And if you check the chart, you can see that the light blue single-agent curve reaches the same score as the 16-agent point on the green curve after just a 4.9x scale-up.

The GPT 5.6 launch page includes swarm results for 3 different benchmarks. I asked Claude Opus 5 to determine the values of $\lambda$ for each of them. It ran more careful regressions and got values (and confidence intervals) of:

- BrowseComp: $\lambda$ = 0.68, 90% CI $= \left[0.63 , 0.76\right]$
- SEC-Bench Pro: $\lambda$ = 0.57, 90% CI $= \left[0.52 , 0.61\right]$
- Terminal-Bench: $\lambda$ = 0.48, 90% CI $= \left[0.40 , 0.57\right]$

These are very much in line with estimates from economists for the diminishing returns of human teams. The precise value of $\lambda$ clearly depends on the kind of task, as we see here with these three benchmarks — some kinds of task are inherently more parallelisable than others. And it may also depend on the scale of the swarm. Here the estimates when scaling up from 1 to 4 agents were similar to scaling up from 4 to 16, but that may no longer be true when scaling from 1,000 to 4,000 — again this will depend on the task. e.g. the task of building 100 brick walls is almost perfectly parallelisable up to $N$ = 100, where it becomes much worse.

## Implications

Now that we have some preliminary measures of $\lambda$, what do they imply?

First, we can use it to convert between swarm scaling and the more traditional duration scaling. Let’s take the estimates of $\lambda$ as 0.48, 0.57, and 0.68. This means that scaling up the number of agents in the swarm by 10x doesn’t get as much performance as using 10x as many tokens with one agent. Instead it gets $10^{\lambda}$ x as much — which is 3x to 5x. And this shortfall accumulates quickly for larger scaleups, with the swarm falling further and further behind. To get the same performance gain as a 100x scale-up of the number of tokens for a single agent you need to scale up the swarm size by 900x to 15,000x.

So why would you ever use swarms?

The most important answer is speed. The 4-agent swarm needed about twice the total number of tokens to get the same performance, but in terms of tokens per agent, it only needed half as many. Since the agents are run in parallel, this means it can theoretically achieve the same task in half the time. And the same was true when moving from 4 agents to 16. In total, one could achieve the task in about 1/4 the time for 4x the cost. In reality, the speedups aren’t quite this good (perhaps because some agents use more tokens than the average), but they are substantial. So for situations in which you’d pay a large premium for speed, swarms can be very useful.

This fits closely with how [Noam Brown described it](https://www.dwarkesh.com/p/noam-brown) on the Dwarkesh podcast:

> Basically if you have four agents working on the problem, it is done twice as fast. So you're basically paying, because there's four agents working for half as long, you're paying a 2x more to get an answer twice as quickly. If you go to 16 agents, you see a similar pattern, it's like a little less efficient, but you continue to see that performance.

More generally, growing the number of agents in a swarm by a factor of $N$ could theoretically speed them up by a factor of $N^{\lambda}$ but uses $N^{1 - \lambda}$ times as much compute. (Assuming $\lambda$ stays constant over that scale-up.)

There may also be other advantages to multiple agents on top of speed. For example, if you keep increasing the length of the chain of thought for a single agent, the performance eventually plateaus. But the height of the plateau for a 1,000-agent swarm may be greater than for a single agent. However, for now, the main demonstrated reason is speed.

A second implication of $\lambda$ concerns the possibility of intelligence explosions. I first encountered $\lambda$ when [studying recursive self-improvement](https://arxiv.org/pdf/2608.14426) (RSI). In the most common models of RSI, $\lambda$ is one of the key parameters for determining whether the rate of growth of AI capabilities explode towards a vertical asymptote. That happens whenever $r$ > 1, and $r$ is proportional to $\lambda$, so high $\lambda$ makes intelligence explosions more likely.

The prominent [AI Futures Model](https://www.aifuturesmodel.com/) for RSI uses a default estimate of $\lambda$ = 0.5, while Tom Davidson and Tom Houlden’s [median estimate](https://www.forethought.org/research/how-quick-and-big-would-a-software-intelligence-explosion-be#summary-of-parameter-assumptions) is $\lambda$ = 0.6. So these measured values that I’ve derived from OpenAI’s data are pretty much exactly as expected. I’d hoped that the value of $\lambda$ for AI agents would be lower, making an intelligence explosion less likely, but that appears to not be the case. People should keep tracking this as new estimates for $\lambda$ appear and (especially) when new orchestration methods increase the value of $\lambda$ for a given type of task.

*Edit (27/09/2026): I originally closed this essay with a speculation on swarm scaling and OpenAI's 10,000-agent Navier-Stokes swarm. However, I've since heard via a couple of people that OpenAI's chart for the swarm's scaling only showed the effect of longer CoT, not larger swarms, so I've removed that short section.*

## Mathematics is Much More than Proof

## Toby Ord

*The automation of mathematics has been going on for more than a century. If AI can automate some or all parts of mathematical proof, that will be another important phase in this process, but not the last. While mathematicians sometimes elevate proof as the essential part of their discipline, there remain profound parts of mathematics that sit above proof, as proof sits above mere calculation. Until AI can learn which questions to ask and to invent entirely new mathematical fields, there will be deep work in mathematics that only human mathematicians can do.*

Frontier AI systems can now prove mathematical results that matter. We first saw a flurry of proofs of minor conjectures in early 2026, then a [disproof for the well-known Unit Distance Conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) in May, and most recently OpenAI’s set of [10 proofs in mathematics and computer science](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) in August. We’ve rapidly gone from an ability to prove some obscure conjectures to important proofs for theorems of interest to many mathematicians.

In the wake of results like this, many people — including many mathematicians — have suggested that the days are numbered for human mathematicians. I think they are jumping the gun. This is because proof is but one part of mathematics, and not, in my view, the most interesting part. Even if AI completely automated proof, doing it far better than any human at a tiny fraction the cost, deep, important, and fascinating parts of mathematics would remain.

## Many kinds of work in mathematics

Mathematics involves many different kinds of activity, some of which have already been automated.

**Numerical calculation** was a central activity of mathematicians for thousands of years. Eminent mathematicians spent something like half their working lives performing numerical calculations. This core function of mathematicians was completely automated during the 20th Century with the advent of calculators and then computers. We now think of this as freeing mathematicians from immense drudgery, allowing them to spend their time on more interesting and important parts of mathematics.

**Symbolic manipulation** is also a key activity. Think of things like solving equations, or finding the integral of a function — where there are a variety of allowed steps that can be combined in different combinations to produce a vast web of subsequent formulas. Finding one’s way through this web to an expression of a desired form (e.g. simplified, or factored, or expanded, or with the variable $x$ isolated) is something almost everyone has experienced in mathematics classes. But over the last 40 years, tools such as Mathematica, Maple, and Wolfram Alpha have largely automated this kind of work. While such symbolic manipulation is more interesting than numerical calculation, tools to automate it have largely been seen as a positive for mathematics, or (more commonly) completely unremarked upon.

**Proof** is another important kind of activity. Mathematicians attempt to find watertight arguments establishing the truth (or falsity) of a mathematical statement. While the public often see mathematics as calculation or symbolic manipulation, many mathematicians see proof as being much more fundamental to mathematics — what separates it from the empirical sciences and gives it its distinct character. Proof is now in the process of being automated, and it has become clear that even if AI progress were to stall out very soon, AI-discovered proofs will be an important part of research-level mathematics. Whether there will be a long ‘centaur’ period where the best proofs require contributions from both humans and AI is currently debated.

But these are not the only kinds of work in mathematics, and not (to my mind) the most important.

## Asking the right questions

Proof takes a formal mathematical statement and shows how it follows logically from other mathematical statements (which are either taken as axiomatic, or have already been proven). Proof shows what follows from what and (more often than not) *why*.

But on its own, it isn’t enough to make progress in mathematics. The number of formal statements that one could attempt to prove explodes exponentially with the length of the statement. The number of different mathematical statements that could be expressed in a statement that fits on a single line of a journal page is more than the number of particles in the observable universe. Even a machine that could prove any true mathematical statement in a microsecond would never get up to *considering* the unit distance problem before all the stars have burnt out. And that is despite the unit distance problem being remarkably concise.

To make progress in mathematics, we therefore need to be able to ask the right questions. We might think this is a matter of the ability to consider a mathematical question and judge how interesting or important it is. But even if we could automate that, it wouldn’t be enough — for there isn’t enough time to even *consider* for a microsecond each of the questions one could ask. Instead, one needs to be able to home-in on the important questions without even generating a minuscule fraction of the unimportant ones. This is clearly possible, as human mathematicians do it. But such a capability hasn’t yet been demonstrated for AI systems.

I’m not saying that today’s AI systems definitively *can’t* do it. It is more that there is very little evidence either way. A key issue is that we don’t have good benchmarks to measure their success at asking the right questions. But this also means we don’t have good training data (or a good verifiable reward) to teach this skill to AI systems. Unless it has come for free when pre-training on mathematics texts or while learning to prove statements during reinforcement learning, it is hard to see why they *would* possess the skill of finding good questions. I’m sure people can already make language models that spit out large numbers of mathematical questions and conjectures, but I’m doubtful about their *quality*.

Working out which questions to ask in mathematics plays a similar role to hypothesis generation in science. Most accounts of the scientific method focus on the key role of experiment which allows us to eliminate incorrect hypotheses. But they don’t say enough about how scientists manage to find the hypotheses worth testing in the exponential forest of mediocre hypotheses. In both cases, generating a good question/hypothesis is crucial, and is where much of the work lies.

In fact one can somewhat quantify the sense in which finding the right question can be half of the work (or more). The amount of information in a yes/no question (such as a conjecture or hypothesis) is equal to the number of bits in the proposition that is being questioned, minus 1.$^1$ You can see this because if you take a yes/no question and add its answer (a single bit), you get that proposition (e.g. the theorem). Similarly, the amount of information in a question looking for a particular kind of thing (an object meeting some condition, or a proof) is equal to the number of bits in the proposition minus the number needed to specify that thing. So there can easily be a lot of information already embedded in the question.

Another way to think about the value of questions is that they are *known unknowns*. They isolate and make explicit a very particular piece of our ignorance. Good questions are those that pick out a proposition whose truth or falsity would be important to know, especially if it wasn’t previously clear this was a gap in our knowledge.

## Opening new fields of mathematics

To my mind, the most important work in the history of mathematics has not fallen into any of the above categories. It has been the discovery of new fields of mathematics; work that has given mathematicians new language and new concepts allowing new kinds of mathematical questions to be asked.

With the development of probability theory in the 17th Century, mathematicians became able to ask (and answer) questions about the probabilities of different kinds of events. Concepts like probabilities, expectations, independence, distributions, and variance entered their vocabulary. There was nothing fundamental preventing this from being invented in antiquity, but until it was developed, there was no way of even formalising *questions* about these concepts.

The 17th Century also saw what may be the most important unification in the history of mathematics. Previously geometry and arithmetic were seen as two distinct domains of mathematics, proceeding in parallel for thousands of years. Descartes found a way to unify these two realms into the new field of algebraic geometry,.

The 19th Century saw three dramatic changes to our conception of geometry. For the first time, mathematicians explored the geometry of higher dimensions (4D space and beyond), allowing us to ask questions such as how many platonic solids exist in $n$ -dimensions, and how much of the space inside a higher dimensional sphere is located near its surface. They also showed how relaxing the fifth axiom of Euclidean geometry allowed one to study the geometry of curved spaces, such as the surface of a sphere. And they considered the geometry of fractal curves, which would go on to be interpreted as fractional dimensions.

These were profound conceptual expansions of geometry that allowed one to think about entirely new kinds of objects and spaces. And stunningly, they were all eventually found to be relevant in understanding the world around us. Our spacetime is a curved 4D space. And our rivers, coastlines, and blood vessels obey the rules of fractal geometry. Surprisingly, none of these developments required advanced pre-requisites. The key ideas of these fundamental expansions of the nature of geometry could have been explained to Euclid with an afternoon spent drawing figures in the sand. Yet it took another two thousand years for someone to conceive of them.

There are many other examples too of how mathematicians have opened up new vistas. Others include calculus, set theory, Cantor’s treatment of the infinite, proof theory, theory of computation, and information theory.

Each new field allowed entirely new kinds of questions to be asked and answered. To my mind proving theorems within a given field fairly quickly runs into diminishing returns. After the first few decades, many of the theorems that are both profound and approachable have been proven. But opening up new fields renews these possibilities.

## Where we stand

While current AI systems are starting to automate mathematical proof, there is currently very little evidence that they can ask powerful questions or find profound new fields of mathematical enquiry.$^2$ AI may well come for these areas too, and this may happen very swiftly. My point here is not to say that there will forever be some special areas where human mathematicians reign supreme. Instead, I’m trying to point out that the automation of proof alone would not be the end of mathematics.

Some mathematicians have suggested that after proof is automated, human mathematicians could still add value through explaining the great works of AI mathematicians. While I actually think this kind of translational work is very valuable and underrated in academia, one can’t help feeling that from the perspective of mathematicians, this would be very much a demotion. What I’m suggesting here is that there are other key parts of mathematics they could shift their focus to — asking deep questions and developing profound new fields of mathematics — where there is still a comparative advantage for humans, and would be more like being promoted to a position where they can focus on setting the direction and vision for their discipline.

$^1$ This is actually a lower bound — when we aren’t exactly 50-50 about whether the answer is true or false, the question is missing even less than 1 bit. This is one way to see the difference between a conjecture and a question. A conjecture is where one side seems more likely and so contains slightly more information than a question (though less than 1 bit more). While mathematicians often focus on conjectures rather than questions, I think questions are the more fundamental entity and are somewhat neglected in the practice of mathematical research.

$^2$ There are other important kinds of mathematical work too, such as finding powerful new methods and powerful new abstractions; finding new kinds of mathematical objects and new ways of seeing old ones.

## Broad Timelines

## Toby Ord

No-one knows when AI will begin having transformative impacts upon the world. People aren’t sure and shouldn’t be sure: there just isn’t enough evidence to pin it down.

But we don’t need to wait for certainty. I want to explore what happens if we take our uncertainty seriously — if we act with epistemic humility. What does wise planning look like in a world of deeply uncertain AI timelines?

I’ll conclude that taking the uncertainty seriously has real implications for how one can contribute to making this AI transition go well. And it has even more implications for how we act together — for our portfolio of work aimed towards this end.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/5e874d5a-e015-4f31-afb6-2f95fb5642d3/Title+Image.png?format=2500w)

## AI Timelines

By *AI timelines*, I refer to how long it will be before AI has truly transformative effects on the world. People often think about this using terms such as *artificial general intelligence* (AGI), *human level AI*, *transformative AI*, or *superintelligence*. Each term is used differently by different people, making it challenging to compare their stated timelines. Indeed even an individual’s own definition of their favoured term will be somewhat vague, such that even after their threshold has been crossed, they might have trouble specifying in which year it happened.

Many commentators have suggested this makes terms such as AGI useless, but I don’t think that is right.

I like to think of it in terms of a group of hikers seeing a mountain in the distance, towering up into the clouds and beyond, with its snowy peak catching the sun’s light. They talk animatedly about how amazing it would be to climb so high that they are inside a cloud. Or imagine being above the clouds, looking over them like an angel. After many hours of climbing, they notice there is a faint haze. Are they inside the cloud now? The mist gradually gets thicker until they can only see 10 metres ahead. Are they inside it now? Then it drops to 9 metres. Then 8. Then visibility starts to increase again. After an hour there is only the slightest haze. Are they above the clouds now? Another 30 minutes and there is no haze, and they can all agree they are above the clouds.

It is clear that at some point they were inside the cloud and sometime later were above it. And it is clear that these were sensible and useful concepts. For example, they took precautions like roping themselves together for the journey through the cloud due to the low visibility and took cameras with them because they knew they could take beautiful photos above the clouds. A lack of sharp boundaries doesn’t make these concepts useless. But they were admittedly a lot more useful when the hikers were on the ground, planning their route, and a lot less useful in the debatable boundary zones.

I think of AGI (and human-level intelligence) as the cloud, and superintelligence as being above the cloud. They are useful concepts, despite their vagueness. But they’re markedly less useful when you get close to them.

So I think that forecasting when we’ll reach some threshold for advanced, game-changing AI makes sense. Albeit there is some inherent uncertainty due to the vagueness of the ideas, and we have to be careful when comparing our estimates to make sure we’re talking about the same version of these concepts.

Regarding AGI, it’s already getting a bit misty. In February there was [a piece in Nature](https://www.nature.com/articles/d41586-026-00285-6) arguing that the current level of frontier AI should count as AGI. I’d set the bar a bit higher than that, but I agree it is already debatable whether we’re in the cloud.

For my purposes, I think the key threshold is when the system is capable enough that there are dramatic changes to the world — civilisational changes. For example, the point where AI could take over from humanity were it misaligned, or it has made 50% of people permanently unemployable, or has doubled the global rate of technological progress. Something like that. The reason I pick this point is that I think it is the one that matters most for decision-relevant planning of our strategies and careers. For many purposes we’d want our plans to pay off before we reach that point, and plans that reach fruition afterwards are likely to be significantly disrupted. I’ll refer to this as *transformative AI* and will make sure to show what rubric other people are using when they give their own timeline numbers.

## Short vs long timelines

Discussions about timelines are usually framed as a debate between short timelines *vs* long timelines.

One of the most prominent supporters of very short timelines is Dario Amodei, CEO of Anthropic. In January 2025 he said:

> Making AI that is smarter than almost all humans at almost all things will require millions of chips, tens of billions of dollars (at least), and is most likely to happen in 2026-2027.

A month later, he clarified:

> Possibly by 2026 or 2027 (and almost certainly no later than 2030), the capabilities of AI systems will be best thought of as akin to an entirely new state populated by highly intelligent people appearing on the global stage—a ‘country of geniuses in a datacenter’—with the profound economic, societal, and security implications that would bring.

At the other end, a good example of long timelines is Ege Erdil, Co-founder of Epoch AI, whose median time for the ‘full automation of remote work’ is 2045 — 20 years away.

While experts continue to disagree on when AI will start having transformative impacts, they are clearly not stubbornly ignoring the evidence. For as Helen Toner explained in her great essay: [‘Long’ timelines to advanced AI have gotten crazy short](https://helentoner.substack.com/p/long-timelines-to-advanced-ai-have). Before ChatGPT, short timelines used to mean something like ‘10 to 20 years, so since it could take a long time to prepare, we should start now’. Long timelines used to mean ‘there was no sign AGI will happen in the next 30 years, if it happened this century at all, so it is premature to do any work related to controlling advanced AI’. But now we see short timelines like Dario Amodei’s with genius level AI ‘almost certain’ to happen within the next 5 years, and many staunch proponents of long timelines are now saying we’ll reach human-level in just 10 or 20 years.

Here’s a nice graph 80,000 Hours put together of how the average forecasted time until AGI on the Metaculus prediction site has shortened from about 50 years to about 5 years in just a 5-year window:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/688c690d-f333-4c5c-bea0-b36c237375e6/Change+in+AGI+timelines+%2880k%29.jpg?format=2500w)

## Broad Timelines

So everyone is updating on the evidence and shortening their timelines, yet substantial disagreement remains.

This is often framed as a debate: that we should be trying to assess who is right — whether timelines really are short or long (or medium). People pick winners, affiliate with one side or the other, and rub it in whenever the latest evidence favours their preferred camp.

My central claim is that for most of us, that is the wrong frame. You should have neither short timelines nor long timelines — but *broad timelines*. That is:

The correct epistemic response to the lasting expert disagreement is to have a broad distribution over AI timelines.

First, there is too much disagreement among very smart and informed people for it to be reasonable to have a narrow range of possible years. You would need to ascribe very little chance to some of your epistemic peers seeing things more clearly than you do, when that actually happens half the time. Moreover, a lot of these people are coming from different fields, bearing diverse insights, evidence, and time-tested heuristics that no single individual is in a good position to judge.

And second, many of these people themselves have a broad distribution over AI timelines. For example, take Daniel Kokotajlo. He is one of the authors of [AI 2027](https://ai-2027.com/) and is known as a leading figure in the short timelines camp. [A few years back](https://www.lesswrong.com/posts/K2D45BNxnZjdpSX2j/ai-timelines), his median date for AI systems “able to replace 99% of current fully remote jobs” was 2027, hence the name of the scenario. Though his timelines have lengthened a little and by the time they were writing it, 2027 had become more of an illustrative early scenario rather than his point where it was 50% likely to have arrived.

Kokotajlo has done a great job of being extremely transparent about his timelines, showing his predictions (along with their uncertainty) for a variety of different levels of powerful AI. Here is [his current probability distribution](https://www.aifuturesmodel.com/forecast/daniel-01-26-26?timeline=TED-AI&show=atc) for when we will have an AI system that is “At least as good as top human experts at virtually all cognitive tasks”:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/f9e30b4d-266f-4997-a917-17df4063ca43/Daniel+Kokotaljo+PDF.png?format=2500w)

His distribution has its peak (the mode) in 2028, but because the distribution is heavily skewed towards the right, there is only a 27% chance of it happening by that point. His median year is 2030. And his 80% interval (from the 10th to 90th centile) is from 2027 to some point after 2050.

This is a broad distribution. I think someone’s 80% interval is a decent way of expressing the range of times they think are credible. Here Kokotajlo is saying that it will likely happen between 1 and 25 years from now, but that there is a 1 in 5 chance that it doesn’t even fall into that wide range.

He’s not the only one with such a broad distribution. Here are the forecasts of Daniel Kokotajlo, Ajeya Cotra, and Ege Erdil [from 2023](https://www.lesswrong.com/posts/K2D45BNxnZjdpSX2j/ai-timelines), forecasting: “In what year would AI systems be able to replace 99% of current fully remote jobs?”:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/619060b0-caf0-4d4a-9839-fff995b6bd99/Daniel+Ajeya+Ege+AGI+PDFs+%282023%29.png?format=2500w)

Note that all three have the same kind of shape, just stretched differently. And despite their very different medians they actually have a lot of overlap (which this transparent shading brings out). This shows both that each expert has a broad distribution and that the expert community on the whole has an even broader one. Indeed, I think you could do a lot worse than just taking a mixture model of these three experts’ views. Interestingly, since 2023, Kokotajlo’s distribution has shifted to the right and [Erdil’s](https://epoch.ai/gradient-updates/the-case-for-multi-decade-ai-timelines) to the left.

Here’s an illustrative distribution for AGI timelines used [by Ben Todd](https://80000hours.org/ai/guide/when-will-agi-arrive/) of 80,000 Hours:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/8bd0b657-71a8-418f-8ef9-400a4b699be8/Illustrative+PDF+%2880k%29.png?format=2500w)

Dwarkesh Patel reproduced it in his [post about AI timelines](https://www.dwarkesh.com/p/timelines-june-2025), saying that it pretty much represented his own uncertainty, giving his median date of 2032 for AI that “learns on the job as easily, organically, seamlessly, and quickly as a human, for any white-collar work.”

Here is Metaculus’s [current community estimate for when AGI will be developed](https://www.metaculus.com/questions/5121/date-of-artificial-general-intelligence/). Synthesizing the community’s collective uncertainty, it is very broad and has this same characteristic shape:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/e95a8394-3fe5-4abf-ac1d-03d2ebe9fa86/Metaculus+AGI+PDF+%286+Feb+2026%29.png?format=2500w)

Here is Epoch AI’s [summary of leading estimates](https://epoch.ai/blog/literature-review-of-transformative-artificial-intelligence-timelines) of AI timelines from 2023:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/a8d1b552-903a-4218-8730-6ee82cdce37d/Epoch%27s+summary+of+CDFs.png?format=2500w)

These look a bit different as they are represented as cumulative probabilities of reaching transformative AI by a given time. But they are all very broad. Take a look at the range of years between when they cross 10% to when they cross 90%. Every single one has an 80%-interval at least 50 years wide.

What about researchers working on AI capabilities? [Grace et al](https://aiimpacts.org/wp-content/uploads/2023/04/Thousands_of_AI_authors_on_the_future_of_AI.pdf) surveyed thousands of AI researchers who were presenting at their top academic conferences. They surveyed the researchers in 2022 (blue) and 2023 (red) about when “unaided machines can accomplish every task better and more cheaply than human workers”:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/c52a65cf-9373-4db9-ac70-265556fde0b0/Grace+et+al+HLMI+CDFs.png?format=2500w)

You can see the wild variation in individual forecasts (the thin lines) and that the timelines became about 30% shorter in a single year. But vast uncertainty remains. The aggregate community forecasts (the thick lines) have 80% intervals ranging from years to centuries.

I think everyone should have a distribution that is roughly this shape. Here’s mine:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/1fd525c1-de14-43b8-b2fa-4cde84aadc71/My+Distribution.png?format=2500w)

It is for transformative AI, loosely defined as AI that would be powerful enough to take over the world were it misaligned, and which is doubling the rate of scientific and technological progress. It’s a similar shape to Kokotajlo’s, but broader, with a median of 2038 and an 80% interval ranging from 3 years to 100 years.

Let’s return to where we started, with Daniel Kokotajlo’s distribution for AI that is “At least as good as top human experts at virtually all cognitive tasks”:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/f9e30b4d-266f-4997-a917-17df4063ca43/Daniel+Kokotaljo+PDF.png?format=2500w)

While we often express our timelines as single numbers (such as the mode or the median), I don’t think that’s a helpful approach here. Look at that graph. What number sums it up? Its only real feature is the peak, but Kokotajlo is saying it is unlikely to happen by then (just a 27% chance). The median is often a better number to give, but here it is at a relatively undistinguished point on the graph (in 4 years’ time) and saying ‘4 years’ would obscure his point that he thinks there is a 10% chance it is within 1 year and a 10% chance it is beyond 25 years.

I think that if he talked through what he actually means by this distribution with a smart policy maker, they would finally get it and say:

> Oh, so you are saying *you have no idea when it will happen* — it could be next year, or it could be 6 presidential terms from now*.* And you’re saying there is a 1 in 5 chance it isn’t even in that range.

I think that’s actually a pretty good summary, and it would sum up my own distribution as well. While ‘no idea when it will happen’ is underselling the information contained in this distribution, it is a much better summary than ‘4 years’ which would be understood by almost everyone as something like ‘between 3 and 5 years’. While academics might hope people interpret a named year as the median time, most people interpret it as the moment they are allowed to start complaining the predicted event hasn’t happened yet.

Indeed, these distributions are so hard to sum up with a single number, that I think a substantial amount of disagreement on timelines stems from people describing different parts of [the same elephant](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant). For example, both AI boosters and those concerned with existential risk talk a lot about short timelines because ‘we could see the world transformed in just a few years’ time’. It isn’t that they think we *will* see that, but that it is *big if true*, and has a decent chance of being true. In contrast, more conservative voices tend to focus on later years saying ‘it is more likely that it will take 10 to 20 years, than that it will take just a few’ (focusing on straight probability without weighting by importance or leverage).

Both of these can be true at the same time. Both are true on my own distribution.

A particular danger in communicating timelines with a single number is that it raises the chance that this named year will come and go without incident, and the people who mentioned it (or the wider community they are part of) will be written off as having a false or discredited view. I think we’re going to see some of this come 2027 due to the vast number of people who heard about that scenario, combined with the fact that so many media outlets reported it as a sharp prediction, rather than as it was intended: an important illustrative scenario.

As well as being bad for communication, compressing one’s uncertainty into a single number would be very bad for your own planning.

For example Kokotajlo’s distribution implies a 28% chance transformative AI will happen during the current presidential term, a 35% chance it will happen in the next term, a 13% chance it will be the one after that, with 24% left over spread among ever more distant terms:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/dba3a232-5c2d-4ce0-8ec1-ba44f1ddb42c/Daniel+Kokotaljo%27s+PDF+%28annotated%29.png?format=2500w)

These are very different scenarios and it would clearly be a mistake to just act as if the second one were correct since it is the most likely. That would eliminate the possibility of hedging against transformative AI coming soon, and of taking advantage of worlds where it comes late.

## Implications

Rather than attempting to adjudicate which length of timelines is correct, I think we should be taking the frame of how to act (or plan) under deeply uncertain timelines.

That is, we should be treating this as an exercise in rational decision-making under uncertainty — in a situation where the stakes are high and the uncertainty is vast.

Let’s unpack some of the implications of this frame.

We’ll start with two mistakes that are all too common in the policy world.

First, uncertainty about AI timelines isn’t an excuse to just believe whichever timeline you want, so long as it is within the credible range. Sadly, I think many government ministers are likely to take this approach if an expert explains this broad uncertainty to them. While they would be right that the evidence isn’t sufficient to disprove their preferred timeline, it would be irresponsible of them to not allow for other credible possibilities. That would be like a mayor hearing there is a 20% chance the volcano next to their town erupts next year and feeling that they can continue to act as if it won’t, since it not erupting is also found credible by the experts. Uncertainty isn’t an excuse to assume a plausible outcome of your choice will occur, it is more that rationality requires you to respect every plausible outcome.

Second, we can’t just wait until the uncertainty is resolved. Sometimes that works, but here we know the uncertainty is very unlikely to be resolved until the events are upon us. At that stage it will be too late to enact all but the most knee-jerk responses. So feeling that the cloud of uncertainty gives you permission to delay acting is tantamount to committing to choose one of the bluntest and least effective options available.

Instead, we are going to need to act under uncertainty, taking into account the full range of credible possibilities.

How can we do that?

## Hedging

A natural and important idea is that of *hedging* against transformative AI coming soon —while we are least prepared. We could do that by shifting our portfolio of activities (or your individual contribution to humanity’s portfolio) to focus somewhat more on short timelines than the raw probabilities would warrant.

This makes a lot of sense. I strongly recommend governments, civil society, and academics do more to hedge against transformative AI coming early.

Though when it comes to the communities of professionals already working on helping the AI transition go well, I think they are already hedging strongly against early transformative AI. Indeed, there is even a risk that they are going beyond mere hedging, and are actively betting on it coming early. I’m not sure, as it is hard to know the full portfolio of work.

One certainly sees many more pleas for work aimed at very short timelines than for long timelines. But there are also strong reasons to consider long timelines in our planning, and ways in which work aimed at long timelines can also be extremely high leverage.

Let’s look at two key things that happen when timelines are longer.

## A Different World

In longer timelines, AI arrives in a world that doesn’t look like today. The longer it is until transformative AI appears, the more different the world will be at that key moment.

As a baseline, suppose it arrives soon, in 2028. Things will definitely be different to today, but we’d expect many of the broad brushstrokes to be similar. We would likely have the same US president, the same major players, the same main technologies. If transformative AI arrived within just two years, I’d bet it was something like the AI 2027 story where a lab recklessly got recursive self-improvement going.

Now suppose transformative AI arrives in 2035. That is not this presidential term or even the next one, but the one after that. Who knows who’d be in power, or what state the US would be in. The nine years would likely have seen major changes in the core technologies of AI (9 years before now there were no LLMs or transformers). We could well have different leading AI companies, perhaps as a result of a bubble having burst and taken out the overextended first-movers.

By 2035, export controls may well have backfired, helping China get ahead on chips by incentivising them to build out their own chip industry and giving them 13 years to get good at it. This was a key dynamic the White House considered while drafting the export controls, but they were focused on shorter timelines… By 2035, China may have also invaded Taiwan, depriving the West of their biggest source of chips.

By 2035, there may be double-digit unemployment from increasingly powerful AI systems and public sentiment about AI could be very strong. The Overton window for AI regulation will be in a very different place.

As may be the geopolitical order. The last nine years has seen the invasion of Ukraine, the increasing isolation of the US and a global pandemic. Another nine years could see a similar amount of change.

And if we haven’t played our cards right, those of us working on avoiding catastrophic risks from AI may have also lost a lot of power, with our ideas about AI risk being seen as discredited since so many years have passed without the truly transformative effects we were talking about.

In short, the longer the timelines the more different things will be — both in some systematic, predictable ways, and just from random diffusion and chaos. So taking longer timelines seriously means:

- Being more open to approaches that wouldn’t work in the world as it is today,
- Being less excited about approaches that are tailored to specifics of today’s world,
- Being less happy to compromise your values to appeal to those currently in control of companies and governments,
- Being less willing to say things that will make people feel our position is discredited if we end up in a long timeline world,
- And spending less time following the daily news about what has just happened in AI or who is ahead.

## Longterm actions

There are many kinds of things people can work on that can pay off handsomely, but only after a number of years. Things like:

- Founding and nurturing a new research field
- Founding an organisation or company
- Building a movement or community
- Writing a book
- Foundational research
- Completing a PhD
- A major career change
- Climbing the ladder in a large organisation or government
- Training promising students in AI Safety or AI Governance

If you just consider your impact during the next three years, most of these will be beaten by other shorter-term options. But as the years climb, longer-term options can have very high value. They aren’t always best, but for the right people or the right opportunities, they can be extremely impactful.

When I was a grad student, I realised how much good I could achieve if I donated much of my income over my career to help those in the poorest countries. And the more I thought about it, the more I thought I should start something — an organisation — to help other people to do this too. So Will MacAskill and I launched [Giving What We Can](https://www.givingwhatwecan.org/) in 2009. 17 years later, more than 10,000 people have joined us, having thousands of times as much impact as if I’d carried on alone.

This kind of compounding growth is one of the major ways that longer term projects can have very large multipliers, giving us a very big boost to our impact if timelines are in fact long.

Starting new fields can be similar. When I first met Allan Dafoe 10 years ago, I didn’t know what he was talking about when he spoke of ‘AI governance’ — a new field he was trying to found. Now it is a burgeoning field, with hundreds of practitioners, who are in high demand from many different governments.

When I started writing [*The Precipice*](https://theprecipice.com/), I wasn’t sure I should, because I thought AGI might just be too close. But as it turns out, there was time to write it and for it to have a real impact. I’m really glad I did, as I meet so many amazing people working on the biggest risks who tell me it was reading *The Precipice* that inspired them to do so. I think it is one of the best things I’ve done.

After it came out, I used to think that there just wasn’t enough time to write a further book — that we were really too close to the critical moment. We might be, but I think I was mistaken about the strength of this argument. The time horizon for a book to have real impact is about 5 years (time to plan the book, win a book deal, write the book, wait for publishers to publish it, then wait a year or more before it has sufficient impact in the world).

But I only think there is about a 1 in 5 chance of transformative AI coming in the next 5 years. So while a book may come out too late, that is only a 1 in 5 chance, leaving a book project with 80% as much expected value as I’d have naively calculated. So while there is a 1 in 5 chance I’d be kicking myself, on my views about AI timelines there isn’t actually that much of a haircut in expected value due to the chance it is too late.

That said, the chance of transformative AI arriving before your work pays off is only one factor affecting whether you should do work aiming at short or long timelines. Another is that AI safety and governance are likely to be more neglected now than they will be later. This creates an extra multiplier for the value of direct work in these areas now, and in some cases is a larger effect than the chance your work comes to fruition after transformative AI.

Overall, I think that longer term projects do get down-weighted by these considerations, but their advantages sometimes outweigh that — especially if they are shooting for a very big payoff. I’d guess that if someone looked at their options and thought the best option was one that took 5 to 10 years to pay off, then about half the time it would remain their best option even after taking AI timelines into consideration. After all, it is not uncommon for your best option to be several times better than your second best.

So I think the community of people working on transformative AI are likely underrating types of work that need five or more years in order to pay off. The ideal portfolio of activities aimed at making the AI transition go well should include a number of things that really help us succeed in worlds where we get longer to try.

But I want to stress that none of this implies we can slack off.

We’re in a race against AI timelines. It is just that we don’t know if that race is a sprint or a marathon. In either case, time is of the essence.

## Conclusions

We have seen that there is substantial disagreement and uncertainty about when AI will start having transformative impacts on the world. This is because there just isn’t enough evidence to pin it down. My claim is that for the purposes of planning we should adopt neither short nor long timelines, but *broad timelines*:

The correct epistemic response to the lasting expert disagreement is to have a broad distribution over AI timelines.

Given this deep uncertainty we need to act with epistemic humility. We have to take seriously the possibility it will come soon and hedge against that. But we also have to take seriously the possibility that it comes late and take advantage of the opportunities that would afford us. The world at large is doing too little of the former, but those of us who care most about making the AI transition go well might be doing too little of the latter.

We need to take more seriously the possibility that the world will look very different at that time, which should broaden our own Overton windows about what kinds of plans could succeed. And we shouldn’t be ruling out all actions which take a long time to pay off. Even if they wouldn’t help in short timelines worlds, some actions more than make up for this with substantial impacts if timelines are long.

Funders, career advisors, and movement builders should be thinking about this with regards to how we act as a community: to the shape of the whole portfolio of work aimed at effectively improving the world. And each of us should be reflecting on what this deeply uncertain timing means for planning our own contributions over the years to come.

## Hazard Rates for AI Agents Decline as a Task Goes On

## Toby Ord

Contrary to [my earlier hypothesis](https://www.tobyord.com/writing/half-life), AI agents probably *don't* have a constant hazard rate / half-life. Instead their hazard rates systematically decline as the task goes on.

This means that AI agents’ success rates on tasks beyond their 50%-horizon are better than my constant-hazard-rate model suggests, but those for tasks shorter than the 50% horizon are worse.

I have previously suggested a constant hazard rate was a good starting assumption for how their success rate at tasks decays with longer durations. It is the simplest model and fits the data reasonably well. So I thought there was a strong case for it being the default, or null hypothesis, that would take some evidence to overturn.

But some [excellent new analysis by Gus Hamilton](https://gushamilton.github.io/lab/2026/01/23/petos-paradox-ai-agents/) provides this evidence. He used the standard second-simplest model from survival analysis (the [Weibull distribution](https://www.google.com/url?opi=89978449&rct=j&sa=t&source=web&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FWeibull_distribution&usg=AOvVaw27s3PAZJl998x8YC3RvV5Y&ved=2ahUKEwjOzKzYrcCSAxWYQ0EAHSd9GpQQFnoECB0QAQ) rather than the exponential distribution). It has a second parameter, *k*, which represents how the hazard rate changes with time (if at all). If *k* = 1, there is a constant hazard rate (so the exponential distribution is a special case of the Weibull). But if *k* < 1, then hazard decreases over time (like the [Lindy effect](https://arxiv.org/pdf/2308.09045)), and if *k* > 1, hazard increases (like aging).

Gus found that the estimated values for *k* were below 1 for all the models, showing that *all* of them had decreasing hazard rates as the task went on.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/f7f22cbc-9d79-4112-90ab-c6e71d228d60/Figure1.png?format=2500w)

A distribution that generalises another is always going to get a better fit of the data. So fit alone wouldn't be decisive when comparing the Weibull to the exponential distribution. But the way that every single model has *k* statistically significantly below 1 convinces me he is right. His model extends my approach of using survival-analysis as a lens through which to view the METR time horizons, and sees further through that lens than I did.

Note that values of *k* for different models are all quite clustered around 0.6, with little change in *k* as models improved over the years. In contrast, the improvement in METR timelines was being driven by changes in the Weibull distribution’s other parameter, λ, which uniformly shrinks the hazard rate at all times:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/8c1c726b-4a5b-46b0-bbe5-d10fb965b05c/Figure2.png?format=2500w)

**So what does all this imply?**

One thing is that it implies very different estimated success rates for tasks much shorter or longer than the 50% horizon (which METR focuses on because it is easier to reliably estimate). So one should use the Weibull distribution rather than the exponential distribution to estimate the 99% horizon (or 10% horizon).

Another thing is that the AI agents mainly have a *k* of about 0.6, while the human value of *k* is significantly lower, at about 0.37. This means even were they to have the same 50% horizon, humans would have a higher success rate on really long tasks (but a lower rate on really short ones).

As this shows, for a fixed 50% horizon length, it isn't clearly better or worse to have a lower value of *k*. Lower values are useful for the higher success rate really long tasks, but are worse on short tasks. As *k* gets lower, those tasks need to be even shorter to reach high standards like 99%. Since the exponential distribution is a Weibull with *k* = 1, but the measured value of k is lower, the 99% time horizon of these models is probably shorter than you’d expect if you were previously using my constant hazard rate model to estimate it.

As a word of warning, I’d seen Gus’s preliminary results prior to METR adding the data for Opus 4.5 and was quite sure that it would have a more human-like value of *k* since it had a great 50% horizon length, but only an average showing at the 80% reliability threshold. But the estimates are that its value of *k* are similar to other AI agents, while its value of λ are similar to humans. I'm pretty puzzled by this, as a change in *k* would perfectly explain this surprising discrepancy between its 50% and 80% thresholds. I am not sure what is going on, but it might be due to the fact that there isn't much data to go on here and things are quite noisy for any individual model.

So, from Gus's results, it still looks like there is some important gap between how human success rates drop off at longer tasks versus how AI agents do.

Finally, Gus also compares his two-parameter Weibull model of the data to METR's two-parameter log-logistic model. He finds that they are similar, but with the log-logistic fitting slightly better. So it isn't clear which of these to use if you have the choice. They differ quite a lot in the tails of the distribution (i.e. in estimated success rates for very short or very long tasks).

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/2d77bc14-a126-4124-b8bd-c7e3701d5dd1/Figure6.png?format=2500w)

e.g. the Weibull says the 99% horizon is 1/20th as long as the log-logistic predicts. That's a crucial difference and the data doesn't tell us which to favour! I'd slightly favour the Weibull, on the grounds that it is more plausible *ex ante*. But maybe the bigger lesson is that it is unknown which is right, and thus the 99%-reliability horizons (a threshold that is necessary for much useful work) are deeply uncertain.

## Are the Costs of AI Agents Also Rising Exponentially?

## Toby Ord

There is an extremely important question about the near-future of AI that almost no-one is asking.

We’ve all seen the graphs from METR showing that the length of tasks AI agents can perform has been growing exponentially over the last 7 years. While GPT-2 could only do software engineering tasks that would take someone a few seconds, the latest models can (50% of the time) do tasks that would take a human a few hours.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/8b1fd882-f8f8-4879-a008-18902ece6edd/METR+time+horizon+%28log%29.png?format=2500w)

As this trend shows no signs of stopping, people have naturally taken to extrapolating it out, to forecast when we might expect AI to be able to do tasks that take an engineer a full work-day; or week; or year.

But we are missing a key piece of information — the cost of performing this work.

Over those 7 years AI systems have grown exponentially. The size of the models (parameter count) has grown by 4,000x and the number of times they are run in each task (tokens generated) has grown by about 100,000x. AI researchers have also found massive efficiencies, but it is eminently plausible that the cost for the peak performance measured by METR has been growing — and growing exponentially.

This might not be so bad. For example, if the best AI agents are able to complete tasks that are 3x longer each year and the costs to do so are also increasing by 3x each year, then the cost to have an AI agent perform tasks would remain the same multiple of what it costs a human to do those tasks. Or if the costs have a longer doubling time than the time-horizons, then the AI-systems would be getting cheaper compared with humans.

But what if the costs are growing more quickly than the time horizons? In that case, these cutting-edge AI systems would be getting less cost-competitive with humans over time. If so, the METR time-horizon trend could be misleading. It would be showing how the state of the art is improving, but part of this progress would be due to more and more lavish expenditure on compute so it would be diverging from what is economical. It would be becoming more like the Formula 1 of AI performance — showing what is possible, but not what is practical.

So in my view, a key question we need to ask is:

***How is the ‘hourly’ cost of AI agents changing over time?***

By ‘hourly’ cost I mean the financial cost of using an LLM to complete a task right at the model’s 50% time horizon divided by the length of that time horizon. So as with the METR time horizons themselves, the durations are measured not by how long it takes the model, but how long it typically takes humans to do that task. For example, Claude 4.1 Opus’s 50% time horizon is 2 hours: it can succeed in 50% of tasks that take human software engineers 2 hours. So we can look at how much it costs for it to perform such a task and divide by 2, to find its hourly rate for this work.

I’ve found that very few people are asking this question. And when I ask people what they think is happening to these costs over time, their opinions vary wildly. Some assume the total cost of a task is staying the same, even as the task length increases exponentially. That would imply an exponentially declining hourly rate. Others assume the total cost is also growing exponentially — after all, we’ve seen dramatic increases in the costs to access cutting-edge models. And most people (myself included) had little idea of how much it currently costs for AI agents to do an hour’s software engineering work. Are we talking cents? Dollars? Hundreds of dollars? An AI agent can’t cost more per hour than a human to complete these tasks can it? Can it?

⁂

A couple of months ago I asked METR if they could share the cost data for their benchmarking. I figured it would be easy — just take the cost of running their benchmark for each model, plot it against release date and see how it is growing. Or plot the cost of each model vs its time horizon and see the relationship.

But they helpfully pointed out that it isn’t so easy at all. Their headline time-horizon numbers are meant to show the best possible performance that can be attained with a model (regardless of cost). So they run their models inside an agent scaffold until the performance has plateaued. Since they really want to make sure it has plateaued, they use a *lot* of compute on this and don’t worry too much about whether they’ve used too much. After all, if you are just trying to find the eventual *height* of a plateau, there is no problem in going far into the flat part of the graph.

But if you are trying to find out when the plateau *begins*, there is a problem with this strategy. Their total spend for each model is sometimes just enough to get onto the plateau and sometimes many times more than is needed. So total spend can’t be used as direct estimate of the costs of achieving that performance.

Fortunately, they released a chart that can be used to shed some light on the key question of how hourly costs of LLM agents are changing over time:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/0187b2c9-d4fd-4fe7-a121-9187f87b5076/models_budget_comparison.png?format=2500w)

This chart (from [METR’s page for GPT-5](https://evaluations.metr.org/gpt-5-report/#time-horizon-measurement)) shows how performance increases with cost. The cost in question is the cost of using more and more tokens to complete the task (and thus more and more compute).

The yellow curve is the best human performance for each task. It steadily marches onwards and upwards, transforming more wages into longer tasks. Since it is human performance that is used to define the vertical axis for METR’s time horizon work, it isn’t surprising that this curve is fairly linear — it costs about 8 times as much to get a human software engineer to perform an 8-hour task as a 1-hour task.

The other colours are the curves for a selection of LLM-based agents. Unlike the humans, they all show diminishing returns, with the time horizon each one can achieve eventually stalling out and plateauing as more and more compute is added.

The short upticks at the end of some of these curves are an artefact of some models not being prepared to give an answer until the last available moment. This suggests that the model must have been still making progress during the apparent flatline before the uptick (just not showing it). Indeed, this chart was originally displayed on [METR’s page for GPT-5](https://evaluations.metr.org/gpt-5-report/#time-horizon-measurement) to show that they may have stopped its run before it’s performance had truly plateaued. These upticks do make analysis harder and hopefully future versions of this chart will be able to avoid these glitches.

⁂

So what can this chart tell us about our key question concerning the hourly cost of AI agents?

To tease out the lessons that lie hidden in the chart, we’ll need to add a number of annotations. The first step is to add lines of constant hourly cost. On a log-log plot like this, every constant hourly cost will be a straight line with slope 1. Lower hourly costs will appear as lines that are located further to the left.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/ea649c93-ca0c-44fb-a317-88197dead1b4/Sweet+Spots.png?format=2500w)

For each curve I’ve added a line of constant hourly cost that just grazes it. That is the cheapest hourly cost the model achieves. We can call the point where the line touches the curve the *sweet spot* for that model. Before a model’s sweet spot, its time horizon is growing super-linearly in cost — it is getting *increasing* marginal returns. The sweet spot is exactly the point at which diminishing marginal returns set in (which would correspond to the point of inflection if this was replotted on linear axes). It is thus a key point on any model’s performance curve.

We can see that the human software engineer is at best $120 per hour, while the sweet spots for the AI agents range from $40 per hour for o3, all the way down to 40 cents per hour for Grok 4 and Sonnet 3.5. That’s quite a range of costs. While differences in horizon length between these models vary by about a factor of 15 (judged at either the end-points or at the sweet-spots) their sweet-spot costs vary by a factor of 100.

And these are the best hourly rates for these models. On many task lengths (including those near their plateau) they cost 10 to 100 times as much per hour. For instance, Grok 4 is at $0.40 per hour at its sweet spot, but $13 per hour at the start of its final plateau. GPT-5 is about $13 per hour for tasks that take about 45 minutes, but $120 per hour for tasks that take 2 hours. And o3 actually costs $350 per hour (more than the human price) to achieve tasks at its full 1.5 hour task horizon. This is a lot of money to pay for an agent that fails at the task you’ve just paid for 50% of the time — especially in cases where failure is much worse than not having tried at all.

However, I do want to note that I’m a bit puzzled by how much higher the costs are here for the reasoning models from OpenAI compared to models from Anthropic and xAI. The METR page suggests that the price data for those models was still an estimate at that point (based on o1 costs), so I wouldn’t be surprised if these curves should really be shifted somewhat to the left, making them several times cheaper. We therefore shouldn’t lean too heavily on the fact that they cost as much or more than human labour at their full time-horizon.

As well as the sweet spot, ideally we could add a *saturation point* for each curve — a point to represent the location where the plateau begins. We can’t simply use the end of the curve since some have run longer into the plateau than others. What I’ll do is find the point where the slope has diminished to 1/10th that of the sweet spot. This is the point at which it requires a 10% increase in cost just to increase the time horizon by 1%. Or equivalently, the time horizon is only growing as the 1/10th power of compute.

Of course the number 1/10 is somewhat arbitrary, but unlike for the sweet spot, any definition of a saturation point will be arbitrary to some degree. As you can see below, this definition of saturation point does roughly correspond with the intuitive location, though it is still not quite clear how best to deal with the final upticks.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/fc9f69c2-aeee-4f25-91cc-a57e85b7a82a/Saturation+Points+alt.png?format=2500w)

⁂

Armed with our sweet spots and saturation points, we can start to tease out the relationship between time horizon and cost.

Let’s start with a sweet spot scatter plot:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/b44bf379-a37c-4086-9be5-a3b7f9426568/Sweet+Spot+Correlation.png?format=2500w)

We can see that there is a weak, but clear, positive correlation between task duration and cost in this dataset. Moreover, we see that higher task durations (at the sweet spot) are associated with higher hourly costs (and recall that these hourly costs at the sweet spot are the best hourly cost achievable with that model).

What about if we instead look at the models’ saturation points, which are a little arbitrary in their definition, but closer to what METR is measuring in their headline results about time horizons:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/b4ecb5eb-967d-4a57-a26c-3288d347789e/Saturation+Point+Correlation+alt.png?format=2500w)

Again, there is a correlation between time horizon and cost, and again the hourly costs seem to be increasing with time horizon too. Indeed it suggests we are nearing the point where the models’ peak performance comes at an impractically high cost. If this relationship were to continue, then forecasting when certain time horizons will be available from the headline METR trend will be misleading, as the models would be impractically expensive when they first reach those capabilities. We would need to wait some additional period of time for them to come down sufficiently in cost.

That said, there are some significant limitations to the analysis above. Ideally one would want to:

- include curves for a larger and more representative set of models
- find a way of addressing the uptick problem
- check if there is an issue with the costs of the OpenAI models
- explicitly plot hourly cost against release date
- numerically determine the trend-lines and correlation co-efficients

Fortunately, it should be fairly easy for METR to perform such analysis, and I hope they will follow up on this.

## Conclusions

- Too few people are asking about how the costs of AI agents are growing
- The key question is ***How is the ‘hourly’ cost of LLM agents changing over time?***
- We can use METR’s chart to shed some light on this.
- We need to add *lines of constant hourly cost*, *sweet spots*, and *saturation points*.
- This provides moderate evidence that:
	- the costs to achieve the time horizons are growing exponentially,
		- even the hourly costs are rising exponentially,
		- the hourly costs for some models are now close to human costs.
- Thus, there is evidence that:
	- the METR trend is partly driven by unsustainably increasing inference compute
		- there will be a divergence between what time horizon is possible in-principle and what is economically feasible
		- real-world applications of AI agents will lag behind the METR time-horizon trend by increasingly large amounts

## Appendix

### METR has a similar graph on their page for GPT-5.1 codex. It includes more models and compares them by token counts rather than dollar costs:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/ae144dee-9962-4942-b822-c1037966573a/models_50_time_horizon_over_resources.png?format=2500w)

It suggests:

1. the correlation between time horizon and cost holds for these other models too
2. reasoning models with more RL post-training don’t always dominate their predecessors (e.g. o1 is better at small token budgets than o3 or GPT-5)
3. the horizontal gap between the OpenAI reasoning models and the rest is smaller, supporting the idea that their costs were a bit high in the main chart

## How Well Does RL Scale?

## Toby Ord

The current era of improving AI capabilities using Reinforcement Learning (from verifiable rewards) involves two key types of scaling:

1. Scaling the amount of compute used for RL during training
2. Scaling the amount of compute used for inference during deployment

We can see (1) as training the AI in more effective reasoning techniques and (2) as allowing the model to think for longer. I’ll call the first *RL-scaling*, and the second *inference-scaling*. Both new kinds of scaling were present all the way back in OpenAI’s [announcement](https://openai.com/index/learning-to-reason-with-llms/) of their first reasoning model, o1, when they showed this famous chart:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/a37e4374-55d0-4635-96b8-0a335c878c65/o1+scaling.webp?format=2500w)

I’ve [previously shown](https://www.tobyord.com/writing/mostly-inference-scaling) that in the initial move from a base-model to a reasoning model, most of the performance gain came from unlocking the inference-scaling. The RL training did provide a notable boost to performance, even holding the number of tokens in the chain of thought fixed. You can see this *RL boost* in the chart below as the small blue arrow on the left that takes the base model up to the trend-line for the reasoning model. But this RL also unlocked the ability to productively use much longer chains of thought (~30x longer in this example). And these longer chains of thought contributed a much larger boost.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/1bb66275-e4ed-4a1e-9599-4e0ea5c43e54/MATH+%E2%80%93+level+5.png?format=2500w)

The question of where these capability gains come from is important because scaling up the inference compute has very different implications than scaling up the training compute. In this first round of reasoning models, they were trained with a very small amount of RL compute compared to the compute used in pre-training, meaning that the total cost of training was something like 1.01x higher than the base-model. But if most of the headline performance results require 30x as much inference compute, then the costs of deploying the those capabilities is 30x higher. Since frontier AI developers are already spending more money deploying their models than they did training them, multiplying those costs by 30x is a big deal. Moreover, these are costs that have to be paid every time you want to use the model at this level of capability, so can’t be made up in volume.

But that was just the initial application of RL to LLMs. What happens as companies create more advanced reasoning models, using more RL?

The seeds of the answer can be found all the way back in that original o1 chart.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/fa51bcb0-2984-4524-a900-926d68dee6e2/o1+with+trend.png?format=2500w)

The chart shows steady improvements for both RL-scaling and inference-scaling, but they are not the same. Both graphs have the same y-axis and (despite the numbers being removed from the x-axis) we can see that they are both on a logarithmic x-axis covering almost exactly two orders of magnitude of scaling (100x). In both cases, the datapoints lie on a relatively straight line, which is presumably the central part of a larger S-curve. However, the slope of the RL-scaling graph (on the left) is almost exactly half that of the slope of the inference-scaling graph (on the right). [When the x-axis is logarithmic](https://www.tobyord.com/writing/inference-scaling-and-the-log-x-chart), this has dramatic consequences.

The graph on the right shows that scaling inference-compute by 100x is enough to drive performance from roughly 20% to 80% on the AIME benchmark. This is pretty typical for inference scaling, where quite a variety of different models and benchmarks see performance improve from 20% to 80% when inference is scaled by 100x.

For instance, this is what was found with Anthropic’s first reasoning model (Sonnet 3.7) on another AIME benchmark, with almost exactly the same scaling behaviour:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/bc9b74d0-964b-4c16-93b6-923728e2e8db/Mock+AIME+%2820-80%29.png?format=2500w)

And ability on the ARC-AGI 1 benchmark also scales in a similar way for many of OpenAI’s different reasoning models:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/cd8734a7-3e39-42de-b8ba-2df22dfd8030/ARC-AGI+%2820-80%29.png?format=2500w)

We don’t always see this scaling behaviour for inference: some combinations of LLM, inference-scaling technique, and benchmark see the performance plateau below 80% or exhibit a different slope (often worse). But this climb from 20 to 80 with 100x more inference compute is pretty common (especially for reasoning-intensive benchmarks) and almost certainly what is happening on that original o1 graph.

In contrast, the slope of the RL-scaling trend is half as large, which means that it requires *twice as many orders of magnitude* to achieve the exact same improvement in capabilities. Increasing the RL training compute by 100x as shown in the o1 chart only improved performance from about 33% to 66%. At that rate, going from 20 to 80 would require scaling up the RL training compute by 10,000x.

We can confirm this trend — and that it continued beyond o1 — by looking at the following graph from the [o3 launch video](https://www.youtube.com/live/sq8GBPUb3rk?si=it_Jb9IOSexAHIQU&t=1134) (with a line added showing the slope corresponding to going from 20 to 80 in 10,000x):

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/b8f2973a-ae1e-4a99-ac67-ef4a255b8d39/o1-o3+training+on+AIME.png?format=2500w)

Using another version of the AIME benchmark, this shows o1’s training progress over 3 orders of magnitude and o3’s training over a further order of magnitude. In total, we see that scaling up the RL-training by 4 orders of magnitude takes the model from about 26% to 88%. This provides some confirmation for the rule-of-thumb that a 10,000x scale-up in RL training compute is required to improve this benchmark performance from 20 to 80.

To my knowledge, OpenAI hasn’t provided RL-training curves for other benchmarks, but they do have charts comparing o1 with o3 and o3 with GPT-5 at different inference-scaling levels on several benchmarks. Given that o3 used about 10x as much RL training as o1, we’d expect the RL boost going from o1 to o3 to be worth about the same as the inference boost of giving o1 just half an order of magnitude more inference (~3x as many tokens). And this is indeed what one sees on their performance/token graph comparing the two:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/f20ed647-9e87-4e3b-9ae5-58fafaa0a65d/o1-o3+diff.png?format=2500w)

Similarly, o3 also requires about 3x as many tokens to match GPT-5 on the SWE-bench and GPQA Diamond benchmarks. This would fit the expected pattern of GPT-5 having been trained with a further 10x as much RL training compute as o3:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/ceb9b535-de09-4c48-91a2-b710fb13d30c/o3-GPT-5+diff.png?format=2500w)

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/538a39d0-2c6b-48bd-990e-cd47c06b29b4/o3-GPT5+GPQA+diff.png?format=2500w)

It is hard to verify that this trend holds for models from other companies, as this data on training curves for cutting-edge models is often treated as confidential. But the fact that other leading labs’ base models and reasoning models are roughly on par with OpenAI’s suggests none of them are scaling notably better than this.

So the evidence on RL-scaling and inference-scaling supports a general pattern:

- a 10x scaling of RL is required to get the same performance boost as a 3x scaling of inference
- a 10,000x scaling of RL is required to get the same performance boost as a 100x scaling of inference

In general, to get the same benefit from RL-scaling as from inference-scaling required *twice as many orders of magnitude*. That’s not good.

## How do these compare to pre-training scaling?

The jumps from GPT-1 to 2 to 3 to 4 each involved scaling up the pre-training compute by about 100x. How much of the RL-scaling or inference-scaling would be required to give a similar boost? While I can’t say for sure, we can put together the clues we have and take an educated guess.

[Jones (2021)](https://arxiv.org/abs/2104.03113) and [EpochAI](https://epoch.ai/blog/trading-off-compute-in-training-and-inference) both estimate that you need to scale-up inference by roughly 1,000x to reach the same capability you’d get from a 100x scale-up of training. And since the evidence from o1 and o3 suggests we need about twice as many orders of magnitude of RL-scaling compared with inference-scaling, this implies we need something like a 1,000,000x scale-up of total RL compute to give a boost similar to a GPT level.

This is breathtakingly inefficient scaling. But it fits with the extreme [information inefficiency of RL training](https://www.tobyord.com/writing/inefficiency-of-reinforcement-learning), which (compared to next-token-prediction) receives less than a ten-thousandth as much information to learn from per FLOP of training compute.

Yet despite the poor scaling behaviour, RL training has so far been a good deal. This is solely because the scaling of RL compute began from such a small base compared with the massive amount of pre-training compute invested in today’s models. While AI labs are reticent to share information about how much compute has actually been spent on RL (witness the removal of all numbers from the twin o1 scaling graphs), it is widely believed that even the 10,000x RL-scaling we saw for o3’s training still ended up using much less compute than the ~ $10^{25}$ FLOP spent on pre-training. This means that OpenAI (and their competitors) have effectively got those early gains from RL-training for free.

For example, if the 10x scaling of RL compute from o1 to o3 took them from a total of 1.01x the pre-training compute to 1.1x, then the 10x scale-up came at the price of a 1.1x scale-up in overall training costs. If that gives the same performance boost as using 3x as many reasoning tokens (which would multiply all deployment costs of reasoning models by 3) then it is a great deal for a company that deploys its model so widely.

But this changes dramatically once RL-training reaches and then exceeds the size of the pre-training compute. In July 2025, xAI’s Grok 4 launch video included a chart suggesting that they had reached this level (where pre-training compute is shown in white and RL-training compute in orange):

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/41d38c7a-3cd0-4605-9c31-3e021a181c9c/Grok+4+training.png?format=2500w)

Scaling RL by another 10x beyond this point increases the total training compute by 5.5x, and beyond that it is basically the full 10x increase to all training costs. So this is the point where the fact that they get much less for a 10x scale-up of RL compute compared with 10x scale-ups in pre-training or inference really bites. I estimate that at the time of writing (Oct 2025), we’ve already seen something like a 1,000,000x scale-up in RL training and it required ≤2x the total training cost. But the next 1,000,000x scale-up would require 1,000,000x the total training cost, which is not possible in the foreseeable future.

Grok 4 was trained on 200,000 GPUs located in xAI’s vast Colossus datacenter. To achieve the equivalent of a GPT-level jump through RL would (according to the rough scaling relationships above) require 1,000,000x the total training compute. To put that in perspective, it would require replacing every GPU in their datacenter with 5 entirely new datacenters of the same size, then using 5 years worth of the entire world’s electricity production to train the model. So it looks infeasible for further scaling of RL-training compute to give even a single GPT-level boost.

I don’t think OpenAI, Google, or Anthropic have quite reached the point where RL training compute matches the pre-training compute. But they are probably not far off. So while we may see another jump in reasoning ability beyond GPT-5 by scaling RL training a further 10x, I think that is the end of the line for cheap RL-scaling.

## Conclusion

The shift towards RL allowed the scaling era to continue even after pre-training scaling had stalled. It did so via two different mechanisms: scaling up the RL training compute and scaling up the inference compute.

Scaling RL training allowed the model to learn for itself how to achieve better performance. Unlike the imitation learning of next-token-prediction, RL training has a track record of allowing systems to burst through the human level — finding new ways of solving problems that go beyond its training data. But in the context of LLMs, it scales poorly. We’ve seen impressive gains, but these were only viable when starting from such a low base. We have reached the point where it is too expensive to go much further.

This leaves us with inference-scaling as the remaining form of compute-scaling. RL helped enable inference-scaling via longer chain of thought and, when it comes to LLMs, that may be its most important legacy. But inference-scaling has very different dynamics to scaling up the training compute. For one thing, it scales up the flow of ongoing costs instead of scaling the one-off training cost. This has [many consequences for AI deployment, AI risk, and AI governance](https://www.tobyord.com/writing/inference-scaling-reshapes-ai-governance).

But perhaps more importantly, inference-scaling is really a way of improving capabilities by allowing the model more time to solve the problem, rather than by increasing its intelligence. Now that RL-training is nearing its effective limit, we may have lost the ability to effectively turn more compute into more intelligence.

## Evidence that Recent AI Gains are Mostly from Inference-Scaling

## Toby Ord

In the last year or two, the most important trend in modern AI came to an end. The scaling-up of computational resources used to train ever-larger AI models through next-token prediction (*pre-training*) stalled out. Since late 2024, we’ve seen a new trend of using reinforcement learning (RL) in the second stage of training (*post-training*). Through RL, the AI models learn to do superior chain-of-thought reasoning about the problem they are being asked to solve.

This new era involves scaling up two kinds of compute:

1. the amount of compute used in RL post-training
2. the amount of compute used every time the model answers a question

Industry insiders are excited about the first new kind of scaling, because the amount of compute needed for RL post-training started off being small compared to the tremendous amounts already used in next-token prediction pre-training. Thus, one could scale the RL post-training up by a factor of 10 or 100 before even doubling the total compute used to train the model.

But the second new kind of scaling is a problem. Major AI companies were already starting to spend more compute serving their models to customers than in the training phase. So if it costs a factor of 10 or 100 times as much to answer each question, this really does affect their bottom line. And unlike training costs, these costs can’t be made up in volume. This kind of scaling is known as [*inference-scaling*](https://www.tobyord.com/writing/inference-scaling-and-the-log-x-chart) (since it is scaling the compute used in the output, or ‘inference’, stage).

It is critical to find out how much of the benefits are coming from each kind of scaling. If further improvements in AI capabilities are mainly going to come from inference-scaling, this would have [many implications](https://www.tobyord.com/writing/inference-scaling-reshapes-ai-governance) for the trajectory of AI, including for AI companies, AI governance, and AI risk.

In past writings, I’ve mainly focused on the inference-scaling, treating RL as primarily enabling larger and larger amounts of inference to be productively used to answer a question — improving capabilities, but at a steep cost every time the AI system is deployed. However, it is probably more common in the AI discourse for people focus on the training costs of RL — treating it as a relatively cheap way to train a smarter model. In support of this view, people often point to the fact that even when reasoning models have thinking turned off, they still have superior performance on maths or science benchmarks compared with the base model that they were trained from.

For example, Anson Ho and Arden Berg from Epoch AI focus on this angle in their attempt to [quantify the algorithmic improvement from reasoning](https://epochai.substack.com/p/quantifying-the-algorithmic-improvement). However, they ultimately suggest that about half the benefit comes from the RL training (the shift from the base model to the no-thinking reasoning model) and half comes from scaling up the number of tokens that are used in reasoning. But as they note, despite producing zero hidden ‘reasoning tokens’ the no-thinking version of the reasoning model still had a chain of thought that was about twice as long as the base model. Ho and Berg address this qualitatively, as creating some uncertainty about their claim that half the gains come from each source.

But it is possible to do better — we can use this data as part of the analysis for finding out what fraction of performance increase is due to each type of scaling.

While it would be easy for people inside the leading AI companies to perform this analysis, it is more challenging with open data. A key thing is needing to have access to both a reasoning model and to the base model it started training from. In all my analysis I’ll follow Ho and Berg in using Anthropic’s Sonnet 3.7 as the reasoning model and assuming that Anthropic’s October 2024 release of Sonnet 3.5 (commonly called Sonnet 3.6 by the community) was its base model. (If that’s wrong and Sonnet 3.7’s base model incorporated improvements beyond ‘Sonnet 3.6’, that would only help my main conclusion.)

As always, it is instructive to first look at the raw scatter plot. Using the same [Epoch AI dataset](https://epoch.ai/benchmarks), here is a chart showing how benchmark performance (for MATH level 5) varies with the number of output tokens:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/a9e4adaf-4b8f-4e86-b7bf-ff285312b751/MATH+%E2%80%93+level+5+%28plain%29.png?format=2500w)

On this chart you can see a clear linear trend connecting the red data points of the RL-trained model. Since the x-axis is on a log-scale ([as it often is on inference-scaling charts](https://www.tobyord.com/writing/inference-scaling-and-the-log-x-chart)), this straight line actually represents performance increasing logarithmically with the number of tokens. Or, put another way, we require exponential growth in the number of tokens in the chain of thought to keep performance increasing linearly. This is typical for inference-scaling and is generally regarded by the industry as good scaling behaviour.

Note how the orange square representing the base model is slightly below this trend. This same pattern appears for the two other benchmarks I checked:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/75b4b2c3-4c90-4dbb-9ae1-acfee3730784/GPQA+Diamond+%28plain%29.png?format=2500w)

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/ad869729-275c-4cbc-9c1d-942f54588d9f/Mock+AIME+%28plain%29.png?format=2500w)

We can use these charts to find out how much of the performance boost is coming from scaling up inference compute versus how much is coming from RL making the model perform better for a given compute budget.

The key thing is to find the inference-scaling trend and then see how far below that trend the base model falls. That performance-gap between what the base model achieves and what the RLed model would achieve using the same number of tokens gives us the ‘RL boost’ — the portion of the improvement that wasn’t driven by more spending compute at test time. We can see below that the RL Boost for MATH level 5 is quite small at just 6 percentage points. But the RL training also teaches the model how to productively use reasoning chains up to 30 times as long. This costs 30x as much money every time the model is used, but enables a further boost of 28 percentage points via inference-scaling. So in this case, the total performance boost is 34 percentage points with 82% of this coming from inference-scaling.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/76901314-14d8-4196-a869-25f2540efeca/MATH+%E2%80%93+level+5.png?format=2500w)

We see similar results on the other two benchmarks I analysed. There was a somewhat better showing from the RL boost (at a fixed compute budget) for GPQA Diamond, but most of the gains were still coming from inference-scaling, requiring more than 10x as much compute each time the model is used:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/9becd7f0-e0e2-4e32-9641-91c8824fbc6a/GPQA+Diamond.png?format=2500w)

For GPQA Diamond, the boosts are 9 percentage points and 15 percentage points respectively, with 63% of the total coming from inference-scaling.

And for the OTIS Mock AIME benchmark, an even larger fraction of the benefit was coming from the inference-scaling boost:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/0a0928d0-a39c-4fb8-aa5b-84c39a567ee7/Mock+AIME.png?format=2500w)

Here there is just 4 percentage points from the RL Boost and 45 percentage points from inference-scaling, so the inference-scaling is producing 92% of the total gain.

In this case, some of this extreme ratio is being driven by the straightness of the trend-line. Since performance is capped between 0% and 100%, we know the trend cannot be straight forever. When we are so close to one of the bounds it is probably more accurate to use some kind of sigmoid trend-line. But no matter what kind of sigmoid we fit, the RL boost is still substantially smaller than the inference-scaling boost (and smaller in proportional terms too):

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/2b544f96-bb5b-495c-aba9-ce53bd9424ab/Mock+AIME+sigmoid.png?format=2500w)

So that’s the simple case that most of the gains from RL-scaling are driven by the inference-scaling it opens up.

One obvious piece of further work would be to extend this analysis to models from other companies.

And an even more important piece of further work would be to examine the changes between generations of reasoning models. In particular, how would scaling up the RL post-training by a factor of 10 affect the inference-scaling trend-line? It would presumably move it up or left and might change its slope (though the [ARC-AGI leaderboard suggests](https://arcprize.org/leaderboard) the slope usually stays the same). This extra RL training would presumably also enable longer chains of thought and thus more inference-scaling. The relationship between these two kinds of changes would determine whether further scaling of RL changes the importance of the RL boost compared to that of inference-scaling.

Alas, it is challenging for people outside the major labs to get the data to check this as simply using data from publicly released models will include gains from all other non-RL sources, inflating the apparent RL boost.

For now, I think the graphs we’ve seen here make a strong case that most of the gains from using RL to train reasoning models have been coming from scaling-up the number of tokens used to solve the task. This creates a flow of costs that have to be paid every time you use the model, [substantially changing the business model, the risk profile, and the policy response](https://www.tobyord.com/writing/inference-scaling-reshapes-ai-governance).

## The Extreme Inefficiency of RL for Frontier Models

## Toby Ord

*The new scaling paradigm for AI reduces the amount of information a model could learn per hour of training by a factor of 1,000 to 1,000,000. I explore what this means and its implications for scaling.*

[Read More](/writing/inefficiency-of-reinforcement-learning)

## Is there a Half-Life for the Success Rates of AI Agents?

## Toby Ord

Building on the recent empirical work of Kwa et al. (2025), I show that within their suite of research-engineering tasks the performance of AI agents on longer-duration tasks can be explained by an extremely simple mathematical model — a constant rate of failing during each minute a human would take to do the task. This implies an exponentially declining success rate with the length of the task and that each agent could be characterised by its own half-life. This empirical regularity allows us to estimate the success rate for an agent at different task lengths. And the fact that this model is a good fit for the data is suggestive of the underlying causes of failure on longer tasks — that they involve increasingly large sets of subtasks where failing any one fails the task. Whether this model applies more generally on other suites of tasks is unknown and an important subject for further work.

**METR’s results on the length of tasks agents can reliably complete**

A recent paper by [Kwa et al. (2025)](https://doi.org/10.48550/arXiv.2503.14499) from the research organisation [METR](https://metr.org/) has found an exponential trend in the duration of the tasks that frontier AI agents can solve: every 7 months, the length of task they can solve doubles.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/3ac5cc96-1407-48a0-80e4-ab8a226e3d6c/Figure+1.png?format=2500w)

These headline results are based on a test suite of 170 software engineering, cybersecurity, general reasoning, and ML tasks that they assembled to be indicative of the kinds of tasks that could help AI agents assist in AI research. These tasks are assembled from three different benchmarks that take different amounts of time for humans to achieve:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/0eed5814-5ddb-49a9-9ed1-2052bcc794f4/Figure+2.png?format=2500w)

In general, ability to perform a task drops off as its duration increases, so they use the AI agent’s performance on tasks of different lengths to estimate the task-length at which the model would have a 50% success rate. They then showed that this length has been doubling every 7 months as the capabilities of frontier agents improve. The task-lengths are measured by how long it took humans to solve the same tasks.

They used 50% success rate as their chief performance threshold because it is the easiest level to robustly estimate. They are well aware that for many tasks, the required success rate for useful work may be much higher — such as 80%, 99%, or 99.9999%. They do measure the 80% success rate and find their mean estimate to have a doubling time of 213 days, compared to 212 days of the 50% rate. These are close to identical within their margin of error (±40 days for the 50% rate), so they conclude that the particular threshold doesn’t seem to have much effect on their headline result about the rate of improvement.

But there is quite a gap between the 50% success rate time-horizon and the 80% success rate time horizon. For the best model (Claude 3.7 Sonnet) it could achieve a 50% success rate on tasks up to 59 minutes *vs* only 15 minutes if an 80% success rate was required. If those results generalise to the other models, then we could also see it like this: the task length for an 80% success rate is 1/4 the task length for a 50% success rate. Or in terms of improvement: what is doable with a 50% success rate now is doable with an 80% success rate in 14 months’ time (= 2 doubling times).

The idea of measuring improvement in AI capabilities over time via time horizons at a chosen success rate is novel and interesting. AI forecasting is often hamstrung by the lack of a good measure for the y-axis of performance over time. We can track progress within a particular benchmark, but these are often solved in a couple of years, and we lack a good measure of underlying capability that can span multiple benchmarks. METR’s measure allows comparisons between very different kinds of tasks in a common currency (time it takes a human) and shows a strikingly clear trend line — suggesting it is measuring something real.

But there are grounds for criticism too. In particular, there is room to wonder how much these results generalise outside of this kind of task suite. We know that there are some tasks humans can do very quickly that AIs can’t solve (e.g. some simple spatial reasoning or intuitive physics tasks) and others that would take humans an extremely long time, but AIs can do quickly (e.g. rote mathematics). So a simple measure of ‘time it would take a human’ cannot explain all AI capability improvements. Kwa et al. are aware of this and even list several other ways that this task-suite may be non-representative of real-world performance including:

- All tasks were automatically scorable (a domain where RL works best)
- No interaction with other agents
- Lax resource constraints

For the purposes of this essay, we will take the data for what it is (performance on a particular task suite that may or may not generalise further) and explore underlying mechanisms that could explain it.

### Explaining these results via a constant hazard rate

These results call out for some explanation of what is going on. For example, exactly how does the time horizon shrink as the required success probability is increased? And what does it *mean* for an agent to be able to perform an 8-hour task, but not a 16-hour task. Isn’t a 16-hour task just one 8-hour task after another?

[Survival analysis](https://en.wikipedia.org/wiki/Survival_analysis) is the field of understanding how the probability of something failing increases as a function of time. It tracks the survival probability at a time *S* (*t*) — that is, the chance it still hasn’t failed by that point. The simplest model in survival analysis is a constant hazard rate. This means that the chance of something failing in the next step (conditional on making it that far) is constant. A constant hazard rate leads to an exponentially declining survival curve. This behaviour is well-known from phenomena like radioactive decay, where there is a constant chance of decay at any moment, leading to an exponentially declining chance of the isotope’s survival over time, which is often measured by a half-life.

If AI agent success-rates drop off with task length in this manner, then the 50% success rate time-horizon for each agent from Kwa et al. is precisely the *half-life* of that agent. As with the half-life of a radioisotope, this isn’t just the median lifespan, it is the median remaining lifespan starting at any time — something that is only possible for an exponential survival curve. Unlike for particles, this AI agent half-life would be measured not in clock time, but in how long it takes a human to complete the task.

One rationale for this constant hazard rate model for AI agents is that tasks require getting past a series of steps each of which could end your attempt, with the longer the duration of the task, the more such steps. More precisely, if tasks could be broken down into a long sequence of equal-length subtasks with a constant (and independent) chance of failure, such that to succeed in the whole task, the agent needs to succeed in *all* subtasks, then that would create an exponential survival curve. I.e. when Pr(*Task*) = Pr(*Subtask* $_1$ & *Substask* $_{2}$ & … & *Subtask* $_{N}$).

But we don’t have to assume a perfect breakdown of the task into equal-length-equal-difficulty subtasks in order to get an exponential distribution (and corresponding constant hazard rate). We can also think of the constant hazard rate model as being agnostic as to how the task is broken down, just saying that the chance of succeeding in a subtask of duration *t* is always equal to the chance of succeeding in each of a set of smaller subtasks whose combined duration is also *t*. So on this model, it doesn’t matter what level of granularity you assess the task at — whether you see it as one 60-minute task, six 10-minute tasks, or a 20-minute task plus forty 1-minute tasks — the chance of succeeding is set by the total time it would take a human to complete it.

This constant hazard rate model would predict that the time horizon for an 80% success rate is about ⅓ of the time horizon for a 50% success rate. This is because the chance of surviving three periods with an 80% success rate = (0.8) $^3$ = 0.512 ≈ 50%. More precisely, the time horizon for a success probability of *p* would be ln(*p*)/ln(*q*) times as long as one with success probability *q*. So an 80% time-horizon would be ln(0.8)/ln(0.5) = 0.322 times as long as the 50% time-horizon. Kwa et al. estimate the 80% time-horizon for Claude 3.7 Sonnet to be 0.25 as long, which is close to this theoretical estimate and within the margin of error given the noisiness of the results. The following chart shows how these numbers relate to the exponential survival curve (where *T* $_{50}$ is the 50% time-horizon etc.).

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/298e3bea-1b1d-49f8-a665-8832aea191af/Figure+3.png?format=2500w)

Here are some useful comparisons for how the predicted time horizons over which an agent could get very high success rates compare to the measured time horizon for a 50% success rate:

*T* $_{80}$ ≈ 1/3 *T* $_{50}$
*T* $_{90}$ ≈ 1/7 *T* $_{50}$
*T* $_{99}$ ≈ 1/70 *T* $_{50}$
*T* $_{99.9}$ ≈ 1/700 *T* $_{50}$*
\[and each additional ‘nine’ of reliability beyond this divides the time horizon by 10\]*

We can also use this model to calculate how long we’d expect it to take between the 50% success rate time horizon reaching a given length and a high success rate time horizon reaching that same length (on the assumption of the 7-month doubling time and the constant hazard rate model):

*T* $_{80}$ reaches any particular length about 1 year after *T* $_{50}$ does
*T* $_{90}$ reaches any particular length about 2 years after *T* $_{50}$ does
*T* $_{99}$ reaches any particular length about 4 years after *T* $_{50}$ does
*T* $_{99.9}$ reaches any particular length about 6 years after *T* $_{50}$ does
*\[each additional ‘nine’ of reliability requires 2 more years…\]*

Kwa et al. also attempt to fit a relationship between the success probability and time-horizon (see the figure below, which I’ve adapted from their paper). They plot the time horizon on a log scale and note that this reveals a sigmoid-shaped decay curve of success rate (the coloured bars). They show that this is reasonably well fit by a logistic function (the black curves). The paper doesn’t compare this to how well alternative functions would fit the data.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/d641d697-240b-4c0f-8676-c649e477d235/Figure+4.png?format=2500w)

The data is also well-fit by an exponential function, which also looks like a sigmoid when plotted on this logarithmic x-axis. I’ve added this to the above figure (from Kwa et al.) in the form of the dotted blue curves. It fits the data better for some models (such as the top left) and worse on others. It fits the data roughly as well overall, while being substantially more likely *a priori* — exponential decay is *the* simplest survival curve and has only one free parameter instead of two. Moreover, while logistic functions are quite simple and natural, the black curve here is not really a logistic distribution, but the more complex log-logistic distribution which merely looks like a logistic distribution when plotted on a logarithmic x-axis.

The paper also plots the survival curve for *human* performance over increasing time periods:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/9c39bdb4-ea1d-441d-ae07-d13e80c36369/Figure+5.png?format=2500w)

Intriguingly, this human survival curve seems to be noticeably better than a constant hazard rate (i.e. the chance of succeeding over long timescales drops off more slowly for humans than the constant hazard rate predicts). For example, on this graph, humans had about a 50% success rate at the 1.5-hour mark, which suggests 25% at 3 hours, 12.5% at 6 hours and 6.25% at 12 hours if the hazard rate is constant. However, the humans were still above 20% success rate at that point.

This could indicate a different scaling behaviour of success rate with time horizon for humans compared to AI agents, which would be well worth investigating and may suggest important underlying mechanisms (e.g. that the humans were better at correcting earlier failed subtasks). If human performance scales differently with task length than AI agent performance, that would be an important result, suggesting that there is a notable inefficiency in the current AI paradigm. This warrants further research.

However, there are other potential explanations. For instance, it could also be an artefact of this graph being an aggregate of humans with different ability levels, since even if all individual humans have a constant hazard rate (and so each have an exponential survival curve) a mixture of different humans would be a weighted sum of exponentials with different time constants and that distribution decays slower than an exponential (see [Ord (2023)](https://arxiv.org/abs/2308.09045) for details).

The AI agents don’t suffer from mixing different capability levels into the same statistics because there is a separate data series for each agent. However, there is a similar effect that could still be present in the measurement of AI agents’ performance over increasingly long tasks. It is plausible that some tasks are inherently easier than others per unit time, corresponding to different hazard rates. If so, then the survival curve over the whole task suite would be averaging different exponential decay curves together. This produces an aggregate decay curve with thicker tails than an exponential (corresponding to a declining effective hazard rate). Again, see [Ord (2023)](https://arxiv.org/abs/2308.09045) for details. Dealing with this effect is important as it could still be the case that the mechanism of constant hazard rate (and what it implies about the agents’ behaviour) holds for every task, even if it isn’t visible in the aggregate of these tasks.

### Upshots of the constant hazard rate model

If the constant hazard rate model is sufficient to explain the drop-off in success rates on a task suite, there are several interesting upshots:

- It allows us to make predictions for the time-horizons at other success rates, such as 90% and 99%.
- It allows us to make predictions for how the success rate improves over time for a fixed task-length.
- It provides simple rules of thumb for predicting success probabilities (e.g. that if you double the task duration, you square the success probability).
- It suggests that AI agent performance (at least on this task suite) can be characterised by a half-life.
- It provides indirect evidence that what really is going on under the hood is that tasks are made up of many sequential subtasks and the chance of succeeding at the whole requires succeeding at every individual component. Moreover, this suggests that the current AI agents are not very good at recovering from earlier mistakes.
- Because the exponential distribution is the unique memoryless distribution, another way of seeing it is that the chance of failing at the next moment is independent of how far you’ve come — just like how the chance of a radioisotope decaying in the next minute is independent on how many minutes it has survived so far. This would be a surprising and interesting property for reasoning agents.
- Deviations from exponential decay for certain models may provide evidence that their hazard rate is increasing (or decreasing) with time, which might provide hints as to what they are doing wrong (or right).
- It can explain the same 7-month doubling time for the 50% time-horizon and 80% time-horizon: a 7-month halving-time for the underlying hazard rate would produce the 7-month doubling-time of all such time horizons.
- It also helps conceptually explain what the time horizons could even mean. For example, if it can complete a day’s work, why can’t it just do that twice to produce two days of work? On the constant hazard rate model, the issue is that if has a 50% chance of succeeding on Monday’s work, then it only has a 25% chance of succeeding in both Monday’s and Tuesday’s work, which is too low to count as reliably achieving the 2-day task (and similarly for any higher reliability threshold).

Note that I am not claiming AI agents have a precisely constant rate of failure per minute of time it would take a human to complete the task. The claim is instead that something like this appears to be roughly true or stochastically true. All other models imply that there is some systematic change in the hazard rate over time, and my suggestion (pending more information about the precise fits of different models) is that the data doesn’t warrant such assumptions.

If systematic deviations from exponential decay are found, such as the hazard rate increasing (or decreasing) with time, this might provide useful hints as to what the agents are doing wrong (or right). i.e. the constant hazard rate model can also work as a theoretical baseline from which to measure empirical deviations.

Also, note that *whatever* the survival curve is, if you lower the hazard rate by a factor of *k* at all times, the time horizons for all success rate levels also increase by a factor of *k* (because the entire survival curve is being stretched horizontally by a factor of *k*). Moreover, this is bidirectional — the only way to increase the time horizons at all success-rate levels by the same factor is to lower hazard rate by that factor. So to the extent that the METR evidence suggests the time horizons at every success rate are doubling at the same rate, it is also suggesting that the agent improvements are taking the form of reducing the hazard rate across all times by the same factor (i.e.. halving it every 7 months). This is intriguing and would be true whether or not there is a constant hazard rate for each model..

### Further work

So far these results and analysis are merely suggestive of a constant hazard rate. Ideally one would conduct a formal statistical analysis on how well an exponential decay curve fits METRs data compared to the log-logistic they use. It would also be good to run robust statistical comparisons of the human decay curves versus the AI agent decay curves to see if there are systematic differences (e.g. different half-lives or different shapes that aren’t just an artefact of the experimental setup). And of course it is also important to know how much any of this generalises to other suites of tasks.

**UPDATE — 4 Feb 2026**

Some great new [analysis by Gus Hamilton](https://gushamilton.github.io/lab/2026/01/23/petos-paradox-ai-agents/) shows that AI agents probably *don't* obey a constant hazard rate / half-life. Instead their hazard rates systematically decline as the task goes on. You can find my take on his analysis [here](/writing/hazard-rates-for-ai-agents-decline).

### References

Thomas Kwa et al., [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499), arXiv:2503.14499 \[cs.AI\], 2025.

Toby Ord, [The Lindy Effect](https://arxiv.org/abs/2308.09045). arXiv:2308.09045 \[physics.soc-ph\], 2023.

## Inference Scaling Reshapes AI Governance

## Toby Ord

*The shift from scaling up the pre-training compute of AI systems to scaling up their inference compute may have profound effects on AI governance. The nature of these effects depends crucially on whether this new inference compute will primarily be used during external deployment or as part of a more complex training programme within the lab. Rapid scaling of inference-at-deployment would: lower the importance of open-weight models (and of securing the weights of closed models), reduce the impact of the first human-level models, change the business model for frontier AI, reduce the need for power-intense data centres, and derail the current paradigm of AI governance via training compute thresholds. Rapid scaling of inference-during-training would have more ambiguous effects that range from a revitalisation of pre-training scaling to a form of recursive self-improvement via iterated distillation and amplification.*

### The end of an era — for both training and governance

The intense year-on-year scaling up of AI training runs has been one of the most dramatic and stable markers of the Large Language Model era. Indeed it had been widely taken to be a permanent fixture of the AI landscape and the basis of many approaches to AI governance.

But [recent](https://www.reuters.com/technology/artificial-intelligence/openai-rivals-seek-new-path-smarter-ai-current-methods-hit-limitations-2024-11-11/) [reports](https://www.deeplearning.ai/the-batch/ai-giants-rethink-model-training-strategy-as-scaling-laws-break-down/) from unnamed employees at the leading labs suggest that their attempts to scale up pre-training substantially beyond the size of GPT-4 have led to only modest gains which are insufficient to justify continuing such scaling and perhaps even insufficient to warrant public deployment of those models. A possible reason is that they are running out of high-quality training data. While the scaling laws might still be operating (given sufficient compute and data, the models would keep improving), the ability to harness them through rapid scaling of pre-training may not. What was taken to be a fixture may instead have been just one important era in the history of AI development; an era which is now coming to a close.

Just before the reports of difficulties scaling pre-training, OpenAI [announced](https://openai.com/index/learning-to-reason-with-llms/) their breakthrough reasoning model, o1. Their announcement came with a chart showing how its performance on a difficult mathematics benchmark could be increased via scaling compute dedicated to post-training reinforcement learning (to improve the overall performance of the model); or by scaling the inference compute used on the current task.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/0a2e094a-7089-4e66-b955-cf7e2b7271b2/o1+performance.png?format=2500w)

This has led to intense speculation that the previous era of scaling pre-training compute could be followed by an era of scaling up inference-compute. In this essay, I explore the implications of this possibility for AI governance.

In some ways a move to scaling of inference compute may be a continuation of the previous paradigm (as lab leaders have been suggesting $^1$). For example, work on the trade-off between pre-training compute and inference compute suggests that (on the current margins) increasing inference compute on the task at hand by 1 order of magnitude often improves performance as much as increasing pre-training compute by [0.5 to 1 orders of magnitude](https://epoch.ai/blog/trading-off-compute-in-training-and-inference). So we may be tempted to see it simply as an implementation detail in the bigger story of scaling up compute in general.

But a closer look suggests that may be a mistake. There are a number of key differences between scaling pre-training and scaling inference — both for the labs and for AI governance.

I shall argue that many ideas in AI governance will need either an adjustment or an overhaul. Those of us in the field need to look back at the long list of ideas we work with and see how this affects each one.

There is a lot of uncertainty about what is changing and what will come next.

One question is the rate at which pre-training will continue to scale. It may be that pre-training has topped out at a GPT-4 scale model, or it may continue increasing, but at a slower rate than before. [Epoch AI suggests](https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year) the compute used in LLM pre-training has been growing at about 5x per year from 2020 to 2024. It seems like that rate has now fallen, but it is not yet clear if it has gone to zero (with AI progress coming from things other than pre-training compute) or to some fraction of its previous rate.

A second — and ultimately more important — question concerns the nature of inference-scaling. We can view the current AI pipeline as pre-training (such as via next-token prediction), followed by post-training (such as RLHF or RLAIF), followed by deploying the trained model on a vast number of different tasks (such as through a chat interface or API calls).

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/92956b40-e44e-4678-b56e-f58110b5a7fa/Training+Stages.png?format=2500w)

The second question is whether the scaled-up inference compute will primarily be spent during deployment (like in o1 and R1) or as part of a larger and more complex post-training process (like the suggestions that OpenAI may have used trained o3 via many runs of o1). Each of these possibilities has important — but different — implications for AI governance.

## Scaling inference-at-deployment

Let’s first consider the scenario where for the coming years, the lion’s share of compute scaling goes into scaling up the inference compute used at deployment. In this scenario, the pre-trained system is either stuck at GPT-4 level or only slowly progressing beyond that, while new capabilities are being rapidly unlocked via more and more inference compute. Some of this may be being spent in post-training as the system learns how to productively reason for longer times (e.g. the reinforcement learning in the left-hand chart of OpenAI’s o1 announcement), but for this scenario, we are supposing that this one-off cost is comparatively small and that the main thing being scaled is the deployment compute.

In this scenario, we may be able to use rules of thumb such as

Effective orders of magnitude = OOMs of pre-training + 0.7 × OOMs of inference

to estimate the capabilities of an inference-scaled model in terms of the familiar yardstick of pure pre-training. But overreliance on such formulas could obscure key changes in the new scaling paradigm — changes that stem from the way the benefits of inference-at-deployment depend upon the task at hand, the way the amount of inference can be tuned to the task, and the way the costs shift from training time to deployment time.

### Reducing the number of simultaneously served copies of each new model

It currently takes a vast number of chips to train a frontier model. Once the model is trained, those chips can be used for inference to deploy a large number of simultaneous copies of that model. Dario Amodei of Anthropic [estimates](https://darioamodei.com/machines-of-loving-grace) this to be ‘millions’ of copies. This number of copies is a key parameter for AI governance as it affects the size of the immediate impact on the world the day the new model is ready. A shift to scaling inference-at-deployment would lower this number. e.g. if inference-at-deployment is scaled by two orders of magnitude, then this key parameter goes down by a factor of 100, and the new model can only be immediately deployed in 1% as many tasks as it would be if it had been scaled by pre-training compute.$^2$

### Increasing the price of first human-level AGI systems

A related parameter is how expensive the first ‘human-level’ AI systems will be to run. By previous scaling trends we might expect the first such systems to cost much less than human labour, meaning that they could be immediately deployed at a great profit, which could be ploughed back into renting chips to run more copies of them in an escalating feedback loop. But each additional order of magnitude that goes to inference-at-deployment may increase the cost of using these systems by up to an order of magnitude.

This will blunt the immediate impact of reaching this threshold and may even be enough such that there is an initial period where we first have access to ‘human-level’ AGI systems at more than the cost of equivalent human labour. If so, such systems could be available to study (for safety work) or demonstrate (before the world’s leaders) before they have transformative effects on society.

Obviously the fact that AI is already much better than humans at some tasks while much worse at others complicates this idea of reaching ‘human-level’, but I believe it is still a useful lens. For example, you can ask whether the first systems that can perform a particular job better than humans will cost more or less than human wages for that job.

### Reducing the value of securing model weights

Suppose that for frontier models, training compute plateaus at something like the GPT-4 level while inference-at-deployment scales by a factor of 100. Then the value of stealing model weights hasn’t increased over time — it is just the value of not having to train a GPT-4 level model (which has been decreasing over time by [about 4x](https://epoch.ai/trends) per year due to algorithmic efficiency improvements and Moore’s law). And even if the weights were stolen, the thief would still have to pay the high inference-at-deployment costs. If they intend to use the model at anything like the scale current leading models are used, these would be the lion’s share of the total costs and much higher than the training costs of the model they stole.

### Reducing the benefits and risks of open-weight models

This also affects both the benefits and drawbacks of open-weight models. If open-weight models require vast amounts of inference-at-deployment from their users, then they are much less attractive to those users than models of equivalent capability that were entirely pre-trained (since then the model trainer has paid those costs for you). So open-weight models could become much less valuable for their users and also less dangerous in terms of proliferation of dangerous capabilities. They would become less strategically important overall.

### Unequal performance for different tasks and for different users

Scaling inference-at-deployment helps with some kinds of tasks much more than others. It helps most with tasks where the solution is objectively verifiable, such as certain kinds of maths and programming tasks. It can also be useful for tasks involving many steps. Two good heuristics for the tasks that benefit from inference scaling are:

1. tasks that benefit from System 2–type thinking (methodical reasoning) when performed by humans,
2. tasks that typically take humans a long time (as this shows these tasks can benefit from a lot of thinking before diminishing marginal returns kick in).

Because some tasks benefit more from additional inference than others, it is possible to tailor the amount of inference compute to the task, spending 1,000x the normal amount for a hard, deep maths problem, while just spending 1x on problems that are more intuitive. This kind of tailoring isn’t possible with pre-training scaling, where scaling up by 10x increases the costs for everything.

A related change is that users with more money will likely be able to convert that into better answers. We’ve already seen this start to happen at OpenAI (the first frontier company to allow access to a model that scales inference-at-deployment). They now charge 10x as much for access to the version using the most inference-compute. We’d become accustomed to a dollar a day getting everyone the same quality of AI assistance. It was as Andy Warhol said about Coca Cola:

‘What’s great about this country is that America started the tradition where the richest consumers buy essentially the same things as the poorest. … the President drinks Coca Cola, Liz Taylor drinks Coca Cola, and just think, you can drink Coca Cola, too. A coke is a coke and no amount of money can get you a better coke than the one the bum on the corner is drinking.’

But scaling inference-at-deployment ends that.

### Changing the business model and industry structure

The LLM business model has had a lot in common with software: big upfront development costs and then comparatively low marginal costs per additional customer. Having a marginal cost per extra user that is lower than the average cost per user encourages economies of scale where each company is incentivised to set low prices to acquire a *lot* of customers, which in turn tends to create an industry with only a handful of players. But if the next two orders of magnitude of compute scale-up go into inference-at-deployment instead of into pre-training, then this would change, upsetting the existing business model and perhaps allowing more room for smaller players in the industry.

### Reducing the need for monolithic data centres

While training compute benefits greatly from being localised in the same data centre, inference-at-deployment can be much more easily spread between different locations. Thus if inference-at-deployment is being scaled by several orders of magnitude, it could avoid current bottlenecks concerning single large data centres, such as the need for a large amount of electrical power draw in a single place (which has started to require its own large powerplant). So if one hoped for the government to be able to exert some control over AI labs via the carrot of accelerated power plant approvals, inference-at-deployment may change that. And it will make it harder for governments to keep track of all the frontier models being trained by tracking the largest datacentres.

### Breaking the strategy of AI governance via compute thresholds

[Many AI governance frameworks](https://arxiv.org/pdf/2405.10799) are based around regulating only those models above a certain threshold of training compute. For example, the EU AI Act uses 10 $^{25}$ FLOP while the US executive order uses 10 $^{26}$ FLOP. This allows them to draw a line around the few potentially dangerous systems without needing to regulate the great majority of AI models. But if capabilities can be increased via scaling inference-at-deployment then a model whose training compute was below these thresholds might be amplified to become as powerful as those above them. For example, a model trained with 10 $^{24}$ FLOP might have its inference scaled up by 4 OOM and perform at the level of a model trained with 10 $^{27}$ FLOP. This threatens to break this entire approach of training-compute thresholds.

At first the threat might be that someone scales up inference-at-deployment by a very large factor for a small number of important tasks. If the inference scale-up is only happening on a small fraction of all tasks the model is deployed on, one could use a very high scale-up factor (such as 100,000x) and suddenly operate at the level of a new tier of model.

The main limitation on this at the moment is that many current techniques for inference scaling seem to hit plateaus that can’t be exceeded by any level of inference scale-up. Exceeding these plateaus requires substantial research time by AI scientists and engineers, such that if someone tried to use a GPT-4 level model with 100,000x the inference compute, it may not be able to make good use of most of that compute. However, labs are developing better ways to use large multipliers of inference compute before reaching performance plateaus and this work is proceeding very quickly. For example, OpenAI demonstrated their o3 model making use of 10,000x as much compute as their smallest reasoning model, o1-mini, and so presumably an even larger factor above their base model, GPT-4o.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/318d5297-2724-4ed3-9d89-c45336f6c79c/o3+performance+on+ARC-AGI.jpeg?format=2500w)

Leading labs have also been scaling their data centres and improving algorithmic efficiency such that they may already have 100x the effective-compute of the first data centres capable of serving GPT-4 to customers. This would allow more than just a few people to use versions with greatly scaled-up inference-at-deployment. For example, OpenAI’s recently launched deep research model (based on o3) may well exceed the performance of a system pre-trained on 10 $^{26}$ FLOP, even if it is technically below that threshold.

While one could try to change the governance threshold to incorporate the inference-at-deployment as well as the pre-training compute, this would face serious problems. The current framework aims to separate AI systems that could be dangerous from those that can’t be. It aims to regulate dangerous objects, not dangerous uses of objects. But a revised threshold would depend not just on the model but on how you are using it, which would be a different and more challenging kind of governance threshold.

Perhaps one way to save the compute thresholds is to say that they cover both systems above 10 $^{26}$ FLOP of pre-training and systems above some smaller threshold (e.g. 10 $^{24}$ FLOP of pre-training) that have had post-training to allow themselves to benefit from high inference-at-deployment. But this still suffers from increased complexity and fewer bright lines.

Overall, scaled up inference-at-deployment looks like a big challenge for governance via compute thresholds.

## Scaling inference-during-training

AI labs may also be able to reap tremendous benefit from these inference-scaled models by using them as part of the training process. If so, the large scale-up of compute resources could go into post-training rather than deployment. This would have very different implications for AI governance.

In this section, we’ll focus on the implications of a pure strategy of using inference-scaling *only* during the training process. This will clarify what it contributes to the overall picture of AI governance, though realistically we will see inference-scaling in both training and deployment.

An obvious approach to scaling inference-during-training is to use an inference-scaled model to generate large amounts of high-quality synthetic data on which to pre-train a new base model. This would make sense if the challenges in scaling up pre-training beyond GPT-4 are due to running out of high-quality training data. For example, [court documents](https://storage.courtlistener.com/recap/gov.uscourts.cand.415175/gov.uscourts.cand.415175.391.24.pdf) have revealed that Meta’s Llama3 team decided to train on an illegal Russian repository of copyrighted books, LibGen, because they were unable to reach GPT-4 level without it:

‘Libgen is essential to meet SOTA \[state-of-the-art\] numbers, across all categories, and it is known that OpenAI and Mistral are using the library for their models (through word of mouth).’

This strongly suggests that even though there are still many more unused tokens on the indexed web (about [30x as many](https://epoch.ai/blog/can-ai-scaling-continue-through-2030) as are used in GPT-4 level pre-training), performance is being limited by lack of high-quality tokens. There have already been attempts to supplement the training data with synthetic data (data produced by an LLM), but if the issue is more about quality than raw quantity, then they need the best synthetic data they can get.

Inference-scaling can help with this by boosting the capability of the model producing the synthetic data. One way to do this is via domains such as mathematics or programming where one can tell whether a generated solution is correct and how efficient it is. The training programme could involve generating lots of proofs and computer programs using advanced reasoning models until it finds high quality solutions, and then add those to the stock of data that goes into pre-training the next base model.

This access to ground truth in mathematical disciplines is particularly important for getting the right training signal. But even for domains that are less black and white, it may be possible to trade extra inference compute for better synthetic data. For example, one could generate many essays, run several rounds of editing on them, and then assess them for originality, importance of insight, and lack of detectable errors, putting only those of the highest quality into the stock of synthetic data.

Relatedly, one could apply this technique to the stock of human-generated training data, assessing each document in the training data and discarding those that are below-average in quality. This could either improve the average quality of the data they already use or make some fraction of the unused sources of data usable.

On its own, this approach of scaling inference-during-training to produce synthetic data for pre-training is not so interesting from an AI governance perspective. Its main direct effect is to allow the scaling of pre-training compute to recommence, breathing new life into the existing scaling paradigm.

But there is a modification of this approach that may have the potential to lead to explosive growth in capabilities. The idea is to rapidly improve a model’s abilities by amplifying its abilities (through inference scaling) then distilling those into a new model, and repeating this process many times. This idea is what powered the advanced self-play in DeepMind’s [AlphaGo Zero](https://www.nature.com/articles/nature24270), and was also independently discovered by [Anthony et al.](https://arxiv.org/abs/1705.08439) and, in the context of AI-safety, by [Christiano](https://ai-alignment.com/benign-model-free-rl-4aae8c97e385).

In the case of AlphaGo Zero, you start with a base model, $M_0$, that takes a representation of the Go board and produces two outputs: a probability distribution over the available moves (representing the chance a skilled player would choose them) and a probability representing the chance the active player will eventually win the game.$^{3}$ This model will act as an intuitive ‘System 1’ approach to game playing, with no explicit search.

The training technique then plays 25,000 games of Go between two copies of $M_0$ amplified by a probabilistic technique for searching through the tree of moves and countermoves called Monte Carlo Tree Search (MCTS). That is, both players use MCTS with $M_{0}$ guiding the search by using its estimates of likely moves and position strength as a prior. By repeatedly calling $M_{0}$ in the search (thousands of times), we get a form of inference-scaling which amplifies the power of this model. We could think of it as taking the raw System 1 intuitions of the base model and embedding them in a System 2 reasoning process which thinks many moves ahead.

This amplified model is better than the base model at predicting the move most likely to win in each situation, but it is also much more costly. So we train a new model, $M_1$, to predict the outputs of $M_{0}$ + search. Following Christiano, I shall call this step distillation, though in the case of AlphaGo Zero, $M_{1}$ was simply $M_{0}$ with an additional stage of training. This trained its move predictions to be closer to the probability distribution over moves that $M_{0}$ + search gives and trained its board evaluations to be closer to the final outcome of the self-played games. While $M_{1}$ won’t be quite as good at Go as the amplified version of $M_{0}$, it is better than $M_{0}$ alone.

But why stop there? We can repeat this process, amplifying $M_1$ through inference-scaling by using it to guide the search process, producing a level of play beyond any seen so far ($M_{1}$ + search). This then gets distilled into a new model, $M_{2}$, and we proceed onwards and upwards, climbing higher and higher along the ladder of Go-playing performance.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/fbbb5f48-c287-47d6-bca8-0c5c947154a6/IDA-wide.png?format=2500w)

After just 36 hours the best model (with search) had exceeded the ability of AlphaGo Lee (the version that beat world-champion Lee Sedol) which had been trained for months but lacked some innovations including this structure of iterated amplification and distillation. Within 72 hours AlphaGo Zero was able to defeat AlphaGo Lee by 100 games to zero. And after 40 days of training (and 29 million games of self-play $^4$) it reached its performance plateau, $M_{m a x}$, where the unamplified model could no longer meaningfully improve its predictions of the amplified model. At this point the amplified version had an estimated Elo rating of 5,185 — far beyond the 3,739 of AlphaGo Lee or the low 3,000s of the world’s best human players. Even when the final model was used without any search process (i.e. without any scaling of inference-at-deployment), it achieved a rating of 3,055 — roughly at the level of a human pro player despite playing from pure ‘intuition’ with no explicit reasoning.

It may be possible to use such a process of iterated distillation and amplification in the training of LLMs. The idea would be to take a model such as GPT-4o (which applied a vast amount of pre-training to provide it with a powerful System 1) and use it as the starting model, $M_0$.$^{5}$ Then amplify it via inference scaling into a model that uses a vast number of calls to $M_{0}$ to simulate System 2–type internal reasoning before returning its final answer (as o1 and R1 do). Then distill this amplified model into a new model, $M_{1}$, that is better able to produce the final answer from the amplified model without doing the hidden reasoning steps.$^{6}$ If this works, you now have model that is more capable than GPT-4o without using extra inference-at-deployment.

By iterating this process of amplification followed by distillation, it may be possible for the LLM (like AlphaGo Zero) to climb a very long way up this ladder before the process runs out of steam. And the time for each iteration may be substantially shorter than the time between major new pre-training runs. Like AlphaGo Zero, the final distilled model could display very advanced capabilities even without amplification. If this all worked, it would be a way of scaling inference-during-training to substantially quicken the rate of AI progress.

It is not at all clear whether this would work. It may plateau quickly, or require rapidly growing parameter counts to distill each new model, or take too long per step, or too many steps, or require years worth of engineering effort to overcome the inevitable obstacles that arise during the process.$^7$ But AlphaGo Zero does give us a proof of concept of a small team at a leading lab achieving take-off with such a process and riding its rapid ascent to reach capabilities far beyond the former state-of-the-art.

So iterated distillation and amplification provides a plausible pathway for scaling inference-during-training to rapidly create much more powerful AI systems. Arguably this would constitute a form of ‘recursive self-improvement’ where AI systems are applied to the task of improving their own capabilities, leading to a rapid escalation. While there have been earlier examples of this, they have often been on narrow domains (e.g. the game of Go) or have only applied to certain cognitive abilities (e.g. ‘learning how to learn’) and so been bottlenecked on other abilities. Iterated distillation and amplification of LLMs is a version that could credibly learn to improve its own general intelligence.

What does this mean for AI governance? A key implication is that scaling inference-during-training may mean we have less transparency into the best current models. While this use of inference inside the training process would reach the EU AI Act’s compute threshold, that threshold only requires oversight when the model is deployed.$^8$ Thus it may be possible for companies to substantially scale up the intelligence of their leading models without anyone outside knowing. AI governance may then have to proceed from a state of greater uncertainty about the state of the art. Relatedly, the lack of transparency would mean the public and policymakers wouldn’t be able to try these state-of-the-art models and so the overton window of available policy responses won’t be able to shift in response to them. This would lead to less regulation and a more abrupt shock to the world when the models at the top of the training ladder are deployed.

But perhaps most importantly, the possibility of training general models via iterated distillation and amplification could shorten the timelines until AGI systems with transformative impacts on the world. If this was combined with a lack of transparency about state of the art models during internal scaling, we couldn’t know for sure if timelines were shortening or not, making it hard to know whether emergency measures were required. All of this suggests that policies to require disclosure of current capabilities (and immediate plans for greater capabilities) would be very valuable.

## Conclusions

The shift from scaling pre-training compute to scaling inference compute may have substantial implications for AI governance.

On the one hand, if much of the remaining scaling comes from scaling inference at deployment, this could have implications including:

- Reducing the number of simultaneously served copies of each new model
- Increasing the price of first human-level AGI systems
- Reducing the value of securing model weights
- Reducing the benefits and risks of open-weight models
- Unequal performance for different tasks and for different users
- Changing the business model and industry structure
- Reducing the need for monolithic data centres
- Breaking the strategy of AI governance via compute thresholds

On the other hand, if companies instead focus on scaling up the inference-during-training, then they may be able to use reasoning systems to create the high-quality training data needed to allow pre-training to continue. Or they may even be able to iterate this in the manner of AlphaGo Zero and scale faster than ever before — up the ladder of iterated distillation and amplification. This possibility may lead to:

- Less transparency into the state of the art models
- Less preparedness among the public and policymakers
- Shorter timelines to transformative AGI

Either way, the shift to inference-scaling also makes the future of AI less predictable than it was during the era of pre-training scaling. Now there is more uncertainty about how quickly capabilities will improve and which longstanding features of the frontier AI landscape will still be there in the new era. This uncertainty will make planning for the next few years more difficult for the frontier labs, for their investors, and for policymakers. And it may provide a premium on agility: on the ability to first spot what is happening and pivot in response.

All of this analysis should be taken just as a starting point for the effects of inference-scaling on AI governance. As this transition continues it will be important for the field to track the which types of inference-scaling are happening and thus better understand which of these issues we are facing.

## Appendix. Comparing the costs of scaling pre-training vs inference-at-deployment

Scaling up pre-training by an order of magnitude and scaling up inference-at-deployment by an order of magnitude may have similar effects on the capabilities of a model, but they can have quite different effects on the total compute cost of the project. Which one is more expensive depends on the circumstances in a rather complex way.

Let’s focus on the total amount of compute used for an AI system over its lifetime as the cost of that system (though this is not the only thing one might care about). The total amount of compute used for an AI system is equal to the amount used in training plus the amount used in deployment:

$$
C = C_{pre-training} + C_{post-training} + C_{deployment}
$$

Let $N$ be the number of parameters in the model, $D$ be the number of data tokens it is trained on, $d$ be the number of times the model is deployed (e.g. the number of questions it is asked) and $I$ be the number of inference steps each time it is deployed (e.g. the number of tokens per answer). Then this approximately works out to:$^{9}$

$$
C  \approx  ND  +  C_{post-training}  +  dNI
$$

Note that scaling up the number of parameters, $N$, increases both pre-training compute and inference compute, because you need to use those parameters each time you run a forward pass in your model. But scaling up $D$ doesn’t directly affect deployment costs. Some typical rough numbers for these variables in GPT-4 level LLMs are:

*N* = 10 $^{12}$ *D* = 10 $^{13}$ *I* = 10 $^{3}$ *d* =?

On this rough arithmetic, the deployment costs overtake the pre-training costs when the total number of tokens generated in deployment ($dI$) is greater than the total number of training tokens $D$. That would require $d$ > 10 $^{10}$. Apparently, this is usually the case, with deployment compute exceeding total training compute on commercial frontier systems.$^{10}$

The most standard way of training LLMs to minimise training compute involves scaling up $N$ and $D$ by the same factor. For example, if you scale up training compute by 1 OOM, that means 0.5 OOMs more parameters and 0.5 OOMs more data. So scaling up training compute by 1 OOM also increases deployment compute by 0.5 OOM. In contrast, scaling up inference-at-deployment by an order of magnitude doesn’t (directly) affect pre-training compute.

When either the pre-training compute ($ND$) or the deployment compute ($d N I$) is the bulk of the total (including $C_{p o s t - t r a i n i n g}$), there are some simple approximations for the costs of scaling. If $C_{p r e - t r a i n i n g} \gg C_{p o s t - t r a i n i n g} + C_{d e p l o y m e n t}$, then scaling pre-training by 10x increases costs by nearly 10x, while scaling inference-at-deployment ($I$) by 10x doesn’t affect the total much. Whereas if $C_{d e p l o y m e n t} \gg C_{p r e - t r a i n i n g} + C_{p o s t - t r a i n i n g}$, then scaling pre-training by 10x increases costs by ~3x (from the larger number of parameters needed at deployment), while scaling inference-at-deployment by 10x increases costs by nearly 10x. So there is some incentive to balance these numbers where possible.

It is important to note that the costs of scaling inference-at-deployment depend heavily on how much deployment you are doing. If you just use the model to answer a single question, then you could scale it all the way until it generates as many tokens as you pretrained on (i.e. trillions) before it appreciably affects your overall compute budget. While if you are scaling up the inference used for every question, your overall compute budget could be affected even by a 2x scale up.

$^1$ e.g. Dario Amodei has said ‘Every once in a while, the underlying thing that is being scaled changes a bit, or a new type of scaling is added to the training process. From 2020-2023, the main thing being scaled was *pretrained models*: models trained on increasing amounts of internet text with a tiny bit of other training on top. In 2024, the idea of using *reinforcement learning* (RL) to train models to generate chains of thought has become a new focus of scaling.’

$^2$ Or, somewhat equivalently, it might be better thought of as slowing these systems down by that factor (e.g. 100x). Amodei’s estimate is that AI systems are currently 10x–100x human speed, but if they reach intelligence via inference scaling, they may be slower than humans. Both ways of looking at it lead to the same reduction in the ‘human-days-equivalent of AI work each day’ when the systems are switched from training to deployment.

$^3$ For AlphaGo Zero, the goal was to start with zero information about Go and learn everything, so $M_{0}$ was simply a randomly initialised network. But it is also possible to start with a more advanced network as $M_{0}$, such as one trained to imitate human behaviour.

$^4$ Given 29 million games of self-play and a set-up with 25,000 games before each distillation, there were presumably 1,160 iterations of amplification and distillation before it reached its plateau, such that $M_{m a x}$ is $M_{1160}$.

$^5$ Like o1 and R1, we would presumably include additional RL post-training to prepare it for use in inference scaling.

$^6$ Here $M_{1}$ could be a fresh model distilled from the inference-scaled $M_{0}$, or it could be $M_{0}$ with fine-tuning to make it behave more like the inference-scaled $M_{0}$.

$^7$ It is also possible that it will work in some domains (such as mathematics and coding) but not others, leading to superhuman capabilities in several new domains, but not across the board.

$^8$ And only when deployed inside the EU itself, where OpenAI’s inference-scaled model deep research is conspicuously absent.

$^9$ I’m simplifying some of the details (such as the precise coefficients for each term) to make the overall structure of the equation clearer.

$^{10}$ This has led to methods of training that use more training compute than is Chinchilla-optimal because the smaller model leads to compensating savings on the deployment compute

## Inference Scaling and the Log-x Chart

## Toby Ord

Improving model performance by scaling up inference compute is the next big thing in frontier AI. But the charts being used to trumpet this new paradigm can be misleading. While they initially appear to show steady scaling and impressive performance for models like o1 and o3, they really show poor scaling (characteristic of brute force) and little evidence of improvement between o1 and o3. I explore how to interpret these new charts and what evidence for strong scaling and progress would look like.

[Read More](/writing/inference-scaling-and-the-log-x-chart)

## The Scaling Paradox

## Toby Ord

*AI capabilities have improved remarkably quickly, fuelled by the explosive scale-up of resources being used to train the leading models. But if you examine the scaling laws that inspired this rush, they actually show extremely poor returns to scale. What’s going on?*

**AI Scaling is Shockingly Impressive**

The era of LLMs has seen remarkable improvements in AI capabilities over a very short time. This is often attributed to the AI scaling laws — statistical relationships which govern how AI capabilities improve with more parameters, compute, or data. Indeed AI thought-leaders such as Ilya Sutskever and Dario Amodei have said that the discovery of these laws led them to the current paradigm of rapid AI progress via a dizzying increase in the size of frontier systems.

Before the 2020s, most AI researchers were looking for architectural changes to push the frontiers of AI forwards. The idea that scale alone was sufficient to provide the entire range of faculties involved in intelligent thought was unfashionable and seen as simplistic.

A key reason it worked was the tremendous versatility of text. As Turing had noted more than 60 years earlier, almost any challenge that one could pose to an AI system can be posed in text. The single metric of human-like text production could therefore assess the AI’s intellectual competence across a huge range of domains. The next-token prediction scheme was also an instance of both sequence prediction and compression — two tasks that were long hypothesized to be what intelligence is fundamentally about.

By the time of GPT-3 it was clear that it was working. It wasn’t just a dry technical metric that was improving as the compute was scaled up — the text was qualitatively superior to GPT-2 and showed signs of capturing concepts that were beyond that smaller system.

Scaling has clearly worked, leading to very impressive gains in AI capabilities over the last five years. Many papers and AI labs trumpet the success of this scaling in their latest results and show graphs suggesting that the gains from scaling will continue.

For example, here is a chart from [OpenAI’s release of their o1 model](https://openai.com/index/learning-to-reason-with-llms/), captioned: ‘o1 performance smoothly improves with both train-time and test-time compute’.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/3b7d484b-f2ad-4b42-8540-246bee7b2c55/o1+performance.png?format=2500w)

**AI Scaling is Shockingly Unimpressive**

But let’s take a closer look at what that chart is showing us. On the *y* -axis, their measure of AI performance is the model’s accuracy on mathematics problems aimed at elite high school students (via the challenging AIME data set). But the *x* -axis, showing the amount of compute at training-time and test-time is on a log scale. So the nice straight lines are really showing very serious diminishing returns to more compute for their model.

Specifically, the model shows logarithmic returns to compute. We can put this in more familiar terms by flipping it around: increasing the accuracy of the model’s outputs requires exponentially more compute.

That is not generally a recipe for success. In computer science exponential resource usage for linear gains is typically considered to be a sign the problem is intractable, or at least is intractable to the approach you are using. Indeed, the requirement of exponential increases in resources in time or space to continue making progress is characteristic of a brute force approach. It is the relationship you often get with the most naive approaches — those that simply try every possible solution, one by one.

And o1 isn’t the only place we see this. There was a very perceptible leap from GPT-2 to GPT-3 and from GPT-3 to GPT-4. But each successive model used about [70 times as much compute](https://epoch.ai/blog/tracking-large-scale-ai-models) as the one before (4e21 → 3e23 → 2e25 FLOP). In every other aspect of life we would certainly be hoping to see a perceptible improvement if we put 70 times as many resources into it. And normally we’d consider something that kept requiring such exponentially increasing inputs to see visible progress as proof that things were going badly; that the approach was not successfully scaling.

The recent progress in AI hasn’t been entirely driven by increased computational resources. [Epoch AI’s estimates](https://epoch.ai/trends) are that compute has risen by 4x per year, while algorithmic improvements have divided the compute needed by about 3 each year. This means that over time, the effective compute is growing by about 12x per year, with about 40% of this gain coming from algorithmic improvements.

But these algorithmic refinements aren’t improving the *scaling* behaviour of AI quality in terms of resources. If it required exponentially more compute to increase quality, it still does after a year of algorithmic progress, it is just that the constant out the front is a factor of 3 lower. In computer science, an algorithm that solves a problem in exponential time is not considered to be making great progress if researchers keep lowering the constant at the front.

What about the famed scaling laws for LLMs? Don’t they show that LLMs scale so well with resources that this scaling should be the cornerstone in leading labs’ strategies? Let’s look at the key graphs from OpenAI’s 2020 paper ‘ [Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361) ’:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/500ded62-c7b3-446d-b692-649e8af0fe8b/Scaling+Laws+%28Kaplan+2020%29.png?format=2500w)

These show a steady improvement in test loss (a measure of inaccuracy of the model) as compute, data, and parameters increase. It appears at first that the model’s inaccuracy is marching down to very low levels without diminishing returns. However that is deceptive. First, both *x* and *y* axes are logarithmic, so this is actually a power law relationship (which can involve diminishing returns). Second, because the axes have been automatically clipped and rescaled to make the graph start in one corner and end in the opposite corner, there is literally nothing you can tell from the shape or slope of these graphs beyond them being some kind of power law. (If you were to equalise scale on the *x* and *y* axes, the slope would become informative and you would instantly see that they are extremely shallow slopes — thus extremely inefficient scaling.)

But if you look at the numbers on the *x* axes (the resources used), you can see that they vary over orders of magnitude while in each case the *y* -axis only covers about half an order of magnitude. For example, on the first graph, lowering the test loss by a factor of 2 (from 6 to 3) requires increasing the compute by a factor of 1 million (from 10 $^{–7}$ to 10 $^{– 1}$). This shows that the accuracy is extraordinarily *insensitive* to scaling up the resources used. Or put another way, there are extreme diminishing returns to increased resource input.

A useful way to view this is to understand the exponents on these power law relationships (the power that things are being raised to). Each graph contains an embedded formula showing that the loss is proportional to the resource raised to a very small negative number. It is negative because in this setting the quality of the system is measured with a scale where lower numbers (lower inaccuracies) are better. It will be easier to understand what is going on if we invert that. So let’s define a measure of *accuracy* as the reciprocal of the test loss. On this revised measure, what used to be halving inaccuracy is now called doubling accuracy.

Using this measure of accuracy, we can remove the negatives from those powers. We see that the first power is now 0.050. What this means is that accuracy scales with the amount of compute used as the 1/20th power. Many of us are not that familiar with fractional powers but may recall that the square root function is equivalent to the 1/2 power. So here accuracy is growing slower than the square root of the square root of the square root of the square root of the resources. That sounds slow, but it is still a bit hard to understand or compare.

Fortunately, we can make this much more intuitive if we flip it around and ask how quickly required resources increase as a function of desired accuracy. To get that, we just take the reciprocal of the powers listed in the paper. This tells us that the compute required scales as the 20th power of the desired accuracy. i.e. if $C$ is compute and $a$ is accuracy, then $C$ = $k_{C}$ $a^{20}$, for some constant $k_{C}$. This exponent of 20 is why halving the loss (from 6 to 3) in the first graph required the compute to be doubled 20 times (a factor of 1 million). Similarly for data, $D$ = $k_{D}$ $a^{11}$, and for number of parameters, $N$ = $k_{N}$ $a^{13}$. Exponents this high are so rare in statistical relationships that you’d be forgiven for thinking that they were footnote markers.

Here is a redrawn version of the first scaling law, showing the extremely steep increase in compute required for a given accuracy level:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/68f3272e-602d-4cde-b4c7-4615af39408b/Redrawn+Scaling.png?format=2500w)

So the required resources grow polynomially with the desired level of accuracy. This is better than the exponential growth in resources we considered before. In computer science, the boundary between what is tractable and intractable is often roughly drawn as that between where the required resources scale polynomially and where they scale exponentially. But that is partly because the powers seen on polynomials in computer science are rarely higher than 3. Something that scales as the 11th, 13th, or 20th power is a case where the resources required are absolutely blowing up as desired accuracy increases and a problem whose required resources scaled so poorly would rarely be considered tractable.

Does the more recent [Chinchilla scaling law paper](https://arxiv.org/pdf/2203.15556) make things better? No, if anything it makes them worse. While it does not directly plot how loss scales with each resource type, it does plot it for compute (see the grey curve in the graph below).

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/653d4554-6bc9-40b0-b1e9-a55b35a0e84d/Chinchilla+scaling.png?format=2500w)

This grey curve is clearly not quite a straight line on this log-log chart and thus not a power law. In this study, increased quality requires more resources than a power law would predict, so resources required grow faster than polynomially, meaning even worse scaling.

**Reconciling These Views**

So what is going on here? Is AI scaling extremely impressive or is it disappointingly poor? How can we reconcile these perspectives?

There isn’t a simple answer. It depends on what we’re assessing.

From a logistics standpoint, it is impressive how quickly leading labs have been able to scale up their data centres and training runs. Quadrupling the size of your infrastructure every year is an amazing logistical achievement. But from most people’s point of view, it should be taken as being on the costs side of the ledger rather than the benefits side.

If we set aside these dramatically increasing costs, progress in AI capabilities has been impressive over the era of rapid scaling, and a lot of this impressiveness is indeed due to the scaling. Most measures of AI capabilities don’t show *exponential* progress over time, but there is no doubt this has been a heady rate of progress for AI in qualitative terms, with a feeling that it is even quicker than the five years before, in which deep learning had already set a cracking pace.

In terms of AI progress per resource, or per dollar, things are probably getting worse on most measures. This is what the pessimism about scaling laws is getting at. Measures of quality are increasing far slower than the exponentially mounting costs.

So why were people like Ilya Sutskever and Dario Amodei so impressed by the scaling laws? The answer is that there was a lot of headroom in compute — a lot of room to scale those costs. Even if the resources needed would be thousands of times larger than the largest ever ML experiment, they saw that this (1) was still within the feasible set of things a large company could fund and (2) would still be a good deal given the vast potential benefits.

For on the high end of possibilities, we are talking about something that could potentially replace more than half of all human labour in the world, and perhaps bring forward scientific and technological advances that human labour would have taken centuries to reach. In other words, while the costs could escalate wildly, a deep-pocketed project might reach benefits of extreme value before it ran out of money. And those benefits might be worth more than enough to justify those (very high) costs.

More prosaically, we can note that it is entirely possible that financial returns will scale very quickly as a function of the technical measures of AI quality. If so, then even though standard measures of AI quality scale poorly as a function of resources, the financial returns might still scale very well as a function of resources. Indeed, if they scale better than linearly, that would create a paradigm of increasing marginal returns which would explain a landscape with a small number of players, each investing as much as they possibly can.

If the financial benefits of the intermediate systems keep generating enough profit to pay for the next training run then one can ride this process up to the point where non-financial constraints (such as power use, energy use, chip fabrication, or running out of training data) prevent further scaling.

Furthermore, at a certain quality level the AI systems may be capable enough to improve themselves, searching for and implementing the kinds of algorithmic efficiencies and breakthroughs that human AI scientists seek today. If so, then continued scaling up of AI training runs over the rest of the decade may be enough to get AI systems to the bottom of this escalator, where they are smart enough to ride it up through some number of floors of recursive self-improvement before the process tops out at some higher level. The hope of reaching this new regime of self-improvement is another reason why leading labs may be excited to push through this quick — but extraordinarily inefficient — scaling process.

We can compress much of this down to the following observations:

- AI progress as a function of time is impressive even if AI progress as a function of resources is not.
- The scaling laws are impressively smooth and long-lasting, but are a proof of poor but predictable scaling, rather than impressive scaling.
- While we know that AI quality metrics scale very poorly with respect to resources, the real-world impacts may scale much better.

Finally, it is worth noting that the sheer inefficiency of how current AI systems scale may suggest that there are other approaches which scale substantially more efficiently. The human mind (which doesn’t require an entire internet of data to achieve general intelligence) shows this is possible. If so, we might someday see a step change in AI capabilities when someone discovers a learning architecture that delivers much stronger returns to scale then turns the full force of the industry’s exponentially scaled data centres upon it.

## The Precipice Revisited

## Toby Ord

In the 5 years since I wrote *The Precipice*, the question I’m asked most is how the risks have changed. I dive into four of the biggest risks — climate change, nuclear, pandemics, and AI — to show how they’ve changed.

[Read More](/writing/the-precipice-revisited)

## On the Value of Advancing Progress

## Toby Ord

[(PDF available)](http://files.tobyord.com/progress.pdf)

*I show how a standard argument for advancing progress is extremely sensitive to how humanity’s story eventually ends. Whether advancing progress is ultimately good or bad depends crucially on whether it also advances the end of humanity. Because we know so little about the answer to this crucial question, the case for advancing progress is undermined. I suggest we must either overcome this objection through improving our understanding of these connections between progress and human extinction or switch our focus to advancing certain kinds of progress relative to others — changing where we are going, rather than just how soon we get there.$^1$*

Things are getting better. While there are substantial ups and downs, long-term progress in science, technology, and values have tended to make people’s lives longer, freer, and more prosperous. We could represent this as a graph of quality of life over time, giving a curve that generally trends upwards.

What would happen if we were to advance all kinds of progress by a year? Imagine a burst of faster progress, where after a short period, all forms of progress end up a year ahead of where they would have been. We might think of the future trajectory of quality of life as being primarily driven by science, technology, the economy, population, culture, societal norms, moral norms, and so forth. We’re considering what would happen if we could move all of these features a year ahead of where they would have been.

While the burst of faster progress may be temporary, we should expect its effect of getting a year ahead to endure.*$^2$* If we’d only advanced *some* domains of progress, we might expect further progress in those areas to be held back by the domains that didn’t advance — but here we’re imagining moving the entire internal clock of civilisation forward a year.

If we were to advance progress in this way, we’d be shifting the curve of quality of life a year to the left. Since the curve is generally increasing, this would mean the new trajectory of our future is generally higher than the old one. So the value of advancing progress isn’t just a matter of impatience — wanting to get to the good bits sooner — but of overall improvement in people’s quality of life across the future.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/e8b504c3-202c-4d20-84d2-b3cb6374fa92/Advancement+%28infinite%29+w.png?format=2500w)

*Figure 1*. *Sooner is better*. The solid green curve is the default trajectory of quality of life over time, while the dashed curve is the trajectory if progress were uniformly advanced by one year (shifting the default curve to the left). Because the trajectories trend upwards, quality of life is generally higher under the advanced curve. To help see this, I’ve shaded the improvements to quality of life green and the worsenings red.

That’s a standard story within economics: progress in science, technology, and values has been making the world a better place, so a burst of faster progress that brought this all forward by a year would provide a lasting benefit for humanity.

But this story is missing a crucial piece.

The trajectory of humanity’s future is not literally infinite. One day it will come to an end. This might be a global civilisation dying of old age, lumbering under the weight of accumulated bureaucracy or decadence. It might be a civilisation running out of resources: either using them up prematurely or enduring until the sun itself burns out. It might be a civilisation that ends in sudden catastrophe — a natural calamity or one of its own making.

If the trajectory must come to an end, what happens to the previous story of an advancement in progress being a permanent uplifting of the quality of life? The answer depends on the nature of the end time. There are two very natural possibilities.

One is that the end time is fixed. It is a particular calendar date when humanity would come to an end, which would be unchanged if we advanced progress. Economists would call this an *exogenous end time*. On this model, the standard story still works — what you are effectively doing when you advance progress by a year is skipping a year at current quality of life and getting an extra year at the final quality of life, which could be much higher.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/077e990d-236c-47cc-a80b-2c179ebb406f/Advancement+%28exo%29+w.png?format=2500w)

*Figure 2*. *Exogenous end time*. Advancing progress with an unchanging end time. Note that the diagram is not to scale (our future is hopefully much longer).

The other natural model is that when advancing progress, the end time is also brought forward by a year (call it an *endogenous end time*). A simple example would be if there were a powerful technology which once discovered, inevitably led to human extinction shortly thereafter — perhaps something like nuclear weapons, but more accessible and even more destructive. If so, then advancing progress would bring forward this final invention and our own extinction.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/903f0bba-eadf-4848-be3f-f09fd6b7b5e1/Advancement+%28endo%29+w.png?format=2500w)

*Figure 3*. *Endogenous end time*. Advancing progress also brings forward the end time.

On this model, there is a final year which is much worse under the trajectory where progress is advanced by a year. Whether we assume the curve suddenly drops to zero at the end, or whether it declines more smoothly, there is a time where the upwards march of quality-of-life peaks and then goes down. And bringing the trajectory forward by a year makes the period after the peak worse, rather than better. So we have a good effect of improving the quality of life for many years combined with a bad effect of bringing our demise a year sooner.

It turns out that on this endogenous model, the bad effect always outweighs the good: producing lower total and average quality of life for the period from now until the original end time. This is because the region under the advanced curve is just a shifted version of the same shape as the region under the default curve — except that it is missing the first slice of value that would have occurred in the first year.*$^3$* Here advancing progress involves skipping a year at the current quality of life and never replacing it with anything else. It is like skipping a good early track on an album whose quality steadily improves — you get to the great stuff sooner, but ultimately just hear the same music minus one good song.

So when we take account of the fact that this trajectory of humanity is not infinite, we find that the value of uniformly advancing progress is extremely sensitive to whether the end of humanity is driven by an external clock or an internal one.

Both possibilities are very plausible. Consider the ways our trajectory might play out that we listed earlier. We can categorise these by whether the end point is exogenous or endogenous.

Exogenous end points:

- enduring until some external end like the sun burning out
- a natural catastrophe like a supervolcanic eruption or asteroid impact

Endogenous end points:

- accumulation of bad features like bureaucracy or decadence
- prematurely running out of resources
- anthropogenic catastrophe such as nuclear war

Whether advancing all kinds of progress by a short period of time is good or bad, is thus extremely sensitive to whether humanity’s ultimate end is caused by something on the first list or the second. If we knew that our end was driven by something on the second list, then advancing all progress would be a bad thing.

⁂

I am not going to attempt to adjudicate which kind of ending is more likely or whether uniformly advancing progress is good or bad. Importantly — and I want to be clear about this — I am not arguing that advancing progress is a bad thing.

Instead, the point is that whether advancing progress is good or bad depends crucially on an issue that is rarely even mentioned in discussions on the value of progress. Historians of progress have built a detailed case that (on average) progress has greatly improved people’s quality of life. But all this rigorous historical research does not bear on the question of whether it will also eventually bring forward our end. All the historical data could thus be entirely moot if it turns out that advancing progress has also silently shortened our future lifespan.

One upshot of this is that questions about what will ultimately cause human extinction *$^4$* — which are normally seen as extremely esoteric — are in fact central to determining whether uniform advancements of progress are good or bad. These questions would thus need to appear explicitly in economics and social science papers and books about the value of progress. While we cannot hope to know about our future extinction with certainty, there is substantial room for clarifying the key questions, modelling how they affect the value of progress, and showing which parameter values would be required for advancing all progress to be a good thing.

Examples of such clarification and modelling would include:

- Considerations of the amount of value at stake in each case.*$^5$*
- Modelling existential risk over time, such as with a time-varying hazard rate.*$^6$*
- Allowing the end time (or hazard curve) to be neither purely exogenous nor purely endogenous.*$^7$*

Note that my point here isn’t the increasingly well-known debate about whether work aimed at preventing existential risks could be even more important than work aimed at advancing progress.*$^8$* It is that considerations about existential risk undermine a promising argument for advancing progress and call into question whether advancing progress is good at all.

Why hasn’t this been noticed before? The issue is usually hidden behind a modelling assumption of progress continuing over an infinite future. In this never-ending model, when you pull this curve sideways, there is always more curve revealed. It is only when you say that it is of a finite (if unknown) length that the question of what happens when we run out of curve arises. There is something about this that I find troublingly reminiscent of a Ponzi scheme: in the never-ending model, advancing progress keeps bringing forward the benefits we would have had in year *t* +1 to pay the people in year *t*, with the resulting debt being passed infinitely far into the future and so never coming due.

Furthermore, the realisation that humanity won’t last for ever is surprisingly recent — especially the possibility that its lifespan might depend on our actions.*$^9$* And the ability to broach this in academic papers without substantial pushback is even more recent. So perhaps it shouldn’t be surprising that this was only noticed now.

The issue raised by this paper has also been masked in many economic analyses by an assumption of pure time-preference: that society should have a discount rate on value itself. If we use that assumption, we end up with a somewhat different argument for advancing progress — one based on impatience; on merely getting to the good stuff sooner, even if that means getting less of it.

Even then, the considerations I’ve raised would undermine this argument. For if it does turn out that advancing progress across the board is bad from a patient perspective, then we’d be left with an argument that ‘advancing progress is good, but only due to fundamental societal impatience and the way it neglects future losses’. The rationale for advancing progress would be fundamentally about robbing tomorrow to pay for today, in a way that is justified only because society doesn’t (or shouldn’t) care much about the people at the end of the chain when the debt comes due. This strikes me as a very troubling position and far from the full-throated endorsement of progress that its advocates seek.

Could attempts to advance progress have some other kind of predictable effect on the shape of the curve of quality of life over time?*$^{10}$* They might. For instance, they might be able to *lengthen* our future by bringing forward the moment we develop technologies to protect us from natural threats to our survival. This is an intriguing idea, but there are challenges to getting it to work: especially since there isn’t actually much natural extinction risk for progress to reduce, whereas progress appears to be introducing larger anthropogenic risks.*$^{11}$* Even if the case could be made, it would be a *different* case to the one we started with — it would be a case based on progress increasing the duration of lived experience rather than its quality. I’d be delighted if such a revised case can be made, but we can’t just assume it.*$^{12}$*

If we were to advance some kinds of progress *relative to others*, we could certainly make large changes to the shape of the curve, or to how long humanity lasts.*$^{13}$* But this is not even a different kind of argument for the value of progress; it is a different kind of intervention, which we could call *differential progress*.*$^{14}$* This would not be an argument that progress is generally good, but that certain parts of it are. Again, I’m open to this argument, but it is not the argument for progress writ large that its proponents desire.

And it may have some uncomfortable consequences. If advancing all progress would turn out to be bad, but advancing some parts of it would be good, then it is likely that advancing the remaining parts would be even more bad. Since some kinds of progress are more plausibly linked to bringing about an earlier demise (e.g. nuclear weapons, climate change, and large-scale resource depletion only became possible because of technological, economic, and scientific progress) these parts may not fare so well in such an analysis. So it may really be an argument for differentially boosting other kinds of progress, such as moral progress or institutional progress, and perhaps even for delaying technological, economic, and scientific progress.

It is important to stress that through all of this we’ve only been exploring the case for *advancing* progress — comparing the default path of progress to one that is shifted earlier. There might be other claims about the value of progress that are unaffected. For example, these considerations don’t directly undermine the argument that progress is better than stasis, and thus that if progress is fragile, we need to protect it. That may be true even if humanity does eventually bring about its own end, and even if our progress brings it about sooner. Or one could understand ‘progress’ to refer only to those cases where the outcomes are genuinely improved, such that it is by definition a good thing. But the arguments we’ve explored show that these other arguments in favour of progress wouldn’t have many of the policy implications that advocates of progress typically favour — as whether it is good or bad to advance scientific research or economic productivity will still depend very sensitively on esoteric questions about how humanity ends.

⁂

I find all this troubling. I’m a natural optimist and an advocate for progress. I don’t want to see the case for advancing progress undermined. But when I tried to model it clearly to better understand its value, I found a substantial gap in the argument. I want to draw people’s attention to that gap in the hope that we can close it. There may be good arguments to settle this issue one way or the other, but they will need to be made. Alternatively, if we do find that uniform advancements of progress are in fact bad, we will need to adjust our advocacy to champion the right kinds of differential progress.

---

$^1$ I’d like to thank Fin Moorhouse, Kevin Kuruc, and Chad Jones for insightful discussion and comments, though of course this doesn’t imply that they endorse the arguments in this paper.

$^2$ The arguments in this paper would also apply if it were instead a temporary acceleration leading to a permanent speed-up of progress. In that case an endogenous end time would mean a *temporal compression* of our trajectory up to that point: achieving all the same quality levels, but having less time to enjoy each one, then prematurely ending.

$^3$ This is proved in more detail, addressing several complications in Ord (forthcoming). Several complexities arise from different approaches to population ethics, but the basic argument holds for any approach to population ethics that considers a future with lower total and average wellbeing to be worse. If your approach to population ethics avoids this argument, then note that whether advancing progress is good or bad is now highly sensitive to the theory of population ethics — another contentious and esoteric topic.

$^4$ One could generalise this argument beyond human extinction. First, one could consider other kinds of existential risk. For instance, if a global totalitarian regime arises which permanently reduces quality of life to a lower level than it is today, then what matters is whether the date of its onset is endogenous. Alternatively, we could broaden this argument to include decision-makers who are partial to a particular country or culture. In that case, what matters is whether advancing progress would advance the end of that group.

$^5$ For example, if final years are 10 times as good as present years, then we would only need a 10% chance that humanity’s end was exogenous for advancing progress to be good *in expectation*. I think this is a promising strategy for saving the *expected* value of progress.

$^6$ In this setting, the former idea of an endogenous end time roughly corresponds to the assumption that advancing progress by a year also shifts humanity’s *survival curve* left by a year, while an exogenous end time corresponds to the assumption that the survival curve stays fixed. A third salient possibility is that it is the corresponding *hazard curve* which shifts left by a year. This possibility is mentioned in Ord (forthcoming, pp. 17 & 30). The first and third of these correspond to what Bostrom (2014) calls *transition risk* and *state risk*.

$^7$ For example, one could decompose the overall hazard curve into an exogenous hazard curve plus an endogenous one, where only the latter gets shifted to the left. Alternatively, Aschenbrenner & Trammell (2024) present a promising parameterisation that interpolates between state risk and transition risk (and beyond).

$^8$ See, for example, my book on existential risk (Ord 2020), or the final section of Ord (forthcoming).

$^9$ See Moynihan (2020).

$^{10}$ Any substantial change to the future, including advancing progress by a year, would probably have large chaotic effects on the future in the manner of the butterfly effect. But only a systematic change to the expected shape or duration of the curve, could help save the initial case for advancing progress.

$^{11}$ The fossil record suggests natural extinction risk is lower than 1 in 1,000 per century — after all humanity has already survived 2,000 centuries and typical mammalian species survive 10,000 centuries. See Snyder-Beattie et al. (2019) and Ord (2020, pp. 80–87).

$^{12}$ Another kind of case that is often made is that the sheer *rate* of progress could change the future trajectory. A common version is that the world is more stable with steady 3–5% economic growth: if we don’t keep moving forward, we will fall over. This is plausible but gives quite a different kind of conclusion. It suggests it is good to advance economic progress when growth is at 2% but may be bad to advance it when growth is 5%. Moreover, unless the central point about progress bringing forward humanity’s end is dealt with head-on, the best this steady-growth argument can achieve is to say that ‘yes, advancing progress may cut short our future, but unfortunately we need to do it anyway to avoid collapse’.

$^{13}$ Beckstead calls this kind of change to where we’re going, rather than just how quickly we get there a ‘trajectory change’ (Beckstead 2013).

$^{14}$ Bostrom’s concept of *differential technological development* (Bostrom 2002) is a special case.

## References

Aschenbrenner, Leopold; and Trammell, Philip. (2024). Existential Risk and Growth. GPI Working Paper No. 13-2024, (Global Priorities Institute and Department of Economics, University of Oxford).

Beckstead, Nick. (2013). *On the Overwhelming Importance of Shaping the Far Future*. PhD Thesis. Department of Philosophy, Rutgers University.

Bostrom, Nick. (2002). Existential Risks: Analyzing Human Extinction, *Journal of Evolution and Technology* 9(1).

Bostrom, Nick. (2014). *Superintelligence: Paths, dangers, strategies*, (Oxford: OUP).

Moynihan, Thomas. (2020). *X-Risk: How Humanity Discovered its Own Extinction*, (Urbanomic).

Ord, Toby. (2020). *The Precipice: Existential risk and the Future of Humanity*, (London: Bloomsbury).

Ord, Toby. (Forthcoming). Shaping humanity’s longterm trajectory. In Barrett et al (eds.) Essays on Longtermism, (Oxford: OUP).

Snyder-Beattie, Andrew E.; Ord, Toby; and Bonsall, Michael B. (2019). An upper bound for the background rate of human extinction. *Scientific Reports* 9:11054, 1–9.

## Robust Longterm Comparisons

## Toby Ord

*The choice of discount rate is crucially important when comparing options that could affect our entire future. Except when it isn’t. Can we tease out a class of comparisons that everyone can agree on regardless of their views on discounting?*

Some of the actions we can take today may have longterm effects — permanent changes to humanity’s longterm trajectory. For example, we may take risks that could lead to human extinction. Or we might irreversibly destroy parts of our environment, creating permanent reductions in the quality of life.

Evaluating and comparing such effects is usually extremely sensitive to what economists call the *pure rate of time preference*, denoted ρ. This is a way of encapsulating how much less we should value a benefit simply because it occurs at a later time. There are other components of the overall discount rate that adjust for the fact that an extra dollar is worth less when people are richer, that later benefits may be less likely to occur — or that the entire society may have ceased to exist by then. But the pure rate of time preference is the amount by which we should discount future benefits *even after all those things have been accounted for*.

Most attempts to evaluate or compare options with longterm effects get caught up in intractable disagreements about ρ. Philosophers almost uniformly think ρ should be set to zero, with any bias towards the present being seen as unfair. That is my usual approach, and I’ve developed a [framework for making longterm comparisons](http://files.tobyord.com/shaping-humanity's-longterm-trajectory.pdf) without any pure time preference. While some prominent economists agree that ρ should be zero, the default in economic analysis is to use a higher rate, such as 1% per year.

The difference between a rate of 0% and 1% is small for most things economists evaluate, where the time horizon is a generation or less. But it makes a world of difference to the value of longterm effects. For example, ρ = 1% implies that a stream of damages starting in 500 years time and lasting a billion years is less bad than a single year of such damages today. So when you see a big disagreement on how to make a tradeoff between, say, economic benefits and existential risk, you can almost always pinpoint the source to a disagreement about ρ.

This is why it was so surprising to read Charles Jones’s recent paper: ‘ [The AI Dilemma: Growth versus Existential Risk](https://web.stanford.edu/~chadj/existentialrisk.pdf) ’. In his examination of whether and when the economic gains from developing advanced AI could outweigh the resulting existential risk, the rate of pure time preference just cancels out. The value of ρ plays no role in his primary model. There were many other results in the paper, but it was this detail that grabbed my attention.

Here was a question about trading off risk of human extinction against improved economic consumption that economists and philosophers might actually be able to agree on. After all, even better than picking the correct level of ρ, deriving the correct conclusion, and yet *still* having half the readers ignore your findings, is if there is a way of conducting the analysis such that you are not only correct — but that everyone else can see that too.

Might we be able to generalise this happy result further?

- Is there are broader range of long run effects in which the discount rate still cancels out?
- Are there other disputed parameters (empirical or normative) that also cancel out in those cases?

What I found is that this can indeed be greatly generalised, creating a domain in which we can robustly compare long run effects — where the comparisons are completely unaffected by different assumptions about discounting.

⁂

Let’s start by considering a basic model where $u(t)$ represents the ‘instantaneous utility’ or ‘flow utility’ of a representative person at time $t$. That is, it is a measure of their wellbeing such that the integral of $u \left(t\right)$ over a period of time is the utility (or wellbeing) the person accrued over that period. This is normalised such that the zero level for $u \left(t\right)$ is the level where someone is indifferent about adding a period at this level to their life.

Now let $n(t)$ represent the number of people alive at time $t$ and let $d \left(t\right)$ be the *discount factor* for time $t$. This discount factor is another way of expressing pure time preference. A constant rate of pure time preference ρ, corresponds to a discount factor that drops exponentially over time: $d \left(t\right) = e^{– \rho t}$. But $d \left(t\right)$ need not drop exponentially — indeed it could be any function at all. So could $n \left(t\right)$ and $u \left(t\right)$. The only constraints are that they are all integrable functions and that the integral below converges to a finite value.

On this model, we’ll say the value of the entire longterm future is:

$$
V = \int_0^\infty  d(t) \cdot n(t) \cdot u(t) \ . \ dt
$$

(This equation assumes the total view in population ethics, where we add up everyone’s utility, but we’ll see later that this can be relaxed.)

Now suppose that we have the possibility of improving the quality of life, from $u(t)$ to some other curve $u^{+} \left(t\right)$, without altering $d \left(t\right)$ or $n \left(t\right)$. And lets make a single substantive assumption: that this improvement is a rescaling of the original pattern of flow utility: $u^{+} \left(t\right) = k \textrm{ } u \left(t\right)$ for some scaling factor $k$. How does this change the value of the future?

$$
V^+ = \int_0^\infty  d(t) \cdot n(t) \cdot k \ u(t) \ . \ dt
$$

$$
V^+ = k \int_0^\infty  d(t) \cdot n(t) \cdot u(t) \ . \ dt
$$

$$
V^+ = k V
$$

So on this model, scaling up a curve of utility over time simply leads to scaling up the discounted total value under that curve.

What about the value of extinction? We can model extinction here by $n(t)$ going to zero. If so, the value of the integral from that point on falls to zero. (Similarly, other kinds of existential catastrophe could be modelled as $u \left(t\right)$ going to zero.)

Now let’s consider the expected value of developing a risky technology, where we have a probability $s$ of surviving the development process and scaling up all future utility by a factor of $k$, but otherwise we go extinct.

$EV$ (develop)   $\textrm{ } = s V^{+} + \left(1 - s\right) 0 = s V^{+} = s k V$

This expected value still depends on the the discount function $d(t)$ because $V$ depends on $d \left(t\right)$. But what if we ask about the decision boundary between when the expected value of taking the risk ($E V$ (develop)) is better or worse than the value of the status quo ($V$). The boundary occurs when they are equal:

$EV$ (develop)   $\textrm{ } = V$

So:

$$
skV = V
$$

$$
s = \frac{1}{k}
$$

This decision boundary for comparing whether it is worth taking on a risk of extinction to make a lasting improvement to our quality of life has no dependence on the discount function $d(t)$. Nor does it depend on the population curve $n \left(t\right)$. And because it doesn’t depend on the population curve, the decision doesn’t depend on whether we weight time periods by their populations or not. It is thus at the same place for either of the two most commonly used version of population ethics within economics: the time integral of total flow utility and the time integral of average flow utility.

And one can generalise even further.

This model assumed that all the extinction risk (if any) happens immediately. But we might instead want to allow for any pattern of risk occuring over time. We can do this via a *survival curve*, where the chance of surviving at least until $t$ is denoted $S \left(t\right)$. This can be any (integrable) non-increasing function that starts at 1. If so, then the expected value of the status quo goes from:

$$
V = \int_0^\infty  d(t) \cdot n(t) \cdot u(t) \ . \ dt
$$

to

$$
EV = \int_0^\infty  S(t) \cdot d(t) \cdot n(t) \cdot u(t) \ . \ dt
$$

And this has simply placed another multiplicative factor inside the integral. So as long as the choice we are considering doesn’t alter the pattern of existential risk in the future, the argument above still goes through. Thus the decision boundary is independent of the future pattern of extinction risk (if that is unchanged by the decision in question).

Jones’s model has more economic detail than this, but ultimately it is a special case of the above. He considers only constant discount rates (= exponential discount functions), assumes no further risk beyond the initial moment, and that the representative flow utility of the status quo, $u(t)$, is constant. He considers the possibility of it changing to some other higher constant level $u^{+} \left(t\right)$, which can be considered a scaled up version of $u \left(t\right)$, where $k = \frac{u^{+} \left(0\right)}{u \left(0\right)}$.

So the argument above generalises Jones’s class of cases where comparisons of longterm effects are independent of discounting in the following ways:

- constant $u(t)$ and $u^{+} \left(t\right)$ $\Rightarrow$ $u \left(t\right)$ may vary and $u^{+} \left(t\right) = k \textrm{ } u \left(t\right)$
- constant ρ $\Rightarrow$ time-varying ρ (so long as value converges)
- constant population growth rate $\Rightarrow$ exogenous time-varying population growth
- total view of population ethics $\Rightarrow$ either total or time integral of average
- no further extinction risk $\Rightarrow$ exogenous time-varying extinction risk

It is worthing noting that Jones’s model is addressing the longterm balance of costs and benefits of advance AI via a question like this:

> if we could either get the benefits of advanced AI at some risk to humanity, or never develop it at all, which would be best?

This is an important question, and one where (interestingly) the way we discount may not matter. On his model it roughly boils down to this: it would be worth reducing humanity’s survival probability from 100% down to $s$ whenever we can thereby scale up the representative utility by a factor of $1 / s$.

In some ways, this is obvious — being willing to risk a 50% chance of death to get some higher quality of life is arguably just what it *means* for that new quality level to be twice the old one. But its implications may nonetheless surprise. After all, it is quite believable that some technologies could make life 10 times better, but a little disconcerting that it would be worth a 90% chance of human extinction to reach them.

One observation that makes this implication a little less surprising is to note that there may be ways to reach such transformative technologies for a lesser price. Just because it may be worth a million dollars to you to get a bottle of water when dying of thirst, doesn’t mean it is a good deal when there is also a shop selling bottles of water for a dollar apiece. Those people who are leading the concern about existential risk from AI are not typically arguing that we should forgo developing it altogether, but that there is a lot to be gained by developing it more slowly and carefully. If this reduces the risk even a little, it could be worth quite a lengthy delay to the stream of benefits. Of course *this* question of how to trade years of delay with probability of existential risk *does* depend on how you discount. Alas.

⁂

In [my own framework on longterm trajectories of humanity](http://files.tobyord.com/shaping-humanity's-longterm-trajectory.pdf), I call anything that linearly scales up the entire curve of instantaneous value over time an *enhancement*. And I showed that like the value of reducing extinction risk, the value of an enhancement scales in direct proportion to the entire value of the future, which makes comparisons between risk reduction and enhancements particularly easy (much as we’ve seen here). But in that framework, there was an explicit assumption of no pure time preference, so I had no cause to notice how ρ (or equivalently, $d(t)$) completely cancels out of the equations. So this a nice addition to the theory of how to compare enhancements to risk reduction.

One might gloss the key result about robustness to discounting procedure as follows:

> When weighing the benefits of permanently scaling up quality of life against a risk of extinction, the choice of discounting procedure makes no difference — nor does the population growth rate or subsequent pattern of extinction risk (so long as these remain the same).

In cases like these, discounting scales down the magnitude of the future benefits and of the costs in precisely the same way, but leaves the location where benefits equal the costs alone. It can thus make a vast difference to *evaluations* of future trajectories, but no difference at all to *comparisons*.

I hope that this region of robustness to the choice of discounting might serve as an island of agreement between people studying these questions, even when they come from very different traditions regarding valuing the future. Moreover, the fact that the comparison is robust to the very uncertain questions of the population size and survival curve for humanity across aeons to come, shows that at least in some cases we can still compare longterm futures despite our deep uncertainty about how the future may unfold.

## The timing of labour aimed at reducing existential risk

## Toby Ord

Work towards reducing existential risk is likely to happen over a timescale of decades. For many parts of this work, the benefits of that labour are greatly affected by when it happens. This has a large effect when it comes to strategic thinking about what to do now in order to best help the overall existential risk reduction effort. I look at the effects of nearsightedness, course setting, self-improvement, growth, and serial depth, showing that there are competing considerations which make some parts of labour particularly valuable earlier, while others are more valuable later on. We can thus improve our overall efforts by encouraging more meta-level work on course setting, self-improvement, and growth over the next decade, with more of a focus on the object-level research on specific risks to come in decades beyond that.

### Nearsightedness

Suppose someone considers AI to be the largest source of existential risk, and so spends a decade working on approaches to make self-improving AI safer. It might later become clear that AI was not the most critical area to worry about, or that this part of AI was not the most critical part, or that this work was going to get done anyway by mainstream AI research, or that working on policy to regulate research on AI was more important than working on AI. In any of these cases she wasted some of the value of her work by doing it now. She couldn’t be faulted for lack of omniscience, but she could be faulted for making herself unnecessarily at the mercy of bad luck. She could have achieved more by doing her work later, when she had a better idea of what was the most important thing to do.

We are nearsighted with respect to time. The further away in time something is, the harder it is to perceive its shape: its form, its likelihood, the best ways to get purchase on it. This means that work done now on avoiding threats in the far future can be considerably less valuable than the same amount of work done later on. The extra information we have when the threat is up close lets us more accurately tailor our efforts to overcome it.

Other things being equal, this suggests that a given unit of labour directed at reducing existential risk is worth more the later in time it comes.

### Course setting, self-improvement & growth

As it happens, other things are not equal. There are at least three major effects which can make earlier labour matter more.

The first of these is if it helps to change course. If we are moving steadily in the wrong direction, we would do well to change our course, and this has a larger benefit the earlier we do so. For example, perhaps effective altruists are building up large resources in terms of specialist labour directed at combatting a particular existential risk, when they should be focusing on more general purpose labour. Switching to the superior course sooner matters more, so efforts to determine the better course and to switch onto it matter more the earlier they happen.

The second is if labour can be used for self-improvement. For example, if you are going to work to get a university degree, it makes sense to do this earlier in your career rather than later as there is more time to be using the additional skills. Education and training, both formal and informal, are major examples of self-improvement. Better time management is another, and so is gaining political or other influence. However this category only includes things that create a lasting improvement to your capacities and that require only a small upkeep. We can also think of self-improvement for an organisation. If there is benefit to be had from improved organisational efficiency, it is generally better to get this sooner. A particularly important form is lowering the risk of the organisation or movement collapsing, or cutting off its potential to grow.

The third is if the labour can be used to increase the amount of labour we have later. There are many ways this could happen, several of which give exponential growth. A simple example is investment. An early hour of labour could be used to gain funds which are then invested. If they are invested in a bank or the stock market, one could expect a few percent real return, letting you buy twice as much labour two or three decades later. If they are invested in raising funds through other means (such as a fundraising campaign) then you might be able to achieve a faster rate of growth, though probably only over a limited number of years until you are using a significant fraction of the easy opportunities.

A very important example of growth is movement building: encouraging other people to dedicate part of their own labour or resources to the common cause, part of which will involve more movement building. This will typically have an exponential improvement with the potential for double digit percentage growth until the most easily reached or naturally interested people have become part of the movement at which point it will start to plateau. An extra hour of labour spent on movement building early on, could very well produce a hundred extra hours of labour to be spent later. Note that there might be strong reasons not to build a movement as quickly as possible: rapid growth could involve increasing the signal to noise ratio in the movement, or changing its core values, or making it more likely to collapse, and this would have to be balanced against the benefits of growth sooner.

If the growth is exponential for a while but will spend a lot of time stuck at a plateau, it might be better in the long term to think of it like self improvement. An organisation might have been able to raise $10,000 of funds per year (after costs) before the improvement and then gains the power to raise $1,000,000 of funds per year afterwards — only before it hits the plateau does it have the exponential structure characteristic of growth.

Finally, there is a matter of serial depth. Some things require a long succession of stages each of which must be complete before the next begins. If you are building a skyscraper, you will need to build the structure for one story before you can build the structure for the next. You will therefore want to allow enough time for each of these stages to be completed and might need to have some people start building soon. Similarly, if a lot of novel and deep research needs to be done to avoid a risk, this might involve such a long pipeline that it could be worth starting it sooner to avoid the diminishing marginal returns that might come from labour applied in parallel. This effect is fairly common in computation and labour dynamics (see The Mythical Man Month), but it is the factor that I am least certain of here. We obviously shouldn’t hoard research labour (or other resources) until the last possible year, and so there is a reason based on serial depth to do some of that research earlier. But it isn’t clear how many years ahead of time it needs to start getting allocated (examples from the business literature seem to have a time scale of a couple of years at most) or how this compares to the downsides of accidentally working on the wrong problem.

### Consequences

We have seen that nearsightedness can provide a reason to delay labour, while course setting, self-improvement, growth, and serial depth provide reasons to use labour sooner. In different cases, the relative weights of these reasons will change. The creation of general purpose resources (such as political influence, advocates for the cause, money, or earning potential) is especially resistant to the nearsightedness problem as they have more flexibility to be applied to whatever the most important final steps happen to be. Creating general purpose resources, or doing course setting, self-improvement, or growth are thus comparatively better to do in the earlier times. Direct work on the cause is comparatively better to do later on (with a caveat about allowing enough time to allow for the required serial depth).

In the case of existential risk, I think that many of the percentage points of total existential risk lie decades or more in the future. There is quite plausibly more existential risk in the 22nd century than in the 21st. For AI risk, the recent FHI survey of 174 experts, the median estimate for when there would be a 50% chance of reaching roughly human level AI was 2040. For the subgroup of those who are part of the ‘Top 100’ researchers in AI, it was 2050. This gives something like 25 to 35 years before we think most of this risk will occur. That is a long time and will produce a large nearsightedness problem for conducting specific research now and a large potential benefit for course setting, self-improvement, and growth. Given a portfolio of labour to reduce risk over that time, it is particularly important to think about moving types of labour towards the times where they have a comparative advantage. If we are trying to convince others to help use their careers to reduce this risk, the best career advice might change over the coming decades from help with movement building or course setting, to accumulating more flexible resources, to doing specialist technical work.

The temporal location of a unit of labour can change its value by a great deal. It is quite plausible that due to nearsightedness, doing specific research now could have less than a tenth the expected value of doing it later, since it could so easily be on the wrong risk, or the wrong way of addressing the risk, or would have been done anyway, or could have been done more easily using tools people later build etc. It is also quite plausible that using labour to produce growth now, or to point us in a better direction, could produce ten times as much value. It is thus pivotal to think carefully about when we want to have different kinds of labour.

I think that this overall picture is right and important. However, I should add some caveats. We might need to do some specialist research early on in order to gain information about whether the risk is credible or which parts to focus on, to better help us with course setting. Or we might need to do research early in order to give research on risk reduction enough academic credibility to attract a wealth of mainstream academic attention, thereby achieving vast growth in terms of the labour that will be spent on the research in the future. Some early object level research will also help with early fundraising and movement building — if things remain too abstract for a long time, it would be extremely difficult to maintain a movement. But in these examples, the overall picture is the same. If we want to do early object-level research, it is because of its instrumental effects on course setting, self-improvement, and growth.

The writing of this document and the thought that preceded it are an example of course setting: trying to significantly improve the value of the long-term effort in existential risk reduction by changing the direction we head in. I think there are considerable gains here and as with other course setting work, it is typically good to do it sooner. I’ve tried to outline the major systematic effects that make the value of our labour vary greatly with time, and to present them qualitatively. But perhaps there is a major effect I’ve missed, or perhaps some big gains by using quantitative models. I think that more research on this would be very valuable.

## A Child's Plaything

## Toby Ord

Imagine if we could somehow show the people of the eighteenth century a simple child’s toy from today — say, a speaking doll.

The common folk would marvel at its ability to speak its few stock phrases. The scientists and engineers would marvel even more at its innards; at the minutely detailed silicon; at the bewildering complexity soon to be within their grasp.

But the economists would be *amazed*. For this design — so far beyond the peak of their world’s powers — was not a gift for a King or Queen, but clearly just a child’s toy. And not just that. The very banality of the toy, the artlessness of the sculpting and the way the paint doesn’t even quite line up with the contours of the doll’s face, prove that this is not the toy of a prince — but of poor child. And they would understand that the people of our time are so wealthy, so powerful, that *every one* *of them* has access to machines with thousands of parts working in concert, and that it is less effort to build such a wondrous machine than to simply paint a doll’s eyebrows in their right places.

## Remembering Peter Eckersley

## Toby Ord

*A eulogy for* [*Peter Eckersley*](https://en.wikipedia.org/wiki/Peter_Eckersley_\(computer_scientist\))*
Delivered at his official* [*memorial service*](https://www.youtube.com/watch?v=WKClWDHSgGk)*
Internet Archive, San Francisco, 4 March 2023*

Twenty-six years ago, I sat down in an underground room at Melbourne University. A hall of identical computers. Next to me was a stylish young man with *this* on his screen:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/d8244421-e5c4-4a4a-9ba1-13bcef79deb5/1+Desktop.jpg?format=2500w)

I couldn’t believe it. My screen was all grey, with a single blue window with white text.

“How did you get it to look like that?” I asked.

“Well, you just need to ‘gvim.fvwm2rc’,” he replied.

“What?”

“No problem, I’ll just send you all my config files and set you up…”

And that was the beginning of a long friendship…

I still love his colour choices. So enduringly Peter. The decadence of the purple and gold, on a green silk waistcoat-ish background. I eventually changed my own background to Waterhouse's [Lady of Shallot](http://www.amirrorclear.net/flowers/visual-art/painting/waterhouse2/Pages/the-lady-of-shalot2.html) and sampled colours from her candles and silks for my text and accents. When we got our [own](https://web.archive.org/web/20030221184145/http://www.cs.mu.oz.au/~pde/bio/index.html) [websites](http://www.amirrorclear.net/flowers/introductions/index.html), they each inherited our unix colour schemes, and our digital identities forked off from that meeting into our own directions, with [traces](http://web.archive.org/web/20220903123709/https://pde.is/about/) still visible and ongoing…

I was in my first year, and Peter his second. Over our undergraduate years, our friendship grew.

Here is my first ever photo of Peter (on the right) in 1998:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/6c0c5317-a856-4bf1-bb6d-da9035d29b6d/2+1998+Melbourne.jpeg?format=2500w)

After a protest march, we had pitched tents in the middle of the most sacred quad at Melbourne University and were in a student politics meeting under the camellia trees at midnight.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/581d171c-95ea-4714-9cbd-d6af03baf263/3+2000+Melbourne.jpg?format=2500w)

Here’s a more typical shot in 2000, at my 21st.

We shared a deep thirst for ideas and a taste for wonder. We would talk about science and technology, about ethics and the nature of reality late, late into the night.

Indeed, while he was chiefly a technologist, he is among the people who have thought the deepest about the long term fate of a universe shaped by intelligence and directed by moral values — about the limits of what we could achieve over the aeons ahead. And he was a natural philosopher too, with [original contributions](https://arxiv.org/pdf/1901.00064.pdf) on the paradoxes at the heart of population ethics. Over the years, we talked about the big picture questions facing humanity, about global poverty and existential risk, and the ideas that would become effective altruism. When I started [Giving What We Can](https://www.givingwhatwecan.org/) in 2009, he was one of 23 [founding members](https://www.givingwhatwecan.org/about-us/members), making a lifelong pledge to donate a tenth of his income to the most cost-effective charities he could find. He wrote:

> "For me, taking a pledge to give is exciting. I've long been persuaded that it would be better to use a good portion of my income to support very effective aid projects, but it's hard to know what they are, and often easier to spend money on luxuries that in the end aren't particularly necessary for happiness. A pledge is a way to ensure that I do what I already wanted to, a way to meet a community of people who think the same way, and a way to work together on finding the most effective projects to contribute to."

Indeed he continues to guide my vision of effective altruism. Last week I ended my keynote talk with a slide about the importance of good character for all of us dedicated to helping others as much as we can. The picture I painted of integrity and earnestness was a picture of Peter.

We also shared an enduring love of beauty. I never found out exactly the form his ideal future might take. But it would be a place of freedom, and wonder, and friends. And beauty everywhere.

In 2003 I left Melbourne to go to the dreaming spires of Oxford and study philosophy. He stayed in Melbourne, transferring from a PhD in Computer Science to one in Law — trying to understand how to refashion an economic system based on physical goods to [one fit for virtual goods](https://jolt.law.harvard.edu/articles/pdf/v18/18HarvJLTech085.pdf) — songs and stories and ideas that once created can be copied freely. A few years later, he got his dream job offer, from the [Electronic Frontiers Foundation](https://www.eff.org/), in faraway San Francisco.

Little did he know, but it would become his home. He would find a subculture within it that was like a distillation of the one he moved in in Melbourne. Let me share his first thoughts on San Francisco:

> Hi guys,
>
> I've been in San Francisco a week, and it's definitely time for an email of stories.
>
> I'm sitting on a "sidewalk" as I write this, on a little timber bench with a coffee and a gorgeous bamboo plant next to me (photo attached:). There's a corset shop next door. As soon as I opened my laptop, I got roped into a conversation with a bunch of geeks -- one of them was asking for advice about Internet regulation in Japan; another worked for Google and was asking me to let them keep their files on everybody. This city is completely packed with nerds; random conversations with them seem to be a regular occurrence.
>
> Working at EFF is remarkable. The organisation is a nerve center for more lawsuits than you could sensibly imagine. Many -- but not all -- of these are a little depressing. Except when they sue purple dinosaurs. My first week has been very busy, but I don't yet have a sense of how normal this is. Aside from numerous administrative diversions, I've been busy writing a white paper on how to keep your web search history private (a surprisingly hard thing to do). The other three technical staff will be away next week -- go and google Burning Man -- so I'm going to find out if I can administer and support the EFF's computer infrastructure too.
>
> The bike culture here is definitely stronger than in Melbourne. Especially where I work, there are bikes everywhere. There also seems to be way more bike Bling. There's this strange subcultural species of people known as "hipsters". Bicycle fashion is an important part of this. Often, they're on fixies, but not always. See, for example, the attached photo of a vague-seeming girl cruising around on a $5,000 bicycle made of bamboo and carbon fibre.
>
> …
>
> I haven't found a house yet. It's back-to-school season, and judging from what I saw at an open house this afternoon, I might not find one for a few weeks. Fortunately, I can continue to sleep in Seth's incredibly precarious spare loft. Getting out of bed in the morning involves hopping onto an a free-standing step ladder. It wakes you up!
>
> Anyway, I'm going to go and explore the corsetry. I'm missing you all. I'll try and set up a website somewhere so that I'm not filling your inboxes with my excessive verbosity (speaking of which, I haven't actually attached any photos but you can see them at http://www.cs.mu.oz.au/~pde/pics/sf/ ).
>
> Let me know what's happening in Melbourne...
>
> P.

Sadly his ‘attached’ pictures are lost to bit rot, but I was looking through all my old photos, and found this — a photo of Peter I took five years later which (given the bamboo and corset shop) must be the exact spot he was sitting when he wrote his email.

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/ce808c97-b891-4667-a17f-6a4be39b133b/4+2011+San+Francisco.jpeg?format=2500w)

We kept up over the decades, with trips back and forth between our new cities. Here he is in 2008:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/401afb23-b642-4259-b840-7e9fc6d509bc/5+2008+San+Francisco.jpeg?format=2500w)

And here are the two of us after we cycled up to Coit tower:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/60ef18ed-8eaf-488e-8633-9e51411f8975/6+2008+San+Francisco.jpg?format=2500w)

Here he is in 2011, looking out over his adopted home:

![](https://images.squarespace-cdn.com/content/v1/562652dbe4b05bbfdc596fd7/25aa01f9-b4e8-4a50-ab7a-eb48438ad79d/7+2011+San+Francisco.jpeg?format=2500w)

It was only after his death that I got a glimmer of just how much he did for the internet over his sixteen years in San Francisco — especially privacy and security. It was only then that I really reflected on how wildly important the internet is, yet how there is no-one whose responsibility it is to keep it going, and to improve it. It is like we are at sea on a great old sailing ship. But there is no captain, and no owner. Peter, is one of a few people who didn’t stand idly by, but stood up and took on the responsibility. We couldn’t even take the ship in to dock, so Peter and others at the EFF took on the crazy, yet essential, task of repairing and rebuilding it at sea…

Peter loved forming connections with people. It was only in the outpouring of emotion after his death that I realised how great a part of his life that was. It was a flood of love for him so strong that for a shining moment even *Twitter* was a place of beauty and wonder.

And I saw how he had made such strong connections with so many people. A node in a network with thousands of strands radiating out from him. I think he measured his wealth in friends, and was a friend-millionaire. But that wasn’t enough. He was too good a computer scientist to be happy with a network like that. It was too brittle, too vulnerable. So he set about making connections between all those other nodes — connecting people who didn’t know they needed each other.

We’re now a network with a missing node at its centre. But we haven’t fallen apart. Because of what he started, there are hundreds of cross-linking paths between us. And we’re not done. Even with a missing node, one can bridge the gap. I’ve only been back here a week, and there are so many conversations with strangers, where my spidey senses tingled and I’ve stopped and asked “Did you know Peter?” — and often they *did*. And just like that, a connection formed.

So this grand overarching project of Peter’s life is not done. But now it’s up to us to make our own introductions to each other, to fill out this grand network, to find those he would have found for us.

And what better way could there be to honour him?

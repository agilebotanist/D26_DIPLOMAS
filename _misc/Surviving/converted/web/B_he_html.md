Scraping: https://arxiv.org/html/2511.04427v3
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://arxiv.org/html/2511.04427v3
  Settled (dom-quiet, 2099ms)
  Extracting content...
  Extracted 95612 characters

--- Content ---

Conference: 23rd International Conference on Mining Software Repositories; April 13–14, 2026; Rio de Janeiro, Brazil23rd International Conference on Mining Software Repositories (MSR ’26), April 13–14, 2026, Rio de Janeiro, BrazilDOI: [10.1145/3793302.3793349](https://doi.org/10.1145/3793302.3793349) ISBN: 979-8-4007-2474-9/2026/04CCS: Software and its engineering Development frameworks and environmentsCCS: Computing methodologies Intelligent agents

How Cursor AI Increases Short-Term Velocity and Long-Term Complexity in Open-Source Projects

Hao He Affiliation: Carnegie Mellon University, Pittsburgh, Pennsylvania, USA, Courtney Miller Affiliation: Carnegie Mellon University, Pittsburgh, Pennsylvania, USA, Shyam Agarwal Affiliation: Carnegie Mellon University, Pittsburgh, Pennsylvania, USA, Christian Kästner Affiliation: Carnegie Mellon University, Pittsburgh, Pennsylvania, USA and Bogdan Vasilescu Affiliation: Carnegie Mellon University, Pittsburgh, Pennsylvania, USA

© cc

###### Abstract.

Large language models (LLMs) have demonstrated the promise to revolutionize the field of software engineering. Among other things, LLM agents are rapidly gaining momentum in software development, with practitioners reporting a multifold increase in productivity after adoption. Yet, empirical evidence is lacking around these claims. In this paper, we estimate the *causal* effect of adopting a widely popular LLM agent assistant, namely Cursor, on *development velocity* and *software quality*. The estimation is enabled by a state-of-the-art difference-in-differences design comparing Cursor-adopting GitHub projects with a matched control group of similar GitHub projects that do not use Cursor. We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity. Further panel generalized-method-of-moments estimation reveals that increases in static analysis warnings and code complexity are major factors driving long-term velocity slowdown. Our study identifies quality assurance as a major bottleneck for early Cursor adopters and calls for it to be a first-class citizen in the design of agentic AI coding tools and AI-driven workflows.

Figure 1. Our theory around how LLM agent assistants impact software development. Solid lines indicate causal relationships supported by our analysis; dashed lines indicate partial evidence; and dotted lines indicate inconclusive evidence.

## 1\. Introduction

Large language models (LLMs) have demonstrated remarkable capabilities in code generation, achieving near-human performance across various software engineering tasks [^36] [^53]. Among emerging applications, LLM agent assistants—tools that combine LLMs with autonomous capabilities to inspect project files, execute commands, and iteratively develop code—represent a particularly promising direction for integrating LLMs into software development. For example, Cursor [^28], a popular LLM agent assistant, has generated considerable enthusiasm among practitioners, with developers self-reporting multi-fold (as large as 10x) productivity increases and claiming transformative workflow impacts [^94] [^54].

However, substantial concerns have been raised about the quality of LLM-generated code and the long-term consequences of AI-driven development workflows. Studies documented that AI coding assistants can produce code with security vulnerabilities [^84] [^86], performance issues [^65], code smells [^95], and increased complexity [^68]. Yet, these findings, derived from evaluations of early Codex models in controlled experiments [^86], completion-based tools like early GitHub Copilot [^84] [^65] [^95], or chat-based interfaces like ChatGPT [^68], may not generalize to modern LLM agent assistants, which represent a qualitative shift in architecture and integration, not simply incremental improvement. Completion tools suggest individual lines based on immediate context; chat-based assistants require context-switching to formulate queries and integrate responses. Both operate at the periphery of the development workflow, with developers remaining the primary agents and maintaining oversight of AI-generated code at a granular level.

LLM agent assistants like Cursor, by contrast, are tightly integrated into the IDE with persistent codebase awareness, autono-mously navigating files, proposing multi-file refactorings, and implementing features spanning dozens of files—all within the development environment. This architectural difference has profound implications that cannot be extrapolated from prior studies: Automation scope shifts from accelerating typing to automating entire workflows; seamless integration may enable both productivity gains and over-reliance or reduced code review rigor; quality implications of reviewing large, AI-generated multi-file changes differ fundamentally from reviewing line-by-line completions; and temporal dynamics may involve longer-term effects as technical debt accumulation. Consequently, prior findings about security vulnerabilities in Copilot completions or complexity issues in ChatGPT-generated functions provide limited insight into whether—and how—these issues manifest in agentic tools that generate code at a substantially larger scale with different developer oversight patterns.

This gap between generations of AI coding tools also shows up in recent research. For example, [^9] show through controlled experiments that early-2025 AI tools, including Cursor, do not help experienced open-source developers solve real day-to-day tasks faster, pointing to potential slowdown mechanisms such as developer over-optimism, low AI reliability, and high task complexity. Their findings contradict substantial prior literature on earlier-generation AI coding assistants [^113] [^106] [^56] [^34] [^85] [^52] [^111] [^97] [^25] [^82] [^100], which generally found modest velocity improvements from code completion tools like early GitHub Copilot.

Most recently, [^109] take an important step toward understanding modern agentic tools by examining 567 pull requests generated by Claude Code, finding that 83.8% are accepted and merged. However, their analysis focuses on PR acceptance rates and task types rather than on longitudinal, project-level effects of tool adoption on development velocity and code quality. Whether high acceptance rates of individual agent-generated PRs translate into sustained productivity gains and maintained quality at the project level—or whether quality degradation accumulates as teams integrate these tools into everyday workflows over months—remains an open empirical question. To address this gap, we ask:

RQ: *How does the adoption of LLM agent assistants impact project-level development velocity and code quality?*

We focus on Cursor, one of the earliest and most widely adopted LLM agent assistants [^1], as our empirical case. Our key insight is that the presence of.cursorrules configuration files in GitHub repositories signals the adoption of Cursor’s multi-file editing and agentic capabilities, and thus the date of the first commit touching these configuration files serves as a proxy for the adoption date of the modern Cursor client with agentic coding features.<sup>1</sup> By scanning Cursor configuration files across GitHub, we identify 806 repositories that adopted the modern Cursor client, with most of the adoptions happening between August 2024 and March 2025.

We then use a *difference-in-differences* (DiD) design with staggered adoption [^13] [^11], comparing repositories that adopt Cursor at different times to a matched control group that never adopts during our observation period. This *quasi-experimental* approach uses naturally occurring variation in adoption timing to identify causal effects while controlling for repository-specific characteristics and common temporal trends. To construct a comparable control group, we use propensity score matching [^8] to select 1,380 similar repositories from those never adopting Cursor during our observation period. Our matching model incorporates the dynamic history of repository characteristics—activity levels, contributor counts, and development patterns over the six months preceding potential adoption—ensuring treated and control repositories exhibit similar observable trajectories before adoption.

To estimate treatment effects, we use *the [^11] imputation estimator*, a modern DiD approach designed for staggered adoption that avoids biases from traditional two-way fixed effects models. Using this approach, we estimate the impact of Cursor adoption on two velocity outcomes (commits and lines added) and three code quality outcomes (static analysis warnings, code complexity, and duplicate line density). Finally, to test temporal interactions between outcomes, we also estimate the impact of changes in code quality on future development velocity (and vice versa) using *panel generalized method of moments* (GMM) models [^4].

Our findings reveal a concerning picture among GitHub open-source projects adopting Cursor. First, the adoption of Cursor leads to significant, large, but transient velocity increases: Projects experience 3-5x increases in lines added in the first adoption month, but gains dissipate after two months. Concurrently, we observe persistent technical debt accumulation: Static analysis warnings increase by 30% and code complexity increases by 41% post-adoption according to the [^11] DiD estimator. Panel GMM models reveal that accumulated technical debt subsequently reduces future velocity, creating a self-reinforcing cycle. Notably, Cursor adoption still leads to significant increases in code complexity, even when models control for project velocity dynamics.

These findings carry important implications for research and practice. Our longitudinal evidence of how Cursor affects real-world software projects reveals complex temporal dynamics between AI-augmented velocity gains and quality outcomes (Figure 1), warranting further investigation. For practitioners, our results suggest that deliberate process adaptations—those that scale quality assurance with AI-era velocity—are necessary to realize sustained benefits from the use of LLM agent assistants. Our findings also highlight the need for quality assurance as a first-class design citizen in AI-driven development tools and workflows, suggesting directions for improvement in tool design and model training.

## 2\. Related Work

The human-level performance of recent LLMs enables their practical applications to various software engineering tasks, such as code completion [^55], code review [^69], and testing [^92] (see also the two surveys by [^36] and [^53]). The 2024 Stack Overflow Developer Survey shows that 76% of all respondents are using or planning to use LLM tools in their development process [^2]. This wide adoption raises two main questions for researchers: (1) To what extent do LLMs improve developer productivity? (2) To what extent should we trust the code generated by LLMs?

A large body of prior research on the productivity impact of LLMs focuses on *code completion tools* —mostly the pre-agentic GitHub Copilot [^113] [^106] [^56] [^34] [^85] [^52] [^111] [^97] [^25] [^82] [^100], with only a few execeptions [^83] [^63]. Evidence from small-scale, constrained randomized controlled experiments demonstrates a productivity increase ranging from 21% [^97] to 56% [^85], as measured by task completion time. Field experiments conducted at Microsoft, Accenture, and Cisco report similar numbers (from 22% [^25] to 36% [^82]). The productivity increase estimated from open-source projects on observational data is similar and sometimes lower: a DiD design comparing Python and R packages estimates a 17.82% increase in new releases among Python packages after Copilot availability [^111] —without clear knowledge of which packages used Copilot. Another study of proprietary Copilot backend data estimates only a 6.5% increase in project-level productivity, as measured by the number of accepted pull requests [^97]. A more general study using a neural classifier to identify AI-generated code on GitHub shows moving to 30% AI use raises quarterly commits by 2.4% [^31]. Studies point to various mechanisms causing the productivity increase, such as how LLM adoption increases work autonomy [^52] and helps iterative development tasks (e.g., bug fixing) [^111].

Although the productivity gains are promising, there are also increasing concerns around the trustworthiness of LLM-generated code. For example, it is well-known that LLMs may generate code with security vulnerabilities [^84] [^60] [^41] [^3] [^68], performance regressions [^65], code smells [^95], and outdated APIs [^59] [^108]. On the other hand, evidence regarding the complexity of LLM-generated code compared to humans is inconclusive [^77] [^21] [^71]. The LLM trustworthiness problem becomes more complicated with humans in the loop. For example, prior controlled experiments report mixed results on whether developers write more or less secure code with the help of LLMs [^86] [^78] [^90], and studies often suggest heterogeneous treatment effects of LLMs on developers of different skill levels [^30] [^85] [^97] [^25]. While prior work points to many mechanisms by which adopting LLMs may affect software quality, their findings are typically derived from benchmark analyses [^84] or developer opinions [^71]. We are unaware of any prior studies that systematically investigated project-level quality outcomes in the wild after LLM adoption, let alone those that used rigorous causal inference techniques (the closest being the study by [^111] discussed above).

Recently, there has been an increasing interest in the application of *LLM agents* —LLMs with the capability to autonomously utilize external resources and tools—to software engineering [^57] [^50] [^67]. A popular application scenario is an *LLM agent assistant* within a code editor, in which LLMs are allowed to inspect/edit project files, conduct web searches, and execute shell commands to fulfill prompts provided by developers. At the time of writing, there are several production-ready code editors with built-in LLM agent assistants, such as Cursor [^28], VS Code [^107], Windsurf [^110], Tabnine [^102], and Cline [^23], with the extreme beginning to shift away from IDEs entirely and switching to command-line or web interfaces, such as Claude Code [^22] and OpenHands [^80]. These agentic tools are seeing rapid adoption among developers, as evidenced also in our data for Cursor in Figure 2. From the gray literature, we see extremely optimistic estimates of the productivity boost from LLM agent assistants: for example, developers self-report multi-fold productivity increases in a Reddit post [^94], orders of magnitude larger than any empirical estimates for prior LLM tools. However, a recent controlled study with human participants shows that developers may be overoptimistic and that adopting LLM agent assistants does not make them faster in real-world open-source development tasks [^9]. To the best of our knowledge, empirical evidence regarding the impact of LLM agent assistants on *long-term project-level outcomes*, especially *software quality outcomes*, is still lacking.

Our contribution is two-fold. First, our DiD design looks at the additional project-level productivity gain, if any, from using a modern agentic coding assistant (Cursor) *relative to the state-of-the-practice* (likely a mixture of human-written code and code generated by earlier-generation AI tools). Second, we provide a comprehensive analysis of the impact of adopting Cursor on code quality, which is the first to the best of our knowledge, and highlight potential velocity-quality trade-offs and their complex interactions.

## 3\. Research Design and Methods

We estimate the *causal* effects of adopting Cursor on *development velocity* and *code quality*, both of which are considered important project outcomes, are commonly measured in prior research, and are closely tied to perceived overall project productivity [^40] [^79] [^20]. We start by building a dataset with: (1) repositories adopting Cursor at different times and (2) comparable repositories that never adopted Cursor (Section 3.1). Then, we define our specific outcomes of interest and additional covariates (Section 3.2). The estimation of Cursor’s causal effect on these outcomes is enabled by a difference-in-differences (DiD) design with staggered adoption [^11] (Section 3.3): Under the assumption that similar repositories would, on average, evolve similarly in the absence of Cursor adoption (i.e., the *parallel trend assumption*), later-adopters and never-adopters can effectively serve as a quasi-experimental comparison group for earlier-adopters while accounting for observable covariates and macro trends (e.g., open-source repositories overall getting more or less active over time). Finally, since the results from DiD suggest *interactions* between development velocity and software quality, as also indicated in prior work [^20] [^10], we fit dynamic panel generalized method of moments (GMM) models [^4] to support our interpretation of the DiD results (Section 3.4).

### 3.1. Data Collection

#### 3.1.1. The Cursor IDE

Cursor [^28] is an AI-powered IDE built as a VS Code fork with agentic capabilities integrated into the development workflow. Unlike earlier code completion tools, Cursor’s agentic mode enables an autonomous, goal-directed AI workflow: The agent can navigate entire codebases, infer project architecture across multiple files, make multi-file edits, run terminal commands, execute tests, and iteratively debug code, with humans mainly serving as supervisors rather than traditional coders. Using this workflow, developers can rely entirely on AI for feature implementation, refactoring, test generation, documentation, and bug fixing within their native development environment. They can choose between frontier models from OpenAI, Anthropic, and Google, either via Cursor’s built-in service or their own API keys.

We chose Cursor as our main study case for two reasons. First, our preliminary exploration found widespread and growing adoption compared to competing tools, providing sufficient statistical power for causal inference. Second, Cursor is among the earliest to allow optional configuration files (e.g.,.cursorrules) in the git repository to direct AI behavior [^27], leading to an adoption event proxy timestamp in the version control history and a scalable identification strategy based on these files. However, this identification strategy also has important limitations (Section 3.5), which we will address through robustness checks (Section 4.3).

#### 3.1.2. Identifying GitHub Projects Adopting Cursor

We identify Cursor-adopting repositories and track adoption dates through configuration files in the git history. In the GitHub code search API [^89], we query for repositories with.cursorrules files or.cursor folders. Since the API limits results to 1,000 per query, we implement an adaptive partitioning algorithm based on file sizes: For each query with size interval $[a,b]$, we create two queries $[a,(a+b)/2)$ and $[(a+b)/2,b]$ until results fall below 1,000. This discovered 23,308 Cursor files across 3,306 non-fork repositories as of March 2025.

To filter non-software, educational, toy, and spam repositories [^58] [^49], we follow prior work [^48] [^51] [^98] by requiring at least 10 stars at collection time—a threshold achieving 97% precision in identifying engineered projects [^74]. This yields 806 repositories with adoption dates between January 2024 and March 2025 that are still available on GitHub at the time of data analysis (August 2025).

As expected, the dataset is highly skewed across many repository-level metrics (Table 1), and adoption time is staggered, with adoptions growing over time (Figure 2). These dataset characteristics motivate us to adopt a DiD design with staggered adoption and a matched control group, as we will discuss in the remainder of this section. While we did not filter based on activity levels here, activity-based subsets will be used as part of our robustness checks. The top five primary programming languages in our dataset are: TypeScript (366 repositories), Python (118 repositories), JavaScript (60 repositories), Go (36 repositories), and Rust (24 repositories).

Table 1. Descriptive statistics of the 806 repositories using Cursor, collected at the time of data collection (April 2025).

|  | Mean | Min | 25% | Median | 75% | Max |
| --- | --- | --- | --- | --- | --- | --- |
| Age (days) | 1,002.3 | 283 | 361.5 | 521.5 | 1164.2 | 6,208 |
| Stars | 1,475.3 | 10 | 20.0 | 51.0 | 242.0 | 122,280 |
| Forks | 215.9 | 0 | 3.0 | 9.0 | 37.0 | 51,745 |
| Contributors | 19.2 | 0 <sup>*</sup> | 1.0 | 3.0 | 10.0 | 461 |
| Commits | 1,816.6 | 1 | 49.0 | 209.0 | 951.8 | 86,954 |
| Issues | 1,070.3 | 0 | 3.0 | 31.5 | 232.5 | 100,614 |
| Pull Requests | 719.6 | 0 | 1.0 | 18.0 | 161.8 | 72,015 |

- The GitHub API will return zero contributors for a repository if none of its commits can be mapped back to a GitHub user.

Figure 2. The Cursor adoption time of the 806 repositories in our study, which all have $\geq$ 10 stars and Cursor configuration files at the time of data collection (April 2025).

#### 3.1.3. Building a Control Group via Propensity Score Matching

A staggered DiD design usually requires a “never-treated” group to serve as comparison units, which, in our case, means repositories that never adopted Cursor (i.e., *never-adopters*). This comparison allows for a causal interpretation under the parallel trend assumption: Repositories that adopted Cursor should, on average, evolve similarly in the absence of Cursor adoption compared to the control group. However, this assumption is unlikely to hold if there are systematic differences between Cursor-adopting repositories and the control group. Repositories adopting Cursor may be more active, more rapidly growing, and have larger communities compared to random never-adopter repositories, leading to biased estimates.

To address these potential confounders and build a comparable quasi-experimental control group, we use *propensity score matching* [^12] [^8]. The high-level idea is to estimate propensity scores (i.e., the probability of adoption conditional on pre-adoption covariates) for each Cursor-adopting repository and a large population of other GitHub repositories, and retain only never-adopter repositories with propensity scores similar to those of the control group. Specifically, we define this population as all GitHub repositories with $\geq$ 10 stars (matching our inclusion threshold for Cursor adopters). For each month with major Cursor adoptions (August 2024—March 2025), we collect monthly time series from GHArchive [^42] for all repositories in the population: age, active users, stars, forks, releases, pull requests, issues, comments, and total events.

Rather than static snapshots, we fit propensity score models to capture dynamics: repositories experiencing rapid growth or changing patterns may be more likely to adopt new tools. Let $T_{it}$ denote repository age and $X_{it}$ denote remaining covariates for repository $i$ at month $t$. We estimate propensity scores $P(\text{treat}|t,T_{i},X_{i})$ (i.e., the probability of getting treated given $t$ and repository-level covarates $T_{i}$, $X_{i}$) via the following logistic regression:

$$
\log\frac{P(\text{treat}|...)}{1-P(\text{treat}|...)}=\alpha+\beta T_{i,t-1}+\sum_{j=1}^{6}\Gamma_{j}X_{i,t-j}+\Theta\sum_{j=7}^{\infty}X_{i,t-j}+\epsilon_{i}
$$

where $\alpha$, $\beta$, $\Gamma_{j}$ and $\Theta$ are regression parameters. This effectively captures: (1) repository maturity ($T_{i,t-1}$), as older repositories may have different adoption patterns, (2) recent dynamics ($\sum_{j=1}^{6}\Gamma_{j}X_{i,t-j}$), i.e., month-by-month evolution over six months captures trends and growth, and (3) historical baselines ($\Theta\sum_{j=7}^{\infty}X_{i,t-j}$), i.e., cumulative history providing context on overall project scale and activity. By including lags, we ensure that propensity scores reflect both activity level and trajectory—two repositories with identical July 2024 pull requests may differ if one is growing while the other declines; such longitudinal characteristics may correlate with both Cursor adoption and long-term velocity and quality outcomes.

Since candidate repositories outnumber Cursor adopters by orders of magnitude, we sample at most 10,000 candidates per Cursor adoption month to avoid extreme imbalance and improve fit. This yields AUC values ranging from 0.83 to 0.91, indicating high discriminative power in the fitted logistic regression models. For each Cursor-adopting repository, we perform 1:3 nearest-neighbor matching (three controls per treated unit). While 1:1 or 1:2 is most common [^7] [^88], many adopters matched the same control during 1:1 matching, so 1:3 provides higher control group diversity. We additionally match only repositories with the same primary language (queried from GitHub API, unavailable in GHArchive), controlling for language-specific LLM performance differences [^17] [^104]. This yields a matched “never-treated” group with similar propensity score distributions and pre-adoption characteristics (see Appendix). Following standard quasi-experimental terminology, we refer to the sample of repositories adopting Cursor as the *treatment group* and the matched “never-treated” repositories not using Cursor as the *control group* in the remainder of this paper.

### 3.2. Metrics

For each repository in the treatment and control group, we collect monthly outcome metrics and time-varying covariates from January 2024 to August 2025. This ensures that there are at least six months of observations pre- and post-adoption for the treatment group and abundant comparison observations from the control group in each month, providing statistical power for DiD-based causal inference. Note that the dataset is an *unbalanced panel*, as not all repositories have observations over the entire observation period.

#### 3.2.1. Outcomes

For repository $i$ at month $t$, we collect two outcome metrics related to development velocity, a key dimension of software engineering productivity [^75] [^20]:

- Commits <sub>it</sub>: Number of commits in repository $i$ at month $t$;
- Lines Added <sub>it</sub>: Total lines added, summed over all commits in repository $i$ at month $t$.

Both have been used as productivity proxies [^73] [^64] [^93] with moderate-to-strong correlation with perceived productivity [^79].

Software quality is multi-faceted and difficult to capture with a single metric [^18] [^61] [^81] [^39]. Quality can be pivoted on defect density [^44], specification rigor [^38], user satisfaction [^33], or technical debt [^35]. However, many metrics cannot be reliably and scalably collected from version control data. In this study, we take the technical debt perspective [^70] and test three source code maintainability metrics that can be reasonably estimated with static analysis: *static analysis warnings*, *duplicate line density*, and *code complexity*. All three are arguably positively correlated with project-level technical debt and negatively correlated with perceived code quality. Specifically, we use a local SonarQube Community server [^96] to compute these outcome metrics for repository $i$ at month $t$:

- Static Analysis Warnings <sub>it</sub>: Total number of reliability, maintainability, and security issues for repository $i$ at month $t$, as detected by SonarQube’s static analysis. We refer to them as warnings, since static analysis can generate false positives [^45]; this metric should be viewed as an estimate of the effort required to review potential issues in a project.
- Duplicate Line Density <sub>it</sub>: Percentage of duplicated lines in codebase for repository $i$ at month $t$. SonarQube’s definition varies across programming languages, but usually requires at least 10 consecutive duplicate statements or 100 duplicate tokens to mark a block as duplicate [^105].
- Code Complexity <sub>it</sub>: Overall cognitive complexity [^14] of codebase for repository $i$ at month $t$. Per SonarQube [^14], this metric quantifies code understandability and aligns better with modern coding practices than classic cyclomatic complexity [^72].

#### 3.2.2. Time-Varying Covariates

We control for the following time-varying covariates in our models for all treatment and control repositories over the entire observation period (Jan 2024 to Aug 2025): lines of code, age (days), number of contributors at month $t$, number of stars received at month $t$, number of issues opened at month $t$, and number of issue comments added at month $t$. Lines of code is collected from SonarQube [^96] along with outcome metrics; number of contributors is estimated from version control history; remaining covariates are estimated from GHArchive event data [^42]. Multi-collinearity analysis reveals that number of issues opened and number of issue comments added are highly correlated (Pearson’s $\rho>0.7$), so we exclude issue comments from subsequent modeling.

### 3.3. Difference-in-Differences

#### 3.3.1. Background

DiD is an established econometric technique for causal inference in observational data [^15] [^26], with growing adoption in software engineering [^76] [^37] [^16]. The key idea is to compare outcome changes in a treatment group to those in a control group (i.e., those not-yet-treated or never-treated) over the same observation periods. The name “difference-in-differences” originates from the fact that temporal changes are first differenced before differencing the outcome changes between the two groups, effectively isolating the effect of an intervention from other factors that affect all repositories similarly over the same period.

A DiD design critically relies on the parallel trends assumption for a causal interpretation: Absent treatment, the treatment and control group should, on average, follow similar outcome trajectories over the same period. While this assumption is generally not directly testable (would need a time machine), *pre-trend tests* are often used for assessing the *plausibility* of this assumption: If the model predicts similar outcomes for the treatment and control groups *before the adoption*, it is more plausible that the treatment group would evolve similarly if they were not exposed to the treatment. Apart from pre-trend tests, a matching process that controls for observable differences pre-adoption (e.g., Section 3.1.3) also strengthens the plausibility of this assumption in a specific research context.

In a DiD design, a staggered adoption setting comes with both promises and perils [^5] [^11]. In this setting, treatments occur at different times across cohorts rather than simultaneously (as in our case, Figure 2), and each treatment unit has repeated observations both before and after treatment. This setting enables repeated, multiple natural experiments: Later-adopters in the treatment group can serve as additional controls for those adopting before them, since they remain untreated during earlier periods. However, a staggered adoption setting also presents significant mathematical challenges to achieve consistent, efficient, and unbiased estimation of the causal effect [^32] [^5] [^43] with ongoing active research [^13] [^11].

#### 3.3.2. The Estimation Targets

In a DiD design, researchers are often interested in estimating the following two types of causal effects: (1) $ATT$, the average treatment effect on treated, and (2) $ATT_{h}$, the “horizon-average” treatment effect in a specific horizon $h$ (i.e., the effect in $h$ periods since the treatment). We define the two estimation targets mathematically in this section.

Let $\Omega=\{it\}$ denote the set of all observations from repository $i$ and month $t$, $\Omega_{1}$ denote the set of treated observations, and $\Omega_{0}$ denote the set of untreated (i.e., never-treated and not-yet-treated) observations. Let $Y_{it}$ denote the *actual* outcome of interest for repository $i$ at month $t$, and $Y_{it}(0)$ denote the *potential* outcome for repository $i$ at month $t$ if it is never treated. ATT is defined as the average of this causal treatment effect on all treated observations:

$$
ATT=\frac{1}{|\Omega_{1}|}\sum_{it\in\Omega_{1}}\mathbb{E}[Y_{it}-Y_{it}(0)]
$$

Let $\Omega_{1,h}$ denote the set of all treated observations $h$ time periods after the treatment; $ATT_{h}$ is defined as the average of the causal treatment effect in that specific horizon $h$:

$$
ATT_{h}=\frac{1}{|\Omega_{1,h}|}\sum_{it\in\Omega_{1,h}}\mathbb{E}[Y_{it}-Y_{it}(0)]
$$

#### 3.3.3. The Estimator

There are many possible methods to estimate $ATT$ and $ATT_{h}$ defined in Section 3.3.2, among which the two-way fixed effects (TWFE) estimator is most commonly used in early econometric studies. However, recent research shows that TWFE may produce biased estimates in the staggered adoption setting if treatment effects are heterogeneous over time [^32] [^5] [^43]. To address this known limitation, we use the *[^11] imputation estimator*, a state-of-the-art estimator designed explicitly for robust and efficient estimation in the staggered adoption setting, with this two-step process:

Step 1: Impute counterfactual outcomes. The estimator fits a counterfactual outcome regression model, *using only untreated observations* $\Omega_{0}$ (i.e., pre-adoption observations for treated repositories and all observations for never-treated controls):

$$
\hat{Y}_{it}(0)=\hat{\mu}_{i}+\hat{\lambda}_{t}+\hat{\Gamma}^{\prime}Z_{it}+\epsilon_{it}
$$

where $\hat{\mu}_{i}$, $\hat{\lambda}_{t}$ represent per-repository and per-month fixed effects; $Z_{it}$ includes time-varying covariates (Section 3.2.2), and $\epsilon_{it}=Y_{it}-\hat{Y}_{it}$, $it\in\Omega_{0}$ is the error term when fitting this model on $\Omega_{0}$. The use of only $\Omega_{0}$ in this step ensures that counterfactual predictions are not contaminated by treatment effects as in the TWFE estimator. It is also important to note that all repository-invariant confounders (e.g., team culture, domain, language) are effectively controlled by per-repository fixed terms $\hat{\mu}_{i}$ and all time-invariant confounders (e.g., industry trends, platform changes, and seasonal patterns) are effectively controlled by per-month fixed terms $\hat{\lambda}_{t}$ in this step.

Step 2: Compare actual to counterfactual. For each repository-month post-adoption ($it\in\Omega_{1}$), the estimator predicts the potential outcome from the counterfactual outcome model: $\hat{Y}_{it}(0)=\hat{\mu}_{i}+\hat{\lambda}_{t}+\hat{\Gamma}^{\prime}X_{it}$. We replace the $Y_{it}(0)$ in Equations 2 and 3 with the estimated $\hat{Y}_{it}(0)$, to get the final $ATT$ and $ATT_{h}$ estimations.

Finally, to assess the plausibility of the parallel trend assumption, [^11] advises fitting an alternative model of $Y_{it}$ for untreated observations $\Omega_{0}$ with additional observables. In our paper, we follow the most typical convention and fit the following model with additional dummies before the onset of treatment:

$$
Y_{it}=\hat{\mu}_{i}+\hat{\lambda}_{t}+\hat{\Gamma}^{\prime}Z_{it}+\sum_{h=-k}^{-2}\hat{\tau}_{h}\mathbf{1}[t=E_{i}+h]+\epsilon_{it}
$$

where $E_{i}$ means the time of treatment for repository $i$ and $\mathbf{1}[t=E_{i}+h]$ is equal to $1$ if and only if the current time $t$ is $h$ months away from treatment (0 otherwise). Then, we use heteroscedasticity- and cluster-robust Wald tests [^11] to test the joint null hypothesis that $\hat{\tau}_{h}=0$ for $h=-k,...,-2$. We drop $h=-1$ due to potential anticipation concerns (the developer may try use Cursor before adding Cursor rule files in the immediate month before). One way of viewing the above pre-trend testing procedure is a placebo test, in which $\tau_{h}$ estimates $ATT_{h}$ for $h<0$, which should be zero if the treatment has not yet happened. The estimated $\hat{\tau}_{h}$ for $h<0$ and $ATT_{h}$ for $h>0$ are often combined into *event study plots* (e.g., Figure 3), in which the dynamic effect of treatment is visualized.

Note that the [^11] imputation estimator has many alternative specifications with varying assumptions, and we merely describe the version we used in our paper. We refer interested readers to the original paper [^11] regarding alternative specifications and the mathematical assumptions behind them. The [^11] estimator is also not the only option, and we present results from alternative DiD estimators (TWFE and [^13]) in the Appendix as additional robustness checks.

### 3.4. Testing Velocity & Quality Interactions

While DiD estimates treatment effects on individual outcomes, it does not capture temporal dynamics between outcomes. However, it is known that velocity and quality outcomes interact in our setting [^20] [^10]. Plus, our DiD results (Section 4) also suggest interactions, showing that the adoption of Cursor leads to non-sustained velocity increases and sustained quality declines: Development velocity increases may cause rapid technical debt accumulation, which may subsequently decrease velocity.

To test for dynamic relationships and bidirectional causality, we use the *generalized method of moments* (GMM) [^47] to obtain consistent estimates when variables are potentially endogenous (correlated with unobserved errors). The key insight is to use *instrumental variables* —correlated with endogenous regressors but uncorrelated with errors—to identify causal effects. In panel data, lagged values serve as natural instruments, assuming past values influence current values but are uncorrelated with current shocks [^4].

In our study, we use Arellano-Bond dynamic panel GMM [^4], suited for: (1) dynamic dependence (current outcomes depend on past); (2) potential bidirectional causality; (3) short time series with many entities. To test a causality direction $X_{t}\to Y_{t}$ while accounting for Cursor adoption $D$, we estimate the following regression:

$$
Y_{it}=\hat{\mu}_{i}+\hat{\lambda}_{t}+\hat{\rho}Y_{i,t-1}+\hat{\beta}D_{it}+\hat{\gamma}X_{it}+\hat{\Gamma}^{\prime}Z_{it}+\epsilon_{it}
$$

where $Y_{i,t-1}$ captures outcome persistence; $D_{it}$ is a dummy representing Cursor adoption; $X_{it}$ represents the potentially endogenous regressor of interest; the remainig follows Equation 4. During estimation, historical values of $X_{it}$ (e.g., a linear combination of $X_{i,t-2}$ and $X_{i,t-3}$) are used as instrumental variables.

Specifically, we test the following temporal interactions:

$$
\displaystyle\text{Lines Added}_{it}
$$

$$
\displaystyle\to\text{Static Analysis Warnings}_{it}
$$

$$
\displaystyle\text{Lines Added}_{it}
$$

$$
\displaystyle\to\text{Code Complexity}_{it}
$$

$$
\displaystyle\text{Static Analysis Warnings}_{it}
$$

$$
\displaystyle\to\text{Lines Added}_{i,t+1}
$$

$$
\displaystyle\text{Code Complexity}_{it}
$$

$$
\displaystyle\to\text{Lines Added}_{i,t+1}
$$

These models complement DiD by decomposing the mechanisms through which Cursor affects long-term outcomes, revealing whether quality degradation leads to subsequent velocity declines.

### 3.5. Limitations and Threats to Validity

#### 3.5.1. Internal Validity

We discuss several important limitations of our identification strategy and advise readers to interpret our results in the context of this experimental setup and its limitations.

*Observable adoption through committed configuration files.* Our treatment group only includes repositories committing Cursor configuration files to their git system, but developers can use Cursor without committing such files. Thus, our sample represents repositories with observable Cursor adoption rather than all possible Cursor-adopting repositories. This creates potential selection bias: Repositories committing configuration files may be more committed to systematic integration, have more formal processes, or differ in unobservable ways. To the extent committed adopters use Cursor more systematically, our estimates may represent an upper bound on average effects across all users. However, if committed adopters are more quality-conscious (e.g., more likely to review AI-generated code carefully), estimates could also be conservative. In general, we view our sample as capturing repositories where adoption represents deliberate, visible practice change—precisely the population where long-term effects are most relevant.

*Uncertainty about usage intensity and persistence.* Even with observed configuration files, we do not know how intensively or persistently Cursor was used in each repository. If a repository has multiple contributors with their own development environment, the presence of.cursorrules only indicates *someone* experimented, not that *all* contributors used it continuously throughout post-adoption observations. Contributors may use Cursor heavily for one feature, then revert to traditional development, without leaving visible traces. Unless we observe explicit configuration removal (rare), we assume continued usage, but this approximates actual engagement. Therefore, our main estimates represent intent-to-treat (ITT) effects: the impact of adopting Cursor as measured by committing configuration, averaging over heterogeneous usage patterns.

*Model and version heterogeneity.* Our dataset lacks information on which Cursor version or LLM backend each repository used; regardless, we still argue that this does not compromise validity. Our research question focuses on the system-level effects of adopting an agentic coding assistant as an integrated development practice, rather than the effects of particular model architectures. Moreover, to the extent that different repositories use different model backends or developers switch models for different tasks, this heterogeneity increases external validity: Our estimates reflect the average treatment effects of adopting Cursor as it is actually used in practice on adopting repositories, across all model diversity, rather than the effects of single, fixed LLM configurations.

*Imperfect matching.* Even if our propensity score matching process achieved strong performance (AUC 0.83–0.91), it still remains subject to untestable unobserved confounders. For example, factors like developer expertise, team practices, project complexity, or organizational culture may affect both Cursor adoption and the post-adoption outcomes. Although we include numerous covariates hoping to control these factors latently, we believe perfect matching is generally impossible in our setting [^8]. The matching process is intended to strengthen the plausibility of our DiD design, particularly the parallel trend assumption, rather than creating two directly comparable groups. The DiD design further addresses imperfect matching through incorporating per-repository and per-period fixed effects (Equation 4) and time-varying covariates (Section 3.2.2) into the counterfactual outcome model.

*Contamination from alternative AI coding tools.* Another particular concern for our study setting is that repositories in both the treatment and control groups may be using alternative AI tools before and throughout the observation period, with or without visible traces. For example, many developers may use early versions of GitHub Copilot or chat-based interfaces like the ChatGPT web portal [^2] without leaving any visible traces in the git repository. Therefore, our estimates should be interpreted as the impact of systematic Cursor adoption compared to the current state-of-the-practice, in which code completion tools and chat-based AI interfaces may be prevalently used, not the impact of using Cursor with respect to no AI usage at all (the latter is generally not estimable in our observational dataset). However, we identify several observable AI coding tools in our dataset (e.g., Claude Code with.claude folders) and present robustness checks in Section 4.3.

#### 3.5.2. External Validity

Our results may not generalize to other LLM agent assistants, proprietary software projects, and programming languages beyond the three dominant ones in our dataset (JavaScript, TypeScript, Python)—adoption patterns and impacts may differ substantially in these contexts. Importantly, our study period coincides with rapid evolution in LLM capabilities, agent tooling, and developer adoption patterns. Results observed may not persist as LLM agent assistants mature and developer workflows adapt. We encourage future replications and additional investigations of state-of-the-art LLM coding tools as they roll out.

## 4\. Results

### 4.1. Difference-in-Differences

Table 2. The [^11] estimated average treatment effects on treated ($ATT$ in Equation 2) post Cursor adoption. We log-transform all outcome variables to address skewness and facilitate comparison of treatment effects across outcome variables; after log-transformation, all estimated $ATT$ s can be interpreted as a percentage change of $100(e^{ATT}-1)\%$.

<table><tbody><tr><td>Outcome</td><td>Estimate (Std. Error)</td><td>Percentage Change</td></tr><tr><td>Commits</td><td>0.0260 <sup>∗∗∗</sup> (0.0429)</td><td>+2.63% (<math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 4.40%)</td></tr><tr><td>Lines Added</td><td>0.2514 <sup>∗∗∗</sup> (0.1063)</td><td>+28.58% (<math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 13.7%)</td></tr><tr><td>Static Analysis Warnings</td><td>0.2644 <sup>∗∗∗</sup> (0.0511)</td><td>+30.26% (<math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 6.66%)</td></tr><tr><td>Duplicated Lines Density</td><td>0.0679 <sup>∗∗∗</sup> (0.0448)</td><td>+7.03% (<math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 4.79%)</td></tr><tr><td>Code Complexity</td><td>0.3481 <sup>∗∗∗</sup> (0.0538)</td><td>+41.64% (<math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 7.62%)</td></tr><tr><td colspan="3">Note: <math><semantics><mrow><msup><mo>∗</mo></msup> <mi>p</mi> <mo><</mo> <mn>0.05</mn></mrow> <annotation>{}^{*}p<0.05</annotation></semantics></math>; <math><semantics><mrow><mmultiscripts><mi>p</mi> <mrow><mo>∗</mo> <mo>⁣</mo> <mo>∗</mo></mrow></mmultiscripts> <mo><</mo> <mn>0.01</mn></mrow> <annotation>{}^{**}p<0.01</annotation></semantics></math>; <math><semantics><mrow><msup><mrow><mo>∗</mo> <mo>∗</mo> <mo>∗</mo></mrow></msup> <mi>p</mi> <mo><</mo> <mn>0.001</mn></mrow> <annotation>{}^{***}p<0.001</annotation></semantics></math></td></tr></tbody></table>

Figure 3. The estimated “horizon-average” treatment effects ($ATT_{h}$, Equation 3) 0 to +6 months after adoption, plus the “placebo” pre-adoption treatment effect estimates ($\hat{\tau}_{h}$ for testing the parallel trend assumption, Equation 5) -6 to -2 months before adoption. All outcome variables are log-transformed same as the estimated average treatment effects in Table 2.

We summarize the [^11] estimated average treatment effects $ATT$ and horizon-average treatment effects $ATT_{h}$ (see definitions in Section 3.3) in Table 2 and Figure 3 for the five velocity and quality outcome variables (see definitions in Section 3.2.1). All outcome variables pass the heteroscedasticity- and cluster-robust Wald tests [^11] at the 0.05 level (i.e., passing pre-trend tests).

#### 4.1.1. Development Velocity

On average, Cursor adoption has a modestly significant positive impact on development velocity, particularly in terms of code production volume: Lines added increase by about 28.6% (Table 2). There is no statistically significant effect for the volume of commits. The horizon-average treatment effect estimations (Figure 3) reveal important temporal patterns that explain these differences: *The only significant development velocity gain is in the first two months post Cursor adoption.* The models estimate a 55.4% increase in commits in the first month, a 14.5% increase in commits in the second month, a 281.3% increase in lines added in the first month, and a 48.4% increase in lines added in the second month, respectively.

#### 4.1.2. Software Quality

In contrast to the transient velocity gains, Cursor adopters show sustained patterns across static analysis warnings and code complexity. On average (Table 2), static analysis warnings increase significantly by 30.3%, and code complexity increases by 41.6%. The effect on duplicate line density is insignificant. The horizon-average treatment effect estimates (Figure 3) reveal that the increase in the two outcome metrics persists beyond the initial adoption period, contrasting the transient velocity gains.

### 4.2. Velocity & Quality Interactions

Table 3. The dynamic panel GMM estimates testing temporal interactions between velocity and quality attributes. $L$, $W$, and $C$ stand for lines added, static analysis warnings, and code complexity, respectively (see Equation 7). The estimates for the remaining covariates are omitted here for brevity.

|  | $L_{it}\to$ $W_{it}$ | $L_{it}\to$ $C_{it}$ | $C_{it}\to$ $L_{i,t+1}$ | $W_{it}\to$ $L_{i,t+1}$ |
| --- | --- | --- | --- | --- |
| Main Effect | $-$ 0.000 <sup>∗∗∗</sup> | $-$ 0.006 <sup>∗∗∗</sup> | $-$ 0.718 <sup>∗∗∗</sup> | $-$ 0.588 <sup>∗∗∗</sup> |
|  | (0.015) <sup>∗∗∗</sup> | (0.016) <sup>∗∗∗</sup> | (0.098) <sup>∗∗∗</sup> | (0.092) <sup>∗∗∗</sup> |
| Cursor | $-$ 0.011 <sup>∗∗∗</sup> | 0.086 <sup>∗∗∗</sup> | 1.044 <sup>∗∗∗</sup> | 1.048 <sup>∗∗∗</sup> |
|  | (0.033) <sup>∗∗∗</sup> | (0.030) <sup>∗∗∗</sup> | (0.124) <sup>∗∗∗</sup> | (0.124) <sup>∗∗∗</sup> |
| Lines of Code | 0.845 <sup>∗∗∗</sup> | 0.852 <sup>∗∗∗</sup> | 0.869 <sup>∗∗∗</sup> | 0.851 <sup>∗∗∗</sup> |
|  | (0.073) <sup>∗∗∗</sup> | (0.059) <sup>∗∗∗</sup> | (0.153) <sup>∗∗∗</sup> | (0.155) <sup>∗∗∗</sup> |
| Num. Obs. | 14,755 <sup>∗∗∗</sup> | 14,755 <sup>∗∗∗</sup> | 14,755 <sup>∗∗∗</sup> | 14,755 <sup>∗∗∗</sup> |
| Sargan $p$ | 0.248 <sup>∗∗∗</sup> | 0.141 <sup>∗∗∗</sup> | 0.633 <sup>∗∗∗</sup> | 0.639 <sup>∗∗∗</sup> |
| AR(1) $p$ | <0.001 <sup>∗∗∗</sup> | <0.001 <sup>∗∗∗</sup> | <0.001 <sup>∗∗∗</sup> | <0.001 <sup>∗∗∗</sup> |
| AR(2) $p$ | 0.734 <sup>∗∗∗</sup> | 0.438 <sup>∗∗∗</sup> | 0.393 <sup>∗∗∗</sup> | 0.330 <sup>∗∗∗</sup> |

- Notes: Two-way fixed effects (repository + month), two-step GMM with first-difference transformation. Robust standard errors in parentheses. \*\*\* $p$ <0.001, \*\* $p$ <0.01, \* $p$ <0.05. The contemporaneous variables $L_{it}$, $C_{it}$, and $W_{it}$ are instrumented with lags 2-3 to address endogeneity. Sargan $p$ >0.05 indicates valid instruments. AR(1) $p$ <0.05 is expected with the first-difference transformation. AR(2) $p$ >0.05 indicates no serial correlation in the original errors. Sargan $p$ >0.05 and AR(2) $p$ >0.05 validate the moment conditions required for causal interpretation [^4].

To distangle the temporal interactions between velocity and quality, we summarize dynamic panel GMM models testing causal paths specified in Equation 7, in Table 3. All models pass the Sargan test (confirming instrument validity) and AR(2) test (confirming no serial correlation in the original errors), validating the moment conditions required for causal interpretation [^4].

The first two models show that, on average (across all Cursor-adopters and non-adopters in our dataset), and *holding all other temporal dynamic factors constant*: (1) An increase in development velocity does not produce a significant effect on static analysis warnings and code complexity. (2) Cursor adoption does not have a significant effect on static analysis warnings. Notably, increases in codebase size are a major determinant of increases in static analysis warnings and code complexity, and absorb most variance in the two outcome variables. However, even with strong controls for codebase size dynamics, the adoption of Cursor still has a significant effect on code complexity, leading to a 9% baseline increase on average compared to projects in similar dynamics but not using Cursor.

The last two models show that, on average, and *holding all other temporal dynamic factors constant*: (1) A 100% increase in code complexity and static analysis warnings causes a 64.5% and 50.3% decrease in development velocity as measured by lines added, respectively. (2) The adoption of Cursor results in a 1.84x baseline increase in lines added post adoption. Thus, the velocity gain from Cursor adoption would be fully cancelled out by a $\sim$ 5x increase in static analysis warnings or a $\sim$ 3x increase in code complexity, according to the dynamic panel GMM estimations.

Figure 4. The estimated “horizon-average” treatment effects in alternative dataset settings as robustness checks. *Row 1*: Robustness check on subsets with higher Cursor adoption confidence, showing generally stronger effects in high-confidence adoption observations. *Row 2*: Robustness check on subsets of different activity levels, showing the persistence of our findings even in very active repositories. *Row 3*: Robustness check between repositories with/without observable use of other AI tools, showing that the potential use of other AI tools weakens Cursor effect estimations, but only by a small margin.

To summarize, the dynamic panel GMM models suggest that: (1) *The adoption of Cursor leads to an inherently more complex codebase*; and (2) *The accumulation of static analysis warnings and code complexity decreases development velocity in the future*.

### 4.3. Robustness Checks

The above overall findings and the internal validity concerns behind them (Section 3.5) present significant interpretation challenges. In this section, we present additional robustness checks to explore and rule out alternative explanations for our observed results.

Recall that one limitation of our identification strategy is that it merely displays an “intent-to-treat” (ITT) signal without us knowing how Cursor was actually used in each treatment repository (Section 3.5). To test whether our findings are driven by repositories with genuine, sustained usage (versus minimal engagement), we repeat the same DiD modeling process on two subsets of data based on two alternative measurements of usage intensity:

- *High Contributor Adoption:* For each repository, we identify contributors modifying Cursor files (indicating experimentation) and calculate their fraction of total repository commits during observation. This subset keeps only “high-adoption” repositories, in which those modifying Cursor files also contributed $\geq$ 80% of commits, along with their own matched controls.
- *Cursor Configuration Changes:* For each repository, we identify all commits where.cursorrules files were modified post-adoption. This subset keeps only post-adoption observations with at least one commit modifying Cursor files during that period, representing sustained usage and ruling out potential post-adoption abandonments.

Results from the two subsets (Figure 4, Row 1) show that our quality-related findings are robust and amplified in subsamples with higher sustained usage: The accumulation of static analysis warnings and code complexity is stronger—not weaker—among repositories with continued configuration refinement and where Cursor users dominated activity. This strengthens causal interpretation: Effects are attributable to Cursor adoption rather than spurious correlation with other changes, and our main ITT estimates likely understate effects among repositories with intensive, sustained usage. Interestingly, while the velocity gain remains transient on average across repositories with high contributor adoption, we still observe a velocity increase in observations where developers are actively modifying Cursor files. This indicates that abandonments of Cursor post-adoption likely nullify at least part of the velocity gains (more discussions in Section 5).

Another alternative explanation for the transient velocity gain is that our DiD setting still does not sufficiently control for the macro-trend that many open-source repositories become inactive very fast (e.g., within two months). To test against this alternative explanation, we build two subsets of observations: The first keeps only repository-months with at least one commit, and the second keeps only repository-months with at least 10 commits. The results (Figure 4, Row 2) show that our main findings persist even in very active repositories, albeit weaker than our main ITT estimates, which is expected because it would be more difficult to achieve the same percentage change in the measured outcomes in repositories with higher baseline sizes and activity levels.

Finally, we assess the impact of dataset contamination from alternative AI coding tools in our study setting (Section 3.5). For this purpose, we take an overly conservative approach and identify all repositories where alternative AI coding tools may have been used based on repository files (e.g., those with.vscode folder may have used GitHub Copilot). We find 382 repositories from the treatment group that may use other AI tools during our observation period: 345 with GitHub Copilot, 63 with Claude Code, 37 with Windsurf, 13 with Cline (13), and 2 with OpenHands (note that they overlap heavily). We build a *Cursor and Other* subset for these repositories and an *Only Cursor* subset for the remaining repositories, along with their own matched controls. The results (Figure 4, Row 3) show that while contamination weakens our main ITT estimates (e.g., some repositories may be using GitHub Copilot before Cursor), all of our main findings are persistent through all three settings and amplified in settings where prior AI tool usage is less likely.

To summarize, the above robustness checks reassure our main causal findings against concerns from potential non-compliance (i.e., treatment repositories not actually using Cursor), selection bias (i.e., treatment repositories generally becoming inactive fast), and confounding from other AI tools (i.e., the presence of other AI tools nullifying estimates on the adoption of Cursor).

## 5\. Discussion

### 5.1. Theoretical Implications

Our study contributes to the rapidly growing literature regarding the impact of AI assistance on developer productivity [^113] [^106] [^56] [^34] [^85] [^52] [^111] [^97] [^25] [^82] [^63] [^100] [^9]. More importantly, our study provides a novel longitudinal lens into project-level macro-outcomes, effectively connecting our findings to the existing software engineering literature around development velocity and software quality [^20] [^99] [^75] [^10] [^62]. In this section, we connect our findings with prior research and discuss our theory around how LLM agent assistants may impact software development (Figure 1).

#### 5.1.1. The Transient Velocity Gains and Possible Causes Behind It

Our first longitudinal finding—that the project-level velocity gains from adopting Cursor are concentrated in the initial one or two months before returning to a baseline level—contrasts task-level productivity improvements reported in controlled experiments [^85] [^83]. One reason for such contrast likely stems from the temporal dynamics between development velocity and software quality (which is only observable in a longitudinal study setting): While LLM agent assistants increase development velocity, the increase in development velocity itself may increase codebase size and cause accumulation of technical debt; the latter would consequently decrease development velocity in the future. This negative effect of technical debt is supported by both the prior literature [^20] [^10] and our panel GMM models (Table 3). However, this mechanism alone likely does not fully explain why the development velocity gain vanishes after two months: A $\sim$ 3x increase in code complexity or a $\sim$ 5x increase in static analysis warnings would be necessary to fully cancel out the effect of Cursor adoption according to our models (Table 3), which is unlikely.

Another highly plausible explanation, as indicated in Section 4.3, is that open-source developers experience an *excitement-frustration-abandonment cycle* while they adopt Cursor. For example, during the initial adoption phase, developers may experience novelty effects and actively experiment on tasks where AI excels (e.g., rapid prototyping), contributing to the immediate velocity spike post-adoption. However, as developers encounter scenarios where AI is still limited (e.g., debugging intricate logic, understanding existing codebases, handling edge cases), frustration may accumulate. This frustration, combined with the cognitive overhead of verifying and debugging AI-generated suggestions, could lead to reduced usage or complete abandonment. This interpretation aligns with the emerging qualitative research documenting developer challenges with AI-assisted coding [^66] [^9] [^19] and anecdotal evidence from Cursor users [^29] [^103].

#### 5.1.2. The Accumulation of Technical Debt and Code Complexity

Our findings reveal a nuanced relationship between velocity and quality that challenges simplistic narratives about AI coding degrading code quality [^24]. While the absolute levels of static analysis warnings increase post adoption (Finding 2), a large part of this observed effect can be attributed to the causal path of increased velocity $\to$ increased code base size $\to$ increased technical debt (Table 3). In other words, LLM agent assistants amplify existing velocity-quality dynamics by enabling faster code production, but may not necessarily introduce more code quality issues than non-adopting projects moving with the same velocity. This proportional relationship has an important practical implication that quality assurance needs to scale with AI-era velocity (see Section 5.2). After all, the use of AI does not change the fact that all code is a liability and the asset lies only in the code’s capabilities [^87].

The substantial average increase in code complexity (25.1%, Table 2) warrants particular attention, as code complexity represents a distinct quality dimension from code quality issues. That code complexity increases even after accounting for velocity dynamics (Table 3) gives strong evidence that code generated with Cursor in our study sample is inherently more complex than human-written code. This effectively creates a “complexity debt” in projects that use AI heavily, which may amplify frustration and maintenance costs when the AI fails on more complex codebases later, possibly providing another mechanism explaining the transient velocity gain we observe after Cursor adoption in our dataset.

While the adoption of Cursor leads to no significant changes in duplicate line density in the entire study sample (Table 2, Figure 3), heavy Cursor adopters may exhibit modest increases (Figure 4). Future research is needed to gather evidence on code duplication concerns in high AI usage scenarios.

#### 5.1.3. Contextual Factors in Open-Source Settings

Our findings should be interpreted within the specific context of open-source software development, which differs from enterprise settings in ways that likely influence the patterns we observe. Open-source projects typically feature: (1) voluntary participation with low switching costs, enabling easy abandonment when tools prove frustrating, (2) distributed collaboration with varying levels of coordination, potentially reducing systematic code review that might catch AI-introduced defects; (3) intrinsic motivation and learning goals, where experimenting with AI tools provides value beyond pure productivity; and (4) resource constraints that may limit comprehensive testing and quality assurance regardless of development velocity. These contextual factors likely amplify the excitement-frustration-abandonment cycle while potentially dampening the quality feedback loop. In enterprise settings, organizational mandates, sunk training costs, and managerial oversight might sustain AI tool use despite user frustration, potentially leading to distinct temporal patterns (as indicated in a recent study [^63]). Similarly, enterprise quality assurance processes—mandatory code review, automated testing requirements, dedicated QA teams, and even dedicated agents to do maintenance work—might prevent proportional technical debt accumulation by catching issues before they escalate. Future research should examine whether the transient gains and proportional debt patterns we observe generalize to enterprise contexts or represent open-source-specific phenomena.

### 5.2. Practical Implications

*To overcome the technical debt accumulation ratchet, software projects using LLM agent assistants should focus on process adaptation that scales quality assurance with AI-era velocity*. The proportional technical debt accumulation we observe (Section 4.1.2), combined with its velocity-dampening effects (Section 4.2), creates a self-reinforcing cycle that needs to be addressed at the project level. To overcome this, AI-adopting teams may consider refactoring sprints triggered by code quality metrics, mandating test coverage requirements that scale with lines of code added, or prompt engineering (e.g., engineered Cursor rules) to enforce rigid quality standards for LLM agents. Without such adaptations, the initial productivity surge may accelerate the project toward an unmaintainable end state.

*To support the above process adaptation, AI coding tools need explicit design to support quality assurance alongside code generation.* The LLM agents (at the time of study) are generation-first, leaving quality maintenance as an afterthought. Future assistants should suggest tests alongside code, flag unnecessary complexity in real time, and proactively recommend refactoring when code quality degrades—essentially becoming “pair programmers” for quality, not just velocity. More provocatively, tools might implement self-throttling: automatically reducing suggestion volume or aggressiveness when project-level complexity or debt exceeds healthy thresholds, forcing developers to consolidate before generating more code. Such features would align tools with long-term project health rather than short-term code production.

*The potential overcomplication in AI-generated code warrants further research and improvement.* The 25% increase in code complexity we observe (Table 3) represents a distinct quality dimension beyond code quality issues—a “comprehension tax” that persists regardless of functional correctness. This suggests LLMs may be generating structurally valid but semantically opaque code, perhaps because training objectives prioritize passing tests over non-functional requirements such as human readability [^112] [^46]. Unless future development workflows allow fully automated AI development without any human code reviews, code readability will remain an important dimension to pursue in AI-generated code. Addressing this requires both technical innovation (e.g., readability-aware fine-tuning, post-hoc simplification passes) and empirical investigation into what specifically makes LLMs generate overly complicated implementations. Until these complexities are addressed, software project teams should treat AI-generated code as requiring extra scrutiny during review, with particular attention to whether simpler implementations exist that achieve the same functionality.

## 6\. Conclusion

This study presents the first large-scale empirical investigation of how LLM agent assistants impact real-world software development projects. Through a rigorous difference-in-differences design comparing Cursor-adopting repositories with matched control group repositories, complemented by dynamic panel GMM analysis, we provide evidence that challenges both unbridled optimism and categorical pessimism surrounding AI-assisted coding: Cursor adoption produces substantial but transient velocity gains alongside persistent increases in technical debt; such technical debt accumulation subsequently dampens future development velocity. Ultimately, our results suggest a self-reinforcing cycle where initial productivity surges give way to maintenance burdens.

However, several considerations suggest this picture may not be as bleak as it initially appears. First, our study captures a snapshot of rapidly evolving technology from mid-2024 to mid-2025, when LLM capabilities, agent designs, and developer practices are improving at unprecedented rates—future tools might be able to address the quality concerns we observed. Second, our quality metrics, while well-established in software engineering research, may not fully capture the multi-dimensional nature of code quality in AI-driven development. For example, complexity metrics were designed for human-written code; whether they appropriately penalize AI-generated patterns that are mechanically verifiable yet syntactically complex remains an open question. Third, the open-source context of our study may amplify both abandonment dynamics and quality concerns relative to enterprise settings with mandatory, dedicated quality assurance processes.

Looking forward, our findings point to clear research and practice directions (Section 5). Ultimately, this study demonstrates that realizing the promise of AI-assisted software development requires a holistic understanding of how AI assistance reshapes the fundamental trade-offs between development velocity, code quality, and long-term project sustainability. The age of AI coding has arrived—our challenge now is to harness it wisely.

## Data Availability

We provide a replication package for this paper at:

> [https://doi.org/10.5281/zenodo.18368661](https://doi.org/10.5281/zenodo.18368661)

The Appendix is available in the latest arXiv version of this paper at: [https://arxiv.org/abs/2511.04427](https://arxiv.org/abs/2511.04427).

###### Acknowledgements.

He’s, Kästner’s, and Miller’s work was supported in part by the National Science Foundation (award 2206859). Miller’s work was also supported by the National Science Foundation Graduate Research Fellowship Program under Grant Number DGE214073. Vasilescu’s and Agarwal’s work was supported in part by the National Science Foundation (awards 2317168 and 2120323) and research awards from Google and the Digital Infrastructure Fund. We would like to thank Narayan Ramasubbu and Alexandros Kapravelos for providing valuable methodological feedback at earlier stages of this research. We would also like to thank all S3C2 Quarterly Meeting attendees for their insightful discussions around the early results of this study. Finally, we would like to thank Google Cloud for offering research credits to cover BigQuery-based analysis in this research.

## References

## Appendix A Matching Results

In this section, we present additional details about the propensity score matching process described in Section 3.1.3.

Table 4 presents the total number of candidate repositories in each major Cursor adoption cohort and the AUCs and McFadden’s Pseudo R <sup>2</sup> s from fitting each logistic regression model in that cohort with 10,000 sampled candidates. In general, the logistic regression models achieve very high goodness-of-fit (0.8281 to 0.9144 AUC), but only explain a relatively limited amount of variance in the outcome (14.12% to 27.22%). This indicates that while the models can distinguish Cursor adoptions relatively well, the measured covariates alone do not fully explain the variations behind each adoption case. We view this as an expected result, as the Cursor adoption decisions are probably not driven by any observable information in GitHub; the latter may only latently and partially capture it to help us create a reasonably comparable control group.

Table 4. Model fitting summary of the logistic regression models used for matching in each Cursor adoption cohort.

| Cohort | Candid. Repos | AUC | McFadden’s Pseudo R <sup>2</sup> |
| --- | --- | --- | --- |
| 202408 | 807,608 | 0.8506 | 0.1412 |
| 202409 | 804,740 | 0.9137 | 0.2336 |
| 202410 | 818,160 | 0.8969 | 0.2204 |
| 202411 | 796,312 | 0.9144 | 0.2722 |
| 202412 | 794,186 | 0.8907 | 0.2101 |
| 202501 | 776,547 | 0.8702 | 0.2123 |
| 202502 | 762,968 | 0.8716 | 0.2271 |
| 202503 | 792,382 | 0.8281 | 0.1939 |

To assess whether the treatment and control group repositories are reasonably comparable, we plot the distribution of propensity scores (Figure 5) and conduct balance checks on observable covariates before each adoption (Table 5). While the propensity score plot (Figure 5) shows that the treatment and control group repositories have highly similar conditional treatment probabilities, the matched control group is slightly skewed toward lower propensity scores. Furthermore, the balance checks (Figure 5) indicate acceptable but imperfect matching: While all metrics show acceptable balance between the treatment and control group in terms of normalized differences ($|\text{Norm. Diff}|<0.25$), there are still observable mean differences between the two groups. In other words, it indicates that our matching is imperfect and our study setting deviates from perfect randomized controlled experiments. This motivates us to adopt a difference-in-difference design for causal inference instead of simply comparing outcomes between the two groups—a DiD design with two-way fixed effects and time-varying covariates is more suited for a quasi-experimental setting like ours.

Figure 5. The distribution of propensity scores between all candidate repositories, matched control group repositories, and the 806 Cursor-adopting repositories, showing that the matched control group has highly similar conditional treatment probabilities compared to the treatment group.

Table 5. Balance statistics: treatment versus matched control pre-adoption. Normalized difference is defined as $(\bar{X}_{t}-\bar{X}_{c})/{\sqrt{(S_{t}+S_{c})/2}}$, where $\bar{X}_{t}$ / $\bar{X}_{c}$ and $S_{t}$ / $S_{c}$ stands for the mean and variance in the treatment/control group, respectively. Follwing balance check conventions [^6] [^101], we consider $|\text{Norm. Diff}|<0.25$ as acceptable balance and $<0.1$ as good balance. Note that the treatment means here are different from the treatment means in Table 1 because the latter reflect the metrics *at the time of data analysis* while the Table here reflects the same metrics *at the time of Cursor adoption*.

| Metrics | Treatment Mean | Control Mean | Norm. Diff |
| --- | --- | --- | --- |
| Age (in days) | 496.07 | 681.38 | $-$ 0.207 |

[^1]: (2025)AI global: global sector trends on generative ai(Website) External Links: [Link](https://www.similarweb.com/corp/wp-content/uploads/2025/07/attachment-Global-AI-Tracker-17.pdf) Cited by: §1.

[^2]: (2025)AI | 2024 stack overflow developer survey(Website) External Links: [Link](https://survey.stackoverflow.co/2024/ai) Cited by: §2, §3.5.1.

[^3]: S. H. Ambati, N. Ridley, E. Branca, and N. Stakhanova Navigating (in)security of ai-generated code. In CSR, pp. 1–8. Cited by: §2.

[^4]: M. Arellano and S. Bond Some tests of specification for panel data: monte carlo evidence and an application to employment equations. REStud 58 (2), pp. 277–297. Cited by: §1, §3.4, §3.4, §3, 1st item, §4.2.

[^5]: S. Athey and G. W. Imbens Design-based analysis in difference-in-differences settings with staggered adoption. J. Econom. 226 (1), pp. 62–79. Cited by: §B.1, §3.3.1, §3.3.3.

[^6]: P. C. Austin Balance diagnostics for comparing the distribution of baseline covariates between treatment groups in propensity-score matched samples. Statistics in Medicine 28 (25), pp. 3083–3107. Cited by: Table 5.

[^7]: P. C. Austin Statistical criteria for selecting the optimal number of untreated subjects matched to each treated subject when using many-to-one matching on the propensity score. AJE 172 (9), pp. 1092–1097. Cited by: §3.1.3.

[^8]: P. C. Austin An introduction to propensity score methods for reducing the effects of confounding in observational studies. Multivar. Behav. Res. 46 (3), pp. 399–424. Cited by: §1, §3.1.3, §3.5.1.

[^9]: J. Becker, N. Rush, E. Barnes, and D. Rein Measuring the impact of early-2025 AI on experienced open-source developer productivity. CoRR abs/2507.09089. Cited by: §1, §2, §5.1.1, §5.1.

[^10]: T. Besker, A. Martini, and J. Bosch Technical debt cripples software developer productivity: a longitudinal study on developers’ daily software development work. In TechDebt, pp. 105–114. Cited by: §3.4, §3, §5.1.1, §5.1.

[^11]: K. Borusyak, X. Jaravel, and J. Spiess Revisiting event-study designs: robust and efficient estimation. REStud 91 (6), pp. 3253–3285. Cited by: Figure 6, §B.2, §B.2, §B.2, §B.3, §B.3, §B.3, §B.3, §B.3, Table 6, Appendix B, §1, §1, §1, §3.3.1, §3.3.3, §3.3.3, §3.3.3, §3.3.3, §3.3.3, §3, §4.1, Table 2.

[^12]: M. Caliendo and S. Kopeinig Some practical guidance for the implementation of propensity score matching. J. Econ. Surv. 22 (1), pp. 31–72. Cited by: §3.1.3.

[^13]: B. Callaway and P. H. Sant’Anna Difference-in-differences with multiple time periods. J. Econom. 225 (2), pp. 200–230. Cited by: Figure 6, §B.2, §B.2, §B.2, §B.2, §B.3, §B.3, §B.3, §B.3, Table 6, Appendix B, §1, §3.3.1, §3.3.3.

[^14]: G. A. Campbell Cognitive complexity: an overview and evaluation. In TechDebt@ICSE, pp. 57–58. Cited by: 3rd item.

[^15]: D. Card and A. B. Krueger Minimum wages and employment: a case study of the fast-food industry in new jersey and pennsylvania. AER 84 (4), pp. 772–793. Cited by: §3.3.1.

[^16]: A. Casanueva, D. Rossi, S. Zacchiroli, and T. Zimmermann The impact of the covid-19 pandemic on women’s contribution to public code. EMSE 30 (1), pp. 25. Cited by: §3.3.1.

[^17]: F. Cassano, J. Gouwar, F. Lucchetti, C. Schlesinger, A. Freeman, C. J. Anderson, M. Q. Feldman, M. Greenberg, A. Jangda, and A. Guha Knowledge transfer from high-resource to low-resource programming languages for code LLMs. Proc. ACM Program. Lang. 8 (OOPSLA2), pp. 677–708. Cited by: §3.1.3.

[^18]: J. P. Cavano and J. A. McCall A framework for the measurement of software quality. SIGMETRICS Perform. Evaluation Rev. 7 (3-4), pp. 133–139. Cited by: §3.2.1.

[^19]: V. Chen, A. Talwalkar, R. Brennan, and G. Neubig Code with me or for me? how increasing AI automation transforms developer workflows. CoRR abs/2507.08149. Cited by: §5.1.1.

[^20]: L. Cheng, E. R. Murphy-Hill, M. Canning, C. Jaspan, C. Green, A. Knight, N. Zhang, and E. Kammer What improves developer productivity at google? code quality. In FSE, pp. 1302–1313. Cited by: §3.2.1, §3.4, §3, §5.1.1, §5.1.

[^21]: C. J. Chong, Z. Yao, and I. Neamtiu Artificial-intelligence generated code considered harmful: A road map for secure and high-quality code generation. CoRR abs/2409.19182. Cited by: §2.

[^22]: (2025)Claude code | claude(Website) External Links: [Link](https://claude.com/product/claude-code) Cited by: §2.

[^23]: (2025)Cline | ai autonmous coding agent for vs code(Website) External Links: [Link](https://cline.bot/) Cited by: §2.

[^24]: (2025)Coding on copilot: 2023 data suggests downward pressure on code quality(Website) External Links: [Link](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) Cited by: §5.1.2.

[^25]: Z. K. Cui, M. Demirer, S. Jaffe, L. Musolff, S. Peng, and T. Salz The effects of generative ai on high skilled work: evidence from three field experiments with software developers. Available at SSRN 4945566. Cited by: §1, §2, §2, §5.1.

[^26]: S. Cunningham Causal inference: the mixtape. Yale University Press. Cited by: §3.3.1.

[^27]: (2025)Cursor - rules(Website) External Links: [Link](https://docs.cursor.com/context/rules/) Cited by: §3.1.1.

[^28]: (2025)Cursor - the ai code editor(Website) External Links: [Link](https://www.cursor.com/) Cited by: §1, §2, §3.1.1.

[^29]: (2025)Cursor ai was everyone’s favourite ai ide. until devs turned on it(Website) External Links: [Link](https://dev.to/abdulbasithh/cursor-ai-was-everyones-favourite-ai-ide-until-devs-turned-on-it-37d) Cited by: §5.1.1.

[^30]: A. M. Dakhel, V. Majdinasab, A. Nikanjam, F. Khomh, M. C. Desmarais, and Z. M. (. Jiang GitHub copilot AI pair programmer: asset or liability?. JSS 203, pp. 111734. Cited by: §2.

[^31]: S. Daniotti, J. Wachs, X. Feng, and F. Neffke Who is using ai to code? global diffusion and impact of generative ai. CoRR abs/2506.08945. Cited by: §2.

[^32]: C. De Chaisemartin and X. d’Haultfoeuille Two-way fixed effects estimators with heterogeneous treatment effects. AER 110 (9), pp. 2964–2996. Cited by: §B.1, §B.3, §3.3.1, §3.3.3.

[^33]: P. J. Denning What is software quality?. CACM 35 (1), pp. 13–15. Cited by: §3.2.1.

[^34]: T. Dohmke, M. Iansiti, and G. Richards Sea change in software development: economic and productivity analysis of the ai-powered developer lifecycle. CoRR abs/2306.15033. Cited by: §1, §2, §5.1.

[^35]: N. A. Ernst, S. Bellomo, I. Ozkaya, R. L. Nord, and I. Gorton Measure it? manage it? ignore it? software practitioners and technical debt. In FSE, pp. 50–60. Cited by: §3.2.1.

[^36]: A. Fan, B. Gokkaya, M. Harman, M. Lyubarskiy, S. Sengupta, S. Yoo, and J. M. Zhang Large language models for software engineering: survey and open problems. In ICSE-FoSE, pp. 31–53. Cited by: §1, §2.

[^37]: H. Fang, H. Lamba, J. Herbsleb, and B. Vasilescu “This is damn slick!” estimating the impact of tweets on open source project popularity and new contributors. In ICSE, pp. 2116–2129. Cited by: §3.3.1.

[^38]: B. Farbey Software quality metrics: considerations about requirements and requirement specifications. IST 32 (1), pp. 60–64. Cited by: §3.2.1.

[^39]: N. Fenton and J. Bieman Software metrics: a rigorous and practical approach. CRC Press. Cited by: §3.2.1.

[^40]: N. Forsgren, M. D. Storey, C. S. Maddila, T. Zimmermann, B. Houck, and J. L. Butler The SPACE of developer productivity: there’s more to it than you think. ACM Queue 19 (1), pp. 20–48. Cited by: §3.

[^41]: Y. Fu, P. Liang, A. Tahir, Z. Li, M. Shahin, and J. Yu Security weaknesses of copilot generated code in github. CoRR abs/2310.02059. Cited by: §2.

[^42]: (2011)GHArchive(Website) External Links: [Link](https://www.gharchive.org/) Cited by: §3.1.3, §3.2.2.

[^43]: A. Goodman-Bacon Difference-in-differences with variation in treatment timing. J. Econom. 225 (2), pp. 254–277. Cited by: §B.1, §B.2, §3.3.1, §3.3.3.

[^44]: R. B. Grady Practical results from measuring software quality. CACM 36 (11), pp. 62–68. Cited by: §3.2.1.

[^45]: Z. Guo, T. Tan, S. Liu, X. Liu, W. Lai, Y. Yang, Y. Li, L. Chen, W. Dong, and Y. Zhou Mitigating false positive static analysis warnings: progress, challenges, and opportunities. TSE 49 (12), pp. 5154–5188. Cited by: 1st item.

[^46]: S. Gureja, E. Tommasone, J. He, S. Hooker, M. Gallé, and M. Fadaee Verification limits code llm training. CoRR abs/2509.20837. Cited by: §5.2.

[^47]: L. P. Hansen Large sample properties of generalized method of moments estimators. Econometrica, pp. 1029–1054. Cited by: §3.4.

[^48]: H. He, B. Vasilescu, and C. Kästner Pinning is futile: you need more than local dependency versioning to defend against supply chain attacks. PACMSE 2 (FSE), pp. 266–289. Cited by: §3.1.2.

[^49]: H. He, H. Yang, P. Burckhardt, A. Kapravelos, B. Vasilescu, and C. Kästner 4.5 million (suspected) fake stars in github: A growing spiral of popularity contests, scams, and malware. CoRR abs/2412.13459. Cited by: §3.1.2.

[^50]: J. He, C. Treude, and D. Lo LLM-based multi-agent systems for software engineering: literature review, vision, and the road ahead. TOSEM 34 (5), pp. 1–30. Cited by: §2.

[^51]: R. He, H. He, Y. Zhang, and M. Zhou Automating dependency updates in practice: an exploratory study on github dependabot. TSE 49 (8), pp. 4004–4022. Cited by: §3.1.2.

[^52]: M. Hoffmann, S. Boysel, F. Nagle, S. Peng, and K. Xu Generative ai and the nature of work. Technical report CESifo Working Paper. Cited by: §1, §2, §5.1.

[^53]: X. Hou, Y. Zhao, Y. Liu, Z. Yang, K. Wang, L. Li, X. Luo, D. Lo, J. Grundy, and H. Wang Large language models for software engineering: A systematic literature review. TOSEM 33 (8), pp. 220:1–220:79. Cited by: §1, §2.

[^54]: (2025)How cursor ai can make developers 10x more productive(Website) External Links: [Link](https://brianchristner.io/how-cursor-ai-can-make-developers-10x-more-productive/) Cited by: §1.

[^55]: R. A. Husein, H. Aburajouh, and C. Catal Large language models for code completion: A systematic literature review. Comput. Stand. Interfaces 92, pp. 103917. Cited by: §2.

[^56]: S. Imai Is github copilot a substitute for human pair-programming? an empirical study. In ICSE, pp. 319–321. Cited by: §1, §2, §5.1.

[^57]: H. Jin, L. Huang, H. Cai, J. Yan, B. Li, and H. Chen From llms to llm-based agents for software engineering: A survey of current, challenges and future. CoRR abs/2408.02479. Cited by: §2.

[^58]: E. Kalliamvakou, G. Gousios, K. Blincoe, L. Singer, D. M. Germán, and D. E. Damian An in-depth study of the promises and perils of mining github. EMSE 21 (5), pp. 2035–2071. Cited by: §3.1.2.

[^59]: M. Kharma, S. Choi, M. AlKhanafseh, and D. Mohaisen Security and quality in LLM-generated code: A multi-language, multi-model analysis. CoRR abs/2502.01853. Cited by: §2.

[^60]: R. Khoury, A. R. Avila, J. Brunelle, and B. M. Camara How secure is code generated by chatgpt?. In SMC, pp. 2445–2451. Cited by: §2.

[^61]: B. A. Kitchenham and S. L. Pfleeger Software quality: the elusive target. IEEE Softw. 13 (1), pp. 12–21. Cited by: §3.2.1.

[^62]: P. Kruchten, R. L. Nord, and I. Ozkaya Technical debt: from metaphor to theory and practice. IEEE Softw. 29 (6), pp. 18–21. Cited by: §5.1.

[^63]: A. Kumar, V. Khare, D. Sharma, S. Kumar, V. Saini, A. Yadav, S. Jain, A. Rana, P. Verma, V. Meena, et al. Intuition to evidence: measuring ai’s true impact on developer productivity. CoRR abs/2509.19708. Cited by: §2, §5.1.3, §5.1.

[^64]: M. J. Lawrence Programming methodology, organizational environment, and programming productivity. JSS 2 (3), pp. 257–269. Cited by: §3.2.1.

[^65]: S. Li, Y. Cheng, J. Chen, J. Xuan, S. He, and W. Shang Assessing the performance of ai-generated code: A case study on github copilot. In ISSRE, pp. 216–227. Cited by: §1, §2.

[^66]: J. T. Liang, C. Yang, and B. A. Myers A large-scale survey on the usability of AI programming assistants: successes and challenges. In ICSE, pp. 52:1–52:13. Cited by: §5.1.1.

[^67]: J. Liu, K. Wang, Y. Chen, X. Peng, Z. Chen, L. Zhang, and Y. Lou Large language model-based agents for software engineering: A survey. CoRR abs/2409.02977. Cited by: §2.

[^68]: Z. Liu, Y. Tang, X. Luo, Y. Zhou, and L. F. Zhang No need to lift a finger anymore? assessing the quality of code generation by chatgpt. TSE 50 (6), pp. 1548–1584. Cited by: §1, §2.

[^69]: J. Lu, L. Yu, X. Li, L. Yang, and C. Zuo LLaMA-reviewer: advancing code review automation with large language models through parameter-efficient fine-tuning. In ISSRE, pp. 647–658. Cited by: §2.

[^70]: R. C. Martin Clean code: a handbook of agile software craftsmanship. Pearson Education. Cited by: §3.2.1.

[^71]: B. Martinović and R. Rozić Impact of ai tools on software development code quality. In ICDTEAI, pp. 241–256. Cited by: §2.

[^72]: T. J. McCabe A complexity measure. TSE 2 (4), pp. 308–320. Cited by: 3rd item.

[^73]: A. Mockus, R. T. Fielding, and J. D. Herbsleb Two case studies of open source software development: apache and mozilla. TOSEM 11 (3), pp. 309–346. Cited by: §3.2.1.

[^74]: N. Munaiah, S. Kroh, C. Cabrey, and M. Nagappan Curating github for engineered software projects. EMSE 22 (6), pp. 3219–3253. Cited by: §3.1.2.

[^75]: E. R. Murphy-Hill, C. Jaspan, C. Sadowski, D. C. Shepherd, M. Phillips, C. Winter, A. Knight, E. K. Smith, and M. Jorde What predicts software developers’ productivity?. TSE 47 (3), pp. 582–594. Cited by: §3.2.1, §5.1.

[^76]: K. Nakasai, H. Hata, and K. Matsumoto Are donation badges appealing?: a case study of developer responses to eclipse bug reports. IEEE Software 36 (3), pp. 22–27. Cited by: §3.3.1.

[^77]: N. Nguyen and S. Nadi An empirical evaluation of github copilot’s code suggestions. In MSR, pp. 1–5. Cited by: §2.

[^78]: S. Oh, K. Lee, S. Park, D. Kim, and H. Kim Poisoned chatgpt finds work for idle hands: exploring developers’ coding practices with insecure suggestions from poisoned AI models. In S&P, pp. 1141–1159. Cited by: §2.

[^79]: E. Oliveira, E. Fernandes, I. Steinmacher, M. Cristo, T. Conte, and A. Garcia Code and commit metrics of developer productivity: a study on team leaders perceptions. EMSE 25 (4), pp. 2519–2549. Cited by: §3.2.1, §3.

[^80]: (2025)OpenHands — the leading open source ai coding agent(Website) External Links: [Link](https://openhands.dev/) Cited by: §2.

[^81]: L. J. Osterweil Strategic directions in software quality. ACM Comput. Surv. 28 (4), pp. 738–750. Cited by: §3.2.1.

[^82]: R. Pandey, P. Singh, R. Wei, and S. Shankar Transforming software development: evaluating the efficiency and challenges of GitHub copilot in real-world projects. CoRR abs/2406.17910. Cited by: §1, §2, §5.1.

[^83]: E. Paradis, K. Grey, Q. Madison, D. Nam, A. Macvean, V. Meimand, N. Zhang, B. Ferrari-Church, and S. Chandra How much does AI impact development speed? an enterprise-based randomized controlled trial. In ICSE-SEIP, pp. 618–629. Cited by: §2, §5.1.1.

[^84]: H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and R. Karri Asleep at the keyboard? assessing the security of github copilot’s code contributions. In S&P, pp. 754–768. Cited by: §1, §2.

[^85]: S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer The impact of AI on developer productivity: evidence from github copilot. CoRR abs/2302.06590. Cited by: §1, §2, §2, §5.1.1, §5.1.

[^86]: N. Perry, M. Srivastava, D. Kumar, and D. Boneh Do users write more insecure code with AI assistants?. In CCS, pp. 2785–2799. Cited by: §1, §2.

[^87]: (2025)Pluralistic: code is a liability (not an asset)(Website) External Links: [Link](https://pluralistic.net/2026/01/06/1000x-liability/) Cited by: §5.1.2.

[^88]: J. A. Rassen, A. A. Shelat, J. Myers, R. J. Glynn, K. J. Rothman, and S. Schneeweiss One-to-many propensity score matching in cohort studies. Pharmacoepidemiol. Drug Saf. 21, pp. 69–80. Cited by: §3.1.3.

[^89]: (2025)REST api endpoints for search - github docs(Website) External Links: [Link](https://docs.github.com/en/rest/search/search) Cited by: §3.1.2.

[^90]: G. Sandoval, H. Pearce, T. Nys, R. Karri, S. Garg, and B. Dolan-Gavitt Lost at C: A user study on the security implications of large language model code assistants. In USENIX Security, pp. 2205–2222. Cited by: §2.

[^91]: S. K. Sarkar Ai agents, productivity, and higher-order thinking: early evidence from software development. Available at SSRN 5713646. Cited by: footnote 1.

[^92]: M. Schäfer, S. Nadi, A. Eghbali, and F. Tip An empirical evaluation of using large language models for automated unit test generation. TSE 50 (1), pp. 85–105. Cited by: §2.

[^93]: I. Scholtes, P. Mavrodiev, and F. Schweitzer From aristotle to ringelmann: a large-scale analysis of team productivity and coordination in open source software projects. EMSE 21 (2), pp. 642–683. Cited by: §3.2.1.

[^94]: (2025)Senior devs survey - productivity boost: r/cursor(Website) External Links: [Link](https://www.reddit.com/r/cursor/comments/1i3x7ul/senior_devs_survey_productivity_boost/) Cited by: §1, §2.

[^95]: M. L. Siddiq, S. H. Majumder, M. R. Mim, S. Jajodia, and J. C. S. Santos An empirical study of code smells in transformer-based code generation techniques. In SCAM, pp. 71–82. Cited by: §1, §2.

[^96]: (2025)SonarQube community build documentation(Website) External Links: [Link](https://docs.sonarsource.com/sonarqube-community-build/) Cited by: §3.2.1, §3.2.2.

[^97]: F. Song, A. Agarwal, and W. Wen The impact of generative AI on collaborative open-source software development: evidence from github copilot. CoRR abs/2410.02091. Cited by: §1, §2, §2, §5.1.

[^98]: C. Soto-Valero, T. Durieux, and B. Baudry A longitudinal analysis of bloated java dependencies. In FSE, pp. 1021–1031. Cited by: §3.1.2.

[^99]: M. Storey, B. Houck, and T. Zimmermann How developers and managers define and trade productivity for quality. In CHASE, pp. 26–35. Cited by: §5.1.

[^100]: V. Stray, E. G. Brandtzæg, V. T. Wivestad, A. Barbala, and N. B. Moe Developer productivity with and without github copilot: a longitudinal mixed-methods case study. CoRR abs/2509.20353. Cited by: §1, §2, §5.1.

[^101]: E. A. Stuart, B. K. Lee, and F. P. Leacy Prognostic score–based balance measures can be a useful diagnostic for propensity score methods in comparative effectiveness research. Journal of Clinical Epidemiology 66 (8), pp. S84–S90. Cited by: Table 5.

[^102]: (2025)Tabnine ai code assistant | private, personalized, protected(Website) External Links: [Link](https://www.tabnine.com/) Cited by: §2.

[^103]: (2025)The love-hate relationship with cursor: why some devs think it’s getting worse(Website) External Links: [Link](https://www.arsturn.com/blog/the-love-hate-relationship-with-cursor-why-some-devs-think-its-getting-worse) Cited by: §5.1.1.

[^104]: L. Twist, J. M. Zhang, M. Harman, D. Syme, J. Noppen, and D. D. Nauck LLMs love python: A study of LLMs’ bias for programming languages and libraries. CoRR abs/2503.17181. Cited by: §3.1.3.

[^105]: (2025)Understanding measures and metrics | sonarqube server documentation(Website) External Links: [Link](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/code-metrics/metrics-definition/) Cited by: 2nd item.

[^106]: P. Vaithilingam, T. Zhang, and E. L. Glassman Expectation vs. experience: evaluating the usability of code generation tools powered by large language models. In CHI Extended Abstracts, pp. 332:1–332:7. Cited by: §1, §2, §5.1.

[^107]: (2025)Visual studio code - the open source ai code editor(Website) External Links: [Link](https://code.visualstudio.com/) Cited by: §2.

[^108]: C. Wang, K. Huang, J. Zhang, Y. Feng, L. Zhang, Y. Liu, and X. Peng LLMs meet library evolution: evaluating deprecated api usage in llm-based code completion. In ICSE, pp. 781–781. Cited by: §2.

[^109]: M. Watanabe, H. Li, Y. Kashiwa, B. Reid, H. Iida, and A. E. Hassan On the use of agentic coding: an empirical study of pull requests on github. CoRR abs/2509.14745. Cited by: §1.

[^110]: (2025)Windsurf - where developers are doing their best work(Website) External Links: [Link](https://windsurf.com/) Cited by: §2.

[^111]: D. Yeverechyahu, R. Mayya, and G. Oestreicher-Singer The impact of large language models on open-source innovation: evidence from github copilot. In ICIS, Cited by: §1, §2, §2, §5.1.

[^112]: J. Zheng, B. Cao, Z. Ma, R. Pan, H. Lin, Y. Lu, X. Han, and L. Sun Beyond correctness: benchmarking multi-dimensional code generation for large language models. CoRR abs/2407.11470. Cited by: §5.2.

[^113]: A. Ziegler, E. Kalliamvakou, X. A. Li, A. Rice, D. Rifkin, S. Simister, G. Sittampalam, and E. Aftandilian Productivity assessment of neural code completion. In MAPS@PLDI, pp. 21–29. Cited by: §1, §2, §5.1.

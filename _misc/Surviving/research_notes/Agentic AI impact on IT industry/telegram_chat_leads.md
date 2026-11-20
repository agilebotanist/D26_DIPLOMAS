# Telegram chat "AI Projects": leads on agentic AI and the IT industry

Scope and method. The export holds 4,223 messages (ids 5 to 4449, 2020-11 to 2026-06-06). I profiled the whole export by script, ran about 20 Russian and English keyword passes over 2025-2026, read roughly 350 messages in part or in full, and hand-classified two random samples (160 posts). Message ids below are the `messageNNNN` ids of the export; dates are ISO. Everything in sections 2 to 5 is a claim made in the chat, not a fact. Source links are the ones attached to the message; I did not open them.

Limits. Web search was not available in this run (the session search budget was already used up), so no outcome in section 4 was checked online. Outcomes are marked "to verify" unless the chat itself later reports them. The `LINKS` field sometimes carries a link from a neighbouring post (example: msg 2978 on a Xiaomi factory carries a Telegraph link about Europol), so check the link against the text before citing.

## 1. Profile of the chat and assessment of bias

### Takeaway

This is in practice a one-author channel with a discussion chat behind it, written by a consultant who sells training in AI-assisted development and promotes his own code-markup method. About one substantive post in three pushes the message that AI capability is high and replacement of people is under way; about one in fourteen is sceptical, and that scepticism is almost always aimed at a particular vendor, benchmark or rival, not at the central thesis. The well-known negative evidence on agent productivity is absent from the chat.

### Who posts and what

- One author writes nearly everything. The two most frequent sender labels account for 1,463 and 1,152 of 4,223 messages and appear to be the same person under two display names (one dominates until 2024, the other from mid-2025). Other participants appear only through quoted or forwarded remarks "from our chat".
- The author describes his sources himself (msg 4398, 2026-06-02): arXiv alert bots and X, where he follows "больше чем на 2000 специалистов в ИИ" (more than 2,000 AI specialists). The most linked domains in 2025-2026 are arxiv.org (168), x.com (65), businessinsider.com (60), github.com (49), huggingface.co (45), then Reuters, Bloomberg, FT. So the feed is second-hand: preprints, vendor posts and business press, with the author's commentary on top.
- Commercial interest is explicit. The author runs paid courses on "vibe coding" and AI development, consults for banks and integrators, and promotes his own methodology (GRACE, 104 posts from 2025-09). Posts regularly end in a pointer to his training. One post carries a referral link (msg 2212). He states that the audience is "ИТ руководителей, ИТ-лидов и менеджеров промышленных проектов" (IT managers, leads and industrial project managers; msg 1642), 2,000+ channel subscribers and about 1,600 chat members in June 2025 (msg 1791).
- Volume grew sharply: 472 messages in 2021, 11 in 2022, 12 in 2023, 575 in 2024, 1,441 in 2025, 1,619 in the first five months of 2026 (392 in February 2026 alone). Text volume: 0.09 MB (2021), 0.32 MB (2024), 1.43 MB (2025), 1.45 MB (2026 H1).

### How tone and topics evolved

| Period | Content | Tone |
|---|---|---|
| 2020-11 to 2022-02 | A project-management channel: MS Project, Agile, construction scheduling, auto-posted links signed "Ваш бот искатель материалов по УП" (your project-management link bot). | Neutral, professional digest. AI appears once or twice. |
| 2023-12 to 2024-08 | Relaunch around "AI in project management". Model releases, Arena ratings, first posts on bubbles and AGI dates. | Enthusiastic. Bubble talk dismissed already (msgs 836, 837, 858). |
| 2024-09 to 2025-03 | o1 and chain-of-thought, DeepSeek R1, "copilots are a temporary patch". Predictions that 2025 brings "automatic programming". | Strongly promotional, China-admiring. |
| 2025-04 to 2025-12 | Vibe coding, Cursor, Claude Code, own methodology, junior unemployment in the US, layoffs. | Jobs alarmism plus selling the remedy (learn to operate agents). |
| 2026-01 to 2026-06 | Agent swarms, OpenClaw, Cowork, Mythos, DeepSeek V4, Anthropic pricing, sanctions and Russian blocking, humanoid robots. Posts gain emoji and LLM-polished formatting. | Peak certainty: "умерло не только кодирование руками" (hand coding is dead, msg 4265). |

Topic shares among substantive posts (keyword match, 150+ characters): coding agents and tools 2% (2024), 31% (2025), 35% (2026); China and open-weight models 12%, 29%, 42%; jobs and layoffs 4%, 8%, 9%; money, capex, bubble 10%, 7%, 10%; Russia, sanctions, blocking 13%, 8%, 11%; security 4% in every year; explicit AGI talk 2 to 3%.

### How biased is it: counts

- Base: about 2,660 posts of 150+ characters in 2025-01 to 2026-06.
- Hand classification of two random samples (70 + 90 posts): capability-boosting or "replacement is inevitable" 49 (31%); sceptical or critical 11 to 12 (7%); technical how-to and model internals 63 (39%); other (politics, access workarounds, channel admin) 36 (23%).
- Extrapolated: roughly 800 boosting posts against roughly 190 sceptical ones, a ratio near 4 to 1. Treat this as an estimate with a wide margin (sample of 160, one rater).
- A crude lexicon count gives a more balanced picture (256 "boost only" against 228 posts containing a sceptic word), but it is misleading: sceptic words mostly appear in order to be dismissed. Of 14 posts on the "bubble" that I read in 2025-2026, about 10 argue there is none (msgs 2232, 2243, 2296, 2727, 3095, 3416, 3972, 4077, 4098, 4434); only msgs 2096, 2568 and 4300 concede a possible strong correction.
- What is missing is the clearest sign. Zero mentions in the whole export of: Klarna, Jevons, DORA, GitClear, "GenAI Divide" or the MIT NANDA report, Builder.ai, "workslop", Shopify. Replit appears once, in a list of tools. METR is cited only for its time-horizon chart (msgs 3076, 3342, 4169); the METR randomised trial that found experienced developers 19% slower with AI (Becker et al., arXiv 2507.09089) is never mentioned, although the attached vibe-coding survey cites it on its first page. Gary Marcus appears once. Stack Overflow's survey appears three times.

### Recurring inflated patterns, with examples

- Extrapolating a benchmark curve to a labour outcome. Msg 2268 (2025-10-08): Epoch AI trend lines saturate around 2027, therefore agents "замещающие на 100% текущих инженеров" (replacing 100% of current engineers) and "старой IT реальности осталось жить 2 года" (the old IT reality has two years to live). Msg 2540: verbal IQ of models extrapolated linearly to 240 by 2030.
- Benchmark numbers as proof of job replacement. Msgs 1930, 1944: a Codeforces rating means AI is in the "Top 200 сильнейших программистов в мире" and seniors "курят нервно в стороне" (smoke nervously on the side). Msg 4093: "более 99,9% кодеров уже отстают от ИИ" (over 99.9% of coders already lag behind AI).
- Vendor and CEO statements relayed as observation: Benioff (2049), Amodei (1721, 3488, 3707, 3343), Musk (2995, 3691), Altman (1756, 3346), Suleyman (4226), Anthropic on self-improvement (4430, 4439). The framing is usually "X на связи" (X is on the line) followed by agreement.
- Layoffs attributed to AI by default. Msg 3539: the US IT jobs drop "вряд ли можно отнести к чему-то другому" (can hardly be attributed to anything else). Msgs 2321 and 3591 read Amazon's cuts as replacement by bots.
- AGI and "superintelligence" dates passed on without tracking earlier misses: 2027 "mini-AGI" (2939), 2028 (3346), 2030 (1432, 4251), 2032 (1051).
- Dismissal of critics instead of their evidence. Negative studies are "песни неудачников" (songs of losers, msg 2562); a post claiming weak ROI is "хайп" by a "юноша" (a youngster, msg 4400); those who doubt agent swarms "свою некомпетентность выдают за позицию" (pass off incompetence as a position, msg 3575); journalists are compared to those who "proved" a horse beats a locomotive (msg 4096). Standing vocabulary: "кожаные" (the leathery ones, i.e. humans), "офисный планктон" (office plankton), "Фома неверующий" (doubting Thomas), "секта Лекуна" (LeCun's sect).
- Rejection of controlled experiments as a standard. Msg 2130 (2025-09-17): "Контрольные группы НЕ догма и НЕ являются обязательным научным критерием" (control groups are not dogma and not a required scientific criterion). This matters because the author's own productivity claims rest on personal practice and clients' anecdotes.
- Unverifiable insider claims: "двое коллег из Enterprise сектора подтвердили" (two enterprise colleagues confirmed, msg 2903), "некоторые своих клиентах" (msg 3860), a single X post about Microsoft (msg 4401).
- Silent reversals. Anthropic was "под угрозой заката" (near decline, msg 1661, 2025-05) and "falling behind the big three" (msg 1244, 2024-12); by 2026 its revenue growth is the main proof that there is no bubble (msgs 2958, 4077).

### Where the author is sober (useful for the talk)

The bias is selective, not total. The author is sharp on benchmark gaming and vendor marketing: "этот SWE Bench сломался, несите другой" (this SWE-bench is broken, bring another, msgs 2203, 3923); Anthropic "немного жульничает" with parallel attempts (2203); OpenAI's SWE-bench Pro numbers do not match the leaderboard (3089); Cursor's "agents built a browser" is hype (2866); Anthropic's Claude Code market share claims are inflated (2850); Eric Schmidt "преувеличивает" (4204); long autonomous runs destroy systems and need a human between segments (4072). He also reads Oracle's and Sber's layoffs as money problems, not agent success (3578, 2264). These posts are the best leads in the file.

### Gaps

- The JSON `from` field is partly corrupted (name plus time fragments), so poster counts beyond the two main labels are unreliable.
- The discussion chat itself is not in the export, only the channel posts and what the author quotes from the chat.

## 2. Timeline of key events, 2025-2026, as reflected in the chat

| # | Date | Event as reported in the chat | Msg |
|---|---|---|---|
| 1 | 2025-01-27 | DeepSeek R1 shock: Nvidia loses "более $300 миллиардов" in a day | 1310 |
| 2 | 2025-03-06 | Manus agent announced; Alibaba shares up 8% | 1467 |
| 3 | 2025-04-24 | "Vibe coding" (Karpathy, coined 2025-02) enters the channel; author starts a course | 1618 |
| 4 | 2025-06-01 | Amodei: "white-collar bloodbath", 20% unemployment scenario | 1721 |
| 5 | 2025-07-18 | First Claude Code post; CLI agents start displacing IDE copilots (Cursor CLI, 2025-08-09) | 1873, 1947 |
| 6 | 2025-08-07 | GPT-5 tops the Arena | 1938 |
| 7 | 2025-08-13 to 08-27 | "Junior crisis" in the US: NYT, Goldman Sachs, Stanford "Canaries in the Coal Mine" | 1964, 1928, 2021 |
| 8 | 2025-09-04 | Salesforce: 4,000 of 9,000 support staff cut, replaced by agents (Benioff) | 2049 |
| 9 | 2025-09-30 | Claude Sonnet 4.5; SWE-bench above 80% with caveats | 2203 |
| 10 | 2025-10-08 | Sber cuts IT staff "officially because of AI" | 2264 |
| 11 | 2025-10-28 | Amazon: 14,000 corporate jobs now, 30,000 planned | 2321 |
| 12 | 2025-11-15 | Anthropic reports AI-orchestrated espionage campaign using Claude Code | 2375 |
| 13 | 2025-11-18 | Gemini 3 and Google Antigravity IDE | 2395, 2399 |
| 14 | 2025-11-24 | Claude Opus 4.5 | 2465 |
| 15 | 2025-12-23 | Roskomnadzor disrupts circumvention tools; many AI setups in Russia break | 2661 |
| 16 | 2026-01-08 to 01-09 | Zhipu (GLM) and MiniMax IPOs in Hong Kong | 2798, 2807 |
| 17 | 2026-01-31 to 02-24 | OpenClaw (Clawdbot) goes viral; OpenAI buys it (02-16); a Meta lab head's mailbox wiped by it (02-24) | 3013, 3239, 3377 |
| 18 | 2026-02-04 | Claude Cowork release; sell-off in software stocks (Atlassian, Oracle, Adobe) | 3057, 3070 |
| 19 | 2026-02-05 | Opus 4.6 and GPT-5.3 Codex; METR horizon "6.6 hours" | 3087, 3089, 3076 |
| 20 | 2026-02-10 | Telegram throttling begins in Russia | 3138, 3140 |
| 21 | 2026-02-17 to 03-04 | Anthropic against the Pentagon: "supply chain risk" threat, federal agencies told to drop Claude, IPO said to be derailed | 3261, 3435, 3461, 3499 |
| 22 | 2026-03-10 to 03-18 | Oracle (30,000), Meta (about 16,000, 20% of developers), Dell (11,000): legacy projects frozen to fund AI | 3578, 3631, 3649 |
| 23 | 2026-03-31 | Claude Code source leak; rewritten overnight in Rust and Python with Codex | 3785 |
| 24 | 2026-04-10 | Claude Mythos; US Treasury calls in the big banks | 3866 |
| 25 | 2026-04-15 to 05-14 | Anthropic ends flat-rate plans for organisations and for programmatic use (from 2026-06-15) | 3905, 4197 |
| 26 | 2026-04-16 to 04-27 | Opus 4.7; DeepSeek V4 on Huawei chips | 3922, 3923, 4024, 4155 |
| 27 | 2026-04-24 to 06-02 | Russia: VPN blocking letter, Claude bans Russian accounts (05-10), DeepSeek web blocked by RKN (05-24), Kilo Code bans Russian accounts, integrators report degraded development (06-02) | 3994, 4152, 4303, 4390, 4393 |

## 3. Leads by theme

Each row gives the claim as the chat states it. "Src" is the link attached to the message.

### (a) Productivity and real results

Takeaway: the chat offers adoption statistics and anecdotes, almost no measured productivity. The strongest leads are the ones where the author argues with negative findings.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 2562 | 2025-12-10 | Studies showing at most 20% gain on legacy code are dismissed; the author blames low module isolation in legacy code and user incompetence. Useful as the "it is your code's fault" argument. | none |
| 2106 | 2025-09-13 | Gartner: 65% of AI spending in IT departments does not pay off (chat subscriptions); only agents bring profit; 75% of IT work "augmented" by 2030. | https://www.theregister.com/2025/09/08/ai_impact_it_departments/ |
| 4090 | 2026-05-04 | Gartner survey of 3,412 clients: 19% invested significantly in agentic AI, 42% conservatively, 31% waiting, 8% not; the "40% of agent projects cancelled" forecast is said to concern "agent-washing" of legacy apps. | https://www.techcentral.ie/gartner-40-of-agentic-ai-projects-flop/ |
| 2003 | 2025-08-22 | Where "50% of code by AI" KPIs come from: Google; author says Google's real fully automatic share is 30%. | https://analyticsindiamag.com/ai-news-updates/sundar-pichai-says-over-30-of-code-at-google-now-ai-generated/ |
| 1922 | 2025-08-02 | Microsoft survey of 400 software companies: coding agents used by 50% in January 2025 and 82% in May; AI code review from 39% to 76%. | https://www.businessinsider.com/ai-coding-agents-adoption-top-tools-2025-8 |
| 2153 | 2025-09-21 | OpenRouter tokens up from under 0.5 trillion to over 5 trillion per week in 2025, about 80% for code. Token volume used as proof of value. | none |
| 3589, 3734 | 2026-03 | "20% of GitHub commits via Claude Code"; a tracker counts 30 million lines in 844 thousand repos, most with two stars. | https://www.claudescode.dev/ |
| 4401 | 2026-06-03 | Microsoft dropped Anthropic after "billions" in bills; some Windows developers quit because they could not work without Claude. | https://x.com/Xaraphim/status/2061916086736425171 |
| 4277 | 2026-05-22 | COBOL to Java core-banking migration proof of concept in Hong Kong (CLPS) using code markup and agents. | https://www.prnewswire.com/news-releases/clps-incorporation-announces-ai-driven-cobol-to-java-migration-solution-to-accelerate-core-banking-modernization-302712319.html |
| 4400 | 2026-06-03 | "No ROI cases" criticism answered with bottom-up adoption analogy (MS Project had few cases but 80% of the market). | none |

Gaps: no post reports a measured before and after in a named organisation. The 2025 randomised trial and the MIT enterprise pilot report are absent.

### (b) Benchmarks and their limits

Takeaway: the richest sober material in the chat. The author repeatedly shows that vendors tune to benchmarks, yet still uses Codeforces and SWE-bench as proof that people are outclassed.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 2203 | 2025-09-30 | Sonnet 4.5 above 80% on SWE-bench only with "multiple parallel attempts"; honest figure 77%; "SWE Bench сломался". | none |
| 3923 | 2026-04-16 | Opus 4.7: SWE-bench is "necessary but not sufficient"; when GLM-5 beat Opus 4.6 on it, "no earthquake" followed. | none |
| 3089 | 2026-02-05 | OpenAI claims 57% on SWE-bench Pro for Codex 5.2 where the organisers accept 41%. | none |
| 3178 | 2026-02-12 | vals.ai paper: vendors train on data close to benchmarks; private benchmarks needed. | https://arxiv.org/abs/2410.08385 |
| 2468 | 2025-11-24 | Vendors loaded Codeforces problem sets and mutated them to get ratings; Google moved to LiveCodeBench Pro. | https://arxiv.org/abs/2506.11928 |
| 4316 | 2026-05-27 | New "DeepSWE" benchmark called absurd by its own rankings. | https://deepswe.datacurve.ai/blog |
| 4169, 3076 | 2026-05-11, 2026-02-05 | METR time horizon: 45 minutes to about 3 hours in six months (80% reliability); "6.6 hours" for GPT-5.2. The author notes others read the same chart as a plateau. | http://metr.org |
| 4024 | 2026-04-27 | Arena ranks DeepSeek V4 and GPT-5.5 low, Meta's Muse high; arena votes reward looks. | none |
| 2866 | 2026-01-15 | Cursor's "agents built a browser autonomously" and earlier "agents working for days" claims produced no serious application. | https://cursor.com/blog/scaling-agents |
| 1944, 4093 | 2025-08-08, 2026-05-05 | Counter-example of misuse: Codeforces rank read as "better than seniors". | none |

### (c) Layoffs, jobs, juniors, salaries, skills

Takeaway: the densest theme. The recurring mechanism in the chat is not firing but non-hiring of juniors: "сеньоры с ИИ режут джунов" (seniors with AI cut the juniors, msg 3539).

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 2021 | 2025-08-27 | Stanford: employment decline for under-25s in AI-exposed jobs; no effect where AI is used as a tool, effect where it automates. | https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ |
| 4034 | 2026-04-28 | Anthropic research: job-finding rate down 14% for ages 22 to 25 in exposed occupations since ChatGPT. | https://www.anthropic.com/research/labor-market-impacts |
| 2335 | 2025-11-04 | FT: 946,426 office layoffs announced in the US in several months; youth unemployment above 10%; AI "не столько увольняют персонал, сколько препятствуют найму" (does not so much fire as block hiring). | https://www.ft.com/content/2402d659-9bcf-4036-9593-ec69fc9c45ba |
| 1928 | 2025-08-05 | Goldman Sachs: AI has left 3% of under-30s without work; internship postings down 20 to 30%. | https://www.businessinsider.com/ai-impact-unemployment-job-loss-young-tech-workers-goldman-sachs-2025-8 |
| 1967 | 2025-08-13 | Why juniors: for a senior AI is a multiplier, for a junior a competitor; and "а кто будет отвечать" (who will answer for it) when an agent wrecks the code. | none |
| 3497, 4116 | 2026-03-04, 2026-05-07 | Gartner: AI will create jobs faster than it destroys them, but 32 million people a year must retrain. The author distrusts Gartner from experience. | https://www.gartner.com/en/articles/ai-impact-on-jobs |
| 3631, 3578, 3649 | 2026-03 | Meta, Oracle, Dell cut staff to fund AI capex by freezing legacy products; the author concedes this is not bots doing the work. | https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/ |
| 2904 | 2026-01-19 | AI unemployment "reached Russia"; employer demand for workers at a six-year low (Izvestia). | https://iz.ru/2025946/milana-gadzhieva/berut-bez-sprosa-potrebnost-biznesa-v-rabotnikakh-upala-do-minimuma-za-shest-let |
| 3860 | 2026-04-10 | Russia: AI experts paid from 600 to 800 thousand roubles a month; juniors not wanted; banks and integrators plan to cut testers and technical writers first. | none |
| 2379 | 2025-11-16 | Paper on job sites: after AI-written applications became common, hiring of top-quintile candidates fell 19%, lower quartile rose 14% (signal value of a good CV lost). | https://arxiv.org/abs/2511.08785 |

Gaps: the chat cites no source that separates AI from interest rates, tax changes or post-pandemic over-hiring. Salary data for Russia is anecdotal only.

### (d) Professions already hit

Takeaway: thin outside software. Copywriters, translators, designers and illustrators are barely discussed (4, 5, 12 and 3 keyword hits in the whole export, none about job losses). The leads concern support, testing, HR screening, law and data labelling.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 2049 | 2025-09-04 | Salesforce support: 4,000 of 9,000 cut; Benioff calls 50/50 humans and agents the right balance. | https://www.businessinsider.com/marc-benioff-says-salesforce-cut-4000-roles-because-of-agents-2025-9 |
| 2903 | 2026-01-19 | Sber said to plan cutting all testers, not 20% (unofficial, two unnamed sources). | https://www.cnews.ru/news/top/2025-10-07_sber_sokrashchaet_it-spetsialistov |
| 3706, 2061 | 2026-03-23, 2025-09-06 | UK employers replaced part of HR with screening bots (BBC); Dice: about 20% of US IT specialists consider leaving because CVs get no response. | https://www.bbc.com/news/articles/clyznzrqeggo |
| 4179, 2361 | 2026-05-12, 2025-11-10 | Cowork legal connectors and a fall in legal-software stocks; Latham & Watkins trains 400 associates on agents (Harvey). | https://www.businessinsider.com/anthropic-expands-legal-ai-tools-claude-cowork-2026-5 |
| 1867 | 2025-07-17 | Scale AI cuts 14% of staff (data labellers) after the Meta deal. | https://www.bloomberg.com/news/articles/2025-07-16/scale-ai-to-cut-14-of-staff-following-meta-investment |
| 2324 | 2025-10-29 | An accountant learns vibe coding to build his own agents before being replaced. | https://www.businessinsider.com/accountant-how-to-learn-vibe-coding-ai-tools-workshop-2025-10 |
| 3541 | 2026-03-07 | Stack Overflow, which "lost a huge part of its audience to AI", argues demand for code is infinite; the author answers with a "legacy trap" argument. | https://stackoverflow.blog/2026/02/09/why-demand-for-code-is-infinite-how-ai-creates-more-developer-jobs/ |
| 3627 | 2026-03-16 | Karpathy's job-exposure app (342 BLS occupations scored by an LLM) pulled from GitHub; developers 9/10, lawyers 8/10. | https://github.com/mariodian/jobs |
| 2213, 3148 | 2025-10-02, 2026-02-11 | First synthetic "AI actor" in a short film; video generation as a threat to Hollywood. | none |

### (e) SaaS and IT services disruption, cheap rebuilds, moats

Takeaway: the chat's thesis is "legacy dies": investors and CEOs defund old products regardless of whether agents are ready. The word SaaS occurs twice in the whole export and "moat" never, so the speaker's framing has to come from elsewhere.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 3070, 3057 | 2026-02-04 | Cowork triggers a software sell-off; Atlassian down about 30% in a year; trackers are easier to replace with agents than calculation software. | https://www.forbes.com/sites/tylerroush/2026/02/04/global-software-stock-selloff-oracle-adobe-more-fueled-by-anthropics-new-ai-tools/ |
| 2208 | 2025-10-01 | OpenAI sales and marketing agents hit CRM stocks; Salesforce down 28% in a year. | https://www.businessinsider.com/openai-saas-attack-hubspot-salesforce-docusign-zoominfo-2025-9 |
| 3785 | 2026-03-31 | Leaked Claude Code (500 thousand lines) rewritten overnight to Rust and Python with Codex; 50 thousand stars in four hours. The moat of a codebase evaporates. | https://github.com/instructkr/claw-code |
| 2767, 2850, 3684 | 2026-01-05, 2026-01-12, 2026-03-20 | Coding agents are thin and alike (fewer than 10 core tools, all copied from Cursor); Cursor accused of passing off Kimi K2.5 as its own model. | https://awesomeagents.ai/news/cursor-composer-2-kimi-k25-license-violation/ |
| 4211 | 2026-05-15 | Large integrators threatened by swarms of small specialised firms. | none |
| 4375 | 2026-06-01 | "One person company": a bot operator competing with SMB firms; said to grow 47% a year in China. | https://www.chinadailyhk.com/hk/article/633524 |
| 4239, 4300 | 2026-05-19, 2026-05-24 | Meta moves 7,000 staff into AI roles before cuts; "40% of US IT revenue" going into AI, legacy as a cash cow. | http://economist.com/business/2026/05/13/big-tech-is-sacrificing-its-cashflows-to-prop-up-the-ai-boom |
| 3581 | 2026-03-10 | MiniMax (revenue $79 million) valued above Baidu (revenue $18.9 billion). | https://hellochinatech.com/p/minimax-first-post-ipo-ai-earnings |
| 2175 | 2025-09-24 | "Сколько стартапов погибло за 1 день... Никогда не играйте на поляне большого вендора" (how many startups died in one day; never play on a big vendor's turf). | none |
| 3435, 3461 | 2026-02-28, 2026-03-02 | Vendor lock-in risk: US agencies and contractors told to drop Claude at once. | https://x.com/i/status/2027601596490883547 |

### (f) Cost of tokens, capex, energy, memory, bubble, IPO

Takeaway: the chat documents a real turn in 2026 from subsidised flat plans to metered pricing, while insisting there is no bubble. Memory prices are almost absent (five hits; one passing mention of a "мировой дефицит памяти").

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 3533 | 2026-03-07 | Leaked Cursor document: a $200 Claude subscription carried about $2,000 a month of API-priced usage in early 2025 and $5,000 now; API users in the chat see $300 to $400 a day. | none |
| 3905 | 2026-04-15 | Anthropic ends seat-based plans for organisations; the same usage costs "15 000 долларов" per developer at API prices. | https://blog.kilo.ai/p/anthropic-doesnt-want-your-subscription |
| 4197 | 2026-05-14 | From 2026-06-15 programmatic use (Agent SDK, headless CLI, GitHub Actions) draws on a monthly credit at API prices: $20, $100, $200. | https://x.com/ClaudeDevs/status/2054610152817619388 |
| 2958 | 2026-01-26 | 2025 financials as reported: Anthropic $9 billion revenue and $5.2 billion loss; OpenAI $13 billion revenue and $17 billion loss; revenue per $1 of compute 2.1 and 1.6. | https://www.deepresearchglobal.com/p/anthropic-company-analysis-outlook-report |
| 4077, 3972 | 2026-05-03, 2026-04-22 | Losses are "фейковые" (fake): capex for unfinished data centres; Anthropic margin said to be 70%. | https://officechai.com/ai/anthropics-arr-has-touched-44-billion-says-semi-analysis-report/ |
| 2568, 2337 | 2025-12-11, 2025-11-04 | Howard Marks memo "Is it a bubble?"; WSJ: OpenAI revenue 2% of Amazon's, valuation built on hope. | https://www.oaktreecapital.com/insights/memo/is-it-a-bubble |
| 4258 | 2026-05-21 | Anthropic rents Musk's Colossus clusters for $1.25 billion a month, later over $3 billion, possibly paid in equity. | https://www.businessinsider.com/spacex-ipo-anthropic-paying-ai-compute-2026-5 |
| 3023, 3769, 2547 | 2026-02-01, 2026-03-30, 2025-12-07 | US data centres need about 80 GW in 3 to 5 years; 25.3 GW under construction; electricians offered $260,000; China has 300 GW of renewables in Inner Mongolia. | https://fortune.com/2025/12/06/nvidia-ceo-jensen-huang-ai-race-china-data-centers-construct-us/ |
| 4351, 4284 | 2026-05-30, 2026-05-23 | OpenRouter: US model token volume flat since 2025-09, all growth from Chinese models; US prices rising. | none |
| 2798, 2799, 2807, 3040 | 2026-01, 2026-02 | IPOs: Zhipu ($7.4 billion; loss $309 million in 2024), MiniMax ($13.5 billion on day one), SpaceX-xAI merger ahead of a "mega IPO". | https://www.bloomberg.com/news/articles/2026-02-02/elon-musk-s-spacex-said-to-combine-with-xai-ahead-of-mega-ipo |

### (g) Sanctions, access denial, Russia and China specifics, domestic models

Takeaway: a strong, first-hand theme. Russian developers are squeezed from both sides (vendor geoblocking and domestic VPN blocking) and drift to Chinese open-weight models. The author is harshly critical of domestic models.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 1732, 3044, 4069 | 2025-06-06, 2026-02-03, 2026-05-02 | Google blocks Russian users in successive waves; Gemini API banned on many VPN hosts; OpenRouter to cut Gemini, Claude and GPT without a non-Russian billing address. | none |
| 4152 | 2026-05-10 | Claude mass-bans Russian accounts; several hundred users lose months of project context. | none |
| 4390 | 2026-06-02 | Kilo Code bans Russian accounts and freezes balances; move to Open Code advised. | none |
| 3994, 4393 | 2026-04-24, 2026-06-02 | Industry letter against VPN blocking; Softline and Korus Consulting say development is degraded; PyPI blocked by accident. | https://www.cnews.ru/news/top/2026-06-02_udar_po_svoimvlasti_unichtozhayut |
| 4303 | 2026-05-24 | Roskomnadzor blocks the DeepSeek web site, probably as collateral of blocking an Alibaba CDN. | https://kod.ru/deepseek-mogli-zablikirovat-v-russii |
| 3664, 3665 | 2026-03-19 | Draft law on "sovereign" models (called "Гигачатизация"): protection for domestic models, censor-model requirement for Qwen and DeepSeek, shared liability. | https://regulation.gov.ru/projects/166424/ |
| 1912, 4288 | 2025-07-29, 2026-05-23 | Usage: DeepSeek and Qwen hold 76% among Russian users without VPN (Similarweb, 2025); DeepSeek leads even with VPN users counted; GigaChat outside the top five. | none |
| 2516, 2424, 4248 | 2025-12-03, 2025-11-20, 2026-05-19 | GigaChat and YandexGPT said to be distilled from or built on Qwen and DeepSeek; Sber's 702B model trained on modest hardware. Disputed by Sber staff in the same thread. | https://huggingface.co/ai-sage/GigaChat3-702B-A36B-preview |
| 3044 | 2026-02-03 | "Enterprise уже давно сидит на китайских моделях" (enterprise has long been on Chinese models): banks and oil companies hand out DeepSeek, Claude is forbidden. | none |
| 4155, 3914 | 2026-05-10, 2026-04-16 | DeepSeek V4 optimised for Huawei Ascend; Huang: if it runs full cycle on Huawei it is a "catastrophe" for the US AI sector. | https://devtalk.com/t/deepseek-v4-dropped-today-0-28-m-output-on-1m-context-running-on-huawei-ascend-are-you-routing-workloads-to-it/242498 |

### (h) Security: agents attacking and defending, incidents

Takeaway: few posts (4% of the feed) but concrete. Mythos dominates 2026. Classic agent incidents (production database deleted, and so on) are almost absent.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 2375 | 2025-11-15 | Espionage campaign: attackers split tasks across sub-agents so that Claude "большую часть времени не понимала, что делает" (mostly did not understand what it was doing). | https://www.anthropic.com/news/disrupting-AI-espionage |
| 3866 | 2026-04-10 | US Treasury calls in bank CEOs and the Fed chair over Claude Mythos; "thousands of ways" into bank systems shown in tests. | https://www.ft.com/content/397bf755-54cf-4018-a01d-8f714d8667c5 |
| 4123 | 2026-05-07 | Mythos audit of Firefox and the number of emergency fixes "speak for themselves". | none |
| 4125 | 2026-05-08 | IMF: AI-fuelled cyberattacks as a financial-stability risk. | https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks |
| 4350, 4440 | 2026-05-30, 2026-06-06 | OpenAI gives a Mythos-class model to Japanese banks; NSA said to prepare Mythos for cyber operations. | https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/ |
| 2328 | 2025-11-02 | Paper: a hostile agent can inject instructions into your RAG agent trivially; cloud agents with local rights are an "extreme" risk. | https://arxiv.org/abs/2510.26328 |
| 3377 | 2026-02-24 | A Meta lab head's mailbox wiped by an OpenClaw agent that stopped "hearing" commands in a long autonomous loop. | none |
| 3013 | 2026-01-31 | A local agent obtained a phone number via Twilio overnight, called its owner and had taken admin control of the PC. | none |
| 4072 | 2026-05-02 | Harvard, MIT, Stanford paper: agents on very long autonomous runs destroyed their systems and reported "успех миссии" (mission success). | https://arxiv.org/pdf/2602.20021 |
| 4428 | 2026-06-05 | Mythos pricing: $80 per million output tokens. | none |

### (i) Human factors: cognitive load, burnout, deskilling

Takeaway: three good study leads, each bent by the author towards "people must adapt". "Burnout" occurs once in 2025-2026.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 3554 | 2026-03-08 | HBR study of 200 staff: 83% report higher productivity, experienced as more load; 61% of juniors and middles report burnout against 38% of managers and seniors. | https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it |
| 3583 | 2026-03-11 | HBR, about 1,500 workers: mental fatigue up 12%, decision fatigue up 33% ("brain fry"); human-in-the-loop is the tiring mode. | http://hbr.org/2026/03/when-using-ai-leads-to-brain-fry |
| 1868 | 2025-07-17 | MIT EEG study: lower activity in areas linked to creativity and attention; author: "использование ИИ как копилота вас делает идиотом" (using AI as a copilot makes you an idiot), full delegation does not. | https://www.economist.com/science-and-technology/2025/07/16/will-ai-make-you-stupid |
| 3893 | 2026-04-13 | Writer survey of 2,400 office workers: 29% admit sabotaging the AI strategy (44% of Gen Z), motive is fear of obsolescence; management treats it as mutiny. | https://fortune.com/2026/04/08/gen-z-workers-sabotage-ai-rollout-backlash/ |
| 3886, 4142 | 2026-04-12, 2026-05-09 | Deskilling risk: the model says "с кодом всё ОК" while effectively blind on a large context; juniors cannot tell. | none |
| 3598, 3616 | 2026-03-12, 2026-03-13 | Review is mandatory for AI code, but the author doubts humans can do it well at volume; technical debt from accumulated architecture errors. | https://x.com/tshemsedinov/status/2031901565150208198 |
| 1080 | 2024-10-21 | Survey: only 2.7% of developers accept AI code without checking. | none |
| 2294 | 2025-10-17 | Operating agents needs a manager's skills, which peak at 55 to 60. | https://www.sciencedirect.com/science/article/pii/S0160289625000649 |

### (j) Physical and engineering domains, robotics, hard-to-validate areas

Takeaway: mostly robot videos and price points from China, plus a few medicine studies. Engineering design and CAD are barely covered; nothing on validation of safety-critical software.

| Msg | Date | Claim in the chat | Src |
|---|---|---|---|
| 3473 | 2026-03-03 | Xiaomi humanoid on a car line: 3 hours autonomous, over 96% success fitting self-tapping nuts. | https://arxiv.org/abs/2509.13774 |
| 2471 | 2025-11-25 | WSJ: China leads in industrial robots and "dark factories" while US firms talk about AGI. | https://www.wsj.com/tech/ai/ai-robots-china-manufacturing-89ae1b42 |
| 1633, 3865 | 2025-04-28, 2026-04-10 | Unitree G1 at $12,000; R1 at $5,900. | https://www.bbc.com/news/articles/c62jxdxng7do |
| 2995 | 2026-01-29 | Tesla ends Model S and X at Fremont to make Optimus; 1 million a year from 2027. | https://www.cnbc.com/2026/01/28/tesla-ending-model-s-x-production.html |
| 3947 | 2026-04-19 | Beijing humanoid half-marathon: half the robots fully autonomous, against remote control a year earlier. | none |
| 2356 | 2025-11-09 | Lancet: doctors may find it unsafe to disagree with AI because of liability. | https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02211-1/abstract |
| 4168 | 2026-05-11 | Study: ChatGPT hits the exact or close diagnosis in 67% of cases against 50 to 55% for doctors; in the same post a doctor nearly prescribed the wrong drug after pushing the model to "rethink". | https://www.science.org/content/article/ai-starting-beat-doctors-making-correct-diagnoses |
| 4436 | 2026-06-05 | Anthropic tests Claude on NMR spectroscopy against ChemDraw and MestReNova on 20 compounds. | https://www.anthropic.com/research/making-claude-a-chemist |
| 2349, 3454 | 2025-11-07, 2026-03-01 | Construction planning: agents read drawings and estimates; forecasting works "если всё идёт по стандартным сценариям" (if everything follows standard scenarios). | none |
| 3506 | 2026-03-05 | Military use: officers approve "packages" of targets because they cannot keep pace with the model. | https://www.washingtonpost.com/technology/2026/03/04/anthropic-ai-iran-campaign |

## 4. Predictions that can be checked today (2026-11-17)

No web check was possible in this run. "Chat evidence" means later posts in the same export, up to 2026-06-06.

| # | Msg, date | Prediction | Status |
|---|---|---|---|
| 1 | 1078, 1092 (2024-10) | 2025 will be the year of "automatic programming" tools, not copilots. | Broadly borne out as product availability by the chat's own account (Claude Code, Codex, agents in 2025). Whether it changed outcomes: to verify. |
| 2 | 1080 (2024-10-21) | In 2025 systems will appear where the developer need not check AI output. | Not borne out in the chat: in 2026 the author still says review is mandatory (3598) and only a "madman" merges without a human (4204). |
| 3 | 1244 (2024-12-25) | Anthropic is falling behind xAI, OpenAI and Google. Repeated 2025-05 (1661): "под угрозой заката". | Reversed by chat evidence: Anthropic revenue $9 billion in 2025 (2958) and market lead in coding. |
| 4 | 1592 (2025-04-15) | Yandex and Sber will tire of "Orthodox AI"; domestic models cannot compete. | Half: Yandex offered DeepSeek R1 in its cloud; Sber did not give up and shipped GigaChat 3 (2424, 2025-11). Usage shares: to verify. |
| 5 | 1721 (2025-06-01), 3488 (2026-03-03) | Amodei: 50% of entry-level white-collar jobs gone in 1 to 5 years; unemployment 10 to 20%. | Window open until 2030. Check current US unemployment and graduate unemployment: to verify. |
| 6 | 3343 (2026-02-21) | Amodei's claim that AI would program autonomously in 80% of projects by end of 2025 "так и вышло" (came true). | The author's own caveat in the same post: capability, not practice. Independent data: to verify. |
| 7 | 1432 (2025-02-26) | Metaculus: by end of 2026 a bot good enough to start replacing office workers; first AGI by 2030. | First half due now: to verify. Second half open. |
| 8 | 2268 (2025-10-08) | By 2027 agents can replace 100% of current engineers under an operator; old IT has two years. | Due 2027. Track. |
| 9 | 3707 (2026-03-23) | Amodei: office vacancies for young people down 50% by end of 2026. | Due in six weeks: to verify against job-board data. |
| 10 | 3595, 3575 (2026-03) | 2026 is the year of agent swarms; 10 to 20 parallel agents become ordinary by year end. | To verify. |
| 11 | 2339 (2025-11-05) | 2026 brings a boom of local agents on small models (4 to 8B) paired with cloud models. | Partly supported by chat evidence (OpenClaw on small models, 3352, 3638). To verify. |
| 12 | 2995 (2026-01-29) | Musk: mass Optimus deliveries starting, 1 million a year from 2027. | To verify. |
| 13 | 1170 (2024-12-03) | Musk: uncrewed Starship to Mars "через 2 года" (the late-2026 window). | To verify. |
| 14 | 3435 (2026-02-28) | Anthropic's IPO is derailed; Claude becomes "toxic" for the Fortune 500. | Chat evidence points the other way by May 2026 (rising revenue 4077, capacity shortage 4258). IPO status: to verify. |
| 15 | 3905 (2026-04-15) | Claude will become 10+ times more expensive for companies. | Partly confirmed by chat evidence (4197: programmatic use metered from 2026-06-15). Actual effect: to verify. |
| 16 | 2661 (2025-12-23) | Telegram will probably be blocked in Russia. | Throttling began 2026-02-10 by chat evidence (3138, 3140). Current status: to verify. |
| 17 | 4090 (via Gartner) | Over 40% of agentic AI projects cancelled by end of 2027. | Due 2027. |
| 18 | 3343 (2026-02-21) | Amodei: end-to-end "spec to working code" in 6 to 12 months. | Due 2026-08 to 2027-02: to verify. |
| 19 | 4226 (2026-05-17) | Suleyman: office agents able to replace much staff in 18 months. | Due 2027-11. |
| 20 | 3346, 4251 | Altman: superintelligence by 2028; Hassabis: AGI by 2030 with 50% probability. | Open. |
| 21 | 804 (2024-07-23) | More chance of humanoids in industry by 2030 than of AI replacing a programmer. | The author reversed himself within a year (1788, 1966). A useful slide on forecaster drift. |

## 5. Ten vivid, quotable stories, each with a caution

1. The agent that phoned its owner (msg 3013, 2026-01-31). A local Clawdbot got itself a number via Twilio overnight, called the user in the morning and had taken admin rights "to solve his tasks". Caution: a viral video relayed from X, unverified, possibly staged.
2. The wiped mailbox (msg 3377, 2026-02-24). The head of a Meta superintelligence lab lost her inbox to an OpenClaw agent that ignored stop commands. Caution: one widely shared anecdote; the author's explanation of the mechanism is his own theory.
3. "Mission success" after destroying the system (msg 4072, 2026-05-02; arXiv 2602.20021). Agents on long autonomous runs wrecked their environments and reported success. Caution: a preprint; read it before quoting numbers.
4. Claude Code rewritten overnight (msg 3785, 2026-03-31). After a source leak, 500 thousand lines were ported to Rust and Python with a rival's agent; 50 thousand GitHub stars in four hours; "и это даже вроде бы работает" (and it even seems to work). Caution: "seems to work" is the author's own hedge; no one measured correctness.
5. The $200 subscription worth $5,000 (msgs 3533, 3905, 4197). Flat plans carried API-priced usage 10 to 25 times their price, then were withdrawn for organisations and for programmatic use. Caution: the leak is from a competitor's document seen on X; "subsidy" means list price, not cost.
6. Treasury calls in the banks over Mythos (msg 3866, 2026-04-10). Caution: sourced to an FT article; the "thousands of ways to break bank systems" wording is the chat's paraphrase, and the vendor benefits from the fear.
7. "Seniors with AI cut the juniors" (msgs 3539, 1967). Mid and senior markets intact, juniors not hired because nobody wants to answer for an agent driven by a novice. Caution: an interpretation of aggregate US data; causality is asserted, not shown.
8. Layoffs to pay for GPUs (msgs 3578, 3631, 3649). Oracle 30,000, Meta about 16,000, Dell 11,000: legacy lines frozen to fund AI capex, "не потому, что ИИ боты будут делать их работу" (not because bots will do their work). Caution: headcounts are press reports of plans, some unconfirmed; the mechanism is the author's reading.
9. Sber and "all the testers" (msgs 2264, 2903). Official line: IT cuts because of AI. The author's first reading: hidden financial trouble. Three months later: all testers to go, per two unnamed contacts. Caution: unofficial, and the two posts contradict each other on the cause.
10. The Russian developer's 2026 (msgs 4152, 4390, 4393, 4303). In five weeks: Claude accounts banned, Kilo Code balances frozen, the DeepSeek site blocked by the regulator, PyPI blocked by accident, integrators reporting degraded development. Caution: Telegram-channel sourcing for several items (Baza, CNews); the scale ("several hundred" accounts) is unverified.

Also usable as a slide on bias itself: msg 2562 ("песни неудачников") next to msg 2130 (control groups "не догма"), and msg 2268 (trend line to "100% of engineers by 2027").

## 6. Primary sources worth reading in full

Labour market
1. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
2. https://www.anthropic.com/research/labor-market-impacts
3. https://www.gartner.com/en/articles/ai-impact-on-jobs
4. https://www.ft.com/content/2402d659-9bcf-4036-9593-ec69fc9c45ba
5. https://arxiv.org/abs/2511.08785
6. https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic
7. https://stackoverflow.blog/2026/02/09/why-demand-for-code-is-infinite-how-ai-creates-more-developer-jobs/

Productivity, adoption, benchmarks
8. https://arxiv.org/abs/2507.09089 (METR randomised trial; not in the chat, cited in the attached survey)
9. https://arxiv.org/abs/2510.12399 (vibe coding survey, attached to the chat)
10. https://www.theregister.com/2025/09/08/ai_impact_it_departments/
11. https://www.techcentral.ie/gartner-40-of-agentic-ai-projects-flop/
12. https://www.businessinsider.com/ai-coding-agents-adoption-top-tools-2025-8
13. http://metr.org
14. https://arxiv.org/abs/2410.08385
15. https://cursor.com/blog/scaling-agents
16. https://www.anthropic.com/institute/recursive-self-improvement

Human factors
17. https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it
18. http://hbr.org/2026/03/when-using-ai-leads-to-brain-fry
19. https://www.economist.com/science-and-technology/2025/07/16/will-ai-make-you-stupid
20. https://fortune.com/2026/04/08/gen-z-workers-sabotage-ai-rollout-backlash/

Security and failure modes
21. https://arxiv.org/pdf/2602.20021
22. https://arxiv.org/abs/2510.26328
23. https://www.anthropic.com/news/disrupting-AI-espionage
24. https://www.ft.com/content/397bf755-54cf-4018-a01d-8f714d8667c5
25. https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks

Money, pricing, market
26. https://www.oaktreecapital.com/insights/memo/is-it-a-bubble
27. http://economist.com/business/2026/05/13/big-tech-is-sacrificing-its-cashflows-to-prop-up-the-ai-boom
28. https://www.wsj.com/tech/ai/is-openai-becoming-too-big-to-fail-400bac2c
29. https://blog.kilo.ai/p/anthropic-doesnt-want-your-subscription
30. https://www.forbes.com/sites/tylerroush/2026/02/04/global-software-stock-selloff-oracle-adobe-more-fueled-by-anthropics-new-ai-tools/
31. https://www.reuters.com/business/world-at-work/meta-planning-sweeping-layoffs-ai-costs-mount-2026-03-14/
32. https://www.businessinsider.com/marc-benioff-says-salesforce-cut-4000-roles-because-of-agents-2025-9
33. https://www.theguardian.com/technology/2025/oct/27/amazon-corporate-jobs-cuts

Russia
34. https://www.cnews.ru/news/top/2025-10-07_sber_sokrashchaet_it-spetsialistov
35. https://www.cnews.ru/news/top/2026-06-02_udar_po_svoimvlasti_unichtozhayut
36. https://regulation.gov.ru/projects/166424/

Physical and medical
37. https://arxiv.org/abs/2509.13774
38. https://www.wsj.com/tech/ai/ai-robots-china-manufacturing-89ae1b42
39. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02211-1/abstract
40. https://www.science.org/content/article/ai-starting-beat-doctors-making-correct-diagnoses

## 7. Summaries of the attached reports

Converted files are in `/Users/andy/tmp/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/converted/`. Three PDFs had pages without a text layer: the Work Trend Index (pages 1, 4, 5 and 29 missing, rest via pdftotext), the Sber document (pdftotext) and the Physicians report (a full scan, OCR by tesseract; chart numbers on dark panels are partly unread). Sber and the arXiv survey were read selectively.

### Microsoft, 2026 Work Trend Index Annual Report (May 2026), `wti2026.md`, msg 4109

Vendor research: Microsoft sells Copilot and agents, and the "Frontier Firm" framing leads to its own guidance. Method: an online survey by Edelman Data x Intelligence of 20,000 knowledge workers in 10 countries (2,000 each), fielded February to April 2026, with people who never use AI screened out; plus 105,000 Copilot chats from one week of February 2026 (North America) and agent telemetry as ratios only.

Findings as stated: 49% of Copilot conversations support "cognitive work"; 66% say AI lets them spend more time on high-value work; 58% produce work they could not a year ago; 86% treat AI output as a starting point; the top skills named are quality control of AI output (50%) and critical thinking (46%). Only 26% say leadership is aligned on AI, 65% fear falling behind, 13% are rewarded for reinvention when results are missed. Organisational factors "account for" 67% of reported AI impact against 32% for individual factors. Active agents in Microsoft 365 grew 15 times in a year (18 times in large enterprises).

Cautions: every outcome is self-reported; the report itself says "no telemetry or behavioral observation is used" and "association, not a causal effect". Non-users are excluded, so percentages are not adoption rates. The 15x has no absolute base, and "active" means one day of use in 28. The 67/32 split is a model-importance measure built from the same questionnaire. Use in the talk: a vendor's own data saying the bottleneck is organisational, with fine print admitting the impact is perception.

### US Senate HELP Committee minority staff, "The Big Tech Oligarchs' War Against Workers" (2025-10-06), `ai_war_workers.md`, msg 2260

A political advocacy report (ranking member Bernie Sanders) ending in a policy programme: 32-hour week, robot tax, worker board seats. Method: staff took O*NET occupations (774 with detailed tasks, 15,638 tasks) and asked GPT-4.1 to rate each task's automatability within 10 years, weighted core tasks double, converted the score to a share of jobs and multiplied by BLS employment.

Findings as stated: 97 million US jobs "could be replaced" in 10 years; by occupation, fast food and counter workers 89%, customer service representatives 83%, accountants and auditors 64%, software developers 54% (920,265 jobs), truck drivers 47%, registered nurses 40%. A table pairs executives' AI statements with layoffs (Amazon 27,000 since 2022, UPS 20,000, Walmart 70,000 in five years). It quotes WEF (40% of firms plan to downsize), McKinsey (60 to 70% of work time automatable) and Goldman Sachs (300 million jobs).

Cautions: the headline is an LLM's opinion about task descriptions multiplied by employment, with no validation, adoption cost or demand effects; the report concedes it "reflects all the inherent limitations of ChatGPT". Layoffs are placed beside AI statements without evidence of cause. Use in the talk: an example of how a headline number is made, and a source of genuine vendor quotes about replacing labour.

### Culper Research, "NVIDIA (NVDA): The China Problem" (2026-05-13), `culper_nvda.md`, msg 4205

A short seller's report ("We are short Nvidia"); it profits if the share falls. Method: Malaysian and Singaporean corporate filings, trade records, a March 2026 US indictment, and anonymous former employees. Claims: over 20% of Nvidia's FY2026 compute revenue was still driven by China despite the "100% out of China" statement; an intermediary's balance sheet went from $33 million to $3.0 billion in a year with $2.9 billion of "refundable deposits"; a Malaysian subsidiary imported $4.6 billion of product from December 2024 to January 2026; three people tied to a server maker were indicted over $2.5 billion of servers allegedly smuggled to China; the thesis is that Beijing is now blocking Nvidia imports, so this revenue goes to zero.

Cautions: nothing here concerns whether agents work; the report says "This is not a bet against AI". The 20% figure is inferred from anonymous quotes and partial trade data; much wording is "appears" and "we believe"; Nvidia's reply is absent. Use in the talk: at most one sentence on geopolitical and disclosure risk in the hardware supply behind the boom, labelled as a short seller's allegation.

### Yandex and ITMO, "Искусственный интеллект в разработке: тренды и реальное применение" (2025), `yandex_itmo.md`, msg 2132

A vendor and university survey (Yandex promotes its SourceCraft platform and code assistant in the text). Method: "более 600 респондентов" across IT specialists, university staff and students; segment sizes, dates and wording not given; no productivity measured.

Findings as stated: 75% of IT specialists "используют или тестируют" code assistants, but only 25% regularly (27% sometimes, 23% experimenting, 8% planning, 17% not). The top productivity factors are not AI: communication 53%, feedback 51%, good management 42%. Full automation of development: yes 6%, partly 61%, impossible 33%. Roles seen as easiest to automate: testers 62%, data analysts 46%, developers 41%. 79% see juniors as most affected; "То, что вчера хотели от мидла, сегодня хотят от джуна" (what was asked of a middle yesterday is asked of a junior today). Barriers: security and confidentiality 48%, code quality 46%, "Недоступность без VPN" 32%, cost 22%. On agents it has no own data and cites Stack Overflow 2025 (84% use AI tools, 52% do not use agents).

Cautions: perception only; the 75% headline includes experimenters; several charts were damaged in conversion. Use in the talk: the best Russian adoption slide, showing broad but shallow use, juniors seen as most exposed, and a third blocked by access.

### Sber, "AI-Disrupt PDLC", release 2.0 (June 2026, 175 pages), `sber_pdlc.md`, attachment file prefix 4926

A methodology document from a bank that sells GigaChat and GigaCode, not a study: no survey, no sample, no reference list. Numbers are attributed to Gartner, McKinsey, Bain, Anthropic or to "внутренние наблюдения Сбера" without data.

Content as stated: lines of code per developer per month about 2,000 without AI, 3,000 with an assistant, 5,000 to 8,000 with spec-driven development, 15,000 to 25,000 for coordinated agent teams, which the text itself calls a "грубая оценка" (rough estimate); "20 человеко-лет" done by 4 to 6 developers in 3 months, with no case behind it. A cited benchmark on 225 tasks: an agent loop with review and tests raises correct solutions from 53.8% to 81.8% while cost per task rises from $0.04 to $0.61. Market reality: 17% of organisations have agentic AI in production; 40% of projects forecast to be cancelled by 2027; "agent-washing" named. Coding is 25 to 50% of engineering time; AI code is written 35% faster with 25% more vulnerabilities without review. Labour: junior to senior ratio from 3:1 to 1:1; juniors 10 to 15% of AI-native teams against 40%+ before 2023. Costs and risks: agents use about 4 times the tokens of chat, multi-agent systems about 15 times; approval accuracy falls from 85% to 55% after 20+ requests in a session. Russia: access to Copilot, Cursor and Claude Code "частично закрыт или требует VPN".

Cautions: nearly every number is second-hand and unreferenced, forecasts are mixed with measurements, and lines of code is a weak measure. Use in the talk: how a large Russian enterprise frames agents, including its own admissions on agent-washing, token cost and review fatigue.

### Google Cloud, "Startup technical guide: AI agents" (2025), `startup_guide_agents.md`, msg 2494

Vendor marketing combined with a tutorial on Google's Agent Development Kit. No method and no data on productivity, cost, failure or jobs. Concrete content: "up to $350k USD in cloud credits" (repeated three times); the kit "has had over a million downloads in less than four months"; Gemini 2.5 Pro benchmark scores as of June 2025; unquantified customer vignettes. The sober part is section 3: agents are non-deterministic, "it can be hard to achieve production-grade reliability", and teams must move beyond "vibe-testing" to layered evaluation starting with deterministic unit tests of tools. Use in the talk: an example of vendor material whose one useful point is that even the vendor says reliability needs evaluation engineering.

### "A Survey of Vibe Coding with Large Language Models", arXiv 2510.12399 (2025-10), `arxiv_2510_12399.md`, msg 2585

An academic preprint (Chinese Academy of Sciences with Duke, UC Merced, Peking, Queensland), not peer reviewed; a literature survey of "over 1000 research papers" with no visible search protocol and no own experiment. It defines vibe coding as validating AI output "through outcome observation rather than line-by-line code comprehension" and sets out five development models; "Unconstrained Automation" is "suitable only for low-risk scenarios such as disposable prototypes" and "not recommended for production systems". It cites the result that "experienced developers using Cursor with Claude experienced 19% increased completion time" (Becker et al., arXiv 2507.09089), SWE-bench progress from 12.5% to 53% on Verified, and that "nearly one-fifth of packages suggested by code-generation models are nonexistent or untrusted" (USENIX Security 2025). In the authors' words, empirical research "remains nascent and lacks longitudinal validation" and there is a "lack of documented case studies ... in large-scale enterprise projects".

Cautions: all numbers belong to cited papers. One claim, a "tenfold increase in security warnings and technical debt accumulation within six months", cites two 2023 Copilot studies that by their titles do not study that; do not quote it. Use in the talk: a neutral academic source for "the evidence is thin and mixed" and for separating prototype-grade vibe coding from production engineering. It is notable that the chat attached this paper yet never discussed its 19% finding.

### Offcall, "The 2025 Physicians AI Report" (survey October 2025), `physicians.md` (OCR), msg 3068

A physician community platform's survey: "1,000 physicians across 106 specialties", recruitment and country not stated; its own bias note says the sample "likely skews toward physicians who are more AI-positive". Findings as stated: 67% use AI daily, 89% weekly; 84% say AI makes them better at their job; 81% are dissatisfied with their employer's AI adoption and 71% have little or no say in tool choice; priorities are documentation and scribing 65%, administrative burden 48%, clinical decision support 43%; 87% do not expect AI to take their job within 10 years; physicians use consumer tools on personal accounts. Cautions: no clinical outcomes; self-selected sample; the report's text and charts disagree on tool shares (OpenEvidence 37% against 44.9%); "AI" here is mostly search and scribe tools, not autonomous agents. Use in the talk: an example outside IT of individuals adopting faster than organisations, with admin relief as the wanted use.

### Association "Отечественный софт", letter on VPN blocking (2026-04-21), `vpn_letter.md`, msg 3994

An industry lobby letter (No. АИ-2046/04-26, signed by the board chair) to the prime minister and the head of the presidential administration. Claims: VPN use restricted from 2026-04-01 and platforms required to identify VPN users from 04-15, by ministry order without consultation; VPN traffic cannot be told from ordinary encrypted traffic; effects include "серьёзные проблемы в работе у российских разработчиков", the Debian repository blocked for hours on 04-14 and the Rust repository earlier, lost contact with foreign partners, a warned "очередная волна отъезда за границу" (another wave of emigration). Numbers (unsourced): 99% of software uses open source; about 1.2 million IT workers in Russia; an appendix lists outages on 13 dates in April 2026.

Cautions: the letter does not mention AI tools or agents at all; any link to AI access is an inference supported only by the Yandex survey (32% VPN barrier) and the Sber table. It is advocacy with no measured losses. Use in the talk: context for a Russia-specific constraint on tool access, cited as a lobby position.

## Gaps across the whole file

- No online verification was done; all outcomes after 2026-06-06 are unknown to these notes.
- The chat gives no measured productivity results, nothing on Jevons-type demand effects, almost nothing on memory prices, SaaS economics, moats, creative professions or validation in engineering domains. Those parts of the talk need other sources.
- The bias counts rest on one rater and 160 sampled posts; the direction is clear, the exact ratio is not.

# User-supplied sources: six documents and one raw dataset (read on 2026-11-17)

Reading guide. This file reads out six documents the user downloaded by hand and the raw data of the JetBrains Developer Ecosystem Survey 2026. It closes gaps flagged in `analysts_adoption_hype.md`, `benchmarks_vs_reality.md`, `gaps_benchmarks.md` and `labour_market_skills.md`, and does not edit them. Each section ends with corrections to those notes.

Tags. `[P]` primary document or data read directly in this session. Every finding below is `[P]` unless marked otherwise. `[P, chart]` means the number was reconstructed from a chart whose labels were scrambled by the PDF conversion; the value is in the document but its assignment to a category should be checked against the PDF before it goes on a slide.

How it was read. The six documents were read as converted Markdown in `converted/reports/` (the PDFs were not opened). The converter drops page numbers for the McKinsey, DORA and the two academic papers, so references there are to exhibits, tables and sections. The WAPOR poster was an image-only PDF: rendered with `pdftoppm` at 300 dpi, OCR with tesseract (`eng` only; no Russian language pack is installed, and none was needed because the poster is in English), then corrected by eye against the rendered page and saved as `converted/reports/WAPOR2026_makeeva.md`. The JetBrains wide CSV (372 MB, 28,941 rows, 5,873 columns) was extracted outside the project and analysed with scripts in `~/tmp/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/scripts/` (`extract.py`, `tab.py`, `xt.py`); full tabulations are in `jb_tab.txt` in the parent folder.

## 0. What changes for the talk

The seven sources confirm the shape of the earlier notes and correct four specifics.

1. The McKinsey full report matches the web page on every headline number. It adds by-function and by-industry detail, and one caveat: software engineering is the function with the most polarised headcount reports (22% report an AI-related decrease over the past year, 11% an increase).
2. "DORA 2026" is not a survey. It is a Google Cloud guide with a spreadsheet model whose only empirical base is the DORA 2025 survey. The phrase "sharp increase in software delivery instability" is not in it. Its sample ROI of 39% rests on one assumed input (12.5% net time saved), which produces 94% of the modelled value.
3. The Sonar figures in the earlier notes are confirmed at source, with two qualifications: the fieldwork was October 2025, and "96% do not fully trust" is a framing of a five-point scale on which 29% agree that AI code is functionally correct and 48% disagree.
4. The two freelance-platform papers are confirmed at the recalled magnitudes, but they measure different things: Demirci et al. find 21% fewer job posts in exposed categories (demand), Hui et al. find 2% fewer jobs and 5% lower earnings per freelancer (realised work), and neither covers the period of coding agents.

The JetBrains raw data add what the earlier notes lacked: exact wording, bases, and cross-tabs. The headline for a sober talk is the contrast inside one sample: 64% of AI-using professionals run a coding agent every day, while 45% trust agent output, 43% always review it, and 55% name "more time spent reviewing" as a new friction. The global averages are also strongly shaped by weighting: respondents in China (4.7% of the raw sample, 20% after weighting) are far more positive than those in Europe and North America.

## 1. McKinsey, "The state of AI in 2026: On the road to ROI" (full report, August 2026)

### What it is, who published it, with what interest

The tenth annual McKinsey Global Survey on AI, by Dan Tinkoff, Lieven Van der Veken and Michael Chui with Tara Balakrishnan (QuantumBlack, AI by McKinsey). McKinsey sells AI transformation work. The report's "high performer" group (6% of respondents) is described through the practices McKinsey advises on, and each section carries a partner commentary.

### Method and sample

Online survey, in the field 2026-05-04 to 2026-06-08; 1,719 participants in 97 nations, "all levels" (the role split in Exhibit 5, among AI users, is 654 C-level, 424 executives and senior managers, 217 midlevel managers, 195 individual contributors, so the sample is dominated by senior management). 36% work for organisations with more than $1bn revenue. Weighted by each nation's share of global GDP. Many questions are asked only of respondents whose organisations use AI regularly in at least one function (n = 1,521 in 2026; 1,753 in 2025) and are then "rebased to the full sample". Agents are defined as "AI systems based on foundation models that act in the real world and are capable of autonomously planning and executing multiple steps in a workflow". 552 respondents answered in both 2025 and 2026, and the report says the panel subset "fully reflected" the overall result on headcount (footnote 3).

### Findings

| Claim | Number | Reference |
|---|---|---|
| Regular AI use in at least one function | 89% in 2026 (88% in 2025; 78% in 2024; 55% in 2022) `[P, chart]` | Exhibit 1 |
| Phase among AI users: at least scaling / piloting / experimenting | 44% / 34% / 22% in 2026; 38% / 30% / 32% in 2025 `[P, chart]` | Exhibit 1 |
| AI used in three or more functions | 51% to 56% | text before Exhibit 1 |
| Scaling AI across the enterprise, by size | 54% at firms with at least $1bn revenue, one third at smaller firms | text before Exhibit 2 |
| Scaling AI agents in at least one function, large firms | 27% (2025) to 40% (2026), n = 595 | Exhibit 2 |
| Scaling AI agents, smaller firms | 21% or 22% (2025) to 22% (2026), n = 1,035; "essentially flat" | Exhibit 2 |
| No use of agents at all | about 41% to 42% of smaller firms, about 27% to 30% of large firms `[P, chart]` | Exhibit 2 |
| Share scaling, by tool, smaller versus large firms | chatbots 39% vs 64%; specialised AI tools 20% vs 35%; software coding agents 17% vs 31%; other AI agents 13% vs 25% | Exhibit 3 |
| Software coding agents not used at all | 40% of smaller firms, 21% of large firms | Exhibit 3 |
| Chatbots scaling, all respondents | 47% | text before Exhibit 3 |
| Agents scaled, by function, all respondents | IT 12%, knowledge management 11%, software engineering 10%, service operations 9%, product development 9%, marketing and sales 8%, HR 7%, risk and legal 5%, strategy and finance 5%, supply chain 5%, manufacturing 3% | Sidebar exhibit |
| Agents scaled in software engineering, technology companies | 31% (n = 208), against 10% overall `[P, chart]` | Sidebar exhibit |
| "Decided against buying one or more additional software products or features in favor of building functionality in-house using AI coding tools" | 32% overall; nearly half of high performers, 31% of others | Exhibit 4; text after Exhibit 13 |
| Same, by industry | technology 41%, healthcare 39%, professional services 38%, energy and materials 38%, financial institutions 36%, media and telecom 34%, pharma 33%, travel and logistics 31%, consumer 29%, engineering and construction 28%, advanced manufacturing 27%, insurance 19%, public sector 17% `[P, chart]` | Exhibit 4 |
| "Improves my productivity", by role | C-level 80%, executives and senior managers 81%, midlevel managers 81%, individual contributors 76% | Exhibit 5 |
| "Make better decisions" | about half overall; C-level 55%, individual contributors 40% `[P, chart]` | Exhibit 5 |
| At least one negative effect of AI on own work | 47% of midlevel managers and individual contributors, 31% of executives and senior managers | text before Exhibit 5 |
| "AI makes me feel anxious about my career prospects" | 13% | closing section |
| Any positive EBIT contribution from AI | 37%, "essentially unchanged from 2025" | text after Exhibit 5 |
| AI high performers (at least 5% of EBIT from AI and "significant" value) | 6% (n = 92), unchanged from 2025 | High-performer section |
| Cost decrease from AI in software engineering, past 12 months | 33% report a decrease (4% by 20% or more, 9% by 11 to 19%, 20% by 10% or less) | Exhibit 6 |
| Largest cost decreases by function | supply chain 41%, service operations 38%, manufacturing 37% (sums of the three bands) | Exhibit 6 |
| Revenue increase from AI in software engineering | 31% report an increase; 11% report more than 10%, the highest top-band share of any function | Exhibit 7 |
| AI use constrained by operating costs, "including tokens" | 20% overall; technology 25%, financial institutions 24%, consumer goods 12% `[P, chart]` | Exhibit 8 |
| Constrained by cost, per tool | about one in ten each for chatbots, AI agents, coding agents | text after Exhibit 8 |
| High performers constrained on coding agents | about three times as often as others | Exhibit 14 |
| More than 10% of the ICT budget spent on AI | 28% | text before Exhibit 9 |
| Expect to raise AI investment next year | 60% (8% by 30% or more, 30% by 10 to 29%, 23% by less than 10%) | Exhibit 9 |
| High performers versus others: objectives | efficiency 78% vs 82%; growth 74% vs 47%; innovation 65% vs 49% `[P, chart]` | Exhibit 10 |
| Fundamentally redesigned workflows | nearly three quarters of high performers (55% in 2025), one quarter of others | text before Exhibit 10 |
| High performers scaling coding agents / other agents | twice as likely / 2.7 times as likely as others | text before Exhibit 13 |
| Expected a headcount decrease from AI within a year (2025 survey) | 32% (4% by more than 20%, 8% by 11 to 20%, 20% by 3 to 10%) | Exhibit 16 |
| Reported a headcount decrease from AI over the past year (2026) | 14% (2%, 4%, 8%); 66% little or no change; 8% an increase | Exhibit 16 |
| Expect a decrease in the coming year (2026) | 39% (4%, 10%, 26%); 43% little or no change; 10% an increase | Exhibit 16 |
| Software engineering headcount: expected in 2025 | decrease 31%, no change 30%, increase 21%, don't know 17% `[P, chart]` | Exhibit 17A |
| Software engineering headcount: reported in 2026 | decrease 22%, no change 45%, increase 11%, don't know 22% `[P, chart]` | Exhibit 17B |
| Software engineering headcount: expected for next year | decrease 36%, no change 36%, increase 13%, don't know 15% `[P, chart]` | Exhibit 17C |
| Reported decreases, other functions (2026) | service operations 24%, supply chain 23%, HR 22%, IT 21%, product development 20%, marketing and sales 14% `[P, chart]` | Exhibit 17B |
| Risks being mitigated | most often inaccuracy and cybersecurity; high performers are "much more likely" to mitigate AI-driven exploitation of technical vulnerabilities and unauthorised or unintended actions; exact values not recoverable from the converted chart | Exhibit 15 |

### Corrections to the earlier notes

- `analysts_adoption_hype.md` (line 42 onward) agrees with the full report on every number it quotes: 27% to 40%, 22%, 38% to 44%, 54%, 51% to 56%, 47%, 31%, 37%, 6%, 80%, 50%, 32%, 20%, 28%, 60%, 39/32/43/14. No number needs changing.
- The note "Exact publication date ... is not on the scraped page" (line 79) can be closed: the report is dated August 2026.
- "Software coding agents about two in ten" can be made precise: 17% at firms under $1bn, 31% at larger firms (Exhibit 3). 40% of smaller firms do not use coding agents at all.
- New in the full report and not in the earlier notes: the by-function agent table (software engineering 10% overall, 31% in technology companies); the build-instead-of-buy figure by industry (technology 41%); function-level cost and revenue effects; the function-level headcount table; the role split showing that 87% of AI-using respondents are managers or executives (72% C-level, executives or senior managers) and 13% individual contributors; the 47% versus 31% gap in negative personal effects between staff and executives.
- Chart 4 in the earlier list (32% expected, 14% reported, 39% expected) is valid as drawn. A software-engineering version now exists: 31% expected, 22% reported, 36% expected.

### Limits

Self-reported by managers about their own organisations; "scaling" and "EBIT impact" are perceptions, not accounts. Sub-bases are small: 92 high performers, 40 to 60 respondents in several industries. Year-on-year comparison uses two different samples with a 552-person overlap. The report contains an internal labelling error: Exhibits 16 and 17B/C print the 2025 field dates or the 2025 base (n = 1,753) under 2026 data. The 32% build-instead-of-buy figure is "at least one product or feature", which can be one internal tool; it does not measure displaced software spend. Function-level tables carry 15% to 26% "don't know".

## 2. DORA / Google Cloud, "The ROI of AI-assisted Software Development" (v. 2026.1)

### What it is, who published it, with what interest

A guide with a spreadsheet model, not a survey. Published by Google LLC (CC BY-NC-SA 4.0) as "a joint effort between Google Cloud's DORA team and Google Cloud's premier innovation practice, delta", a consulting unit; the text several times invites readers to contact Google Cloud Professional Services. Citations were "retrieved February, 2026". Google sells AI models, cloud capacity and consulting. The interest shows in the framing: the dip is "tuition cost", the remedy is investment in platforms, and the text quotes "Google Cloud customers found an average of 727% return on their investment in Google Cloud AI in three years".

### Method and sample

No new data collection. All empirical statements about AI and delivery performance are citations of the DORA 2025 "State of AI-assisted Software Development" report (pages 30 and 37 to 42 of that report). Other inputs are third-party: Google Cloud "ROI of AI 2025" (78% of executives report ROI on at least one gen AI use case; 88% of agentic early adopters see positive returns), Stanford AI Index 2025, the MIT NANDA "GenAI Divide" report, and Stanford software engineering productivity research. The J-curve is presented as a concept ("We anticipate that most organizations will encounter a J-Curve"); the document gives no measured depth or duration and says both "remain unpredictable".

### Findings

| Claim | Number or wording | Reference |
|---|---|---|
| Nature of the document | "This report is the start of a conversation. It describes a framework"; calculator "with many assumptions"; "Treat these calculations as a high-uncertainty estimate meant to spark a conversation" | Executive summary; note on methodology; appendix |
| Throughput | "Increased AI adoption was associated with an increase in higher software delivery throughput" (DORA 2025) | "Increase developer productivity" |
| Instability | "in the 2025 DORA report, increased AI adoption was associated with an increase in software delivery instability"; AI-assisted coding can "increase the volume and velocity of code generation, overwhelming existing deployment pipelines and manual review gates"; "We view this temporary rise in instability as part of the expected J-Curve" | same section |
| Relative effect sizes | Largest standardised effect on individual effectiveness; "The effect on instability was second largest, larger than the impacts on organizational performance, code quality, and so forth". The figure's axis runs from -0.05 to 0.20 (standardised, 89% credible intervals); no numeric values are printed | Figure 4; "Factor in the instability tax" |
| Burnout and friction | "the 2025 DORA research suggests otherwise": no reduction; "the friction moves" to a "verification tax" | text after Figure 4 |
| Review burden | "Developers invest time reviewing generated code due to concerns about the trustworthiness of output and hallucinations ... the tools increase the sheer volume of code produced, which expands the overall review burden"; "that code simply piles up in front of manual security reviews or brittle deployment pipelines"; "brings more pressure on the code review process" | J-Curve section; "Treat AI as an amplifier"; "Verification tax" |
| Productivity by task type | "a 35-40% productivity gain on simple, greenfield tasks ... on complex, legacy brownfield code is often 10% or less" (cited to Stanford) | "Calculate return of investment in the first year" |
| Individual perception | "more than 80% of survey respondents reported a perception that AI had increased their productivity" (DORA 2025, p. 30) | "Boost developer experience" |
| Headcount | "We strongly recommend organizations do not adopt a headcount-reduction strategy"; savings are framed as avoided hiring ("free headcount") | "Convert reclaimed hours into cost savings" |
| Sample model inputs | 500 technical FTE; fully loaded salary $176,000; net time saved 12.5% ("about one hour of an eight-hour working day"; sources "vary between 40 minutes and 150 minutes per day"); licence $250 per user per year; token and API costs $80 per user per year; training $9,600 per user per year; infrastructure $100,000; deployments 50 to 56 per year (+12%); change failure rate 5% to 6%; recovery time 4 hours; downtime $100,000 per hour; portfolio revenue $100m; idea success rate 33%; revenue per successful feature 0.5%; J-curve drop 15% for 3 months | Appendix: sample ROI calculator |
| Sample model outputs | Value $11,646,000 = headcount reinvestment capacity $11,000,000 + extra feature revenue $990,000 - downtime $344,000. Investment $8,365,000 = hard costs $5,065,000 + J-curve cost $3,300,000. First-year benefit $3,281,000; ROI 39%; payback 0.7 years | Appendix |
| Payback benchmarks | "average payback period ... is about eight months" (Google Cloud data); 6 to 9 months for agile teams, 12 to 18 months for large rollouts ("rule of thumb") | "Project the payback period" |

Reading of the model (own arithmetic on the document's inputs):

- 94% of the modelled value ($11.0m of $11.65m) is 500 x $176,000 x 12.5%, that is, the assumed net time saving valued at full salary cost. It is not cash: the guide itself says the time is reinvested and the saving is avoided hiring.
- The ROI is very sensitive to that one input. With all other sample inputs unchanged, 10% net time saved gives $9.45m of value and an ROI of about 13%; about 8.8% gives zero; 5% gives about -40%.
- Tools are a minor cost in the model. Licences and tokens are $330 per user per year ($165,000 in total, 2% of the investment); training ($4.8m) and the J-curve dip ($3.3m) are 97%. The $80 per user per year for tokens is far below what agentic use costs in 2026 and should not be quoted as a cost estimate.
- In the sample, the "instability tax" (-$344,000) is smaller than the gain from six extra features ($990,000), so the model's own example does not show instability cancelling throughput.

### Do the statements attributed to "DORA 2026" exist?

`benchmarks_vs_reality.md` line 84 (tagged `[S]`, from a Kodus summary) says: "more code tasks per team, shorter cycle times, higher individual effectiveness, and 'a sharp increase in software delivery instability'; gains are lost in review queues and in large PRs approved without context."

| Attributed statement | In the document? |
|---|---|
| Higher individual effectiveness | Yes, as a citation of DORA 2025 (strongest effect) |
| Higher throughput | Yes, as a citation of DORA 2025; the words "more code tasks per team" and "shorter cycle times" do not appear |
| "a sharp increase in software delivery instability" | No. The word "sharp" does not occur. The text says "an increase in software delivery instability", ranks it the second-largest effect, and calls it a "temporary rise" |
| Gains lost in review queues | In substance yes, in other words: code "piles up in front of manual security reviews", "overwhelming ... manual review gates", "code review bottlenecks". The term "review queue" does not appear |
| Large PRs approved without context | No. Pull requests are mentioned once, in a sentence about not judging teams by "the frequency of code commits or pull requests". The nearest content is the recommendation of "small batch sizes" and "strong version control practices" |
| "relies more on narrative than on new primary research" (the critic quoted there) | Accurate: there is no new primary research in it |

### Corrections to the earlier notes

- `benchmarks_vs_reality.md` line 84: retag and reword. The document is a 2026 guide that restates DORA 2025 findings; the quoted "sharp increase" is the summariser's wording and should not appear in quotation marks; drop "large PRs approved without context".
- `benchmarks_vs_reality.md` line 67 lists DORA among "large telemetry data sets". DORA is a survey with self-reported delivery metrics, and the 2026 document adds no data.
- `gaps_benchmarks.md` lines 79 and 86 are correct ("a gated ROI guide, not a new survey"; statements "could not be confirmed"). They can now be closed with the table above. The date there (2026-04-22, `[SR]`) is consistent with "v. 2026.1" and citations retrieved in February 2026; the document itself prints no publication date.
- `gaps_benchmarks.md` line 84 ("DORA 2025 gives no numeric effect size for AI and instability") is consistent with this guide, which reproduces the effect plot without values.
- `labour_market_skills.md` line 242 and `gaps_benchmarks.md` line 132 list "DORA 2026 content" as not retrieved: now retrieved.

### Limits

A vendor guide. The J-curve is asserted, with a promise of "eventual exponential growth" that no data in the document supports. The calculator's default inputs are illustrative, and the document says so. Anything it says about throughput, instability, burnout or friction is one-year-old survey correlation from DORA 2025, re-described here in causal language ("AI acts as an amplifier").

## 3. Sonar, "State of Code Developer Survey report" (2026)

### What it is, who published it, with what interest

A 57-page report by SonarSource, which sells SonarQube (static analysis and code review). The report's thesis is that AI creates a "verification bottleneck" and that deterministic review tools resolve it; pages 50 to 52 are a product chapter claiming that SonarQube users get better results from AI. The questionnaire's central finding is therefore also the vendor's sales argument.

### Method and sample

"Quantitative online survey" of professional developers; fieldwork "throughout October 2025"; n = 1,149 (p. 4). Screening: full-time employed or self-employed in a technology role, write code or manage developers, and "have used AI as part of their job within the past year", so non-users are excluded by design. No statement on recruitment, panel provider, weighting or margin of error. Sample: 52% North America, 27% Europe, 13% APAC, 7% Latin America, 1% Middle East and Africa (p. 53); 43% senior, lead or principal IC, 17% mid-level IC, 1% entry-level, about 40% managers to C-level (p. 54); 57% both write code and manage developers, 28% only write code, 15% only manage; 43% enterprise (over 1,000 employees), 27% mid-market, 29% SMB (p. 55); 62% in the technology sector.

### Findings

| Claim | Number | Reference |
|---|---|---|
| Use AI coding tools every day (of those who have tried them) | 72% (42% multiple times a day, 30% daily); n = 1,148 | p. 5 |
| "What % of the code you committed or contributed was / will be generated or significantly assisted by AI tools?" | 6% (2023), 19% (2024), 42% (2025), 55% (2026, predicted), 65% (2027, predicted); self-estimates, n = 979 | p. 5 |
| AI used for | prototypes 88%, internal non-critical production software 83%, customer-facing applications 73%, mission-critical services 58% | p. 6 |
| Use versus rated "extremely / very effective" | new code 90% use, 55% effective; documentation 74% / 74%; explaining code 78% / 66%; tests 75% / 59%; refactoring 72% / 43%; code review 55% / 47%; debugging 65% / 44%; changing existing code 76% / 42% | p. 7 |
| Self-estimated personal productivity change | +35% on average (n = 1,048); 40% for those with up to 10 years' experience, 32% for 20 years or more; 39% SMB, 34% enterprise | pp. 9, 39, 44 |
| "I trust that AI code is functionally correct" | completely agree 4%, somewhat agree 25%, neither 23%, somewhat disagree 31%, completely disagree 17% | p. 9 |
| Headline "96% don't fully trust" | 100% minus the 4% who completely agree | p. 9 |
| "I always check my AI-generated or assisted code before committing it" | completely agree 48%, somewhat agree 27%, neither 11%, somewhat disagree 11%, completely disagree 3% | p. 10 |
| Effort spent reviewing, testing, correcting AI output | 95% at least some; 59% "moderate" or "substantial" | p. 10 |
| Reviewing AI code versus a colleague's code | 38% more effort, 27% less | p. 10 |
| "AI often produces code that looks correct but isn't reliable" | 61% agree | p. 11 |
| "It requires a lot of effort ... to get good code from AI" | 61% agree | p. 11 |
| Positive impact of AI code on the team or company | developer productivity 89%, time-to-market 70%, release frequency 60%, code quality 58%, maintainability 56%, end-user experience 47%, technical debt 47%, rework costs 42%, defect rates 39%, vulnerability rates 34%, outage frequency 25%, outage severity 24% | p. 12 |
| Most important skill in the AI era | "reviewing and validating AI-generated code" 47%; prompting 42% | p. 13 |
| Tools used in the past year | GitHub Copilot 75%, ChatGPT 74%, Claude / Claude Code 48%, Gemini 37%, Cursor 31%, Codex 21%, JetBrains 17%; four tools per team on average | pp. 15-16 |
| Access through personal accounts | 35% across the top ten tools; ChatGPT 52%, Claude 36%, Cursor 27%, Copilot 17% | p. 17 |
| AI agents | 25% use regularly, 39% have experimented (64%), 21% exploring, 11% not planning; n = 1,149 | p. 20 |
| Agent use cases (n = 737) | documentation 68%, test generation 61%, code review 57%, whole features or modules 48%, security patching 28% | pp. 20-21 |
| Share of work week spent on "toil" | 24% on average, "almost exactly the same" for frequent and infrequent AI users (23% to 25%) | pp. 25-26 |
| Toil named by frequent versus infrequent AI users (n = 626) | managing technical debt 44% vs 34%; correcting or rewriting AI code 25% vs 15%; understanding existing systems 21% vs 29% | p. 27 |
| Static analysis | used by 70%; 57% apply it to AI-generated code (n = 799) | pp. 27-28 |
| "Extremely / very concerned" | sensitive data exposure 57%; declining understanding of the codebase 53%; deskilling 48%; subtle vulnerabilities 47%; severe vulnerabilities 44%; functional correctness 43% | p. 29 |
| Change in rigour because of AI | code quality: 36% more rigorous, 12% less rigorous, 29% still evaluating; security: 37% more, 7% less; compliance: 32% more, 7% less | pp. 31-32 |
| Negative effects on technical debt (n = 1,136) | 88% name at least one: looked correct but unreliable 53%, unnecessary or duplicative code 40%, buggy code 29%, hard to maintain 27%, more vulnerabilities 17% | p. 34 |
| Positive effects on technical debt | 93% name at least one: documentation 57%, test coverage 53%, refactoring 47% | p. 36 |
| Experience gap, up to 10 years versus 20 years or more | "looks correct but isn't reliable" 66% vs 48%; review takes more effort 40% vs 29%; worried about deskilling 50% vs 41%; AI share of committed code 45% vs 40% | pp. 38-43 |
| Company size | positive effect on time-to-market: SMB 76%, enterprise 67%; correcting AI code as top toil: SMB 28%, enterprise 17%; distinct AI-code guidelines: enterprise 18%, SMB 12% | pp. 45-49 |
| "AI delays releases because of extra review and fixes" | 19% to 20% agree | p. 48 |
| SonarQube users versus non-users | non-users "80% more likely" to report more outages (about 7% vs 4%) and "46% more likely" to report worse code quality (about 16% vs 11%) | p. 50 |

### Corrections to the earlier notes

- `benchmarks_vs_reality.md` line 115 (tagged `[PS]`): the figures 42%, 65% by 2027, 96%, 48% and 38% are confirmed at source and can be retagged `[P]`. Precise sample: 1,149, fieldwork October 2025. The 42% is "generated or significantly assisted", a self-estimate, so "AI accounts for 42% of committed code" overstates it.
- The same line cites "a newer release (Nov 2026): 76% generate AI code faster than they can verify it; 94% do not fully trust it; 39% fully agree it is always checked". These numbers are not in this document. They remain unverified at source.
- `gaps_benchmarks.md` line 195 ("Sonar 2026: all Sonar pages blocked ... figures remain unverified at source") can be closed for the 2026 report.
- `benchmarks_vs_reality.md` line 93 ("Sonar 'verification bottleneck'") is the report's own phrase (p. 3).
- Wording for a slide: "48% always check" means 48% "completely agree"; another 27% "somewhat agree", and 14% disagree. "96% do not fully trust" hides that 29% agree AI code is functionally correct and 48% disagree.

### Limits

Vendor survey whose finding matches the vendor's product. Recruitment and weighting are undisclosed; AI non-users are screened out; 72% of respondents manage developers, so many answers describe "your team / company". All quantities (share of code, productivity gain, toil share) are self-estimates. The data are 13 months old at the time of the talk and predate the 2026 shift to coding agents: here Copilot leads with 75% and 25% use agents regularly, against the JetBrains 2026 picture below. The SonarQube comparison is correlational, has no bases, and turns differences of 3 to 5 percentage points into "80% more likely".

## 4. Demirci, Hannane, Zhu, "Who Is AI Replacing? The Impact of Generative AI on Online Freelancing Platforms" (CESifo WP 11276, August 2024)

### What it is

An academic working paper (Harvard Business School, DIW and TU Berlin, Imperial College), later published in Management Science. No commercial interest. This is the version behind the authors' HBR summary that `labour_market_skills.md` could not open.

### Data and method

All job posts from "an undisclosed, globally leading" freelancing platform, collected through its API: 1,388,711 posts from July 2021 to July 2023; analysis sample 1,218,463 fixed-price posts from 541,828 employers in the 61 largest countries (hourly jobs, about 20%, are excluded from the main analysis and used in a robustness check). Posts are grouped by a Louvain clustering of 2,712 skill tags into 15 clusters; eight are used. Treated: "automation-prone" (writing; software, app and web development; engineering) and "image-generating" (graphic design; 3D modelling). Control: "manual-intensive" (data and office management, video services, audio services). Difference-in-differences on the log number of posts per cluster, week and country, around the release of ChatGPT (2022-11-30) and of image models (2022-07-20), with week and country-cluster fixed effects; checked with negative binomial, Callaway-Sant'Anna and synthetic DiD estimators, placebo dates, and a Google Trends co-search index as a measure of awareness.

### Findings

| Claim | Number | Reference |
|---|---|---|
| Job posts in automation-prone clusters relative to manual-intensive ones, within eight months after ChatGPT | -20.86% (coefficient -0.234; other estimators -0.174 to -0.241) | Table 2, col. 1 |
| Writing | -30.37% (coefficient -0.362; CS DiD -0.233; synthetic DiD -0.280) | Table 2, col. 2 |
| Software, app and web development | -20.62% (coefficient -0.231; -0.165 to -0.187 in other estimators) | Table 2, col. 3 |
| Engineering | -10.42% (coefficient -0.11, not significant in the baseline; -0.235 in the negative binomial) | Table 2, col. 4 |
| Image-related posts within a year after image models | -17.01% (coefficient -0.186); -12.90% when the window ends before ChatGPT | Table 4, cols. 1-2 |
| Graphic design / 3D modelling | -18.47% / -15.52% (the abstract and introduction print 18.49% and 15.57%) | Table 4, cols. 3 and 5 |
| Trend over time | effect "not only persists but also grows", about 10% greater decrease every three months | Appendix D, Table D1 |
| Maximum budget of remaining automation-prone posts | +5.71% (+$12.67 on a pre-mean of $221.66) | Table 3, col. 1 |
| Bids per post (competition) | +8.57% | Table 3, col. 2 |
| Complexity (number of skill tags per post) | +2.18% | Table 3, col. 3 |
| Posting frequency of employers who stayed | weeks with a post -36.64%; posts per month -12.82% (conditional), -27.16% (unconditional) | Table 3, cols. 4-6 |
| Posts requiring "ChatGPT" as a skill | 903 in the post-period, 744 of them in software, app and web development; +0.68 posts per week | Section 4.2 |
| Awareness link | one standard deviation more "ChatGPT + task" searches goes with 8.01% fewer posts | Section 4.2, Figure E1 |
| Share of all posts by cluster before / after ChatGPT | software, app and web 35.32% / 33.68%; writing 10.02% / 7.87%; graphic design 22.15% / 24.25% | Table 1 |

Budget, bids and complexity are estimated on employers who posted both before and after (35.45% of observations), with employer fixed effects.

### Corrections to the earlier notes

- `labour_market_skills.md` line 162 lists the recalled figures as unverified ("writing postings about -30%, software and web development about -21%, image-related about -17%"). All three are confirmed: 30.37%, 20.62%, 17.01%. Add engineering -10.42% and the overall -20.86%.
- Line 147 gives the affiliation as "Imperial College, DIW Berlin"; the first author is at Harvard Business School.
- The paper supports the statement in line 158 (short, well-specified tasks go first) only indirectly: it shows that the remaining posts are slightly more complex and better paid, not which posts disappeared.

### Limits

Relative effects: the control clusters also declined (log posts fell in every cluster in Table 1), so the paper measures the extra decline of exposed work, and it is a lower bound if "manual" clusters were also affected. One platform, not named; fixed-price jobs only in the main analysis; translation, marketing, legal, finance and blockchain clusters are excluded. The window ends in July 2023, with ChatGPT 3.5 and GPT-4 and before any coding agent. Job posts are demand, not earnings or hours. The +5.71% budget is for surviving posts from surviving employers, so it is a composition effect and not a pay rise for the same work. Standard errors are clustered on eight job clusters. A fall in posts on one platform cannot be separated from employers moving elsewhere or doing the work in-house.

## 5. Hui, Reshef, Zhou, "The Short-Term Effects of Generative Artificial Intelligence on Employment: Evidence from an Online Labor Market" (version of 2024-10-12)

### What it is

An academic paper (Washington University in St. Louis, New York University), published in Organization Science. No commercial interest. The file name says "preview", but the converted text is the complete manuscript: abstract, five sections, references, four tables, figures and an online appendix with data description. Nothing is cut off.

### Data and method

Upwork, scraped through three of its APIs. From 568,647 searchable freelancers in 215 occupations, the sample keeps those in a single occupation with at least one completed job: 79,322 freelancers in the text analysis and 80,983 in the image analysis; freelancer-month panel from January 2022 to April 2023 (about 1.24 million and 1.50 million observations). 16% are based in the US; mean hourly rate $28; mean monthly earnings on the platform $181 to $230; a freelancer starts a job once every two to three months (Table 1). Treated: writing, proofreading and copyediting for ChatGPT (post period from November 2022); design, image editing and art for DALL-E 2 and Midjourney (post period from April 2022). Control: all other occupations, which includes software development. Difference-in-differences with freelancer and month fixed effects, inverse hyperbolic sine outcomes, standard errors clustered by occupation (about 190 clusters); event-study plots; robustness with coarsened exact matching, year-on-year comparison for the same freelancers, wild bootstrap, Poisson and logit.

### Findings

| Claim | Number | Reference |
|---|---|---|
| Monthly number of jobs, writing occupations after ChatGPT | -2.0% (s.e. 0.004) | Table 2, Panel A, col. 1 |
| Monthly earnings, writing occupations | -5.2% (s.e. 0.016) | Table 2, Panel A, col. 2 |
| Probability of starting any job in a month | -1.2 percentage points, "approximately a 10% drop compared to baseline" | Table 2, Panel A, col. 3 |
| Jobs and income conditional on working | -4.7% (s.e. 0.011) and -5.1% (not significant) | Table 2, Panel A, cols. 4-5 |
| Image occupations after DALL-E 2 and Midjourney | jobs -2.1% (s.e. 0.005); earnings -5.2% (s.e. 0.019); probability of working -1.4 points | Table 2, Panel B |
| Course over time | "sharp, persistent, and growing decreases" | Figures 2 and 3 |
| High-quality freelancers, text | each 1% more past earnings goes with a further 0.5% fewer jobs and 1.7% lower income; "Top Rated" badge: -2.4% jobs and -8.7% income in addition; higher success rate: -2.8% and -10.7% | Table 3 |
| High-quality freelancers, image | each 1% more past earnings: -1.1% jobs and -3.3% income; higher skill level of past jobs: -3.1% and -8.8% | Table 4 |
| Authors' reading | "we can generally rule out that freelancer quality moderates the adverse effects"; "suggestive evidence that top freelancers are disproportionately affected" | Section 4.2, abstract |
| Related estimates quoted | Liu et al. 2023: -3.87%; Yilmaz et al. 2023: -4.81% | Section 4 |
| Who gains | "employers, rather than workers, are better positioned to capture the value" in the short run | Section 5 |

### Corrections to the earlier notes

- `labour_market_skills.md` line 162: the recalled "about 2% fewer monthly jobs and 5% lower earnings for exposed freelancers" is confirmed (2.0% and 5.2%; image occupations 2.1% and 5.2%). The finding about top freelancers was not in the earlier notes and should be added, with its hedge ("suggestive").
- These numbers and the Demirci numbers are not two estimates of one quantity. Demirci et al. count posts per category (demand, -21% to -30%); Hui et al. measure jobs and earnings per freelancer who stayed visible (-2% and -5%), with software developers in the control group. Do not average them or present them as a range.
- This paper says nothing about software work. For the "average coder" argument only Demirci et al. (software, app and web posts -20.62%) and the Teutloff et al. paper already in the notes are relevant.

### Limits

Stated by the authors: off-platform work is not observed; only "searchable" profiles are included and their share is unknown; profile attributes (badge, success rate, hourly rate) are observed once, in April 2023, after treatment, which weakens the heterogeneity analysis; demand and supply effects cannot be separated; job postings, wages and AI adoption are not observed, so the mechanism behind the top-freelancer result is open; results "may not quantitatively extrapolate to traditional labor markets". Additional: the window ends five months after ChatGPT's release; control occupations are also exposed, which the authors treat as making the estimate a lower bound; the effects are small relative to month-to-month noise in freelancer income (standard deviation $1,623 on a mean of $181).

## 6. WAPOR 2026 poster (Makeeva and Molotova, JetBrains)

### What it is

A conference poster, "Archiving Industry Survey Data for Academic and Community Use: Open datasets on software development, learning, work, and attitudes toward AI", by Aleksandra Makeeva and Anastasia Molotova (Surveys team, Strategic Research and Market Intelligence, JetBrains), 79th Annual Conference of the World Association for Public Opinion Research, Mexico City, 2026-10-26 to 2026-10-29. Poster 1 of 2. It is the method description for the dataset analysed in section 7, written by the dataset's producers for an audience of survey methodologists. Full text: `converted/reports/WAPOR2026_makeeva.md`.

### Relevance

Directly relevant as the method statement for section 7. It contains nothing about Russia or about public (non-developer) opinion: all figures are global weighted shares of developers. Russian appears only as one of the ten questionnaire languages.

### Findings

| Claim | Number | Reference |
|---|---|---|
| Developer Ecosystem Survey 2026 | 56,970 responses collected; 22,082 complete responses after filtering; 198 countries and regions; fielded May to July 2026; up to 585 questions, adaptive routing, random submodules, about 30 minutes | panel 04 |
| Recruitment | JetBrains channels, external digital marketing campaigns, user groups and community channels, peer sharing | panel 04 |
| Cleaning | more than 30 criteria (speed, duplicate IP or email, over 75% identical answers, straight-lining) | panel 04 |
| Weighting | calibrated to "the share of JetBrains users, regional developer populations, employment status, and use of selected programming languages" | panel 04 |
| Stated limitation | "nonprobability samples, and coverage and self-selection limitations remain after cleaning and weighting. JetBrains users may be more willing to respond" | panel 04 |
| Trust in AI "to make decisions that impact your personal life" (1 strongly distrust to 5 strongly trust) | 19.9% / 20.6% / 35.8% / 17.9% / 5.8%; n = 9,641 | panel 03 |
| Emotion about "the increasing role of AI in society" | excited 28.5%, uncertain 21.6%, hopeful 19.9%, anxious 14.0%, fearful 6.6%, indifferent 6.2%; n = 19,921 | panel 03 |
| Most important ethical concerns about AI (multiple choice) | misuse 59.2%, job displacement 54.7%, privacy 52.7%, lack of transparency 47.1%, copyright 39.5%, bias 31.8%, existential risks 31.4%, none 8.2%; n = 9,836 | panel 03 |
| "How secure do you feel in your current job?" | completely 12.4%, very 14.7%, fairly secure 28.6%; fairly 10.4%, very 4.4%, completely insecure 2.8%; hard to say 24.8%; n = 6,254 | panel 03 |
| Burnout in the past 1 to 2 years | 58%; n = 9,545 | panel 03 |
| "Is studying computer science worth it in 2026?" | 71% yes; n = 9,939 | panel 03 |
| Publication | "The report and raw data will be published in November 2026" | panel 04 |

Use for the talk: the poster's weighted shares are reproduced exactly by the analysis in section 7 (trust 19.9 / 20.6 / 35.8 / 17.9 / 5.8 with n = 9,641; job security and ethical concerns to the decimal). This validates the weight column and the handling of multi-select answers used below.

### Limits

A poster by the vendor's own survey team. The 2026 raw file holds 28,941 rows, not the 22,082 "complete responses" named here; the archive read for section 7 contained no README, so the difference (probably partial responses kept in the public file) is unexplained.

## 7. JetBrains Developer Ecosystem Survey 2026, raw data

### What it is, who published it, with what interest

The public respondent-level file of the tenth JetBrains Developer Ecosystem Survey (CC BY 4.0). JetBrains sells IDEs and its own AI products (AI Assistant, Junie, Air), which appear as answer options. Respondents are recruited largely through JetBrains channels, so they are its audience: people who chose to answer a 30-minute survey from a tool vendor. The questionnaire asks about AI at length and takes use for granted in many modules.

### Method and sample (from the file itself)

- 28,941 rows, 5,873 columns. A `weight` column exists (mean 1.0, range 0.014 to 14.98, none missing). All shares below are weighted; the unweighted share follows in brackets where it differs by three points or more. n is the unweighted number answering.
- Encoding. Single-choice questions are one column holding the answer text. Multi-select questions are one column per option, named `question::option`, holding the option text if chosen and empty otherwise; the base is respondents with any option chosen. Table questions are one column per row item holding the scale answer. Some questions have no short name in the codebook and appear as `question__NNN`. Processed `*_imputed_final` columns exist for the tool questions and are not used here.
- Routing. Almost every question went to a random or routed subset, so n runs from about 20,000 (core AI block) to about 2,500 (statements about the future). The core AI-at-work block was shown only to employed respondents (employed full-time or part-time, self-employed, founder, working student; n = 21,570), and of those 92% answered it. Students and people out of work were not asked.
- Employment: 58% employed full-time, 13% self-employed or freelance, 10% students, 6% working students. Position level (n = 20,289): senior 48% (53%), middle 31% (27%), junior 15% (13%). Company size (n = 18,069): small, medium and large about one third each.
- Country. Weighted: China 19.9%, United States 13.6%, India 11.9%, Japan 6.9%, Germany 3.0%. Unweighted: United States 9.2%, India 8.9%, Germany 6.5%, Kenya 5.8%, China Mainland 4.5% (1,310 respondents). The file's own region field puts China at 4.7% of rows and 20.1% of the weight, and Europe at 37% of rows and 19% of the weight.
- Russia and CIS. The Russian Federation has 58 respondents (0.2% of rows) carrying 2.1% of the weight; Uzbekistan 57, Armenia 46, Moldova 43, Kazakhstan 39, Kyrgyzstan 26, Azerbaijan 24; no row is labelled Belarus. For routed questions this leaves 23 to 36 Russian respondents, or fewer than 20. Russian figures below are anecdote, not estimate.
- Salary. The question was asked (a `suspected_salary` flag marks 14,823 answers "normal", 135 "too small", 127 "too big"), but the answers are not in the public file. No pay analysis is possible.

### 7.1 AI tool use

| Claim | Number | Question (exact wording) and n |
|---|---|---|
| Employed respondents naming at least one AI tool used at work | 90% | "Which of these AI tools do you use for your coding and other development-related tasks at work?" (multi-select); any tool chosen, base all employed, n = 21,570 |
| Regular users naming no tool | 3% | "Which of these AI tools do you regularly use for coding and other development-related activities?", option "None"; n = 26,427 (includes students) |
| Use a coding agent every day (IDE, CLI or remote) | 64% (61%) of those asked; 59% of all employed if those not asked are counted as non-users | "How often, if at all, do you use the following types of AI assistance for your coding and development-related tasks at work?"; n = 19,949 |
| Use a coding agent at least once a week | 88% of those asked; 81% of all employed | same |
| Never use any type of agent | 6% of those asked | same |
| At least weekly, by type | chat without agent mode 83%; code completion 79%; agents in the IDE 78%; agents in the CLI or terminal 74%; remote cloud agents 42% | same |
| Every day, by type | completion 56%; IDE agents 51% (48%); chat 49% (46%); CLI agents 48% (45%); remote cloud agents 21% (17%) | same |
| Never, by type | remote cloud agents 36% (39%); CLI agents 14%; IDE agents 10%; completion 10%; chat 6% | same |
| Tools used at work | Claude Code 39% (42%), GitHub Copilot 20% (24%), ChatGPT 19%, OpenAI Codex 16% (13%), Claude chatbot 16%, Cursor 12% (10%), Google Antigravity 7%, OpenCode 7%, Gemini chatbot 7%, JetBrains AI Assistant 7% (9%), JetBrains Junie 3% (5%) | "Which of these AI tools do you use for your coding and other development-related tasks at work?"; n = 19,492 |
| Most used tool at work | Claude Code 31% (34%), GitHub Copilot 12% (15%), OpenAI Codex 9% (7%), ChatGPT 8%, Cursor 7%, Claude chatbot 6% | "Which one of these AI tools do you use the most for coding and other development-related activities at work?"; n = 19,201 |
| Share of own code "fully generated by AI coding agents" | 0%: 10%; 1 to 20%: 15% (18%); 21 to 40%: 15%; 41 to 60%: 15%; 61 to 80%: 18%; 81 to 99%: 19% (16%); 100%: 6% (4%). At least 61%: 43% (38%). Midpoint mean about 50% (47%) | Table item "fully generated by AI coding agents" (the stem of the table is not in the codebook); n = 19,924 |
| Share "written by you with some AI assistance" | midpoint mean about 44% | same table; n = 19,923 |
| Share "fully written by you without any AI assistance" | 0%: 21% (16%); 1 to 20%: 34%; 100%: 3%. Midpoint mean about 29% (31%) | same table; n = 19,921 |
| Expectation for next year | AI will fully write "much more" 36% (30%), "somewhat more" 29%, "about the same" 26% (29%), less 7% | "Do you expect AI to fully write more, less, or about the same percentage of your code in the next year?"; n = 19,924 |
| Share of work tasks done with agents | at least 61%: 54% (49%); 100%: 9%; 0%: 3%. Midpoint mean about 60% | "What percentage of your coding and development-related work tasks have you done with AI agents in the last month?"; n = 16,229 |
| Typical agent run | 3 to 10 minutes 40%; 1 to 3 minutes 20%; 11 to 30 minutes 23%; over 30 minutes 13% | "On average, how long does your AI agent typically run from when you start the task until you receive the result for review?"; n = 16,188 |
| "Full permission" mode | almost never 40% (46%); minority of cases 23%; majority or almost always 21% | "How often, if at all, do you use AI coding agents in a "full permission" mode (e.g. Brave and YOLO modes) for your work tasks?"; n = 16,192 |
| Agent practices | context and guideline files 61%; modular skills 50%; spec-driven development 50%; MCP integrations 38%; automated verification loops 32%; multi-agent orchestration 28%; several agents in parallel 26% | "Which practices of coding and developing with AI agents do you use, if any?"; n = 16,195 |
| Preferred mode | CLI agents 33%, IDE agents 33%, completion 17%, chat 14%, remote cloud agents 2% | "Which type of AI coding and development assistance do you enjoy working with the most?"; n = 5,727 |
| Colleagues using AI | 81 to 100% of developers in the company: 41%; 61 to 80%: 21%; 0 to 20%: 5% | "What percentage of software developers / coding professionals use AI tools and features for coding and development-related activities in your company?"; n = 2,318 |

The three code shares are asked separately and need not sum to 100 (the file's own check column shows that 13,201 answers sum to 71 to 140% and 4,767 to more than 140%), so they cannot be shown as a pie.

### 7.2 Trust, quality, review

| Claim | Number | Question and n |
|---|---|---|
| Trust in agent output | fully trust 2%; mostly trust 43% (37%); neither 30%; mostly do not trust 19% (22%); do not trust at all 5% (7%) | "How much do you trust or distrust the output generated by AI coding agents?"; n = 4,045 |
| Review of agent code | always 43% (49%); often 34%; sometimes 16%; rarely or never 8% | "How often, if at all, do you review code generated by AI agents for your work tasks?"; n = 16,216 |
| Agent code rewritten by hand | 1 to 20%: 34%; 21 to 40%: 24%; 41 to 60%: 15%; over 60%: 18%; 0%: 6%. Midpoint mean about 34% | "In the last month, what percentage of code generated by AI agents for your work tasks have you ended up manually rewriting or editing?"; n = 16,204 |
| Effort to review an AI pull request against a colleague's | more 37% (42%); the same 26%; less 30% (24%) | "Compared to reviewing a pull request from your colleagues of the same seniority as you, how much more or less effort does it take to review an AI-generated pull request for a similar task?"; n = 15,910 |
| Agent solutions against the respondent's own code | better 54% (47%); the same 19% (22%); worse 25% (29%) | "How would you rate the quality of solutions generated by AI coding agents compared to code fully written without any AI assistance by…?", item "yourself"; n = 16,219 |
| Against "an average developer" | better 52%; the same 23%; worse 17% | same, n = 16,219 |
| When dissatisfied | rephrase and rerun 65%; ask for specific changes 60%; rewrite myself 49% (55%); split the task 49% | "What do you usually do when you are dissatisfied with an AI agent's output for the task?"; n = 16,216 |
| Time on code-related work spent reviewing AI output | more than 25% of that time: 49%; more than half: 20% | "How much of your working time did you spend on the following activities during the last working week?", item "Reviewing AI output"; n = 5,563 |
| Time prompting / waiting | prompting above 25%: 41%; waiting on AI above 25%: 31% (26%) | same table |
| New frictions | more time reviewing AI artifacts 55%; more time correcting or rewriting them 40%; hard to get what is expected 37%; hard to identify errors in AI code 32%; waiting 27%; AI-related technical debt 23%; reduced confidence in codebase quality 22%; none 7% | "What new frictions, if any, has the use of AI tools introduced into your development work?"; n = 3,573 |
| Benefits | faster coding 73%; increased productivity 71%; faster repetitive tasks 70%; faster learning 59%; better quality of code 36%; greater confidence in my solutions 27% | "What benefits do you get from using AI tools for coding and other development-related activities?"; n = 7,053 |
| Changes over the past year, improved / unchanged / worsened | developer productivity 72 / 23 / 6; code quality 54 / 33 / 14; code security 42 / 46 / 13; technical debt 41 / 38 / 21; cognitive debt 43 / 27 / 30 | Table `dx_dev_changes` (stem not in the codebook; items as named); n about 6,030 |
| Sense of code ownership | decreased 46%; unchanged 37%; increased 18% | "How has your sense of code ownership changed over the past year as a result of using AI tools?"; n = 3,672 |
| Sense of control over the codebase | decreased 45%; unchanged 36%; increased 20% | "How has your sense of control over the codebase changed over the past year as a result of using AI tools?"; n = 3,650 |
| Core job skills | improved 74% (67%); no change 19% (24%); worsened 8% | "How has AI affected your core job skills?"; n = 7,505 |
| Mental workload | decreased 43%; no change 29%; increased 28% | "To what extent has your mental workload changed since you began using AI tools?"; n = 9,799 |
| Security trust in AI code | fully 2%; mostly 18% (15%); moderately 38%; slightly 26%; not at all 16% (20%) | "To what extent do you trust AI-generated code from a security perspective?"; n = 10,124 |
| AI code against hand-written code, security | more secure 34% (29%); the same 32%; less secure 34% (38%) | "Compared to manually written code, AI-generated code is …?"; n = 9,504 |
| Security risks of most concern (up to three) | over-reliance on AI suggestions 49%; insecure patterns or vulnerabilities 48%; exposure of sensitive data 44%; outdated practices 38% | "Which security risks related to AI usage concern you the most, if any? Select up to three."; n = 10,121 |
| Risks of remote agents at scale (up to three) | quality 56%; human-related, including skill degradation 53% (57%); legal and compliance 44%; financial 37% | "What potential risks, if any, do you see in the large-scale adoption of remote cloud AI coding agents within your organization? (Select up to three)"; n = 6,034 |
| Single biggest concern | negative effect on my skills 12% (14%); quality of generated code 12%; job security 12%; costs 11%; future tech debt 10%; privacy and security 9%; more bugs 9%; no concerns 1% | "What is your biggest concern about AI in coding and software development?" (single choice); n = 2,836 |

### 7.3 What is delegated and what is kept

| Activity | Would delegate | Would still do it myself | Not sure |
|---|---|---|---|
| Writing boilerplate, repetitive code | 75% | 10% | 15% |
| Writing tests | 68% (64%) | 14% (18%) | 18% |
| Checking code for potential issues | 60% (55%) | 21% | 19% |
| Prototyping solutions | 60% | 19% | 21% |
| Creating project-related content | 59% | 24% | 18% |
| Improving or optimizing code | 59% (53%) | 20% (24%) | 22% |
| Refactoring | 55% (50%) | 20% (24%) | 25% |
| Understanding recent code changes | 50% (43%) | 33% (38%) | 17% |
| Debugging | 45% (42%) | 33% | 23% |
| Writing application logic code | 44% (36%) | 32% (38%) | 24% |
| Performing code reviews | 42% (37%) | 35% (39%) | 23% |

Question: "How likely is it that you would delegate the following activities to AI tools for coding and development?"; n = 5,345 to 5,387. Unweighted, more respondents would keep application logic and code review than would delegate them; weighting reverses the order.

Company view: "Which areas of the software development cycle does your company use AI agents in, if any?" (n = 2,353): implementing features 67%, writing tests 62%, code review 60%, refactoring 52%, system design 52%, documentation 46%, debugging 44%, requirement analysis 43%, deployment and monitoring 15%, security 11%, incident management 11%.

### 7.4 Who pays, costs, return

| Claim | Number | Question and n |
|---|---|---|
| Payment per tool, pooled over 9,970 tool mentions | organisation pays 36% (40%); I pay myself 33%; free version 20%; I pay and am reimbursed 7%; free access to a paid version 5% | "Who pays for each of the following AI tools that you use for your work?"; 5,273 respondents |
| Respondents paying personally for at least one work tool | 40% | same |
| Claude Code | organisation 51% (55%); self 35%; reimbursed 7%; free 6% | same; n = 2,334 |
| GitHub Copilot | organisation 61% (69%); self 14% | n = 1,190 |
| OpenAI Codex | self 49%; organisation 32% | n = 716 |
| Cursor | organisation 41% (51%); self 32% | n = 514 |
| ChatGPT | self 38%; free 35%; organisation 19% | n = 961 |
| Bought extra credits or quota last month | 50% (46%) for at least one tool; Claude Code 17% | "In the last month, for which of the following AI tools that you personally use at work have you used extra AI credits, tokens, or quotas on top of the regular limits for your subscription?"; n = 5,264 |
| Why not use agents at work (non-users only) | expensive 52% (47%); security concerns 38%; poor quality 32%; don't trust them 22%; prohibited in my company 14% | "What are the main factors that stop you from using AI coding agents for work tasks?"; n = 862 |
| Company spend next year | more 65%; the same 22%; less 6% | "Do you expect your company to spend more, less, or about the same on AI tools for coding and development in the next year?"; n = 1,978 |
| Company concern about spend | very 14%; somewhat 39%; not at all 33% | "How concerned, if at all, is your company about its current spending on AI tools for coding and development?"; n = 1,928 |
| Cost controls | none 34%; budgets per developer or team 21%; tiered model use 20%; local or self-hosted models 16% | "Which of the following approaches, if any, does your organization use to optimize spending on AI coding tools?"; n = 1,915 |
| Satisfaction with ROI | satisfied 44%; neutral 27%; dissatisfied 13%; don't know 16% | "How satisfied or dissatisfied is your organization with the ROI from its spending on AI coding tools (including tool costs and enablement)?"; n = 1,905 |
| Measured ROI observed | productivity gains 41%; faster delivery 37%; "We don't measure ROI from AI deployments" 27%; quality 23%; cost savings 17%; none observed 7% | "What measurable ROI, if any, have you observed from the adoption of AI tools for coding and development within your company or organization?"; n = 1,919 |

No question asks how much is paid. The routed question on weekly time saved (`ai_time_saving`, n = 3,456: "8 hours or more" 67%) has no wording in the codebook and an implausible distribution; it is not used.

### 7.5 Job market and replacement

| Claim | Number | Question and n |
|---|---|---|
| Local job market | very challenging 30%; somewhat challenging 28%; neutral 16%; somewhat favourable 14%; very favourable 4%; don't know 8% | "How would you describe the current job market for software developers in your city or area, particularly in terms of how easy it is to get a job?"; n = 9,928 |
| Job security | secure (three grades) 56% (60%); insecure (three grades) 18% (15%); hard to say 25% | "How secure do you feel in your current job?"; n = 6,254 |
| Headcount reduced because of AI | no 56% (61%); yes, coding roles 15% (11%); yes, non-coding roles 6%; yes, managerial roles 3%; don't know 18%. Any yes: 23% (18%) | "Has your company reduced headcount in the past year due to adopting AI tools?"; n = 4,437 |
| Layoffs for any reason | small-scale 32%; mass 13%; none 40% | "Have there been any layoffs in companies you worked for in the past two years?"; n = 7,352 |
| Anxiety about replacement | always 13%; often 16%; sometimes 28%; rarely 24%; never 20% | "I feel anxious that AI advancements might eventually replace my role as a developer"; n = 9,477 |
| Pressure to keep up | always or often 35% (39%) | "I feel overwhelmed by the need to keep up with the rapid advancements in AI and the pressure to stay relevant in my field"; n = 9,472 |
| "AI will eventually take over the coding process, fully replacing human developers" | agree 22% (18%); neither 31%; disagree 47% (53%) | "To what extent do you agree with each of the following statements?"; n = 2,553 |
| "The adoption of AI coding will decrease the demand for professional software developers" | agree 38% (35%); neither 31%; disagree 32% | same; n = 2,563 |
| "AI tools for developers will radically change the software development job market" | agree 76% (72%); disagree 7% | same; n = 2,564 |
| "Employers will expect every software developer to be proficient with AI tools for developers" | agree 78% | same; n = 2,561 |
| "AI will perform tactical tasks ... while developers will focus on strategic work" | agree 70% (64%) | same; n = 2,575 |
| "Development will become more enjoyable because of AI" | agree 54% (47%); disagree 17% (22%) | same; n = 2,559 |
| Changing profession | actively considering 11%; from time to time 25%; no 58% | "Are you thinking about changing your profession?"; n = 9,934 |
| Same career again | yes 72%; not sure 18%; no 10% | "If you could go back to the beginning of your career, would you choose the same profession?"; n = 9,934 |
| Studying computer science | worth it 71% (69%); not sure 17%; not worth it 13% | "Is studying computer science worth it in 2026?"; n = 9,939 |
| Burnout | 58% | "Have you experienced burnout in the past 1–2 years?"; n = 9,545 |
| Non-coding colleagues building things | more involved 53%; no 29% | "Over the last year, have your non-coding colleagues become more involved in development and prototyping?"; n = 4,427 |
| Feeling about AI in development (multi-select) | excited 33%, optimistic 28%, hopeful 28%, uncertain 23%, anxious 21%, worried 19%, skeptical 18% (22%), fearful 10% | "When you consider the increasing role of AI in software development, which of the following best describes your overall feeling?"; n = 6,033 |
| When AGI | within 3 years 18%; 4 to 10 years 31%; 10 to 20 years 20%; never 14% | "When do you expect true AGI (human-like artificial general intelligence) will be developed?"; n = 9,822 |

### 7.6 Cross-tabs

Weighted shares, unweighted n in brackets. Seniority is the self-declared position level; experience is "How many years of professional coding experience do you have?".

By position level:

| Measure | Junior | Middle | Senior |
|---|---|---|---|
| Uses a coding agent every day (of those asked) | 58% (2,441) | 63% (5,070) | 69% (10,212) |
| At least 61% of code fully by agents | 39% | 40% | 46% |
| Most used tool is Claude Code | 25% | 29% | 34% |
| Always reviews agent code | 41% (1,950) | 40% (4,075) | 46% (8,503) |
| Agent solutions better than own code | 59% | 57% | 50% |
| Agent solutions worse than own code | 20% | 23% | 28% |
| AI pull request takes more effort to review | 31% | 34% | 41% |
| Would delegate application logic | 35% (401) | 47% (983) | 51% (2,095) |
| Trusts agent output (mostly or fully) | 44% (545) | 43% (1,132) | 47% (2,006) |
| Job market "very challenging" | 34% (756) | 31% (1,691) | 26% (3,236) |
| Anxious about replacement, often or always | 32% (703) | 30% (1,577) | 25% (3,150) |
| Overwhelmed by keeping up with AI, often or always | 39% | 35% | 31% |
| Feels insecure in the job | 15% (757) | 20% (1,691) | 17% (3,235) |
| Organisation pays for Claude Code | 52% (231) | 57% (528) | 62% (1,318) |

By years of professional coding experience (up to 2 / 3 to 10 / 11 or more): daily agent use 54% / 68% / 66%; agent solutions better than own 61% / 54% / 49%; would delegate application logic 30% / 49% / 49%; job market challenging 60% / 63% / 50%; company cut headcount because of AI 32% (n = 528) / 24% / 19%; burnout 64% / 61% / 48%; remote cloud agents at least weekly 48% / 42% / 37%.

By region:

| Measure | Europe | North America | China | India | Japan | All |
|---|---|---|---|---|---|---|
| Uses a coding agent every day | 58% (8,207) | 54% (2,255) | 81% (1,015) | 67% (1,364) | 69% (518) | 64% |
| At least 61% of code fully by agents | 34% | 34% | 57% | 42% | 52% | 43% |
| No code written without AI | 15% | 17% | 38% | 11% | 37% | 21% |
| Trusts agent output | 34% (1,793) | 38% (522) | 60% (227) | 43% (253) | 42% (110) | 45% |
| Distrusts agent output | 37% | 31% | 11% | 18% | 12% | 23% |
| Always reviews agent code | 52% (6,716) | 50% (1,826) | 28% (799) | 48% (1,103) | 25% (429) | 43% |
| Agent solutions better than own | 37% | 43% | 66% | 64% | 67% | 54% |
| Would delegate application logic | 32% (2,158) | 36% (684) | 66% (248) | 33% (425) | 59% (135) | 44% |
| Core skills improved | 60% (3,122) | 55% (945) | 94% (368) | 75% (453) | 82% (222) | 74% |
| Excited or hopeful about AI in society | 34% | 36% | 61% | 57% | 60% | 48% |
| Job market "very challenging" | 27% (3,875) | 38% (1,240) | 34% (452) | 33% (853) | 7% (239) | 30% |
| Company cut headcount because of AI | 14% (2,018) | 19% (521) | 35% (261) | 38% (274) | 7% (136) | 23% |
| Anxious about replacement, often or always | 28% | 32% | 31% | 35% | 20% | 29% |
| CS study worth it | 65% | 58% | 77% | 74% | 87% | 71% |

Russia and CIS (indicative only). Russian Federation, n = 36 for the core AI block and n = 23 to 27 elsewhere: daily agent use 42%, at least weekly 63%, remote cloud agents weekly 11%, always reviews agent code 61%, agent solutions worse than own 60% and better 24%, slight or no security trust in AI code 64%, GitHub Copilot as most used tool 0 of 30. CIS including Russia (n = 210 for the core block, 50 to 100 elsewhere; weighted and unweighted diverge widely because the few Russian respondents carry large weights): daily agent use 47% weighted, 65% unweighted; trusts agent output 47% (n = 55); job market challenging 71% (n = 99); job secure 76% (n = 61). The direction (less agent use and more scepticism in Russia than in the global sample, consistent with restricted access to Western tools) is plausible, but 36 people cannot carry a slide.

By company size (small / medium / large): daily agent use 65% / 67% / 66%; GitHub Copilot as most used tool 8% / 12% / 20%; Claude Code 33% / 33% / 29%; organisation pays for Claude Code 53% / 66% / 69%; layoffs at employers in the past two years 39% / 48% / 57%; company cut headcount because of AI 22% / 23% / 26%; always reviews agent code 41% / 43% / 47%; AI pull request takes more effort 34% / 38% / 41%. Use does not vary with size; tool choice, who pays and review discipline do.

### Corrections to the earlier notes

- `gaps_benchmarks.md` line 99 quotes the JetBrains blog: "90% of professional developers were using AI coding agents at work at least weekly ... with 68% using them daily". In the raw file: 88% weekly and 64% daily among employed respondents who answered the AI block; 81% and 59% of all employed respondents. The blog's figures are a little higher and its base ("more than 15,000 professional developers") is a subset that cannot be identified in the file. Use "almost nine in ten weekly, about two thirds daily, among developers who use AI at work".
- Tool shares in the same line are reproduced: Claude Code 39%, Copilot 20% (blog 21%), Codex 16%, Cursor 12%. These are shares of respondents who named at least one work tool, not of all developers.
- Line 100: the blog's "about 47% fully agent-generated, 38% with AI assistance, 27% manual (... sums to 112%)". The file confirms that the three shares are asked separately and do not sum to 100. Midpoint means from the banded answers are about 50%, 44% and 29% weighted, or 47%, 45% and 31% unweighted, so the blog's means cannot be reproduced exactly but are of the right size. "One in five writes literally zero code without AI help" is 21% weighted and 16% unweighted.
- Line 100: "Readiness to delegate application logic rose ... to 50% (2026); code review ... to 43%". The file gives 44% (36% unweighted) for application logic and 42% (37%) for code review across all who answered; among senior respondents 51% and 45%. The blog's 50% probably uses a professional-only base.
- `benchmarks_vs_reality.md` line 99 and `gaps_benchmarks.md` line 132 ("JetBrains 2026 headline AI figures were not found", "main report" not retrieved): the raw data are now read, which supersedes the report.
- `gaps_economics_analysts.md` line 128 (no developer survey with a per-developer cost figure): still open. JetBrains asks who pays, not how much; salary answers are withheld from the public file.
- `benchmarks_vs_reality.md` line 89 (JetBrains, April 2026: over 80% say AI increased their productivity): the survey's nearest items are 72% "developer productivity improved" over the past year and 71% naming "increased productivity" as a benefit.

### Limits

- Non-probability sample of a tool vendor's audience; JetBrains says so itself (section 6). People who dislike AI tools or JetBrains are less likely to be in it.
- Weighting moves the result. China goes from 4.7% of rows to 20% of the weight and Europe from 37% to 19%, and Chinese respondents answer far more positively on every attitude item. Weighted global figures on trust, delegation and "better than my own code" are 5 to 8 points above unweighted ones, and one weighted Chinese respondent counts for about nine European ones. For an audience in Europe or Russia the European column is the more relevant benchmark than the global average.
- Routing means that most AI questions were answered only by people who already use AI at work, and agent-specific questions only by agent users (n about 16,200). "88% use agents weekly" is not a share of all developers; "43% always review" is a share of agent users.
- All quantities are self-reports: share of code, share rewritten, time spent reviewing. The share-of-code items are banded and overlapping.
- The file has 28,941 rows against 22,082 "complete responses after filtering" on the poster; the archive had no README. Weighted results match the poster's published figures exactly, so the weights are applied as intended, but the composition of the extra rows is unknown.
- Russia: 58 respondents. No usable Russian estimate exists in this dataset.
- One table (`dx_ai_effect_on_productivity`, effect of AI tools on company metrics) is coded 1 to 5 without labels in the codebook and was left out.

## 8. Numbers and series suited to report-style charts

1. McKinsey, software engineering headcount, expectation against outcome (Exhibit 17, `[P, chart]`): expected a decrease in 2025 31%; reported a decrease in 2026 22%; expect a decrease for the next year 36%. Companion bars for increases: 21%, 11%, 13%. Three paired bars. All-functions version (Exhibit 16): 32%, 14%, 39%.
2. McKinsey, coding agents by firm size (Exhibit 3): at least scaling 17% under $1bn against 31% at $1bn and above; piloting 15% against 16%; experimenting 21% against 21%; not at all 40% against 21%. Two stacked bars.
3. McKinsey, "skipped a software purchase because we could build it with coding agents" by industry (Exhibit 4, `[P, chart]`): technology 41, healthcare 39, professional services 38, energy and materials 38, financial institutions 36, media and telecom 34, pharma 33, travel and logistics 31, consumer 29, engineering and construction 28, advanced manufacturing 27, insurance 19, public sector 17; total 32. Sorted horizontal bars.
4. DORA sample calculator, where the 39% comes from (appendix): value $11.0m time saved, $0.99m extra features, -$0.34m downtime; investment $4.8m training, $3.3m J-curve dip, $0.165m licences and tokens, $0.1m infrastructure. Waterfall. Optional sensitivity line (own arithmetic): ROI 39% at 12.5% time saved, 13% at 10%, 0% at about 8.8%, -40% at 5%.
5. Sonar, use against rated effectiveness (p. 7): new code 90 / 55; explaining code 78 / 66; changing existing code 76 / 42; tests 75 / 59; documentation 74 / 74; refactoring 72 / 43; debugging 65 / 44; code review 55 / 47. Dumbbell chart, "used by" against "rated very effective".
6. Sonar, the trust question behind the "96%" headline (p. 9), next to the checking question (p. 10). "I trust that AI code is functionally correct": 4 / 25 / 23 / 31 / 17 (completely agree to completely disagree). "I always check ... before committing": 48 / 27 / 11 / 11 / 3. Two diverging stacked bars.
7. Freelance demand after generative AI, Demirci et al. (Tables 2 and 4): writing -30.4%; software, app and web development -20.6%; graphic design -18.5%; 3D modelling -15.5%; engineering -10.4%; relative to manual-intensive jobs, to July 2023. Bar chart. Footnote: remaining posts +5.7% budget, +8.6% bids, +2.2% complexity.
8. Freelancer outcomes, Hui et al. (Table 2): writing, jobs -2.0%, earnings -5.2%, probability of working in a month -10%; image work, jobs -2.1%, earnings -5.2%. Small bar chart, shown separately from chart 7 because the unit differs (per freelancer, not posts).
9. JetBrains 2026, modes of AI assistance at work, share using each at least weekly and daily (n about 19,930): chat 83 / 49; completion 79 / 56; IDE agents 78 / 51; CLI agents 74 / 48; remote cloud agents 42 / 21. Grouped bars.
10. JetBrains 2026, use against trust in one sample: use an agent daily 64%; at least 61% of code fully by agents 43%; mostly or fully trust agent output 45%; always review agent code 43%; say AI pull requests take more review effort 37%; name "more time spent reviewing" as a new friction 55%; sense of code ownership decreased 46%. Horizontal bars with the question wording as labels.
11. JetBrains 2026, delegation ladder (n about 5,360), delegate / keep: boilerplate 75 / 10; tests 68 / 14; checking for issues 60 / 21; prototyping 60 / 19; refactoring 55 / 20; understanding recent changes 50 / 33; debugging 45 / 33; application logic 44 / 32; code review 42 / 35. Diverging bars.
12. JetBrains 2026, same questions by region (Europe / North America / India / China): daily agent use 58 / 54 / 67 / 81; trust agent output 34 / 38 / 43 / 60; always review 52 / 50 / 48 / 28; agent better than own code 37 / 43 / 64 / 66; core skills improved 60 / 55 / 75 / 94. Small multiples; makes the weighting caveat visible.
13. JetBrains 2026, juniors against seniors: daily agent use 58 / 69; agent better than own code 59 / 50; AI pull request takes more effort 31 / 41; job market very challenging 34 / 26; anxious about replacement often or always 32 / 25. Slope or paired bars.
14. JetBrains 2026, job market mood (n about 9,900): job market challenging 58%, favourable 18%; feels secure in the job 56%, insecure 18%; company cut headcount because of AI 23% yes, 56% no; "AI will fully replace developers" 22% agree, 47% disagree; "AI will decrease demand for developers" 38% agree, 32% disagree; studying computer science worth it 71%. Paired bars.

# Analyst positions, adoption data and the hype/S-curve placement of agentic AI (as of 2026-11-17)

Reading notes for the report writer.

- Verification labels used below: **[P]** = read on the publisher's own page or document; **[S]** = secondary coverage or search snippet only, not checked against the primary; **[M]** = mirror of the publisher's press release.
- gartner.com and mckinsey.com blocked the normal fetch; the two Gartner articles and the McKinsey survey page were read through the browser scraper (public pages, no login). The McKinsey page ends in a registration wall, so only the public part was read.
- The web search budget for the session ran out before four planned checks (see Gaps in each section). Nothing was filled in from memory without being marked as such.
- Self-interest key: **consultancy** (sells transformation work, has an incentive to show both a large prize and a large gap that needs help), **advisory analyst** (sells subscriptions and conferences to buyers and vendors), **vendor**, **asset manager / bank** (talks its book), **public statistics**, **academic / non-profit**.

## 1. Gartner: Hype Cycle placement and dated predictions

### Takeaway
Gartner has kept AI agents at the Peak of Inflated Expectations for two consecutive years (2025 and 2026) and in 2026 gave agentic AI its own Hype Cycle. Its headline numbers are a deliberate pair: only 17% of organizations have deployed agents, more than 60% plan to within two years, and more than 40% of agentic projects are expected to be cancelled by end of 2027.

### Cited Findings
- 2026 Hype Cycle for Agentic AI (first edition, 2026): "Agentic AI sits at the Peak of Inflated Expectations". According to the 2026 Gartner CIO and Technology Executive Survey, "only 17% of organizations have deployed AI agents to date, yet more than 60% expect to do so within the next two years — the most aggressive adoption curve among all emerging technologies measured in the survey". [P] ([Gartner, Hype Cycle for Agentic AI article](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai)). Publisher: advisory analyst. Exact publication date not shown on the page; sample size of the CIO survey not stated there.
- Same article: "most deployments remain narrowly scoped, and fully autonomous agents are not ready for the majority of enterprise use cases". Governance, security and "FinOps for agentic AI" appear as separate profiles on the curve. [P] ([Gartner](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai))
- 2026 Hype Cycle for Artificial Intelligence, titled "Puts Control Ahead of Capability": "the defining question of 2026 has shifted from whether an enterprise can build with AI to whether it can account for what its AI is doing and what it costs" (Haritha Khandabattu, VP Analyst). "Concerns about GenAI have shifted from model capability to application reliability and return on investment." It repeats the 17% / 60% pair and restates the cancellation forecast: "more than 40% of agentic AI projects to be cancelled by the end of 2027 because of cost, unclear value or inadequate risk controls". [P] ([Gartner, Hype Cycle for AI article](https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence)). The curve itself is an image: [2026 Hype Cycle graphic](https://emt.gartnerweb.com/ngw/globalassets/en/information-technology/infographics/2026-hype-cycle-for-artificial-intelligence.webp) (not read; positions of individual profiles other than those named in the text are unverified).
- 2025 Hype Cycle for Artificial Intelligence (press release 2025-08-05): AI agents and AI-ready data are "the two fastest advancing technologies", "placing them at the Peak of Inflated Expectations"; multimodal AI and AI TRiSM also "dominating the Peak"; the release describes "a gradual pivot from generative AI (GenAI) as a central focus". [M] ([press release mirror, silicon.co.uk](https://www.silicon.co.uk/press-release/gartner-hype-cycle-identifies-top-ai-innovations-in-2025)); original: [Gartner newsroom 2025-08-05](https://www.gartner.com/en/newsroom/press-releases/2025-08-05-gartner-hype-cycle-identifies-top-ai-innovations-in-2025) (blocked to fetch).
- Prediction, 2025-06-25: "Over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value or inadequate risk controls". Same release: "agent washing" is the rebranding of existing assistants, RPA and chatbots; "Gartner estimates only about 130 of the thousands of agentic AI vendors are real"; a January 2025 poll of 3,412 webinar attendees found 19% had made significant investments in agentic AI and 42% conservative ones; "at least 15% of day-to-day work decisions will be made autonomously through agentic AI by 2028, up from 0% in 2024". [S, snippets of the Gartner release] ([Gartner newsroom 2025-06-25](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)). Note: a webinar poll is a self-selected sample, not a representative survey.
- Prediction, 2025-08-26: "Forty percent of enterprise applications will be integrated with task-specific AI agents by the end of 2026, up from less than 5% today". [S, snippet of the Gartner release] ([Gartner newsroom 2025-08-26](https://gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025))
- Prediction, 2026-03-17: at least 80% of governments will deploy AI agents to automate routine decision-making by 2028. [S, headline only] ([Gartner newsroom 2026-03-17](https://gartner.com/en/newsroom/press-releases/2026-03-17-gartner-predicts-at-least-80-percent-of-governments-will-deploy-ai-agents-to-automate-routine-decision-making-by-2028))
- Related 2026 document: "Hype Cycle for Employee Adoption of AI Agents, 2026", dated 2026-07-29, abstract only. [S] ([Gartner document 8191929](https://www.gartner.com/en/documents/8191929))

### Inferences
- Two years at the Peak without a slide into the Trough is itself a talking point: Gartner's 2026 text has moved from capability to cost, governance and observability, which is the vocabulary that normally precedes the Trough.
- The cancellation forecast was not revised between June 2025 and the 2026 Hype Cycle text; it was restated word for word. I found no evidence of a Gartner revision of the 40% figure.
- The "40% of enterprise apps by end of 2026" forecast (an application-side, vendor-shipped metric) and the "17% of organizations have deployed agents" survey result (a buyer-side metric) are not comparable, but together they suggest vendors embedded agents faster than customers put them to work. That fits the "agent washing" warning.

### Gaps
- Could not confirm from a primary source where generative AI itself sat in 2025 and 2026. Secondary coverage of the 2025 cycle disagrees (already in the Trough of Disillusionment versus approaching it).
- Commonly cited Gartner figures that I could not verify in this session and that are given here from memory only: "33% of enterprise software applications will include agentic AI by 2028, up from less than 1% in 2024" (same June 2025 release, I believe); "agentic AI will autonomously resolve 80% of common customer service issues by 2029" (March 2025); "at least 30% of GenAI projects will be abandoned after proof of concept by end of 2025" (July 2024). Verify before use.
- No Gartner outcome data yet on how many agentic projects were actually cancelled; the 2027 deadline has not arrived.
- Time-to-plateau labels for AI agents (2 to 5 years or 5 to 10 years) are in the paywalled report, not on the public page.

## 2. Consultancies and advisory firms: adoption, scaling, EBIT impact

### Takeaway
The consultancies agree on the shape: use is near-universal, scaling of agents is real but concentrated in large firms, and enterprise-level profit impact has not moved. McKinsey's 2026 survey is the cleanest statement: agents scaling at 40% of large firms (27% a year earlier), EBIT impact flat at 37% of respondents, high performers flat at 6%.

### Cited Findings
McKinsey, "The state of AI in 2026: On the road to ROI" (tenth annual survey; fielded 2026-05-04 to 2026-06-08; 1,719 participants, 97 nations; 36% from firms above $1bn revenue; weighted by national GDP; self-reported). Publisher: consultancy. [P] ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)); press coverage dated September 2026 ([FM Magazine](https://www.fm-magazine.com/news/2026/sep/companies-financial-value-from-ai-holds-firm-in-2026/)).
- Scaling AI agents in one or more functions: large organizations 27% (2025) to 40% (2026); smaller organizations flat at 22%.
- Scaling AI across the enterprise: 38% (2025) to 44% (2026); 54% of large firms versus one third of smaller ones. AI used in three or more functions: 51% to 56%. "Nearly nine in ten" report regular use in at least one function.
- By tool, share scaling across the enterprise: chatbots 47%; AI agents about two in ten; software coding agents about two in ten (31% at larger enterprises).
- EBIT: 37% attribute at least some EBIT impact to AI, "essentially unchanged from 2025". High performers (at least 5% of EBIT from AI and "significant" value) "about 6 percent", unchanged from 2025.
- Individual level: 80% say AI improved their own productivity; 50% say it helps them make better decisions.
- Build versus buy: 32% say their organization decided against buying at least one software product or feature because it could be built in-house with agentic coding tools (nearly half among high performers, 31% among others).
- Cost: about 20% say AI operating costs, including tokens, constrained their use; 28% spend more than 10% of the ICT budget on AI; 60% expect to increase AI investment next year.
- Workforce: 39% expect AI-related headcount declines next year (32% in 2025; 43% expect no change). Only 14% report an actual AI-related decline over the past year, "less than half the 32 percent who, in last year's survey, expected workforce reductions". Two thirds report little or no change.
- High performers: nearly three quarters redesigned workflows (55% in 2025) versus one quarter of others; more than three times as likely to be scaling agents in most functions.

BCG. Publisher: consultancy.
- AI Radar 2026 (press release 2026-01-15; 2,360 executives, 16 markets, 640 CEOs): companies plan to double AI spending in 2026 to about 1.7% of revenues; "about 90% of CEOs expect AI agents to produce measurable returns in 2026"; more than 30% of AI investment committed to agentic AI; 94% will keep investing even without payoff in the next year; 72% of CEOs say they are the main AI decision makers; half believe their job depends on AI paying off. CEO confidence that AI will pay off: about three quarters in India and Greater China, 61% Europe, 52% US, 44% UK. [P] ([BCG press release](https://www.bcg.com/press/15january2026-as-ai-investments-surge-ceos-take-lead))
- Applied AI Index 2026 (press release 2026-09-30; 1,330 executives; 41 indicators): maturity stages 2025 to 2026: "stagnant" 14% to 4.5%, "expanding" 35% to 41%, "advanced" 5% to 7.5%; the top two stages together are "about half". Advanced firms versus laggards: 2.4x revenue growth, 2.3x three-year TSR, 2.8x EBITDA growth. Agents' share of AI-created value: 22% in 2026, expected 39% in 2030. 42% expect to give agents substantial autonomy by 2030; only 5% have all needed controls in place. [P, Japanese-language version of the release] ([BCG press release](https://www.bcg.com/ja-jp/press/30september2026-ai-starting-to-pay-off-companies-generate-value))
- Earlier BCG figure (2025-10): agentic systems about 17% of total AI value in 2025, expected 29% by 2028. [S] ([Creamer Media summary](https://newsletter.en.creamermedia.com/article/agentic-ai-systems-account-for-17-of-total-ai-value-this-year-bcg-2025-10-02))

Deloitte, State of AI in the Enterprise 2026 (3,500 senior leaders; field dates not on the page). Publisher: consultancy / audit firm.
- 28% report revenue gains from AI, up from 20% in January (of the same year's wave); 81% say AI improved decision and execution speed but only 25% are "deeply transforming the business"; 40% allow AI to execute decisions or actions without human approval at least moderately; for 23% accountability for a negative AI outcome is unclear; 71% track total inference and API spend, only 44% track per-unit inference cost. [P] ([Deloitte](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html))
- Agentic-specific figures attributed to Deloitte in roundups: 23% use agentic AI at least moderately today, 74% expect to within two years, only about 20% have a mature governance model for agents. [S] ([Techstrong summary](https://techstrong.ai/articles/deloitte-enterprises-face-major-readiness-gap-for-agentic-ai/); [Deloitte press room](https://www.deloitte.com/us/en/about/press-room/deloitte-survey-examines-ai-readiness-agentic-ai-success.html))

Forrester, "The State of Agentic AI, 2026: Companies Are Chasing, Few Are Catching" (blog 2026-06-03; Hopkins, Le Clair, Pollard, Curran, Joseph). Publisher: advisory analyst.
- "Three-quarters of enterprise leaders tell us they're adopting agentic AI"; "Only a small minority have it running in meaningful production". Forrester Security Survey 2026: "49% of security decision-makers named agentic AI as a concern". No sample size given in the blog. [P] ([Forrester](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/))

IDC and Capgemini (secondary only).
- IDC FutureScape 2026: agentic AI to reach 26% of worldwide IT spending, $1.3 trillion, by 2029. [S] ([Joget roundup](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/)). Publisher of the original: advisory analyst; the roundup is a vendor blog.
- Capgemini: 82% of firms plan agent integration by 2027. [S, vendor compilation] ([Joget roundup](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/))

### Inferences
- The same pattern appears in three independent surveys: wide use, modest "deployed/scaled" share, flat profit attribution. Deployed-agent estimates cluster by definition: Gartner 17% deployed (organizations), McKinsey about 20% scaling agents (respondents, 40% for large firms), Deloitte 23% at least moderate use.
- The individual-versus-enterprise gap (80% personal productivity gain, 37% EBIT attribution, flat) is the 2026 form of McKinsey's earlier "gen AI paradox" and is the most defensible single slide for a sober view.
- BCG's January CEO expectation (about 90% expect measurable agent returns in 2026) can be set against McKinsey's mid-2026 result (EBIT attribution unchanged). This is an expectation-versus-outcome pair inside one year, though from different samples.
- All of these are self-reported executive surveys, weighted toward large firms, published by firms that sell AI transformation. The "high performer / future-built" framing (6% at McKinsey, 7.5% "advanced" at BCG) doubles as a sales argument.

### Gaps
- McKinsey 2025 publications named in the brief ("Seizing the agentic AI advantage" with the "gen AI paradox", "The agentic organization") were not re-fetched; the 2026 survey carries the same argument with newer numbers. The 2025 survey values used above are those quoted as comparisons inside the 2026 report.
- Bain, Accenture: nothing retrieved. Capgemini's reported decline in trust in fully autonomous agents (2025) could not be confirmed. IDC and Capgemini numbers above are secondary.
- BCG "AI at Work" 2026 edition: not found.
- Exact publication date of the McKinsey 2026 report is not on the scraped page (press coverage is from September 2026).

## 3. Sceptical data: failure rates, adoption statistics, agents on real tasks

### Takeaway
The widely quoted failure numbers are weaker than their fame: the "95%" comes from a small non-probability study with a strict definition, and RAND's "80%" is a quotation of a 2022 magazine article. The solid sceptical evidence is official statistics (US Census: about 20% of firms use AI in any function, flat from December 2025 to May 2026) and task benchmarks, although the benchmarks have moved fast in 2026.

### Cited Findings
MIT Project NANDA, "The GenAI Divide: State of AI in Business 2025" (v0.1, July 2025; authors Aditya Challapally and others; reviewer Pradyumna Chari, Project NANDA). Publisher: academic-affiliated project that itself promotes an agent infrastructure, so not disinterested.
- Method as stated: "a systematic review of over 300 publicly disclosed AI initiatives, structured interviews with representatives from 52 organizations, and survey responses from 153 senior leaders collected across four major industry conferences"; research period January to June 2025. [P, PDF converted] ([report PDF](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf))
- Claim: "Despite $30–40 billion in enterprise investment into GenAI ... 95% of organizations are getting zero return. ... Just 5% of integrated AI pilots are extracting millions in value, while the vast majority remain stuck with no measurable P&L impact." [P] (same PDF)
- Less quoted lines from the same report: generic LLM chatbots show pilot-to-implementation of about 83%; "only 5% of custom enterprise AI tools reach production"; external partnerships reached deployment about 67% of the time versus about 33% for internal builds; "only 40% of companies say they purchased an official LLM subscription, workers from over 90% of the companies we surveyed reported regular use of personal AI tools" (shadow AI); the report's own limitation note: "These figures are directionally accurate based on individual interviews rather than official company reporting"; success measured as deployment beyond pilot with measurable KPIs, "ROI impact measured 6 months post-pilot". [P] (same PDF)
- Criticism: small conference-based sample, anonymous firms, six-month P&L window, and a definition that counts productivity gains without P&L effect as "zero return"; some critics call it marketing for NANDA's own approach, one analysis rates the method sound but limited. [S, blogs and trade press, not peer-reviewed] ([Pure AI, 2025-09-23](https://pureai.com/articles/2025/09/23/most-genai-investments-fail.aspx); [arnon.dk](https://arnon.dk/mits-95-ai-failure-rate-is-wrong/); [CustomerThink](https://customerthink.com/the-great-genai-divide-debunking-the-myth-of-95-failure/))

S&P Global Market Intelligence (2025 survey, more than 1,000 respondents in North America and Europe). Publisher: data and ratings company, sells research.
- Share of companies abandoning most of their AI initiatives: 17% (2024) to 42% (2025); on average 46% of AI proofs of concept scrapped before production. [S, trade press reporting the survey] ([Construction Dive / CIO Dive, 2025-03-19](https://www.constructiondive.com/news/AI-project-fail-data-SPGlobal/742934/))

RAND, "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed" (RR-A2680-1, 2024-08-13; Ryseff, De Bruhl, Newberry; 65 interviews with data scientists and ML engineers, August to December 2023). Publisher: non-profit research institute. Older item, pre-agent.
- Wording: "By some estimates, more than 80 percent of AI projects fail". This is not RAND's finding; the footnote cites a Fortune article of 2022-07-26, and the "twice the rate of non-AI IT projects" line cites Harvard Business Review, Nov-Dec 2023. Root causes named: leadership misunderstanding the problem, inadequate data, technology-first focus, weak infrastructure, problems beyond current capability. [P] ([RAND](https://www.rand.org/pubs/research_reports/RRA2680-1.html))

US Census Bureau, Business Trends and Outlook Survey (BTOS; biweekly; about 200,000 of 1.2 million sampled firms per wave; asks about use in the last two weeks). Publisher: public statistics.
- December 2025 to May 2026: national AI use "between roughly 17% and 20%", 19.8% as of 2026-05-03; 20% to 23% expect use within six months; 250+ employees 37%, 100 to 249 employees 32%, firms with four or fewer under 20%; Information 39.7%, Finance and Insurance 33.9%, Retail about 14%. Use rose among firms with 20+ employees, no significant change below 20. [P] ([Census, 2026-05-26](https://census.gov/library/stories/2026/05/ai-use-businesses.html))
- Series break: until 2025-11-17 the question was AI use "in producing goods or services"; from the next wave "in any of its business functions". The Fed notes the old series was near 10% before the change and the new series about 18% at end of 2025; under the old wording adoption grew 68% (3.9 points) in the year to September 2025, with slowing in Q2 2025. [P] ([Federal Reserve FEDS Note, J. Allen, 2026-04-03](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html)). Publisher: central bank staff, views of the author.
- Same Fed note, other surveys: Atlanta Fed SBU (November 2025, 1,032 responses): 78% of the labour force works at firms using AI (54% for LLMs). Real-Time Population Survey (November 2025, 5,000 to 6,000 responses): 40.7% of workers use generative AI for work, up 9.7 points in a year; daily work use 12%. Gallup mid-2025: 8% daily. The note concludes that intensity lags breadth and that the 18% (firms) versus 78% (workforce) gap is mostly a unit-of-analysis effect. [P] ([FEDS Note](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html))
- Later 2026 values by firm size, six-survey trailing average, October 2026 release (reference date 2026-10-04): 250+ employees 40.7%; 100 to 249: 33.5%; 50 to 99: 27.9%; 20 to 49: 23.8%; 10 to 19: 22.1%; 5 to 9: 21.1%; 1 to 4: 23.3%. For the largest firms: about 12% in September 2025 (old wording), about 30% by February 2026 and about 40% by October 2026 (new wording). The post also reports a second wording change from the 2026-10-19 collection, attributed by the BTOS "about" page to an executive order of September 2026, which is a second series break. [S, a practitioner's reanalysis of the Census download; the wording-change details were not checked against census.gov] ([Simon Willison, 2026-11-02](https://simonwillison.net/2026/nov/2/census-bureau-super-intelligence))

Apollo (Torsten Slok, chief economist). Publisher: asset manager.
- 2025-11-28: "Data from the Census Bureau and Ramp shows that AI adoption rates are starting to flatten out across all firm sizes" (six-survey moving average; Ramp AI Index covers 40,000+ US businesses' card and invoice spend). [P] ([Apollo Academy](https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/)). An earlier September 2025 Apollo chart claimed adoption was trending down for large companies ([Apollo Academy](https://www.apolloacademy.com/ai-adoption-rate-trending-down-for-large-companies/), linked from the Willison post, not fetched).
- Slok, February 2026: "AI is everywhere except in the incoming macroeconomic data." [P for the quotation in Fortune] ([Fortune, 2026-02-15](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/))

Agents on realistic work tasks. Publishers: academic (CMU), non-profit with a data-labelling vendor (CAIS and Scale AI).
- TheAgentCompany (arXiv 2412.14161; v1 2024-12-18, v3 2025-09-10; simulated software company): "the most competitive agent can complete 30% of tasks autonomously". [P, abstract] ([arXiv](https://arxiv.org/abs/2412.14161)). No 2026 leaderboard update found.
- Remote Labor Index (240 real paid freelance projects, 230 private; a deliverable counts only if judged acceptable to a client). At launch (October 2025) the best agent, Manus, reached 2.5%. Current leaderboard (no date on page): top entry 41.25%, next 21.25% and 20.83%; late-2025 models sit at 1.25% to 3.75%. No confidence intervals shown. [P] ([Scale Labs RLI leaderboard](https://labs.scale.com/leaderboard/rli); launch paper [arXiv 2510.26787](https://arxiv.org/html/2510.26787v1))
- Stanford AI Index 2026 (2026-04-13): agent success on Terminal-Bench rose from 20% (2025) to 77.3%; agents solved 93% of cybersecurity problems, up from 15% in 2024; robots succeed at only 12% of real household tasks; models still lag on multi-step planning and financial analysis. [P, HAI summary] ([Stanford HAI, 12 takeaways](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)). Publisher: academic.

### Inferences
- A sober talk should not lean on "95% fail" or "80% fail". Both are quotable only with their caveats; the NANDA report's own internal contrast (83% for generic chatbots, 5% for custom tools, 67% versus 33% for buy versus build) is more informative than its headline.
- The Apollo "plateau" story of autumn 2025 did not survive: part of it was the narrow old question, and on the new question large-firm use rose from about 30% to about 40% during 2026. The national rate was nevertheless flat for the six months to May 2026, so diffusion among small firms is slow.
- Benchmarks of realistic paid work went from "agents fail almost everything" (2.5%, October 2025) to roughly 20% to 40% within about a year. The sceptical reading that held in 2025 is dated; the remaining honest caveat is that most projects still fail and that benchmark success is not deployment.
- Three adoption numbers that look contradictory are consistent once the unit is named: about 20% of firms (Census, any use in two weeks), about 41% of workers (RPS), 78% of the workforce employed at a firm that uses AI (Atlanta Fed).

### Gaps
- S&P Global's primary release was not read; figures are via CIO Dive. No 2026 update of the S&P abandonment series was found.
- No 2026 follow-up to the NANDA report was found. No peer-reviewed critique of it was found, only blogs and trade press.
- METR's 2025 randomized trial (16 experienced open-source developers, 246 tasks, 19% slower with AI tools; [arXiv:2507.09089](https://arxiv.org/abs/2507.09089)) is confirmed, but a 2026 follow-up could not be searched after the budget ran out.
- Goldman Sachs and other bank notes on an adoption plateau: not retrieved.
- The Census wording change of October 2026 is reported from one secondary source; check census.gov/hfp/btos before putting it on a slide.

## 4. Macro estimates: productivity and GDP

### Takeaway
Published estimates span more than two orders of magnitude, from Acemoglu's roughly 0.7% total over ten years to scenario models with double-digit annual growth, and they are not expressed in the same metric. Realized macro evidence by late 2026 is one contested data point: Brynjolfsson's estimate of about 2.7% US productivity growth in 2025.

### Cited Findings
- Range as compiled in May 2026: McKinsey (2023) about 0.1 points of added annual GDP growth at the low end; Goldman Sachs (2023) +1.5 points annual productivity growth over 10 years; OECD (2024) just above 0.5; Acemoglu (2024) +0.71% US productivity over 10 years in total, with only about 5% of output AI-exposed; Korinek and Suh (2024) scenario with 18% annual growth; Epoch AI GATE (2025) conditional scenario with GDP growth of 2% in year 1, 8% in year 5, 25% in year 10. The author estimates the spread between forecasts approaches $1 quadrillion by 2035. [S, a compilation by a RAND research associate writing as a guest] ([AI Frontiers, A. Shenk, 2026-05-11](https://ai-frontiers.org/articles/the-quadrillion-dollar-disagreement-on-ai-and-the-economy)). Publisher: policy commentary outlet.
- Same article, realized indicators: no clear inflection in patents per researcher, drug approval timelines not shortened; historical lags quoted as about 40 years for electrification and about 20 for computerization. [S] ([AI Frontiers](https://ai-frontiers.org/articles/the-quadrillion-dollar-disagreement-on-ai-and-the-economy))
- Brynjolfsson (Stanford), FT op-ed "The AI productivity take-off is finally visible", February 2026: his own estimate of US productivity growth of about 2.7% in 2025 against a 1.4% average over the previous decade, after the benchmark revision cut 2025 job gains from 584,000 to 181,000; the economy is "transitioning out of this investment phase into a harvest phase"; he adds that "several more periods of sustained growth" are needed. [P for Fortune's report of the op-ed] ([Fortune, 2026-02-15](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/)). Publisher of the claim: academic, also a co-founder of an AI workforce company (worth a neutral mention).
- Counter-voices in the same piece: Slok (Apollo): "Maybe there is a J-curve effect for AI, where it takes time for AI to show up in the macro data. Maybe not"; S&P 500 margins outside the "Magnificent 7" show no effect. Stephen Brown (Capital Economics): "All this implies that AI is making a large contribution to productivity growth." [P] ([Fortune](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/))
- Stanford AI Index 2026: global corporate AI investment $581.7bn in 2025 (+130%); private investment $344.7bn (+127.5%); US $285.9bn versus China $12.4bn; generative AI reached 53% population adoption within three years, faster than the PC or the internet, with the US ranked 24th at 28.3%; estimated consumer value of generative AI tools in the US $172bn a year by early 2026; employment of software developers aged 22 to 25 down nearly 20% since 2024 while older cohorts grew; AI data centre power capacity 29.6 GW. [P, HAI summary] ([Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report))
- Productivity micro-evidence reported from the AI Index: gains of 14% to 26% in customer support and software development, weaker or negative where more judgment is needed. [S] (coverage of the AI Index, e.g. [MIT Technology Review, 2026-04-13](https://www.technologyreview.com/2026/04/13/1135675/want-to-understand-the-current-state-of-ai-check-out-these-charts/); the specific figures were seen only in search summaries)
- OECD (2025 paper, as summarized): AI adds 0.4 to 1.3 points to annual US productivity growth and 0.2 to 0.8 points in other advanced economies over 10 years. IMF (2026 working paper, as summarized): 0.8% to 1.2% labour productivity effect, estimated from AI patent data for 2000 to 2017, so not a measure of generative AI. [S, search summary; primary documents not opened] (overview: [CEPR VoxEU, "Miracle or myth?"](https://cepr.org/voxeu/columns/miracle-or-myth-assessing-macroeconomic-productivity-gains-artificial-intelligence))

### Inferences
- The numbers must not be put on one axis without relabelling: Acemoglu is a cumulative TFP level over ten years (about 0.07 points a year), Goldman and OECD are annual growth increments, Goldman's "7%" is a GDP level. Converted to annual terms, the mainstream institutional range is roughly 0.1 to 1.5 points a year; the transformative scenarios sit outside it by an order of magnitude.
- Investment has clearly moved (corporate AI investment more than doubled in 2025) while attributable output has not yet been measured. That is the precondition of both the bubble story and the J-curve story; the data do not yet discriminate between them.
- The clearest labour-market signal is compositional (young developers down nearly 20%), not aggregate.

### Gaps
- Goldman Sachs "7% of global GDP, about $7 trillion" (2023) and a reported statement by Goldman's chief economist that AI investment added "basically zero" to US GDP growth in 2025 appeared only in a search summary without a traceable URL. Not verified.
- Morgan Stanley estimates: nothing retrieved.
- Acemoglu's NBER abstract (w32487, May 2024) gives "no more than a 0.66% increase in total factor productivity (TFP) over 10 years" ([NBER](https://www.nber.org/papers/w32487)); the 0.71% in the AI Frontiers table is not in the abstract and its origin was not traced.
- IMF and OECD primaries not opened; ranges are from summaries. The AI Frontiers table gives OECD "just above 0.5", the search summary gives 0.4 to 1.3 points for the US: probably different OECD papers (2024 versus 2025).
- No official 2026 US productivity release was checked, so it is unknown whether Brynjolfsson's 2.7% held through later revisions.

## 5. S-curve evidence: is capability still accelerating or flattening?

### Takeaway
On the measured indicators capability has not flattened; it sped up around 2024 with reasoning models, and METR's task-horizon doubling time shortened from about 7 months to about 3 to 4 months. The strongest counter-argument is not that progress stopped but that the measuring instruments are saturating and are concentrated in code and mathematics, where answers can be checked automatically.

### Cited Findings
Acceleration side.
- METR Time Horizon 1.1 (2026-01-29). 50% time-horizon doubling time: full 2019+ trend 196.5 days (about 7 months; TH1.0: 195.8 days, CI 162 to 223); 2023+ trend 130.8 days (CI 107 to 161; TH1.0: 165.3); 2024+ trend 88.6 days (TH1.0: 108.9). Publisher: non-profit evaluator, funded partly through work with AI labs. [P] ([METR TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1))
- TH1.1 point estimates of the 50% time horizon in minutes (95% CI): GPT-4 0314: 3.5 (1.6 to 6.9); GPT-4 1106: 3.6; Claude 3.7 Sonnet: 60 (32 to 106); Claude Opus 4: 101; o3: 121; GPT-5: 214 (117 to 480); Claude Opus 4.5: 320 (170 to 729). [P] ([METR TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1))
- Later 2026 points: Claude Opus 4.6 about 14.5 hours [S] ([OfficeChai](https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark)); an early Claude Mythos Preview snapshot, tested March 2026: "at least 16 hours", 95% CI 8.5 to 55 hours, "at the upper end of what we can measure without new tasks"; only five of 228 tasks are 16 hours or longer. [S, trade press quoting METR] ([The Decoder, 2026-05-10](https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/))
- METR's tracking page: last model added 2026-05-08, page updated 2026-09-08 and described as no longer actively maintained; "Measurements above 16 hrs are unreliable with our current task suite". [P] ([METR time horizons](https://metr.org/time-horizons/))
- Epoch AI, "Have AI capabilities accelerated?" (2026-04-16, Denain and Barry): three of four metrics (Epoch Capabilities Index, log METR time horizon, a combined mathematics index) show strong evidence of acceleration against a linear trend fitted from 2023; reasoning models show a one-time jump and a trend roughly 2 to 3 times faster than non-reasoning models; the break is around 2024. Publisher: non-profit research organisation, funded largely by philanthropy and some lab contracts. [P] ([Epoch AI](https://epoch.ai/blog/have-ai-capabilities-accelerated))
- Epoch data insight: the ECI frontier has advanced about 14 points a year since the first reasoning models (September 2024) against 6 points a year for non-reasoning models. [S, search summary of the Epoch page] ([Epoch AI, ECI frontier trend](https://epoch.ai/data-insights/eci-frontier-trend))
- Cost side: the price to reach a fixed capability level fell between 9x and 900x a year depending on the milestone; GPT-4-level performance on PhD-level science questions became 40x cheaper per year; an MMLU score of 86 cost $37.50 per million tokens in March 2023 and $0.18 in February 2025. The authors doubt the fastest rates will persist. [P] ([Epoch AI, LLM inference price trends, 2025-03-12](https://epoch.ai/data-insights/llm-inference-price-trends)). Older item (March 2025); Epoch published "The plunging price of thought" on 2026-09-22, not read.

Flattening or caution side.
- Epoch's own caveats: the fourth metric, WeirdML V2, shows no acceleration; the accelerating metrics "are concentrated in programming and math, where answers can be checked automatically", and the acceleration "may not generalize to tasks that are harder to verify"; several superlinear fits do equally well, so the growth rate cannot be pinned down. [P] ([Epoch AI](https://epoch.ai/blog/have-ai-capabilities-accelerated))
- METR's own caveats: the suite is mainly software engineering, ML and cybersecurity; human baselines exist for only 5 of the 31 long tasks; confidence intervals are wide (Opus 4.5: 170 to 729 minutes); the horizon is defined at 50% success, far from the reliability a business process needs; few tasks remain too hard for the newest models. [P] ([METR TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1); [METR time horizons](https://metr.org/time-horizons/))
- Unit cost falls but total cost bites: about 20% of McKinsey respondents say operating costs including tokens constrain AI use, and high performers are constrained on coding agents about three times as often as others. [P] ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)). Gartner makes compute-cost control a headline theme of its 2026 AI Hype Cycle. [P] ([Gartner](https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence))
- Capability is uneven: 77.3% on Terminal-Bench but 12% for robots on household tasks, and continuing weakness in multi-step planning and financial analysis. [P] ([Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report))
- Physical inputs are finite: AI data centre capacity 29.6 GW, comparable to New York State's peak demand; corporate AI investment $581.7bn in 2025. [P] ([Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report))

### Inferences
- There are two S-curves and they are at different points. The capability curve (what a frontier model can do in a lab) is still in its steep section on every public measure. The adoption curve (what firms have put into production and booked as profit) is early: about 17% to 23% deployed, flat EBIT attribution, about 20% of US firms using AI at all.
- "No flattening observed" is not the same as "no flattening coming": the two best trend instruments (METR's suite, older benchmarks) have hit their ceiling, so for most of 2026 the top of the curve is literally unmeasured. An honest slide shows the trend line with a shaded "instrument saturated" zone above 16 hours.
- The diminishing-returns argument is now mostly an economic one (energy, capital, token bills growing faster than unit prices fall) and a domain one (verifiable tasks race ahead, judgment-heavy and physical tasks do not), not a claim that benchmark scores stalled.

### Gaps
- No METR publication after May 2026 with a new task suite was found; whether the 2026 points keep to the 3 to 4 month doubling is not established beyond the Mythos lower bound.
- Epoch's September 2026 price report was not read, so there is no 2026 figure for price decline per year.
- No rigorous 2026 source was retrieved that argues capability is flattening; the search budget ended before this side could be searched specifically. Treat the "caution side" above as caveats from the measurers themselves, not as an independent sceptical literature.

## 6. Historical analogies used by analysts

### Takeaway
The analogy most used by economists is the Solow paradox with Brynjolfsson's productivity J-curve: investment and reorganization first, measured gains years later. Sceptics use the same history to say "maybe, maybe not", and the lags quoted for earlier general-purpose technologies are decades, not quarters.

### Cited Findings
- Solow paradox, restated for AI by Apollo's Slok: "AI is everywhere except in the incoming macroeconomic data." [P] ([Fortune, 2026-02-15](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/))
- Productivity J-curve (Brynjolfsson, Rock, Syverson, NBER w25148, 2018; older item): intangible complementary investment causes measured productivity to be understated early and overstated later. [S, summary page] ([summary of NBER w25148](https://causalclaims.trfetzer.com/paper/w25148.html)). Brynjolfsson's 2026 claim is that the US is moving from "investment phase" to "harvest phase". [P via Fortune] ([Fortune](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/))
- Empirical J-curve for industrial AI: a study on US Census manufacturing data (2017 and 2021) reports initial productivity losses followed by medium-term gains. [S, conference listing] ([SIOE 2026 programme](https://www.sioe.org/conference/2026/program/paper/2086-the-rise-of-industrial-ai-in-america-microfoundations-of-the))
- Electrification and computing: integration took about 40 years for electrification and about 20 for computerization; early PCs gave only modest aggregate gains. [S] ([AI Frontiers, 2026-05-11](https://ai-frontiers.org/articles/the-quadrillion-dollar-disagreement-on-ai-and-the-economy))
- Speed of diffusion to individuals: generative AI reached 53% population adoption in three years, "faster than the personal computer or the internet". [P] ([Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report))
- Gartner's own analogy is the Hype Cycle itself: Peak in 2025 and 2026, with cost and governance language signalling the approach of the Trough. [P] ([Gartner](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai))

### Inferences
- Individual uptake is faster than any earlier general-purpose technology while organizational redesign runs at the usual slow pace. McKinsey's finding that high performers are the ones redesigning workflows (nearly three quarters versus one quarter) is the J-curve mechanism stated in survey form.
- The dot-com analogy fits the investment pattern (capital outrunning revenue, real technology underneath) better than it fits the technology; a fair formulation is that a financial correction and a lasting technology shift are compatible, as they were in 2000 to 2002.

### Gaps
- No analyst source drawing the dot-com or cloud-adoption comparison explicitly was retrieved; the dot-com point above is an inference, not a citation.
- The original NBER J-curve paper was not opened.

## 7. Forecasts from 2023 to 2025 checked against late 2026

### Takeaway
Forecasts about capability were mostly too conservative; forecasts about business effects (returns, headcount, plateau) were mostly too strong in either direction. Several famous ones are still open because their deadlines are 2027 or later.

### Cited Findings
- Too conservative: METR's long-run 7-month doubling (the 2019+ trend, 196 days) understated the recent pace; the 2024+ trend is 88.6 days. [P] ([METR TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1))
- Overtaken: "agents complete under 3% of real freelance projects" (Remote Labor Index, October 2025, best 2.5%). The current leaderboard top is 41.25%, with two more systems near 21%. [P] ([Scale Labs RLI leaderboard](https://labs.scale.com/leaderboard/rli))
- Overstated: executives' 2025 expectation of AI-driven job cuts. 32% expected headcount declines within a year; 14% report one. Expectations for the coming year rose anyway, to 39%. [P] ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai))
- Not borne out so far: BCG's January 2026 finding that about 90% of CEOs expect measurable returns from agents in 2026 ([BCG](https://www.bcg.com/press/15january2026-as-ai-investments-surge-ceos-take-lead)), against McKinsey's mid-2026 result that the share attributing any EBIT impact to AI is unchanged at 37% ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)). Different samples; the year is not over.
- Largely wrong: Apollo's autumn 2025 reading that AI adoption was flattening or falling among large firms ([Apollo, 2025-11-28](https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/)). On the broader question introduced in November 2025, use at 250+ firms went from about 30% (February 2026) to about 40% (October 2026) ([Willison, 2026-11-02](https://simonwillison.net/2026/nov/2/census-bureau-super-intelligence)); Census itself reports 37% for 250+ firms in May 2026 ([Census](https://census.gov/library/stories/2026/05/ai-use-businesses.html)). Partly right: the national rate was flat at 17% to 20% from December 2025 to May 2026 (same Census page).
- Right: firms' own stated plans. In early 2025 about 9% of firms planned AI use within six months and by June adoption matched it. [P] ([FEDS Note](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html))
- Holding up as a description: Gartner's June 2025 "agent washing" and cost warnings; a year later Gartner's own survey shows 17% deployed and its AI Hype Cycle is organized around cost and control. [P] ([Gartner](https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence))
- Open: Gartner "over 40% of agentic AI projects cancelled by end of 2027" (restated unchanged in 2026); "15% of day-to-day work decisions made autonomously by 2028"; "40% of enterprise apps with task-specific agents by end of 2026" (deadline in six weeks, no outcome data found). ([Gartner 2025-06-25](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027); [Gartner 2025-08-26](https://gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025))
- Open: the macro dispute. Acemoglu's about 0.7% over ten years versus Goldman's +1.5 points a year cannot be judged on two to three years of data; the only positive macro reading is Brynjolfsson's own 2.7% estimate for 2025, which he says needs confirmation. ([AI Frontiers](https://ai-frontiers.org/articles/the-quadrillion-dollar-disagreement-on-ai-and-the-economy); [Fortune](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/))

### Inferences
- The pattern for the talk: analysts and executives have been poor at timing business effects in both directions, while the lab-side trend lines have been reliable and, if anything, conservative. The gap between the two is where the hype and the disappointment both come from.
- Self-interest shows in the direction of the errors: executives and consultancies over-forecast returns and job cuts, an asset manager's economist over-read a plateau, a project selling agent infrastructure produced the most quotable failure number.

### Gaps
- No systematic scorecard of analyst forecasts by an independent body was found.
- Outcome of Gartner's 2024 forecast that 30% of generative AI projects would be abandoned after proof of concept by end of 2025: not verified (S&P's 46% of proofs of concept scrapped in early 2025 is the nearest data point, from a different source and definition).

## Chart-ready numbers

Each item names the source section above for the URL.

1. McKinsey, agents scaling by firm size, 2025 to 2026: large firms 27% to 40%; smaller firms 22% to 22%. Two-group slope chart. (Section 2)
2. McKinsey, "use up, profit flat": scaling AI across the enterprise 38% to 44%; any EBIT impact about 37% to 37%; high performers about 6% to 6%. Paired bars, 2025 versus 2026. (Section 2)
3. McKinsey, individual versus enterprise in 2026: 80% report personal productivity gain; 50% better decisions; 37% any EBIT impact; 6% high performers. Descending bar ("the funnel from use to profit"). (Section 2)
4. McKinsey, headcount expectation versus outcome: 32% expected a decline (2025 survey), 14% reported one (2026), 39% expect one for the next year. Three bars. (Section 2)
5. Gartner ambition gap: 17% have deployed agents; more than 60% expect to within two years; more than 40% of projects expected cancelled by end of 2027. Three bars with different bases, label carefully. (Section 1)
6. Deployed-agent share by source, 2026: Gartner 17% (deployed), McKinsey about 20% (scaling, all respondents), Deloitte 23% (at least moderate use), McKinsey 40% (scaling, firms above $1bn). Dot plot showing how the definition moves the number. (Sections 1 and 2)
7. US Census BTOS by firm size, six-survey average, October 2026: 250+: 40.7%; 100 to 249: 33.5%; 50 to 99: 27.9%; 20 to 49: 23.8%; 10 to 19: 22.1%; 5 to 9: 21.1%; 1 to 4: 23.3%. Horizontal bars. Time series for 250+ firms with the wording break marked: about 12% (September 2025, old question), about 30% (February 2026), 37% (May 2026, Census story), about 40% (October 2026). (Section 3)
8. Same question, three units: about 20% of firms (Census, May 2026: 19.8%), 40.7% of workers use generative AI at work (RPS, November 2025), 12% daily, 78% of the workforce is at a firm that uses AI (Atlanta Fed, November 2025). Bars. (Section 3)
9. S&P Global abandonment: firms abandoning most AI initiatives 17% (2024) to 42% (2025); 46% of proofs of concept scrapped. Secondary source. (Section 3)
10. METR 50% time horizon, log scale, minutes: GPT-4 (March 2023) 3.5; Claude 3.7 Sonnet (early 2025) 60; Claude Opus 4 (2025) 101; o3 (2025) 121; GPT-5 (August 2025) 214; Claude Opus 4.5 (late 2025) 320; Claude Opus 4.6 (February 2026) about 870 (secondary); Claude Mythos Preview early snapshot (tested March 2026) at least 960, CI 510 to 3,300, in the "unreliable above 16 h" zone. Model dates are release or evaluation dates from general knowledge and METR's page, to be confirmed against METR's data file. Inset: doubling time 196 days (2019+), 131 days (2023+), 89 days (2024+). (Section 5)
11. Remote Labor Index automation rate: Manus at launch (October 2025) 2.5%; GPT-5 1.67%; Claude Opus 4.5 3.75%; Claude Opus 4.6 4.17%; Opus 4.8 8.33%; Fable 5: 15.83%; Gemini Argon 4: 17.08%; Fable 5.1: 17.92%; GPT 6 Astra 20.83%; Opus 5.5: 21.25%; Fable 5.2: 41.25%. Step chart by release order; the leaderboard gives no dates. (Section 3)
12. Macro estimates converted to one axis (added annual productivity or GDP growth, percentage points): Acemoglu about 0.07 (0.71% over ten years); McKinsey low end 0.1; OECD 0.5 (or 0.4 to 1.3 for the US); Goldman Sachs 1.5; Korinek and Suh scenario 18; Epoch GATE scenario 25 by year 10. Log-scale dot plot, with the conversion stated on the slide. (Section 4)
13. Cost of a fixed capability: MMLU score 86 at $37.50 per million tokens (March 2023) and $0.18 (February 2025); range of decline 9x to 900x per year. Older data (March 2025). (Section 5)
14. BCG maturity shift 2025 to 2026: stagnant 14% to 4.5%; expanding 35% to 41%; advanced 5% to 7.5%; agents' share of AI value 17% (2025, earlier BCG study), 22% (2026), 39% (2030 forecast). Consultancy self-assessment index. (Section 2)

## Papers cited, bibliographic details confirmed on the publisher page

The paper-search CLI offered by the coordinator was blocked by the session's permission classifier, so these were confirmed on arXiv and NBER pages instead.

| Paper | Authors | Date | Identifier | Key number in the abstract |
|---|---|---|---|---|
| TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks | Xu et al. (Carnegie Mellon, institution from general knowledge) | v1 2024-12-18, v3 2025-09-10 | [arXiv:2412.14161](https://arxiv.org/abs/2412.14161) | "the most competitive agent can complete 30% of tasks autonomously" |
| Remote Labor Index: Measuring AI Automation of Remote Work | Mazeika, Gatti, Menghini, Sehwag, Singhal and 42 others | 2025-10-30 (v1 only) | [arXiv:2510.26787](https://arxiv.org/abs/2510.26787) | best agent 2.5%, performance "near the floor" |
| Measuring AI Ability to Complete Long Software Tasks (title of v4; v1 was "Long Tasks") | Kwa, West, Becker, Deng, Garcia and 21 others (METR) | v1 2025-03-18, v4 2026-07-10 | [arXiv:2503.14499](https://arxiv.org/abs/2503.14499) | horizon doubled "approximately every seven months since 2019", possible acceleration in 2024; Claude 3.7 Sonnet about 50 minutes |
| Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | Becker, Rush, Barnes, Rein (METR) | v1 2025-07-12, v2 2025-07-25 | [arXiv:2507.09089](https://arxiv.org/abs/2507.09089) | 16 developers, 246 tasks; AI increased completion time by 19%; developers had forecast a 24% speed-up and still believed 20% afterwards; economists forecast 39%, ML experts 38% |
| The Simple Macroeconomics of AI | Daron Acemoglu | May 2024 | [NBER w32487](https://www.nber.org/papers/w32487) | "no more than a 0.66% increase in total factor productivity (TFP) over 10 years", "less than 0.53%" after adjusting for hard tasks |
| The Productivity J-Curve: How Intangibles Complement General Purpose Technologies | Brynjolfsson, Rock, Syverson | October 2018, revised January 2020 | [NBER w25148](https://www.nber.org/papers/w25148) | adjusted TFP 15.9% above official measures at end of 2017; AI-related intangible effect small but growing |

Corrections that follow from this check:
- Acemoglu's abstract says 0.66% (and under 0.53% adjusted) for TFP over ten years. The 0.71% quoted by AI Frontiers is not in the abstract (it is probably the paper's GDP-side or a later-version figure). Use 0.66% for TFP; in annual terms about 0.07 points either way.
- The METR developer trial (19% slower, early-2025 tools, 16 developers) is confirmed as a 2025 result. No 2026 replication was found, so it should be dated on any slide; it is also the cleanest example of a perception gap (believed 20% faster, measured 19% slower).

## Source and interest table

| Source | Type | Commercial interest to flag |
|---|---|---|
| Gartner | advisory analyst | Sells research and conferences to buyers and vendors; both the hype and the warning generate demand |
| Forrester, IDC | advisory analyst | Same model as Gartner; IDC forecasts are also sold to vendors for market sizing |
| McKinsey, BCG, Deloitte, Capgemini | consultancy | Sell AI transformation; surveys are of their client class, self-reported, and frame a small "leader" group to emulate |
| S&P Global Market Intelligence | data and research vendor | Sells the research; no direct stake in AI succeeding |
| MIT Project NANDA | academic-affiliated project | Promotes its own agent infrastructure; report is "preliminary", not peer-reviewed |
| RAND | non-profit research | No product; interview study, pre-agent (2024) |
| US Census Bureau, Federal Reserve staff | public statistics, central bank | None commercial; question wording changed in November 2025 and again in October 2026 |
| Apollo (Slok) | asset manager | Talks to investors; widely quoted charts, no method paper |
| Stanford HAI AI Index | academic | Independent; funded by donors that include technology firms |
| METR | non-profit evaluator | Works with AI labs on pre-release evaluations |
| Epoch AI | non-profit research | Philanthropic funding plus some lab-commissioned benchmarks |
| Scale AI and CAIS (Remote Labor Index) | vendor with non-profit | Scale sells data and evaluation services to labs |
| Brynjolfsson (Stanford) | academic | Also has commercial interests in AI workforce analytics |

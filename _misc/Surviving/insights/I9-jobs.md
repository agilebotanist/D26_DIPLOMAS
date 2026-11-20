# I9. Jobs

Synthesis of the research notes as of 2026-11-17. Sources: `labour_market_skills.md`, `gaps_labour.md` (later, wins where the two differ), `user_supplied_sources.md` (later, wins), with single items from `industry_structure_five_forces.md`. Verification levels are those of `references_keymap.tsv`: primary (the publisher's own page or document was read), secondary (a press or blog account was read), search-result only, not opened.

## Summary

The one thing to remember: firing because of AI is mostly a story companies tell, while not hiring beginners is the effect that shows up in the data.

The best story: Geoffrey Hinton told the world in 2016 to stop training radiologists; nine years later residency places are at a record, pay is up by about half, and he has said he got the timing wrong.

The best picture: one chart with two lines for 2026. The loud line is the number of US job cuts that employers blamed on AI each month, which jumps to 38,579 in May and falls to 1,265 in October. The quiet line is the employment gap for 22 to 25 year olds in AI-exposed jobs, which moves steadily from 15% to 19%.

The best question for discussion: if a company stops hiring juniors today, who will be its senior engineers in ten years?

What the speaker should not claim: that AI caused the 2026 layoffs, that Microsoft "fired 60,000 people", that design, copywriting and translation are dead, or that anyone knows how many developers will be needed.

## I9.1 "Because of AI" is what companies say when they cut, and in 2026 the saying went out of fashion in five months

1. Claim. AI is the reason employers state for about one announced US job cut in five in 2026. The share swung from about 40% of all cuts in May to under 3% in October. A technology does not retreat like that; a way of talking does.

2. Data. US job cuts for which the employer cited AI, by month, 2026 (Challenger, Gray and Christmas counts; monthly values derived by HCAMag from the cumulative totals) [@hcamagaiattributed], secondary:

| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct |
|---|---|---|---|---|---|---|---|---|---|
| 7,624 | 4,680 | 15,341 | 21,490 | 38,579 | 14,029 | 10,970 | 3,462 | 3,961 | 1,265 |

Totals: 121,401 AI-attributed cuts out of 617,189 announced in January to October 2026 (about 20%), against 54,836 in all of 2025 [@hcamagaiattributed], [@thestreetprocommentary], both secondary. The July figure (10,970, 33% of the month, 112,713 year to date, 184,538 since 2023) was checked in Challenger's own report [@challenger2026jobcuts], primary. In October "market and economic conditions" (130,531 year to date) overtook AI as the leading stated reason. For scale, in the first eleven months of 2025 AI was cited for about 4.5% of cuts [@fortune2026aiwashing], secondary.

Tech layoffs per year from the crowd-sourced tracker layoffs.fyi: 265,660 (2023), 152,922 (2024), 122,606 (2025), 128,536 (2026 to 10 September) [@freepressjournaltechlayoffs], secondary; no later 2026 total was found.

Slide number, if one is wanted: "38,579 in May, 1,265 in October". Better as the picture described in the summary.

3. Quotes.

"Naming AI in a layoff announcement can win over investors while pushing current and prospective employees away." Andy Challenger, chief revenue officer of the outplacement firm that publishes the count; the firm sells services to companies that are cutting staff and gains visibility from the monthly report. [@challenger2026jobcuts]. Checked against `converted/web/i9_challenger_jul26.md` (scraped in this session): EXACT.

"As cost unfortunately seems to have been a too predominant evaluation factor when organizing this, what you end up having is lower quality". Sebastian Siemiatkowski, chief executive of Klarna, to Bloomberg, as quoted by Fortune in May 2025; he had spent a year advertising Klarna as an AI-first company before its stock listing. [@fortune2025klarna]. Checked against `converted/web/C_fortune_klarna.md`: EXACT.

4. Case. Two reversals, both with names.

Klarna let its headcount fall from about 3,800 to about 2,000 through a hiring freeze and said its AI assistant did the work of 700 agents. In May 2025 the chief executive conceded "lower quality" and began bringing people back into customer support as a pool of remote contractors [@gizmodo2025klarna], [@fortune2025klarna], both secondary. Klarna later moved staff from marketing, engineering and legal into customer service [@cxtodayklarnaredeploying], secondary.

Block cut more than 4,000 people, about 40% of staff, on 26 February 2026. Jack Dorsey said "intelligence tools" had changed what it means to run a company, and in the same breath admitted over-hiring during the pandemic. The shares rose. Former employees disputed the AI explanation and at least four say they were rehired within weeks [@eweekblock], [@businesstodayblock], [@leaddev2026techlayoffs], all secondary. Engineers were under 30% of those let go [@signalfire2026state], primary.

5. Counter-evidence, in proportion. Part of it is real. Technology is the sector with the most cuts in 2026 (149,023 in January to July, up 67% on the year, 31% of all cuts) [@challenger2026jobcuts], and some companies do run with fewer support staff. Inside one developer survey, 23% of respondents say their company reduced headcount in the past year because of AI tools and 56% say it did not [@jetbrains2026rawdata], primary, self-reported. There is also a real AI effect that runs through budgets and not through automation: cash is moved from salaries to data centres (see I9.2). What the sources do not support is a measured count of jobs that AI took. Independent labour data (Yale Budget Lab, Economic Innovation Group, Oxford Economics, Anthropic's own economists) find no AI-driven rise in unemployment at the scale of the economy [@yalebudgetlab2025brookings], [@eckhardt2025aijobs], [@massenkoff2026labor], all primary; [@oxfordeconomicspatchy], secondary.

6. Speaker notes. Challenger records the reason an employer states in the announcement. It is a count of statements, not of causes. The three causes that every serious source names beside AI are the correction of 2021 to 2022 over-hiring, the end of zero interest rates, and the reallocation of cash to AI capital spending. Sam Altman, who sells the technology, said in February 2026 that some firms are blaming AI for layoffs they would have done anyway [@fortune2026aiwashingforever], secondary; that sentence is in the notes but was not checked against a local copy, so paraphrase it. Forrester (an advisory firm) defines "AI washing" as presenting financially motivated cuts as AI-driven and expects many of them to be quietly reversed; Gartner predicts that half of the companies that cut customer service staff because of AI will rehire by 2027 [@leaddev2026techlayoffs], [@customerexperience2026gartner], secondary; both are forecasts by firms that sell advice. Orgvue's "55% of leaders regret AI redundancies" comes from a vendor of workforce-planning software and reached the notes second-hand [@invezz2026companies]; keep it off slides. The US tax rule on research costs (Section 174) is often named as a hidden cause; the link to layoffs is argued, not demonstrated. Correction recorded: the earlier notes had no primary read of Challenger; the July report is now held locally.

7. Confidence and theses. High that AI attribution is volatile and self-reported; medium on how much of it is framing, because nobody can observe the cuts that would have happened anyway. Corrects T9: layoffs are a sign of change in budgets and in corporate language more than a sign that agents replaced the people. Supports T7 in spirit (numbers published by parties with an interest).

8. Question for the audience. When your own company next reorganises, which explanation will sound better to investors: "we over-hired" or "we became AI-first"?

9. Personal angle. The brief gives the speaker no layoff story of his own, and none should be invented. Speaker to supply: a moment when someone he knows was told that a reorganisation was "because of AI", or a moment when he himself was asked whether an assistant could replace a hire. Plain sentence for the slide: "Companies say AI when they cut people; whether AI did it is a different question, and so far the answer is mostly no."

## I9.2 Microsoft in 2026 is shrinking by invitation to pay for data centres, and says itself that AI did not replace these people

1. Claim. The largest software company reduced its headcount for the first time since 2016. It did so mostly with voluntary instruments, its own stated reasons are cost and reorganisation during a record AI investment programme, and the teams that build its agents were not spared.

2. Data. Three series.

Workforce actions in 2026, eligible against actual (all secondary unless marked):

| Date | Action | Eligible or announced | Known outcome |
|---|---|---|---|
| 23 April | Voluntary Retirement Program, first in 51 years | about 8,750 (7% of 125,000 US staff) | about 30% accepted, about 2,600 people [@geekwire2026microsoft], [@geekwire2026microsoftcutting] |
| 14 May | LinkedIn cuts | about 850 | executed [@seattlered2026local] |
| 6 July | Layoffs | 4,800, just over 2% of staff; about 1,600 in Xbox | executed; about 400 found internal roles [@geekwire2026microsoftcutting], [@seattletimes2026microsoftcuts] |
| 22 September | Further cuts | 450 (Seattle Times) or fewer than 600 (GeekWire) | the two company-sourced totals conflict [@seattletimes2026microsoftcuts], [@geekwire2026microsoftfurther] |
| 12 October | Copilot Studio team, Israel | about 50 summoned to pre-dismissal hearings | about half expected to stay; a hearing is not a dismissal [@calcalist2026microsoft] |
| 12 to 13 October | Africa Development Centre, Nairobi | nearly 400 jobs per employees | Microsoft confirms "proposed changes", not closure [@techcabal2026microsoft], [@businessinsider2026nairobi] |
| 26 October | Voluntary Exit Offer | about 60,000, about 27% of 223,000 | none yet; decision in early December, exit 31 December; Microsoft expects under 5% [@coleman2026introducing] primary, [@cnbc2026microsoft], [@fortune2026microsoft] |

Headcount: about 144,000 (2019), 228,000 (June 2025), 223,000 (June 2026, minus 2%, the first annual fall since 2016) [@seattletimes2026microsoft], [@fortune2026microsoft]. Capital expenditure for the September quarter: USD 34.9 billion in 2025, guided above USD 50 billion in 2026; free cash flow in the June quarter down 23% on the year [@cnbc2026microsoft].

Paid Microsoft 365 Copilot seats: 15 million (January 2026), over 20 million (April), over 30 million (July) on a base of about 450 million commercial seats, so about 3.3% rising to about 7%; in October the company gave no seat count [@microsoft2026fourth] primary for the July figure, [@nojitter2026microsoft], [@motleyfool2026whether]. A leaked internal memo, seen only second-hand, said fewer than 4.5% of commercial customers paid for Copilot and only 20 to 30% of those used it weekly [@techtimes2026azure].

Slide number, if one is wanted: "60,000 were offered money to leave; Microsoft expects fewer than 3,000 to take it". The pair is the story; the 60,000 alone misleads.

3. Quotes.

"Some organizations are providing the Voluntary Exit Offer, and some are not. Participation varies based on each business's priorities, customer commitments and workforce needs." Amy Coleman, chief people officer of Microsoft, in the published memo of 26 October 2026; the employer's own framing. [@coleman2026introducing]. Checked against `converted/web/ms_memo_blog.md`: EXACT.

"Some things like coding require less time of software developers". Brad Smith, vice chair and president of Microsoft, on the day of the July layoffs; he went on to say that product management, software design and "working directly with customers" are growing. [@geekwire2026microsoftcutting]. Checked against `converted/web/ms_gw_july.md`: EXACT.

Also verified and usable in notes: "we anticipate an under 5% uptake on the 60,000 employees that are eligible for the program" (Microsoft spokesperson to Fortune, [@fortune2026microsoft], `converted/web/ms_fortune_exit.md`, EXACT); "This is a time of tumult, right? I wish I could just sit here and say, it'll all be the same. I cannot" (Satya Nadella, chief executive, on The Pragmatic Engineer podcast as quoted by ETHRWorld, [@ethrworld2026nadella], `converted/web/ms_ethr_nadella.md`, EXACT, second-hand for the podcast); the chief financial officer on Copilot seats, "we did not disclose, to answer your direct question, an update on the Copilot number this quarter" ([@motleyfool2026whether], `converted/web/cop_fool_ignite.md`, EXACT from the second letter; the source prints the first word as "[W]e").

Not usable as a quotation: the sentence that the July roles "are not being directly replaced by AI" is GeekWire's paraphrase of Coleman's memo, not her words. Her verified words from the same memo are "AI is changing how work gets done." (`converted/web/ms_gw_july.md`, EXACT).

4. Case. The Copilot Studio team in Israel. Copilot Studio is Microsoft's platform for building AI agents. On 12 October 2026 about 50 of its people at the Israeli research and development centre (about 3,000 staff) were called to pre-dismissal hearings, attributed to "a global organizational restructuring" [@calcalist2026microsoft], [@ynetnews2026version], both secondary and from the same publishing group. Two weeks later Copilot teams were, according to anonymous sources of Reuters and Bloomberg, among those receiving the exit offer [@computerworld2026exitoffers], [@fortune2026microsoft]. Building the agents did not protect the builders from cost pressure.

5. Counter-evidence, in proportion. Microsoft has kept hiring while cutting: an economist quoted by Fortune notes that the company is at about 220,000 after announcing about 20,000 layoffs since 2024 [@fortune2026microsoft]. More than 4,000 employees were redeployed internally in the prior year, and the same week as the July layoffs Microsoft launched a USD 2.5 billion programme to place 6,000 engineers inside customers [@geekwire2026microsoftcutting]. Copilot seats doubled in six months, and Microsoft reports weekly engagement "on par with Outlook and Teams" for its large customers (a vendor claim) [@nojitter2026microsoft]. So the picture is a managed shrink and a shift of roles, not a collapse and not a triumph.

6. Speaker notes. Corrections to the earlier notes, from `gaps_labour.md`: the figure 8,750 is the number eligible for the spring retirement programme, not a hiring-freeze figure; 60,000 is an eligibility number and no departure figure can exist before December 2026; 50 in Israel is the number summoned to hearings; for Nairobi the company has confirmed "proposed changes" only, and the closure and the count of nearly 400 come from employees. The March hiring freeze rests on The Information through aggregators and is unconfirmed [@foley2026microsoft]. Confirmed involuntary cuts in 2026 add up to roughly 6,000 to 6,500, against more than 15,000 in 2025 [@cnbc2025microsoft]. The list of divisions in the exit offer was never published by Microsoft. The description that the offer went to "most software engineers" is Gergely Orosz's reading, not a Microsoft figure [@nacionale2026nadella]. The Andreou memo on weekly use was seen only through TechTimes relaying The Decoder. Seat counts are contracted licences, some discounted, not active users, and Microsoft has never disclosed Copilot revenue. The switch from seat counts to usage metrics in October coincides with a pricing change to seats plus consumption, so it has an innocent explanation; it also removes the one comparable number outsiders had. Interests: Microsoft sells Copilot; GeekWire and the Seattle Times are local outlets with company access (Microsoft Philanthropies funds some Seattle Times journalism, disclosed by the paper).

7. Confidence and theses. High on the timeline and on the distinction between eligible and departed; medium on motives, which are company statements plus press reading. Corrects T9 (the layoff is a budget story) and supports T8 (the physical build-out is expensive enough to move headcount). It also gives T16 a concrete line from the company itself: less time on coding, more on design and customers.

8. Question for the audience. If the company that sells the agents has paid users at about 7% of its own customer base, and is asking a quarter of its staff whether they would like to leave, what does that tell you about where the money is going?

9. Personal angle. Speaker to supply, if he has one: a moment from his own work with Copilot or a similar office assistant that shows the gap between having a licence and using it every week. Plain sentence for the slide: "Microsoft did not replace these people with AI; it is paying for the machines, and it said so."

## I9.3 The door that is closing is the entry door

1. Claim. The best-documented labour effect of generative AI so far is that fewer young people are hired into exposed occupations. Experienced workers show no comparable gap. The evidence is descriptive, and the people who lead the industry disagree in public about what to do.

2. Data.

Stanford Digital Economy Lab, "Canaries in the Coal Mine?", ADP payroll data, revision of August 2026: employment of 22 to 25 year olds in highly AI-exposed occupations is about 19% below where it would be had it tracked less-exposed peers (June 2026), up from 15% at the July 2025 vintage. In levels from November 2022 to June 2026 the two most exposed quintiles fell about 11% and the three least exposed grew about 10%. The adjustment runs through reduced hiring, not dismissals [@brynjolfsson2026canaries], primary; the 19% and 15% were re-checked in the local copy.

SignalFire, hiring against 2019 at twelve large technology companies: all hiring minus 25%, engineering minus 11%, marketing minus 36%, product management minus 39%, design minus 48%, new graduates about minus 65%. At early-stage startups: new graduates about minus 76%, engineering plus 7% [@signalfire2026state], primary (a venture firm's proprietary data built largely on public profiles).

Supporting series: US postings in software development are 69.3% senior and 4.5% entry-level (first quarter of 2026) [@indeedhiringlab2026seniority], primary. Dallas Fed: even if the whole shortfall of young workers became unemployment it would add about 0.1 percentage point to the national rate [@federalreservebank2026fedeconomics], primary. Cleveland Fed: job-finding rates fell about 6 points more in the most exposed occupations, with no clear pattern in separations [@cline2026fedeconomic], primary. JetBrains 2026: 34% of juniors call their local job market "very challenging" against 26% of seniors; among respondents with up to two years of experience 32% say their company cut headcount because of AI, against 19% of those with eleven years or more [@jetbrains2026rawdata], primary.

Slide number, if one is wanted: none on the main slide. The SignalFire bar chart is the picture; in it engineering is the least-hit function and new graduates are the most-hit channel.

3. Quotes.

"These are descriptive patterns, not causal estimates of the effect of AI." The Stanford authors (Brynjolfsson, Chandar, Chen) about their own result; an academic lab, and one author has commercial AI interests. [@brynjolfsson2026canaries]. Checked against `converted/web/i9_stanford_canaries_aug26.md` (scraped in this session): EXACT.

"How's that going to work when ten years in the future you have no one that has learned anything". Matt Garman, chief executive of Amazon Web Services, August 2025, explaining why he called replacing juniors with AI "the dumbest thing I've ever heard"; he sells AI services, and Amazon cut about 30,000 corporate jobs between October 2025 and January 2026. [@register2025awsceo]. Checked against `converted/web/jr_garman_reg.md`: both phrases EXACT.

For the opposite position: "We hire almost no junior devs". Bjorn Hovland, president of the Linux vendor CIQ, November 2026; in the same interview, "We cannot hire enough engineers now." [@businessinsider2026aicoding]. Checked against `converted/web/jr_bi_90pct.md`: both EXACT.

4. Case. Anthropic against Anthropic. In May 2025 the chief executive, Dario Amodei, told Axios that AI could remove half of entry-level white-collar jobs and push unemployment to 10 to 20% within one to five years (Axios's wording of his forecast), adding in his own words: "We, as the producers of this technology, have a duty and an obligation to be honest about what is coming" [@axios2025behind], primary, `converted/web/amo_axios.md`, EXACT. In July 2026 the company's head of economics, Peter McCrory, wrote: "I don't expect unemployment to be noticeably higher a year from now", and he added that this holds at least as far as AI is concerned [@fortune2026anthropichead], secondary, `converted/web/amo_fortune_econ.md`, EXACT for the quoted words. In between, Sam Altman of OpenAI said in May 2026: "I thought there would have been more impact on entry-level white-collar jobs being eliminated by now than has actually happened", and "I'm delighted to be wrong about this." [@hrexecutive2026openai], secondary, `converted/web/amo_hrexec.md`, both EXACT. Eighteen months of the "one to five years" have passed with US unemployment near 4.2%. The forecast is neither confirmed nor expired, and the narrow signal that does exist is the one about juniors.

5. Counter-evidence, in proportion. On the evidence: the Stanford authors report some differences in trend before generative AI, a smaller gap once education is accounted for, and larger gaps in ADP data than in national surveys. Apollo's chief economist attributes the weakness at entry level to a low-hire, low-fire market [@fortune2026aiimpact], secondary. Economy-wide studies find a gap of 0.2 to 0.3 percentage points for recent graduates or none [@eckhardt2025aijobs], primary; [@iza2026discussion], secondary. These fit together: a hiring slowdown concentrated in one age group and a few occupations is too small to move national unemployment. On the positions: several large employers say on the record that they keep hiring juniors. Amazon: 11,000 interns and new graduates in 2026 [@platformer2026awsceo], primary. Cloudflare: 750 internships hosted toward a goal of 1,111 [@cloudflare2026oneyear], primary. Shopify: from about 100 interns a year to more than 1,000 [@coderpad2026shopify], primary. Accenture expects to hire more at entry level [@constellation2026accenture], secondary. The Indian services firms kept fresher intake high while removing mid-level staff (I9.5). The same firms cut total staff: Cloudflare removed about 20% of its people in May 2026 [@siliconrepublic2026cloudflare], secondary. "We hire juniors" and "we employ fewer people" are both true there. None of these firms shows data that junior hiring pays off; these are stated strategies. Jensen Huang's answer was "Wait two years." [@newstack2026jensen], secondary, `converted/web/jr_huang_newstack.md`, EXACT; he sells the chips and benefits from adoption without fear.

6. Speaker notes. Separate correlation from cause aloud: Canaries, the Cleveland Fed and the Dallas Fed are associations; the Harvard resume study (junior employment at AI-adopting firms about 7.7% lower within six quarters) is a working paper by two doctoral students [@hosseini2026generative], and the 7.7% is a press figure. SignalFire is a venture firm; its data rest on public profiles. Corrections recorded: the earlier notes could not source Garman, Amodei or the Cloudflare and GitHub positions; `gaps_labour.md` supplies them. The Axios sentence about "half of all entry-level white-collar jobs" is Axios's summary, so do not put it in quotation marks as Amodei's. Fortune reports that Amodei re-escalated in June 2026, which leaves the company holding two positions at once. NY Fed data put unemployment of recent computer science graduates near 7% on 2024 data with underemployment below 20%; the by-major figures reached the notes second-hand.

7. Confidence and theses. High that the entry tier has narrowed in the United States; medium that AI is the main cause; low on how long it lasts. Supports T15 (shocks before stabilisation) and refines T16: what disappears first is not the average coder but the first job of the future coder.

8. Question for the audience. For the students: what can you already own and verify, without someone senior checking it? For the employers in the room: who trains your seniors of 2036?

9. Personal angle. The brief says the speaker teaches. Speaker to supply: one concrete moment from his own teaching or supervision in the past year, for example a student asking whether there will be a job, or a graduate's first job search. Plain sentence for the slide: "Nobody is firing the seniors; they are just not opening the door for the beginners, and that is the part I worry about as a teacher."

## I9.4 Writing, translation and design were badly hurt at the commodity end, not killed

1. Claim. On freelance platforms, demand for writing fell by about a third and for graphic design by about a fifth against comparable work within months of the tools appearing. The people who stayed lost a few percent of jobs and income, and the best-rated lost more. Unions report a third of translators losing work. That is damage at the cheap, short, well-specified end of the market, not the death of the occupations.

2. Data. Two studies that measure different things and must be shown on separate charts.

Demirci, Hannane and Zhu count job posts per category on one large platform (1.2 million fixed-price posts, July 2021 to July 2023), relative to manual-intensive work [@demirci2024aireplacing], primary:

| Category | Change in posts |
|---|---|
| Writing | minus 30.4% |
| Software, app and web development | minus 20.6% |
| Graphic design | minus 18.5% |
| 3D modelling | minus 15.5% |
| Engineering | minus 10.4% (not significant in the baseline) |
| All automation-prone categories | minus 20.9% |

The remaining posts had a 5.7% higher budget, 8.6% more bids and 2.2% more skill tags.

Hui, Reshef and Zhou follow individual freelancers on Upwork (about 80,000 people, January 2022 to April 2023), with software developers in the control group [@hui2024short], primary:

| Occupation | Jobs per month | Monthly earnings |
|---|---|---|
| Writing, after ChatGPT | minus 2.0% | minus 5.2% |
| Image work, after DALL-E 2 and Midjourney | minus 2.1% | minus 5.2% |

The probability of starting any job in a month fell by about a tenth.

Surveys: Society of Authors (UK, 787 members, January 2024): 26% of illustrators and 36% of translators said they had already lost work to generative AI; 37% and 43% said their income had fallen in value [@booksellersociety], [@europeanwriterssociety], both secondary. Netherlands, over 700 creatives: one in five freelance artists lost income, translators hardest hit [@nltimes2025aihitting], secondary. Design inside technology companies: hiring at the twelve largest is 48% below 2019, at startups 22% below, against minus 11% and plus 7% for engineering [@signalfire2026state], primary. The World Economic Forum's 2025 employer survey added graphic designers to its list of fastest-declining roles [@wef2025future], primary.

Slide number, if one is wanted: "a third of translators say they have already lost work" (a union survey, say so aloud).

3. Quotes.

"we can generally rule out that freelancer quality moderates the adverse effects of generative AI on employment". Hui, Reshef and Zhou, academic authors with no commercial interest, on the finding that good freelancers were not protected. [@hui2024short]. Checked against `converted/reports/TheShort-termEffectsOfGenerativeArt_preview.md`: EXACT.

"the effect not only persists but also grows". Demirci, Hannane and Zhu, academic authors, on the fall in job posts over the eight months after ChatGPT. [@demirci2024aireplacing]. Checked against `converted/reports/ssrn-4991774.md`: EXACT.

4. Case. The translator in the union survey is the clearest human case the sources hold: one in three says work has already gone. Duolingo is the company case: it cut about 10% of its contractors in early 2024 with AI taking over part of the content work, then faced a backlash to its "AI-first" memo in 2025, after which the chief executive said no full-time employee had been laid off [@techspotduolingo], secondary. No named individual story is in the notes; if the speaker knows a designer or translator, that story belongs here.

5. Counter-evidence, in proportion. Demand grew for work that complements the tools: a peer-reviewed study of another platform finds machine-learning programming up 24% and chatbot development nearly tripled while substitutable writing and translation fell 20 to 50% against trend [@teutloff2025winners], primary. Remaining posts became slightly better paid and more complex (a composition effect, not a pay rise for the same work). Graphic design's share of all posts on the Demirci platform rose from 22.2% to 24.3%, because other categories fell faster. An earlier polarisation after desktop publishing left the median designer's wage flat for thirty years while the top tenth did well [@bessen2015finance], primary, so the pattern is not new.

6. Speaker notes. Correction recorded from `user_supplied_sources.md`: the earlier notes held the Demirci and Hui figures as unverified recollections and gave the wrong first affiliation; both papers are now read at source (first author of Demirci et al. is at Harvard Business School). The two results are not two estimates of one quantity: one counts posts (demand), the other follows freelancers who stayed visible (realised work), so never average them or show them as a range. Both windows end in 2023, before any coding agent. Both are relative to control groups that also declined, so the authors treat them as lower bounds. One platform each; a fall in posts cannot be told apart from employers moving elsewhere. The top-freelancer result in Hui et al. is "suggestive" in the authors' own word, with quality measured after treatment. The union and guild surveys come from interested parties and measure perceived loss. The Hui paper says nothing about software work.

7. Confidence and theses. High for "hurt at the commodity end"; the word "killed" is not supported. Corrects T2. The minus 20.6% for freelance software and web development is the only causal-style number in the notes that bears on T16's "average coder".

8. Question for the audience. Which part of your own job looks like a short, well-specified freelance task, and which part needs someone who knows the customer?

9. Personal angle. The brief says the speaker uses the tools daily for office, admin, teaching and research work, which includes writing. Speaker to supply: when did he last pay a person for a translation, a text or a picture, and what does he do now? Plain sentence for the slide: "These professions are not dead; the cheap end of them is, and the cheap end is where people used to start."

## I9.5 Cheaper software has not yet told us whether we need more developers or fewer, and history has gone both ways

1. Claim. More software is being shipped and developer postings are recovering, mostly for seniors. Nobody has a series that settles whether demand for software grows faster than agents absorb the work. The three classic stories (radiologists, accounting clerks, bank tellers) each end differently, and the difference is how much more of the product people wanted once it became cheap.

2. Data.

More supply, flat use: new app submissions to Apple's App Store were 235,800 in the first quarter of 2026, up 84% on the year (Sensor Tower), and the first half of 2026 brought about 560,000 new apps, close to the whole of 2025 [@9to5mac2026appstore], [@gigazine2026appstore], both secondary. Downloads rose 3% in 2025 and 2% in the first half of 2026 [@gigazine2026appstore]. A second data provider, Appfigures, is cited in opinion pieces for new releases across both stores up 60% in the first quarter of 2026 [@oreillyradarworld], [@neomindlabs2026jevons], both secondary.

Postings: Indeed's software development index (February 2020 = 100) was 61.1 on 17 May 2025 and 76.1 on 4 September 2026; 71% of the net increase between May 2025 and May 2026 came from senior roles and 37% from postings with AI in the title [@drorpolegdashboard], [@officechaisoftware], [@ciohiring], all secondary relays of Indeed data.

Official projection, United States, 2024 to 2034: computer programmers minus 6%, software developers, quality assurance analysts and testers plus 15% [@blsoccupational], [@blsoccupationaloutlook], both primary.

Executives' reports for software engineering headcount (McKinsey 2026, chart reconstructed from scrambled labels, check against the PDF): 22% report a decrease over the past year because of AI and 11% an increase; a year earlier 31% had expected a decrease [@mckinsey2026stateofai], primary.

IT services, falling then rising: TCS headcount 582,163 (December 2025), 584,519 (March 2026, minus 23,460 over the fiscal year), 593,798 (June 2026), 598,056 (September 2026), with 44,000 freshers onboarded in the year of the fall [@storyboard182026tcshr], [@peoplematters2026tcsadding], [@ethrworld2026indian], all secondary. The five largest Indian firms together: minus 7,389 in fiscal 2026, plus 24,398 in the following half-year [@moneycontrol2026topfive], [@moneycontrol2026topfiveindian], secondary, headline and description only. Wipro is the outlier (minus 6,716 in one quarter, campus hiring paused) [@moneycontrol2026wipro]. Accenture's headcount rose 5% in the year to August 2026 [@accenture2026q4fiscal], primary.

History, three series:

| Story | Data points |
|---|---|
| Radiologists after 2016 | residency positions 1,208 in 2025, a record; average pay USD 520,000 in 2025, 48% above 2015; Mayo Clinic radiology staff about 260 to over 400; over 700 cleared AI models, about 48% of radiologists use AI [@worksinprogressaireplaced], [@decoderhinton], secondary |
| Spreadsheets | 400,000 fewer accounting clerks and 600,000 more accountants in the US since 1980 [@bbcplanet], secondary; or, 1987 to 2000, clerks 2.0 to 1.5 million, accountants and auditors 1.3 to 1.5 million, analysts and financial managers 0.6 to 1.5 million [@businessinsider2023morgan], secondary |
| Bank tellers, phase one | tellers per urban branch 20 to 13 (1988 to 2004), urban branches plus 43%, more tellers in total for about thirty years [@bessen2015finance], primary |
| Bank tellers, phase two | 339,200 tellers in 2025, projected minus 13% for 2025 to 2035 as branches close and banking moves to the phone [@blsoccupationaloutlookhandbook], primary; [@oksatmdidn], secondary |

Slide number: none. The teller story as a two-phase line is the picture.

3. Quotes.

"If you work as a radiologist, you're like the coyote that's already over the edge of the cliff but hasn't yet looked down". Geoffrey Hinton, computer scientist, later a Nobel laureate, at a conference in Toronto in 2016, as quoted by Fortune in 2026. [@fortune2026hinton]. Checked against `converted/web/rad_fortune.md`: EXACT. His sentence "people should stop training radiologists now" was checked against `converted/web/rad_wip.md` [@worksinprogressaireplaced]: EXACT.

"While the rate of productivity growth influences the pace of change, the elasticity of demand determines the sign of the change." James Bessen, economist, summarising a century of automation in textiles and steel; academic, no commercial interest. [@bessenautomation]. Checked against `converted/web/bessen_vox.md`: EXACT.

Also verified: "in the US alone, there are 400,000 fewer accounting clerks today than in 1980, the first full year that VisiCalc went on sale" (a BBC article by the Financial Times's Undercover Economist columnist, relaying Planet Money, [@bbcplanet], `converted/web/ss_bbc.md`, EXACT); "We do not believe that there will be drastic change in headcount." (K. Krithivasan, chief executive of TCS, July 2026, [@peoplematters2026tcsadding], `converted/web/its_tcs_q1.md`, EXACT; his company sells labour by the hour).

4. Case. Hinton and the radiologists. In 2016 the most respected name in the field said it was "completely obvious" that within five years deep learning would do better than radiologists. In May 2025 he told the New York Times that he had spoken too broadly, had meant image analysis only, and had been wrong on the timing but not the direction (reported through the radiology trade press; the Times piece was not read) [@auntminnieeuroperadiology], secondary. Why the forecast failed, as the sources give it: models lose accuracy on other hospitals' data, most tools detect one finding in one kind of image, payment and liability rules require a physician's final read, reading images was about a third of the job, and cheaper imaging raised demand [@worksinprogressaireplaced].

5. Counter-evidence, in proportion. Against the comforting reading: David Autor and co-authors find that the negative effect of automation on employment was more than twice as large in 1980 to 2018 as in 1940 to 1980, while the positive effect of augmentation rose only modestly [@mitnews2024autor], secondary. Bessen's own rule cuts both ways: employment rises while demand is unsaturated and falls afterwards. The radiologist "shortage" is itself contested: a job board's analysis found almost half of postings were re-posts [@auntminnie2026radboard], secondary. On the Jevons side, the arithmetic is unforgiving: a 70% cut in delivery effort needs more than three times as much software to keep build hours flat [@forbestechnology2026aimake], secondary, a paid-membership opinion column. And the generic application developer may lose demand even if total software grows, because end users build one-off tools themselves [@davidsjjevons], secondary. In the JetBrains data, 53% say non-coding colleagues became more involved in development and prototyping over the past year [@jetbrains2026rawdata], primary.

6. Speaker notes. Corrections recorded from `gaps_labour.md`: the earlier notes had no sources for radiologists and spreadsheets; they are now read, mostly through secondary essays. The two radiologist pay figures (USD 520,000 and USD 571,000) come from different Medscape editions and are not reconciled; use "up by about half". The data behind Planet Money's 400,000 and 600,000 were not seen. The compiler analogy rests on one opinion piece without counts [@wired2023chatgpt] and should not carry a slide. Two providers give two growth figures for app releases (84% for the App Store, 60% for both stores); name one and its provider. Postings are vacancies, not employment. All Indian figures come from press reports of company fact sheets; fiscal 2026 was the trough, so a chart that ends in March 2026 would mislead. The analogy is in active use by vendors (Jensen Huang cites the radiologists to argue that AI will not destroy jobs), which is a reason to tell both halves.

7. Confidence and theses. High that the question is open; that is the finding. Supports T15 as worded (an open question, shocks before stabilisation). The official split between "programmers" and "developers" supports T16 in direction.

8. Question for the audience. Is the agent the ATM, which made branches cheaper so that banks opened more of them, or the smartphone, which made the branch unnecessary?

9. Personal angle. The brief's thesis T10 says an idea now reaches a proof of concept in hours, and T17 says there is no way back. Speaker to supply: one thing he built this year that he would never have commissioned from a developer, which is the Jevons argument in one example. Plain sentence for the slide: "I build more software than ever and I hire no one to do it; multiply me by a million and tell me whether that is more work for developers or less."

## I9.6 Most developers call the job market hard and would still choose the profession again; in Russia the squeeze has domestic causes first

1. Claim. In the largest open developer survey of 2026, a majority find it hard to get a job where they live, a majority feel secure in the job they have, and seven in ten say studying computer science is still worth it. In Russia the market turned sharply in favour of employers, and Russian sources name the economy and taxes before AI.

2. Data.

JetBrains Developer Ecosystem Survey 2026, raw data, weighted shares [@jetbrains2026rawdata], primary; method in [@makeeva2026archiving], primary:

| Question | Result |
|---|---|
| Local job market for developers | challenging 58% (very 30%, somewhat 28%); favourable 18% |
| Security in the current job | secure 56%; insecure 18%; hard to say 25% |
| Company reduced headcount in the past year because of AI tools | yes 23%; no 56%; do not know 18% |
| Layoffs for any reason at employers in the past two years | small-scale 32%; mass 13%; none 40% |
| Anxious that AI might replace my role | always or often 29%; rarely or never 44% |
| "AI will fully replace human developers" | agree 22%; disagree 47% |
| "AI coding will decrease demand for professional developers" | agree 38%; disagree 32% |
| Thinking about changing profession | actively 11%; from time to time 25%; no 58% |
| Would choose the same career again | yes 72% |
| Studying computer science worth it in 2026 | yes 71%; not worth it 13% |
| Burnout in the past one to two years | 58% |

By seniority (junior, middle, senior): job market "very challenging" 34%, 31%, 26%; anxious about replacement often or always 32%, 30%, 25%. By region, "company cut headcount because of AI": Europe 14%, North America 19%, China 35%, India 38%, Japan 7%.

Russia. hh.ru, IT, February 2026 against February 2025: vacancies minus 36%, resumes plus 30%, resumes per vacancy 9.6 to 19.6; offered median salary 89.9 to 100.0 thousand roubles [@datalab2026hhruvacancies], secondary. About 505 thousand IT vacancies in 2025, 25% fewer than in 2024; the senior segment stays tight (index 0.5 to 2.3) while junior competition reached about 19 resumes per vacancy [@incrussiarussian], [@incrussiajunior], secondary. Habr Career, first half of 2026: median IT salary 191 thousand roubles, plus 4.5% on the year against plus 20% a year earlier and below inflation of 5.62% [@smartlab2026rbchabr], secondary.

Slide number, if one is wanted: "71% of working developers say computer science is still worth studying".

3. Quotes. One verified quote, and it is a caveat: "coverage and self-selection limitations remain after cleaning and weighting". Makeeva and Molotova of the JetBrains surveys team, the producers of the dataset, in their method poster; JetBrains sells developer tools and its own AI products. [@makeeva2026archiving]. Checked against `converted/reports/WAPOR2026_makeeva.md`: EXACT. No quote on the Russian market could be verified: none of the Russian sources is held locally.

4. Case. The Russian junior. A year ago about ten resumes competed for each IT vacancy on hh.ru; in February 2026 about twenty did, and for juniors about nineteen per vacancy against about two for seniors. The causes named in Russian coverage: a slowing economy, the insurance contribution rate for IT firms rising from 7% to 15% from 1 January 2026, the end of the import-substitution impulse, a 34% fall in IT companies' net profit in 2025, and AI adoption last [@tproger2026hired], [@mailrufinanceendera], [@devbyrussian], all secondary. Supply keeps growing: budget-funded IT admissions were 117.1 thousand in 2022 and over 128 thousand in 2024 [@datalab2026hhruvacancies].

5. Counter-evidence, in proportion. The survey mood is sober, not dark: the same people who call the market hard mostly feel secure and would choose the career again. On the Russian side, one integrator claims AI cuts budgets for typical IT positions by 30 to 50%; that is a vendor claim [@mailrufinanceendera]. The hh.ru author does not attribute the change to AI at all.

6. Speaker notes. JetBrains is a non-probability sample of a tool vendor's audience. Weighting moves the answers: respondents in China are 4.7% of rows and 20% of the weight and answer far more positively, so for a European or Russian audience the European column is the better benchmark. The job-market questions went to routed subsets (n from about 2,500 to 9,900). "Company cut headcount because of AI" is a respondent's belief about the employer's motive. Russia has 58 respondents in the file; no Russian estimate can be taken from it. The hh.ru analysis is by an individual author who calls the method still in refinement; no hh.ru data later than February 2026 and no Habr Career grade split were found. Correction recorded: `user_supplied_sources.md` replaces the JetBrains blog figures used earlier with the raw data.

7. Confidence and theses. High for the survey as a description of its own sample; medium as a description of all developers; medium for the Russian series, low for any Russian AI attribution. Qualifies T9 for a Russian audience: the local layoffs and hiring freeze are not evidence about agents. Speaks to T15.

8. Question for the audience. Hands up: who here finds it harder to get a job than three years ago, and who would still choose this profession?

9. Personal angle. This is the question the students will ask. The brief does not give the speaker's answer, and it should be his. Speaker to supply: what he actually says when a student asks "will I have a job". Plain sentence for the slide: "The people already inside are worried and staying; I would still tell a student to come in, and to come in able to check the machine's work."

## Open points

Unverified or second-hand facts that should be checked before they reach a slide: the monthly AI-attributed series (derived by HCAMag, not printed by Challenger month by month); the October 2026 Challenger figures (two secondary sources); layoffs.fyi totals (press relays, none after 10 September 2026); Block's rehires (four former employees through one outlet); the Andreou memo on Copilot's weekly use (third-hand); the Microsoft hiring freeze of March 2026; the Nairobi closure and its headcount; the list of divisions in the exit offer; the Harvard resume study's 7.7%; NY Fed unemployment by major; the Indeed index values (through dashboards and press); the Appfigures figure; the Planet Money counts; both radiologist pay figures; Hinton's concession (the New York Times piece was not read); all Indian headcount figures (press reports of fact sheets); all Russian figures (secondary, and none held locally).

Unknowable today: how many people accept Microsoft's exit offer (decision in early December 2026, likely reported in January 2027), and whether Microsoft gave a new Copilot seat count at Ignite on 17 November 2026.

Contested: how much of the junior hiring gap is caused by AI as opposed to interest rates and the hiring cycle; whether there is a radiologist shortage; whether the fall in posts on freelance platforms is lost work or work that moved elsewhere; the sign of the Jevons effect for developers.

Not held in the notes: any series of total developer employment that would settle I9.5; a programmer headcount around the compiler transition; EU-wide developer employment; a Russian developer survey with a usable sample; a named individual story for I9.4.

Quotes considered and left out as unverified, keep off slides: Sam Altman's "blaming AI for layoffs" sentence (Fortune, not held locally); Jack Dorsey's "intelligence tools" (not held locally); Microsoft's "not being directly replaced by AI" (a paraphrase by GeekWire); the Andreou memo's "earn the right to exist" (the words are EXACT in `converted/web/cop_techtimes30m.md`, but the memo itself is third-hand); Hinton's "wrong on the timing but not the direction" (a paraphrase in the trade press); Microsoft's "Microsoft remains committed to Kenya" (not checked).

## Bibliography additions needed

No source cited above lacks a key. The following entries need attention.

Local copies to record in the `file` field (scraped in this session into `converted/web/`): `challenger2026jobcuts` to `i9_challenger_jul26.md`; `brynjolfsson2026canaries` to `i9_stanford_canaries_aug26.md`.

Local copies that exist in `converted/web/` but are not recorded in the `file` field of the entry: `fortune2026microsoft` (`ms_fortune_exit.md`), `ethrworld2026nadella` (`ms_ethr_nadella.md`), `nacionale2026nadella` (`ms_nacionale_nadella.md`), `seattletimes2026microsoft` (`ms_st_headcount.md`), `motleyfool2026whether` (`cop_fool_ignite.md`), `techtimes2026azure` (`cop_techtimes30m.md`), `register2025awsceo` (`jr_garman_reg.md`), `platformer2026awsceo` (`jr_garman_platformer.md`), `businessinsider2026aicoding` (`jr_bi_90pct.md`), `newstack2026jensen` (`jr_huang_newstack.md`), `fortune2026anthropichead` (`amo_fortune_econ.md`), `hrexecutive2026openai` (`amo_hrexec.md`), `fortune2026hinton` (`rad_fortune.md`), `auntminnieeuroperadiology` (`hinton_auntminnie.md`), `bbcplanet` (`ss_bbc.md`), `peoplematters2026tcsadding` (`its_tcs_q1.md`).

Exact titles learned from local copies, to replace bracketed descriptive titles:

| Key | Exact title |
|---|---|
| `seattletimes2026microsoft` | Microsoft's head count falls for first time in a decade |
| `fortune2026microsoft` | Microsoft's 60,000-person buyout offer hints at a future with fewer workers and more equipment |
| `ethrworld2026nadella` | Nadella explains Microsoft's voluntary exit offer, says employees need greater career flexibility |
| `nacionale2026nadella` | What did Satya Nadella say about Microsoft's buyouts and AI coding? Key points from his new interview |
| `motleyfool2026whether` | Microsoft Ignite Starts Nov. 17. Will Microsoft Update Its Paid Copilot Seat Count? |
| `techtimes2026azure` | Azure Tops $100B, Copilot Paid Seats Jump to 30M in Microsoft Blowout Quarter |
| `register2025awsceo` | AWS CEO says AI replacing junior staff is 'dumbest idea' |
| `platformer2026awsceo` | The CEO of AWS on why Amazon is hiring 11,000 interns and junior employees |
| `businessinsider2026aicoding` | AI writes 90% of the code at this company. It still can't hire enough engineers. |
| `newstack2026jensen` | Jensen Huang says the junior developer problem ends in two years. Here's his math. |
| `fortune2026anthropichead` | Anthropic's head of economics just explained why we haven't seen a white-collar bloodbath (the printed title ends with a dash and the word "yet") |
| `hrexecutive2026openai` | OpenAI, Anthropic CEOs walk back AI job warnings as IPOs loom |
| `fortune2026hinton` | A decade after the 'Godfather of AI' said radiologists were obsolete, their salaries are up to $571K and demand is growing fast |
| `auntminnieeuroperadiology` | Hinton acknowledges mistake in predicting AI replacement of radiologists |
| `bbcplanet` | How computing's first 'killer app' changed everything |
| `peoplematters2026tcsadding` | TCS hires 14,000 freshers, adds 9,279 employees as CEO rules out AI-driven job cuts |

Sources mentioned in the notes without a key, not cited above, to add only if the speaker wants them: the New York Times feature of 14 May 2025 by Steve Lohr with Hinton's concession (proposed key `lohr2025radiologists`; paywalled, not read; URL not in the notes); the Appfigures release counts at source (proposed key `appfigures2026releases`; only relayed by [@oreillyradarworld] and [@neomindlabs2026jevons]); the Sensor Tower counts at source (proposed key `sensortower2026appstore`; relayed by [@9to5mac2026appstore]).

# I3. The productivity paradox

Theme file for the talk "Agentic AI impact on the IT industry". Sources: `research_notes/Agentic AI impact on IT industry/` (mainly `benchmarks_vs_reality.md`, `gaps_benchmarks.md`, `analysts_adoption_hype.md`, `gaps_economics_analysts.md`, `user_supplied_sources.md`), read on 2026-11-17. Where a later notes file corrects an earlier one, the later value is used and the correction is recorded in item 6 of the insight. Verification levels in brackets are those of `references_keymap.tsv`.

## Five-line summary

1. The one thing to remember: "I feel faster" is true, widely shared and not yet a measurement. The gain is real at the desk, moves to review and rework inside the team, and has not reached the profit line or the national statistics.
2. The best story: in 2025 experienced developers felt 20% faster and were measured 19% slower; a year later the same researchers could not repeat the experiment, because developers refused to work without AI.
3. The best picture: a funnel from use to profit, in four bars from one survey (80% say it improves their own productivity, about half say better decisions, 37% see any profit contribution, 6% are high performers).
4. The best question for discussion: if you feel faster, who measured it, and where did the saved time go?
5. What the speaker should not claim: that "developers are 19% slower with AI" (a 2025 result that its authors no longer apply to current tools), that "95% of AI projects fail" or "80% fail" (weak numbers), or any single figure for the productivity gain, whether from a vendor or from a sceptic.

## I3.1 Developers felt 20% faster, were measured 19% slower, and a year later refused to be measured without AI

1. Title as claim. The only randomised field trial with experienced developers found a gap of about 40 points between felt and measured speed. Its sequel could not produce a clean number, and the reason is itself evidence of value.

2. Number or data series.
   - METR 2025 trial [@becker2025measuring] (primary): 16 experienced open-source developers, 246 real tasks of about two hours, randomised to AI allowed or not. Forecast before: 24% faster. Belief afterwards: 20% faster. Measured: 19% slower. Outside forecasts: economists 39% faster, machine-learning experts 38% faster. Chart: three bars (forecast, felt, measured).
   - METR 2026 update [@metr2026changing] (primary), change in task time with AI, with 95% intervals: original study +19% (+2 to +39); returning developers -18% (-38 to +9); new developers -4% (-15 to +9). Negative means faster. Both new intervals include zero. Design: 57 developers (10 returning, 47 new), 143 repositories, more than 800 tasks, pay $50 an hour instead of $150. Between 30% and 50% of developers withheld tasks they did not want to do without AI. Chart: three points with intervals and the annotation "30 to 50% withheld tasks".
   - METR self-report survey, February to April 2026 [@metr2026technical] (primary): 349 technical workers, median self-reported gain of 1.4 to 2 times in the value of work and 3 times in speed.
   - Other randomised studies: Google, 96 engineers, one enterprise task, about 21% faster, not significant at the 5% level [@arxiv2024muchai] (primary); three field experiments at Microsoft, Accenture and a Fortune 100 firm, 4,867 developers, 26.08% more completed tasks with a standard error of 10.3 [@cui2025effects] (primary). No randomised study of 2026 tools was found.
   - Slide number: the pair "felt 20% faster, measured 19% slower", labelled 2025. This is one of the cases where the number is the story.

3. Quotes (all checked with `verify_quotes.py`).
   - "it's like trying to get across the city walking when all of a sudden I was more used to taking an Uber." [@metr2026changing]. Speaker: an unnamed developer in METR's second study, explaining why he or she would not do some tasks without AI. Role and interest: study participant, paid by the hour; no stake in the result. Local file: `converted/web/metr_uplift.md`. Result: EXACT.
   - "we believe that the data from our new experiment gives us an unreliable signal of the current productivity effect of AI tools" [@metr2026changing]. Speaker: METR. Role and interest: non-profit evaluator that works with AI labs. Local file: `converted/web/metr_uplift.md`. Result: EXACT.
   - Checked and held in reserve: "our data is only very weak evidence for the size of this increase" (same file, EXACT); "found that people overestimated AI's effect on their time spent on tasks by 40 percentage points on average" [@metr2026technical], `converted/web/A_metr_2026-05-11-ai-usage-survey.md`, EXACT.

4. Example or case. The sequel is the case. METR lowered the pay, recruited 47 new developers and found that a growing share would not take part at all because they did not wish to work without AI; one developer completed none of the tasks where AI was disallowed. METR's position is that developers are probably faster now than in early 2025 and that its data cannot say by how much.

5. Counter-evidence, in proportion. The 2025 slowdown is one study of 16 people on large, mature repositories they knew well, with the tools of early 2025. Two other randomised studies point to a gain of 20% to 26%, with intervals that nearly touch zero. The refusal to work without AI is revealed preference, and strong: people do not give up a tool that slows them down. What survives from 2025 is the perception gap, not the sign of the effect.

6. Speaker-note material. Provenance: both METR posts read at the primary page; the paper is on arXiv. Corrections from later notes: the analysts file said that no 2026 follow-up could be found; the later files read the February 2026 update in full. The notes recommend that "19% slower" is no longer quoted as current: the METR page for the 2025 study now carries a note that METR does not believe the result reflects current tools. METR's own update opens by calling the 2025 result "a 20% slowdown"; the paper's figure is 19%. A third METR note explains why headline numbers diverge: people move their time toward tasks where AI helps, so the gain on old tasks is the smallest and the gain on new tasks the largest [@metr2026tasksubstitution] (primary). Interest: METR is funded partly through work with labs; the developers were paid.

7. Confidence and theses. High on the 2025 numbers as a dated result and on the perception gap; low on the size of the effect in 2026. Supports T1 (acceleration is felt strongly and still needs validation) and corrects any use of the 2025 result as a statement about today's tools.

8. Question for the audience. When did you last time yourself with and without it, and would you agree to work a week without it to find out?

9. Personal angle. The speaker's own statement is "I feel it accelerates my work", and the brief adds daily use and "no way back" (T17). One plain sentence: "I feel faster, and so did the developers who were measured slower; the difference is that today neither they nor I would agree to switch it off to check." Speaker to supply: one task where he could compare, even roughly, the time it took with the agent against the time it used to take.

## I3.2 Eight in ten say AI makes them more productive; the profit line has not moved in a year

1. Title as claim. Use is near universal and personal gain is reported by almost everyone, while the share of firms that see any contribution to profit is flat.

2. Number or data series. McKinsey, "The state of AI in 2026" [@mckinsey2026stateofai] (primary; full report read as converted text), 1,719 participants in 97 nations, fielded 2026-05-04 to 2026-06-08, self-reported, 36% from firms above $1bn revenue:
   - The funnel in 2026: 80% say AI improves their own productivity (C-level 80%, executives and senior managers 81%, midlevel managers 81%, individual contributors 76%); about half say it helps them make better decisions (C-level 55%, individual contributors 40%); 37% report any positive EBIT contribution; 6% are "high performers" (at least 5% of EBIT from AI, n = 92).
   - Year on year: regular AI use in at least one function 88% to 89%; scaling AI across the enterprise 38% to 44%; agents being scaled at large firms 27% to 40%, at smaller firms 22% to 22%; any EBIT contribution about 37% to 37%; high performers about 6% to 6%.
   - Headcount, expectation against outcome: 32% expected an AI-related decline within a year (2025 survey); 14% report one (2026); 39% expect one for the coming year. Software engineering alone: 31% expected, 22% reported, 36% expect (values reconstructed from a chart).
   - Cost: 20% say AI operating costs, including tokens, constrain their use.
   - Beside it, official statistics: 24.2% of US firms used AI in the last two weeks (late October 2026), up from 17.3% in December 2025 on a constant question; 44.1% of firms with 250 or more employees [@census2026btosdownloads] (primary). In the same wave, the effect on headcount over six months: 6.6% increased, 2.5% decreased, 87.3% no change.
   - And the expectation it can be set against: about 90% of CEOs expected AI agents to produce measurable returns in 2026 (BCG AI Radar, January 2026) [@bcg2026airadar] (primary). Different sample from McKinsey's.
   - Chart: descending bars 80, 50, 37, 6 ("from use to profit").
   - Slide number: none is needed if the funnel is drawn. If one number is wanted: "37%, the same as last year".

3. Quotes.
   - "Eight in ten respondents say AI has improved their own productivity." [@mckinsey2026stateofai]. Speaker: McKinsey, report summary. Role and interest: consultancy that sells AI transformation work; the survey is of its client class. Local file: `converted/reports/the-state-of-ai-in-2026-on-the-road-to-roi.md`. Result: EXACT.
   - "These individual gains have yet to translate into broad financial impact for organizations." [@mckinsey2026stateofai]. Same speaker and file. Result: EXACT.
   - Checked and held in reserve: "less than half the 32 percent who, in last year's survey, expected workforce reductions over the same period" (same file, EXACT).

4. Example or case. The build-instead-of-buy answer from the same survey shows where the gain may be going before it reaches profit: 32% say their organisation decided against buying at least one software product or feature because it could be built in-house with AI coding tools (technology companies 41%, public sector 17%). That is real activity, and it can be a single internal tool; it does not measure displaced spending.

5. Counter-evidence, in proportion. Function-level effects are reported: in software engineering 33% report a cost decrease from AI over the past 12 months and 31% a revenue increase. BCG's Applied AI Index reports that firms it classes as advanced grow revenue 2.4 times faster than laggards [@bcg2026japanese] (primary); this is a consultancy's self-assessment index and the direction of cause is not shown. A flat share of respondents does not mean a flat amount of profit. And one year is short: the survey's own high performers are the ones that redesigned workflows (nearly three quarters, against one quarter of others), which is the slow part.

6. Speaker-note material. Provenance: the web page was read first, then the full report; the later reading confirmed every headline number and dated the report to August 2026. Caveats from the full report: 87% of the AI-using respondents are managers or executives and 13% are individual contributors, so "improves my productivity" is mostly managers speaking about themselves; "EBIT impact" is a perception, not an account; year-on-year comparison uses two samples with a 552-person overlap; the report mislabels the field dates under some 2026 exhibits. Staff see it differently from executives: 47% of midlevel managers and individual contributors report at least one negative effect of AI on their own work, against 31% of executives. The Census "do not know" share rose by about 4 points when the question's term was renamed in October 2026, a small reminder that wording moves surveys. Interest: McKinsey and BCG sell the remedy for the gap they describe.

7. Confidence and theses. High that the flat EBIT share and the rising use are what the survey shows; medium that this describes firms in general (self-reported, large-firm weighted). Supports T1 in its second half and T7 by analogy (consultancy numbers serve a sale); informs T15 (expected job cuts were more than twice the reported ones).

8. Question for the audience. If four people in five are more productive and the profit share is flat, where did the time go: into more work, better work, or checking the machine's work?

9. Personal angle. The speaker says "I feel it accelerates my work" and the brief records high cognitive load, project switching and exhaustion alongside it (T17). One plain sentence: "It makes me faster, and I am not sure it has made my week shorter." Speaker to supply: what he did with the time he saved, in one concrete week.

## I3.3 The famous numbers are weaker than their fame, in both directions

1. Title as claim. "95% get zero return" and "80% of AI projects fail" do not survive a look at their sources. A vendor's return-on-investment figure, examined the same way, turns out to be one assumption multiplied by a salary.

2. Number or data series.
   - "95%": MIT Project NANDA, "The GenAI Divide" (July 2025) [@nanda2025genaidivide] (primary, PDF converted). Base: a review of over 300 public initiatives, interviews at 52 organisations, 153 survey responses collected at four conferences. Definition of success: deployment beyond pilot with measurable effect on profit and loss, measured six months after the pilot. Inside the same report: generic chatbots go from pilot to implementation about 83% of the time; 5% of custom enterprise tools reach production; external partnerships reach deployment about 67% of the time against about 33% for internal builds.
   - "80%": RAND (2024) [@ryseff2024rootcauses] (primary). The sentence is a quotation of other people's estimates; the notes trace its footnote to a 2022 magazine article. RAND's own work is 65 interviews in 2023 on why projects fail.
   - S&P Global (2025): companies abandoning most AI initiatives 17% (2024) to 42% (2025); 46% of proofs of concept scrapped [@constructiondive2025cioglobal] (secondary; primary release not read).
   - Gartner: at least 30% of generative AI projects abandoned after proof of concept by end of 2025 [@gartner2024least] (primary); no outcome data published after the deadline.
   - The vendor side, DORA and Google Cloud, "The ROI of AI-assisted Software Development" [@dora2026roiai] (primary, read as converted text). Sample calculator inputs: 500 technical staff, salary $176,000, net time saved 12.5%, licence $250 and tokens $80 per user per year, training $9,600 per user per year, a productivity dip of 15% for 3 months. Outputs: value $11,646,000 (time saved $11,000,000, extra features $990,000, downtime -$344,000); investment $8,365,000 (training $4,800,000, the dip $3,300,000, licences and tokens $165,000, infrastructure $100,000); return on investment 39%, payback 0.7 years.
   - Sensitivity of that 39% to the one input (arithmetic by the note-taker on the document's own inputs): 12.5% time saved gives 39%; 10% gives about 13%; about 8.8% gives zero; 5% gives about -40%.
   - Chart: a waterfall of the DORA sample (value, then costs), with the sensitivity as four small bars beside it.
   - Slide number: "95%" crossed out, or no number. The DORA arithmetic belongs in a backup slide.

3. Quotes.
   - "These figures are directionally accurate based on individual interviews rather than official company reporting." [@nanda2025genaidivide]. Speaker: the report's own limitations note. Role and interest: an academic-affiliated project that promotes its own agent infrastructure; the report is a preliminary version and not peer reviewed. Local file: `converted/reports/nanda_genai_divide.md`. Result: EXACT.
   - "Treat these calculations as a high-uncertainty estimate meant to spark a conversation, rather than a rigid mathematical formula." [@dora2026roiai]. Speaker: DORA and Google Cloud, note on methodology. Role and interest: Google sells AI models, cloud capacity and consulting. Local file: `converted/reports/dora-roi-of-ai-assisted-software-development-2026.md`. Result: EXACT.
   - Checked and held in reserve: "95% of organizations are getting zero return" (NANDA, same file, EXACT); "By some estimates, more than 80 percent of AI projects fail" [@ryseff2024rootcauses], `converted/web/i_rand_rra2680.md` (fetched 2026-11-17 for this check), EXACT; "The sample calculator uses a conservative estimate of 12.5% or about one hour of an eight-hour working day." (DORA, same file, EXACT).

4. Example or case. How a vendor number is built, in three steps taken from the DORA guide. First, assume each of 500 people saves one hour in eight. Second, value that hour at full salary cost: 500 times $176,000 times 12.5% is $11.0 million, which is 94% of the modelled value. Third, call it "reinvestment capacity": the guide itself says the time is reinvested and advises against cutting headcount, so the $11 million is not cash. The document is open about all of this; the 39% travels without the caveats.

5. Counter-evidence, in proportion. The weak numbers point at something real. Abandonment did rise in the S&P survey, most custom tools do stall between pilot and production in the NANDA interviews, and the DORA guide is honest that its model is a conversation starter. Its sample even shows the cost of instability (-$344,000) as smaller than the gain from extra features ($990,000). The fault lies less with the documents than with the single figure that is lifted out of them.

6. Speaker-note material. Corrections from later notes. The first benchmarks file described a "DORA 2026" report with "a sharp increase in software delivery instability", taken from a secondary summary [@kodusdoradora]. The later reading of the document shows that it is a guide with a spreadsheet model and no new data, that its empirical statements are citations of the DORA 2025 survey [@dora2025state], and that the word "sharp" does not occur in it; that phrase must not be quoted. The same notes also listed DORA among telemetry data sets; it is a survey with self-reported delivery metrics. The $80 per user per year for tokens in the DORA sample is far below what agentic use costs in 2026 and should not be cited as a cost estimate. Criticism of the NANDA report comes from blogs and trade press [@pureai2025mitnanda] [@arnondkmitnanda] [@customerthinkdebunking] (all secondary); no peer-reviewed critique and no 2026 follow-up were found. Interests: NANDA promotes agent infrastructure, Google sells the tools, S&P sells research, Gartner sells both the hype and the warning.

7. Confidence and theses. High on what the documents say and on the arithmetic; the judgment "weak" is the notes' and ours. Supports T7 (vendor analytics may be inflated) and extends it: sceptical numbers are produced with the same shortcuts. Belongs with theme I11.

8. Question for the audience. Which number about AI did you last repeat to someone, and do you know how many people were asked?

9. Personal angle. The brief asks for a meta view with as little hype as possible. One plain sentence: "The scariest number in this field rests on about a hundred and fifty questionnaires collected at four conferences, and the most comforting one on a single assumed hour a day." Speaker to supply: a number he himself used to quote and has stopped quoting, if there is one.

## I3.4 The speed gain fades after two months; the complexity stays

1. Title as claim. In open-source projects that adopted an AI coding agent, output jumped and returned to baseline within two months, while warnings and complexity rose and stayed.

2. Number or data series.
   - Carnegie Mellon study of Cursor adoption [@he2025speed] (primary; arXiv 2511.04427, published at MSR 2026): 806 GitHub repositories that adopted Cursor between January 2024 and March 2025, matched one to three with controls. Lines added: +281% in month 1, +48% in month 2, no significant gain afterwards. Static-analysis warnings +30.3% and code complexity +41.6%, both persistent. Duplication not significant. Higher complexity predicts later slowdown. Chart: velocity by month as a line that falls back to zero, with two flat bars for warnings and complexity.
   - Faros AI, "The Acceleration Whiplash" (analysis as of March 2026) [@farosai2026aiengineering] (primary, PDF read): 22,000 developers, 4,000 teams, comparison of each team's quarters of lowest and highest AI adoption. Task throughput per developer +33.7%; epics +66.2%; bugs per developer +54%; pull requests merged without review +31.3%; average pull request size +51.3%; median time in review +441.5%; incidents per pull request +242.7%; deployments per week -11% and lead time +480.4%, both on about 10% of the data. Chart: diverging bars.
   - Bain, survey of 293 senior technology leaders (2026): developers complete roughly 21% more tasks while review time rises about 91% [@bain2026technologysenior] (primary).
   - One company over time: 802 developers, 196,212 pull requests, January 2024 to April 2026; throughput up about 12% on adoption and reaching 2 times in month 10, with the load on each reviewer doubling [@arxiv2026aiwrites] (primary, abstract; not randomised).
   - Slide number: none. The picture is the line that comes back down.

3. Quotes.
   - "We find that the adoption of Cursor leads to a statistically significant, large, but transient increase in project-level development velocity, along with a substantial and persistent increase in static analysis warnings and code complexity." [@he2025speed]. Speakers: He, Miller, Agarwal, Kästner and colleagues, Carnegie Mellon University, paper abstract. Role and interest: academic researchers with no product. Local file: `converted/web/B_he_abs.md`. Result: EXACT.
   - "Our data directly contradicts DORA's 2025 findings." [@farosaiacceleration]. Speaker: Faros AI, landing page of its 2026 report. Role and interest: vendor of engineering analytics, which sells the measurement of exactly this problem. Local file: `converted/web/A_faros.md`. Result: EXACT. Use only with the vendor label.

4. Example or case. The Cursor study is the case, and it can be told without a number: the first month looks like a revolution, the third month looks like before, and the code that was added in between is still there to be maintained.

5. Counter-evidence, in proportion. The Cursor study covers adoption up to March 2025, before the agents of 2026; it detects adoption through a committed configuration file, knows nothing about how intensely the tool was used, covers open source only, and its control projects may use other AI tools. The Faros figures are correlations inside customer organisations, not a controlled comparison, and Faros lists three explanations for its churn figure as consistent with the data. On the other side, the single-company study shows throughput doubling by month 10, and DORA's 2025 survey associates AI adoption with higher delivery throughput (and with higher instability) [@dora2025state] (primary). Fading speed is established for one tool generation in open source, not as a law.

6. Speaker-note material. Corrections from later notes: the first benchmarks file described Faros lead time and deployment frequency as roughly flat, from a secondary summary; the PDF shows lead time +480% and deployments -11%, on about 10% of the data set, so these two should be left off any chart or shown with that caveat. The 2025 and 2026 Faros editions are separate cross-sections, not the same teams. Bain's 2025 edition put the gain at 10% to 15% and noted that writing and testing code is about 25% to 35% of the time from idea to launch [@bain2025technology] (primary), which is the simplest explanation of why faster coding does not become faster delivery. Interests: Faros and Bain sell remedies; the Carnegie Mellon authors do not.

7. Confidence and theses. Medium to high for the Cursor result within its scope (peer-reviewed venue, quasi-experimental design); medium for the telemetry figures (vendor, correlational). Supports T5 (generated code carries technical debt and maintenance problems) and the second half of T1.

8. Question for the audience. If the speed-up lasts two months and the code lasts ten years, which of the two are you paying for?

9. Personal angle. The brief's T1 says agents accelerate strongly yet need many iterations and expert validation, and T10 says an idea becomes a proof of concept in hours. One plain sentence: "The first version arrives in an afternoon, and I am still living with what it left behind a month later." Speaker to supply: a project of his own where the fast first version later cost time, if there is one.

## I3.5 Two developers in three use an agent every day; fewer than half trust what it writes

1. Title as claim. In one sample of developers, daily use is the norm, trust is a minority position, and the new work is reviewing.

2. Number or data series. JetBrains Developer Ecosystem Survey 2026, public raw data analysed locally [@jetbrains2026rawdata] (primary; 28,941 rows, weighted shares, base mostly developers who already use AI at work):
   - Use: 64% use a coding agent every day and 88% at least weekly (n = 19,949); 43% say at least 61% of their code is fully generated by agents; 21% write no code without AI.
   - Trust in agent output (n = 4,045): fully 2%, mostly 43%, neither 30%, mostly not 19%, not at all 5%.
   - Review (n = 16,216): always 43%, often 34%, sometimes 16%, rarely or never 8%. Share of agent code rewritten or edited by hand: midpoint mean about 34%.
   - Review effort for an AI pull request against a colleague's (n = 15,910): more 37%, the same 26%, less 30%.
   - Time: 49% spend more than a quarter of their code-related working time reviewing AI output; 20% more than half (n = 5,563).
   - New frictions (n = 3,573): more time reviewing AI artifacts 55%; more time correcting or rewriting them 40%; hard to identify errors in AI code 32%; AI-related technical debt 23%.
   - Benefits (n = 7,053): faster coding 73%; increased productivity 71%; better quality of code 36%.
   - Ownership and control: sense of code ownership decreased 46%, unchanged 37%, increased 18% (n = 3,672); sense of control over the codebase decreased 45% (n = 3,650).
   - Return, as seen from inside (n about 1,900): organisation satisfied with the return on AI coding tools 44%, dissatisfied 13%; "We don't measure ROI from AI deployments" 27%.
   - By region, Europe / North America / India / China: daily agent use 58 / 54 / 67 / 81; trust agent output 34 / 38 / 43 / 60; always review 52 / 50 / 48 / 28.
   - Chart: horizontal bars from one sample, with the question wording as labels: use daily 64, trust 45, always review 43, more review time as a new friction 55, ownership decreased 46.
   - Slide number: the pair "64% daily, 45% trust", or no number and the sentence in item 9.

3. Quotes. None could be verified. The source is a respondent-level data file; the question wordings recorded in the notes come from its codebook, which is not held as text in `converted/`. The option text "We don't measure ROI from AI deployments" is given above as recorded in the notes and is unverified: keep it off slides or paraphrase it.

4. Example or case. The delegation ladder from the same file shows where developers draw the line (delegate / keep): boilerplate 75 / 10; tests 68 / 14; refactoring 55 / 20; debugging 45 / 33; application logic 44 / 32; code review 42 / 35. Unweighted, more respondents would keep application logic and code review than would hand them over. People give away the typing first and the judgment last.

5. Counter-evidence, in proportion. The same respondents are positive on balance: 54% rate agent solutions as better than their own code, 74% say their core skills improved, and mental workload decreased for 43% against 28% for whom it increased. Other surveys agree on conditional trust more than on distrust: in Stack Overflow's 2026 survey 48.0% trust AI output when they can easily verify it and 12.3% do not trust it for most work [@stackoverflow2026developeraisection] (primary). And the picture depends on who is asked: Chinese respondents trust and delegate far more than European ones.

6. Speaker-note material. Corrections from later notes: the JetBrains blog reported 90% weekly and 68% daily use of agents among professional developers [@jetbrains2026aicoding]; the raw file gives 88% and 64% among employed respondents who answered the AI block, and 81% and 59% of all employed respondents. Use "almost nine in ten weekly, about two thirds daily, among developers who use AI at work". The blog's 50% readiness to delegate application logic is 44% in the file (36% unweighted). Caveats: a non-probability sample of a tool vendor's audience; routing means most questions were answered only by people who already use AI; weighting lifts China from 4.7% of rows to 20% of the weight, and weighted global figures on trust and delegation are 5 to 8 points above unweighted ones. For an audience in Europe or Russia the European column is the better benchmark. Russia has 58 respondents and no usable estimate. All quantities are self-reports. Interest: JetBrains sells IDEs and its own AI products, which appear as answer options.

7. Confidence and theses. Medium: primary data and exact bases, from a self-selected sample. Supports T1 (iterations and expert validation), T4 (plausible output that needs checking) and T17 (the load moves to the human). On cognitive load the same file cuts against T17: more respondents report a lower mental workload than a higher one.

8. Question for the audience. Who in this room reads every line the agent writes, and who has stopped?

9. Personal angle. The brief describes daily use, no way back, and high cognitive load from project switching (T17). One plain sentence: "I use it every day and I check everything it gives me, and the checking is now the job." Speaker to supply: whether "I check everything" is true for him, and where he has stopped checking.

## I3.6 The economy-wide estimates differ by a factor of hundreds, and the old paradox has returned under a new name

1. Title as claim. Forecasts of AI's effect on growth run from almost nothing to double digits a year, the measured macro evidence is one contested data point, and economists are replaying the argument they had about computers in 1987.

2. Number or data series.
   - Estimates converted to one axis, added annual growth in percentage points (compilation [@shenk2026productivity], secondary; conversions by the note-taker): Acemoglu about 0.07 (no more than 0.66% of total factor productivity over ten years [@acemoglu2024simple], primary abstract); McKinsey low end 0.1; OECD about 0.5 (0.4 to 1.3 for the United States in a later paper, seen only in a summary [@ceprvoxeumiracle], search-result only); Goldman Sachs 1.5; Korinek and Suh scenario 18; Epoch GATE scenario 25 by year 10. Chart: dot plot on a log scale, with the conversion stated on the slide.
   - Realised macro: Erik Brynjolfsson's own estimate of US productivity growth of about 2.7% in 2025, against 1.4% a year over the previous decade [@fortune2026brynjolfsson] (primary for Fortune's report of his op-ed).
   - Realised micro to macro: customer support +15% on average [@brynjolfsson2025generative] (primary); Danish administrative data show no effect on earnings or hours, ruling out effects above 2% two years after the launch of ChatGPT [@humlumnberw33777] (primary); a summer 2026 survey of nearly 9,000 executives finds 78% of firms using AI, essentially no net effect on firm employment over three years and reported productivity growth of +0.2% a year [@nberw34836] (primary).
   - History: about 40 years for electrification and about 20 for computerisation to show in the aggregate [@shenk2026productivity] (secondary). The productivity J-curve paper found adjusted productivity 15.9% above official measures at the end of 2017 [@brynjolfsson2018productivity] (primary abstract).
   - Slide number: none. The spread itself is the message: "from 0.07 to 25".

3. Quotes.
   - "AI is everywhere except in the incoming macroeconomic data" [@fortune2026brynjolfsson]. Speaker: Torsten Slok, chief economist of Apollo, as quoted by Fortune. Role and interest: asset manager's economist who speaks to investors; his autumn 2025 reading of an adoption plateau did not hold. Local file: `converted/web/i_fortune_jcurve.md` (fetched 2026-11-17 for this check; the page is cut short, so only its opening section was available). Result: EXACT.
   - "The updated 2025 US data suggests we are now transitioning out of this investment phase into a harvest phase where those earlier efforts begin to manifest as measurable output" [@fortune2026brynjolfsson]. Speaker: Erik Brynjolfsson (Stanford), from his Financial Times op-ed as quoted by Fortune. Role and interest: academic who also has commercial interests in AI workforce analytics. Same local file. Result: EXACT. Fortune adds that he cautions that several more periods of sustained growth are needed to confirm a trend.

4. Example or case. Robert Solow's remark of 1987, that the computer age was visible everywhere except in the productivity statistics, is the template (paraphrased here; the original is not held locally). Slok's sentence is a deliberate echo of it, and Fortune says so. The computer paradox resolved itself about a decade later, after firms had reorganised around the machines. Whether this one resolves faster, slower or not at all is what the two quoted economists disagree about.

5. Counter-evidence, in proportion. Individual uptake is faster than for any earlier general-purpose technology: 53% of the population within three years [@stanfordhai2026aitakeaways] (primary). Investment has moved on a scale the 1980s never saw: global corporate AI investment of $581.7bn in 2025, up 130% (same source). Goldman Sachs's chief economist is reported to have said that the effect of AI investment on US growth in 2025 is much smaller than often perceived, because much of the spending adds to output in Taiwan and Korea (secondary report, no key yet, see Bibliography additions). So the same year has a "take-off" reading and a "not in the data" reading, and the data do not yet separate them.

6. Speaker-note material. The figures must not be put on one axis without relabelling: Acemoglu's is a cumulative level over ten years, Goldman's and the OECD's are annual increments. Corrections from later notes: the compilation gives Acemoglu as 0.71%; the paper's abstract says no more than 0.66% (and under 0.53% after an adjustment), so 0.66% is used. The phrase "basically zero" attributed to Goldman's economist was an outlet's headline, not his wording. The J-curve paper was read only as a summary page [@causalclaimsnberw25148]. No official 2026 US productivity release was checked, so it is not known whether the 2.7% held through revisions. Interests: banks and asset managers talk their book, consultancies size the prize, scenario modellers are funded to explore extremes, and Brynjolfsson has a company in the field.

7. Confidence and theses. High that the spread is this wide and that the macro evidence is thin; low on which end is right. Supports T15 (open question, shocks before stabilisation) and frames T1: a revolution at the desk can coexist with flat aggregates for years.

8. Question for the audience. In 1987 the computers were everywhere except in the statistics, and ten years later they were in the statistics. What would you have done differently in 1987 if you had known?

9. Personal angle. The speaker's statement is "I feel it accelerates my work". One plain sentence: "I feel it every day, and the economists cannot find it yet; both can be true for a long time." No further first-person story is needed here.

## Quote verification record

All quotes were checked on 2026-11-17 with `python3 /Users/andy/_code/_EDU/msd_review/scripts/verify_quotes.py <file> -`. "EXACT" means a contiguous match after the script's normalisation (the script prints this case as VERIFIED without the "interleaved" remark). The haystacks carry no `converted-by` stamp, so the script reports the converter as unknown.

| Quote (first words) | Key | Local file | Result |
|---|---|---|---|
| "it's like trying to get across the city walking..." | metr2026changing | converted/web/metr_uplift.md | EXACT |
| "we believe that the data from our new experiment..." | metr2026changing | converted/web/metr_uplift.md | EXACT |
| "our data is only very weak evidence..." | metr2026changing | converted/web/metr_uplift.md | EXACT (reserve) |
| "found that people overestimated AI's effect..." | metr2026technical | converted/web/A_metr_2026-05-11-ai-usage-survey.md | EXACT (reserve) |
| "Eight in ten respondents say AI has improved their own productivity." | mckinsey2026stateofai | converted/reports/the-state-of-ai-in-2026-on-the-road-to-roi.md | EXACT |
| "These individual gains have yet to translate..." | mckinsey2026stateofai | same | EXACT |
| "less than half the 32 percent who..." | mckinsey2026stateofai | same | EXACT (reserve) |
| "These figures are directionally accurate..." | nanda2025genaidivide | converted/reports/nanda_genai_divide.md | EXACT |
| "95% of organizations are getting zero return" | nanda2025genaidivide | same | EXACT (reserve) |
| "By some estimates, more than 80 percent of AI projects fail" | ryseff2024rootcauses | converted/web/i_rand_rra2680.md | EXACT (reserve) |
| "Treat these calculations as a high-uncertainty estimate..." | dora2026roiai | converted/reports/dora-roi-of-ai-assisted-software-development-2026.md | EXACT |
| "The sample calculator uses a conservative estimate of 12.5%..." | dora2026roiai | same | EXACT (reserve) |
| "We find that the adoption of Cursor leads to..." | he2025speed | converted/web/B_he_abs.md | EXACT |
| "Our data directly contradicts DORA's 2025 findings." | farosaiacceleration | converted/web/A_faros.md | EXACT |
| "AI is everywhere except in the incoming macroeconomic data" | fortune2026brynjolfsson | converted/web/i_fortune_jcurve.md | EXACT |
| "The updated 2025 US data suggests we are now transitioning..." | fortune2026brynjolfsson | converted/web/i_fortune_jcurve.md | EXACT |

Short phrases inside the running text were checked the same way and are EXACT: "a 20% slowdown" (`converted/web/metr_uplift.md`); "reinvestment capacity" (`converted/reports/dora-roi-of-ai-assisted-software-development-2026.md`); "harvest phase" (`converted/web/i_fortune_jcurve.md`).

Not used, or unverified and to be kept off slides:

- Slok's second remark in the notes, on a possible J-curve effect for AI, was not found in the fetched copy of the Fortune page, which is cut short. Not used.
- Solow's 1987 sentence is paraphrased; the original is not held locally.
- JetBrains question and option wordings come from the notes' reading of the codebook, not from a local text copy. Unverified.
- "a sharp increase in software delivery instability" is not in the DORA guide and must not be quoted (see I3.3, item 6).

## Bibliography additions needed

- Report of Jan Hatzius (Goldman Sachs chief economist) at the Atlantic Council on the contribution of AI investment to US GDP growth in 2025: Tom's Guide, about 2026-02-24 (reached through a Google News redirect; Washington Post, 2026-02-23, seen as a headline). Proposed key: `tomsguide2026hatzius`. Strand `4.economics` (also `1.analysts`). Verification: secondary. Interest: press reporting an investment bank's economist. Source of the metadata: `gaps_economics_analysts.md`, section 3. The canonical URL is not recorded in the notes.
- Robert M. Solow, "We'd Better Watch Out", New York Times Book Review, 12 July 1987, p. 36. Proposed key: `solow1987watch`. Metadata from general knowledge, not from a page read in this project. Needed if the Solow remark is to be cited instead of paraphrased.
- The METR blog page of the 2025 trial (2025-07-10, https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), which according to the notes now carries a note that METR no longer believes the result reflects current tools. The paper has the key `becker2025measuring`; the blog page with the note has none. Proposed key: `metr2025earlyblog`. Strand `2.benchmarks`. Verification: primary per `benchmarks_vs_reality.md`. No local copy was found.
- `file` fields that can now be filled: `fortune2026brynjolfsson` has a local copy at `converted/web/i_fortune_jcurve.md` (partial page) and `ryseff2024rootcauses` at `converted/web/i_rand_rra2680.md` (both scraped 2026-11-17).
- Title corrections: none. The scraped copy of the Fortune article does not carry its headline, so the bracketed descriptive title of `fortune2026brynjolfsson` stays. The keymap marks that entry "primary"; it is a primary read of Fortune and a secondary source for Brynjolfsson's op-ed and for Slok's remark, which the bibliography note could say.

## Open points

- No randomised estimate exists for the tools of 2026. METR's position (probably faster than in early 2025, size unknown) is the best available statement.
- Whether the 2025 perception gap of about 40 points still holds is untested; the 2026 self-report survey (3 times faster) has no measured counterpart.
- McKinsey's flat 37% is a share of respondents who perceive a profit contribution. No audited figure for profit from AI across firms is in the notes.
- The "80%" trace to a 2022 magazine article is from the notes' reading of RAND's footnote; the fetched RAND page confirms the sentence, and the footnote text was not re-read.
- The DORA sensitivity figures are the note-taker's arithmetic, not the document's. The document prints no publication date.
- The Cursor study ends in March 2025 and concerns one tool in open source; no replication for agents of 2026 is in the notes.
- Faros lead time and deployment figures rest on about 10% of its data; its comparison with 2025 is called directional by Faros itself. Faros and DORA contradict each other on whether mature organisations are protected.
- JetBrains: non-probability sample, strong weighting effect, self-reports; the composition of about 6,900 extra rows in the public file is unknown.
- Macro: the 2.7% US productivity figure for 2025 is one economist's estimate and was not checked against later official releases; the OECD and IMF ranges were seen only in summaries; the origin of the 0.71% Acemoglu figure in the compilation was not traced.
- Contested: whether the gap between felt and booked productivity is a lag (the J-curve reading) or a ceiling (the "normal technology" and Acemoglu reading). The notes do not settle it.

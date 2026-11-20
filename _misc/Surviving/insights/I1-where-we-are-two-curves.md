# I1. Where we are: two curves

Theme file for the talk "Agentic AI impact on the IT industry". Sources: `research_notes/Agentic AI impact on IT industry/` (mainly `analysts_adoption_hype.md`, `gaps_economics_analysts.md`, `gaps_benchmarks.md`, `benchmarks_vs_reality.md`), read on 2026-11-17. Where a later notes file corrects an earlier one, the later value is used and the correction is recorded in item 6 of the insight. Verification levels in brackets are those of `references_keymap.tsv`.

## Five-line summary

1. The one thing to remember: capability is still climbing steeply where answers can be checked, expectations are at or just past their peak, and what firms have booked as profit is far below both. The gap between the curves is where the hype and the disappointment both come from.
2. The best story: the people who drew the most famous progress curve in AI stopped updating it in September 2026, because their test tasks top out at about 16 hours and the newest models are beyond that.
3. The best picture: one slide with a rising S-shaped capability line whose top part is dashed ("not measured"), a hype curve drawn over it, and a "we are here" band instead of a dot.
4. The best question for discussion: if the same model finishes a day-long task at coin-flip odds and only an hour-long task at four-in-five odds, which of the two numbers describes your work?
5. What the speaker should not claim: that capability has flattened (nobody has measured a plateau), that it will keep doubling (the instrument is saturated and the evidence is partly redacted), or that the Gartner curve is a measurement (it is an analyst's schematic).

## I1.1 The people who measure the curve stopped measuring, because their ruler ran out

1. Title as claim. The most quoted curve of AI progress has no data points after April 2026: the measuring instrument is saturated, the trend is not known to have stopped.

2. Number or data series. METR 50% time horizon (the length of task, in human expert time, that a model completes in half of the attempts), from METR's raw data file [@metrrawbenchmark] (primary) and the Time Horizon 1.1 post [@metr2026timehorizon] (primary):
   - GPT-4 (March 2023): 3.5 minutes
   - Claude 3.7 Sonnet (February 2025): 1.0 h
   - o3 (April 2025): 2.0 h
   - GPT-5 (August 2025): 3.4 h (95% interval 1.9 to 6.8)
   - Claude Opus 4.5 (November 2025): 4.9 h (2.7 to 10.4)
   - GPT-5.2 (December 2025): 5.9 h (3.3 to 13.6)
   - Claude Opus 4.6 (February 2026): 12.0 h (5.3 to 60.6)
   - Gemini 3.1 Pro (February 2026): 6.4 h (3.9 to 11.6)
   - GPT-5.4 (March 2026): 5.7 h (3.1 to 12.8)
   - Claude Mythos Preview, early snapshot (April 2026): 17.4 h (8.5 to 55.1), above the 16-hour line that METR calls unreliable
   - Doubling time: 187.8 days over the whole series, 128.7 days since 2023 (interval 104.4 to 158.0), both excluding points above 16 hours. The TH1.1 post also gave 88.6 days for the trend since 2024.
   - Chart: log scale, a horizontal line at 16 hours, a shaded zone above it labelled "instrument saturated", and the note "series ends April 2026".
   - Slide number, if one is wanted: "16 hours", the point where the ruler ends. The doubling time is backstage.

3. Quotes (all checked with `verify_quotes.py`).
   - "Measurements above 16 hrs are unreliable with our current task suite" [@metr2026taskcompletion]. Speaker: METR, on its own tracking page. Role and interest: non-profit evaluator, partly funded through work with AI labs. Local file: `converted/web/metr_th.md`. Result: EXACT.
   - "Clarified that this page is no longer actively updated." [@metr2026taskcompletion]. Same page, update note dated September 8th, 2026. Local file: `converted/web/metr_th.md`. Result: EXACT.

4. Example or case. In the last six months of the series the picture stops being a line. GPT-5.6 Sol (evaluated 2026-06-26) comes out at 11.3 hours if attempts to cheat the grader count as failures and at more than 270 hours if they count as successes, and METR says it does not consider any of these numbers reliable [@metr2026evaluation] (primary). No time horizon exists on the page for any model released after April 2026 [@metr2026taskcompletion].

5. Counter-evidence, in proportion. Saturation of one instrument is not silence about progress. On paid freelance projects the Remote Labor Index went from 2.5% (October 2025) to 15.8% (mid-2026) to 41.25% (November 2026) on the official board [@scaleaileaderboard] (primary), and METR's own assessment of one lab in November 2026 found progress on well-specified tasks at about twice the earlier rate [@metr2026independent] (primary). So the honest reading is "unmeasured at the top", not "stopped". Against the instrument itself: a validity critique argues the human baselines are thin (about three baseliners per task, recruited through METR's network) [@witkin2026against] (primary); this questions the ruler, not the direction.

6. Speaker-note material. Provenance: METR page and raw YAML read at source on 2026-11-17. Corrections from later notes: the analysts file gave Opus 4.6 as "about 14.5 hours" from a secondary article [@officechai2026claude]; the raw file gives 12.0 h. The analysts file gave the since-2023 doubling time as 130.8 days; the raw file gives 128.7 days after METR corrected "a regularization mistake" on 2026-03-03. The Mythos point was a lower bound of 16 hours from trade press [@decoder2026metrclaude]; the raw file gives 17.4 h with the interval above. Opus 4.5 appears as 5.3 h in the January post, 4 h 49 min in the limitations note and 4.9 h in the data file: the estimate moves with analysis choices, which METR documents itself [@metr2026timehorizontask]. Interest: METR works with the labs on pre-release evaluations. The model release months come from the raw file.

7. Confidence and theses. High that the series ends in April 2026 and that the page is no longer maintained. Medium on any statement about the trend after that date. Supports T3 (benchmarks are revealing and also run out); corrects any reading of T1 that rests on "the curve keeps doubling" as a measured fact for late 2026.

8. Question for the audience. If the best instrument we had cannot read the newest models, what are the confident forecasts on both sides reading?

9. Personal angle. From the brief, the speaker uses these tools daily and sees no way back (T17). One plain sentence: "The people who measured this curve stopped measuring in September, so from here I trust what I see in my own work more than any chart." Speaker to supply: a moment in the past year when a new model release visibly changed what he could hand over, or failed to.

## I1.2 At coin-flip odds an agent works for a day; at four-in-five odds, for about an hour

1. Title as claim. The famous curve is drawn at 50% success. At the reliability a business process needs, the reach is five to ten times shorter.

2. Number or data series. METR 50% horizon against 80% horizon for the same model [@metrrawbenchmark] (primary):
   - GPT-5: 3.4 h against 38 min
   - Claude Opus 4.5: 4.9 h against 49 min
   - GPT-5.2: 5.9 h against 66 min
   - Claude Opus 4.6: 12.0 h against 70 min (80% interval 27 min to 2.8 h)
   - Gemini 3.1 Pro: 6.4 h against 90 min
   - GPT-5.4: 5.7 h against 54 min
   - Claude Mythos Preview (early): 17.4 h against 3.1 h (1.6 to 6.6)
   - Chart: paired bars per model, with the note "series ends April 2026".
   - Slide number: the pair "12 hours at 50%, 70 minutes at 80%" for one model. This is one of the few pairs that is the story by itself.
   - Beyond 80%: METR does not report a 99% horizon because it "would require many more tasks" [@metr2026taskcompletion]. Toby Ord's approximation puts the 90% horizon at about one seventh and the 99% horizon at about one seventieth of the 50% horizon [@ord2025there] (primary); he corrected the underlying assumption in 2026 and now calls 99% horizons "deeply uncertain" [@ord2026hazard] (primary).

3. Quotes.
   - "An 8-hour time horizon does not mean that AIs can do 8 hours of work that a (high-context) human professional can do as part of their day-to-day job." [@metr2026taskcompletion]. Speaker: METR, page FAQ. Role and interest: non-profit evaluator that works with the labs. Local file: `converted/web/metr_th.md`. Result: EXACT.
   - "nearly two years of rapid capability progress have produced only modest reliability gains" [@kapoor2026paper]. Speaker: Sayash Kapoor (Princeton), announcing a paper with co-authors. Role and interest: academic, co-author of a book and newsletter built on the sceptical "normal technology" position. Local file: `converted/web/f_nt_reliab.md`. Result: EXACT. The authors call the findings tentative.

4. Example or case. For GPT-5 on tasks of 1.5 to 3 hours, METR reports that about one third of tasks always succeed, one third always fail and one third vary from run to run [@metr2026taskcompletion] (primary). That is what 50% means in practice: not "half done", but "you do not know in advance which half".

5. Counter-evidence, in proportion. The 80% horizon is also rising: from 12 minutes (Claude 3.7 Sonnet, February 2025) to 3.1 hours (Mythos Preview, April 2026) in the same file. Where the result can be checked mechanically, long runs already work with light supervision: an independent benchmark had a model reimplement a 16,000-line toolkit from behaviour alone, a task its authors guess at 2 to 17 human weeks [@epochai2026metrmirrorcode] (primary). The limit is reliability on tasks without an automatic check, not ability as such.

6. Speaker-note material. Provenance: raw data file read at source. The time horizon measures task difficulty in human time, not how long the agent runs; tasks are self-contained and well specified, closer to what a new hire with no context could do. On visual computer-use tasks METR reports horizons 40 to 100 times lower [@metr2026limitations] (primary). Ord's first essay should be cited together with his own correction, not alone. The reliability paper itself [@arxiv2026science] was not opened; the figures come from the authors' post. Earlier note corrected: `benchmarks_vs_reality.md` gave "80% horizon about 1.5 h against 12 h" from a secondary overview; the raw file gives 70 minutes against 12.0 h for Opus 4.6.

7. Confidence and theses. High for the paired values (primary data), medium for anything beyond 80%. Supports T1 (strong acceleration that still needs iterations and expert validation) and T4 (probabilistic output); it gives T13 a mechanism (where checking is hard, the short horizon is the one that counts).

8. Question for the audience. For the work you are responsible for, which success rate would you sign for: one in two, four in five, or ninety-nine in a hundred?

9. Personal angle. T1 in the brief already says it: agents accelerate strongly, yet need many iterations and expert validation. One plain sentence: "It can do a day of my work, and I cannot tell in advance which half of the day I will have to redo." Speaker to supply: a recent task where the agent's result looked finished and an expert check found the gap.

## I1.3 Capability is still accelerating, but only where the answer can be checked automatically

1. Title as claim. Every public measure that shows acceleration measures code, mathematics or other verifiable tasks. Outside that zone the evidence is thin or flat.

2. Number or data series.
   - Epoch AI, "Have AI capabilities accelerated?" (2026-04-16): three of four metrics show strong evidence of acceleration against a linear trend from 2023; the break is around 2024; reasoning models run roughly 2 to 3 times faster than non-reasoning models; the fourth metric (WeirdML V2) shows no acceleration [@denain2026aicapabilities] (primary).
   - METR, independent assessment of one lab (2026-11-05): progress on well-specified tasks at 1.9 times the rate of March 2024 to October 2025, 95% interval 1.5 to 2.8 [@metr2026independent] (primary).
   - Remote Labor Index, share of real paid freelance projects delivered at client-acceptable quality: 2.5% (October 2025), 4.17%, 8.33%, 15.83% (mid-2026), 21.25% (September 2026), 41.25% (November 2026) [@scaleaileaderboard] (primary). Only the first and last dates are firm; the board has no row dates and no confidence intervals; one project is 0.42 points.
   - Stanford AI Index 2026: Terminal-Bench from 20% (2025) to 77.3%; robots succeed at 12% of real household tasks [@stanfordhai2026aitakeaways] (primary).
   - AI Futures Project, grading its own fast scenario: progress on quantitative metrics at roughly 65% of the predicted pace, about 75% by July 2026 [@aifutures2026grading] (primary).
   - Chart: RLI as a step chart, with "59% of projects still not delivered" written on it so that both readings are visible.
   - Slide number: none needed. If one is wanted, "2.5% to 41% in thirteen months", said aloud with the second half of the sentence: "and most projects still fail".

3. Quotes.
   - "Anthropic redacted a majority of the evidence we found most informative for these conclusions." [@metr2026independent]. Speaker: METR, redaction summary of its own assessment. Role and interest: non-profit evaluator working under an agreement with the lab it assessed. Local file: `converted/web/i_metr_anthropic_assessment.md` (fetched 2026-11-17 for this check). Result: EXACT.
   - "Babies don't keep doubling forever, and nor will AI progress." [@marcus2026misplaced]. Speaker: Gary Marcus. Role and interest: author and entrepreneur, a committed sceptic of scaling. Local file: `converted/web/f_marcus_misplaced.md`. Result: EXACT. In the same post he concedes that Claude Code is a real advance.
   - Checked and held in reserve: "we would not be surprised if the true acceleration was closer to 1.3x or 3x the historical rate" [@metr2026independent], same file, EXACT.

4. Example or case. METR's note of August 2026 on discoveries: the discovery of cyber vulnerabilities has accelerated sharply in its assessment, mathematics somewhat, and optimisation discoveries have not shown a dramatic acceleration [@metr2026seenacceleration] (primary). The order follows how cheaply a result can be verified.

5. Counter-evidence, in proportion. No named 2026 source shows that measured capability has flattened (`gaps_economics_analysts.md`, section 6). The sceptical arguments are of other kinds: reliability improves more slowly than accuracy [@kapoor2026paper], the headline metric overstates practical reach and its cost rises [@ord2025costs], and Yann LeCun calls extending language models to human-level intelligence "complete nonsense" [@wired2026yannlecun] (secondary), which is a claim about an architecture's ceiling by the founder of a company built on another approach. On the other side, the authors of the fast scenario forecast a superhuman AI researcher in 2027 on the strength of the METR assessment [@aifutures2026forecasts] (primary); this is a forecast by interested authors, not a measurement.

6. Speaker-note material. Label the stakes symmetrically: Marcus and LeCun have a stake in the sceptical case, AI Futures and lab-commissioned assessments in the fast case. Epoch states its own caveat: the accelerating metrics are concentrated in programming and mathematics and may not generalise to tasks that are harder to verify. The METR assessment covers one lab and verifiable tasks, with most of the supporting evidence redacted at the lab's request. Correction from later notes: the analysts file took the Remote Labor Index top rows as possibly "provider self-reports per one aggregator"; the official Scale board shows them with manual expert grading and marks no row as self-reported. The CAIS mid-2026 figure is 15.8%, not 16.1%. Marcus predicted a Remote Labor Index score "under 20% and perhaps under 10%" for the Mythos model; which board row, if any, corresponds to that model was not established, so the prediction must not be scored on a slide.

7. Confidence and theses. High that measured capability on checkable tasks has not flattened. Low on how far this carries into judgment-heavy and physical work. Supports T1 and T13; qualifies T3 (benchmarks are inflated in places, and the fresh ones still show real gains).

8. Question for the audience. Which part of your job has an automatic check, and which part only a person who knows the context can judge?

9. Personal angle. The brief lists the speaker's daily use for office, admin, teaching and research work (T17), which is mostly work without an automatic check. One plain sentence: "It gets better fastest at the things a machine can verify, and most of my day is not that." Speaker to supply: one task of his own that became routine for an agent this year and one that did not move.

## I1.4 Expectations are at or just past the peak, and the forecaster hedges in both directions

1. Title as claim. Gartner places AI agents at the Peak of Inflated Expectations or just past it, and publishes a large adoption forecast and a large cancellation forecast at the same time.

2. Number or data series.
   - Placement. 2025 Hype Cycle for AI: AI agents at the Peak [@gartner2025hypecycle] (primary). 2026 Hype Cycle for Agentic AI: "at the Peak" [@gartner2026hypecycleagentic] (primary). 2026 Hype Cycle for AI graphic, read as an image: AI agents and multimodal AI just past the Peak, on the way down, both labelled 2 to 5 years [@gartner2026hypecycleartificial] (primary, image).
   - The pair Gartner repeats: 17% of organisations have deployed AI agents; more than 60% expect to within two years; more than 40% of agentic projects are expected to be cancelled by the end of 2027 [@gartner2026latest] (primary). Three bars with three different bases; label each.
   - Forecast ladder, failure side: at least 30% of generative AI projects abandoned after proof of concept by end of 2025 (made July 2024) [@gartner2024least]; more than 40% of agentic projects cancelled by end of 2027 (June 2025, restated unchanged in 2026) [@gartner2025agenticcancel]; 70% of enterprises abandon agentic AI built by vendor engineers by 2028 (September 2026) [@gartner2026enterprises] (all primary).
   - Forecast ladder, adoption side: 40% of enterprise applications with task-specific agents by end of 2026 [@gartner2025enterprise]; 33% of enterprise software with agentic AI and 15% of daily work decisions made autonomously by 2028 [@gartner2025agenticcancel]; 80% of common customer service issues resolved autonomously by 2029 [@gartner2025agentic] (all primary).
   - Slide number: "17%" (deployed) if any. The ladders are backup material.

3. Quotes.
   - "Agentic AI sits at the Peak of Inflated Expectations, reflecting extraordinary market attention and aggressive adoption intent." [@gartner2026hypecycleagentic]. Speaker: Gartner, article on its 2026 Hype Cycle for Agentic AI. Role and interest: advisory analyst that sells research and conferences to buyers and vendors; both the hype and the warning create demand. Local file: `converted/web/gartner_agentic_hc.md`. Result: EXACT.
   - "Concerns about GenAI have shifted from model capability to application reliability and return on investment." [@gartner2026latest]. Speaker: Gartner, article on the 2026 Hype Cycle for AI. Same interest. Local file: `converted/web/gartner_ai_hc.md`. Result: EXACT.
   - Checked and held in reserve: "most deployments remain narrowly scoped, and fully autonomous agents are not ready for the majority of enterprise use cases" [@gartner2026hypecycleagentic], `converted/web/gartner_agentic_hc.md`, EXACT.

4. Example or case. In June 2025 Gartner named "agent washing" (existing assistants and chatbots relabelled as agents) and estimated that only about 130 of the thousands of agentic AI vendors were real [@gartner2025agenticcancel] (primary). A year later its own survey shows 17% deployed, and its AI Hype Cycle is organised around cost and control.

5. Counter-evidence, in proportion. Other surveys put agent use higher, with other definitions: McKinsey reports agents being scaled at 40% of firms above $1bn revenue (27% a year earlier) and 22% of smaller firms [@mckinsey2026stateofai] (primary); BCG's employee survey has agents integrated into workflows at 30% (13% in 2025, wording differs) [@bcg2026aiwork] (primary); Deloitte has 23% using agentic AI at least moderately [@techstrongaideloitte] (secondary). So "17%" is the low end of a cluster, and the definition moves the number. Also, none of Gartner's forecasts has been scored by Gartner, including the one whose deadline passed at the end of 2025.

6. Speaker-note material. Correction from later notes: the analysts file said agents had sat "at the Peak" for two consecutive years. The 2026 AI Hype Cycle graphic, read later, shows AI agents just past the Peak, while the separate agentic cycle still says "at the Peak". "At or just past the Peak" is the accurate wording. Generative AI itself was reported in the Trough of Disillusionment on the 2025 cycle by trade press [@zdnet2025synthetic] (secondary); its 2026 position is not established. The cancellation forecast rests on a January 2025 poll of 3,412 webinar attendees, a self-selected sample. The Hype Cycle is a schematic drawn by analysts, with no measured vertical axis. The sample size of the 2026 CIO survey behind "17%" is not on the public page. The four predictions that the analysts file held "from memory" were later confirmed on gartner.com.

7. Confidence and theses. High on the placement and the published figures; low on whether any of the forecasts will hold. Supports T7 in a wider sense (who publishes which numbers, and why) and belongs with theme I11.

8. Question for the audience. When one firm predicts both that everyone will deploy agents and that four in ten projects will be cancelled, what would it take for that firm to be wrong?

9. Personal angle. The brief asks for as little hype as possible and a view from above. One plain sentence: "Even the people who draw the hype curve say we are at the top of it, and they are already selling the map of the way down." No first-person story is needed here.

## I1.5 Individuals adopted in three years; organisations take decades, as they did with electricity and computers

1. Title as claim. The capability curve and the adoption curve run on different clocks. The second one has always been slow, and nothing in 2026 shows it to be different this time.

2. Number or data series.
   - Individuals: generative AI reached 53% population adoption within three years, faster than the personal computer or the internet [@stanfordhai2026aitakeaways] (primary).
   - Firms, constant question since December 2025 (US Census, share of firms that used AI in the last two weeks): 17.3% (December 2025), 17.7% (January 2026), 19.5%, 21.5%, 23.8%, 24.2% (late October 2026). By size in the latest wave: 250 or more employees 44.1%; 100 to 249: 40.0%; 50 to 99: 33.2%; 20 to 49: 29.2%; 10 to 19: 25.3%; 5 to 9: 23.4%; 1 to 4: 22.8% [@census2026btosdownloads] (primary).
   - Profit: 37% of McKinsey respondents attribute any EBIT contribution to AI, unchanged from 2025; high performers 6%, unchanged [@mckinsey2026stateofai] (primary). Detail in theme I3.
   - History: integration took about 40 years for electrification and about 20 for computerisation [@shenk2026productivity] (secondary compilation). The productivity J-curve: complementary intangible investment makes measured productivity understate early and overstate later [@brynjolfsson2018productivity] (primary for the paper's existence and abstract; the notes read a summary page).
   - Chart: the Census line from 17.3% to 24.2% with the size split as bars beside it. Mark the older series (about 10%, different question) separately and do not join it.
   - Slide number: none. Say "one firm in four" aloud.

3. Quotes.
   - "the speed of diffusion is inherently limited by the speed at which not only individuals, but also organizations and institutions, can adapt to technology" [@narayanan2025ainormal]. Speakers: Arvind Narayanan and Sayash Kapoor (Princeton), essay for the Knight First Amendment Institute. Role and interest: academics whose book and newsletter are built on this position. Local file: `converted/web/f_normaltech_essay.md`. Result: EXACT.
   - "valuations are not stretched. P/E ratios actually have fallen because earnings keep surprising to the upside." [key needed, see Bibliography additions]. Speaker: Athanasios Vamvakidis, Deputy Director, IMF, at the press briefing for the October 2026 Global Financial Stability Report. Role and interest: intergovernmental lender with a surveillance mandate. Local file: `converted/web/c_imf_brief.md`. Result: EXACT. Use for the dot-com comparison only; in the same answer he calls the falling price-to-earnings ratio "the key difference" from the dot-com bubble and adds that it becomes increasingly difficult for earnings to keep beating forecasts.

4. Example or case. The dot-com years are the analogy the audience will bring. The notes hold two official statements: the IMF's, above, that the difference from 2000 is earnings that keep beating forecasts; and the Bank of England's, that one valuation measure for the S&P 500 has edged down "towards levels not seen since the dot-com bubble" [@bankofengland2026financial] (primary). A fair formulation is the one from the notes: a financial correction and a lasting technology shift are compatible, as they were in 2000 to 2002. The talk gives no investment advice, so this is said once and left.

5. Counter-evidence, in proportion. The authors of the fast scenario reply that the pace of adoption will be set by the most aggressive adopters, not by the average organisation [@aifutures2025aiprofoundly] (primary; paraphrase, the wording was not checked against a local copy). The Census series is not flat: 17.3% to 24.2% in eleven months on a constant question is fast for firm-level adoption. Erik Brynjolfsson reads the 2025 US productivity data as the start of the "harvest phase" [@fortune2026brynjolfsson] (detail and quotes in I3.6). So "slow" means slower than the capability curve, not standing still.

6. Speaker-note material. Corrections from later notes: the analysts file reported the national rate as flat at 17% to 20% from December 2025 to May 2026 and flagged the October 2026 wording change as unconfirmed. The later file confirms both wording changes on census.gov. The first (from the 2025-11-17 collection) broadened the question from "producing goods or services" to "any of its business functions" and opened a new series [@census2025btosai] [@censusbtosbusiness]. The second (from the 2026-10-19 collection) only renamed the term, following an executive order; the "yes" share did not move and "do not know" rose by about 4 points. Apollo's autumn 2025 chart of adoption flattening [@slok2025academy] did not survive the broader question. The dot-com comparison in the analysts file was an inference without a source; the IMF and Bank of England statements now give it one. The 40-year and 20-year lags come from a secondary compilation by a guest author; the usual scholarly source for electrification (Paul David, 1990) is named in the Narayanan and Kapoor essay but has no entry in the bibliography.

7. Confidence and theses. High on the Census series and the McKinsey flat line; medium on the historical lags (secondary). Supports T15 (shocks before stabilisation, open question on numbers) and frames T1: the revolution is real at the desk and slow in the accounts.

8. Question for the audience. Electric motors took a generation to change factories because the factories had to be rebuilt around them. What in your organisation has to be rebuilt before agents show up in the results?

9. Personal angle. The brief says the speaker's use is daily and that there is no way back (T17). One plain sentence: "I changed how I work in a year; the institutions I work in have not changed yet." Speaker to supply: one process in his own institution that still runs exactly as it did before these tools.

## I1.6 The curve bends when cost and reliability stop following capability, and those are the two things to watch

1. Title as claim. A flattening will not show first in a benchmark headline. It will show in the price of an hour of agent work and in the gap between coin-flip success and dependable success.

2. Number or data series. Indicators the notes support, with the current reading:
   - Cost per hour of agent work. From METR's charts as read by Toby Ord: a human engineer about $120 an hour; GPT-5 about $13 an hour on 45-minute tasks and about $120 an hour on 2-hour tasks; o3 about $350 an hour at its full horizon [@ord2025costs] (primary; he describes the evidence as moderate). Follow-up on UK AISI data: ten times the tokens buys less than ten times the horizon [@ord2026ukaisi] (primary).
   - Price of a fixed capability: still falling about 13 times a year on average, 75 times a year when a level is first reached and 4.7 times a year two years later [@epochai2026plunging] (primary).
   - Reliability gap: the 80% horizon against the 50% horizon (I1.2). Bending would show as the ratio widening.
   - Reset benchmarks: top score on the old and the new version. OSWorld-Verified 86.0% against OSWorld 2.0 44.3% [@xlanglabosworld] [@xlanglabosworldbenchmark]; Terminal-Bench 2.0 84.7% against the newer default board 65.8% [@terminalbenchleaderboard] [@terminalbenchdefault] (all primary). Bending would show as the new versions not being climbed.
   - Real paid work: the Remote Labor Index (I1.3) and whether "×2 every ~3.3 months" on the project site [@caisremote] (primary) continues.
   - Expectations side: where Gartner puts AI agents on the 2027 cycle; whether its 40% cancellation forecast is scored; whether McKinsey's 37% EBIT share moves; the Census series.
   - Token bills in use: about 20% of McKinsey respondents say operating costs including tokens constrain their AI use, and high performers are constrained on coding agents about three times as often as others [@mckinsey2026stateofai] (primary).
   - Slide: a short list of three or four of these as "what I will watch", without numbers.

3. Quotes.
   - "I believe that many people to some extent both overstate the precision of our time horizon measurements and draw conclusions I don't think the evidence fully supports." [@metr2026limitations]. Speaker: one of the main authors of the METR time horizon paper, in a METR research note of 2026-01-22 (the name is not recorded in the notes or in the local copy). Role and interest: staff of a non-profit evaluator that works with the labs. Local file: `converted/web/f_metr_limits.md`. Result: EXACT.
   - No second quote. The cost figures are Ord's readings of charts and are better paraphrased.

4. Example or case. METR's note of March 2026: as the task suite saturates, results become more sensitive to analysis choices, and excluding public tasks cuts one model's horizon by 40% [@metr2026timehorizontask] (primary). The first sign of the top of a curve is that the people measuring it start to disagree with their own earlier numbers.

5. Counter-evidence, in proportion. Each indicator currently has a reading on the "not bending" side as well: the price of a fixed capability keeps falling fast, the reset benchmarks are being climbed within months (the old Terminal-Bench went from 20% to 77.3% in a year), and the one independent look inside a lab found acceleration. The physical inputs (energy, memory, capital) are a separate set of limits treated in theme I5; they are reasons the curve could bend, not evidence that it has.

6. Speaker-note material. This insight is a reading aid, not a finding: the list is assembled from the measurers' own caveats in the notes, and no source in the notes proposes it as a set. Ord's cost figures are his reading of METR charts from late 2025 and are not updated for 2026 models. The McKinsey cost constraint is self-reported by managers. Do not present any of these as a forecast.

7. Confidence and theses. Medium: the indicators are well sourced one by one, the selection is ours. Supports T8 and T14 (cost and physical limits as bottlenecks) and the brief's closing section on what to watch.

8. Question for the audience. Which would change your plans more: a model that does twice as much, or one that does the same and is right nine times in ten instead of five?

9. Personal angle. The brief's intent is to end with indicators. One plain sentence: "I do not watch the leaderboards any more; I watch what an hour of the agent costs me and how often I have to redo its work." Speaker to supply: whether he tracks his own spending or redo rate in any form, even roughly.

## How to draw the two curves on one slide

This is a sketch, and the slide should say so. The two curves have different vertical axes (what the technology can do, and what people expect of it), so they share only the time axis.

Draw the horizontal axis as time, without year ticks except three anchors: 2022 (chat assistants reach the public), 2024 (reasoning models, the break Epoch finds), and "now". Draw the capability curve as the lower part of an S: slow at the left, steep through 2024 to 2026. Stop the solid line at spring 2026 and continue it as a dashed fan that opens upward and flattens, with a small label "not measured since April 2026". The fan is the honest part: the same data are compatible with continued doubling and with the start of a bend.

Draw the expectations curve in a second colour over the same time axis: a fast rise, a peak, the beginning of a descent. Do not draw the trough and the later plateau as if they were known; fade the line out after the peak.

Put the "we are here" marker as a vertical band, not a dot. On the expectations curve the band covers the top and the first part of the way down ("at or just past the peak", Gartner's own two placements in 2026). On the capability curve the same band sits on the steep section, at the point where the solid line turns into the dashed fan. The vertical distance between the two curves inside the band is the talking point: expectations at their highest while the measured line is still rising and its top is unread.

Optionally add a third, thin line near the bottom for what firms have put into use and booked: about one US firm in four using AI at all, about one organisation in six with agents deployed, profit attribution unchanged for a year. If it is drawn, it should be visibly lower and flatter than the other two, with no numbers on the slide.

What to say about uncertainty, in one breath: nobody can locate the inflection of an S-curve while standing on it; the hype curve is an analyst's drawing, not a measurement; and the instrument that drew the capability line ran out in the spring. The slide shows where the evidence ends, and the band shows how wide "here" is.

## Quote verification record

All quotes were checked on 2026-11-17 with `python3 /Users/andy/_code/_EDU/msd_review/scripts/verify_quotes.py <file> -`. "EXACT" means a contiguous match after the script's normalisation (the script prints this case as VERIFIED without the "interleaved" remark). All haystacks are scraper output without a `converted-by` stamp, so the script reports the converter as unknown.

| Quote (first words) | Key | Local file | Result |
|---|---|---|---|
| "Measurements above 16 hrs are unreliable..." | metr2026taskcompletion | converted/web/metr_th.md | EXACT |
| "Clarified that this page is no longer actively updated." | metr2026taskcompletion | converted/web/metr_th.md | EXACT |
| "An 8-hour time horizon does not mean..." | metr2026taskcompletion | converted/web/metr_th.md | EXACT |
| "nearly two years of rapid capability progress..." | kapoor2026paper | converted/web/f_nt_reliab.md | EXACT |
| "Anthropic redacted a majority of the evidence..." | metr2026independent | converted/web/i_metr_anthropic_assessment.md | EXACT |
| "we would not be surprised if the true acceleration..." | metr2026independent | converted/web/i_metr_anthropic_assessment.md | EXACT (reserve) |
| "Babies don't keep doubling forever..." | marcus2026misplaced | converted/web/f_marcus_misplaced.md | EXACT |
| "Agentic AI sits at the Peak of Inflated Expectations..." | gartner2026hypecycleagentic | converted/web/gartner_agentic_hc.md | EXACT |
| "most deployments remain narrowly scoped..." | gartner2026hypecycleagentic | converted/web/gartner_agentic_hc.md | EXACT (reserve) |
| "Concerns about GenAI have shifted..." | gartner2026latest | converted/web/gartner_ai_hc.md | EXACT |
| "the speed of diffusion is inherently limited..." | narayanan2025ainormal | converted/web/f_normaltech_essay.md | EXACT |
| "valuations are not stretched. P/E ratios actually have fallen..." | no key yet | converted/web/c_imf_brief.md | EXACT |
| "I believe that many people to some extent both overstate the precision..." | metr2026limitations | converted/web/f_metr_limits.md | EXACT |

Short phrases inside the running text were checked the same way and are EXACT: "would require many more tasks" and "a regularization mistake" (`converted/web/metr_th.md`); "deeply uncertain" (`converted/web/f_ord_writing.md`); "agent washing" and the sentence on about 130 real vendors (`converted/web/e_g1a.md`); "towards levels not seen since the dot-com bubble" (`converted/web/c_boe_fsr_jul26.md`); "×2 every ~3.3 months" (`converted/web/D_rli_remotelabor.md`); "complete nonsense" (`converted/web/f_lecun_wired.md`, a secondary report of LeCun's words); "producing goods or services" and "any of its business functions" (`converted/web/e_btos_about.md`); "the key difference" (`converted/web/c_imf_brief.md`); "harvest phase" (`converted/web/i_fortune_jcurve.md`); "under 20% and perhaps under 10%" (`converted/web/f_marcus_misplaced.md`).

Unverified, keep off slides: the AI Futures sentence "the speed of adoption will be determined by the most aggressive" [@aifutures2025aiprofoundly] (in the notes as a primary quote; no local copy was found, so it is paraphrased in I1.5); METR's phrases on GPT-5.6 Sol ("beyond 270hrs") and on discoveries ("has accelerated sharply") [@metr2026evaluation] [@metr2026seenacceleration] (in the notes as primary quotes; no local copy was found, so they are paraphrased in I1.1 and I1.3).

## Bibliography additions needed

- IMF, press briefing for the Global Financial Stability Report, October 2026 (transcript). Speakers quoted in the notes: Jason Wu (Assistant Director) and Athanasios Vamvakidis (Deputy Director). Proposed key: `imf2026gfsrbriefing`. Strand `4.economics` (also `1.analysts`). Verification: primary, transcript read; the local copy `converted/web/c_imf_brief.md` was reached through a Google News redirect, so the canonical imf.org URL still has to be recorded. Interest: intergovernmental lender, surveillance mandate. The existing key `imf2026global` is the report, not the briefing.
- Paul A. David, "The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox", American Economic Review 80(2), 1990, pp. 355 to 361. Proposed key: `david1990dynamo`. Metadata from general knowledge, not from a page read in this project; the essay [@narayanan2025ainormal] cites David's analysis of electrification. Needed only if the 40-year lag is to rest on a scholarly source instead of the secondary compilation [@shenk2026productivity].
- `file` fields that can now be filled: `metr2026independent` has a local copy at `converted/web/i_metr_anthropic_assessment.md` (scraped 2026-11-17).
- Title corrections: none. The scraped copies of the bracketed entries cited here (`metr2026taskcompletion`, `metr2026limitations`, `metr2026timehorizon`, `metr2026evaluation`, `gartner2026hypecycleartificial`, `census2026btosdownloads`) do not carry the page title, so no exact title was learned.

## Open points

- The METR series has no point after April 2026 and no successor instrument is in the notes. Whether the 2026 models keep to the doubling of about four months is not established beyond one lower bound and one partly redacted assessment of a single lab.
- The author of the METR limitations note of 2026-01-22 is not named in the notes or the local copy. Name him or her before the quote is attributed aloud.
- Generative AI's own position on the 2026 Hype Cycle is not established; the 2025 Trough placement rests on trade press.
- The 2026 Gartner graphic was read as an image; positions other than those named in the article text are a visual reading.
- The Remote Labor Index rows carry no dates and no confidence intervals; the middle points of the series are ordered by model release, not dated.
- The historical lags (40 and 20 years) are from a secondary compilation. The dot-com comparison rests on two official statements about valuations, not on an analysis of the technology.
- Whether Ord's cost-per-hour reading holds for the models of late 2026 is unknown.
- Contested, and likely to stay so: whether progress on checkable tasks carries over to work that needs judgment. Both camps in the notes agree on the facts and differ on this step.

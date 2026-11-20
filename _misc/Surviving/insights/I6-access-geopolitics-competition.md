# I6. Access, geopolitics and competition

Theme file for the talk "Agentic AI impact on the IT industry". Synthesis of the research notes as of 2026-11-17, not new research. Backstage material: items 2, 3, 5 and 6 of each insight are for speaker notes, backup slides and questions. Item 9 is what may reach a slide.

## Summary in five lines

1. The one thing to remember: the frontier is sold by very few companies from one country and they can switch a customer off, yet the same capability appears as downloadable weights about four months later, so access is a supplier risk to manage and not a fate.
2. The best story: in June 2025 Anthropic cut a paying customer, Windsurf, off its best coding models at short notice because a rival was about to buy it, and its co-founder explained on stage that it would be odd to sell Claude to OpenAI.
3. The best picture: one market drawn twice, by enterprise dollars (two American labs take 86%) and by requests on an open router (a Chinese lab leads with about a third).
4. The best question for discussion: which is the better position for a team in Russia, four months behind on a model nobody can take away, or at the frontier on a model that can disappear tomorrow?
5. What the speaker should not claim: that foreign models are banned in Russia, that Russian models are measurably competitive or uncompetitive (the evidence is thin), that Chinese providers will serve Russian customers (no source), or any figure for Russian developers from the JetBrains data (58 respondents). Nothing here is advice on getting around a provider's or a state's restrictions.

How to read the verification levels: "primary", "secondary", "search-result only", "not opened" and "not stated" are the levels recorded in `references_keymap.tsv`. Quote results are explained in the quote log at the end. Items from the Telegram chat are leads only and are marked as such.

## I6.1 Two American labs take most of the enterprise money, and one country holds most of the measured compute

1. Title as a claim. Two American labs take most of the enterprise money, and one country holds most of the measured compute.

2. Number or data series.
   - Enterprise LLM API spend share, Menlo Ventures, survey of nearly 400 US enterprise buyers fielded 2026-09-08 to 09-26 (primary; Menlo is an Anthropic investor): Anthropic 40% (2025) to 55% (2026); OpenAI 27% to 31%; Google 21% to 9%; all others 12% to 5%. Anthropic and OpenAI together 67% to 86% [@menlo2026stateenterpriseai]. An earlier point, Anthropic 24% in 2024, is search-result only [@dataconomy2025anthropic].
   - The same market by requests, OpenRouter, week beginning 2026-11-09 (primary; a routing marketplace used mostly by individual developers and start-ups, and a Menlo portfolio company): DeepSeek 31.8%; OpenAI 19.0%; Google 15.1%; Z.ai 7.0%; Anthropic 6.3%; Qwen 6.2%; Mistral 2.6%; Tencent 2.3%; Nvidia 1.6%; others 8.2% [@openrouter2026aimodel].
   - Compute by country, Epoch AI, data to March 2025 (primary): United States about 75% of AI supercomputer performance in the dataset, China about 15%, the rest about 10%; industry owned about 80% in 2025 against about 40% in 2019. Epoch states that the dataset covers an estimated 10 to 20% of global capacity [@epochai2025trends].
   - Count of public or public-private AI supercomputers by region in 2025, Stanford AI Index 2026 (primary): China 85; Europe and Central Asia 44; North America 41; East Asia and Pacific 27. The United States hosts 5,427 data centres. Private AI investment in 2025: United States 285.9 billion dollars, Europe 20.9 billion, China 12.4 billion [@stanfordhai2026aicumulative].
   - Slide number, if any: 86%. The paired bars (Menlo dollars beside OpenRouter requests) are the picture.

3. Quotes.
   - "Anthropic and OpenAI now account for 86% of enterprise LLM API spend, up from 67% last year." [@menlo2026stateenterpriseai]. Speaker: Menlo Ventures report text. Role and interest: venture investor and Anthropic shareholder; it marks Anthropic and OpenRouter as portfolio companies. Result: EXACT (Q1).
   - "The United States dominates AI supercomputers globally, owning about 75% of total computing power in our dataset. China is in second place at 15%." [@epochai2025trends]. Speaker: Epoch AI. Role and interest: non-profit research institute, no product to sell. Result: EXACT (Q2).

4. Example or case. The same week can be told two ways. By the dollars of large American companies, the market is a two-horse race. By the requests of price-sensitive developers on a router, the leader is DeepSeek and the lab with 55% of enterprise dollars has 6.3%. Menlo's own report holds the same contrast in one sentence: "Open-source remains 4% of spend despite 19% of usage." (EXACT, Q3).

5. Counter-evidence, in proportion. The Menlo sample is American, small and run by an interested party, and its market sizes are its own estimates. Epoch's country split is from March 2025 and covers a minority of capacity. Stanford's count puts China first by number of state systems, the opposite ranking to Epoch's capacity share. Sovereign programmes exist but are small in delivered capacity so far: the EU's committed public money is up to 10 billion euros for up to seven sites with construction from 2027 [@europeancommission2026launching], and Stargate UAE planned 200 MW of 1 GW for 2026 [@openai2025stargate].

6. Speaker-note material. Corrections from later notes: the 55, 31 and 9% shares were search-result only in the earlier file and are now read in the Menlo PDF. The earlier file had no compute-by-country figure; the later one supplies Epoch's 75 and 15%. "Share" depends on the denominator (dollars, tokens, requests, count of machines, capacity), and showing two denominators side by side is itself the lesson. Menlo also estimates that Anthropic and OpenAI account for more than 25% of the revenue of the three large clouds, which shows the dependence running both ways. Always label Menlo's interest when the numbers are shown.

7. Confidence and thesis. Medium for the enterprise shares (primary document, interested publisher, US only). Medium for compute (primary, dated, partial coverage). High that the picture changes with the denominator. Supports T6 for money, chips and the top tier. Does not support it for volume of use.

8. Question for the audience. When someone says a company "leads the market", which market do they mean: who pays, who uses, or who owns the machines?

9. Personal angle. The brief gives the speaker's daily use (T17) without naming tools. Plain sentence without a number: "Almost everything I do with these tools in a day passes through two or three companies, and none of them is in my country." Speaker to supply: which tools he actually relies on, if he is willing to name them.

## I6.2 A provider can switch you off for where you are, who owns you, or whom you compete with

1. Title as a claim. A provider can switch you off for where you are, who owns you, or whom you compete with.

2. Number or data series.
   - Supported-country lists, vendors' own pages (primary). Anthropic: 185 countries and regions listed on the page fetched for this file. OpenAI: 208 countries and territories. Google Gemini API and AI Studio: about 230. Russia, Belarus, mainland China, Hong Kong and Iran appear on none of the three API lists; Kazakhstan and Uzbekistan appear on all three [@anthropicsupported; @openai2026apisupported; @openai2026helpcenter; @google2026available]. Google's web app list includes Hong Kong, Macau and mainland China for Workspace only, and omits Russia, Belarus and Iran [@google2026where].
   - Ownership rule (primary): since 2025-09-04 Anthropic's terms bar entities more than 50% owned, directly or indirectly, by companies headquartered in unsupported regions, wherever they operate [@anthropic2025extending]. The current country page extends the wording to entities "majority-owned or controlled" by persons or entities in unsupported regions.
   - Commercial rivalry, a short timeline: June 2025, Windsurf loses direct access to Claude 3.5 and 3.7 Sonnet (secondary, page read for this file) [@techcrunch2025anthropic]; August 2025, Anthropic revokes OpenAI's API access; January 2026, xAI staff blocked from Claude through Cursor (both search-result only) [@storyboard18anthropic]. A report that OpenAI planned to cut Cursor's access rests on one outlet (search-result only) and stays off slides [@newstack2026anthropic].
   - Retirement as a quieter form of withdrawal (primary): Anthropic's price list marks Opus 4, Opus 4.1 and Sonnet 4 as retired within about 18 months of release [@anthropic2026apipricing].
   - Slide number, if any: none. The story carries it.

3. Quotes.
   - "I think it would be odd for us to be selling Claude to OpenAI" [@techcrunch2025anthropic]. Speaker: Jared Kaplan, co-founder and Chief Science Officer of Anthropic, on stage at a TechCrunch event, June 2025. Role and interest: the vendor explaining why it cut a customer off. Result: EXACT (Q4).
   - "Any country or region not listed is unsupported." [@anthropicsupported]. Speaker: Anthropic's supported-countries page. Role and interest: the vendor's own policy. Result: EXACT (Q5).
   - "Accessing or offering access to our services outside of the countries and territories listed below may result in your account being blocked or suspended." [@openai2026apisupported]. Speaker: OpenAI's supported-countries page. Role and interest: the vendor's own policy. Result: EXACT (Q6).

4. Example or case. Windsurf. A coding-tool company built on Claude was reported to be in acquisition talks with OpenAI. According to TechCrunch, Anthropic cut its direct access to two of the most popular coding models, "forcing the startup to find third-party computing providers on relatively short notice" (EXACT, Q7). Kaplan also gave a second reason, that Anthropic was short of computing capacity and wanted to keep it for lasting partnerships. The customer had broken no rule. It had become, or was about to become, part of a competitor.

5. Counter-evidence, in proportion. For most of the world the door is open: 185 to about 230 countries are served. The United States withdrew its own plan for country tiers in AI exports before it took effect (the AI Diffusion Rule, rescinded 2025-05-13) [@usbureauindustry2025biscommerce]. The vendors give reasons that are not commercial: Anthropic names compelled data sharing, use by adversarial military and intelligence services, and distillation. The rivalry cases involve direct competitors of the labs, which an ordinary customer is not.

6. Speaker-note material. Corrections from later notes: the earlier file stated Russia's absence from the OpenAI and Google lists only through secondary sources; the later file read both lists. The Anthropic list and the ownership announcement were held only as notes, with no local copy; both pages were fetched for this file and the quotes checked. The filing shows that enforcement is a routine risk on the vendor's side too: "When we identify such usage, we seek to restrict or terminate the customer’s access" (EXACT, Q8) [@anthropic2026pbcform]. The statement that the ownership rule cost revenue in the low hundreds of millions of dollars (wording not checked) comes through the South China Morning Post citing the Financial Times and has no recorded verification level [@southchinamorningscmpstart]; keep it backstage. Interest: all three lists are the vendors' own legal pages, facts as of the read date.

7. Confidence and thesis. High for the lists and the ownership rule (primary). Medium for Windsurf (secondary, one outlet, direct quotation of a named executive). Low for the other rivalry items. Supports T14 (denial of access as a business bottleneck) and adds two forms the thesis did not name: ownership and rivalry.

8. Question for the audience. If your main model disappeared on Monday morning, what would still work on Tuesday?

9. Personal angle. T17 says there is "no way back" from daily use. Plain sentence without a number: "I have built my working day on a tool that somebody else can turn off, and I did not sign anything that says they will not." Speaker to supply: a moment when a tool or account he depended on stopped working, was blocked, or changed its terms, and what he lost or had to rebuild.

## I6.3 In Russia there are two barriers, and a grey market has grown between them

1. Title as a claim. In Russia there are two barriers, the provider's and the domestic one, and a grey market has grown between them.

2. Number or data series.
   - Grey market, Vedomosti, 2026-11-05 (primary for the public lead paragraphs; the single source of the estimate is the legal aggregator GPTunneL, a competitor of the grey sellers): sole traders reselling foreign model access through Chinese proxies went from practically none at the end of 2025 to about 50 by August 2026; grey turnover 100 to 150 million roubles a month; legal aggregators about 700 million roubles a month in August and 5 to 6 billion roubles for January to August, four times the year before, excluding big tech [@vedomosti2026greymarket].
   - What Federal Law 243-FZ does (legal summaries, secondary; full text not read): signed 2026-07-26, in force from 2026-09-01 with later dates for some provisions; defines sovereign and national large foundation models, both developed only by Russian legal entities; data stored in Russia; the state may require Russian models in certain state information systems and other sensitive areas; a national model may use foreign components distributed under an open licence; text and data mining of lawfully accessed works is not an infringement [@garant2026legal; @habr2026aisupport; @russianfederation2026federal].
   - What it does not do, according to the same summaries and press coverage: it sets no general ban on foreign models [@tzh2026journal; @comnews2026government].
   - The domestic barrier (primary documents, but advocacy and vendor material): an industry association's letter of 2026-04-21 says VPN use was restricted from 2026-04-01 and lists outages on 13 dates in April [@association2026letter]; in a Yandex and ITMO survey of more than 600 respondents (2025), 32% name unavailability without a VPN as a barrier to AI coding assistants [@yandexitmo2025respondents]; Sber's 2026 methodology document describes access to Copilot, Cursor and Claude Code as partly closed or requiring a VPN [@sber2026aidisrupt].
   - Slide number, if any: 50 (resellers, from almost none, in about eight months), with the source named aloud as an estimate by one market participant.

3. Quotes.
   - «К августу 2026 г. число продавцов выросло до 50, а оборот таких услуг достиг 100–150 млн руб. в месяц.» [@vedomosti2026greymarket]. Gloss: "By August 2026 the number of sellers had grown to 50, and the turnover of such services had reached 100 to 150 million roubles a month." Speaker: Vedomosti, reporting an estimate by a representative of GPTunneL. Role and interest: business daily; the estimate comes from a legal aggregator that competes with the grey sellers. Result: EXACT by Unicode-aware check (Q9).
   - «позволяет государству требовать использования только российских ИИ‑моделей в отдельных государственных информационных системах и других чувствительных сферах» [@habr2026aisupport]. Gloss: "[the law] allows the state to require the use of only Russian AI models in certain state information systems and other sensitive areas." Speaker: Habr news item summarising the law. Role and interest: Russian technology news site, secondary. Result: EXACT by Unicode-aware check (Q10).
   - Backup: «попытки блокировок VPN вызывают серьёзные проблемы в работе у российских разработчиков» [@association2026letter]. Gloss: "attempts to block VPNs cause serious problems in the work of Russian developers." Speaker: the association "Отечественный софт" in a letter to the prime minister. Role and interest: industry lobby; the letter does not mention AI tools. Result: EXACT by Unicode-aware check (Q11).

4. Example or case. The reseller chain as Vedomosti's reporting, relayed by The Moscow Times, describes it (secondary): access sold at up to 70% below official prices, traffic passing through three or four intermediaries, and two risks named by Russian experts, that conversations are stored and resold, and that a cheaper model is silently substituted for the one paid for [@moscowtimes2026russian]. The buyer cannot easily tell which model answered. The same relay says the provider began blocking Russian accounts more often in autumn 2026 and names public tenders by large Russian companies for foreign AI subscriptions; those names should stay off slides unless checked against the tender records.

5. Counter-evidence, in proportion. The legal aggregator market is about five times the grey one on the same estimate, so the grey market is the smaller part. The law, as summarised, supports domestic models and does not ban foreign ones; a deputy prime minister is reported as saying foreign services will not be banned while the public sector must use Russian solutions (search-result only) [@bfmdeputy]. The 32% VPN barrier is from a 2025 vendor and university survey with no segment sizes. The association's letter is advocacy with no measured losses. The contraction of the Russian IT job market in 2025 and 2026 (vacancies minus 36% and résumés plus 30% on hh.ru, February 2026 against February 2025) is attributed in Russian coverage to the economy and taxes ahead of AI, and nothing in the notes links it to access; it does not belong in this theme [@datalab2026hhruvacancies].

6. Speaker-note material. Corrections from later notes: the earlier file knew the grey-market story only through The Moscow Times; the later file read Vedomosti's own page and confirmed the figures in its public paragraphs, so cite Vedomosti. The Moscow Times is an exile outlet designated "undesirable" in Russia; its page was not fetched for this file and no quotation is taken from it. Still unconfirmed against the law's text: the bill number 1271570-8, the transition date 2032-09-01 for systems built on foreign models, and the 2027-03-01 dates. Telegram chat leads, not evidence: mass bans of Russian Claude accounts in May 2026, a block of the DeepSeek web site by the regulator as a side effect, a coding tool freezing Russian balances, and the claim that large Russian enterprises already run on Chinese models [@kodrudeepseek; @cnews2026vpnblocking]. On domestic models the only comparison found is one Habr review of a benchmark run by a Sber-affiliated alliance (search-result only) against Sber's own announcement [@habrreview; @sbergigachat]; that is too thin for any claim in either direction.

7. Confidence and thesis. Medium for the grey-market figures (one interested source, reported by a business daily). Medium for what the law does (two secondary summaries agree, text not read). Low for everything from the chat. Supports T14 for Russia and adds a second, domestic barrier that the thesis did not name.

8. Question for the audience. When you buy access through an intermediary, how would you know which model actually answered you?

9. Personal angle. The speaker works in Russia and uses these tools daily (T17). The brief says nothing on how he gets access, and that must not be guessed. Plain sentence without a number: "Between the provider who does not serve us and the network that does not let us out, a market has appeared, and it sells something nobody can inspect." Speaker to supply: only what he is comfortable saying in public about access from Russia; if nothing, keep the sentence impersonal.

## I6.4 The frontier has competitors a few months behind, and most of them are Chinese

1. Title as a claim. The frontier has competitors a few months behind, and most of them are Chinese.

2. Number or data series.
   - Open against closed, Epoch AI, 2026-05-29 (primary, page fetched for this file): since January 2026 the best open-weight models lag the closed frontier by an average of four months, or 8 points on the Epoch Capabilities Index; the same measure gave three months for January 2023 to October 2025. Scores recorded in the notes (the page shows them only in a chart): GPT-5.5 Pro 159.4; Kimi K2.6 151.6; Kimi K2.5 148.2; MiniMax-M2.5 147.4; GLM-5 146.6 [@epochai2026insight].
   - United States against China, Stanford AI Index 2026 (primary): top US model 1,503 against top Chinese model 1,464 on Arena in March 2026, a lead of 2.7% [@stanfordhai2026aicumulative].
   - What price-sensitive developers route to, OpenRouter, seven days to 2026-11-16, tokens in trillions (primary): DeepSeek V4.1 Flash 1017 61.2; Tencent Hy4 16.0; DeepSeek V4.1 Flash 15.5; GLM 5.3 Flash 11.8; GPT-6 Luna 8.08; Claude Opus 5.5 7.37; StepFun Step 5 Preview 6.36; Xiaomi MiMo-V2.6-Flash 4.16; GLM 5.3 3.74; GPT-6.1 Sol 3.71. Seven of the ten are Chinese and hold about 86% of top-ten tokens (derived) [@openrouter2026aimodel].
   - Price distance (primary): DeepSeek V4 Pro 3.96 dollars per 1M output tokens at peak against 40 to 50 for the US flagships [@deepseek2026models; @openai2026apipricing; @anthropic2026apipricing].
   - Enterprise uptake, Menlo 2026 (primary, interested publisher): open-source models 19% of tokens (11% a year earlier) and 4% of spend (6% a year earlier) [@menlo2026stateenterpriseai].
   - Slide number, if any: "four months".

3. Quotes.
   - "Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months" [@epochai2026insight]. Speaker: Epoch AI. Role and interest: non-profit research institute, no product to sell. Result: EXACT (Q12).
   - "as of March 2026 Anthropic’s top model leads by just 2.7%" [@stanfordhai2026aicumulative]. Speaker: Stanford HAI, AI Index 2026 summary. Role and interest: academic institute with industry sponsors. Result: EXACT (Q13).

4. Example or case. Epoch's own comparison makes the distance concrete: the gap is about the size of one version step at a leading lab, "similar to the gap between GPT-5 and GPT-5.5" in the page's words. The leading open-weight models on that index are Kimi (Moonshot), MiniMax and GLM (Z.ai), all Chinese. On the router, the single most used model of the week is a DeepSeek model.

5. Counter-evidence, in proportion. Epoch says the gap has widened (three months before, four now) and adds in the chart note: "This gap may be understated: open-weight models tend to perform worse on private benchmarks compared to closed models" (EXACT, Q14). On a cyber-capability index the lag is reported as six to seven months (search-result only) [@epochaitopic]. On the Artificial Analysis index the distance looks larger: the best open-weight model scores 46 against 65 for the top closed model [@artificialanalysis2026comparison]. American enterprises spend only 4% of their model budget on open models. Self-hosting needs GPUs that are themselves export-controlled, and the licence terms of the Chinese open-weight models were not checked.

6. Speaker-note material. Corrections from later notes: the earlier file, from Menlo's 2025 report, said open-source models had fallen to 11% of enterprise use from 19%; the 2026 report gives the opposite direction for tokens (11% to 19%) while spend share fell (6% to 4%), and the later one wins. The earlier file's history of Chinese share on OpenRouter (61% of top-ten tokens in February 2026, a weekly peak of 46% of all tokens in July) is search-result only and partly from Chinese state-affiliated media. The Epoch page was fetched for this file; its text confirms the four months, the 8 points and the earlier three months, while the individual scores sit inside a chart and were not re-read. Interests: OpenRouter's users skew to individuals and start-ups; the Arena scores behind Stanford's 2.7% are preference votes, not task success.

7. Confidence and thesis. High that capable open-weight and Chinese models exist close behind the frontier on general indices (two independent primary sources). Medium on the size of the gap for hard agentic work. Supports the last sentence of T14, "competition still exists", and qualifies T6.

8. Question for the audience. Four months behind the frontier: for your work, is that a handicap or a rounding error?

9. Personal angle. Nothing in the brief says which models the speaker uses. Plain sentence without a number: "The model I could not get last spring is, more or less, a file anyone can download this autumn." Speaker to supply: whether he has tried an open-weight or Chinese model for real work, and what the difference felt like.

## I6.5 Developers in China and in Europe use the same tools with opposite levels of trust

1. Title as a claim. Developers in China and in Europe use the same tools with opposite levels of trust.

2. Number or data series. JetBrains Developer Ecosystem Survey 2026, public raw data, weighted shares with unweighted n for Europe and China (primary, analysed locally; self-selected audience of a tool vendor) [@jetbrains2026rawdata]. Order of values: Europe, North America, China, India, Japan, all.
   - Uses a coding agent every day: 58%, 54%, 81%, 67%, 69%, all 64% (Europe n = 8,207; China n = 1,015).
   - At least 61% of own code fully written by agents: 34%, 34%, 57%, 42%, 52%, all 43%.
   - Trusts agent output, mostly or fully: 34%, 38%, 60%, 43%, 42%, all 45% (Europe n = 1,793; China n = 227).
   - Distrusts agent output: 37%, 31%, 11%, 18%, 12%, all 23%.
   - Always reviews agent code: 52%, 50%, 28%, 48%, 25%, all 43% (Europe n = 6,716; China n = 799).
   - Finds agent solutions better than own code: 37%, 43%, 66%, 64%, 67%, all 54%.
   - Would delegate application logic: 32%, 36%, 66%, 33%, 59%, all 44% (Europe n = 2,158; China n = 248).
   - Weighting: respondents in China are 4.7% of rows and about 20% of the weight; Europe is 37% of rows and 19% of the weight.
   - Slide number, if any: none alone. The pair "trust 34% in Europe, 60% in China" is the picture, as two bars.

3. Quotes. None could be verified for the regional figures, because the source is a data file and not a text. The one checked sentence is the producers' own caveat: "JetBrains users may be more willing to respond" [@makeeva2026archiving]. Speaker: Aleksandra Makeeva and Anastasia Molotova, JetBrains survey team, conference poster. Role and interest: the dataset's producers, employees of a tool vendor. Result: EXACT (Q15).

4. Example or case. Two developers answer the same questionnaire. The one in Europe uses an agent daily in a little over half of cases, trusts its output in one case in three and always reviews it in half. The one in China uses an agent daily in four cases out of five, trusts it in three out of five and always reviews it in a little over a quarter. The published "global" figure is an average of the two, moved towards China by the weights.

5. Counter-evidence, in proportion. This is a non-probability sample recruited largely through a vendor's own channels. The Chinese subsamples are a few hundred to a thousand people, each counted about nine times as heavily as a European respondent. All answers are self-reports. Differences in survey culture and in who answers a 30-minute questionnaire could produce part of the gap. The data say nothing on which attitude gives better software. On worries the regions are close: anxiety about replacement "often or always" is 28% in Europe and 31% in China.

6. Speaker-note material. This comes from the later user-supplied file, which corrects the earlier notes on the same survey: the vendor's blog said about 90% weekly and 68% daily use; the raw file gives 88% and 64% among employed respondents who answered the AI block. For an audience in Europe or Russia the European column is the relevant benchmark, not the global average. Russia has 58 respondents in the file, 23 to 36 on routed questions, so there is no Russian estimate; the indicative direction (less agent use, more scepticism) cannot carry a slide. Whether the divide has anything to do with access is not shown by the data; do not suggest that it does. Interest: JetBrains sells IDEs and its own AI products, which appear among the answer options.

7. Confidence and thesis. Medium that a large regional difference in self-reported use and trust exists in this sample. Low on its cause. It bears on T14 only indirectly: the market for these tools is not one culture, and a second large ecosystem with its own habits is forming. It also touches T4 (trust in plausible output).

8. Question for the audience. Trust less and review everything, or trust more and move faster: which side will have the better software in three years, and which will have the better engineers?

9. Personal angle. T17 and the Voice section give a practitioner who uses the tools daily and worries about validation and load. Plain sentence without a number: "I read every line the agent writes, and I am no longer sure whether that makes me careful or slow." Speaker to supply: whether that sentence is true of him; if he reviews selectively, he should say how he decides.

## I6.6 Access risk is a supplier risk: there are several options, and each has a price

1. Title as a claim. Access risk is a supplier risk: there are several options, and each has a price.

2. Number or data series. This insight is a set of options with trade-offs for a company or a student in Russia. It is a synthesis and partly inference; it is not advice to get around any restriction.
   - Domestic models. Gain: legal certainty, and they are what the state may require in designated state systems and sensitive areas under 243-FZ [@habr2026aisupport]. Price: the capability evidence is thin and comes from the vendors or from a benchmark run by a vendor-affiliated alliance (search-result only) [@habrreview; @sbergigachat].
   - Self-hosted open-weight models. Gain: nobody can withdraw them, data stays inside, and the law's "national model" category allows foreign components under an open licence. Price: about four months behind on Epoch's general index and further behind on other indices [@epochai2026insight; @artificialanalysis2026comparison]; hardware that is export-controlled; operating skill; licence terms that vary and were not checked.
   - Chinese providers' hosted services. Gain: prices 3 to 25 times below US flagships on list [@deepseek2026models; @moonshotai2026model], and at least one provider documents an international endpoint [@alibabacloud2026model]. Price: no source was found on their terms for Russian customers; data leaves the country; reachability from Russia is itself uncertain (chat lead only).
   - Access to US frontier models through legal aggregators. Gain: the frontier, with a contract in Russia; the legal segment is the larger one on Vedomosti's figures [@vedomosti2026greymarket]. Price: continuity depends on the provider tolerating the aggregator, and at least one provider states that offering access outside its list may lead to suspension [@openai2026apisupported]; the provider's indemnities and support do not reach the end customer.
   - Grey resellers. The sources describe this as a risk, not an option: no recourse, possible retention and resale of conversations, possible silent substitution of the model (secondary) [@moscowtimes2026russian].
   - What companies already do about cost and dependence, JetBrains 2026 (primary, global, self-selected): tiered model use 20%; budgets per developer or team 21%; local or self-hosted models 16%; no controls 34% (n = 1,915) [@jetbrains2026rawdata].
   - Slide number, if any: none. A two-column table of "what you gain, what you pay" is the picture.

3. Quotes.
   - «может использовать зарубежные компоненты, распространяемые на условиях открытой лицензии» [@habr2026aisupport]. Gloss: "[a national model] may use foreign components distributed under an open licence." Speaker: Habr news item summarising 243-FZ. Role and interest: Russian technology news site, secondary. Result: EXACT by Unicode-aware check (Q16).
   - «Разработчиками обеих моделей могут быть только российские юрлица. Все данные должны храниться исключительно на территории России.» [@garant2026legal]. Gloss: "Only Russian legal entities may be developers of both kinds of model. All data must be stored exclusively on the territory of Russia." Speaker: Garant legal reference summary. Role and interest: legal reference service, secondary. Result: EXACT by Unicode-aware check (Q17).

4. Example or case. No documented case of a Russian company's access strategy was found in the notes, only chat leads. The nearest documented case is from outside Russia: when Windsurf lost direct access to Claude, it had to find other computing providers at short notice (see I6.2). The general lesson that travels: a team that kept its prompts, test cases and data in its own hands could change supplier in days, and a team that had not could not. This is an inference, not a sourced finding.

5. Counter-evidence, in proportion. Each option's price may be smaller than it looks. For bulk and routine work a model four months behind is enough for many tasks (the notes' own inference from price and capability data). For the hardest agentic work the gap may matter more than the general index suggests. Portability has a cost of its own: the newest tools tie their best features to one vendor's models, and the JetBrains data show that a third of companies run no cost or model controls at all. Nothing in the sources measures how well any of these options works for Russian teams.

6. Speaker-note material. This insight goes beyond the sources in one respect: the idea of treating models as replaceable suppliers (own evaluation set, routing by task, a tested fallback) is the notes' inference and standard supplier-risk practice, not a finding. Say so if asked. The law's details rest on secondary summaries. For a student the same logic applies in a smaller form: skills that transfer across models (specifying a task, checking a result, building a test) are safe from any access decision, and an open-weight model that runs on available hardware is a legitimate place to learn them. Do not name specific intermediaries on a slide, and do not describe methods of bypassing a provider's or a regulator's controls.

7. Confidence and thesis. Medium for the description of each option's gain and price (assembled from primary and secondary sources). Low for any ranking between them. Supports T14 and connects to T11: what cannot be taken away is what the team itself owns, its data, tests and judgement.

8. Question for the audience. Which of these prices is your organisation already paying without having decided to?

9. Personal angle. T17 says talking to people remains the speaker's source of ideas and that there is no way back from the tools. Plain sentence without a number: "I cannot choose who sells me the model, but I can choose that my own work survives a change of model." Speaker to supply: a moment when he moved a piece of work from one tool or model to another, and what did and did not survive the move.

## Open points

- Unverified items flagged in the notes and kept out of this file: the reported fall in Nvidia's share price with the departure of its CEO around 2026-11-13 (secondary coverage only, no filing checked), and details around US Executive Order 14434 and the Census Bureau's survey wording. Neither is needed for this theme.
- Federal Law 243-FZ: the full text was not read. The absence of a general ban on foreign models, the bill number, the 2032-09-01 transition date and the 2027-03-01 dates rest on press and legal summaries.
- Vedomosti: only the public lead paragraphs were read. The estimate has one source with an interest. The details about account blocking, tenders and model substitution are known only through The Moscow Times relay, which was not fetched.
- Chinese providers' terms for Russian customers, and the licence terms of Chinese open-weight models: no source.
- Standing of Russian models: no independent comparison found.
- Compute by country: the 75 and 15% split is from March 2025 and covers an estimated 10 to 20% of capacity; no 2026 figure was found.
- Rivalry cut-offs other than Windsurf are search-result only; the OpenAI and Cursor item rests on one outlet.
- Size of the open-closed gap is contested between indices (four months on Epoch's index, a wider distance on the Artificial Analysis index, six to seven months reported for cyber capability).
- JetBrains regional divide: cause unknown, Chinese subsample small and heavily weighted, no Russian estimate.
- Tooling limit found during this work: `verify_quotes.py` strips every character outside a to z and 0 to 9 before matching, so it cannot check Cyrillic text (a Russian quote is reduced to its digits and Latin letters, or to nothing). The five Russian quotes here were checked instead with a Unicode-aware contiguous match that applies the same normalisation idea (case-fold, letters and digits only). Their record is therefore not a `verify_quotes.py` result.

## Quote log

English quotes were checked with `verify_quotes.py`; EXACT means a contiguous match after normalisation (the script prints this as VERIFIED with no interleaving note). Russian quotes were checked with a Unicode-aware contiguous match for the reason given under Open points. Paths are relative to `converted/`. Files beginning `i56_` were fetched once for this work with the project scraper from public pages.

| Q | Quote (verbatim) | Key | Speaker, role, interest | Local file | Result |
|---|---|---|---|---|---|
| Q1 | Anthropic and OpenAI now account for 86% of enterprise LLM API spend, up from 67% last year. | menlo2026stateenterpriseai | Menlo Ventures report; investor, Anthropic shareholder | reports/menlo2026.md | EXACT |
| Q2 | The United States dominates AI supercomputers globally, owning about 75% of total computing power in our dataset. China is in second place at 15%. | epochai2025trends | Epoch AI; non-profit research institute | web/d_epoch_trends.md | EXACT |
| Q3 | Open-source remains 4% of spend despite 19% of usage. | menlo2026stateenterpriseai | Menlo Ventures report; investor | reports/menlo2026.md | EXACT |
| Q4 | I think it would be odd for us to be selling Claude to OpenAI | techcrunch2025anthropic | Jared Kaplan, co-founder and Chief Science Officer of Anthropic, quoted by TechCrunch; vendor | web/i56_tc_windsurf.md | EXACT |
| Q5 | Any country or region not listed is unsupported. | anthropicsupported | Anthropic policy page; vendor | web/i56_anthropic_supported.md | EXACT |
| Q6 | Accessing or offering access to our services outside of the countries and territories listed below may result in your account being blocked or suspended. | openai2026apisupported | OpenAI policy page; vendor | web/d_openai_countries.md | EXACT |
| Q7 | forcing the startup to find third-party computing providers on relatively short notice | techcrunch2025anthropic | TechCrunch article text; press | web/i56_tc_windsurf.md | EXACT |
| Q8 | When we identify such usage, we seek to restrict or terminate the customer’s access | anthropic2026pbcform | Anthropic S-1/A; issuer | web/s1a3.md | EXACT |
| Q9 | К августу 2026 г. число продавцов выросло до 50, а оборот таких услуг достиг 100–150 млн руб. в месяц. | vedomosti2026greymarket | Vedomosti, reporting a GPTunneL estimate; business daily, interested source | web/v_art.md | EXACT (Unicode-aware check) |
| Q10 | позволяет государству требовать использования только российских ИИ‑моделей в отдельных государственных информационных системах и других чувствительных сферах | habr2026aisupport | Habr news item on 243-FZ; technology news site | web/habr_law.md | EXACT (Unicode-aware check) |
| Q11 | попытки блокировок VPN вызывают серьёзные проблемы в работе у российских разработчиков | association2026letter | Association "Отечественный софт"; industry lobby | reports/vpn_letter.md | EXACT (Unicode-aware check) |
| Q12 | Since January 2026, the most capable open-weight models have lagged frontier closed models by an average of four months | epochai2026insight | Epoch AI; non-profit research institute | web/i56_epoch_open_closed.md | EXACT |
| Q13 | as of March 2026 Anthropic’s top model leads by just 2.7% | stanfordhai2026aicumulative | Stanford HAI, AI Index 2026; academic institute with industry sponsors | web/d_aiindex_top.md | EXACT |
| Q14 | This gap may be understated: open-weight models tend to perform worse on private benchmarks compared to closed models | epochai2026insight | Epoch AI, chart note | web/i56_epoch_open_closed.md | EXACT |
| Q15 | JetBrains users may be more willing to respond | makeeva2026archiving | Makeeva and Molotova, JetBrains survey team; dataset producers | reports/WAPOR2026_makeeva.md | EXACT |
| Q16 | может использовать зарубежные компоненты, распространяемые на условиях открытой лицензии | habr2026aisupport | Habr news item on 243-FZ; technology news site | web/habr_law.md | EXACT (Unicode-aware check) |
| Q17 | Разработчиками обеих моделей могут быть только российские юрлица. Все данные должны храниться исключительно на территории России. | garant2026legal | Garant legal summary; legal reference service | web/law243.md | EXACT (Unicode-aware check) |

Short phrases quoted in passing and checked the same way: "majority-owned or controlled" (web/i56_anthropic_supported.md), "similar to the gap between GPT-5 and GPT-5.5" (web/i56_epoch_open_closed.md). Unverified, keep off slides: any wording attributed to Russian experts in The Moscow Times relay, and all wording from the Telegram chat. No quote that was checked failed verification; one Epoch sentence first returned PARTIAL because two sentences of a chart note had been joined, and it passed once cut at the sentence boundary (Q14).

## Bibliography additions needed

No source cited in this file lacks a key. The following corrections and file links for existing entries were learned from local copies.

- `anthropicsupported`: add `file = {converted/web/i56_anthropic_supported.md}`. The bracketed description says "about 185 countries and regions"; the page fetched on 2026-11-17 lists exactly 185 entries. Exact page title not captured by the scraper.
- `anthropic2025extending`: add `file = {converted/web/i56_anthropic_ownership.md}`. Exact title not captured; the URL slug reads "updating-restrictions-of-sales-to-unsupported-regions".
- `techcrunch2025anthropic`: add `file = {converted/web/i56_tc_windsurf.md}`. The description quotes Kaplan as "it would be odd for us to sell Claude to OpenAI"; his words in the article are "I think it would be odd for us to be selling Claude to OpenAI". Level stays "secondary".
- `epochai2026insight`: add `file = {converted/web/i56_epoch_open_closed.md}`. The chart on the page is headed "Open models lag state-of-the-art closed models by 4 months"; whether that is also the page title was not captured.
- `garant2026legal`: add `file = {converted/web/law243.md}`. The local copy carries the document heading «Федеральный закон от 26 июля 2026 г. № 243-ФЗ "О поддержке развития технологий искусственного интеллекта в Российской Федерации"», which can replace the bracketed description.
- `stanfordhai2026aicumulative`: the bracketed description mentions only supercomputer counts; the same local page (converted/web/d_aiindex_top.md) also carries the 2.7% US and China gap and the Arena scores 1,503 and 1,464 used here. A proper title would be "The 2026 AI Index Report" (by analogy with the 2025 entry; confirm on the page).
- `jetbrains2026rawdata`: no URL and no local file are recorded; the regional cross-tabs used here exist only in the notes file `user_supplied_sources.md` and in the tabulation `jb_tab.txt` outside the project.
- Possible duplicate to resolve: `iea2026keyquestions` and `ieakeyquestions` point to the same report at different verification levels.

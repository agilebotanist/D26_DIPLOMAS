# Russian IT labour market: citable data for the talk (as of 2026-11-19)

Reading guide. This file closes the "no Russian data" gap and checks the disputed figure "hh.ru: about 19 CVs per junior IT vacancy, about 2 per senior". Method: discovery through Google News RSS (ru) and web search, then full-page scrapes with the browser scraper; two PDFs (hh.ru monthly review, HSE preprint) converted to text and read. Tags:

- [P] primary: the publisher of the data, read in full text in this session (hh.ru dashboard or report, Habr Career's own report, Bank of Russia, company press release, HSE preprint).
- [S] secondary: a news article read in full text that relays the data (named original in brackets).
- [SR] search snippet only; body not read. Do not put [SR] items on a slide without opening them.

Scratch copies of every page read are in `/Users/andy/tmp/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/ru/`.

A warning that applies to everything below: the three job boards measure different things. hh.ru's hh.index is active CVs divided by active vacancies on hh.ru (all Russia, monthly averages). Habr Career counts vacancies posted on its own, much smaller, IT-only board, and its salaries come from a self-reported salary calculator, not from vacancies. SuperJob counts its own vacancies and CVs. Their percentages for "vacancy decline" therefore differ (−21% to −56% for the same half-year) and must not be mixed on one chart.

## 1. Verdict on "19 CVs per junior vacancy, 2 per senior"

Takeaway: the junior number is real hh.ru data, but it is 2025 data for programmers and developers only, and the senior number in the talk is the training company's, not hh.ru's. hh.ru's own figure for seniors was 3, not 2. hh.ru does not publish an experience-level split on its public dashboard or in its monthly reviews, so the split exists only as numbers hh.ru gave to the press.

- What hh.ru itself said. hh.ru analysts told Kommersant: January to August 2025, more than 88,000 vacancies for programmers and developers, 14 active CVs per vacancy on average; juniors 18.6, middles 14.7, seniors 3. A year earlier: juniors 9.8, middles 7.5, seniors 1.1. hh.ru's stated causes: more cautious hiring because companies cut budgets, while the wish to "get into IT" has not fallen, and the covid-era course graduates are now becoming middles. CEO Dmitry Sergienkov: in IT "a huge number of people want to work whose skills often do not match employers' expectations". [S] [Kommersant, 11 Sep 2025, "Конкуренция за опытных IT-специалистов в России растет"](https://www.kommersant.ru/doc/8025417) (data: hh.ru, period Jan to Aug 2025, segment: programmers and developers). Same numbers relayed by [S] [Inc. Russia](https://incrussia.ru/news/it-rynok-v-rossii-vakansij-menshe-rezyume-bolshe-konkurentsiya-sredi-dzhunov-rastet/).
- What the talk currently cites. Zerocoder ("Зерокодер", a commercial AI and vibe-coding school) study "based on hh.ru data and other open sources": junior 8 (2021) to 19 (2025), middle 3.5 to 10.5, senior 0.5 to 2.3; whole IT profarea 4.4 (2021) to 22.9 (March 2026). The article closes with the Zerocoder co-founder recommending vibe-coding courses as the fix, so the source sells the remedy. [S] [Inc. Russia, 10 Jul 2026](https://incrussia.ru/news/v-it-tesno-na-vhode-konkurentsiya-sredi-dzhunov-vyrosla-do-19-rezyume-na-vakansiyu/). The study itself was not found online; only press relays exist.
- Comparison. Junior "19" matches hh.ru's 18.6 (Jan to Aug 2025, developers) after rounding, so it is corroborated in substance. Senior "about 2" does not match hh.ru's 3.0; the 2.3 is Zerocoder's own number with unknown method. Middle 10.5 (Zerocoder) vs 14.7 (hh.ru) also differs. The 2021 baselines (8 / 3.5 / 0.5) appear in no hh.ru publication I found.
- Not verifiable from hh.ru's public publications. The public dashboard [P] [stats.hh.ru](https://stats.hh.ru/) and the monthly PDF review [P] [hh.ru "Краткий обзор рынка труда", April 2026](https://stats.hh.ru/api/v1/monthly-report/f-09e48122-625a-4d6d-9e2a-9b1e37e5e772) show hh.index by professional area and region only, with no split by experience.
- Stale by now. The whole IT index has risen a lot since August 2025 (14 for developers then; 22.6 in April 2026; 29.8 in October 2026, see section 2). Any 2025 junior number understates today's pressure, but no current junior figure from hh.ru exists in public.

Suggested slide wording: "hh.ru, Jan to Aug 2025, developers: 18.6 CVs per junior vacancy, 14.7 per middle, 3 per senior (a year earlier: 9.8 / 7.5 / 1.1). Source: hh.ru via Kommersant, 11 Sep 2025." Then add the current whole-IT figure from hh.ru's own dashboard (29.8, October 2026). Drop Zerocoder.

## 2. hh.ru official numbers for IT in 2026

Takeaway: on hh.ru's own dashboard, IT is now one of the most crowded professional areas in Russia: 29.8 CVs per vacancy in October 2026, against 9.0 for the whole market. hh.ru's scale calls 12 or more "extremely high competition".

- October 2026, Russia: hh.index for "Информационные технологии" = 29.8; all professional areas = 9.0. Only marketing (33.7), top management (31.1), arts and media (54.0) and consulting (54.1) are higher; retail is 2.4. hh.ru's scale: ≤1.9 acute shortage of applicants, 2.0 to 3.9 shortage, 4.0 to 7.9 moderate, 8.0 to 11.9 high (employer's market), ≥12 extremely high competition. [P] [stats.hh.ru dashboard, region Russia, "hh.индекс в профобластях за последний месяц", read 19 Nov 2026](https://stats.hh.ru/) (live dashboard; the month shown was October 2026; it will roll forward, so screenshot it for the slide).
- April 2026, Russia: IT hh.index 22.6; IT active vacancies −35% year on year, active CVs +25% year on year; IT is 5.1% of all active vacancies but 11.2% of all active CVs. Whole market: hh.index 10.3, vacancies −25%, CVs +36% y/y. [P] [hh.ru, "Краткий обзор рынка труда", April 2026 (PDF)](https://stats.hh.ru/api/v1/monthly-report/f-09e48122-625a-4d6d-9e2a-9b1e37e5e772), slide "Россия, апрель 2026 года. Рэнкинг по доле от общего числа активных вакансий".
- June 2026 (approx.): HeadHunter told Kommersant that IT salaries rose 3%, average offered pay in IT 98,800 RUB nationally and 151,400 RUB in Moscow, and "22 CVs per IT vacancy". [S] [Kommersant, 10 Jul 2026, "Искод кадров"](https://www.kommersant.ru/doc/8799897) (data: hh.ru; exact month not stated).
- Monthly series for other 2026 months (January 21.3, February 19.6, March 22.9, June 22.4, July 24.4) circulate in blogs and Habr posts by third parties. [SR] e.g. bezpanikiit.ru, habr.com/ru/articles/1011162. Not checked against hh.ru; use only April (PDF) and October (dashboard).
- Share of vacancies open to beginners: hh.ru's Ural press office reportedly said 1,700 IT vacancies without experience in the Ural Federal District, January to August 2026, 13% of IT vacancies there. [SR] [Rossiyskaya Gazeta, 28 Aug 2026](https://rg.ru/2026/08/28/reg-urfo/zolotoe-vremia-dzhunov-zakonchilos-stoit-li-idti-v-it-v-2026-m-i-kak-najti-rabotu.html) (page did not load; regional only).

## 3. Habr Career: juniors vs middles and seniors, salaries, specialisations

Takeaway: Habr Career's own reports show a shrinking board where postings for juniors and interns are about one in ten graded vacancies, middles and seniors about eight in ten; salaries are flat in real terms, and developers had the weakest growth of any group in H1 2026.

Vacancies by grade (Habr Career board; counts of vacancies open for applications in the half-year that state a grade). [P] [Habr Career, "Активность найма на IT-рынке во втором полугодии 2025", 24 Feb 2026](https://habr.com/ru/companies/habr_career/articles/1003122/) and [P] [same series, H1 2025, 22 Jul 2025](https://habr.com/ru/companies/habr_career/articles/929986/). Shares are my arithmetic.

| Grade | H1 2025 | H2 2025 | Change | Share H2 2025 |
|---|---|---|---|---|
| Intern | 304 | 275 | −10% | 3.3% |
| Junior | 637 | 595 | −7% | 7.2% |
| Middle | 5,394 | 3,559 | −34% | 43.3% |
| Senior | 4,234 | 2,904 | −31% | 35.3% |
| Lead | 1,037 | 887 | −14% | 10.8% |
| Total graded | 11,606 | 8,220 | −29% | |

- All vacancies: 10,820 in H2 2025, 38% fewer than in H1 2025. [P] same H2 2025 report. Note the counter-intuitive detail: junior postings fell least in H2 2025; the junior share was already tiny, so the squeeze shows up as competition per posting, not as a further fall in share.
- Competition per posting (Habr Career data relayed by Kommersant): vacancies −17%, responses per vacancy +14%; junior postings drew 129 responses on average, senior postings 58 ("not all respondents belong to that grade"). [S] [Kommersant, 11 Sep 2025](https://www.kommersant.ru/doc/8025417). The article dates this "second half of 2025", which is impossible for a 11 September 2025 article; treat the period as unclear (likely the most recent months).
- H1 2026 vacancies: −56% on the platform (H1 2025: −32%); smallest falls in information security (−40%) and AI (−27%); largest in design, testing and marketing; people searching or open to offers +69%; average IT salary +5% y/y. [S] [Kommersant, 10 Jul 2026](https://www.kommersant.ru/doc/8799897) (data: Habr Career statement to the paper). No Habr Career H1 2026 hiring report with grade counts was found; its hiring-report series ends at H2 2025 [P] [career.habr.com/journal/hiring](https://career.habr.com/journal/hiring).
- Top specialisations by vacancy count, H2 2025: backend 1,833 (17%), system analysts 722, DevOps 556, frontend 386, QA automation 376. [P] H2 2025 hiring report (above).

Salaries (Habr Career salary calculator, self-reported actual pay, not vacancy offers):

- H1 2026: median 191,000 RUB, +4% vs H2 2025 (the Bank of Russia's 2026 inflation forecast is 4.5 to 5.5%, so flat in real terms); Moscow 235,000 (+2%), St Petersburg 200,000 (0%), regions 160,000 (+1%); sample 45,226 salaries. Growth by group: support +10%, marketing +9%, sales +8%, content +6%, QA +5%, analysts +5%, design +3%, developers +1%, HR +1%, management and administration 0%. Within development: backend, frontend, mobile +3%; ERP −22%, database −13%, games −8%. By language: JavaScript −2%, Scala −7%, Python +6%. For comparison Rosstat's H1 2026 average wage for all of Russia: 106,979 RUB. [P] [Habr Career, "Зарплаты IT-специалистов в первой половине 2026 года: рост ниже инфляции", 21 Jul 2026](https://habr.com/ru/specials/1060148/).
- H2 2025: median 183,333 RUB, essentially unchanged from H1 2025 (182,700); regions 159,166 (−1%). [P] [Habr Career, H2 2025 salary report, Feb 2026](https://habr.com/ru/specials/994308/).
- No grade split (junior vs senior pay) appears in either 2026 report. Interpretive quote from an employer published by Habr Career: the main AI effect "is not mass layoffs but slower hiring... while they answer these questions, new positions open more cautiously"; competition rose "in mass specialisations and at entry level", while companies still compete for strong seniors, architects, security and infrastructure experts (Anna Senatorova, HR director, Axiom JDK). [P] [Habr Career blog, "Почему зарплаты в IT перестали быстро расти", Sep 2026](https://habr.com/ru/companies/habr_career/articles/1081998/) (opinion, not data).

Specialisations growing or shrinking, all sources together:

- Shrinking: testing/QA, design, marketing (largest Habr Career vacancy falls, H1 2026); support, network and system engineers, and rank-and-file programmers (demand for programmers −47%, testers −55%, per a CMACP study of 2020 to 2025 vacancy data). [S] [Kommersant, 10 Jul 2026](https://www.kommersant.ru/doc/8799897); [S] [Kommersant, "IT-рынок труда сменил приоритеты", 2026](https://kommersant.ru/doc/9040626) (study: V. Artemenko, CMACP, "Рынок ИТ-специалистов в 2020–2025 годах", Problemy Prognozirovaniya, 2026; original not read; article date not captured, URL id suggests autumn 2026).
- Holding up or growing: information security (smallest fall, −40%), AI/ML (−27%) on Habr Career; business analysts +38% and data specialists +15% in the CMACP study; security vacancies outside tech growing fast (food production +88%, medicine and education +36%, logistics +33%, construction +31%). Sources as above.

## 4. Causes: AI and non-AI, by who says it

Takeaway: every official and analyst source names more than AI. The common list is: budget cuts and frozen projects at a 14% key rate, the end of the post-2022 import-substitution hiring wave, a flood of course and university graduates, and AI as an accelerator mainly of slower entry-level hiring.

- Ministry of Digital Development (Mintsifry), July 2026: fewer vacancies and more CVs "reflect first of all a change in the structure of employer demand and the growing number of young specialists thanks to the development of IT education"; demand for middle and senior specialists with practical experience remains high. No mention of AI. [S] [Kommersant, 10 Jul 2026](https://www.kommersant.ru/doc/8799897).
- SuperJob (head of research Natalya Golovanova), July 2026: IT vacancies −21% y/y in H1 2026, CVs +21%; IT pay +3.9% y/y in June 2026 vs 5.31% inflation; "AI development covers part of companies' need for specialists and 'near-IT' staff"; "the high key rate means R&D projects are postponed until better times"; pay rises only for middle and senior. [S] same Kommersant article.
- hh.ru, September 2025: budget optimisation and cautious hiring; oversupply of course graduates (see section 1). [S] Kommersant, 11 Sep 2025.
- Bank of Russia: key rate held at 14.00% on 23 October 2026; the Bank says the economy is growing "at moderate rates" in H2 2026 and inflation pressure stays elevated. [P] [Bank of Russia press release, 23 Oct 2026](https://www.cbr.ru/press/pr/?file=23102026_133000Key.htm).
- Insurance contributions: Federal Law No. 425-FZ of 28 Nov 2025 replaced the single reduced 7.6% rate for accredited IT companies with 15% on pay up to the contribution base cap and 7.6% above it, from 1 January 2026 (Tax Code art. 427 p. 5). For a typical salary below the cap this doubles the employer's contribution rate. [S] [ppt.ru, legal news, on Law 425-FZ](https://ppt.ru/news/strah-vsnosy/s-2026-goda-menyayutsya-lgotnye-tarify-strakhovykh-vznosov-dlya-it-kompaniy). The 2026 cap is reported as 2,979,000 RUB/year [SR]. I found no Habr Career, hh.ru or Mintsifry statement that quantifies the effect of this change on hiring; it is a plausible cost factor, not a measured cause.
- HSE (Higher School of Economics), exposure, not observed job loss: in "information and communication", 48.9% of workers are in jobs with high AI risk and 71.1% with significant risk (finance 69.7% / 85.3%); about a third of all Russian jobs are exposed; under 1% face full automation; workers aged 20 to 29 have the highest high-risk share of any age group (16%). Method: ILO task-level exposure scores mapped to Russian occupations. [P] [R. Kapelyushnikov, "Риски внедрения искусственного интеллекта для занятости в России", HSE preprint WP3/2026/01, May 2026 (PDF)](https://wp.hse.ru/data/2026/05/28/214621940/WP3_2026_01_____.pdf). Press version: [S] [Finance Mail / Rossiyskaya Gazeta, ~1 Jun 2026](https://finance.mail.ru/article/ii-byil-ne-takov-69211149/), which also quotes a RANEPA expert: in the 2026 slowdown with a high key rate firms favour projects with quick measurable return, so "a mass explosive growth [of AI] in Russia should not be expected".
- CMACP (Centre for Macroeconomic Analysis and Short-term Forecasting): IT vacancies −36% y/y by summer 2025; the author attributes falls in support, network and system engineer demand to automation and LLM use. [S] Kommersant doc 9040626 (above).
- Employment has not fallen: ICT sector average headcount about 1.7 million in Q1 2026, +6.4% y/y, explained by import substitution and digitalisation. [S] [ComNews, 16 Jul 2026](https://www.comnews.ru/content/246418/2026-07-16/2026-w29/1008/sektor-ikt-barabane-rost-vsem-pokazatelyam) (only the teaser was readable; the headcount figure comes from search snippets of the full text [SR]; underlying source presumably HSE ISSEK / Rosstat, not verified). This matters for the talk: fewer openings plus rising headcount means employers are hiring less, not firing en masse.
- Earlier SuperJob figure for beginners: in January 2026 only 10 to 11% of IT vacancies were for people without experience, vs 37 to 38% across the whole labour market; nearly half of those were support roles; junior programmer posts were 1 in 7 beginner vacancies. [S] [Expert.ru, early 2026, "Молодым в IT трудна дорога"](https://expert.ru/obshchestvo/molodym-v-it-trudna-doroga) (data: SuperJob).

## 5. Named companies with dated statements

Sber (Herman Gref):

- Reported 11 Feb 2026 (speech at a public-administration forum, exact day not given): "Last year we cut 20% of staff and 20% of engineers. This was unthinkable. Even three years ago they were growing exponentially at our place." "20% of living people were cut and it was a shock inside the company. We have paused now, but in principle we need to move on." [S] [The Moscow Times (Russian service), 11 Feb 2026](https://ru.themoscowtimes.com/2026/02/11/gref-o-sokrascheniyakh-personala-v-sbere-my-seychas-sdelali-pauzu-no-nado-dvigatsya-dalshe-a186930).
- 19 Jun 2026: Sber cut 65% of regional managers supervising branches using its AI management system; the press office says most moved to other roles. Group headcount 289,700 on 31 Mar 2026; −5.3% in 2025 (308,100 to 291,800). [S] [Interfax, 19 Jun 2026](https://www.interfax.ru/business/1096960).
- November 2026 (strategy presentation, reported 13 Nov): "today more than 50% of code is written by agents... so in routine work the number of engineers employed will shrink, while in new intelligent areas it will grow." In the first nine months of 2026 Sber hired almost three times more AI staff than in all of 2025: 279 ML, 95 other AI roles, 616 data labelling. [S] [The Moscow Times (Russian service), 13 Nov 2026](https://ru.themoscowtimes.com/2026/11/13/sber-v-26g-uvelichil-nabor-sotrudnikov-dlya-raboty-s-ii-a211279) (relaying Sber and Reuters).

Yandex:

- 29 Jul 2026, programme "75/75/75": 73% of Yandex developers use AI regularly and "more than half of new code in the company is created with generative models"; target by end of 2026: at least 75% of developers use AI regularly, AI takes part in at least 75% of code changes and generates at least 75% of the code in each. "Architectural decisions, quality checks and responsibility for the result remain with developers." Internal agent GENA "solves programmers' tasks from ticket to finished code" and is connected to over a thousand projects. [P] [Yandex press release, 29 Jul 2026](https://yandex.ru/company/news/29-07-2026-01). Repeated in [P] [Yandex B2B Tech press release, 24 Sep 2026](https://www.yandex.ru/company/news/24-09-2026-02) (autonomous agents in SourceCraft).
- No Yandex statement on junior hiring or headcount cuts was found. An April 2026 "AI employee doing junior analyst tasks" is reported [SR] (new-retail.ru), not read.

Other companies: no dated T-Bank or VK statement on juniors and AI was found in primary form. Habr Career lists IT Holding T1, Kaspersky Lab and Sber as the largest posters of vacancies in H2 2025 [P] (hiring report above).

## 6. The 5 to 8 strongest figures for slides

1. hh.ru, October 2026: 29.8 CVs per IT vacancy, vs 9.0 for the whole Russian labour market. [P] stats.hh.ru.
2. hh.ru, April 2026: IT vacancies −35% and IT CVs +25% year on year; IT is 5.1% of vacancies but 11.2% of CVs. [P] hh.ru monthly review.
3. hh.ru, Jan to Aug 2025, developers: 18.6 CVs per junior vacancy, 14.7 per middle, 3 per senior (2024: 9.8 / 7.5 / 1.1). [S] Kommersant, 11 Sep 2025.
4. Habr Career, H2 2025: of 8,220 graded vacancies, 7.2% junior and 3.3% intern; 43% middle and 35% senior. [P].
5. Habr Career, H1 2026: median IT salary 191,000 RUB, +4% in half a year, below the 4.5 to 5.5% inflation forecast; developers +1%. [P].
6. Habr Career via Kommersant, H1 2026: vacancies −56%, smallest falls in security (−40%) and AI (−27%), job seekers +69%. [S].
7. Yandex, July 2026: more than half of new code generated with AI; target 75/75/75 by end 2026. Sber, November 2026: "more than 50% of code is written by agents"; engineers cut 20% in 2025. [P] / [S].
8. Counterweight: ICT headcount about 1.7 million in Q1 2026, +6.4% y/y (fewer openings, not mass layoffs) [S/SR], and the IT insurance contribution rate went from 7.6% to 15% (below the cap) on 1 Jan 2026 [S]; key rate 14% [P].

## Gaps

- No current (2026) hh.ru figure for CVs per vacancy by experience level is public. The only hh.ru level split is the 2025 developer figure given to Kommersant.
- The Zerocoder study itself, its method and its 2021 baselines could not be found.
- Habr Career has not published an H1 2026 hiring-activity report with grade counts (or I did not find it); H1 2026 vacancy figures come only through Kommersant.
- No source quantifies how much of the 2026 hiring fall is due to AI versus the insurance-contribution rise versus the key rate; statements are qualitative.
- ComNews ICT headcount figure (1.7 million) was not read in full text; the Rossiyskaya Gazeta Ural item and the CMACP original were not read.
- No Rosstat IT-specific employment series was checked in this pass.

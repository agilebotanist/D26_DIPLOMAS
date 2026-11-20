# Archiving Industry Survey Data for Academic and Community Use

Open datasets on software development, learning, work, and attitudes toward AI

Aleksandra Makeeva, Anastasia Molotova. Surveys team, Strategic Research and Market Intelligence team, JetBrains. alexandra.makeeva@jetbrains.com

79th Annual Conference of the World Association for Public Opinion Research, October 26-29, 2026, Mexico City, Mexico. Poster 1 of 2; companion: "Where Are Developers on the Cultural Map of Human Values?"

Source: raw/WAPOR2026_makeeva.pdf (one page, image only). Text recovered by OCR (pdftoppm at 300 dpi, tesseract `-l eng`) and corrected by eye against the rendered page. Chart values were read from the image where OCR failed. QR codes and layout omitted.

## Header figures

- 780K developers have taken part in our surveys since 2015
- 170K developers took part in our surveys last year
- 198 countries and regions in our latest survey
- 10 languages our surveys are available in

## 01 Background and aim

The Surveys team, part of the Strategic Research and Market Intelligence team at JetBrains, has run large multilingual surveys of software developers, IT specialists, and computer science learners every year since 2017, publishing the anonymized raw data alongside each report.

These datasets are already used in software engineering, human-computer interaction, and computing education research. We believe they hold at least as much for social scientists: measures of work, learning, well-being, values, and attitudes toward AI from a population that general-population surveys struggle to reach.

This poster shows how the data are made, what they contain, and how to obtain them.

## 02 Why developers need a dedicated survey

Software developers, 19.6 million worldwide (JetBrains estimate, 2024), are a large, globally mobile, and well-paid occupational group. In a world where AI is reshaping work faster than any previous technology, they are the first profession whose core task, writing code, is being handed over to AI at scale. How they adapt is an early signal for every other knowledge profession.

They are hard to survey: dispersed, online, privacy-conscious, and survey-fatigued. In large-scale social surveys, they are not absent, but they are coded together with other engineers and technical specialists and are too few in any national sample to analyze.

| Survey | Where developers land, and what that allows |
|---|---|
| World Values Survey (WVS) | "1 Professional and technical (for example: doctor, teacher, engineer, artist, accountant, nurse)". Developers are mixed with all other professionals; no way to compare developers with, say, nurses |
| European Values Study (EVS) | "25 Information and Communications Technology Professionals" (including web developers, programmers, systems analysts, database and network professionals). ICT professionals only, at a high level of generalization; no split between developer types; Europe only |
| Eurobarometer | Any of: "Employed position, working mainly at a desk"; "middle management ... teacher, technician"; "Employed professional (doctor, lawyer, accountant, architect)". IT specialists cannot be distinguished at all; EU-centered, not worldwide |
| European Social Survey (ESS) | 251X "Software and Applications Developers and Analysts". Identifiable, but Europe only; specific roles such as data science or machine learning engineers are not covered; dozens of cases per country |
| International Social Survey Programme (ISSP), Work Orientations IV | 251X "Software and Applications Developers and Analysts". Most detailed, but topic modules rotate, so the last available wave is 2015; not worldwide; same role gaps |

None of these programs asks about the type of development work, as our "job role" question does.

## 03 What you can find in our data

A few examples of questions that may interest social scientists. Developer Ecosystem Survey 2026, weighted shares.

- 58% have experienced burnout in the past 1-2 years. "Have you experienced burnout in the past 1-2 years?" Single choice, n = 9,545
- 71% say studying computer science is worth it in 2026. "Is studying computer science worth it in 2026?" Single choice, n = 9,939
- 84% identify as Generation Z or millennials. "Which generation do you identify with?" Single choice, n = 9,917

Trust in AI to make decisions that affect personal life. "To what extent do you trust AI systems to make decisions that impact your personal life?" Five-point scale, poles labeled, n = 9,641

| 1 Strongly distrust | 2 | 3 | 4 | 5 Strongly trust |
|---|---|---|---|---|
| 19.9% | 20.6% | 35.8% | 17.9% | 5.8% |

Emotions about the growing role of AI in society. "When you think about the increasing role of AI in society, which emotion best describes your overall feeling?" Single choice, n = 19,921

| Emotion | Share |
|---|---|
| Excited | 28.5% |
| Uncertain | 21.6% |
| Hopeful | 19.9% |
| Anxious | 14.0% |
| Fearful | 6.6% |
| Indifferent | 6.2% |
| Other | 3.1% |

Most important ethical concerns about AI. "Which ethical concerns about AI development do you consider to be most important?" Multiple choice, n = 9,836

| Concern | Share |
|---|---|
| Potential for misuse | 59.2% |
| Job displacement | 54.7% |
| Privacy violations | 52.7% |
| Lack of transparency | 47.1% |
| Copyright violations | 39.5% |
| Bias and discrimination | 31.8% |
| Existential risks | 31.4% |
| None | 8.2% |
| Other | 4.0% |

Perceived job security. "How secure do you feel in your current job?" Single choice, n = 6,254

| Answer | Share |
|---|---|
| Completely secure | 12.4% |
| Very secure | 14.7% |
| Fairly secure | 28.6% |
| Fairly insecure | 10.4% |
| Very insecure | 4.4% |
| Completely insecure | 2.8% |
| Hard to say | 24.8% |
| I don't know | 1.9% |

A worked example, Poster 2 of 2: "Where Are Developers on the Cultural Map of Human Values?" (Molotova and Makeeva) uses the 2021 edition's values module, adapted from the WVS, ISSP, EVS, and ESS, to place developers on the cultural value map and to test the "tech elite" hypothesis against national populations.

## 04 How we make, archive, and share the data

1. Localize. Every questionnaire is fielded in 10 languages: English, Chinese, French, German, Japanese, Korean, Brazilian Portuguese, Russian, Spanish, Turkish.
2. Collect. We recruit respondents through: JetBrains channels; external digital marketing campaigns; posts in user groups and tech community channels; peer sharing by respondents.
3. Clean. More than 30 criteria flag suspicious responses, for example: completed too fast; duplicate IP address or email, or over 75% identical answers; one option selected on almost all multiple-choice questions. The full list is in each report.
4. Weight. Weights calibrate the sample to known margins: the share of JetBrains users, regional developer populations, employment status, and use of selected programming languages. Individual weights minimize variance subject to these margins (dual method of Goldfarb and Idnani, 1982, 1983).

Known limitations. Because we survey online, our samples are nonprobability samples, and coverage and self-selection limitations remain after cleaning and weighting. JetBrains users may be more willing to respond, and as the ecosystem keeps evolving, fluctuations between editions cannot be fully ruled out.

Developer Ecosystem Survey 2026. Who: professional developers and coding students worldwide, on tools, practices, work, and attitudes. 56,970 responses collected; 22,082 complete responses after filtering; 198 countries and regions. Tenth annual edition, fielded from May to July 2026: up to 585 questions with adaptive routing and random submodules, about 30 minutes to complete. Topics span languages and tools, infrastructure, developer experience, AI adoption and attitudes, and life and work: job market, pay, job security, burnout, and well-being. The report and raw data will be published in November 2026. The 2025 edition (24,534 developers, 194 countries) is already public with raw data.

Computer Science Learning Curve Survey 2024. Who: people learning computer science worldwide, both formal students and self-taught enthusiasts. 28,500+ answers collected; 18,032 complete responses after filtering; 173 countries. Fielded from mid-February to the end of June 2024 through targeted ads, a consented research panel, and external panels for underrepresented regions. The questionnaire has 87 questions in 10 topics. The research dataset is archived on Zenodo together with an ACM CompEd 2025 paper (arXiv:2508.05286).

Python Developers Survey. Who: Python users. 30,000+ participants in 2024. An annual survey run jointly by the Python Software Foundation and JetBrains PyCharm. Raw data are published with each edition.

Django Developers Survey. Who: Django users. 4,600+ Django users in 2025. An annual survey run by the Django Software Foundation together with JetBrains PyCharm. Raw data are published with each edition.

Archiving. Every dataset ships as one downloadable ZIP archive with the same structure for every survey, so files from different editions can be processed with the same code: README (scope, edition, cleaning, and weighting notes); LICENSE (Creative Commons Attribution 4.0 International); answers.csv (respondent-level data in narrow and wide formats, with weights for each respondent); questions.csv (question texts and answer options, codebook); questionnaire.pdf (full instrument including all survey logic). Free to reuse, share, and build upon with attribution (CC BY 4.0).

## 05 How researchers already use the data

- Framework-usage shares from the 2024 survey ground a Java migration benchmark. Pavuluri, A., et al. (2026). ScarfBench: A benchmark for cross-framework application migration in enterprise Java. arXiv:2605.06754.
- The 2023 AI module informed a study of AI coding assistants in practice. Sergeyuk, A., Golubev, Y., Bryksin, T., & Ahmed, I. (2024). Using AI-based coding assistants in practice: State of affairs, perceptions, and ways forward. Information and Software Technology. https://doi.org/10.1016/j.infsof.2024.107610
- Python survey results motivate a framework for reproducible scientific workflows. Zills, F., Schäfer, M., Tovey, S., Kästner, J., & Holm, C. (2024). ZnTrack: Data as code. arXiv:2401.10603.
- Secondary analysis of 2024 raw data: coding experience and the roles given to AI tools. Zakharov, I., Koshchenko, E., & Sergeyuk, A. (2025). From teacher to colleague: How coding experience shapes developer perceptions of AI tools. GenAICHI Workshop, CHI 2025. arXiv:2504.13903.

## Conclusions

- Developers are a large, mobile, high-leverage occupation that general-population surveys cannot separate out. Dedicated industry surveys are the only large-n source.
- Those surveys already contain material of interest well beyond technology: work, learning, well-being, values, and attitudes toward AI.

Download all reports, methodology, questionnaires, and raw data: jetbrains.com/resources/industry-reports

Copyright 2026 JetBrains s.r.o. Data licensed under CC BY 4.0.

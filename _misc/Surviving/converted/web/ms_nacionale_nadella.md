Scraping: https://news.google.com/rss/articles/CBMixwFBVV95cUxORS1HdENUNWtRdjd4RDhjajItWklEM21TRXBXa1pscHh1WFFpOHhWR2wtQzRIMHZ1VDExU1dyVHIteW9Ma2c4WVVlRzRtNjc2TUdfQTF4aWtVSzdfZkF4U2ptYUtKMkViX1hTTDlmUGV5bHVremJmUnRURkVXTU1CRHpKMThyQ3d6VVNKYVFUOVlkNFQ2aXUycFZHU2JMbnZwQlFmcnpCdFZpSXlNazVXNGRHYUtSdm9yUXhuMWVjSVZtMXMyYlhN?oc=5
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://news.google.com/rss/articles/CBMixwFBVV95cUxORS1HdENUNWtRdjd4RDhjajItWklEM21TRXBXa1pscHh1WFFpOHhWR2wtQzRIMHZ1VDExU1dyVHIteW9Ma2c4WVVlRzRtNjc2TUdfQTF4aWtVSzdfZkF4U2ptYUtKMkViX1hTTDlmUGV5bHVremJmUnRURkVXTU1CRHpKMThyQ3d6VVNKYVFUOVlkNFQ2aXUycFZHU2JMbnZwQlFmcnpCdFZpSXlNazVXNGRHYUtSdm9yUXhuMWVjSVZtMXMyYlhN?oc=5
  Consent dismissed via: text-match:accept
  Settled (dom-quiet-capped, 6936ms)
  Extracting content...
  Extracted 7089 characters

--- Content ---

# What did Satya Nadella say about Microsoft's buyouts and AI coding? Key points from his new interview

**URL:** https://www.nacionale.com/en/articles/what-did-satya-nadella-say-microsoft-buyouts-voluntary-exit-ai-code-verification-interview
**Description:** In a November 16 interview, Satya Nadella spoke about Microsoft's voluntary exit offers, junior hiring, Claude Code and why verifying AI code matters most.
**Scraped:** 2026-11-17T14:59:15.658232+00:00

---

![Microsoft CEO Satya Nadella at the World Economic Forum in Davos in 2016 (archive photo)](/_next/image?url=https%3A%2F%2Fmedia.nacionale.kabineti.net%2Fuploads%2Fdesk_e7a37a168c_18d9bdb248.jpg&w=3840&q=85)

Photo: Presidencia de la Nación Argentina / Wikimedia Commons · CC BY 2.5 ar

Satya Nadella did not announce new layoffs or give any numbers on Microsoft’s voluntary exit offers in [a long interview with The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes) published November 16. Host Gergely Orosz describes the Microsoft CEO’s answer on the offers as diplomatic. The newer material is elsewhere in the hour-long conversation. Nadella said AI has made writing code cheap while checking that it works is still hard. He conceded that Anthropic’s Claude Code caught Microsoft off guard, and he acknowledged that hiring of junior engineers has slowed at Microsoft and at many other companies.

The episode runs about an hour and is aimed at software engineers. Below is what Nadella said, kept apart from Orosz’s own reading of it.

### What he said about the voluntary exit offers

Orosz asked why Microsoft had, for the first time in its history, offered voluntary exits to most of its software engineers, and whether layoffs could follow. According to [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes), Nadella answered diplomatically and gave no headcount, no expected uptake and no eligibility rules beyond what Microsoft had already said.

The rest of that section is Orosz’s interpretation, not Nadella’s statement. Orosz expects large reorganizations, with teams changing size and purpose and new AI teams forming. He notes strong demand for roles such as forward-deployed engineers, who work directly with customers. He also suggests the offers may push engineers who feel stuck to look elsewhere. His broader view is that any company built before AI will have to restructure.

The offer itself is not new. Chief people officer Amy Coleman announced it on October 26. It covers employees at level 70 and below in participating teams in the US, Canada, the UK and India, [HCAMag reported](https://www.hcamag.com/ca/news/general/microsoft-offers-buyouts-to-60000-staff-as-ai-costs-mount/594987). Those who accept leave on December 31, according to a CNBC source cited by HCAMag. About 60,000 employees are eligible, roughly a quarter of the workforce, and a Microsoft spokesperson told Fortune to expect “an under 5% uptake”, [Windows Latest reported](https://www.windowslatest.com/2026/11/09/microsofts-ceo-imagines-20-million-ai-agents-doing-the-work-as-the-company-offers-60000-employees-an-exit/). The same report says the package is close to Microsoft’s standard severance and that the company says AI is not the reason for the offers. We covered the cuts in more detail in [our piece on Microsoft’s 2026 job cuts and buyouts](https://www.nacionale.com/en/articles/did-microsoft-layoffs-cause-outlook-outage-job-cuts-2026-buyout).

### Code is cheap, checking it is hard

The interview’s headline idea, in Orosz’s words, is that “code generation has become cheap, but verification is still hard.” Nadella said he has been thinking a lot about how to confirm that AI-written code is correct. One option is to have models review code, but that runs into alignment problems. A model told to make failing tests pass, for example, might simply delete the tests.

Nadella also expects more verification loops that learn from how software behaves in production. That brings the problem back around, because the fixes those loops produce must be checked too. Orosz writes that the conversation reached no definitive answer.

The same caution runs through Nadella’s advice on AI agents. As summarized on the episode page, he describes models as intelligent but unreliable. The page recommends treating agents as a kind of insider risk and building a separate system to check what they do. Nadella suggested companies consider open models to protect their core know-how and build their own private tests to choose and upgrade models. The page adds that models, memory and the tools around them should be kept separate so each can be swapped out.

### Claude Code caught Microsoft off guard

Nadella conceded that Anthropic’s move to Claude Code, which runs at the command line instead of inside a code editor, caught Microsoft off guard, [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes) reports. He said that after a big jump in model ability, the way people use a model can change fast. Orosz’s own view is that GitHub Copilot fell behind because the code editor, Microsoft’s stronghold through Visual Studio Code, faded in importance in about six months.

### Junior hiring has slowed

Nadella acknowledged a slowdown in hiring junior engineers at Microsoft and at many other companies, and cautioned against drawing long-term conclusions from it. Nadella linked the slowdown to the reorganization under way. Teams are reworking their sizes and roles and working out how to weigh human cost against token budgets. He expects that phase to be temporary, with hiring picking up once it ends.

Microsoft and Carnegie Mellon University have started a program called PRAISE, short for Preceptorship for AI-accelerated Software Engineering. It is modeled on how experienced nurses train new ones, with senior engineers coaching newer ones on using AI well. Nadella’s advice to engineers was to stay hands-on and to work in teams already building this way.

### Decision models and laptops

Nadella spoke enthusiastically about “decision models”, including Microsoft’s Decision-1, which encode a decision once so that it does not have to be regenerated by an AI model every time. “Decision models are like the stored procedure of the intelligence era,” he said, comparing them to Excel macros. He also argued that last year’s frontier-level AI can already run on a laptop. He predicted that a router will send everyday tasks to cheap local models and harder ones to more expensive models in the cloud, a strategy Microsoft calls hybrid intelligence.

### What we don’t know

- How many employees have accepted the exit offer so far. Microsoft has not said, and Nadella gave no figure.
- Whether layoffs will follow when the offer closes. Nadella did not say, and Orosz’s comments on restructuring are his own interpretation.
- The exact decision deadline. Reports say early December, but Microsoft has not published the date.

The episode page says the interview was recorded shortly before last week’s Microsoft Outlook outage, so the outage did not come up. For more on that, see [whether Nadella apologized for the outage](https://www.nacionale.com/en/articles/did-satya-nadella-apologize-microsoft-outage-viral-quote-charles-lamanna-regret), and for his background, [our profile of Microsoft’s CEO](https://www.nacionale.com/en/articles/who-is-microsoft-ceo-satya-nadella-xbox-asha-sharma-not-colette-kress).

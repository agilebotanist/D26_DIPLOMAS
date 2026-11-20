# Fact-check: agent-commerce claims suggested by a reader (checked 2026-11-19)

Reading guide. A reader suggested six claims for the slide on how businesses survive the AI-agent era. Each section gives the claim as suggested, the primary source, its exact wording, date, sample and method, and a verdict: confirmed, different wording or number, unverifiable, or misattributed.

Tags. `[P]` primary source read directly in this session. `[S]` secondary source only (news coverage of a paywalled original, or a search summary), not read at source. Scratch copies of every page read are in `~/tmp/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/agentcom/`.

## 0. Summary for the slide

| # | Claim as suggested | Verdict | What to put on the slide instead |
|---|---|---|---|
| 1 | 40% of B2B buyers use agents vs 24% of suppliers ready (Deloitte) | Different wording and number | "38% of large US B2B buyers already use agentic AI in purchasing; 24% of suppliers use it in sales" (Deloitte Digital, survey Aug to Sep 2025, n = 530 + 530) |
| 2 | Stripe: 70% of CLI API requests come from agents provisioning services autonomously | Number confirmed, wording overstated | "70% of Stripe CLI requests for API resources come from agents" (Stripe, 2026-06-11) |
| 3 | "The primary users of the Internet are no longer human. They're AI agents." (a16z) | Confirmed, verbatim | Credit Olivia Moore and Justine Moore, a16z, 2026-11-10 |
| 4 | Open protocols MCP, UCP, ACP | Confirmed, with an ambiguity on "ACP" | MCP (Anthropic, 2024-11-25), UCP (Google with Shopify, Etsy, Wayfair, Target, Walmart, 2026-01-11), ACP (OpenAI and Stripe, 2025-09-29) |
| 5 | Bill Gates, *Business @ the Speed of Thought* (1999): "If your business is not on the Internet, then your business will be out of business" | Misattributed (not in the book, no primary source found) | Drop it, or use the line that is in the book (section 5) |
| 6 | AI providers trained on clients' data, then launched a similar product | No proven AI-lab case found; the documented precedent is Amazon (seller data, not model training) | "Platforms have been accused of this: the EU found preliminarily that Amazon relied on its sellers' non-public data to compete with them (2020)" |

## 1. Deloitte: buyers vs suppliers using agentic AI

**Claim.** "40% of B2B buyers use AI agents vs. only 24% of suppliers ready for them."

**Primary source** `[P]`. Paul do Forno, Apurva Pangam and Pooja Warudkar, *Accelerating sales growth through B2B digital commerce*, Deloitte Digital, January 2026. PDF: https://www.deloittedigital.com/content/dam/digital/nl/pdfs/2026/deloitte-digital-b2b-commerce-research-report.pdf (landing page: https://www.deloittedigital.com/us/en/insights/research/b2b-commerce-trends.html).

Exact wording, section "Agentic AI in B2B commerce":

> "According to our research, 45% of all B2B suppliers currently use AI and 24% of all B2B suppliers use agentic AI."
>
> "Among buyers, adoption of AI and agentic AI in purchasing processes is higher, with 61% of respondents using AI and 38% using agentic AI."

The graphic beside it adds that 67% of suppliers are "planning to use [AI agents] in the future".

Method (report, "Methodology"). Two blind surveys commissioned by Deloitte Digital and conducted by Lawless Research in August and September 2025. 530 suppliers and 530 buyers, each a full-time employee of a US B2B company with 1,000 or more employees and $100 million or more in annual revenue, director level or above, in sales, commerce, IT, operations or executive roles, across 14 sectors (agriculture to wholesale). Self-reported, not validated by Deloitte (the report's own disclaimer). No definition of "agentic AI" is given to respondents in the published text.

**Secondary Deloitte page that rounds the number** `[P]`. Apurva Pangam, Gagan Mehra and Paul do Forno, "Agentic commerce: The future of B2B commerce", Deloitte, 2026-06-26, https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/articles/b2b-agentic-commerce.html:

> "Nearly 40% of B2B buyers already use agentic AI in purchasing — evaluating products, configuring orders, reviewing contracts, and benchmarking prices. Supplier adoption is trailing but poised to grow, with 24% of suppliers using agents in the sales process and 67% reporting that they plan to in the future."

**Verdict: different wording and number.** The figure is 38%, which Deloitte itself rounds to "nearly 40%". The 24% measures suppliers *using* agentic AI in their own sales process, not suppliers being "ready for" buyers' agents; the survey does not measure readiness for agent buyers at all. The comparison is also between two different samples (buyers and suppliers are different firms), so "vs" is a contrast of adoption rates, not a matched gap. Scope is large US companies only.

## 2. Stripe: 70% of CLI requests from agents

**Claim.** "Stripe reports that 70% of its CLI API requests already come from agents provisioning services autonomously."

**Primary source** `[P]`. Rami Banna (Product Lead, Stripe Projects), "Stripe Projects adds new agent integrations, more providers, and custom developer controls", Stripe blog, 2026-06-11, https://stripe.com/blog/stripe-projects-adds-new-agents-providers-developer-controls.

> "Agent traffic to Stripe's documentation grew more than 10x in 2025 and now makes up nearly 40% of docs traffic. We've also seen exponential growth in new Stripe CLI users over the past year, with 70% of CLI requests for API resources coming from agents."

Method: Stripe's internal telemetry. No period, denominator, or definition of how a request is classified as coming from an agent is given. a16z repeats it accurately ("70% of CLI requests for API resources", citing this post).

**Verdict: number confirmed, wording overstated.** The 70% is a share of Stripe CLI requests for API resources. It does not say the agents were "provisioning services", nor that they acted "autonomously": the post presents provisioning (Stripe Projects) as the thing that is still "too hard for agents to do on their own" and that the product is meant to fix. Correct phrasing: "70% of Stripe CLI requests for API resources come from agents (Stripe, June 2026)".

## 3. a16z: "The primary users of the Internet are no longer human"

**Primary source** `[P]`. Olivia Moore and Justine Moore, "Welcome to the B2A Economy", a16z, 2026-11-10, https://a16z.com/welcome-to-the-b2a-economy/.

Opening lines, verbatim:

> "The primary users of the Internet are no longer human. They're AI agents.
>
> Agents now make up the majority of web traffic, write more than half of new articles published online, and generate most of the code pushed to production."

Nature of the source. A venture-capital essay, first of a series, not a study. The traffic claim rests on a chart of bot vs human web traffic (Stripe's June post links Cloudflare Radar for "agent traffic surpassed human traffic"). The essay also cites Shopify (AI-driven traffic to stores up 8x year over year in Q1 2026, orders from AI searches up nearly 13x), Human Security (agentic browser traffic up 8x between August and October 2026), Supabase, Neon, Stripe and Vercel. a16z invests in agent companies, and its posts carry the standard disclaimer that views are those of the individual personnel quoted.

**Verdict: confirmed, verbatim.** Attribute to the authors ("Olivia and Justine Moore, a16z, Nov 2026"), and present it as an investor thesis, not a measurement. "Users" stretches "majority of web traffic": bot traffic is not the same as agent users acting for people.

## 4. The protocols: MCP, UCP, ACP

**MCP, Model Context Protocol.** Open standard for connecting AI applications to tools and data. Introduced by Anthropic on 2024-11-25. Donated to the Agentic AI Foundation, a directed fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI, on 2025-12-09 `[S]`, https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation (launch post: https://www.anthropic.com/news/model-context-protocol; neither read in this session). It is a general agent-to-tool protocol, not a commerce protocol.

**UCP, Universal Commerce Protocol.** Open standard (Apache 2.0) for agentic shopping: product discovery, cart, checkout and post-purchase. Announced by Google on 2026-01-11 at the NRF conference; co-developed with Shopify, Etsy, Wayfair, Target and Walmart, endorsed by 20+ companies including Adyen, American Express, Best Buy, Mastercard, Stripe, The Home Depot, Visa and Zalando. Designed to work with A2A, AP2 (Google's Agent Payments Protocol) and MCP. Primary: Amit Handa and Ashish Gupta, "Under the Hood: Universal Commerce Protocol (UCP)", Google Developers Blog, 2026-01-11, https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/ `[S]` (the date, authors and partner list come from the post's header and coverage; body not read).

**ACP, Agentic Commerce Protocol.** Open standard (Apache 2.0) "codeveloped by Stripe and OpenAI" for programmatic checkout between buyers, AI agents and businesses, with the business remaining merchant of record. Announced 2025-09-29; its first implementation was Instant Checkout in ChatGPT (US users buying from US Etsy sellers, Shopify merchants announced). Primary `[P]`: Jeff Weinstein and Steve Kaliski, "Developing an open standard for agentic commerce", Stripe blog, 2025-09-29, https://stripe.com/blog/developing-an-open-standard-for-agentic-commerce. Spec: https://agenticcommerce.dev/. One secondary glossary says OpenAI scaled back Instant Checkout in March 2026; not verified.

**Ambiguity.** "ACP" also names IBM's *Agent Communication Protocol* (BeeAI, March 2025), which merged into Google's A2A under the Linux Foundation on 2025-08-29 `[S]`, and Zed's *Agent Client Protocol* (editor-to-coding-agent). On the slide, spell out "Agentic Commerce Protocol (OpenAI, Stripe)".

**Verdict: confirmed.** The reader's guess for ACP is correct. Note that UCP and ACP are competing commerce standards (Google camp vs OpenAI camp), while MCP sits underneath both as the tool-access layer.

## 5. Bill Gates: "If your business is not on the Internet, then your business will be out of business"

**What was searched.** Open Library's full-text "search inside" index (https://openlibrary.org/search/inside.json), which covers three Internet Archive scans of the book: `businessspeedoft00gate` and `businessspeedoft00gaterich` (Warner, 1999) and `isbn_9780140283129` (Penguin, 2000). The index demonstrably covers the book's body text (it returns the book for in-text phrases, see below). Also checked: English Wikiquote, "Bill Gates" (raw page, 2026-11-19), and quote-site search results. Log: `agentcom/openlibrary_inside.txt`.

**Results.**

- The exact phrase "your business will be out of business" occurs in three indexed books, none by Gates. The only one attributing it to Gates is Daniel DiPiazza, *Rich20Something* (TarcherPerigee, 2017): "If your business is not on the Internet, then your business will be out of business. — Bill Gates".
- "business is not on the Internet" occurs in seven indexed books; none is the Gates book.
- Wikiquote lists no such quote under Gates (sourced, attributed or misattributed). Quote sites (AZQuotes, Quotefancy, QuoteNova and others) give no source; QuoteNova states that no credible source was found.
- A related sentiment circulated around 2000 without attribution, e.g. Ed McMahon, *Bricks to Clicks* (Stoddart, 2000): "the idea that if you're not on the Internet in two years, you'll soon be out of business".

**What the book does say** `[P, OCR snippet, Penguin 2000 edition]`, about Microsoft itself:

> "If we go out of business, it won't be because we're not focused on the Internet. It'll be because we're too focused on the Internet."

The same line is quoted in later business books (Jeffrey Krames, *What the Best CEOs Know*; *What Makes Great Leaders Great*; Yoffie and Cusumano, *Strategy Rules*).

**Verdict: misattributed (no primary source).** The sentence is not in *Business @ the Speed of Thought*, and no earlier source naming Gates was found; the earliest print attribution found is 2017. Caveat: OCR full-text search can miss a passage, but three independent scans give no hit while the search does find the book's genuine Internet lines. If a Gates line is wanted, use the in-book quote above (and note it is about Microsoft betting on the Internet, not a warning to other firms).

## 6. "AI providers trained on their clients' data and soon after launched a similar product"

No named, documented case was found of an AI lab (OpenAI, Anthropic, Google, Microsoft and others) training a model on its customers' data and then launching a product competing with those customers. A Bloomberg Law commentary dated 2026-11-09 (Benjamin Lajoie, Nelson Mullins, "AI Platforms Create New Risks When They Compete With Customers") says such concerns "no longer appear purely hypothetical" but names no instance; its only named precedent is Amazon `[S, paywalled, read via fetch summary]`. The major labs' business terms say they do not train on API or enterprise data by default.

What exists, ordered by strength of evidence:

**Regulator's preliminary finding, closed by binding commitments, no infringement decision: Amazon and marketplace seller data (not AI model training).**
- European Commission, Statement of Objections, 2020-11-10, IP/20/2077 `[P]`, https://ec.europa.eu/commission/presscorner/detail/en/ip_20_2077: "The Commission takes issue with Amazon systematically relying on non-public business data of independent sellers who sell on its marketplace, to the benefit of Amazon's own retail business, which directly competes with those third party sellers." Its "preliminary findings show that very large quantities of non-public seller data are available to employees of Amazon's retail business and flow directly into the automated systems of that business". The release adds that a Statement of Objections "does not prejudge the outcome".
- European Commission, commitments decision, 2022-12-20, IP/22/7777, cases AT.40462 and AT.40703 `[P]`, https://ec.europa.eu/commission/presscorner/detail/en/ip_22_7777: Amazon commits "not to use non-public data relating to, or derived from, the independent sellers' activities on its marketplace, for its retail business", covering "automated tools and employees". An Article 9 decision "does not reach a conclusion as to whether there is an infringement", but breach can be fined up to 10% of turnover.
- Investigative reporting that triggered much of it `[S]`: Dana Mattioli, *Wall Street Journal*, 2020-04-23, "Amazon Scooped Up Data From Its Own Sellers to Launch Competing Products", based on interviews with more than 20 former private-label employees and documents; example: a car-trunk organiser made by the seller Fortem. Amazon said the claims were not accurate and opened an internal investigation. Coverage: https://www.cnbc.com/2020/04/23/wsj-amazon-uses-data-from-third-party-sellers-to-develop-its-own-products.html.

**Reported allegation, settled without admission: Amazon's investments in startups.** Dana Mattioli and Cara Lombardo, *WSJ*, 2020-07-23, "Amazon Met With Startups About Investing, Then Launched Competing Products" `[S]`. Named cases: Nucleus (video-chat device; Amazon later launched the Echo Show; WSJ reports a $5 million settlement without admission of wrongdoing) and DefinedCrowd (data labelling; AWS later launched Augmented AI, A2I). Amazon said it does not use confidential information shared with it to build competing products. Coverage: https://foxbusiness.com/money/amazon-met-with-startups-about-investing-then-launched-competing-products.

**Pending allegation, AI training on customer data (competing product not the core claim): Figma.** Proposed class action filed 2025-11-21 in California federal court: Figma allegedly enrolled customers by default and trained AI on their designs despite promising not to; claims include trade-secret misappropriation and misrepresentation. Figma says it does not train on customer data without explicit authorisation `[S]`, https://news.bloomberglaw.com/litigation/figma-trained-ai-on-user-data-without-consent-class-action-says.

**Allegation that failed on appeal (public code, not client data): GitHub Copilot.** *Doe v. GitHub*: programmers alleged Copilot was trained on their public repositories. The Ninth Circuit affirmed dismissal of the DMCA claim on 2026-09-16 (No. 24-7700); training-data copyright questions were not decided `[S]`.

**Reverse direction (a customer or third party trained on the provider's data).** OpenAI's 2025 accusation that DeepSeek distilled its models `[S]`; *Thomson Reuters v. Ross*, where a district court held in February 2025 that copying Westlaw headnotes to build a competing legal-research tool was not fair use `[S]`. These do not support the reader's sentence.

**Verdict.** For AI labs: unverifiable, no proven case. For platforms generally: documented as an EU preliminary finding against Amazon (2020), resolved by binding commitments without an infringement decision (2022), plus press-reported allegations. Safe slide wording: "Platforms have been accused of turning client data into competing products: the EU found preliminarily that Amazon used sellers' non-public data to compete with them (2020); Amazon committed to stop (2022). The same risk now applies to AI providers that see their clients' prompts and data."

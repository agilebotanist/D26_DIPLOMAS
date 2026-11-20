Scraping: https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries
  Settled (dom-quiet, 1344ms)
  Extracting content...
  Extracted 13869 characters

--- Content ---

A new study reveals the need for benchmarking and public evaluations of AI tools in law.

Artificial intelligence (AI) tools are rapidly transforming the practice of law. Nearly [three quarters of lawyers](https://www.legaldive.com/news/generative-ai-legal-use-cases-wolters-kluwer-report/700342/) plan on using generative AI for their work, from sifting through mountains of case law to drafting contracts to reviewing documents to writing legal memoranda. But are these tools reliable enough for real-world use?

Large language models have a documented tendency to “ [hallucinate](/ai-definitions/what-are-hallucinations),” or make up false information. In one highly-publicized case, a New York lawyer [faced sanctions](https://www.nytimes.com/2023/05/27/nyregion/avianca-airline-lawsuit-chatgpt.html) for citing ChatGPT-invented fictional cases in a legal brief; [many similar cases](https://www.nytimes.com/2023/12/29/nyregion/michael-cohen-ai-fake-cases.html) have since been reported. And our [previous study](https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive) of general-purpose chatbots found that they hallucinated between 58% and 82% of the time on legal queries, highlighting the risks of incorporating AI into legal practice. In his [2023 annual report on the judiciary](https://www.supremecourt.gov/publicinfo/year-end/2023year-endreport.pdf), Chief Justice Roberts took note and warned lawyers of hallucinations.

Across all areas of industry, [retrieval-augmented generation (RAG)](/ai-definitions/what-is-rag) is seen and promoted as the solution for reducing hallucinations in domain-specific contexts. Relying on RAG, leading legal research services have released AI-powered legal research products that they claim [“avoid”](https://legal.thomsonreuters.com/blog/legal-research-meets-generative-ai/) hallucinations and guarantee [“hallucination-free”](https://www.lexisnexis.com/community/pressroom/b/news/posts/lexisnexis-launches-lexis-ai-a-generative-ai-solution-with-hallucination-free-linked-legal-citations) legal citations. RAG systems promise to deliver more accurate and trustworthy legal information by integrating a language model with a database of legal documents. Yet providers have not provided hard evidence for such claims or even precisely defined “hallucination,” making it difficult to assess their real-world reliability.

### AI-Driven Legal Research Tools Still Hallucinate

In a new [preprint study](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf) by [Stanford RegLab](https://reglab.stanford.edu/) and [HAI](https://hai.stanford.edu/) researchers, we put the claims of two providers, LexisNexis (creator of Lexis+ AI) and Thomson Reuters (creator of Westlaw AI-Assisted Research and Ask Practical Law AI)), to the test. We show that their tools do reduce errors compared to general-purpose AI models like GPT-4. That is a substantial improvement and we document instances where these tools provide sound and detailed legal research. But even these bespoke legal AI tools still hallucinate an alarming amount of the time: the Lexis+ AI and Ask Practical Law AI systems produced incorrect information more than 17% of the time, while Westlaw’s AI-Assisted Research hallucinated more than 34% of the time.

*Read the full study, [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf)*

To conduct our study, we manually constructed a pre-registered dataset of over 200 open-ended legal queries, which we designed to probe various aspects of these systems’ performance.

Broadly, we investigated (1) general research questions (questions about doctrine, case holdings, or the bar exam); (2) jurisdiction or time-specific questions (questions about circuit splits and recent changes in the law); (3) false premise questions (questions that mimic a user having a mistaken understanding of the law); and (4) factual recall questions (questions about simple, objective facts that require no legal interpretation). These questions are designed to reflect a wide range of query types and to constitute a challenging real-world dataset of exactly the kinds of queries where legal research may be needed the most.

![comparison of hallucinated and incomplete responses](https://hai.stanford.edu/assets/images/inline-images/Hallucinations%201.png)

***Figure 1:*** *Comparison of hallucinated (red) and incomplete (yellow) answers across generative legal research tools.*

These systems can hallucinate in one of two ways. First, a response from an AI tool might just be *incorrect* —it describes the law incorrectly or makes a factual error. Second, a response might be *misgrounded* —the AI tool describes the law correctly, but cites a source which does not in fact support its claims.

Given the critical importance of authoritative sources in legal research and writing, the second type of hallucination may be even more pernicious than the outright invention of legal cases. A citation might be “hallucination-free” in the narrowest sense that the citation *exists*, but that is not the only thing that matters. The core promise of legal AI is that it can streamline the time-consuming process of identifying relevant legal sources. If a tool provides sources that *seem* authoritative but are in reality irrelevant or contradictory, users could be misled. They may place undue trust in the tool's output, potentially leading to erroneous legal judgments and conclusions.

![examples of hallucinations from models](https://hai.stanford.edu/assets/images/inline-images/Hallucinations%202.png)

***Figure 2:*** *Top left: Example of a hallucinated response by Westlaw's AI-Assisted Research product. The system makes up a statement in the Federal Rules of Bankruptcy Procedure that does not exist (and Kontrick v. Ryan, 540 U.S. 443 (2004) held that a closely related bankruptcy deadline provision was not jurisdictional). Top right: Example of a hallucinated response by LexisNexis's Lexis+ AI. Casey and its undue burden standard were overruled by the Supreme Court in Dobbs v. Jackson Women's Health Organization, 597 U.S. 215 (2022); the correct answer is rational basis review. Bottom left: Example of a hallucinated response by Thomson Reuters's Ask Practical Law AI. The system fails to correct the user’s mistaken premise—in reality, Justice Ginsburg joined the Court's landmark decision legalizing same-sex marriage—and instead provides additional false information about the case. Bottom right: Example of a hallucinated response from GPT-4, which generates a statutory provision that has not been codified.*

### RAG Is Not a Panacea

![a chart showing an overview of the retrieval-augmentation generation (RAG) process.](https://hai.stanford.edu/assets/images/inline-images/RAG%20blog%203.png)

*Figure 3: An overview of the [retrieval-augmentation generation (RAG)](/ai-definitions/what-is-rag) process. Given a user query (left), the typical process consists of two steps: (1) retrieval (middle), where the query is embedded with natural language processing and a retrieval system takes embeddings and retrieves the relevant documents (e.g., Supreme Court cases); and (2) generation (right), where the retrieved texts are fed to the language model to generate the response to the user query. Any of the subsidiary steps may introduce error and hallucinations into the generated response. (Icons are courtesy of FlatIcon.)*

Under the hood, these new legal AI tools use retrieval-augmented generation (RAG) to produce their results, a method that many tout as a potential solution to the hallucination problem. In theory, RAG allows a system to first *retrieve* the relevant source material and then use it to *generate* the correct response. In practice, however, we show that even RAG systems are not hallucination-free.

We identify several challenges that are particularly unique to RAG-based legal AI systems, causing hallucinations.

First, legal retrieval is hard. As any lawyer knows, finding the appropriate (or best) authority can be no easy task. Unlike other domains, the law is not entirely composed of verifiable *facts* —instead, law is built up over time by judges writing *opinions*. This makes identifying the set of documents that definitively answer a query difficult, and sometimes hallucinations occur for the simple reason that the system’s retrieval mechanism fails.

Second, even when retrieval occurs, the document that is retrieved can be an inapplicable authority. In the American legal system, rules and precedents differ across jurisdictions and time periods; documents that might be relevant on their face due to semantic similarity to a query may actually be inapposite for idiosyncratic reasons that are unique to the law. Thus, we also observe hallucinations occurring when these RAG systems fail to identify the truly binding authority. This is particularly problematic as areas where the law is in flux is precisely where legal research matters the most. One system, for instance, incorrectly recited the “undue burden” standard for abortion restrictions as good law, which was overturned in *Dobbs* (see Figure 2).

Third, sycophancy—the tendency of AI to agree with the user's incorrect assumptions—also poses unique risks in legal settings. One system, for instance, naively agreed with the question’s premise that Justice Ginsburg dissented in *Obergefell*, the case establishing a right to same-sex marriage, and answered that she did so based on her views on international copyright. (Justice Ginsburg did not dissent in *Obergefell* and, no, the case had nothing to do with copyright.) Notwithstanding that answer, here there are optimistic results. Our tests showed that both systems generally navigated queries based on false premises effectively. But when these systems do agree with erroneous user assertions, the implications can be severe—particularly for those hoping to use these tools to increase access to justice among *pro se* and under-resourced litigants.

### Responsible Integration of AI Into Law Requires Transparency

Ultimately, our results highlight the need for rigorous and transparent benchmarking of legal AI tools. Unlike other domains, the use of AI in law remains alarmingly opaque: the tools we study provide no systematic access, publish few details about their models, and report no evaluation results at all.

This opacity makes it exceedingly challenging for lawyers to procure and acquire AI products. The large law firm [Paul Weiss](https://www.bloomberglaw.com/product/blaw/bloomberglawnews/business-and-practice/BNA%200000018f-1b15-dda8-a78f-1f75a0570001) spent nearly a year and a half testing a product, and did not develop “hard metrics” because checking the AI system was so involved that it “makes any efficiency gains difficult to measure.” The absence of rigorous evaluation metrics makes responsible adoption difficult, especially for practitioners that are less resourced than Paul Weiss.

The lack of transparency also threatens lawyers’ ability to comply with ethical and professional responsibility requirements. The bar associations of [California](https://www.calbar.ca.gov/Portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf), [New York](https://nysba.org/app/uploads/2024/04/Task-Force-on-AI-Report-draft-2024-04-02-FINAL.pdf), and [Florida](https://www.floridabar.org/etopinions/opinion-24-1/) have all recently released guidance on lawyers’ duty of supervision over work products created with AI tools. And as of May 2024, [more than 25 federal judges](https://www.law360.com/pulse/ai-tracker) have issued standing orders instructing attorneys to disclose or monitor the use of AI in their courtrooms.

Without access to evaluations of the specific tools and transparency around their design, lawyers may find it impossible to comply with these responsibilities. Alternatively, given the high rate of hallucinations, lawyers may find themselves having to verify each and every proposition and citation provided by these tools, undercutting the stated efficiency gains that legal AI tools are supposed to provide.

Our study is meant in no way to single out LexisNexis and Thomson Reuters. Their products are far from the only legal AI tools that stand in need of transparency—a slew of startups offer similar products and have [made](https://www.midpage.ai/ChatGPT-plugin) [similar](https://vlex.com/products/vincent-ai) [claims](https://www.paxton.ai/post/paxton-ai-has-raised-6m-to-power-fast-highly-accurate-legal-research-and-drafting-using-ai), but they are available on even more restricted bases, making it even more difficult to assess how they function.

Based on what we know, legal hallucinations have not been solved.The legal profession should turn to public benchmarking and rigorous evaluations of AI tools.

*This story was updated on Thursday, May 30, 2024, to include analysis of a third AI tool, Westlaw’s AI-Assisted Research.*

*Paper authors: Varun Magesh is a research fellow at Stanford RegLab. Faiz Surani is a research fellow at Stanford RegLab. Matthew Dahl is a joint JD/PhD student in political science at Yale University and graduate student affiliate of Stanford RegLab. Mirac Suzgun is a joint JD/PhD student in computer science at Stanford University and a graduate student fellow at Stanford RegLab. Christopher D. Manning is Thomas M. Siebel Professor of Machine Learning, Professor of Linguistics and Computer Science, and Senior Fellow at HAI. Daniel E. Ho is the William Benjamin Scott and Luna M. Scott Professor of Law, Professor of Political Science, Professor of Computer Science (by courtesy), Senior Fellow at HAI, Senior Fellow at SIEPR, and Director of the RegLab at Stanford University.*

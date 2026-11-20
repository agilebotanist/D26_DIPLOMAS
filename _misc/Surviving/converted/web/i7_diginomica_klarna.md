Scraping: https://www.diginomica.com/those-shutting-down-salesforce-and-workday-rumors-klarna-no-we-didnt-replace-saas-llm-admits-ceo
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.diginomica.com/those-shutting-down-salesforce-and-workday-rumors-klarna-no-we-didnt-replace-saas-llm-admits-ceo
  Settled (dom-quiet, 2966ms)
  Extracting content...
  Extracted 10491 characters

--- Content ---

![oops](/sites/default/files/styles/scaled_740/public/images/2025-03/man-5989553_640.jpg.webp?itok=83Uf0k0q)

Remember six months ago when payment platform Klarna caused a stir and won itself a lot of media attention when its CEO Sebastian Siemiatkowski declared that it was switching off Salesforce and that Workday wouldn’t be far behind? In comments made to analysts that found their way into the public domain via [the SeekingAlpha website](https://www.seekingalpha.com/), Siemiatkowski stated:

> We just shut down Salesforce. Within a few weeks, we will shut down Workday. We are shutting down a lot of our SaaS providers, as we are able to consolidate.

What was going to replace both of these? All together now - AI, of course. (Go on, admit it, you'd guessed that one, hadn't you?) Klarna had earlier in 2024 revealed an AI-powered assistant for customer service, developed in partnership with OpenAI, that it claimed could perform the work of 700 customer service agents, reducing the average resolution time from 11 minutes to two, which in turn had boosted average revenue per human staffer by 76%. That being so, who needs traditional CRM and HCM systems, eh?

On the eve of both Salesforce’s Dreamforce and Workday’s Rising annual conferences, these were not exactly helpful comments being thrown into the conversational zeitgeist. Both companies actually maintained a dignified stance on the issue, choosing to throw questions back onto the mix rather than engage directly.

For his part, [Salesforce CEO Marc Benioff confirmed that he was aware of the remarks](https://diginomica.com/dreamforce-24-ai-future-work-and-those-klarna-comments) and had reached out to try to find out what was going on, but was still in the dark. This caused him to ask:

> He hasn't said where he's managing this data. How is he managing and sharing this information? How is he achieving compliance governance of his company? What is his institutional memory? Does he have a new type of data management system that he's using a new type of applications? How is he doing this? I thought it was so interesting, but there's no other data. I just know from my own perspective at Salesforce, I need to know who all my employees are and who all my customers are and all their transactions. I think that there's a broad misunderstanding of Artificial Intelligence, how it relates to data management and applications. You know, humans aren't going away…this is a moment where the technology is awesome, but it's about humans with AI driving customer success together.

Meanwhile at Rising, [Workday Co-President Sayan Chakraborty, who plays an integral role in Workday's AI strategy, said bluntly of the Klarna commented](https://diginomica.com/workday-rising-24-rip-out-erp-build-ai-workday-executives-respond):

> It's a specious misunderstanding of what actually ERP and HCM systems do to say, 'I'm going to replace it with AI.' Beyond the AI parts of these technologies, we do a lot under the covers to do that. Have we seen lots of companies build and maintain their own HCM systems and their own financial systems through the decades? Absolutely. There's dozens of homegrown HCMs. What we've seen in the history of humankind is increased specialization and focus on what you do really well. I'm not sure, if I was on an advisory board of a company like that, that I would say, 'You should be diverting your software resources to recreating HCM, CRM, ERP' - and you are going to have to build it for yourself. The AI is not going to build the system for you... I don't think there's an existential threat of people throwing out their their HCM, CRM or ERP for ChatGPT.

## What really happened...

Since then, it’s been radio silence all round on the situation, until this week when Siemiatkowski suddenly chose to raise the subject again to clarify that while Klarna did indeed shut down Salesforce, this didn’t spell the end for the firm. In fact, he suggested, it might be just the opposite. In a lengthy thread on X, he explained that Klarna had decided to explore the potential of AI and Large Language Models, being open to “testing all things that seemed to be trending”.

Now, as a strategic direction that might smack rather of chasing the silver ball across the floor and seeing where you end up. But Siemiatkowski appears to suggest he was not in favor of top-down ‘parenting’, but rather encouraging the ‘kids’ to set their own agendas and boundaries:

> We encouraged all employees to do it allowed them to pursue ideas organically rather than following "management direction" on what they should build.

At which point I rather shudder as I’ve spent long hours in cafes, on trains and in public spaces with ~~spoilt brats~~ kids who were brought up in such a 'progressive' way. But regardless of that negative comparison, there were apparently some valuable lessons learned, according to Siemiatkowski:

> In the early days of ChatGPT, we heard a lot, ‘This tool allows you to feed all your PDFs, all your data sources to a LLM!' However, the old universal truth of data scientists still holds true, even in AI: "shit in, shit out.” Feeding an LLM the fractioned, fragmented, and dispersed world of corporate data will result in a very confused LLM.
>
> Instead we explored a few key concepts: What of our data was actually valuable? What data was duplicative, incorrect, or contradicting? Why was it like that? While people nowadays can criticize Wikipedia, we also reflected on the fact that it is a remarkable achievement—having over 20,000 people collaborate on the largest graph of knowledge that is of high quality, accessibility, and accuracy. What could we learn from this?

At some point in all this, Klarna met Neo4j and it was magic! The Swedish graph database firm introduced Klarna’s teams to its tech and encouraged exploration of data modelling, ontology, vectors and Retrieval-Augmented Generation (RAG). Being exposed to all this seems to have moved Klarna’s thinking on. According to Siemiatkowski

> We store knowledge of Klarna in SaaS, why and what (docs), plans (slides, tickets), performance (sheets), relations (CRM), people (ERP, HR) —all siloed different, creating an unnavigable web of knowledge that requires tons of Klarna specific expertise to operate and utilize. We also recognized that enterprise software has some set of features that are vital for it to operate—features such as audit, versioning, access and edit management, and similar universal needs. Important but further fragmentation that adds friction, admin overhead, and more.

## But what did you actually do with Salesforce and Workday?

So does all of that mean Klarna did indeed try to ditch proven market-leading SaaS solutions with an LLM? Siemiatkowski says:

> We started consolidating; put things together, connected our knowledge, removed the silos. The side consequence of this \[was\] liquidation of SaaS—not, but a lot of them. Not for the license fees, though those savings are nice, but for unification and standardization of knowledge=data.
>
> So no, we did not replace SaaS with an LLM,. Storing CRM data in an LLM would have its limitations. But we developed an internal tech stack, using Neo4j and other things, to start bringing data/knowledge together. Ultimately, we found this very interesting, but more importantly starting seeing serious productivity gains. We allowed our internal AI to use this knowledge, and we realised with the help of \[code editor\] Cursor AI, we could quickly deploy new interfaces and interactions with it.

That's a somewhat more nuanced version of events than ‘look at us, we’re chucking out Salesforce and Workday’ than the scuttlebutt that emerged last August. How *did* everyone get the wrong idea then? Not down to us, guv, protests Siemiatkowski.

> I discussed with one of my board members, should we share this publicly? We decided not to. We hold no grudge against SaaS (not true - I hate some, but won't tell you which). But we are a neo bank, there is limited value for us to share this externally. However, Klarna, being a bank, holds investors earnings call, and in passing I mentioned that we had removed some SaaS software, including Salesforce. Turns out that the recording was leaked to SeekingAlpha and they put out a news post about it. And from there, it went crazy.

Now that the position has been made clear, what then can we all learn from this? Siemiatkowski postulates:

> Will all companies do what Klarna does? I doubt it. On the contrary, much more likely is that we will see fewer SaaS consolidate the market, and they will do what we do and offer it to others. Those are likely to be your next SaaS. And it is very likely that Salesforce will be one of those companies. As highlighted many times, they do so much more than CRM today and hence have the opportunity to become that hub of knowledge that modern companies will seek.

But he warns the SaaS veterans with the confidence only a challenger brand can muster:

> There are also risks for them. They suffer from a fallacy. They started with a clear opinion of how to do things, but over time, as they try to satisfy every whim of any random person working at any large enterprise, they become a glorified database and lose their opinion.

His final thought (for now):

> Just like when mobile came along, we talked about mobile-first, now you need to be AI-first. SaaS will need to learn adopt and evolve. But if they do there is tremendous opportunity ahead.

## My take

> Suddenly, Benioff was asked on stage why Klarna was leaving Salesforce. I was tremendously embarrassed.

Not embarrassed enough to clear things up six months ago, but there ya go….

I said at the time all this fuss broke out:

> As for Klarna, good luck to it. I suspect it’s going to need it. Buy now, pay later, as it were.

For his part, Siemiatkowski gives no indication of regretting the direction Klarna took - and maybe why should he? It’s a feisty, up-and-coming *enfant terrible* of a company. We should be encouraging exploration and innovation and daring to confront sacred cows.

As to why, six months on, he’s decided to provide some clarity on what happened, the clue may lie in scuttlebutt that Klarna is gearing up to go public very soon. It’s going to need total transparency around its finances and spending and not scare the investor horses by allowing the impression to be had that it’s in some way gambling with potentially reckless anti-SaaS adventuring.

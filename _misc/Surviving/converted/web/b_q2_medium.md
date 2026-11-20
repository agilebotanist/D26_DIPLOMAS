Scraping: https://medium.com/@iamdavidchan/did-satya-nadelle-really-say-saas-is-dead-fa064f3d65d1
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://medium.com/@iamdavidchan/did-satya-nadelle-really-say-saas-is-dead-fa064f3d65d1
  Settled (dom-quiet, 2389ms)
  Extracting content...
  Extracted 11133 characters

--- Content ---

Over the winter break, a [podcast by BG2 dropped where they interviewed Satya Nadella, CEO of Microsoft](https://www.youtube.com/watch?v=9NtsnzRFJ_o&ab_channel=Bg2Pod). It flew under the radar a bit. The podcast epsiode provided a fascinating insight into Satya’s mind, how he thinks, and his approaches to problem solving. I came away really impressed and he’s definitely left an impression on me. Of course the conversation inevitably turned to the topic of AI, the co-opetition with OpenAI, and it then led to this incredible 3 minute soundbite around the 46:45 minute mark where he dropped a spicy take that will likely be one of the most discussed / dissected / debated topics in 2025. Talk about starting the new year with a bang!

## “…I think, the notion that \[SaaS\] business applications exist, that’s probably where they’ll all collapse, right in the Agent era…” — Satya Nadella

The setup was that Bill Gurley asked whether Satya was worried that newer startups who are building business applications with a fresh AI-first approach could (and should) obfuscate some of complexity of legacy SaaS business application UIs (for example Excel or a CRM system), and therefore put legacy software providers, like Microsoft under pressure. [Satya’s response was](https://www.youtube.com/watch?v=a_RjOhCkhvQ&t=8s&ab_channel=Manusahoo):

==*“Yeah, I mean, it’s a it’s a very, very, very important question, the SaaS applications, or biz apps. So let me just speak of our own dynamics. The approach at least we’re taking is, I think,*== ==***the notion that business applications exist, that’s probably where they’ll all collapse, right in the agent era,***== ==*because if you think about it, right, they are essentially CRUD databases with a bunch of business logic. The business logic is all going to these agents, and these agents are going to be multi repo CRUD, right? So they’re not going to discriminate between what the back end is. They’re going to update multiple databases, and all the logic will be in the AI tier, so to speak. And once the AI tier becomes the place where all the logic is, then people will start replacing the back ends, right?”*==

A lot to unpack. I think a lot of people were stunned and trying to process what he said. I myself had to re-listen to this soundbite to make sure I understood what he was saying.

These few lines in an almost ninety minute podcast created a bit of a mini firestorm because if you take Satya’s words literally, you could interpret that he implied AI Agents could / would replace SaaS. Many people did infact conclude that was what he was saying, including some of the world’s largest SaaS vendors. But if you listened to the entire podcast, I really believe he was speaking a bit off the cuff in this segment because it would contradict a bunch of other comments he made earlier and later in the podcast.

**Three main takeaways from Satya’s comments:**

**#1 SaaS UI — What is it good for? Absolutely!@#$**

![](https://miro.medium.com/v2/resize:fit:1212/format:webp/1*ihzyBsP3Uq00M0lj2-XnNA.png)

AI Agent interaction with legacy SaaS versus future iteration of SaaS optimized for Agents

Assume for argument’s sake that your objective is to use an AI Agent to replace a human employee. If you think about most SaaS UIs, they are designed for human interaction. Specifically, it’s to help the human employee perform a task. However, if you remove the human out of the equation, and the human employee is no longer the user of the SaaS solution, then wouldn’t it make the UI (e.g. menu items, buttons, where things are above / below the fold) extraneous? Because now the user of the SaaS solution is not a human but an AI Agent. And an AI Agent doesn’t need to *click on anything.* The solve then shouldn’t be to write up a script to hit a bunch of buttons in sequence in a UI. If you took a step back and reimagined the SaaS application for an AI Agent persona, it would probably look a lot different. For example, it would be likely be quicker and way more efficient if the AI Agent can directly interface with the business application itself through APIs etc and execute the task(s)…the UI wouldn’t be needed at all other than to help humans visualize the outputs.

## Get David Chan’s stories in your inbox

Join Medium for free to get updates from this writer.

**#2 Do backends go away, or does the backend not matter?**

![](https://miro.medium.com/v2/resize:fit:1140/format:webp/1*pVsjd9hMLFBzzZvoE2LatA.png)

Today, databases and their schemas limit our ability to orchestrate seamlessly between systems

Satya then oversimplifies SaaS as just a CRUD database. I mean technically is SaaS a CRUD database? Yes, I guess so. But also so much more. The point he was trying to make was more around the backend schemas and he mentioned it earlier in the podcast. Today, there are no universally agreed upon schema standards. The schema used by every SaaS software is almost unequivocally unique and optimized for that application. And because each SaaS solution uses their own \[essentially\] proprietary schema it makes it so hard to orchestrate tasks and actions across multiple business applications because the definition of each data entity varies from app to app. My take is that he’s envisioning a future where AI Agents for each business application can interface auto-magically with each other, and help map out the data entities so everything is apples to apples. Because the promise of an Agentic Eco-system that delivers on unified orchestration of delegated tasks requires a way to make the backend proprietary schemas inconsequential.

**#3 What the heck is the AI Tier?**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ej62Oj4ZCkRNfpbyJA78zQ.png)

Applying Smart Hubs and Dummy Spokes concept to AI Tier

Satya also suggests that all business logic will be moved into the “AI Tier”. I believe he’s saying that today SaaS solutions are implemented with specific requirements and rules but within an org, it may vary from application to application and from function to function which means there is likely inconsistencies. He’s suggesting abstracting that logic from the individual business applications and moving it into an “AI Tier” that is essentially a decisioning layer that provides commands/instructions to each AI Agent for each business application.

It’s actually not an entirely new concept and something that has been discussed in the past. Ben Bloom from Gartner actually came up with something called [Smart Hub and Dumb Spokes](https://www.gartner.com/en/documents/3880127). The idea is that most companies today operate using a Dumb Hub and Smart Spokes model. Think of the SaaS technologies as Smart Spokes, and you aggregate all the information in the Dumb Hub. However, a Smart Hub approach is centralizing the decision making with all the information available, and then passing along the actions to the Dumb Spokes to execute against.

It’s a grand idea that I love, but also think it’s extremely hard to execute against. Technically, we actually have most of the capabilities today. The issue is more buy in and alignment across the organization which unfortunately I don’t think AI can solve for…yet. Just kidding, the answer is never. AI will never solve organizational alignment.

**Final Thoughts**

Did Satya Nadella really say SaaS is DEAD? No. It might be an unpopular opinion though and I might be in the minority. However, if you listen to the full podcast I believe he’s really talking about a transformation and an evolution of what SaaS will look like in the future.

— — — — — — — — — — — FULL TRANSCRIPT BELOW — — — — — — — — — — —

**Bill Gurley:**
*Do you worry that someone might think kind of first principles AI from ground up, and that some of the infrastructure say in an Excel spreadsheet isn’t necessary to know if you did a if you did an AI first product. And the same thing, by the way, could be said about the CRM, right? There’s a bunch of fields and tasks that may be able to be obfuscated for the use?*

**Satya Nadella:**

*Yeah, I mean, it’s a it’s a very, very, very important question, the SaaS applications, or biz apps. So let me just speak of our own dynamics. The approach at least we’re taking is, I think, the notion that business applications exist, that’s probably where they’ll all collapse, right in the agent era, because if you think about it, right, they are essentially CRUD databases with a bunch of business logic. The business logic is all going to these agents, and these agents are going to be multi repo CRUD, right? So they’re not going to discriminate between what the back end is. They’re going to update multiple databases, and all the logic will be in the AI tier, so to speak. And once the AI tier becomes the place where all the logic is, then people will start replacing the back ends, right? We have people. That’s what. In fact, it’s interesting. As we speak, I think we are seeing pretty high rates of wins on dynamics, back ends and the agent use. And we are going to go pretty aggressively and try and collapse it all right, whether it’s in customer service, whether it is in you know, by the way, the other fascinating thing that’s increasing is just not CRM, but even our what we call finance and operations, because people want more AI, native biz apps, right? That means the biz app, the logic tier can be orchestrated by AI and AI agent. So in other words, Copilot to agent to my business application should be very seamless now, in the same way you could even say, Hey, why do I need Excel? Like, interestingly enough, one of the most exciting things for me is Excel with Python is like, GitHub with Copilot, right? That’s essentially so what we have done is, when you have Excel like this, by the way, will be fun for you guys, right? Which is, you should just bring up Excel, bring up Copilot, and start playing with it, because it’s no longer like, oh, you know, it is like having a data analyst, and so it’s no longer just making sense of the numbers that you have. It will do the plan for you, right? It will literally like how GitHub Copilot workspace creates the plan, and then it executes the plan. This is like a data analyst who is using Excel as a sort of row column visualization to do analysis, scratchpad. So it’s kind of tools you so the Copilot is using Excel as a tool with all of its action space, because it can generate and it has Python interpreter, Dao. And that is also true. After all, there’s a code interpreter, right? So therefore you can generate anything. And so, yes, I think there will be disruption. But so the way we are approaching at least our M365 stuff is one is build Copilot, as that organizing layer UI for AI, get all agents, including our own agents. You can say the Excel is an agent through my Copilot. Word is an agent. It’s kind of specialized canvases, which is, I’m doing a legal document. Let me take it into Pages, and then to Word, and then have the Copilot go with it. Go into Excel and have the compiler go with it. And so that’s sort of a new way to think about the work in workflow.*

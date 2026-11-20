Scraping: https://a16z.com/newsletter/big-ideas-2026-part-1/
  Mode: headed | Format: markdown
  Launching visible browser (anti-bot mode)...
  Visible browser ready
  Navigating to: https://a16z.com/newsletter/big-ideas-2026-part-1/
  Settled (dom-quiet, 1456ms)
  Extracting content...
  Extracted 31812 characters

--- Content ---

This first appeared in the a16z News newsletter. [Subscribe](https://www.a16z.news/embed) to stay on top of the latest news.

Our job as investors is to immerse ourselves in the ins-and-outs of every corner of the tech industry in order to understand where things are moving next. So every December, we ask our investing teams to share one big idea they think tech builders will tackle in the year to come.

Today, we’re sharing ideas from our Infrastructure, Growth, Bio + Health, and speedrun teams. Stay tuned for takes from our other teams tomorrow.

## Infrastructure

## Startups tame the chaos of multimodal data

**Jennifer Li**

Unstructured, multimodal data has been enterprises’ biggest bottleneck and their biggest untapped treasure. Every company is drowning in PDFs, screenshots, videos, logs, emails, and semi-structured sludge. Models keep getting smarter but the inputs keep getting messier, which causes RAG systems to hallucinate, agents to break in subtle, expensive ways, and critical workflows to still heavily rely on human QA. The limiting factor for AI companies is now data entropy: the steady decay of freshness, structured, and truth inside the unstructured universe where 80% of corporate knowledge now lives.

**That’s why untangling unstructured data becomes a generational opportunity.** Enterprises need a continuous way to clean, structure, validate and govern their multimodal data so downstream AI workloads actually work. The use cases are everywhere: contract analysis, onboarding flows, claims handling, compliance, support, procurement, engineering search, sales enablement, analytics pipelines, and every agent workflow that depends on reliable context. Startups that build the platform that extracts structure from documents, images, and videos; reconciles conflicts; repairs pipelines; or keeps data fresh and retrievable hold the key to the kingdom of enterprise knowledge and process.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Jennifer-Li-1.png)

#### Jennifer Li

is a general partner at Andreessen Horowitz, where she leads infrastructure investments with an eye on data systems, developer tools and AI.

- [**Investing in General Translation**
	Jennifer Li, Martin Casado, and Jason Cui
	](https://a16z.com/announcement/investing-in-general-translation/)
- [**Investing in TypeSafe AI**
	Jennifer Li, Sarah Wang, Martin Casado, Marc Andreessen, and Ben Horowitz
	](https://a16z.com/announcement/investing-in-typesafe-ai/)
- [**Investing in Preference Model**
	Jennifer Li
	](https://a16z.com/announcement/investing-in-preference-model/)
- [**The Next Frontier of AI Video Is Control**
	Gorkem Yurtseven, Batuhan Taskaya, and Jennifer Li
	](https://a16z.com/podcast/the-next-frontier-of-ai-video-is-control/)
- [**Who Grades the AI Models? | Ben Horowitz & Rayan Krishnan**
	Rayan Krishnan, Ben Horowitz, Jennifer Li, and Erik Torenberg
	](https://a16z.com/podcast/who-grades-the-ai-models-ben-horowitz-rayan-krishnan/)

## AI revives cybersecurity hiring

**Joel de la Garza**

For the better part of the last decade, the biggest challenge CISOs faced was hiring. From 2013 to 2021, the number of unfilled cybersecurity jobs grew from under 1M to 3M. That’s because security teams hire highly skilled technicians to spend their days doing soul-crushing level 1 security work like reviewing logs, and no one wants to do this work. The problem is that cybersecurity teams *create* that drudgery by buying products that detect everything, which means that their teams need to review everything—which, in turn, creates false labor scarcity. It’s a vicious cycle.

In 2026, AI will break this cycle and close this hiring gap by automating much of this repetitive and redundant work for cybersecurity teams. Anyone who has ever spent time working on a large security team knows that half the work is easily solved with automation, but it’s impossible to figure out what to automate when you’re drowning in work. AI-native tools that figure this out for security teams will finally free them up to do what they want to do: chase down bad guys, build new systems, and fix vulnerabilities.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Joel-de-la-Garza-1.png)

#### Joel de la Garza

is a partner focused on information security related investments and other chaos adjacent businesses.

- [**Investing in doxxnet**
	Joel de la Garza and Martin Casado
	](https://a16z.com/announcement/investing-in-doxxnet/)
- [**Rebuilding the Internet for Privacy | Barrett Lyon on DoxxNet**
	Barrett Lyon and Joel de la Garza
	](https://a16z.com/podcast/rebuilding-the-internet-for-privacy-barrett-lyon-on-doxxnet/)
- [**Microsoft’s Deputy CISO on Securing AI Agents**
	Aaron Zollman and Joel de la Garza
	](https://a16z.com/podcast/microsofts-deputy-ciso-on-securing-ai-agents/)
- [**How Do You Defend Against AI That Can Hack?**
	Nick Warner, Max Pollard, and Joel de la Garza
	](https://a16z.com/podcast/how-do-you-defend-against-ai-that-can-hack/)
- [**The CISO Playbook for AI Agents | Datadog**
	Emilio Escobar and Joel de la Garza
	](https://a16z.com/podcast/the-ciso-playbook-for-ai-agents-datadog/)

## Agent-native infrastructure becomes table stakes

**Malika Aubakirova**

In 2026, the biggest infrastructure shock won’t come from outside companies, but from within. We’re shifting from human-speed traffic that’s predictable and low concurrency to “agent-speed” workloads that’re recursive, bursty, and massive.

The enterprise backend of today was built for a 1:1 ratio of human action-to-system response. It’s not architected for a single agentic “goal” to trigger a recursive fan-out of 5,000 sub-tasks, database queries, and internal API calls in under milliseconds. When an agent attempts to refactor a codebase or remediate a security log, it doesn’t look like a user. To a legacy database or rate-limiter, it looks like a DDoS attack.

Building for agents in 2026 means re-architecting the control plane. We’ll see the rise of “agent-native” infrastructure. The next generation must treat “thundering herd” patterns as the default state. Cold starts must shrink, latency variance must collapse, and concurrency limits must jump by orders of magnitude. The bottleneck becomes coordination: routing, locking, state management, and policy enforcement across massive parallel execution. The winning platforms will be the only ones capable of surviving the deluge of tool execution that follows.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2024/09/Malika-Aubakirova-1.png)

#### Malika Aubakirova

was an investor on the AI Infrastructure team at a16z.

- [**Investing in Mirendil**
	Matt Bornstein and Malika Aubakirova
	](https://a16z.com/announcement/investing-in-mirendil/)
- [**Why We Need Continual Learning**
	Malika Aubakirova and Matt Bornstein
	](https://a16z.com/why-we-need-continual-learning/)
- [**Et Tu, Agent? Did You Install the Backdoor?**
	Joel de la Garza, Malika Aubakirova, and Zane Lackey
	](https://a16z.com/et-tu-agent-did-you-install-the-backdoor/)
- [**The Cinderella “Glass Slipper” Effect: Retention Rules in the AI Era**
	Malika Aubakirova
	](https://a16z.com/the-cinderella-glass-slipper-effect-retention-rules-in-the-ai-era/)
- [**State of AI: An Empirical 100 Trillion Token Study with OpenRouter**
	Malika Aubakirova and Anjney Midha
	](https://a16z.com/state-of-ai/)

## Creative tools go multimodal

**Justine Moore**

We now have the building blocks to tell stories with AI: generative voices, music, images, and video. But for anything beyond a one-off clip, it’s often time-consuming and frustrating—if not impossible—to get the outputs you want, especially if you want anywhere near the level of control that a traditional director would have.

Why can’t we feed a model a 30 second video and ask it to continue the scene with a new character created from a reference image and voice? Or reshoot a clip so we can see a scene from a different angle, or make the motion match a reference video?

2026 is the year AI goes multimodal. Give a model whatever form of reference content you have and work with it to make something new or edit an existing scene. We’ve started to see some early products here, like Kling O1 and Runway Aleph. But there’s a lot more to be done—and we need innovation at both the model and application layers.

Content creation is one of the killer use cases of AI, and I expect we’ll see multiple successful products across use cases and types of customers from meme makers to Hollywood directors.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Justine_Moore.png)

#### Justine Moore

is a partner on the investing team at Andreessen Horowitz, where she focuses on AI — both foundation models and applications.

- [**Welcome to the B2A Economy**
	Olivia Moore and Justine Moore
	](https://a16z.com/welcome-to-the-b2a-economy/)
- [**Investing in Highstock**
	Olivia Moore and Justine Moore
	](https://a16z.com/announcement/investing-in-highstock/)
- [**AI Micro Dramas, Generative Media, and the Future of Creativity**
	Justine Moore
	](https://a16z.com/podcast/ai-micro-dramas-generative-media-and-the-future-of-creativity/)
- [**AI, Design, and the Power of Open Models**
	Mohammad Norouzi, Justine Moore, and Yoko Li
	](https://a16z.com/podcast/ai-design-and-the-power-of-open-models/)
- [**Investing in Town**
	Alex Rampell and Justine Moore
	](https://a16z.com/announcement/investing-in-town/)

## The AI-native data stack continues to evolve

**Jason Cui**

We’ve seen a lot of consolidation in the “modern data stack” in the past year as data companies have moved from specialization across ingestion (ETL), transformation, and compute towards bundling and unified platforms. See: the Fivetran/dbt merger and continued rise of unified platforms like Databricks.

While the ecosystem feels notably more mature, we’re still in the early days of a truly AI-native data architecture. We’re excited by ways AI can continue to transform multiple parts of the data stack, and we’re beginning to see how data and AI infrastructure are becoming inextricably linked.

A few ideas we’re excited by:

- How data will continue to flow into performant vector databases alongside traditional structured data
- How AI agents navigate “the context problem”: continuously accessing the right data context and semantic layers in order to build robust applications, like chatting with your data, that always have the correct business definitions across multiple systems of record
- How traditional BI tools and spreadsheets will change as data workflows become more agentic and automated

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/09/Jason-Cui.png)

#### Jason Cui

is a partner at Andreessen Horowitz, where he invests in infrastructure and AI.

- [**Investing in General Translation**
	Jennifer Li, Martin Casado, and Jason Cui
	](https://a16z.com/announcement/investing-in-general-translation/)
- [**Investing in Netris**
	Guido Appenzeller, Raghu Raghuram, and Jason Cui
	](https://a16z.com/announcement/investing-in-netris/)
- [**Investing in Exa**
	Sarah Wang, Jennifer Li, Stephenie Zhang, and Jason Cui
	](https://a16z.com/announcement/investing-in-exa/)
- [**Your Data Agents Need Context**
	Jason Cui and Jennifer Li
	](https://a16z.com/your-data-agents-need-context/)
- [**Investing in Inferact**
	Matt Bornstein, Jason Cui, and Raghu Raghuram
	](https://a16z.com/announcement/investing-in-inferact/)

## The year we step inside video

**Yoko Li**

[![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/12/unnamed.jpg)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/12/unnamed.jpg)

**In 2026, video stops behaving like something we passively watch and starts feeling like a place we can actually step into.** Video models can finally understand time, remember what they’ve already shown us, react when we do something, and hold together with the kind of quiet consistency we expect from the physical world. Instead of producing a few seconds of disconnected imagery, these systems sustain characters, objects, and physics long enough for actions to matter and for consequences to unfold. This shift turns video into a medium we can build on: a space where robots can practice, games can evolve, designers can prototype, and agents can learn by doing. What emerges is less like a clip and more like a living environment, one that starts to close the gap between perception and action. For the first time, it feels like we can *inhabit* the videos we generate.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Yoko-Li-2.png)

#### Yoko Li

is a partner at Andreessen Horowitz, where she focuses on developer tools, infrastructure, AI, and creative tools.

- [**Investing in Eka Robotics**
	Raghu Raghuram and Yoko Li
	](https://a16z.com/announcement/investing-in-eka-robotics/)
- [**Investing in Vals**
	Jennifer Li, Yoko Li, Raghu Raghuram, and Shangda Xu
	](https://a16z.com/announcement/investing-in-vals/)
- [**Knowing When to Stop: The Art of Making a Loop Converge**
	Yoko Li
	](https://a16z.com/knowing-when-to-stop-the-art-of-making-a-loop-converge/)
- [**Investing in Runta**
	Martin Casado, Yoko Li, and Guido Appenzeller
	](https://a16z.com/announcement/investing-in-runta/)
- [**Building AI for Creators | Luma & Phota Labs**
	Matt Tancik, Zach Xia, and Yoko Li
	](https://a16z.com/podcast/building-ai-for-creators-luma-phota-labs/)

## Growth

## Systems of record lose ground

**Sarah Wang**

In 2026, the real disruption in enterprise software is that *the system of record will finally start to lose primacy*. AI is collapsing the distance between intent and execution: models can now read, write, and reason directly across operational data, turning ITSM and CRM systems from passive databases into autonomous workflow engines. And as recent advances in reasoning models and agentic workflows compound, these systems gain the ability not just to respond, but to anticipate, coordinate, and execute end-to-end processes. The interface becomes a dynamic agent layer, while the traditional system of record slips into the background as a commodity persistence tier—its strategic leverage ceded to whoever controls the intelligent execution environment employees actually use.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Sarah-Wang-v2.png)

#### Sarah Wang

is a general partner on the Growth team at Andreessen Horowitz, where she leads growth-stage investments across AI, enterprise applications, and infrastructure.

- [**Investing in TypeSafe AI**
	Jennifer Li, Sarah Wang, Martin Casado, Marc Andreessen, and Ben Horowitz
	](https://a16z.com/announcement/investing-in-typesafe-ai/)
- [**The $1 Trillion AI Buildout | State of Markets**
	David George, Sarah Wang, Alex Immerman, and Santiago Rodriguez
	](https://a16z.com/podcast/the-1-trillion-ai-buildout-state-of-markets/)
- [**Databricks CEO on AI Pacing, Cyber Risk, and the Enterprise**
	Ali Ghodsi, Martin Casado, and Sarah Wang
	](https://a16z.com/podcast/databricks-ceo-on-ai-pacing-cyber-risk-and-the-enterprise/)
- [**Investing in Gimlet**
	Raghu Raghuram, Sarah Wang, Shangda Xu, and Stephenie Zhang
	](https://a16z.com/announcement/investing-in-gimlet/)
- [**You are not a model. Don’t price per token.**
	Tugce Erten and Sarah Wang
	](https://a16z.com/you-are-not-a-model-dont-price-per-token/)

## Vertical AI evolves from information retrieval and reasoning to multiplayer

**Alex Immerman**

AI has driven vertical software to unprecedented growth. Healthcare, legal, and housing companies reached $100M+ ARR within a few years; finance and accounting are close behind. The evolution was first information retrieval: finding, extracting, and summarizing the right information. 2025 brought reasoning: Hebbia analyzing financial statements and building models, Basis reconciling trial balances across systems, EliseAI diagnoses maintenance issues and dispatches the right vendors.

2026 unlocks multiplayer mode. Vertical software benefits from domain-specific interfaces, data, and integrations. But vertical work is inherently multi-party. If agents are going to represent labor, they need to collaborate. From buyers and sellers, to tenants, advisors and vendors, each party has distinct permissions, workflows and compliance requirements that only vertical software understands.

Today, each party uses AI in isolation, which creates handoffs without authority. The AI analyzing purchase agreements doesn’t talk to the CFO for its model adjustments. The maintenance AI does not know what the onsite staff promised the tenant. Multiplayer changes by coordinating across stakeholders: routing to functional specialists, maintaining context, syncing changes. Counterparty AIs negotiate within parameters and flag asymmetries for human review. The senior partner’s markup trains the system for the entire firm. Tasks performed by AI will be completed with higher success rates.

And when value increases from multi-human and multi-agent collaboration, switching costs rise. Here we’ll see the network effects that have eluded AI applications: the collaboration layer becomes the moat.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Alex-Immerman.png)

#### Alex Immerman

is a partner on the Growth team at Andreessen Horowitz, where he focuses on fintech, consumer, enterprise, and crypto/web3 companies.

- [**The $1 Trillion AI Buildout | State of Markets**
	David George, Sarah Wang, Alex Immerman, and Santiago Rodriguez
	](https://a16z.com/podcast/the-1-trillion-ai-buildout-state-of-markets/)
- [**Who Gets Paid When AI Does the Shopping?**
	Alex Immerman and Santiago Rodriguez
	](https://a16z.com/who-gets-paid-when-ai-does-the-shopping/)
- [**From “System of Record” to “System of Intelligence”**
	Gio Ahern, Stephenie Zhang, and Alex Immerman
	](https://a16z.com/from-system-of-record-to-system-of-intelligence/)
- [**Prediction Markets: They Grow Up So Fast**
	Alex Immerman and Santiago Rodriguez
	](https://a16z.com/prediction-markets-they-grow-up-so-fast/)
- [**We Can (and Do) Solve Crime**
	David Ulevitch and Alex Immerman
	](https://a16z.com/we-can-and-are-solving-crime/)

## Creating for agents, not humans

**Stephenie Zhang**

In 2026, people will start interfacing with the web through their agents. And what mattered for human consumption won’t matter the same way for agent consumption.

For years, we’ve optimized for predictable human behavior: rank high on Google, appear among the first few items on Amazon, lead with a TL;DR. When I took a journalism class in high school, we were taught the 5Ws + H for news, and to start with a hook for features. Maybe a human would miss the deeply relevant, insightful statement buried on page five, but the agent won’t.

This shift is about software, too. Apps were designed for human eyes and clicks, and optimization meant good UI and intuitive flows. As agents take over retrieval and interpretation, visual design becomes less central to comprehension. Instead of engineers staring at Grafana dashboards, AI SREs can interpret telemetry and post insights in Slack. Instead of sales teams combing through CRMs, agents can surface patterns and summaries automatically.

We’re no longer designing for humans, but for agents. The new optimization isn’t for visual hierarchy, but for machine legibility—and that will change the way we create and the tools we use to do it.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Stephanie-Zhang-1024x1024.png)

#### Stephenie Zhang

is a partner on the Growth investing team, focused on enterprise technology companies.

- [**Defense in Depth, Rebuilt for Machine Speed**
	Asaf Ezra and Stephenie Zhang
	](https://a16z.com/defense-in-depth-rebuilt-for-machine-speed/)
- [**The Exploit Was the Bottleneck**
	Asaf Ezra and Stephenie Zhang
	](https://a16z.com/the-exploit-was-the-bottleneck/)
- [**The New Security Agenda**
	Stephenie Zhang and Owen Colby
	](https://a16z.com/the-new-security-agenda/)
- [**Investing in Armadin**
	David George and Stephenie Zhang
	](https://a16z.com/announcement/investing-in-armadin/)
- [**Investing in Gimlet**
	Raghu Raghuram, Sarah Wang, Shangda Xu, and Stephenie Zhang
	](https://a16z.com/announcement/investing-in-gimlet/)

## The end of the screen time KPI in AI applications

**Santiago Rodriguez**

For the last 15 years, screen time has been the best indicator of value delivery in both consumer and business applications. We’ve been living in a paradigm focused on hours of Netflix streaming, mouse clicks in a healthcare EHR UX (to demonstrate meaningful use), or even time spent on chatGPT as the key performance indicator. As we move to a future based on outcome-based pricing that perfectly aligns incentives between vendors and users, we’ll first move away from screen time reporting.

We’re already seeing this in practice. When I run DeepResearch queries on ChatGPT, I capture an enormous amount of value despite almost no screen time. When Abridge magically captures the patient-provider conversation and automates downstream activities, the doctor barely looks at the screen. When Cursor develops entire applications end-to-end, the engineer is planning the next feature development cycle. And when Hebbia drafts a pitch deck from hundreds of public filings, the investment banker is getting well deserved sleep.

This presents a unique challenge: how much an application can charge per user requires a more complex method of measuring ROI. Doctor satisfaction, developer productivity, financial analyst wellbeing and consumer happiness all increase with AI applications. The companies that tell the simplest sales pitch on ROI will continue to outpace their competitors.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Santiago-Rodriguez-1.png)

#### Santiago Rodriguez

is a partner on the Growth investing team, focused on fintech, consumer, and crypto technology companies.

- [**The $1 Trillion AI Buildout | State of Markets**
	David George, Sarah Wang, Alex Immerman, and Santiago Rodriguez
	](https://a16z.com/podcast/the-1-trillion-ai-buildout-state-of-markets/)
- [**Who Gets Paid When AI Does the Shopping?**
	Alex Immerman and Santiago Rodriguez
	](https://a16z.com/who-gets-paid-when-ai-does-the-shopping/)
- [**Prediction Markets: They Grow Up So Fast**
	Alex Immerman and Santiago Rodriguez
	](https://a16z.com/prediction-markets-they-grow-up-so-fast/)
- [**The Algorithm That Keeps Compounding**
	Alex Immerman and Santiago Rodriguez
	](https://a16z.com/the-algorithm-that-keeps-compounding/)
- [**Good news: AI Will Eat Application Software**
	Alex Immerman and Santiago Rodriguez
	](https://a16z.com/good-news-ai-will-eat-application-software/)

## Bio + Health

## Healthy MAUs

**Julie Yoo**

In 2026, a new healthcare customer segment will take center stage: the “healthy MAUs.”

The traditional healthcare system has primarily served three main user segments: (a) “sick MAUs”: people with spiky, high-cost needs; (b) “sick DAUs\*”: like those in intensive, long-term care; and (c) “healthy YAUs\*”: relatively healthy individuals who rarely see a doctor. Healthy YAUs are at risk of becoming Sick MAUs/DAUs, and preventive care could slow that shift. But our reaction-pilled healthcare reimbursement system rewards treatment over prevention, so access to proactive check-ins and monitoring services are not prioritized, and insurance rarely covers them anyway.

Enter Healthy MAUs: consumers who aren’t actively sick but want to monitor and understand their health on a recurring basis—and also represent the potentially largest portion of the consumer population. We expect a wave of companies—both AI-native upstarts, and repackaged versions of incumbents—to start offering recurring services to serve this user base.

With AI’s potential to reduce the cost structure of care delivery, the advent of novel health insurance products focused on prevention, and consumers more comfortable paying for subscription-based models out of pocket, “healthy MAUs” represent the next high-potential customer segment for healthtech: continuously engaged, data-informed, and prevention oriented.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Julie-Yoo-2-1024x1024.png)

#### Julie Yoo

is a general partner on the Bio + Health team, where she leads investments into companies that are transforming how we access, pay for, and experience healthcare.

- [**Employers Are Shopping for a New Health Plan**
	Julie Yoo
	](https://a16z.com/the-great-health-plan-replacement/)
- [**Your AI Doctor Is Coming | Julie Yoo**
	Julie Yoo and Sophia Dew
	](https://a16z.com/podcast/your-ai-doctor-is-coming-julie-yoo/)
- [**Healthcare Will Benefit Most from AI | Julie Yoo on StartUp Health**
	Julie Yoo and Unity Stoakes
	](https://a16z.com/podcast/healthcare-will-benefit-most-from-ai-julie-yoo-on-startup-health/)
- [**Deploying AI in Healthcare**
	Julie Yoo and Nikhil Buduma
	](https://a16z.com/podcast/deploying-ai-in-healthcare/)
- [**Infinite Healthcare: What’s It Worth?**
	Jay Rughani, Jane Rhee, and Julie Yoo
	](https://a16z.com/infinite-healthcare-whats-it-worth/)

## speedrun

## World models take the spotlight in storytelling

**Jonathan Lai**

In 2026, AI-powered world models will revolutionize storytelling through interactive virtual worlds and digital economies. Technologies like Marble (World Labs) and Genie 3 (DeepMind) already generate full 3D environments from text prompts, allowing users to explore them as if in a game. As creators adopt these tools, entirely new storytelling formats will emerge, potentially culminating in a “generative Minecraft,” where players co-create vast, evolving universes. These worlds could blend game mechanics with natural language programming, such as commanding, “create a paintbrush that changes the color of anything I touch to pink.”

Such models will blur the boundary between player and creator, transforming users into co-authors of dynamic shared realities. This evolution could spawn interconnected generative multiverses, where diverse genres like fantasy, horror, adventure can exist side by side. Within them, digital economies will flourish as creators earn income crafting assets, guiding newcomers, or developing new interactive tools. Beyond entertainment, these generative worlds will serve as rich simulation environments for training AI agents, robots, and perhaps even AGI. The rise of world models thus signals not just a new genre of play, but an entirely new creative medium and economic frontier.

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Jon-Lai-1.png)

#### Jonathan Lai

is a general partner at Andreessen Horowitz, where he oversees speedrun and its investing motion. He backs founders at the earliest stage, with a focus on AI-native products, developer tools, and new consumer formats.

- [**Gaming’s Next Origin Stories**
	Elena Burger, Anish Acharya, and Jonathan Lai
	](https://a16z.com/gamings-next-origin-stories/)
- [**Marc Andreessen on Startup Timing**
	Marc Andreessen and Jonathan Lai
	](https://a16z.com/podcast/marc-andreessen-on-startup-timing/)
- [**Investing in Hedra**
	Justine Moore, Troy Kirwin, Jonathan Lai, and Matt Bornstein
	](https://a16z.com/announcement/investing-in-hedra/)
- [**AI Learned to Talk. Now it’s Learning to Build Reality**
	Colin Campbell and Jonathan Lai
	](https://a16z.com/ai-is-learning-to-build-reality/)
- [**Anime Is Eating The World**
	Robin Guo and Jonathan Lai
	](https://a16z.com/anime-is-eating-the-world/)

## “The year of me”

**Joshua Lu**

2026 will become “the year of me”: the moment when products stop being mass-produced and start being *made for you.*

We’re seeing it everywhere already.

In education, startups like Alphaschool are building AI tutors that adapt to each student’s pace and curiosity, giving every kid an education that matches their pace and preferred method of learning. This level of attention previously would not be possible without tens of thousands of tutoring dollars spent per student.

In health, AI is designing daily supplement stacks, workout plans, and meal routines tailored to your biology. No need for a trainer or a lab.

Even in media, AI lets creators remix news, shows, and stories into personalized feeds that match your exact interests and tone.

The biggest companies of the last century won by finding *the average consumer.
*The biggest companies of the next century will win by finding *the individual inside the average.*

2026 is the year the world stops optimizing for everyone and starts optimizing for *you.*

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2023/04/Josh-Lu-1.png)

#### Joshua Lu

is an Investment Partner at Andreessen Horowitz for speedrun.

- [**Applications for speedrun SR008 are now open**
	Samira Behrouzan, Joshua Lu, and Rose Johnson
	](https://a16z.com/applications-for-a16z-speedrun-sr008-are-now-open/)
- [**Applications for a16z speedrun SR007 are now closed.**
	Samira Behrouzan and Joshua Lu
	](https://a16z.com/applications-for-a16z-speedrun-sr007-are-now-open/)
- [**Drop EVERYTHING — speedrun SF applications are live ![👀](https://s.w.org/images/core/emoji/17.0.2/svg/1f440.svg)**
	Samira Behrouzan and Joshua Lu
	](https://a16z.com/a16z-speedrun-application-winter-spring-2026/)
- [**Applications for SR005 are officially open**
	Samira Behrouzan and Joshua Lu
	](https://a16z.com/applications-for-sr005-are-officially-open/)
- [**Meet the new a16z speedrun!**
	Samira Behrouzan and Joshua Lu
	](https://a16z.com/meet-the-new-a16z-speedrun/)

## The first AI-native university

**Emily Bennett**

In 2026, I expect we’ll see the birth of the first AI-native university, an institution built from the ground up around intelligent systems.

Over the past several years, universities have dabbled in AI-enabled grading, tutoring, and scheduling. But what’s emerging now is deeper, an adaptive academic organism that learns and optimizes itself in real time.

Picture an institution where courses, advising, research collaboration, and even building operations continuously adapt based on data feedback loops. Schedules optimize themselves. Reading lists evolve nightly and rewrite themselves as new research appears. Learning paths shift in real time to meet each student’s pace and context.

We’re already seeing precursors. ASU’s campus-wide partnership with OpenAI produced hundreds of AI-driven projects across teaching and administration. SUNY now embeds AI literacy into its general education requirements. These are the building blocks for more foundational deployment.

In the AI-native university, professors become **architects of learning**, curating data, tuning models, and teaching students how to interrogate machine reasoning

Assessment shifts, too. Detection tools and plagiarism bans give way to AI-aware evaluation, grading students on *how* they use AI, not whether they used it. Transparency and tactful application replaces prohibition.

And as every industry struggles to hire people who can design, govern, and collaborate with AI systems, this new university becomes the training ground, producing graduates fluent in orchestration who help augment a rapidly shifting workforce.

This AI-native university will become the talent engine for a new economy.

*Stay tuned for part 2 tomorrow.*

About the Contributor

![](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/09/Emily_Bennett.png)

#### Emily Bennett

is an investing partner for a16z speedrun.

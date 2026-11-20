Scraping: https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-one-year-milestone/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-one-year-milestone/
  Consent dismissed via: text-match:accept
  Settled (dom-quiet, 2497ms)
  Extracting content...
  Extracted 16050 characters

--- Content ---

A year ago, we launched [AWS Transform](/transform/) with one mission: modernize the world’s infrastructure and applications.

12 months in, here’s what 4.5+ billion lines of code processed, hundreds of thousands of servers migrated, and saving customers 1.6+ million hours taught us about migration, modernization, and why this work cannot wait.

## Why this matters more than ever

![](https://d2908q01vomqb2.cloudfront.net/1f1362ea41d1bc65be321c0a378a20159f9a26d0/2026/05/15/ATX-Anniversary-Blog-Hero-Image-3.png) Enterprises still run a significant portion of their infrastructure on-premises. A huge chunk of the world’s software is 20+ years old. It still runs payroll. It still runs claims. It still runs the systems your business depends on every day. And now leadership wants agentic AI on top of it. You can’t run agentic AI workloads on a mainframe that hasn’t been touched in 15 years. You can’t drop AI agents into a.NET Framework app stitched together by retired engineers. The modernization you keep deferring is now the thing standing between you and the AI strategy your CEO announced last quarter.

Meanwhile, the debt is compounding. Technical debt costs an estimated $1.52 trillion per year in the U.S. alone, and AI coding agents are making the pile bigger, not smaller. They generate code that ships today but won’t follow tomorrow’s standards. The signal from enterprise leaders has shifted from “should modernize” to “must modernize.” But modernization is technically hard, carries business complexity, and critically, it never ends. Today’s modernization is tomorrow’s legacy, and that’s why it can’t be a project—it has to be a continuous process.

This is why we built AWS Transform.

## What customers actually asked for

Not architectures. Not frameworks. Not another tool.

They asked for outcomes: Speed. Accuracy. Continuity. They wanted to finish what stalled. Some of their projects had been sitting untouched for years. At AWS, we spent two decades helping customers with hundreds of thousands of projects and built migration tools ourselves. We knew what worked, what is needed to scale, and where the gaps were.

That’s how AWS Transform was born, a year ago. We packaged all our learnings into dozens of expert AI agents, connected by agentic workflows. These agents use goal-driven orchestration to run end-to-end automation. Discovery, planning, transformation, and testing are all interconnected. Seamless handoffs between collaborators. No context lost between stages. Two decades of migration expertise, delivered as an AI-assisted service that improves with every iteration.

We started this journey by launching three use cases (VMware infrastructure migration, IBM z/OS COBOL application modernization, and.NET upgrades) because those were the workloads blocking customers from running modern and now agentic workloads. At re:Invent 2025, we added the ability to define your own custom transforms for any code, language, API, or framework upgrade to reduce technical debt at scale.

## What happened in 12 months

Through AWS Transform, we processed over 4.5 billion lines of code and migrated hundreds of thousands of VMs.

The speed differences are not subtle. Customers are completing full transformation and testing of 250,000-line mainframe applications in six weeks. The same work used to take years. Infrastructure teams are now planning migrations of thousands of servers in hours instead of weeks. These assessments consistently uncover an average of 35% in compute and 45% in licensing savings by moving to AWS, and and customers reduce costs by 60% by moving to the cloud. Windows and.NET modernization is delivering 40% reductions in licensing costs and 4x acceleration in project timelines.

The customer roster behind those numbers tells the bigger story. CSL planned migrations for thousands of servers in days, a 10x acceleration over prior approaches. ADP modernized a complex mainframe using Transform’s mainframe and custom capabilities, along with Kiro to complete building new code. They’re now scaling for 1.1 million clients with results in weeks, not years. Signaturit Group cut its Windows.NET to Linux migration from six to eight months down to a few days. Air Canada upgraded Node.js runtimes in days at a 90% efficacy rate and 80% cost reduction, then made Transform their internal standard. And across thousands of customers, we’ve already saved 810 developer years of effort, investing into innovation for the future instead of fixing tech debt from the past.

But the strongest signal is not in any single metric. It’s that 4 out of 5 customers come back and do more projects. Roughly half now use multiple transformation capabilities. Customers don’t return to tools unless they see value.

Partners and ISVs create a compounding effect. More than three dozen partner organizations are building solutions and delivery practices on top of Transform. ISVs are integrating with Transform to expand as well. Wavicle published BI modernization transforms through AWS Marketplace. AWS field engineers contribute transforms for patterns they encounter with customers. Just last week a field member expanded infra assessments to support needs of regulated customers.

## Four things we learned and how that evolved our roadmap

![](https://d2908q01vomqb2.cloudfront.net/1f1362ea41d1bc65be321c0a378a20159f9a26d0/2026/05/15/ATX-Anniversary-Blog-Hero-Image-2.png) After working with thousands of customers and dozens of partners this year, four key insights have shaped our approach and roadmap:

**1\. Meet users where they work.** We started with a purpose-built web app for program managers and architects. But architects live in dashboards. Developers and platform engineers live in IDEs and CLIs. Partners live in their own delivery environments. Everyone wants to pick up where someone else left off. Our answer continues our commitment to choice: meet the user where they are.

Today we are providing unbundled access to our agents, via an MCP server. That MCP server powers new access surfaces, including a Kiro power and agent plugins for Claude Code, Cursor, Codex, and more. Customers and partners can even more easily integrate these into their existing workflows, or bring their agents to construct new workflows. The CLI enables repeatable code modernization patterns. Every surface shares the same context, no re-entry, no lost progress.

**2\. Federated development with guardrails.** Our team builds every transform with customer feedback baked in. Then we ship it to thousands of practitioners, and they take it places we never planned for. AWS field teams work with customers and solve problems on the fly. Partners bring in unique perspectives. AI has lowered the bar for teams to innovate. A federated model compounds faster than a closed one. But it’s not easy to harness this power, while still delivering with quality and operational consistency. That’s why we built Transform with composability into our design from day 1, so customers, partners, ISVs, and our own field teams can personalize and add their own special sauce.

Today we are introducing an agent builder toolkit as a Kiro power that makes it even easier to build agents in AgentCore and bring them into Transform. With this composability offering you can build custom agents, and mix and match them with the capabilities within AWS Transform.

**3\. Enterprise modernization is multi-player.** Modernizing an enterprise portfolio is not single-developer work. Architects define the target state. Developers execute. Leads review and approve. Partners deliver at scale. The bottleneck is orchestration, governance, and the ability to collaborate across teams inside the company’s own security boundary. That’s why we built Transform as a collaborative enterprise foundation first: full traceability from source to target, consistency that doesn’t depend on which user runs it, connectors into existing IT systems.

And today we are adding a new S3 connector, expanding authorization to support IAM Roles, and expanding the human-in-the-loop interaction to span multiple surfaces. Users can look at job summaries across the team, with easy reminders on next steps, from any surface.

**4\. Listen, build, ship, repeat.** As customers started using Transform for early use cases, we learned about new capabilities they needed. When doing migrations, they didn’t just want to move servers; they wanted to modernize along the way. With mainframes, customers wanted additional languages and better integration with their coding agents to generate new code. When modernizing Windows workloads, experts wanted more control over how they run transformations and edit plans. And customers wanted to remediate other types of tech debt beyond what we initially shipped for. Across the board, as customers tackle more complex migrations, they wanted more control to iterate and the option to use deterministic approaches when precision and repeatability were needed.

Today, we are introducing capabilities across all our use cases that deepen what customers can do with Transform. For migrations, customers can now modernize during migration, such as containerizing VMs and reimagining networks. For mainframe modernization, we are expanding to PL/I and providing integrations with coding agents like Kiro and Claude. To provide more interactivity, we enhanced our Windows modernization capability with the ability to combine expert guidance with autonomous transformations. And we added dozens of new custom transforms that allow you to remediate tech debt at scale, across the org.

## Deeper look: how each use case is evolving

**On infrastructure migration**, we continue to enhance planning and execution. Upload your inventory in any format, add business context, explore what-if scenarios, and land on an optimized TCO in minutes. Then plan migration waves in hours—across thousands of servers—accounting for both technical and business constraints. We learned that moving networks and security settings often derails projects. We provide the ability to migrate on-premises networks to AWS equivalents, and now we’re expanding to reimagine your networks—optimizing VPCs, right-sizing CIDRs, tightening security groups, and fixing naming so your network is migration-ready without weeks of manual review. To simplify provisioning secure target environments, we now automatically create landing zones and integrate with AWS Control Tower. And, we’ve expanded beyond VMware to support Hyper-V, bare metal, and cloud-based servers. For customers that want to modernize, you can containerize apps and move to ECS or EKS. We’ve also made it easier to use MGN—our classic migration tool—from Transform for a project-oriented approach. Post-migration, you can automate configuration, validation, and compliance enforcement—turning cutover from a multi-day manual runbook into a deterministic, repeatable event. And you can migrate to any commercial AWS region and GovCloud, spanning multiple target accounts. And every step is integrated, with shared context from discovery through deployment and post-migration validation.

**On mainframe app modernization**, we kept pushing performance across the entire pipeline. Fact-producing agents analyze code, runtime behavior, business rules, and data lineage to build a detailed execution graph, extract the intent of legacy code as business rules, and map every function in the transformed code back to those original rules—closing projects in weeks that historically stalled for months or years. Our combination of deterministic analysis and AI-driven generation delivers the most accurate and broadest outcome we’ve benchmarked. We started with IBM COBOL, VSAM, IMS, and DB2, and have now expanded to PL/I —a language common in financial services, insurance, and the public sector, and historically harder to modernize due to pointer arithmetic and dynamic storage allocation. Using the same reimagine pattern, Transform extracts PL/I business logic into a syntax-independent specification, then Kiro takes over interactively: developers steer forward engineering conversationally—reviewing generated service specs, refining architecture decisions, and iterating on code and infrastructure in real time until the modernized application is deployed on cloud-native, event-driven patterns.

**On Windows app modernization**, we’re going beyond.NET upgrades. Enterprise Windows environments aren’t just code—they’re code, databases, and application dependencies tangled together. Transform handles this autonomously: assess complexity, sequence work into waves, and execute transformations end-to-end. But we have also seen complex projects where architects want to steer decisions—adjusting transformation plans, overriding specific choices, and finishing that most complex piece of change—they can now step in at any point without breaking the autonomous flow, then step back out. We’ve also been expanding full-stack modernization capabilities—UI modernization from ASP.NET web forms to Blazor and migration from SQL Server to Aurora PostgreSQL. Our expanded database modernization capability, now in beta, converts every object in the stack together: schemas, stored procedures, and application data-access code. Getting started is easy. Use virtual sources so you don’t have to wait for direct access to production databases. The workflow is iterative: get an assessment with level of effort, DBAs review and approve, Transform executes. Three layers of validation confirm correctness—syntax validation, semantic equivalence, and functional verification with synthetic data—before any production data moves.

**On code modernization**, we’re expanding toward our vision of eliminating tech debt at enterprise scale. Tech debt is accelerating—frameworks aging out, SDKs going EOL, dependencies piling up—and with agents creating new code faster than ever, customers need to move faster than one-off projects allow. They’ve been using our existing Java, Python, Node.js, and SDK upgrades, and customer demand has pulled us into dozens of new patterns. We’re now shipping out-of-the-box transforms for Vue.js upgrades, Scala/Glue upgrades, Spring Boot updates, Log4j to SLF4J, Angular to React, Angular to Flutter, Progress 4GL to Java, PHP replatforming, ColdFusion to React/Java, DataDog to CloudWatch Monitors, JBoss to Spring Boot—all applicable across entire orgs and repos without depending on the craft of individual experts. And now, we’re introducing three new code assessment capabilities. Tech debt assessments help customers prioritize. Simply point to your code repos and get a full portfolio-level analysis in minutes—framework vulnerabilities, end-of-life dependencies, with criticality to fix. Agentic Readiness assessments tell you how agent-ready your applications actually are, by checking for documentation, pipeline and test completeness. Modernization Assessments understand the steps to cloud-native maturity, and help identify pathways to AWS best practices. To power these new features, we re-architected the underlying agents, delivering up to 2x the performance.

## The road ahead

The mission is to modernize the world’s legacy software and infrastructure—continuously. One workload pulls in the next: a customer migrates VMs, discovers Windows apps that need transformation, modernizes those, then realizes the codebase has accumulated framework debt. The cycle never ends, and the service that keeps pace is the one that never stops learning.

By the end of 2026, our goal is simple: every enterprise that wants to become agentic should be able to use Transform to get their infrastructure and portfolio ready—continuously, without dedicated programs or multi-year roadmaps.

Modernization becomes a background process, not a project. You begin with one workload. The service carries the context forward. What you modernize next is up to you.

*PS: 4 out of 5 customers are already expanding. We’d like you to be the next one.*

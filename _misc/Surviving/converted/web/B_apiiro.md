Scraping: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
  Settled (dom-quiet, 4567ms)
  Extracting content...
  Extracted 8637 characters

--- Content ---

Every CEO Is Mandating AI Coding. Few Realize They’re Mandating Risk Too. Here’s the Data to Prove It.

**When Coinbase CEO Brian Armstrong** [ordered every engineer to adopt AI coding assistants](https://fortune.com/2025/08/25/coinbase-ceo-brian-armstrong-ai-coding-assistants-mandate-tech/) (**and fired those who didn’t**) he captured the new reality: AI adoption is no longer optional. He’s not alone. Lemonade’s CEO Daniel Schreiber has told employees “AI is mandatory.” Citi bank rolled out agentic AI to its 40,000 developers.

Across industries, from fintech to insurance to Wall Street, the message from the top is the same: AI isn’t a choice. It’s a directive.

But even Armstrong admits the risks are uncharted. As Stripe’s John Collison quipped on his podcast: “It’s clear that it is very helpful to have AI helping you write code. It’s not clear how you run an AI-coded codebase.” Armstrong’s reply: “I agree. We’re still figuring that out.”

And his intuition is spot on. Apiiro’s new research inside Fortune 50 enterprises shows the same AI tools driving 4× speed are also generating 10× more security risks. Pull requests are ballooning, vulnerabilities are multiplying, and shallow syntax errors are being replaced with costly architectural flaws.

The message for CEOs and boards is blunt: if you’re mandating AI coding, you must mandate AI AppSec in parallel. Otherwise, you’re scaling risk at the same pace you’re scaling productivity.

**Methodology**

Apiiro, the leading Agentic Application Security platform, used its patented Deep Code Analysis (DCA) engine to analyze code from tens of thousands of code repositories and several thousand developers across Fortune 50 enterprises, and a variety of coding assistants. The results offer one of the first real-world looks at how AI coding assistants are reshaping software risk.

**1\. AI Coding Assistants Generate More Commits, Fewer PRs — and Break the Review Process**

AI-assisted developers produced **3 – 4× more commits** than their non-AI peers. But those commits didn’t land as small, incremental merges. They were packaged into **fewer PRs overall – each one significantly larger in scope, touching more files and services per change.**

That packaging is the problem. Bigger, multi-touch PRs slow review, dilute reviewer attention, and raise the odds that a subtle break slips through. In one case, a single AI-driven PR **changed an authorization header across multiple services**. One downstream service wasn’t updated. Result: a silent auth failure that could expose internal endpoints.

**Bottom line:** AI accelerates code creation; it also **concentrates change**, overloading code review and expanding blast radius per merge.

![](https://apiiro.com/_b44/api/apps/6991bfdc25eeb87584b7bd76/files/mp/public/6991bfdc25eeb87584b7bd76/bae054e3b_unnamed-19-1024x749.jpg)

**2\. 4× Faster, 10× Riskier: AI Writes More Code – And More Flaws**

AI-assisted teams didn’t just ship faster – they shipped **10× more security findings**. And while findings soared, PR volume actually **fell by nearly a third**. That means more emergency hotfixes, more incident response, and a higher probability that issues slip into production before review catches them.

**Why this happens:** the same dynamic from Section 1 (fewer, **much larger PRs**) compounds risk. Big, multi-touch PRs tend to introduce **multiple issues at once**, so every merge carries more potential blast radius. The faster AI accelerates output, the faster unreviewed risk accumulates.

![](https://apiiro.com/_b44/api/apps/6991bfdc25eeb87584b7bd76/files/mp/public/6991bfdc25eeb87584b7bd76/3e2a712bb_image-2-1024x601.png)

**3\. 10,000+ AI-Induced Security Flaws in a Single Month**

By June 2025, AI-generated code was introducing **over 10,000 new security findings per month** across the repositories in our study — a **10× spike in just six months** compared to December 2024. And the curve isn’t flattening; it’s accelerating.

These flaws span **every category of application risk** — from open-source dependencies to insecure coding patterns, exposed secrets, and cloud misconfigurations. AI is multiplying not one kind of vulnerability, but all of them at once.

For security teams, that means a shift from managing issues to drowning in them.

![](https://apiiro.com/_b44/api/apps/6991bfdc25eeb87584b7bd76/files/mp/public/6991bfdc25eeb87584b7bd76/41c48c319_image-3-1024x611.png)

**4\. From Typos to Timebombs: AI Swaps Syntax Errors for Architectural Flaws**

AI assistants are good at catching the small stuff. Our analysis shows trivial syntax errors in AI-written code dropped by **76%**, and logic bugs fell by more than **60%**.

But the tradeoff is dangerous: those shallow gains are offset by a surge in deep architectural flaws. **Privilege escalation paths jumped 322%, and architectural design flaws spiked 153%.** These are the kinds of issues scanners miss and reviewers struggle to spot – broken auth flows, insecure designs, systemic weaknesses.

In other words, AI is fixing the typos but creating the timebombs. That makes reviews and automated scans less effective, and raises the stakes for context-aware analysis at design and code time.

![](https://apiiro.com/_b44/api/apps/6991bfdc25eeb87584b7bd76/files/mp/public/6991bfdc25eeb87584b7bd76/be170aaf1_image-1024x650.png)

**5\. AI-Generated Code Leaks Cloud Credentials**

Our analysis found that **AI-assisted developers exposed Azure Service Principals and Storage Access Keys nearly twice as often** as their non-AI peers. Unlike a bug that can be caught in testing, a leaked key is live access: an immediate path into production cloud infrastructure.

Because assistants generate large, multi-file changes, a single credential can be propagated across multiple services or configs before anyone notices. One mistake can lead to a systemic exposure.

![](https://apiiro.com/_b44/api/apps/6991bfdc25eeb87584b7bd76/files/mp/public/6991bfdc25eeb87584b7bd76/1e7b19294_image-1-1024x643.png)

**Implications: AI coding assistants without AI AppSec is a breach waiting to happen**

AI coding assistants are no longer optional. CEOs are mandating them, boards are asking about productivity gains, and developers are adopting them at scale. But our research makes the tradeoff clear: accelerated output comes with accelerated risk.

- Bigger PRs break the review process: complexity scales faster than human oversight.
- 10× more vulnerabilities enter the pipeline, exposing enterprises to incidents before review can catch them.
- These risks run deeper, like structural design gaps and leaked credentials, and they are missed by automated scans and surface checks.

The bottom line: adopting AI coding assistants without adopting an AI AppSec Agent in parallel is a false economy. You get the productivity, but you also get the risk, multiplied.

**Apiiro: When You Add an AI Coding Assistant, Add an AI AppSec Agent in Parallel**

The numbers are blunt: AI coding assistants multiply speed, and multiply risk. CEOs are mandating adoption, but even Coinbase’s Brian Armstrong admitted he doesn’t know how to “run an AI-coded codebase.” That’s why the missing piece is just as urgent as the assistants themselves: an AI AppSec Agent to govern and fix what they generate.

With **Apiiro’s AI AppSec Agent**, every change is analyzed in the context of your codebase, runtime, and policies. Powered by [Apiiro’s patented Deep Code Analysis (DCA)](https://apiiro.com/product/deep-code-analysis-dca-apiiro/), the agent understands your software architecture from code to runtime — giving AutoFix, AutoGovern, and AutoManage the context generic tools lack.

- AutoFix → Automatically fix SAST, SCA, secrets, API vulnerabilities, and design flaws, with fixes tailored to your software architecture and organization policy.
- AutoGovern → Enforces your org’s policies and secure coding guardrails in real time, blocking unsafe changes before they ship.
- AutoManage → Tracks the full lifecycle of every risk – risk acceptance workflows, SLA, MTTR and compliance evidence.

For leaders, that means confidence that AI-generated code is governed against your standards before it ships. For practitioners, it means fewer false positives, smaller backlogs, and fixes that actually stick. The result: you scale developer productivity without scaling security risk.

Trusted by **hundreds of global enterprises**, including Shell, USAA, BlackRock, Bloomberg, and Equinix, Apiiro is the Agentic Application Security platform built for the AI era.

[See a demo of Apiiro’s AutoFix Agent today](https://apiiro.com/schedule-a-demo/)**.**

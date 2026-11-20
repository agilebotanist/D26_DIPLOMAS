Scraping: https://www.aikido.dev/blog/owasp-top-10-agentic-applications
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.aikido.dev/blog/owasp-top-10-agentic-applications
  Settled (dom-quiet, 1349ms)
  Extracting content...
  Extracted 10800 characters

--- Content ---

Agentic AI is moving into production in CI/CD pipelines, internal copilots, customer support workflows, and infrastructure automation. These systems no longer just call a model. They plan, decide, delegate, and take actions on behalf of users and other systems. This creates new attack surfaces that do not map cleanly to traditional application security or even the OWASP Top 10 2025. To address this, OWASP published the [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), a focused list of the highest impact risks in autonomous, tool using, multi agent systems.

For teams that already use the [OWASP Top 10 2025](https://www.aikido.dev/blog/owasp-top-10-2025-changes-for-developers) as a guide for web and software supply chain security, the Agentic Top 10 extends the same mindset to AI agents, tools, orchestration, and autonomy.

## Why a Separate OWASP Top 10 for Agentic Systems

The [original OWASP Top 10](https://www.aikido.dev/blog/what-is-owasp-top-10) focuses on risks such as access control failures, injection, and misconfigurations. The 2025 update expanded into modern supply chain risks like malicious dependencies and compromised build pipelines.

Agentic applications introduce additional properties that fundamentally change how risk propagates:

- Agents operate with autonomy across many steps and systems
- Natural language becomes an input surface that can carry actionable instructions
- Tooling, plugins, and other agents are composed dynamically at runtime
- State and memory are reused across sessions, roles, and tenants
	In response, OWASP introduces the concept of least agency in the 2026 list. The principle is simple. Only grant agents the minimum autonomy required to perform safe, bounded tasks.

## The OWASP Top 10 for Agentic Applications (2026)

Below is a practical summary of each category, based on the OWASP document, written for developers and security teams.

### ASI01 – Agent Goal Hijack

Agent Goal Hijack occurs when an attacker alters an agent’s objectives or decision path through malicious text content. Agents often cannot reliably separate instructions from data. They may pursue unintended actions when processing poisoned emails, PDFs, meeting invites, RAG documents, or web content.

Examples include indirect prompt injection that causes exfiltration of internal data, malicious documents retrieved by a planning agent, or calendar invites that influence scheduling or prioritization.

Mitigation focuses on treating natural language input as untrusted, applying prompt injection filtering, limiting tool privileges, and requiring human approval for goal changes or high impact actions.

### ASI02 – Tool Misuse and Exploitation

Tool Misuse occurs when an agent uses legitimate tools in unsafe ways. Ambiguous prompts, misalignment, or manipulated input can cause agents to call tools with destructive parameters or chain tools together in unexpected sequences that lead to data loss or exfiltration.

Examples include over privileged tools that can write to production systems, poisoned tool descriptors in MCP servers, or shell tools that run unvalidated commands.

Aikido’s [PromptPwnd research](https://www.aikido.dev/blog/promptpwnd-github-actions-ai-agents) is a real example of this pattern. Untrusted GitHub issue or pull request content was injected into prompts in certain GitHub Actions and GitLab workflows. When paired with powerful tools and tokens, this resulted in secret exposure or repository modifications.

Mitigation includes strict tool permission scoping, sandboxed execution, argument validation, and adding policy controls to every tool invocation.

### ASI03 – Identity and Privilege Abuse

Agents often inherit user or system identities, which can include high privilege credentials, session tokens, and delegated access. Identity and Privilege Abuse occurs when these privileges are unintentionally reused, escalated, or passed across agents.

Examples include caching SSH keys in agent memory, cross agent delegation without scoping, or confused deputy scenarios.

Mitigation includes short lived credentials, task scoped permissions, policy enforced authorization on every action, and isolated identities for agents.

### ASI04 – Agentic Supply Chain Vulnerabilities

Agentic supply chains include tools, plugins, prompt templates, model files, external MCP servers, and even other agents. Many of these components are fetched dynamically at runtime. Any compromised component can alter agent behavior or expose data.

Examples include malicious MCP servers impersonating trusted tools, poisoned prompt templates, or vulnerable third party agents used in orchestrated workflows.
Mitigation includes signed manifests, curated registries, dependency pinning, sandboxing, and kill switches for compromised components.

### ASI05 – Unexpected Code Execution

Unexpected Code Execution occurs when agents generate or run code or commands unsafely. This includes shell commands, scripts, migrations, template evaluation, or deserialization triggered through generated output.

Examples include code assistants running generated patches directly, prompt injection that triggers shell commands, or unsafe deserialization in agent memory systems.

Mitigation involves treating generated code as untrusted, removing direct evaluation, using hardened sandboxes, and requiring previews or review steps before execution.

### ASI06 – Memory and Context Poisoning

Agents rely on memory systems, embeddings, RAG databases, and summaries. Attackers can poison this memory to influence future decisions or behavior.

Examples include RAG poisoning, cross tenant context leakage, and long term drift caused by repeated exposure to adversarial content.

Mitigation includes segmentation of memory, filtering before ingestion, provenance tracking, and expiry of suspicious entries.

### ASI07 – Insecure Inter Agent Communication

Multi agent systems often exchange messages across MCP, A2A channels, RPC endpoints, or shared memory. If communication is not authenticated, encrypted, or semantically validated, attackers can intercept or inject instructions.

Examples include spoofed agent identities, replayed delegation messages, or message tampering on unprotected channels.

Mitigation includes mutual TLS, signed payloads, anti replay protections, and authenticated discovery mechanisms.

### ASI08 – Cascading Failures

A small error in one agent can propagate across planning, execution, memory, and downstream systems. The interconnected nature of agents means failures can compound rapidly.

Examples include a hallucinating planner issuing destructive tasks to multiple agents or poisoned state being propagated through deployment and policy agents.

Mitigation includes isolation boundaries, rate limits, circuit breakers, and pre deployment testing of multi step plans.

### ASI09 – Human Agent Trust Exploitation

Users often over trust agent recommendations or explanations. Attackers or misaligned agents can use this trust to influence decisions or extract sensitive information.

Examples include coding assistants introducing subtle backdoors, financial copilots approving fraudulent transfers, or support agents persuading users to reveal credentials.

Mitigation involves forced confirmations for sensitive actions, immutable logs, clear risk indicators, and avoiding persuasive language in critical workflows.

### ASI10 – Rogue Agents

Rogue Agents are compromised or misaligned agents that act harmfully while appearing legitimate. They may self repeat actions, persist across sessions, or impersonate other agents.

Examples include agents that continue exfiltrating data after a single prompt injection, approval agents that silently approve unsafe actions, or cost optimizers deleting backups.

Mitigation includes strict governance, sandboxing, behavioral monitoring, and kill switches.

## Aikido’s Perspective on Agentic Risk

The OWASP Agentic Top 10 is based on incidents observed in real systems. The OWASP tracker includes confirmed cases of agent mediated data exfiltration, RCE, memory poisoning, and supply chain compromise.

Aikido’s research team has seen similar patterns emerge in CI/CD and supply chain investigations. Notably:

- The [PromptPwnd](https://www.aikido.dev/blog/promptpwnd-github-actions-ai-agents) vulnerability class, discovered by Aikido Security, demonstrated how untrusted GitHub issue, pull request, and commit content can be injected into prompts inside GitHub Actions and GitLab workflows. When combined with over privileged tools, this created practical exploit paths.
- AI enhanced CLI tools and actions showed how untrusted prompt inputs could influence commands executed with sensitive tokens.
- Misconfigurations in open source workflows revealed that developers often grant AI driven automation more access than intended, sometimes including write capable repository tokens.

These findings overlap with ASI01, ASI02, ASI03, ASI04, and ASI05. They highlight that agentic risks in CI/CD and automation are already practical. Aikido continues to publish research as these patterns evolve.

## How Aikido Helps Secure the Surrounding Environment

Aikido’s platform focuses on strengthening the surrounding environment so that any adoption of agentic tools happens on a more secure foundation.

### What Aikido does today

- Identifies insecure or overly permissive GitHub and GitLab workflow configurations such as unsafe triggers or write capable tokens. These issues increase the blast radius of PromptPwnd style attacks.
- Detects leaked tokens, exposed secrets, and excessive privileges in repositories.
- Flags supply chain risks in dependencies, including vulnerable or compromised packages used by tools or supporting code.
- Surfaces misconfigurations in infrastructure as code that could amplify the impact of an agent compromise.
- Provides real time feedback in the IDE to help prevent common misconfigurations during development.

Aikido’s goal is to improve the security posture of the systems that agents operate within, not to claim full agentic vulnerability coverage.

## Scan Your Environment with Aikido

If your engineering team is exploring agentic workflows or already using AI for triage, automation, or code suggestions, strengthening the surrounding environment is an important first step.

Aikido can help identify misconfigurations, excessive permissions, and supply chain weaknesses that directly affect how safe these workflows are.

Start for free with read only scanning, or book a demo to see how Aikido can help reduce the underlying risks that shape your agentic environment.

Share:

https://www.aikido.dev/blog/owasp-top-10-agentic-applications

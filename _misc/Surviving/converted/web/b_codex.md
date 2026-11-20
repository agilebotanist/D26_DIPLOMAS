Scraping: https://developers.openai.com/codex/pricing
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://developers.openai.com/codex/pricing
  Settled (dom-quiet, 2702ms)
  Extracting content...
  Extracted 26323 characters

--- Content ---

**ChatGPT Work and Codex share usage.** ChatGPT Work usage inside ChatGPT uses the same pricing, credits, and usage limits as Codex.

GPT-5.5 retires from Codex with ChatGPT sign-in on October 14, 2026, at noon PDT (19:00 UTC). The OpenAI API and Codex sessions authenticated with an API key aren’t affected. See [GPT-5.5 retirement](about:/docs/models#gpt-55-retirement) for migration guidance.

See [token rates](#token-rates) for credit-based plans and [GPT-6.1 Sol model guidance](about:/docs/models#gpt-61-sol) for model details. API token prices are separate from subscription usage; don’t use them to estimate included tasks.

### Free

Explore Codex capabilities on quick coding tasks.

$0/month

[Get Free](https://chatgpt.com/plans/free/)

- GPT-6 Luna at Standard speed in the desktop app, subject to rollout

### Go

Use Codex for lightweight coding tasks.

$8/month

[Get Go](https://chatgpt.com/plans/go)

- GPT-6 Luna at Standard speed in the desktop app, subject to rollout

### Plus

Power a few focused coding sessions each week.

$20/month

[Get Plus](https://chatgpt.com/explore/plus?utm_internal_source=openai_developers_codex)

- Codex on the web, in the CLI, in the IDE extension, and on iOS
- Cloud-based integrations like automatic code review and Slack integration
- GPT-6.1 Sol and GPT-6 Luna
- Flexibly extend usage with [ChatGPT credits](#credits-overview)
- Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Plus plan

### Pro

Choose the Pro plan that fits your usage.

From

$100/month

[Get Pro](https://chatgpt.com/explore/pro?utm_internal_source=openai_developers_codex)

Everything in Plus and:

- Plans at $100, $200, or $500 USD per month
- [Ultrafast mode](about:/docs/agent-configuration/speed#ultrafast-mode) access on Pro $500
- Other [ChatGPT features](https://chatgpt.com/pricing) as part of the Pro plan

[Compare Pro plans and usage limits.](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-plans)

### API Key

Great for automation in shared environments like CI.

[Learn more](/docs/auth)

- Codex in the CLI, SDK, or IDE extension
- No cloud-based features (GitHub code review, Slack, etc.)
- Model availability follows the API models available to your key
- Pay for Codex usage based on [API pricing](/api/docs/pricing)

## Invite friends and coworkers

Eligible users can send Codex invitations from the profile menu in the lower-left corner of the app. Choose **Invite a friend** on an eligible personal plan or **Invite a coworker** in an eligible Business workspace, enter the recipient’s email address, and send the invitation.

The invitation dialog shows the current reward, recipient requirements, invite limits, and when rewards expire for your plan or promotion. Personal and Business referral programs have separate rewards and eligibility rules. Referrals aren’t currently available for ChatGPT Enterprise.

Business referrals use separate shared-workspace credit rewards; review the [current terms](https://help.openai.com/en/articles/20001271) before you send an invitation.

## Frequently asked questions

### What are the usage limits for my plan?

The number of messages you can send depends on the model used, size and complexity of your tasks, and whether you run them locally or in the cloud. Small scripts or routine functions may consume only a fraction of your allowance, while larger projects, long-running tasks, or extended sessions that require the agent to hold more context will use significantly more per message.

Tasks that look similar can consume different amounts of your allowance. Model choice, context, reasoning, tool use, retrieval, and caching all affect usage, so prompt length alone isn’t a reliable estimate.

For model recommendations, see [Models](/docs/models).

The estimates below show local messages per five-hour period for Plus and Standard Business. Pro plans currently have no five-hour limit. Cloud tasks may use more of your allowance than local messages. Usage depends on the model and task. These estimates are not fixed message limits; check your [usage dashboard](#where-can-i-see-my-current-usage-limits) for current limits and reset times.

<table><thead><tr><th>Model</th><th><p>Plus</p></th><th><p>Standard Business</p></th></tr></thead><tbody><tr><td>GPT-6 Astra</td><td>5-45</td><td>5-45</td></tr><tr><td>GPT-6.1 Sol</td><td>15-160</td><td>15-160</td></tr><tr><td>GPT-6.1 Terra</td><td>35-285</td><td>35-285</td></tr><tr><td>GPT-6 Sol</td><td>15-150</td><td>15-150</td></tr><tr><td>GPT-6 Luna</td><td>350-3,000</td><td>350-3,000</td></tr></tbody><tfoot><tr><td colspan="3"><p>Local messages and cloud chats share your plan’s usage allowance. Weekly limits may also apply.</p></td></tr><tr><td colspan="3"><p>Enterprise/Edu users with flexible pricing have no fixed rate limits. Usage scales with <a href="#credits-overview">credits</a>.</p></td></tr><tr><td colspan="3"><p>Enterprise and Edu plans without flexible pricing have the same per-seat usage limits as Plus for most features.</p></td></tr></tfoot></table>

Usage limits are shared with other agentic features once pricing for those features is effective. This currently includes [ChatGPT for Excel](https://help.openai.com/articles/20001063) on Plus and Pro.

GPT-6.1 Sol usage drawn from your subscription has no long-context surcharge in Codex or ChatGPT Work.

Fast and Ultrafast modes use included subscription limits and paid credits at different rates, relative to Standard mode for the same model:

| Speed mode | Included subscription usage | Purchased credits and Enterprise pay-as-you-go usage |
| --- | --- | --- |
| Fast | 2.5x | 2x |
| GPT-6 Astra Ultrafast | 8x | 6x |
| GPT-6.1 Sol Ultrafast | 8x | 6x |

Check your [usage dashboard](#where-can-i-see-my-current-usage-limits) for current limits and reset times. See [Speed](/docs/agent-configuration/speed) for supported models and how speed modes affect usage.

Image generations use included limits ~3-5x faster on average, depending on image quality and size.

For Ultrafast mode eligibility and administrator controls, see [Ultrafast mode](about:/docs/agent-configuration/speed#ultrafast-mode).

### How much does Sites cost?

[Sites](/docs/sites) is included with eligible ChatGPT plans during public beta. Availability depends on your plan, region, and workspace settings.

### How much does Voice cost?

Voice in Desktop uses your existing Codex usage budget at $0.05 per minute.

GPT-Live manages the live conversation. The model handling your task is billed separately at its applicable token rates. Voice and tasks share your plan’s usage limits.

For Business, Edu, and Enterprise workspaces with credit-based billing, desktop voice costs 1.25 credits per minute. This rate also applies when Plus and Pro users spend additional credits. ChatGPT Voice in Desktop isn’t available via API key.

### What happens when you hit usage limits?

We want you to be able to complete work already in progress. If you reach your usage limits during an active turn, the agent will be able to continue working on that turn, subject to fair use limits.

ChatGPT Plus and Pro users who reach their usage limit can purchase additional credits to continue working without needing to upgrade their existing plan.

Business, Edu, and Enterprise plans with [flexible pricing](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans) can purchase additional workspace credits to continue working.

All users may also run extra local chats using an API key, with usage charged at [standard API rates](https://platform.openai.com/docs/pricing).

### How does image generation count toward usage limits?

Image generation counts toward the same general usage limits as local messages and cloud chats. Image generations use included limits 3-5x faster on average than similar turns without image generation, depending on image quality and size. After you reach your included limits, image generation also draws from [credits](#credits-overview).

Image generation isn’t available on the Free plan. When you use Codex with an API key, API pricing applies to image generation instead of included ChatGPT usage limits.

### Where can I see my current usage limits?

You can find your current limits in the [usage dashboard](https://chatgpt.com/codex/settings/usage). If you want to see your remaining limits during an active Codex CLI session, you can use `/status`.

Check the dashboard every week or two to understand your pace and remaining capacity. If usage is higher than expected, consider whether a smaller model or tighter task scope would still produce a useful result.

### What are tokens and credits?

Tokens are small units of information that ChatGPT reads and writes. Your prompt, files, chat history, tool results, and ChatGPT’s response all use tokens.

Credits are the unit used to pay for eligible usage on credit-based plans. After you reach your included limits, available credits let you continue working. Credit purchase prices and applicable discounts depend on your plan or agreement.

#### Token rates

The rates below are for Standard speed, quoted in credits per million input tokens, cached input tokens, and output tokens. [Learn more about tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them).

Codex credit billing has no separate cache-write charge. API-key usage follows [API pricing](/api/docs/pricing).

GPT-5.6 Sol, Terra, and Luna rates remain unchanged. Credit prices alone don’t determine included subscription usage; check your [usage dashboard](#where-can-i-see-my-current-usage-limits) for current limits.

A small subset of Enterprise customers should continue using the legacy rate card until we migrate you to the new token-based pricing. For more information, [contact OpenAI sales](https://chatgpt.com/contact-sales?utm_internal_source=openai_developers_codex).

<table><thead><tr><th>Credits per 1M tokens</th><th><p>Input Tokens</p></th><th><p>Cached input tokens</p></th><th><p>Output Tokens</p></th></tr></thead><tbody><tr><td>GPT-6 Astra</td><td>250 credits</td><td>25 credits</td><td>1,250 credits</td></tr><tr><td>GPT-6.1 Sol</td><td>50 credits</td><td>2.5 credits</td><td>250 credits</td></tr><tr><td>GPT-6.1 Terra</td><td>25 credits</td><td>1.25 credits</td><td>125 credits</td></tr><tr><td>GPT-6 Sol</td><td>50 credits</td><td>5 credits</td><td>250 credits</td></tr><tr><td>GPT-6 Luna</td><td>2.5 credits</td><td>0.25 credits</td><td>12.5 credits</td></tr><tr><td>GPT-5.6 Sol</td><td>100 credits</td><td>10 credits</td><td>500 credits</td></tr><tr><td>Daybreak Blue</td><td>100 credits</td><td>10 credits</td><td>500 credits</td></tr><tr><td>Daybreak Red</td><td>312.5 credits</td><td>31.25 credits</td><td>1875 credits</td></tr><tr><td>GPT-5.6 Terra</td><td>50 credits</td><td>5 credits</td><td>300 credits</td></tr><tr><td>GPT-5.6 Luna</td><td>5 credits</td><td>0.5 credits</td><td>30 credits</td></tr><tr><td>GPT-Rosalind-Research</td><td>125 credits</td><td>12.5 credits</td><td>625 credits</td></tr><tr><td>GPT-Image-2 (image)</td><td>200 credits</td><td>50 credits</td><td>750 credits</td></tr><tr><td>GPT-Image-2 (text)</td><td>125 credits</td><td>31.25 credits</td><td>250 credits</td></tr></tbody><tfoot><tr><td colspan="4"><p>A typical GPT-5.6 Sol task may use 2-15 credits.</p></td></tr><tr><td colspan="4"><p>These are Standard credit rates. For purchased credits and Enterprise pay-as-you-go usage, Fast mode uses 2x the Standard rate where available, and Ultrafast mode uses 6x. Included subscription usage has different multipliers. See <a href="/docs/agent-configuration/speed">Speed</a> for availability and billing details.</p></td></tr><tr><td colspan="4"><p>Daybreak access requires <a href="about:/docs/cyber-safety#trusted-access-for-cyber">Trusted Access for Cyber</a> approval. Daybreak Blue uses GPT-5.6 Sol credit rates. Daybreak Red requires separate approval and provisioning.</p></td></tr></tfoot></table>

*GPT-5.6 Sol’s promotional pricing is available at least through November 21, 2026.*

[Learn more about credits in ChatGPT Plus and Pro.](https://help.openai.com/en/articles/12642688)

[Learn more about credits in ChatGPT Business, Enterprise, and Edu.](https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans)

For Business and Enterprise/Edu credit billing, use the [credit-based rate card](https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing). If your Enterprise agreement specifies usage-based billing in USD, use the [Enterprise USD rate card](https://help.openai.com/en/articles/20001415-chatgpt-rate-card-enterprise-token-based-pricing) and your agreement instead. Workspace administrators can also review [ChatGPT Work usage and cost](about:/docs/enterprise/chatgpt-work-usage-and-cost#understand-tokens-and-credits).

### What counts as Code Review usage?

Code Review usage applies only when Codex runs reviews through GitHub, for example, when you tag `@Codex` for review in a pull request or enable automatic reviews on your repository. Reviews run locally or outside of GitHub count toward your general usage limits.

### What can I do to make my usage limits last longer?

The local-message counts above are estimates; the token table lists credit rates per million tokens. To make your usage allowance last longer, try these tips:

- **Control the size of your prompts.** Be precise with the instructions you give the agent, but remove unnecessary context.
- **Limit source material.** Provide only relevant files and, when possible, narrow the sources or date range.
- **Match the output to the need.** Define the audience, format, and length, and separate required work from optional improvements.
- **Reduce the size of your AGENTS.md.** If you work on a larger project, you can control how much context you inject through AGENTS.md files by [nesting them within your repository](about:/docs/agent-configuration/agents-md#layer-project-instructions).
- **Limit the number of MCP servers you use.** Every [MCP](/docs/extend/mcp) server adds more context to your messages and uses more of your limit. Disable MCP servers when you don’t need them.

For guidance on choosing and scoping tasks, see [Use Work efficiently](about:/docs/prompting#use-work-efficiently).

## Feature availability

In ChatGPT, GPT-6.1 Sol is available in Work and Codex, not Chat. For Enterprise and Edu, the model is off by default until an administrator enables it. Using it in ChatGPT Work or Codex also requires access to the respective surface. API-key access follows API model availability.

[GPT-6.1 Terra](about:/docs/models?surface=app#app-gpt-61-terra) is available in Work and Codex on Plus, Pro, Business, Enterprise, and Edu plans. It does not support UAE inference residency. It isn’t available in Chat. Access requires the corresponding surface; Enterprise access also depends on workspace availability and administrator controls. Overall Work and Codex plan limits are unchanged.

<table><colgroup><col> <col> <col> <col> <col> <col></colgroup><thead><tr><th>Feature</th><th>ChatGPT Plus</th><th>ChatGPT Pro</th><th>ChatGPT Business</th><th>Enterprise / Education</th><th>API Key</th></tr></thead><tbody><tr><th colspan="6">Access and surfaces</th></tr><tr><th><a href="/docs/cloud">Codex cloud</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/get-started-with-work">ChatGPT Work on the web</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/app">ChatGPT desktop app for local chats</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/codex/cli">Codex CLI</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/codex/ide">IDE extension</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/codex-sdk">Codex SDK, <code>codex exec</code>, and scriptable workflows</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/enterprise/access-tokens">Codex access tokens for trusted automation</a></th><td><span>—</span></td><td><span>—</span></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="https://help.openai.com/articles/20001063">ChatGPT for Excel</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th colspan="6">Models and multimodal</th></tr><tr><th><a href="about:/docs/models#gpt-61-sol">GPT-6.1 Sol</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="about:/docs/models?surface=app#app-gpt-61-terra">GPT-6.1 Terra</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/models">GPT-6 Sol and Luna</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/agent-configuration/speed">Fast mode</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="about:/docs/agent-configuration/speed#ultrafast-mode">Ultrafast (Pro $500 and eligible Enterprise/Edu plans)</a></th><td><span>—</span></td><td></td><td><span>—</span></td><td></td><td></td></tr><tr><th><a href="/docs/image-generation?surface=app">Image generation and editing</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="about:/docs/prompting#use-voice-dictation">Voice dictation</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/features/voice">ChatGPT Voice</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/web-search?surface=app">Web search</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th colspan="6">Local features</th></tr><tr><th><a href="/docs/features/composer-predictions">Composer predictions (beta)</a></th><td><span>—</span></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td></tr><tr><th><a href="about:/docs/prompting#do-a-local-code-review">Local code review with <code>/review</code></a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/sandboxing/auto-review">Auto-review for approval requests</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/permissions">Sandboxing and permission controls</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/automations">Project and standalone scheduled tasks</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/automations">Scheduled tasks</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/environments/git-worktrees">Worktrees and built-in Git tools</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/environments/local-environment">Local environments and repeatable actions</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/appshots">Appshots</a></th><td></td><td></td><td></td><td><span>—</span></td><td></td></tr><tr><th colspan="6">Browser and remote control</th></tr><tr><th><a href="/docs/browser?surface=app">Built-in browser previews and comments</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="about:/docs/browser?surface=app#app-computer-use-in-the-browser">Computer Use in the browser</a></th><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td></tr><tr><th><a href="/docs/chrome-extension">Use ChatGPT with Chrome</a></th><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td></tr><tr><th><a href="/docs/computer-use">Computer Use</a></th><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td></tr><tr><th><a href="/docs/extend/record-and-replay">Record & Replay (macOS)</a></th><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td></tr><tr><th><a href="about:/docs/remote-connections#connect-to-an-ssh-host">SSH remote connections</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/remote-connections">Mobile remote control</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/browser?surface=web">Browser in ChatGPT Web</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th colspan="6">Customization and extensions</th></tr><tr><th><a href="/docs/agent-configuration/agents-md">Custom instructions with <code>AGENTS.md</code></a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/build-skills">Skills</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/plugins">Plugins</a></th><td></td><td></td><td></td><td></td><td><a href="#codex-plan-plugin-limits">Limited†</a></td></tr><tr><th><a href="https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace">Plugin sharing</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/plugins">Connectors</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/extend/mcp">MCP</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/agent-configuration/subagents">Subagents and custom agents</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/customization/memories">Memories</a></th><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td><td><a href="#codex-plan-region-limits">Limited*</a></td></tr><tr><th><a href="/docs/customization/computer-history">Computer History</a></th><td><span>—</span></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th colspan="6">Cloud and integrations</th></tr><tr><th><a href="/docs/cloud">Codex cloud chats</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/environments/cloud-environment">Cloud environments and setup scripts</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/cloud/internet-access">Cloud agent internet access controls</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/sites">Sites</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/third-party/github">GitHub code review and automatic PR reviews</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/third-party/slack">Slack cloud integration</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/third-party/linear">Linear cloud integration</a></th><td></td><td></td><td></td><td></td><td><span>—</span></td></tr><tr><th colspan="6">Admin, security, and analytics</th></tr><tr><th><a href="/docs/enterprise/admin-setup">SAML SSO, MFA, and workspace user management</a></th><td><span>—</span></td><td><span>—</span></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/enterprise/managed-configuration"><code>requirements.toml</code> managed config</a></th><td></td><td></td><td></td><td></td><td></td></tr><tr><th><a href="about:/docs/enterprise/managed-configuration#cloud-managed-requirements">Cloud-managed config policies</a></th><td><span>—</span></td><td><span>—</span></td><td></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/enterprise/roles-and-workspace-permissions">ChatGPT workspace RBAC and custom roles</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr><tr><th><a href="about:/docs/enterprise/admin-setup#enterprise-grade-security-and-privacy">SCIM, EKM, and domain verification</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr><tr><th><a href="about:/docs/enterprise/admin-setup#enterprise-grade-security-and-privacy">Enterprise retention and residency controls</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr><tr><th><a href="https://openai.com/business-data/">No training on API or business data by default</a></th><td><span>—</span></td><td><span>—</span></td><td></td><td></td><td></td></tr><tr><th><a href="/docs/enterprise/workspace-analytics">Analytics dashboard</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/enterprise/analytics-api">Analytics API</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/enterprise/compliance-api">Compliance API and audit logs</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr><tr><th><a href="/docs/security">Codex Security for connected GitHub repositories</a></th><td><span>—</span></td><td><span>—</span></td><td><span>—</span></td><td></td><td><span>—</span></td></tr></tbody></table>

<sup>*</sup> Feature is currently limited to only specific regions. Check the individual feature documentation to learn more about geographic restrictions.

<sup>†</sup> Some first party plugins are not available.

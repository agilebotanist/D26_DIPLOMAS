Scraping: https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/
  Settled (dom-quiet, 7550ms)
  Extracting content...
  Extracted 6898 characters

--- Content ---

Even as OpenAI works to harden its [Atlas AI browser](https://techcrunch.com/2025/10/21/openai-launches-an-ai-powered-browser-chatgpt-atlas/) against cyberattacks, the company admits that [prompt injections](https://techcrunch.com/2025/09/28/wiz-chief-technologist-ami-luttwak-on-how-ai-is-transforming-cyberattacks/), a type of attack that manipulates AI agents to follow malicious instructions often hidden in web pages or emails, is a risk that’s not going away anytime soon — raising questions about how safely AI agents can operate on the open web.

“Prompt injection, much like scams and social engineering on the web, is unlikely to ever be fully ‘solved,’” OpenAI wrote in a Monday [blog post](https://openai.com/index/hardening-atlas-against-prompt-injection/) detailing how the firm is beefing up Atlas’ armor to combat the unceasing attacks. The company conceded that “agent mode” in ChatGPT Atlas “expands the security threat surface.”

OpenAI launched its ChatGPT Atlas browser in October, and security researchers rushed to publish their demos, showing it was possible to write a few words in Google Docs that were capable of changing the underlying browser’s behavior. That same day, Brave [published a blog post](https://brave.com/blog/unseeable-prompt-injections/) explaining that indirect prompt injection is a systematic challenge for AI-powered browsers, including [Perplexity’s Comet](https://techcrunch.com/2025/07/09/perplexity-launches-comet-an-ai-powered-web-browser/).

OpenAI isn’t alone in recognizing that prompt-based injections aren’t going away. The [U.K.’s National Cyber Security Centre earlier this month warned](https://www.ncsc.gov.uk/news/mistaking-ai-vulnerability-could-lead-to-large-scale-breaches) that prompt injection attacks against generative AI applications “may never be totally mitigated,” putting websites at risk of falling victim to data breaches. The U.K. government agency advised cyber professionals to reduce the risk and impact of prompt injections, rather than think the attacks can be “stopped.”

For OpenAI’s part, the company said: “We view prompt injection as a long-term AI security challenge, and we’ll need to continuously strengthen our defenses against it.”

The company’s answer to this Sisyphean task? A proactive, rapid-response cycle that the firm says is showing early promise in helping discover novel attack strategies internally before they are exploited “in the wild.”

That’s not entirely different from what rivals like Anthropic and Google have been saying: that to fight against the persistent risk of prompt-based attacks, defenses must be layered and continuously stress-tested. [Google’s recent work](https://security.googleblog.com/2025/12/architecting-security-for-agentic.html), for example, focuses on architectural and policy-level controls for agentic systems.

But where OpenAI is taking a different tact is with its “LLM-based automated attacker.” This attacker is basically a bot that OpenAI trained, using reinforcement learning, to play the role of a hacker that looks for ways to sneak malicious instructions to an AI agent.

The bot can test the attack in simulation before using it for real, and the simulator shows how the target AI would think and what actions it would take if it saw the attack. The bot can then study that response, tweak the attack, and try again and again. That insight into the target AI’s internal reasoning is something outsiders don’t have access to, so, in theory, OpenAI’s bot should be able to find flaws faster than a real-world attacker would.

It’s a common tactic in AI safety testing: build an agent to find the edge cases and test against them rapidly in simulation.

“Our \[reinforcement learning\]-trained attacker can steer an agent into executing sophisticated, long-horizon harmful workflows that unfold over tens (or even hundreds) of steps,” wrote OpenAI. “We also observed novel attack strategies that did not appear in our human red teaming campaign or external reports.”

![a screenshot showing a prompt injection attack in an OpenAI browser.](https://techcrunch.com/wp-content/uploads/2025/12/openai-prompt-injection-demo-2.png)

Image Credits: OpenAI

In a demo (pictured in part above), OpenAI showed how its automated attacker slipped a malicious email into a user’s inbox. When the AI agent later scanned the inbox, it followed the hidden instructions in the email and sent a resignation message instead of drafting an out-of-office reply. But following the security update, “agent mode” was able to successfully detect the prompt injection attempt and flag it to the user, according to the company.

The company says that while prompt injection is hard to secure against in a foolproof way, it’s leaning on large-scale testing and faster patch cycles to harden its systems before they show up in real-world attacks.

An OpenAI spokesperson declined to share whether the update to Atlas’ security has resulted in a measurable reduction in successful injections, but says the firm has been working with third parties to harden Atlas against prompt injection since before launch.

Rami McCarthy, principal security researcher at [cybersecurity firm Wiz](https://techcrunch.com/2025/09/28/wiz-chief-technologist-ami-luttwak-on-how-ai-is-transforming-cyberattacks/), says that reinforcement learning is one way to continuously adapt to attacker behavior, but it’s only part of the picture.

“A useful way to reason about risk in AI systems is autonomy multiplied by access,” McCarthy told TechCrunch.

“Agentic browsers tend to sit in a challenging part of that space: moderate autonomy combined with very high access,” said McCarthy. “Many current recommendations reflect that trade-off. Limiting logged-in access primarily reduces exposure, while requiring review of confirmation requests constrains autonomy.”

Those are two of OpenAI’s recommendations for users to reduce their own risk, and a spokesperson said Atlas is also trained to get user confirmation before sending messages or making payments. OpenAI also suggests that users give agents specific instructions, rather than providing them access to your inbox and telling them to “take whatever action is needed.”

“Wide latitude makes it easier for hidden or malicious content to influence the agent, even when safeguards are in place,” per OpenAI.

While OpenAI says protecting Atlas users against prompt injections is a top priority, McCarthy invites some skepticism as to the return on investment for risk-prone browsers.

“For most everyday use cases, agentic browsers don’t yet deliver enough value to justify their current risk profile,” McCarthy told TechCrunch. “The risk is high given their access to sensitive data like email and payment information, even though that access is also what makes them powerful. That balance will evolve, but today the trade-offs are still very real.”

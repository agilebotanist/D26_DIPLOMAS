Scraping: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
  Settled (dom-quiet, 2261ms)
  Extracting content...
  Extracted 2000 characters

--- Content ---

There are crucial differences between prompt and SQL injection which – if not considered – can undermine mitigations.

![](/sites/default/files/styles/uncropped_lg/public/images/sql-confused-robot-20251208.jpg?itok=5Pk2xo_-)

Created using MS Copilot

The term ‘prompt injection’ [was coined in 2022](https://simonwillison.net/2022/Sep/12/prompt-injection/) to describe a new class of **application vulnerability** in genAI applications. Prompt injection is where developers concatenate their own instructions with untrusted content in a single prompt, and then treat the model’s response as if there were a robust boundary between ‘what the app asked for’ and anything in the untrusted content.

Whilst [initially reported](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it) as command execution, the underlying issue has turned out to be more fundamental than classic client/server vulnerabilities. Current large language models (LLMs) simply do not enforce a security boundary between instructions and data inside a prompt. Prompt injection attacks are regularly reported in systems that use generative AI (genAI), and are the [OWASP’s #1 attack](https://owasp.org/www-project-top-10-for-large-language-model-applications/) to consider when “developing and securing generative AI and large language model applications”.

On the face of it, prompt injection can initially feel similar to that well known class of application vulnerability, ‘SQL injection’. However, there are crucial differences that if not considered can severely undermine mitigations. When talking to other security professionals, I’ve noticed many with experience in web app security misunderstand prompt injection, assuming it’s conceptually similar to SQL injection.

**This blog argues that comparing SQL injection with prompt injection is dangerous, and that the latter needs to be approached differently to mitigate the risks associated with it.**

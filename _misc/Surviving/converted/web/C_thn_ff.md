Scraping: https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://thehackernews.com/2026/03/anthropic-finds-22-firefox.html
  Settled (dom-quiet, 2162ms)
  Extracting content...
  Extracted 5441 characters

--- Content ---

Anthropic on Friday said it [discovered](https://www.anthropic.com/news/mozilla-firefox-security) 22 new security vulnerabilities in the Firefox web browser as part of a security partnership with Mozilla.

Of these, 14 have been classified as high, seven have been classified as moderate, and one has been rated low in severity. The issues were addressed in [Firefox 148](https://www.firefox.com/en-US/firefox/148.0/releasenotes/), released late last month. The [vulnerabilities](https://www.mozilla.org/en-US/security/advisories/mfsa2026-13/) were identified over a two-week period in January 2026.

The artificial intelligence (AI) company said the number of high-severity bugs identified by its Claude Opus 4.6 large language model (LLM) represents "almost a fifth" of all high-severity vulnerabilities that were patched in Firefox in 2025.

Anthropic said the LLM detected a use-after-free bug in the browser's JavaScript after "just" 20 minutes of exploration, which was then validated by a human researcher in a virtualized environment to rule out the possibility of a false positive.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9hjzSN2bSutSbaNO6ZWEm02wC6hue03kC4VKPSfsdPvcDX2PAvPE-u9QrLCw3POvN3hXFPlyYyFgkAgtKrs4I2oSb9BkIFOWQ_k1ISfIBdT2AoWNvq2Q2DF_3AyA4fJriKPHkTjqYFxu-Y_H4IH9uqscX8lh-puQ5cPmc_veAEr9p4fC0497XT8Fktlp6/s728-nu-rw-lo-l85-e365/tl-insidem-d.jpg)](https://thehackernews.uk/ai-governance-platform-d)

"By the end of this effort, we had scanned nearly 6,000 C++ files and submitted a total of 112 unique reports, including the high- and moderate-severity vulnerabilities mentioned above," the company said. "Most issues have been fixed in Firefox 148, with the remainder to be fixed in upcoming releases."

The AI upstart said it also fed its Claude model access to the entire list of vulnerabilities submitted to Mozilla and tasked the AI tool with developing a practical exploit for them.

Despite carrying out the test several hundred times and spending about $4,000 in API credits, the company said Claude Opus 4.6 was able to turn the security defect into an exploit only in two cases.

This behavior, the company added, signaled two important aspects: the cost of identifying vulnerabilities is cheaper than creating an exploit for them, and the model is better at finding issues than at exploiting them.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiR7S27TSUj8zO6SfTKVyaaZU_d2fqSjR6LwvQB3LL616Df2gFbzN92rJite4Bgyz-rX8A5YN-CydNBhLytbNq7DkZx4rMuhElnME6aDBTDPWHGEzUsY1cu8V8twKOFYXKfon62a_8nyaIuJnidHE5iS_SE5qigtSmFkeHBCMmLKOXe3gSzDFPKhF7rheHA/s1700-nu-rw-lo-l85-e365/firefox-ai.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiR7S27TSUj8zO6SfTKVyaaZU_d2fqSjR6LwvQB3LL616Df2gFbzN92rJite4Bgyz-rX8A5YN-CydNBhLytbNq7DkZx4rMuhElnME6aDBTDPWHGEzUsY1cu8V8twKOFYXKfon62a_8nyaIuJnidHE5iS_SE5qigtSmFkeHBCMmLKOXe3gSzDFPKhF7rheHA/s1700-nu-rw-lo-l85-e365/firefox-ai.jpg)

"However, the fact that Claude could succeed at automatically developing a crude browser exploit, even if only in a few cases, is concerning," Anthropic emphasized, adding the exploits only worked within the confines of its testing environment, which has had some security features like sandboxing intentionally stripped off.

A crucial component incorporated into the process is a task verifier to determine if the exploit actually works, giving the tool real-time feedback as it explores the codebase in question and allowing it to iterate its results until a successful exploit is devised.

One such exploit Claude wrote was for [CVE-2026-2796](https://nvd.nist.gov/vuln/detail/CVE-2026-2796) (CVSS score: 9.8), which has been [described](https://red.anthropic.com/2026/exploit/) as a just-in-time (JIT) miscompilation in the JavaScript WebAssembly component.

The disclosure comes weeks after the company [released](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html) Claude Code Security in a limited research preview as a way to fix vulnerabilities using an AI agent.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWypk5aSrjVVXdRpyJaxKDe9VERLYId6cVdoZUwHGSe-EMh90qROsc-jk3uEKqB8-L4eSpBaka7err1zF86IrsEA4S2IZ8yyEsoZTsiGq2YvGuaCtdFvE8-ej7uEBhLbYJNENjs9umU6qmZCJ1aAzvG-ZDO0NtTVddy5hIGv4FBpDJp8UeOxYEzF5AeuK1/s728-nu-rw-lo-l85-e36/core-d.png)](https://thehackernews.uk/network-defense-dd)

"We can't guarantee that all agent-generated patches that pass these tests are good enough to merge immediately," Anthropic said. "But task verifiers give us increased confidence that the produced patch will fix the specific vulnerability while preserving program functionality—and therefore achieve what's considered to be the minimum requirement for a plausible patch."

Mozilla, in a coordinated announcement, said the AI-assisted approach has discovered 90 other bugs, most of which have been fixed. These consisted of assertion failures that overlapped with issues traditionally found through fuzzing and distinct classes of logic errors that the fuzzers failed to catch.

"The scale of findings reflects the power of combining rigorous engineering with new analysis tools for continuous improvement," the browser maker [said](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/). "We view this as clear evidence that large-scale, AI-assisted analysis is a powerful new addition to security engineers' toolbox."

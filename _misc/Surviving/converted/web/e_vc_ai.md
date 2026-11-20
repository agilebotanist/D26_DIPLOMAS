Scraping: https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery
  Settled (dom-quiet, 2293ms)
  Extracting content...
  Extracted 13467 characters

--- Content ---

![CVE Growth](/blog/ai-assisted-vulnerability-discovery/top20_cnas_cumulative.png)

Key Takeaways:

- CVE disclosure volumes are up sharply year-to-date (YTD) across several software suppliers, including Chrome (+563.2%), VMware (+180.9%), Apache (+170.3%), Mozilla (+156.9%), HPE (+132.3%), and F5 (+113.8%).
- GitHub CVE issuance is also up significantly YTD (+476.07%), with GitHub indicating the increase is spread across many reporters and projects rather than concentrated in one source.
- The increases are consistent with broader use of AI-assisted vulnerability discovery, though the signal is still emerging and not all increases can be directly attributed to AI.
- Public examples from Mozilla, Microsoft, Apache, Curl, and Palo Alto show AI models being used to find, validate, or triage vulnerabilities, with mixed results depending on the project.
- What is less clear is whether these volumes will be sustained, or whether this is a temporary surge as frontier AI models are applied across different code bases.
- Defenders should prepare for higher vulnerability volumes while continuing to use threat intelligence to prioritize emerging threats that are being actively exploited or likely to be.

Since the start of this year, I've been watching for evidence of AI-assisted vulnerability discovery in publicly disclosed CVE volumes. The early signals were noisy. Our " [report a vulnerability](https://www.vulncheck.com/advisories/report) " service saw a flood of submissions that, frankly, started as slop. But over the past few months, the quality of incoming submissions has noticeably improved, and the underlying volume hasn't subsided.

Then on April 7, 2026, Anthropic announced [Project Glasswing](https://www.anthropic.com/project/glasswing) and Claude Mythos Preview, and the conversation shifted hard. Anthropic claimed Mythos had already identified thousands of zero-day vulnerabilities across every major operating system and web browser. Rather than releasing the model publicly, they funneled access to a coalition of partners, including AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks, plus several other organizations.

The cybersecurity industry's response was a mix of awe, fear, uncertainty, and doubt, which prompted two questions: At what scale is AI-assisted vulnerability discovery real? And at what scale would we see it in the public disclosure of vulnerabilities? Which led me to building a list tracking [Anthropic attributed CVEs](https://www.vulncheck.com/blog/anthropic-glasswing-cves) We are now two Patch Tuesdays past the Glasswing announcement, and the signals are starting to emerge.

To put the results in perspective, I started by looking at the top 20 CVE Numbering Authorities and their CVE issuance volume over the past five years and found clear indications across several projects of the likely impact AI-assisted vulnerability discovery is having on public disclosures of vulnerabilities.

## CVE Issuance Trends - Top Software Suppliers

![Software Supplier Trends](/blog/ai-assisted-vulnerability-discovery/2026-cve-trends.png)

Digging in a bit deeper, I decided to look at the top Software Suppliers and their year-over-year growth to better understand what significant changes might be happening. From the chart above we can see some notable increases across Chrome (+563.2%), Mozilla (+156.9%), VMware (+180.9%), Apache (+170.3%), HPE (+132.3%), F5 (+113.8%), among several others. In addition to these, GitHub's 476.07% increase highlights accelerated vulnerability disclosure across a high volume of open source projects.

The evidence appears to point to emerging AI models that have enabled software suppliers and security researchers to discover and remediate vulnerabilities that would have likely gone overlooked otherwise.

## Digging Into Noteworthy Software Suppliers and Open Source Projects

To provide some visibility into the emerging trend of AI-assisted vulnerability discovery, we took a deeper look at several of the software suppliers and open source projects.

### GitHub (Open Source Project)

![Github](/blog/ai-assisted-vulnerability-discovery/github.png)

During the same window in which our submission queue was experiencing its AI-driven surge, GitHub was seeing its own surge in vulnerability reports. Both the volume of findings and the corresponding increase in CVE issuance have been confirmed as real by the GitHub team. "No single reporter accounts for more than ~3% of volume, and no single project accounts for more than ~7%. This isn't one person or one tool, it's a systemic shift in how vulnerability reporting is happening across the ecosystem." - Madison Oliver Ficorilli. Something in the ecosystem has changed, and the most likely explanation is the greater availability of AI models that are effective at discovering vulnerabilities in open source software. It also highlights how open source software appears to serve as a testing ground for AI vulnerability discovery tools and an early indicator of what's to come.

References: [https://www.linkedin.com/pulse/everyones-blaming-ai-bad-vulnerability-reports-data-oliver-ficorilli-kvoxc/?trackingId=miFeABHjId5tHsdVftUuaA%3D%3D](https://www.linkedin.com/pulse/everyones-blaming-ai-bad-vulnerability-reports-data-oliver-ficorilli-kvoxc/?trackingId=miFeABHjId5tHsdVftUuaA%3D%3D)

### Mozilla

![Mozilla](/blog/ai-assisted-vulnerability-discovery/firefox.png)

Mozilla has been one of the more vocal and transparent projects when it comes to AI-assisted vulnerability discovery, and is a participant in Project Glasswing. The Mozilla team stated, "Since February, the Firefox team has been working around the clock using frontier AI models to find and fix latent security vulnerabilities in the browser." They also highlighted their participation in Anthropic's Mythos preview: "As part of our continued collaboration with Anthropic, we had the opportunity to apply an early version of Claude Mythos Preview to Firefox."

References:

- [https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/](https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/)
- [https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)
- [https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/>](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/%3E)

### Chrome

![Chrome](/blog/ai-assisted-vulnerability-discovery/chrome.png)

Chrome experienced a 563% increase in CVE disclosures, one of the most significant upticks we observed, and Google has confirmed its participation in Project Glasswing.

While we haven't seen concrete confirmation of what tools were used to drive the sudden increase, we suspect it's related to AI discovery tools, likely some combination of Mythos and Google's own AI models. The trend points toward AI-assisted discovery as the most likely driver.

Additionally, Google's Threat Intelligence Group recently published an article on adversaries leveraging AI for vulnerability exploitation, highlighting that the use of new tools isn't limited to the defender side.

References: [https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)

### Microsoft

![Microsoft](/blog/ai-assisted-vulnerability-discovery/microsoft.png)

Microsoft is a participant in Project Glasswing and has also announced the launch of its own AI discovery tool, clear evidence that AI is making an impact on CVE disclosures. As Microsoft noted, "The findings in this Patch Tuesday and the retrospective recall on five years of CLFS MSRC cases are evidence that AI vulnerability findings can scale."

This suggests we're likely just at the beginning of higher volumes of CVE disclosures across Microsoft products. It will be interesting to see how far Microsoft's CVE issuance scales over the coming months.

References: [https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)

### Apache

![Apache](/blog/ai-assisted-vulnerability-discovery/apache.png)

Apache is a participant in Project Glasswing and is experiencing a 170%+ increase in CVEs published. As Anthropic stated, "we've donated $1.5M to the Apache Software Foundation to enable the maintainers of open-source software to respond to this changing landscape." We thought it would be worthwhile to provide some examples of security researchers using AI tools to assist in their discovery work. ActiveMQ CVE-2026-34197 was discovered by Naveen Sunkavally with the assistance of Claude and is now known to be exploited in the wild and recently landed on CISA KEV.

In his words: "These days I always use Claude to take a first pass at source code for vulnerability hunting. I prompt it lightly and set up a target on the network for it to validate findings. A lot of the time, Claude finds interesting stuff but it doesn't quite rise to the level of a CVE I'd bother reporting. In this case, it did a great job, with nothing more than a couple of basic prompts. This was 80% Claude with 20% gift-wrapping by a human." - Naveen Sunkavally.

References: [https://horizon3.ai/attack-research/disclosures/cve-2026-34197-activemq-rce-jolokia/](https://horizon3.ai/attack-research/disclosures/cve-2026-34197-activemq-rce-jolokia/)

## Other Observations in AI-Assisted Vulnerability Discovery

### Curl

While Curl didn't make our chart for CVE growth (we excluded lower-volume CVE software suppliers), it remains one of the most heavily audited and fuzzed code bases in existence.

Daniel Stenberg, who maintains Curl, offers a grounded perspective: of the five "confirmed" vulnerabilities Mythos initially reported, only one held up as a valid CVE after his security team's review, with the rest being false positives or non-security bugs. He also emphasizes that running multiple AI models over time continues to uncover different bugs and vulnerabilities, and notes that previous AI tools have already driven hundreds of bugfixes in curl. Daniel's blog is well worth the read.

References: [https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/)

### Palo Alto

While Palo Alto didn't make the charts due to lower overall CVE issuance, they've seen a 37% increase in CVE issuance year to date and have been very vocal recently about their use of frontier models. "For over a month, we've been using the latest frontier AI models, including Anthropic's Mythos and Claude Opus 4.7 and OpenAI's GPT-5.5-Cyber as part of the Trusted Access for Cyber program. Our teams have worked tirelessly to learn how to fully leverage the immense power of these models, and to find and fix any vulnerabilities as quickly as possible." - Rich Campagna, SVP Palo Alto Networks.

References:

- [https://www.paloaltonetworks.com/blog/2026/05/defenders-guide-frontier-ai-impact-cybersecurity-may-2026-update/](https://www.paloaltonetworks.com/blog/2026/05/defenders-guide-frontier-ai-impact-cybersecurity-may-2026-update/)
- [https://www.linkedin.com/feed/update/urn:li:activity:7460374274588061696/?utm\_source=share&utm\_medium=member\_desktop&rcm=ACoAAADShEQBPA7bU2zaIIHMTqDWMnEOq7PYu7g](https://www.linkedin.com/feed/update/urn:li:activity:7460374274588061696/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAADShEQBPA7bU2zaIIHMTqDWMnEOq7PYu7g)

## A Bit of a Reality Check for Defenders

Vulnerability volumes are clearly trending up, with a short-term spike in public disclosures tied to AI-assisted discovery. What's less clear is whether these volumes will be sustained, or whether this is a temporary surge as better AI models are pointed at different code bases and new models continue to surface vulnerabilities. Most defenders are starting to see the initial impact of AI-assisted vulnerabilities in their backlogs and should plan for sustained volumes over time. That reinforces the importance of patching early and often, updating to the latest version when possible, and using threat intelligence to prioritize emerging threats that are being actively exploited or likely to be.

## About VulnCheck

VulnCheck is helping organizations not just to solve the vulnerability prioritization challenge - we’re working to help equip any product manager, CSIRT/PSIRT or SecOps team and Threat Hunting team to get faster and more accurate with infinite efficiency using VulnCheck solutions.

We knew that we needed better data, faster across the board, in our industry. So that’s what we deliver to the market. We’re going to continue to deliver key insights on vulnerability management, exploitation and major trends we can extrapolate from our dataset to continuously support practitioners.

Are you interested in learning more? If so, VulnCheck's [Exploit & Vulnerability Intelligence](https://vulncheck.com/product/exploit-intelligence) has broad threat actor coverage. Register and demo our data today.

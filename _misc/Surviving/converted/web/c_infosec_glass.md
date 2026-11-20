Scraping: https://www.infosecurity-magazine.com/news/anthropic-glasswing/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.infosecurity-magazine.com/news/anthropic-glasswing/
  Settled (dom-quiet, 2074ms)
  Extracting content...
  Extracted 5217 characters

--- Content ---

Seven months on, Anthropic’s Project Glasswing is “overwhelming” maintainers with “underwhelming findings.”

This harsh conclusion comes from Patrick Garrity, a vulnerability researcher at VulnCheck, in [a report](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) released on November 9.

The analysis represents Garrity’s latest update on Project Glasswing’s results based on data publicly reported by Anthropic, an exercise aimed at understanding “whether Anthropic’s claims are overhyped or grounded in reality,” Garrity said.

Project Glasswing is [Anthropic’s flagship effort](https://www.infosecurity-magazine.com/news/anthropic-launch-project-glasswing/) to offer the company’s frontier AI models to security researchers in order to help them find and remediate software vulnerabilities.

## Only 217 Vulnerabilities Publicly Fixed After Seven Months of Glasswing

According to the latest update on Anthropic’s coordinated vulnerability disclosure dashboard, dated November 2, 2026, Project Glasswing has enabled researchers to find 37,966.

However, only 7349 (19.4%) are listed in the ledger, Anthropic's public tracking register of vulnerabilities and potential vulnerabilities identified through Project Glasswing.

Out of the vulnerabilities included in the ledger, Garrity has found that 5276 have been validated as real unique vulnerabilities. The rest is made of 1654 duplicates and 419 that were withdrawn.

Of the 5276 relevant vulnerabilities, almost 13% (4866) have been reported to the maintainers and 193 are still in a phase of “pre-disclosure” and are yet to be reported to maintainers.

This leaves 217 vulnerabilities - less than 0.5% of the total of vulnerabilities claimed to be found thanks to Glasswing – that have been fixed, Garrity noted.

![Visualization of Glasswing vulnerability reports categorized by VulnCheck’s Patrick Garrity. Source: VulnCheck](https://assets.infosecurity-magazine.com/content/span/fba1e7ba-dcb8-4143-8708-2f3d25cca5f0.png)

Visualization of Glasswing vulnerability reports categorized by VulnCheck’s Patrick Garrity. Source: VulnCheck

The researcher added that since [his last analysis of Glasswing vulnerability findings in September](https://www.vulncheck.com/blog/anthropic-glasswing-receipts), Anthropic had added 4613 vulnerability findings to its ledger, yet only 15 were marked as fixed within the same period. A significant volume of findings added to the ledger between September and November (1668) were marked as duplicates.

This led the researcher to question Anthropic’s latest claimed true positive rate of 94.2%, which, he said, raises “questions about how it accounts for duplicates and withdrawn findings.”

[*Read more: Anthropic Expands Mythos Access to 150 More Organizations*](https://www.infosecurity-magazine.com/news/anthropic-glasswing-expansion/)

## Anthropic Launched OSS Scanner to Scale Vulnerability Disclosures

One reason that could explain the gap between the vulnerabilities claimed to be found through Glasswing and vulnerabilities publicly fixed is the pace of human vulnerability report triage.

On October 8, Anthropic said it had found more than 29,000 candidate vulnerabilities but had manually reviewed only about 6000, and that it remains "bottlenecked on our human capacity to validate these findings."

“We are working on scaling our vulnerability disclosures,” the company [added](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source).

Therefore, it launched its own Open Source Security Scanner (OSS Scanner), a self-service new tool inspired by Google's OSS-Fuzz project and that allows maintainers to request a scan and triage the findings themselves.

Anthropic also said it has already sent nearly 5000 unverified vulnerability reports directly to maintainers who asked to receive everything in bulk.

This new shift in Project Glasswing started showing issues in AI-powered vulnerability reports more clearly.

For instance, Daniel Stenberg, maintainer of the Client and URL (cURL) project, [said](https://www.linkedin.com/feed/update/urn:li:share:7524224297595269120/) on November 6 he received 45 vulnerability reports from Anthropic through Glasswing.

After analyzing 34 of them using Anthropic OSS Scanner and other tools, Stenberg pointed out that 19 weren't vulnerabilities at all and six have been confirmed as low severity.

“AI is a valuable tool for finding vulnerabilities, and I'm not discounting that. But seven months in, the evidence still doesn't match the launch narrative. The CVEs are a sliver of this year's total, almost none are being exploited, fixes have stalled while duplicates and withdrawals pile up, and the triage burden is shifting onto the open source maintainers Glasswing promised to help. The receipts keep coming in. They still don't reconcile,” Garrity concluded.

*Infosecurity* contacted Anthropic for comment, but the company had not responded by the time of publication.

*Image credits: Stockinq / gguy / Shutterstock.com*

[*Read now: How Industry Coalitions Are Rallying to Secure Open Source Software for the AI Era*](https://www.infosecurity-magazine.com/news-features/industry-coalitions-secure-open/)

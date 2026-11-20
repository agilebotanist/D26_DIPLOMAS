Scraping: https://www.vulncheck.com/blog/anthropic-glasswing-cves
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.vulncheck.com/blog/anthropic-glasswing-cves
  Settled (dom-quiet, 2418ms)
  Extracting content...
  Extracted 12593 characters

--- Content ---

Anthropic's Project Glasswing has generated significant attention—but very little concrete data. One question keeps coming up: what exactly did it find, disclose, and receive CVEs for? We've fielded this question repeatedly, so I did the work of tracking down publicly disclosed CVEs credited to the Anthropic research team at this time.

## Key Takeaways

- 75 CVEs mention “Anthropic”
- 40 are actually credited to Anthropic researchers
- Only 1 is explicitly attributed to Glasswing
- 10 are from external collaboration programs (Calif.io / MADBugs)

Taken together, this suggests that while Anthropic researchers are actively contributing to vulnerability discovery and appears to be promising, the publicly attributable impact of Glasswing itself remains limited so far.

## Methodology

I started by re-reading the [Glasswing report](https://www.anthropic.com/glasswing) and the advisories published at [red.anthropic.com](https://red.anthropic.com/). Neither source provides a comprehensive CVE list of vulnerabilities discovered by Anthropic. So I decided to search the full CVE record database, and searched every CVE record containing the term "anthropic" and reviewed each one.

## What Disclosed Vulnerabilities Have Been Credited to the Anthropic Research Team?

75 CVE records contain the term "Anthropic." Of those, 40 are credited to Anthropic or Anthropic-affiliated researchers in the credits field. The remaining 35 are CVEs affecting Anthropic tools like Claude Code, MCP Inspector, and third party integrations which are out of scope for this analysis..

Searching the credits field for "Anthropic" is one way to explore this question today, though the credits vary. The 40 break down across three distinct credit attributions: the core Anthropic research team, Nicholas Carlini individually, and Calif.io, an independent security research firm running a program called MADBugs (Month of AI-Discovered Bugs) that credits their work jointly as "Calif.io in collaboration with Claude and Anthropic Research." The 9 wolfSSL CVEs and the NGINX CVE all fall into that third category.

CVE credits are not standardized and depend on how individual CNAs populate the field, meaning attribution is incomplete and sometimes inconsistent.

Here is the breakdown by vendor:

| Vendor | Product | \# of CVEs |
| --- | --- | --- |
| Mozilla | Firefox | 28 |
| wolfSSL | wolfSSL | 9 |
| F5 | NGINX Plus | 1 |
| FreeBSD | FreeBSD | 1 |
| OpenSSL | OpenSSL | 1 |
| **Total** |  | **40** |

## The List of 40 CVEs Attributed to Anthropic

The Latest Updated List is Here: [https://github.com/patrickmgarrity/Anthropic-Credited-CVEs](https://github.com/patrickmgarrity/Anthropic-Credited-CVEs)

| CVE Number | Date Published | Vendor | Product | CVSS | Credit |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-2763 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2764 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2765 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2766 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2769 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2770 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2771 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2772 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2773 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2774 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2775 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2785 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2786 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2787 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2788 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2789 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2791 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2796 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2797 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2799 | 2026-02-24 | Mozilla | Firefox | 8.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2804 | 2026-02-24 | Mozilla | Firefox | 5.4 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-2805 | 2026-02-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-4702 | 2026-03-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-4704 | 2026-03-24 | Mozilla | Firefox | 7.5 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-4705 | 2026-03-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-4718 | 2026-03-24 | Mozilla | Firefox | 8.1 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-4723 | 2026-03-24 | Mozilla | Firefox | 9.8 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-4724 | 2026-03-24 | Mozilla | Firefox | 9.1 | Evyatar Ben Asher, Keane Lucas, Nicholas Carlini, Newton Cheng, Daniel Freeman, Alex Gaynor, and Joel Weinberger using Claude from Anthropic |
| CVE-2026-27654 | 2026-03-24 | F5 | NGINX Plus | 8.2 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-4747 | 2026-03-26 | FreeBSD | FreeBSD | 8.8 | Nicholas Carlini using Claude, Anthropic |
| CVE-2026-28386 | 2026-04-07 | OpenSSL | OpenSSL | 9.1 | Stanislav Fort (Aisle Research); Pavel Kohout (Aisle Research); Alex Gaynor (Anthropic) |
| CVE-2026-5194 | 2026-04-09 | wolfSSL | wolfSSL | 9.3 | Nicholas Carlini from Anthropic |
| CVE-2026-5446 | 2026-04-09 | wolfSSL | wolfSSL | 6.0 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5503 | 2026-04-09 | wolfSSL | wolfSSL | 6.9 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5447 | 2026-04-09 | wolfSSL | wolfSSL | 6.3 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5466 | 2026-04-10 | wolfSSL | wolfSSL | 7.6 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5477 | 2026-04-10 | wolfSSL | wolfSSL | 8.2 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5479 | 2026-04-10 | wolfSSL | wolfSSL | 7.6 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5500 | 2026-04-10 | wolfSSL | wolfSSL | 8.7 | Calif.io in collaboration with Claude and Anthropic Research |
| CVE-2026-5501 | 2026-04-10 | wolfSSL | wolfSSL | 8.6 | Calif.io in collaboration with Claude and Anthropic Research |

CVEs Added Post Blog Publication

| CVE Number | Date Published | Vendor | Product | CVSS | Credit |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-5588 | 2026-04-15 | Legion of the Bouncy Castle Inc. | BC-JAVA | 6.3 | Nicholas Carlini using Claude, Anthropic |

## What Vulnerabilities Are Directly Attributable to Glasswing?

Despite the attention around Glasswing, only one publicly disclosed CVE can currently be directly tied to it. CVE-2026-4747 (FreeBSD NFS RCE) is explicitly attributed to Glasswing and Mythos Preview by name, described as fully autonomously identified and exploited.

The Glasswing page also references three vulnerabilities without CVE numbers: a 27-year-old OpenBSD flaw, a 16-year-old FFmpeg bug, and Linux kernel privilege escalation chains. All three are still under embargo pending patches.

The broader limitation is that Anthropic committed the details of additional findings via cryptographic hashes prior to public disclosure as they are currently under embargo until a patch is released and the vulnerability is publicly disclosed. The full picture won't be known until public disclosure takes place and Anthropic has indicated a public summary report is expected around July 2026.

The July 2026 report will be the real tell. When Anthropic follows through with a full public accounting of what Glasswing found and fixed, it will provide broader visibility into the details you might be looking for. Until then, the best signals available are the CVE credits field and Anthropic's own advisories at [red.anthropic.com](https://red.anthropic.com/).

## Considerations for Anthropic

It would be beneficial for Anthropic to create a dedicated security advisory page where security advisories and vulnerability disclosures were published in a consistent way, to provide a way for consumers to understand the question: what vulnerabilities have been discovered by the Anthropic research team and Project Glasswing?

## About VulnCheck

VulnCheck is helping organizations not just to solve the vulnerability prioritization challenge - we’re working to help equip any product manager, CSIRT/PSIRT or SecOps team and Threat Hunting team to get faster and more accurate with infinite efficiency using VulnCheck solutions.

We knew that we needed better data, faster across the board, in our industry. So that’s what we deliver to the market. We’re going to continue to deliver key insights on vulnerability management, exploitation and major trends we can extrapolate from our dataset to continuously support practitioners.

Are you interested in learning more? If so, VulnCheck's [Exploit & Vulnerability Intelligence](https://vulncheck.com/product/exploit-intelligence) has broad threat actor coverage. Register and demo our data today.

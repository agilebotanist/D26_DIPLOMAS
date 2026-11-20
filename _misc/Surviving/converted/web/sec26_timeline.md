
On October 21, 2026, multiple vulnerabilities -- collectively known as PHP2Shell -- that affected all versions of the open source PHP programming language were disclosed. Although patches are available, the disclosure led to a flurry of media reports as organizations around the world scrambled to patch the issue.

PHP first gained notoriety in the mid-1990s as the P in the LAMP (Linux, Apache, MySQL, PHP) stack that defined the first era of web applications. Decades later, PHP remains a foundational element of many web applications, particularly content management systems. According to [some estimates](https://w3techs.com/technologies/details/pl-php), PHP powers 70% of the websites on the internet today. That ubiquity makes any serious vulnerability a significant risk to the internet.

## PHP2Shell: A timeline of events

To understand PHP2Shell, it’s critical to look at the timeline, which spans multiple years. PHP regularly patches code for vulnerabilities and is always looking for issues. The discovery of the PHP2Shell issues was not a one-day event, nor was it made by any single individual or organization.

All times are UTC unless noted.

- **2024:** An audit funded by Germany’s Sovereign Tech Agency and conducted by security firm Quarkslab [found](https://thephp.foundation/blog/2025/04/10/php-core-security-audit-results/) early indications of the out-of-memory problem behind CVE-2026-109618, though at the time no direct exploit path was found.
- **July 30, 2026:** An audit by security firm Calif, done using OpenAI’s Patch the Planet program, begins.
- **Aug. 11, 2026:** Calif researcher Ryan Austin reports an unconditional remote code execution ([RCE](https://www.techtarget.com/it-infrastructure/definition/remote-code-execution-RCE)) flaw with the same out-of-memory problem first spotted in 2024, the PHP Foundation [said](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/). OpenAI also independently reported the root cause.
- **Aug. 14 and 15:** Calif shares a working proof of concept (PoC) on the 14th.
- **Aug. 15:** PHP confirms the PoC.
- **Aug. 19:** Wiz Research, part of Google Cloud, discovers its first unauthenticated remote code PHP vulnerability using Wiz’s Atlas tool and the Gemini 4 Argon and GPT-5.6 Sol AI models.
- **Aug. 24:** Wiz reports its findings to the PHP security team.
- **Aug. 21:** Calif reports a second bug to PHP.
- **Sept. 18:** OpenAI reports additional attack vectors.
- **Sept. 21:** The PHP Foundation begins developing a coordinated fix.
- **Oct. 17:** Amazon reports a PHP exploitation attempt against its MadPot honeypot network.
- **Oct. 20, about 15:00:** PHP publishes a [pre-announcement](https://www.php.net/archive/2026.php#2026-10-20-1) warning that a security update will be released on Oct. 21. Calif mistakenly publishes a video of its PoC working against several targets. Around 23:00, mitigation advice that PHP had given to a few critical infrastructure providers might also have leaked.
- **Oct. 21, 02:00 to 08:00:** AWS identifies multiple PoC exploits for the flaws, the earliest around 02:00. It also identifies additional exploitation attempts against its MadPot sensors from anonymized infrastructure between 02:00 and 08:00. It gives no attempt counts.
- **Oct. 21, 14:00:** PHP [releases](https://www.techtarget.com/news/PHP2Shell-22M-exposed-servers-at-risk-as-emergency-patches-released/836071/) 8.5.12, 8.4.27, 8.3.36 and 8.2.35.
- **Oct. 23:** PHP discloses a third flaw, CVE-2026-115560.
- **Oct. 26:** PHP releases updated builds for Windows to patch CVE-2026-111497, an out-of-bound vulnerability in Brotli decompression.
- **Oct. 26:** PHP2shell vulnerabilities CVE-2026-109618 and CVE-2026-109619 are added to the CISA Known Exploited Vulnerabilities (KEV) catalog.
- **Nov. 19:** Scheduled release date for PHP 8.6, which will patch CVE-2026-115560.

## The vulnerabilities

PHP2Shell isn’t a single vulnerability; it’s the name given to two distinct issues. Both CVEs could potentially enable an attacker to remotely execute code without any authentication. RCE is among the most dangerous types of software vulnerabilities.

**CVE-2026-109618**, also called RCE via OOM corruption, is an RCE issue stemming from an out-of-memory flaw.

Inside PHP, every web request has a memory limit. When a request exceeds the limit, PHP aborts it. Some unfinished data, however, remains in that type of request. When PHP cleans up, it treats that unfinished data as valid and tries to free memory that was never set up. Attackers can force this by sending a crafted upload that pushes a request over the limit. The result is an unauthenticated request that can run code.

The vulnerability was confirmed to run on Apache with mod\_php, a common way to deploy PHP for web applications.

**CVE-2026-109619**, also known as RCE via stale global state, is an RCE vulnerability issue related to how state retains memory pointers from a prior request.

PHP processes incoming requests and uses sessions, cookies and other mechanisms to manage state between requests. This flaw lets an attacker trigger a fatal error, such as by exhausting memory, that skips the step that resets that state. The request’s memory is then freed while the state still points to it. A future request can then use the dangling pointer in a way that could enable unauthenticated RCE.

This flaw has been confirmed against Apache mod\_php. PHP-FPM (FastCGI Process Manager) -- a PHP implementation designed to handle high-performance applications -- is also exposed under certain front-end configurations.

**CVE-2026-115560** is an unpatched (as of Oct. 27) PHP RCE vulnerability. The limited details available identify it as a session upload progress issue.

According to the PHP Group’s [limited advisory](https://www.php.net/archive/2026.php#2026-10-23-1):

“The issue can only occur under an unusual combination of configuration and application code. An application must set session.serialize\_handler to php\_binary or php\_serialize in its configuration and then switch it to php at runtime with ini\_set() before calling session\_start(). Session upload progress must also still be enabled. Applications that never change the serialize handler at runtime can keep the feature enabled.”

## The role of AI in vulnerability discovery

The presence of vulnerabilities and flaws is essentially inherent to software development. Memory-related vulnerabilities, such as use-after-free and out-of-memory, have existed for decades, though finding them is often tedious and time-consuming. On the other hand, just because a vulnerability exists doesn’t mean it can be easily exploited, at least by a human.

The widespread use of AI is changing the calculus for both [vulnerability detection and exploitation](https://www.techtarget.com/news/Vulnerability-management-needs-an-update-for-the-AI-era/836156/). AI-powered tools can scan more at a greater speed than humans, surfacing weaknesses quickly and effectively -- for both defenders and attackers. In the latter case, they can probe and exploit those weaknesses just as quickly.

### Read More in Cybersecurity

When the PHP Foundation conducted an audit of its code in 2024, there was no clear exploit path. But in 2026, with the help of AI tools, Calif, OpenAI and Wiz were all able to find real exploitable conditions.

OpenAI [reported](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) that Calif identified a critical flaw using GPT-5.6 Sol as part of Patch the Planet. It’s important to note that Calif wasn’t using any kind of exotic or special version of GPT-5.6. Nor did Calif [use](https://calif.io/php2shell/) any special harnesses or models that were not generally available.

“The vulnerable code had been there for more than a decade -- what AI changed was the ability to understand the weaknesses and turn them into a working exploit,” Wiz stated in its [disclosure](https://www.wiz.io/blog/php2shell-php-rce). “With frontier AI models and the right tools, a single researcher completed in a week what previously would have taken a world-class team months of work.”

## A point of contention: A botched disclosure

In the modern era of software development, the concept of responsible disclosure is critical to limiting panic and protecting users. It also ensures malicious hackers don’t have an early heads-up on any issue before it’s fixed.

In the case of PHP2Shell, the researchers who found the vulnerabilities responsibly and privately disclosed them, enabling developers to verify the issues and work on fixes.

PHP, meanwhile, was working to keep security vendors and platform providers informed on the fix. The goal was to have a coordinated disclosure in which the fixes and any related posts were made available simultaneously.

PHP set the release for Oct. 22 at 14:00 UTC. Its pre-announcement reserved the right to release early if details became public or evidence of exploitation appeared.

### Read More in Cybersecurity

PHP ultimately published its pre-announcement at 19:30 UTC on Oct. 20 and moved the patch release up a day to Oct. 21. The embargo was subsequently broken by the software security vendor Chainguard. The PHP Foundation [said](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) Chainguard published images containing the fix at 07:41 UTC on Oct. 21, more than six hours before the scheduled release. Like other distributors, Chainguard received the patch in advance so its users could update as soon as the vulnerabilities were disclosed.

According to PHP, Chainguard’s early disclosure put everyone else at risk because attackers could study the fix before patches were widely available.

## Who was affected

PHP is widely used across the internet and is a core element of many popular content management systems, including WordPress and Drupal.

In the first days following the disclosure, the most visible impact was the response from governments and organizations. Multiple security organizations, including the National Security Agency, CISA, CERT-EU and the National Cyber Security Centre, advised organizations to be cautious and to take sites offline or place them in maintenance mode until the patch was fully deployed. Hundreds of websites subsequently went offline, including government sites in the Netherlands, Canada, France, Germany, Finland, Belgium and Czech Republic.

Numerous private entities restricted access to their sites until a patch was deployed, among them Wikimedia Foundation, Internet Archive, 4chan, Pinboard, BBC, OpenStreetMap and Duolingo.

There isn’t a complete list of every site impacted. At the height of the incident on Oct. 21, that number was in the thousands and steadily declined in the days since. The PHPocalypse Tracker [provides](https://allixsenos.github.io/phpocalypse-tracker/) regular updates on the status of impacted sites.

## What’s happening now

Attackers will always be opportunistic; if there’s a known vulnerability that hasn’t been patched, they’ll go after it. With an attack surface as big as PHP’s, it was inevitable that the opportunity wouldn’t be overlooked.

The initial round of attack volume was reported by platform and security vendors:

- **AWS.** The importance of enabling platforms to patch under embargo was highlighted by Amazon, which reported more attack volume after the patch was released. “Once the embargo was lifted and the patch was released, additional proof-of-concept exploits appeared within hours, and we saw them used against our sensors almost immediately,” Amazon said in its [disclosure.](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/) “PHP2Shell is now seeing broad exploitation attempts in the wild.”
- **Cloudflare.** In an [X post](https://x.com/eastdakota/status/2113079352682570051?s=20), CEO Matthew Prince reported that the company saw thousands of exploits in the 10 hours before PHP2Shell was publicly announced, and that the number jumped to tens of thousands in the 45 minutes post-announcement, hundreds of thousands within two hours and then millions.
- **Fastly.** As of Oct. 22, Fastly reported approximately 250,000 requests from roughly 3,200 public IPs.
- **Imperva.** Early attack volume was [reported](https://www.imperva.com/blog/php2shell-early-attack-activity-through-impervas-lens/) at 482,342 requests and 122,311 attack sessions against 21,998 sites in 103 countries in its first 24 hours of observation. U.S. sites comprised 64.5% of targets.
- **Wordfence.** Wordfence, a widely deployed firewall in front of WordPress deployments, [reported](https://www.wordfence.com/blog/2026/10/attacks-on-php2shell-continue-but-no-known-compromises-as-a-result-yet/) blocking more than 74,000 exploit or probing attempts through Oct. 22.

### Patching status

The whole point of coordinated responsible disclosure is that a patch is available when the vulnerability is disclosed. That’s the difference with a zero-day flaw: Attackers can exploit sites that have no recourse or patch available.

The PHP2Shell patches impact both individual organizations running PHP and platforms that use PHP as part of a service or application offering. The patches also enable web application firewall (WAF) providers to have network-level mitigations to help reduce the risk.

- **PHP language.** The PHP Foundation [released](https://www.php.net/downloads.php) PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, which corrected the PHP2shall issues, on Oct. 21. Many Linux providers have released patches and updated versions for their respective distributions, including Red Hat, Ubuntu, SUSE and Debian.
- **Edge and security providers.** Cloudflare, Akamai, Fastly and Imperva are among the many vendors that provided updated WAF protection to users on Oct. 21.
- **Cloud platforms.** AWS, Google Cloud and Microsoft Azure all report updating PHP packages for potentially affected services.
- **Hosting providers.** GoDaddy [updated](https://www.godaddy.com/resources/news/important-php-security-update-what-website-owners-need-to-do) its Managed Hosting for WordPress, Windows Hosting and Web Hosting products, but customers must update PHP in their virtual private servers (VPSes). Bluehost [said](https://www.bluehost.com/status/announcement/271) most platforms were updated as of Oct. 22, and that customers on VPSes and dedicated servers must update PHP themselves.

## How many sites have actually patched PHP?

It’s difficult to pinpoint how many sites have been patched, but reliable public resources indicate overall trends.

Censys deployed a [public PHP service tracker](https://php2shell.censys.com/) by version that updates hourly. At 15:15 UTC on Oct. 26, it showed 32,473,855 services were still using an affected version of PHP. It counted 42,405,807 services using an affected version since tracking began Oct. 21. Censys said version-based counts are an upper bound because Linux distributions often backport fixes without changing the version.

PHP2Shell Patch Update Tracker [reported](https://php2shell-tracker.com/) that 20.86% of PHP hosts with a visible version were patched globally as of 17:00 on Oct. 27. The site doesn’t name its operator or methodology, so treat the figure with caution.

## How CISOs should respond to PHP2Shell

A lot of guidance is available to IT security teams and CISOs, with the most authoritative coming from CISA and the PHP Foundation.

First, it’s important to identify what to patch, what to pull offline and which vendors to question. CISA [advised](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) organizations to immediately patch and prioritize internet-facing systems, and to take PHP-based systems offline if they can’t be updated promptly or if they run PHP 8.1 or earlier.

CISOs and their teams must also address the following:

- **Find every PHP system.** Organizations need an accurate inventory of every system that uses PHP. Note that PHP is often a component of other software, so be sure to check [software bills of materials](https://www.techtarget.com/news/SBOM-formats-explained-Guide-for-enterprises/836510/) for it. Don’t limit the search to older versions of PHP because all versions could be affected.
- **Ask vendors about embedded PHP.** Products could be vulnerable even when PHP runs behind the scenes. Ask each product vendor whether its software embeds PHP and when it will patch.
- **Patch and restart.** It should go without saying, but patch as soon as possible. Update to PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35 and restart every PHP worker.
- **Replace end-of-life PHP.** Organizations can only patch supported PHP versions, leaving older versions at risk. Migrate to a supported PHP branch or use a vendor backport for an older version if available.
- **Use a WAF as a backstop.** It’s not always possible to patch running PHP instances immediately. Using a WAF can provide additional protection.
- **Check for compromise.** Attackers jumped on the exploit quickly. Conduct a threat-hunting exercise to identify any indicators of compromise related to PHP2Shell and continuously monitor for anomalous activity. [AWS](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/) detected the first attempt on Oct. 17, so look back at least that far.

*Sean Michael Kerner is an IT consultant, technology enthusiast and tinkerer. He has pulled Token Ring, configured NetWare and been known to compile his own Linux kernel. He consults with industry and media organizations on technology issues.*

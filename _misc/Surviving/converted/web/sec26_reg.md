
### READ MORE

- [
	#### Oracle reveals fix-this-ASAP-grade Java4Shell bug that allows attacks on many third-party apps
	5 hours ago
	](/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661)
- [
	#### Attackers backdoor trusted AWS integrations to steal secrets
	8 days ago
	](/security/2026/11/09/attackers-backdoor-trusted-aws-integrations-to-steal-secrets/5308553)
- [
	#### AI agents are a 'bane' for some website operators, says Cloudflare
	12 days ago
	](/networks/2026/11/06/ai-agents-are-a-bane-for-some-website-operators-says-cloudflare/5308022)
- [
	#### North Korean fake job interview led to $6.3B Binance heist
	14 days ago
	](/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398)
- [
	#### Suspected Chinese attackers built a custom PHP2Shell exploit and rooted 25 servers
	19 days ago
	](/security/2026/10/29/suspected-chinese-attackers-built-a-custom-php2shell-exploit-and-rooted-25-servers/5306456)

PHP developers have accused software supply chain security shop Chainguard of effectively revealing critical bugs in the open-source scripting language ahead of a planned official disclosure.

On Wednesday, just hours after [releasing emergency patches](https://www.theregister.com/security/2026/10/21/php-devs-publish-critical-bug-fix-as-site-owners-warned-pull-em-offline-if-youre-unpatched/5304519) for the two bugs collectively called PHP2shell, PHP maintainers published a blog about how the vulnerabilities were found and fixed.

They credited researchers at Calif, OpenAI, and Wiz with finding the security holes between August and September. All three companies have said they used AI models to find the vulnerabilities, which are now tracked as CVE-2026-109618 and CVE-2026-109619, and can allow an unauthenticated attacker to execute code on servers running PHP.

This is especially serious because PHP powers huge chunks of the public web. It also adds a dose of irony to the “leak and disrupted disclosure” part of the blog, which [blames Chainguard](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) - a company that aims to secure software supply chains by hardening open source code - for the messy disclosure.

The trouble, according to PHP developers, started on Tuesday around 15:00 UTC, when “two CVE IDs began circulating on online forums and social media,” along with incorrect information about the release time and CVSS severity rating. At that point, no technical details leaked.

The rumors, however, prompted PHP maintainers to [warn people in advance](https://www.php.net/archive/2026.php#2026-10-20-1) about the critical flaws, and move the planned disclosure forward a day, from Thursday to Wednesday.

“Distributors were still packaging the fix, so releasing immediately would have left many users without an easy way to update,” the PHP Foundation blog says. “Moving the release forward by one day was the best compromise between acting quickly, giving people time to prepare, and making sure everyone had a simple update path when the vulnerabilities were disclosed.”

A couple of hours later, Calif “mistakenly” published a video showing a proof-of-concept exploit and “additional, though limited” information about the bugs, we’re told.

“Mitigation advice we started providing to a few critical infrastructure providers around Oct 20th 23:00 UTC, may have leaked as well,” the PHP blog says, but it does not name these providers. And then it throws Chainguard under the bus:

“On October 21st at 07:41 UTC, more than six hours before the coordinated release, Chainguard unilaterally broke the embargo and published built images containing the fix. Like other distributors, Chainguard had received the patch in advance so its users could update the moment the vulnerabilities were disclosed. Any attacker could now study the fix in binary form while every other PHP user was still waiting for the release. This disregarded weeks of work by many parties toward a coordinated disclosure.”

### Chainguard CEO: 'We made the call'

Chainguard CEO Dan Lorenc spoke with The Register on Wednesday, and while he doesn’t dispute the timeline, said his company "didn't leak."

“These things are messy,” Lorenc said.

Chainguard learned “something was coming in PHP” on Friday from one of the researchers that found the bugs, Lorenc told us. Later that night, using his company’s AI harness and a frontier model, the CEO and the Chainguard team independently found the same memory corruption vulnerabilities.

All it took was a “basic prompt of ‘find bad vulnerabilities in PHP,’” Lorenc [wrote](https://www.linkedin.com/feed/update/urn:li:activity:7518756994284077056/) in a subsequent LinkedIn post.

On Saturday, Chainguard began working with the PHP maintainers, confirmed that some of its findings matched the bug reports, and helped test the patches.

“The patches are crazy - this is not a simple vulnerability,” Lorenc told The Register. “It really did take them months to build a real, working patch for it. And then on Monday, the rumors started, and yesterday it just spiraled.”

Some people published POCs on social media, other security vendors reported seeing real-world exploitation, and late Tuesday night Lorenc told us he decided to ship the fixes, and notified the PHP coordinated disclosure channel about his plans.

“People were getting hit in advance” of the official PHP disclosure, “so we made the call to ship the fixes under that,” Lorenc said. “It's coordinated vulnerability disclosure, unless there's evidence of active exploits in the wild.”

Also on Tuesday night, Chainguard published built artifacts and made them accessible to anyone, not just customers. “And then I woke up this morning and saw that this was all our fault,” Lorenc said.

When asked if he would do anything differently, given the fallout from Chainguard’s early disclosure, Lorenc said no. “This process and policy is based on trying to coordinate as much as possible until shit hits the fan and people start weaponizing things,” he said. “It sucks, because we really are all on one team, and there's bad guys over there doing stuff.”

Chainguard’s honeypots trapped IPs from China and Russia targeting the vulnerabilities on Wednesday, Lorenc added.

“Just being told there's a vulnerability in a piece of software - even something as big as PHP - is enough to find it,” he told us. “I did that myself without any other knowledge on Friday."

"I think this is kind of the new normal. People are able to build an exploit in hours without even knowing what the vulnerability is."

### What we know about the CVEs and how to exploit them

While we still don’t know the scope of exploitation - or what will happen to vulnerable legacy systems that don’t have security fixes - threat hunters predict it’s going to be a doozy.

“Successful exploitation could allow attackers to take control of affected servers, steal sensitive data, and deface the websites running on them,” Wiz researchers Sagi Tzadik, Shir Tamari, Nir Ohfeld, and Tomer Schwartz warned on Wednesday, adding the oft-quoted stat that PHP powers 70 percent of all websites in the world.

“Every PHP version released in the last decade is affected by at least one of these vulnerabilities, going back to version 5.4,” the Wiz kids wrote. “Attackers can exploit them remotely, in some cases fairly easily. Immediate patching is strongly advised.”

Both bugs are related to how PHP handles memory management and error handling, and both lead to remote code execution (RCE). They can cause a corrupted internal PHP state when a request ends unexpectedly, and then a later request can reuse that state, leading to memory disclosure or RCE.

“Both are memory corruption vulnerabilities,” VulnCheck researcher Patrick Garrity explained. “If an attacker can shape the memory PHP trusts, they can potentially hijack what it does next, and in these cases that means remote code execution.”

CVE-2026-109618 ([GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)) leads to RCE via out-of-memory corruption. “If a request reached PHP's memory\_limit at exactly the wrong moment, PHP could leave partially initialized internal data behind and later treat it as valid, corrupting memory,” the project maintainer wrote. “On Apache with mod\_php, an unauthenticated request can trigger this before any application code runs.”

CVE-2026-109619 ([GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)) allows RCE via stale state. “A fatal error at the wrong point could leave internal state pointing to memory that belonged to a previous request,” according to the PGP Foundation. “A later request handled by the same worker could then use that freed memory. A use-after-free and worker crash were confirmed, and the reporter demonstrated remote code execution against a real-world application running on Apache with mod\_php.”®

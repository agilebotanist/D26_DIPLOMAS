
**Threat actors have been exploiting PHP2Shell vulnerabilities to hack Check Point Gateway appliances and deploy a wiper against victim organizations, Check Point reports.**

The attacks unfolded in two waves. An initial, destructive round started on October 30 and targeted Israeli organizations, and a second one started on November 2, targeting organizations across multiple countries.

[PHP2Shell](https://www.securityweek.com/topics/php2shell/), tracked as CVE-2026-109618 and CVE-2026-109619, refers to two critical vulnerabilities leading to remote code execution (RCE) and affecting all PHP versions from PHP 5 onwards. They were patched on October 21, but exploitation started [days before patches](https://www.securityweek.com/php2shell-exploitation-started-days-before-patches/) and [mass exploitation](https://www.securityweek.com/php2shell-exploitation-moves-from-probes-to-working-shells/) shortly after.

Dream has linked attacks targeting PHP2Shell to [root Palo Alto Networks firewalls](https://www.securityweek.com/php2shell-attacks-root-palo-alto-firewalls-but-fail-against-wordpress/) to Chinese hackers, and the hackers targeting Check Point gateways have left a note mentioning the cybersecurity firm.

As part of the [Check Point campaign](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/), the attackers exploited PHP2Shell for initial access, then targeted [CVE-2026-123039](https://support.checkpoint.com/results/sk/sk1000362), a local privilege escalation in the DynamicCLI process, to gain root access and deploy PHP webshells and establish persistence.

In late October, the attackers targeted Check Point Mobile Access gateways across multiple Israeli organizations. They placed PHP webshells in a directory the Mobile Access portal uses to construct login pages, allowing them to send commands and establish a stronger foothold on the environment.

Advertisement. Scroll to continue reading.

Next, they deployed TSGA and TSProxy, variants of the malware framework PhiliKit previously [seen](https://web-assets.esetstatic.com/wls/en/papers/threat-reports/eset-apt-activity-report-q4-2025-q1-2026.pdf) (PDF) in China-linked [UNC5221](https://www.securityweek.com/chinese-apt-exploited-beyondtrust-vulnerability-as-zero-day/) ’s hacking into Ivanti products, for backdoor access and network function interception.

The attackers followed up with internal asset discovery, then moved laterally to a VMware ESXi host where they deployed and executed a wiper, and then deployed a note mentioning Dream Security.

According to Check Point, the hackers operated during typical Chinese working hours. Despite this and the use of China-linked malware and infrastructure, the use of a wiper and the destructive nature of the attacks do not align with known Chinese cyber operations.

“Taken together, the evidence does not allow us to assess with high confidence the true nature of this operation. Several scenarios remain plausible: the identified actor ran the entire campaign, acted solely as an initial access broker, or took part in a false-flag operation. It is also possible that the destructive activity served as a smoke screen,” Check Point says.

The second wave targeted Check Point Security Gateways across organizations worldwide, including some Israeli entities targeted in the first wave. No destructive activity was observed during this second wave.

“Neither wave showed a clear sector preference, suggesting opportunistic initial-access attempts rather than sector-specific targeting,” Check Point notes.

**Related:** [Hackers Exploit New N-central Zero-Day Hours After PoC Publication](https://www.securityweek.com/hackers-exploit-new-n-central-zero-day-hours-after-poc-publication/)

**Related:** [Hackers Target N-central Zero-Days as N-able Rushes Patches](https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches/)

**Related:** [Recently Patched Barracuda Vulnerabilities Exploited in Attacks](https://www.securityweek.com/recently-patched-barracuda-vulnerabilities-exploited-in-attacks/)

**Related:** [Threat Actors Exploit Openwave, Cisco BroadWorks Vulnerabilities](https://www.securityweek.com/threat-actors-exploit-openwave-cisco-broadworks-vulnerabilities/)

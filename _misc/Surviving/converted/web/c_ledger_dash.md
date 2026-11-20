Scraping: https://red.anthropic.com/2026/cvd/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://red.anthropic.com/2026/cvd/
  Settled (dom-quiet, 1836ms)
  Extracting content...
  Extracted 21757 characters

--- Content ---

Last updated 2026-11-02 19:30 UTC.

Anthropic uses Claude models, including an early snapshot of Claude Mythos Preview, to find security vulnerabilities in open-source software. We partner with external security research firms to triage findings, validate them, and report human-reviewed vulnerabilities, prioritizing critical- and high-severity ones, to the software's maintainers under our [Coordinated Vulnerability Disclosure policy](https://www.anthropic.com/coordinated-vulnerability-disclosure). This page tracks the findings that we've disclosed, and, in line with our policy, publishes details of the ones whose disclosure window has now closed.

As of November 2, 2026, we've disclosed 5,087 vulnerabilities across 680 open source projects. To our knowledge, 629 of these have been patched. Across all findings in the ledger, 733 identifiers have been issued: 230 CVE records and 503 GitHub Security Advisories (a single finding may carry both). In other cases, maintainers have shipped a fix without publishing an advisory. The number of vulnerabilities we've disclosed is a subset of the total number of vulnerabilities that Mythos Preview (and other Claude models) has found, since the process of independent human triage and review is the rate limiting step.

This page covers a headline count of the vulnerabilities we've disclosed. For those vulnerabilities we've disclosed and where the disclosure window has now closed, it also includes identifier records (CVE & GHSA) and finding details, further below.

Finally, it includes a disclosure ledger. The ledger lists hash commitments for findings we have reported or plan to report. The details we publish later can be checked against them.

Assessed by

Severity

Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.

The date range filters by discovery date and combines with the severity selection. The flowchart, the disclosure ledger, the identifier records, and the severity-agreement heatmap reflect findings discovered in the selected window.

Discovered Triaged [37,966 findings Candidates](#ledger) [6,376 findings Reviewed by external security firms](#ledger) [6,009 findings Confirmed valid 94.2% true positives of 6,376](#ledger) [1,862 findings Reported to maintainers](#ledger) [3,225 findings Reported direct to maintainers by Anthropic May contain false positives](#ledger) Disclosed Remediated [5,087 findings Total reported to maintainers](#ledger) [3,635 findings Acknowledged by maintainer](#ledger) [629 findings Patched upstream](#ledger) [733 advisories CVEs and GHSAs assigned](#ledger) Counts as of November 2, 2026 [Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.")

The statistics above reflect all bugs found by Claude Mythos Preview and other Claude models. They can also be filtered by severity under at least one of three assessment sources: Claude's own assessment, the assessment of the external security research firm that triaged the finding, or the project maintainer's assessment. Each source is defined in the glossary on the [About](about/index.html) page, and the filtered view states how many findings the selected sources have not assessed. These figures are designed to reflect our coordinated vulnerability disclosure process, which works approximately as follows. A glossary of the terms is available on the [About](about/index.html) page.

First, our models find candidate vulnerabilities, which we add to a list for human triage. This is the figure at the top. The count includes candidates from Mythos Preview, other Mythos-class models and other Claude models.

Then, in order to disclose a vulnerability to a maintainer, we take one of two steps.

**Triage:** We pass them to one of six external security research firms that we have engaged for this endeavor. The security research firms reproduce each issue, assess whether it is a real bug (and if so, assess how severe it is), and then write a report for confirmed bugs that will go to the project's maintainer. Importantly, there are many additional bugs that we or our security partners have investigated and confirmed are real but that we have not yet reported to maintainers, due to capacity limitations.

In our triage process, the "true positive rate" (the number of findings confirmed as valid, as a share of the number of findings manually reviewed) reflects how often the external security research firms determined that a finding Mythos Preview (and other Claude models) produced was a real vulnerability. This includes real bugs that we later discover have already been reported, and "won't fix" findings (the bug is real, but the maintainer is unlikely to address it—e.g. because it falls outside the project's threat model, or affects code that isn't typically reachable). We include these in the true positive rate because we're reliant on our security research partners (rather than maintainers) to tell us how many bugs they've confirmed, and it's only *after* the maintainers have received the report and assessed the vulnerability that we'll learn whether a vulnerability is one they plan to fix. For this reason, it's also possible that a vendor has marked a vulnerability as a true positive (or a false positive) in error. Given this, the number of "true positives" in the dashboard above should only be taken as one proxy for impact. Another, more reliable one is the number of patches created, though this is only a lagging indicator of progress, since patches take a long time to create.

**Direct disclosure:** Other vulnerabilities are disclosed to maintainers directly, without the same independent check. This also happens when maintainers specifically request that we provide them un-triaged findings.

Once bugs have either been triaged or directly disclosed, "Acknowledged by maintainer" counts all bugs whose reports maintainers have responded to. "Patched upstream" counts the reported vulnerabilities that maintainers have since created and released fixes for, whether or not they replied to the report, though this does not guarantee that those patches have been widely installed. Finally, "CVEs and GHSAs assigned" counts the CVE records and GitHub Security Advisories issued across all findings in the ledger, whether or not a patch has shipped (a finding may carry both). Some advisories are now public, and we list them out further down on this page. We leave whether to create a security advisory up to the discretion of maintainers.

See [About](about/index.html) for more information.

DISCLOSURE LEDGER [Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.")

Each entry is a SHA-3-512 hash of one finding's details. "Date committed" comes from our records. It can be earlier than the date the hash was computed or first listed here. Each ledger entry shows more detail as it progresses through disclosure: before the maintainer has been notified, only the commitment hash and the commitment date are published; once the report has been sent, the status and the severity assessments are shown and the discovery date is published (it drives the date filter); and the identifier, project, and bug class are revealed only when the disclosure window closes. A commitment that is withdrawn at any stage keeps its hash and commitment date and is marked withdrawn in the status column; a commitment withdrawn before the finding was revealed is also struck through in the table.

7,349 / 7,349 · [View full ledger →](ledger/index.html)

<table><thead><tr><th>Date committed</th><th>Hash / identifier</th><th>Project</th><th>Bug class</th><th>Severity assessments</th><th>Status</th></tr></thead><tbody><tr><td>2026-11-01</td><td colspan="3"><span>7a7d464d009b…</span></td><td>—</td><td></td></tr><tr><td>2026-10-31</td><td><span>0148f65dd05a…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>bec0fa471b37…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>a0c6e173ba36…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>a89b85f1a93f…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>1ccc14162af0…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>28847f59ae94…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>7d32ffac48b3…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>de67e0e87fc8…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr><tr><td>2026-10-31</td><td><span>1962d6104eda…</span></td><td>—</td><td>—</td><td><span>Claude: high</span> <span>Firm: high</span></td><td>disclosed</td></tr></tbody></table>

Showing 1–10 of 7349 · page 1/735

[View all 7,349 entries →](ledger/index.html)

CVEs [Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.")

Common Vulnerabilities and Exposures records assigned to findings disclosed through this program. The records below are publicly available. Identifiers not listed belong to findings whose disclosure window has not yet closed, or have not yet been published by the assigning authority.

[CVE-2026-12340](https://nvd.nist.gov/vuln/detail/CVE-2026-12340) wolfssl/wolfssl · oob-read · low · [ANT-2026-87DJGDRB](findings/ANT-2026-87DJGDRB.html) Heap-buffer-overflow in sha.c:733

[CVE-2026-13595](https://nvd.nist.gov/vuln/detail/CVE-2026-13595) util-linux/util-linux · use-after-free · medium · [ANT-2026-ZRDQDR79](findings/ANT-2026-ZRDQDR79.html) Heap-use-after-free in blkid\_partition\_get\_start at partitions.c:1447 via nested BSD disklabel in DOS partition table

[CVE-2026-15165](https://nvd.nist.gov/vuln/detail/CVE-2026-15165) wireshark/wireshark · oob-write · medium · [ANT-2026-Y5M37QY4](findings/ANT-2026-Y5M37QY4.html) TLS ECH transcript reconstruction heap overflow

[CVE-2026-15166](https://nvd.nist.gov/vuln/detail/CVE-2026-15166) wireshark/wireshark · oob-write · medium · [ANT-2026-WT5AMKP5](findings/ANT-2026-WT5AMKP5.html) 802.11 EAPOL key-data decryption stack buffer overflow

[CVE-2026-15170](https://nvd.nist.gov/vuln/detail/CVE-2026-15170) wireshark/wireshark · oob-write · medium · [ANT-2026-3FWTCMVC](findings/ANT-2026-3FWTCMVC.html) Z39.50 MARC directory count floor/ceil mismatch overflow

[CVE-2026-19694](https://nvd.nist.gov/vuln/detail/CVE-2026-19694) wireshark/wireshark · oob-write · medium · [ANT-2026-EKGJXN5A](findings/ANT-2026-EKGJXN5A.html) TTL reader fixed-offset write into undersized buffer

[CVE-2026-20213](https://nvd.nist.gov/vuln/detail/CVE-2026-20213) cisco-talos/clamav · integer-error · high · [ANT-2026-VVPEMVDE](findings/ANT-2026-VVPEMVDE.html) Integer overflow in PE rebuild section size summation in Aspack unpacker

[CVE-2026-20214](https://nvd.nist.gov/vuln/detail/CVE-2026-20214) cisco-talos/clamav · integer-error · high · [ANT-2026-Z477W54M](findings/ANT-2026-Z477W54M.html) Unsigned integer underflow in FSG unpacker section loop

[CVE-2026-20215](https://nvd.nist.gov/vuln/detail/CVE-2026-20215) cisco-talos/clamav · oob-write · high · [ANT-2026-8DRZW7VM](findings/ANT-2026-8DRZW7VM.html) Integer overflow in 7z SubStreams count leading to heap buffer overflow

[CVE-2026-26980](https://nvd.nist.gov/vuln/detail/CVE-2026-26980) tryghost/ghost · query-injection · critical · [ANT-2026-69D8H6RP](findings/ANT-2026-69D8H6RP.html) Critical Vulnerability (CVSS 9.1): SQLi from unauthenticated user; arbitrary DB reads

Page 1 of 10

GHSAs [Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.")

GitHub Security Advisory records assigned to findings disclosed through this program. The records below are publicly available. Identifiers not listed belong to findings whose disclosure window has not yet closed, or have not yet been published by the assigning authority.

[GHSA-3q2h-7599-7r76](https://github.com/advisories/GHSA-3q2h-7599-7r76) wireshark/wireshark · oob-write · medium · [ANT-2026-Y5M37QY4](findings/ANT-2026-Y5M37QY4.html) TLS ECH transcript reconstruction heap overflow

[GHSA-425r-vwq2-26qv](https://github.com/advisories/GHSA-425r-vwq2-26qv) libexpat/libexpat · oob-write · medium · [ANT-2026-X3EB6DN3](findings/ANT-2026-X3EB6DN3.html) Heap-buffer-overflow in doProlog at xmlparse.c:5957 via deeply nested DTD with external entity interaction

[GHSA-44h9-v855-6rj3](https://github.com/CESNET/libyang/security/advisories/GHSA-44h9-v855-6rj3) cesnet/libyang · oob-write · high · [ANT-2026-573F8CSS](findings/ANT-2026-573F8CSS.html) Stack buffer overflow storing LYB integer values

[GHSA-47qf-hp3h-rwmm](https://github.com/advisories/GHSA-47qf-hp3h-rwmm) wolfssl/wolfssl · authenticity-not-verified · high · [ANT-2026-KNXJMVYC](findings/ANT-2026-KNXJMVYC.html) Universal ECCSI signature forgery in wolfSSL wc\_VerifyEccsiHash via r = 0, s = 0

[GHSA-589g-qgf8-m6mx](https://github.com/asterisk/asterisk/security/advisories/GHSA-589g-qgf8-m6mx) asterisk/asterisk · oob-write · critical · [ANT-2026-HFGGE6HR](findings/ANT-2026-HFGGE6HR.html) Stack buffer overflow in parse\_simple\_message\_summary via unbounded sscanf %s (SIP MWI NOTIFY)

[GHSA-59q6-j4w8-8pjx](https://github.com/OISF/suricata/security/advisories/GHSA-59q6-j4w8-8pjx) oisf/suricata · use-after-free · high · [ANT-2026-WCSVRYAX](findings/ANT-2026-WCSVRYAX.html) heap-use-after-free in suricata

[GHSA-5jqq-xpcr-q3r7](https://github.com/advisories/GHSA-5jqq-xpcr-q3r7) wolfssl/wolfssl · oob-write · low · [ANT-2026-6615Y595](findings/ANT-2026-6615Y595.html) Final Assessment: 2-Byte Heap Overflow in wolfSSL\_X509\_notAfter / wolfSSL\_X509\_notBefore

[GHSA-65xm-pfx9-g5p3](https://github.com/advisories/GHSA-65xm-pfx9-g5p3) wolfssl/wolfssl · oob-write · medium · [ANT-2026-0JRYQPCF](findings/ANT-2026-0JRYQPCF.html) wolfSSL ECH: heap buffer overflow in TLSX\_EchChangeSNI via publicName SNI pollution

[GHSA-6gff-7f37-2v35](https://github.com/advisories/GHSA-6gff-7f37-2v35) cisco-talos/clamav · oob-write · high · [ANT-2026-8DRZW7VM](findings/ANT-2026-8DRZW7VM.html) Integer overflow in 7z SubStreams count leading to heap buffer overflow

[GHSA-72j9-356v-88xq](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-72j9-356v-88xq) freerdp/freerdp · oob-write · high · [ANT-2026-EWM7B5QP](findings/ANT-2026-EWM7B5QP.html) Opus audio decode resizes wrong stream, overflows output

Page 1 of 7

SEVERITY AGREEMENT [Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.](#filters "Showing all assessment sources and severities for findings discovered between November 1, 2025 and November 2, 2026.")

This graph compares Claude's initial severity assessments against the external security research firms' assessments, for those findings that have completed triage. Cells on the diagonal indicate agreement. The number assessed here represents the subset of vulnerabilities included on our disclosure ledger that were reviewed by our security partners, rather than disclosed by us directly.

<svg viewBox="0 0 316 316" width="100%" xmlns="http://www.w3.org/2000/svg"><text x="196.0" y="10" text-anchor="middle"><tspan x="196.0">External security research</tspan> <tspan x="196.0" dy="12">firm-assessed</tspan></text> <text x="14" y="196.0" text-anchor="middle" transform="rotate(-90 14 196.0)">Claude-assessed</text> <text x="78" y="116.0" text-anchor="end">critical</text> <rect x="84" y="84" width="56" height="56" data-count="170" fill="rgba(204,0,0,0.21)"><title>Claude-assessed critical vs external security research firm-assessed critical: 170</title></rect> <text x="112.0" y="116.0" text-anchor="middle">170</text> <rect x="140" y="84" width="56" height="56" data-count="110" fill="rgba(204,0,0,0.16)"><title>Claude-assessed critical vs external security research firm-assessed high: 110</title></rect> <text x="168.0" y="116.0" text-anchor="middle">110</text> <rect x="196" y="84" width="56" height="56" data-count="8" fill="rgba(204,0,0,0.09)"><title>Claude-assessed critical vs external security research firm-assessed medium: 8</title></rect> <text x="224.0" y="116.0" text-anchor="middle">8</text> <rect x="252" y="84" width="56" height="56" data-count="14" fill="rgba(204,0,0,0.09)"><title>Claude-assessed critical vs external security research firm-assessed low: 14</title></rect> <text x="280.0" y="116.0" text-anchor="middle">14</text> <text x="78" y="172.0" text-anchor="end">high</text> <rect x="84" y="140" width="56" height="56" data-count="14" fill="rgba(204,0,0,0.09)"><title>Claude-assessed high vs external security research firm-assessed critical: 14</title></rect> <text x="112.0" y="172.0" text-anchor="middle">14</text> <rect x="140" y="140" width="56" height="56" data-count="1079" fill="rgba(204,0,0,0.90)"><title>Claude-assessed high vs external security research firm-assessed high: 1079</title></rect> <text x="168.0" y="172.0" text-anchor="middle">1079</text> <rect x="196" y="140" width="56" height="56" data-count="23" fill="rgba(204,0,0,0.10)"><title>Claude-assessed high vs external security research firm-assessed medium: 23</title></rect> <text x="224.0" y="172.0" text-anchor="middle">23</text> <rect x="252" y="140" width="56" height="56" data-count="12" fill="rgba(204,0,0,0.09)"><title>Claude-assessed high vs external security research firm-assessed low: 12</title></rect> <text x="280.0" y="172.0" text-anchor="middle">12</text> <text x="78" y="228.0" text-anchor="end">medium</text> <rect x="84" y="196" width="56" height="56" data-count="2" fill="rgba(204,0,0,0.08)"><title>Claude-assessed medium vs external security research firm-assessed critical: 2</title></rect> <text x="112.0" y="228.0" text-anchor="middle">2</text> <rect x="140" y="196" width="56" height="56" data-count="33" fill="rgba(204,0,0,0.11)"><title>Claude-assessed medium vs external security research firm-assessed high: 33</title></rect> <text x="168.0" y="228.0" text-anchor="middle">33</text> <rect x="196" y="196" width="56" height="56" data-count="367" fill="rgba(204,0,0,0.36)"><title>Claude-assessed medium vs external security research firm-assessed medium: 367</title></rect> <text x="224.0" y="228.0" text-anchor="middle">367</text> <rect x="252" y="196" width="56" height="56" data-count="2" fill="rgba(204,0,0,0.08)"><title>Claude-assessed medium vs external security research firm-assessed low: 2</title></rect> <text x="280.0" y="228.0" text-anchor="middle">2</text> <text x="78" y="284.0" text-anchor="end">low</text> <rect x="84" y="252" width="56" height="56" data-count="3" fill="rgba(204,0,0,0.08)"><title>Claude-assessed low vs external security research firm-assessed critical: 3</title></rect> <text x="112.0" y="284.0" text-anchor="middle">3</text> <rect x="140" y="252" width="56" height="56" data-count="0" fill="rgba(204,0,0,0.00)"><title>Claude-assessed low vs external security research firm-assessed high: 0</title></rect> <rect x="196" y="252" width="56" height="56" data-count="4" fill="rgba(204,0,0,0.08)"><title>Claude-assessed low vs external security research firm-assessed medium: 4</title></rect> <text x="224.0" y="284.0" text-anchor="middle">4</text> <rect x="252" y="252" width="56" height="56" data-count="27" fill="rgba(204,0,0,0.10)"><title>Claude-assessed low vs external security research firm-assessed low: 27</title></rect> <text x="280.0" y="284.0" text-anchor="middle">27</text> <text x="112.0" y="76" text-anchor="middle">critical</text> <text x="168.0" y="76" text-anchor="middle">high</text> <text x="224.0" y="76" text-anchor="middle">medium</text> <text x="280.0" y="76" text-anchor="middle">low</text></svg>

Claude-assessed (rows) against external security research firm-assessed (columns), n = 1868. 88.0% exact agreement, 97.9% within one band.

Anthropic's severity assessments are produced before any maintainer input. Project maintainers often apply project-specific severity rules that Claude does not have access to at run time, so what one maintainer rates as critical another may rate as low. The external security research firms incorporate that context, which is why their assessments tend to be lower.

PROVENANCE

This snapshot was generated on 2026-11-02 19:30 UTC. The manifest hash below is the SHA-3-512 hash of the structured payload and is republished with every dated snapshot so any figure on this page can be verified against the [machine-readable record](data/payload.json).

Revision 40 · checksum 25d811e7b56632ef5bbb23eb25f82a46ebe97446ce2b5d3d2b1a17dc556dac9496752a21b063ebfb4d822074e621ae109af6b97aca35762cacc8c960d868e23f

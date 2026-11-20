Scraping: https://www.first.org/blog/20260211-vulnerability-forecast-2026
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.first.org/blog/20260211-vulnerability-forecast-2026
  Settled (dom-quiet, 2004ms)
  Extracting content...
  Extracted 12323 characters

--- Content ---

![Yearly Vulnerability Forecast](_media/20260211-01.png)

Yearly Vulnerability Forecast

**Happy New Year 2026!**

As we turn the page on another year and raise our glasses to new beginnings, we at FIRST have been busy doing what we do best: thinking quantitatively about what lies ahead. And our forecast for 2026 is both sobering and, we hope, useful.

**Our prediction: 2026 will be the year we cross 50,000 published CVEs.**

In fact, our median forecast sits at approximately **59,000 vulnerabilities** for the year—a number that should give pause to anyone responsible for patch management, detection engineering, or coordinated vulnerability disclosure.

## The Three-Year Outlook

| Year | Median Forecast | Lower 90% CI | Upper 90% CI |
| --- | --- | --- | --- |
| 2026 | 59,427 | 30,012 | 117,673 |
| 2027 | 51,018 | 18,765 | 138,703 |
| 2028 | 53,289 | 14,714 | 192,993 |

While our central estimate for 2026 hovers around 59,000, we believe it is entirely realistic that this year we reach **70,000 to 100,000 vulnerabilities**. The upper bound of our 90% confidence interval sits at nearly 118,000—a number that would represent a paradigm shift in vulnerability management workloads. We think it is more likely to be closer to 60k, but it is important that we prepare for more extreme scenarios such as 70 or 80k as well.

## Why Forecast Vulnerabilities?

These forecasts are not an exercise in academic curiosity. They exist to help us **prepare our patch and signature writing capabilities and capacities** for the year ahead.

Whether you are:

- **Planning patching capacity** across your organisation's fleet
- **Writing coordinated vulnerability disclosure reports** as a researcher or vendor
- **Developing detection signatures** for your SIEM, EDR, or IDS platforms

...it helps to think about capacity at this time of year. Much like a city planner considering population growth before commissioning new infrastructure, security teams benefit from understanding the likely volume and shape of vulnerabilities they will need to process in the coming year. So ask yourself, are my people and processes ready to handle the 50k of CVEs next year?

## What Makes a Good Vulnerability Forecast?

We believe a forecast worth its salt should embody several principles:

**Be quantified, with confidence intervals.** A single point estimate is almost useless for planning. Our forecast includes ranges precisely because the range is more important than the mean. It is the range that helps us plan for a spectrum of possible outcomes throughout the year. The difference between preparing for 30,000 vulnerabilities and 100,000 is not merely operational—it is strategic.

**Aid decision making and capacity planning.** A forecast should incorporate uncertain factors honestly. We don't pretend to have a crystal ball, but we do have statistical models that capture the fundamental uncertainty in vulnerability publication rates. Giving you realistic sense of the range of possibilities is more important than precision of the number.

**Get into the details.** Aggregate counts are a starting point, but a truly useful forecast should eventually decompose into vendor, product, and CVSS vector breakdowns. These details become actionable when paired with good asset registers—if you know you run a lot of Microsoft Exchange, a forecast weighted by vendor exposure is considerably more useful than a raw count. There’s no reason you can’t train up someone in your team to do forecasting, time series analysis tools and models are easily explored in this vibecoding era.

**Respect that the risks of your readers differ from each other.** Your asset priorities, your threat landscape, and your risk appetite are unique. A good forecast should allow you to re-prioritise based on your own circumstances while still providing enough information to support strategic decisions in the boardroom.

**Be reviewed for accuracy.** We hold ourselves accountable. Our 2025 forecast achieved a MAPE of 7.48% for the yearly prediction and 4.96% for Q4—results we are proud of, and results that give us confidence in the methodology underpinning this year's projections.

**We’re using a new model** Within the vulnerability forecasting community, it’s widely accepted that 2017 was the toughest year to forecast. It marks a new epoch, and one where the upward trends of CVE publication can be much larger. Many people believe we should only include data from after 2017 in our models, because of this change in structural CVE data. We’ve chosen a model that includes it and accounts for it to allow us more realistic prediction intervals. In other words we chose to optimise our forecasts to reflect the range of possibilities instead of the accuracy of the point prediction. Of course, we also needed to back test the model to see how it performs, and you can see that below. Please note, this is the performance of the new model and NOT the accuracy of all our previous blog posts. In short, we’re willing to let the model be wrong up to 2018, in training exercises so it can more realistically reflect possible outcomes of 2026.

![Prediction Interval Coverage Check](_media/20260211-02.png)

Prediction Interval Coverage Check

We’ve included those testing results here, and it really does perform better for every year after that epoch change in 2017-18. It gives asymmetric confidence intervals too, which is realistic, we’re more likely to be above the median than below it, because CVEs just seem to be growing.

## What's Coming Next

Throughout 2026, we will publish **quarterly forecast updates** that refine our predictions as new data arrives. These updates will begin to incorporate more granular analysis, including expected **CVSS v3 vector distributions** amongst the CVEs we anticipate. Understanding not just *how many* vulnerabilities but *what kind* —their attack vectors, complexity, and impact profiles—will further sharpen capacity planning efforts.

## Preparing for Uncertainty

The widening confidence intervals as we look further into the future (note how 2028's upper bound approaches 193,000) remind us that forecasting is not about predicting the future with certainty. It is about preparing for a range of plausible futures. Like the branching of a great oak, the further out we look, the more paths remain possible.

Here's to a year of thoughtful preparation, rigorous analysis, and—we hope—fewer surprises than there might otherwise have been.

*From all of us at FIRST, happy 2026!*

### FIRST Blog

FIRST runs a blog open to members and invited guest authors. It publishes contributions relevant to incident responders. Articles should focus on general topics interesting to members. It will not be used to promote individual organisations, products or services. If you are interested in contributing, please get in touch with [first-blog@first.org](mailto:first-blog@first.org).

Learn more about the Forum of Incident Response and Security Teams through regular blog posts about our organization, events and other programs. Questions or comments? Contact [first-press@first.org](mailto:first-press@first.org).

[A4](about:/blog/#a4) [Abuse](about:/blog/#abuse) [Africa](about:/blog/#africa) [AI](about:/blog/#ai) [alert](about:/blog/#alert) [Amsterdam](about:/blog/#amsterdam) [Anniversary](about:/blog/#anniversary) [APAC](about:/blog/#apac) [APNIC](about:/blog/#apnic) [APT](about:/blog/#apt) [ARL](about:/blog/#arl) [Asia](about:/blog/#asia) [attack](about:/blog/#attack) [Balkans](about:/blog/#balkans) [Bangalore](about:/blog/#bangalore) [board](about:/blog/#board) [Board of Directors](about:/blog/#board-of-directors) [CCB](about:/blog/#ccb) [CERT](about:/blog/#cert) [CERT Tonga](about:/blog/#cert-tonga) [certificate](about:/blog/#certificate) [CIRT](about:/blog/#cirt) [clustering](about:/blog/#clustering) [collaboration](about:/blog/#collaboration) [Comms Lens](about:/blog/#comms-lens) [Communications SIG](about:/blog/#communications-sig) [community](about:/blog/#community) [Conference](about:/blog/#conference) [Conferences](about:/blog/#conferences) [Consumer](about:/blog/#consumer) [cryptography](about:/blog/#cryptography) [CSIRT](about:/blog/#csirt) [CSIRT Maturity](about:/blog/#csirt-maturity) [CTI 2026](about:/blog/#cti-2026) [cvd](about:/blog/#cvd) [CVE](about:/blog/#cve) [cvss](about:/blog/#cvss) [cyber](about:/blog/#cyber) [Cyber norms](about:/blog/#cyber-norms) [Cybersecurity](about:/blog/#cybersecurity) [Data Protection](about:/blog/#data-protection) [defense](about:/blog/#defense) [Denver](about:/blog/#denver) [DNS](about:/blog/#dns) [DNS Abuse](about:/blog/#dns-abuse) [doa](about:/blog/#doa) [Error](about:/blog/#error) [ethics](about:/blog/#ethics) [Events](about:/blog/#events) [Facebook](about:/blog/#facebook) [Factors](about:/blog/#factors) [Fellows](about:/blog/#fellows) [file similarity](about:/blog/#file-similarity) [FIRST](about:/blog/#first) [first-tech](about:/blog/#first-tech) [FIRSTCON](about:/blog/#firstcon) [FIRSTCON26](about:/blog/#firstcon26) [forecast](about:/blog/#forecast) [forecasting](about:/blog/#forecasting) [Framework](about:/blog/#framework) [GCSC](about:/blog/#gcsc) [GDPR](about:/blog/#gdpr) [Geneva. Cyber Week](about:/blog/#geneva-cyber-week) [Ghana](about:/blog/#ghana) [Google](about:/blog/#google) [human](about:/blog/#human) [ICANN](about:/blog/#icann) [IGF](about:/blog/#igf) [incident](about:/blog/#incident) [Incident Response](about:/blog/#incident-response) [infrastructure](about:/blog/#infrastructure) [insights](about:/blog/#insights) [inteligence](about:/blog/#inteligence) [Internet Governance](about:/blog/#internet-governance) [ioc](about:/blog/#ioc) [ISP](about:/blog/#isp) [keynote](about:/blog/#keynote) [Latam](about:/blog/#latam) [loa](about:/blog/#loa) [Malware](about:/blog/#malware) [management](about:/blog/#management) [Matrix](about:/blog/#matrix) [maturity](about:/blog/#maturity) [Mexico](about:/blog/#mexico) [Microsoft](about:/blog/#microsoft) [Multi-Stakeholder](about:/blog/#multi-stakeholder) [Munich](about:/blog/#munich) [NatCSIRT](about:/blog/#natcsirt) [NCSC](about:/blog/#ncsc) [Netherlands](about:/blog/#netherlands) [Networks](about:/blog/#networks) [Open Source](about:/blog/#open-source) [OSV](about:/blog/#osv) [Outreach](about:/blog/#outreach) [Oxford](about:/blog/#oxford) [Pacific](about:/blog/#pacific) [Paris](about:/blog/#paris) [Patch Tuesday](about:/blog/#patch-tuesday) [Philippines](about:/blog/#philippines) [planning](about:/blog/#planning) [Policy](about:/blog/#policy) [Policymakers](about:/blog/#policymakers) [printNightmare](about:/blog/#printnightmare) [Privacy](about:/blog/#privacy) [Product Security](about:/blog/#product-security) [Proxy](about:/blog/#proxy) [psirt](about:/blog/#psirt) [ransom](about:/blog/#ransom) [Ransomware](about:/blog/#ransomware) [Regional](about:/blog/#regional) [Residential Vulnerability](about:/blog/#residential-vulnerability) [San Juan](about:/blog/#san-juan) [Scottsdale](about:/blog/#scottsdale) [SE Asia](about:/blog/#se-asia) [Secureworks](about:/blog/#secureworks) [Security](about:/blog/#security) [Security Analytics](about:/blog/#security-analytics) [Serbia](about:/blog/#serbia) [services](about:/blog/#services) [SIG](about:/blog/#sig) [similarity](about:/blog/#similarity) [SOAR](about:/blog/#soar) [stakeholders](about:/blog/#stakeholders) [Strategy](about:/blog/#strategy) [SY Fellowship](about:/blog/#sy-fellowship) [Symposium](about:/blog/#symposium) [T3](about:/blog/#t3) [tactical intelligence](about:/blog/#tactical-intelligence) [targets](about:/blog/#targets) [TC](about:/blog/#tc) [Technical Colloquium](about:/blog/#technical-colloquium) [threat](about:/blog/#threat) [threat campaigns](about:/blog/#threat-campaigns) [threat context](about:/blog/#threat-context) [Threat hunting](about:/blog/#threat-hunting) [Threat intelligence](about:/blog/#threat-intelligence) [tools](about:/blog/#tools) [Training](about:/blog/#training) [trends](about:/blog/#trends) [UNGGE](about:/blog/#ungge) [velociraptor](about:/blog/#velociraptor) [volunteer](about:/blog/#volunteer) [Volunteers](about:/blog/#volunteers) [VulnCon 2026](about:/blog/#vulncon-2026) [vulnerabilities](about:/blog/#vulnerabilities) [vulnerability](about:/blog/#vulnerability) [WHOIS](about:/blog/#whois) [Women](about:/blog/#women)

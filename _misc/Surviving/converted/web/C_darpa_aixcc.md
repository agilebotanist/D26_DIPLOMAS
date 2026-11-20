Scraping: https://www.darpa.mil/news/2025/aixcc-results
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.darpa.mil/news/2025/aixcc-results
  Settled (dom-quiet, 1889ms)
  Extracting content...
  Extracted 8550 characters

--- Content ---

##### Aug. 8, 2025

A cyber reasoning system (CRS) designed by Team Atlanta is the winner of the DARPA AI Cyber Challenge (AIxCC), a two-year, first-of-its-kind competition in collaboration with the Advanced Research Projects Agency for Health (ARPA-H) and frontier labs. Competitors successfully demonstrated the ability of novel autonomous systems using AI to secure the open-source software that underlies critical infrastructure.

Numerous attacks in recent years have illuminated the ability for malicious cyber actors to exploit vulnerable software that runs everything from financial systems and public utilities to the health care ecosystem.

“AIxCC exemplifies what DARPA is all about: rigorous, innovative, high-risk and high-reward programs that push the boundaries of technology. By releasing the cyber reasoning systems open source — four of the seven today — we are immediately making these tools available for cyber defenders,” said [DARPA Director Stephen Winchell.](/about/people/stephen-winchell) “Finding vulnerabilities and patching codebases using current methods is slow, expensive, and depends on a limited workforce – especially as adversaries use AI to amplify their exploits. AIxCC-developed technology will give defenders a much-needed edge in identifying and patching vulnerabilities at speed and scale.”

To further accelerate adoption, DARPA and ARPA-H are adding $1.4 million in prizes for the competing teams to integrate AIxCC technology into real-world critical infrastructure- relevant software.

“The success of today’s AIxCC finalists demonstrates the real-world potential of AI to address vulnerabilities in our health care system,” said ARPA-H Acting Director Jason Roos. “ARPA-H is committed to supporting these teams to transition their technologies and make a meaningful impact in health care security and patient safety.”

![Team Atlanta comprises experts from Georgia Tech, Samsung Research, the Korea Advanced Institute of Science & Technology (KAIST), and the Pohang University of Science and Technology (POSTECH).](/sites/default/files/gallery/2025-08/aixcc-afc-podium-atlanta-wins.jpg)

Team Atlanta comprises experts from Georgia Tech, Samsung Research, the Korea Advanced Institute of Science & Technology (KAIST), and the Pohang University of Science and Technology (POSTECH).

**Team Atlanta** comprises experts from Georgia Tech, Samsung Research, the Korea Advanced Institute of Science & Technology (KAIST), and the Pohang University of Science and Technology (POSTECH).

**Trail of Bits,** a New York City-based small business, won second place, and **Theori**, comprising AI researchers and security professionals in the U.S. and South Korea, won third place.

The top three teams will receive $4 million, $3 million, and $1.5 million, respectively, for their performance in the Final Competition.

All seven competing teams, including teams **all\_you\_need\_is\_a\_fuzzing\_brain, Shellphish, 42-beyond-bug** and **Lacrosse**, worked on aggressively tight timelines to design automated systems that significantly advance cybersecurity research.

#### Deep Dive: Final Competition Findings, Highlights

In the Final Competition scored round, teams’ systems attempted to identify and generate patches for synthetic vulnerabilities across 54 million lines of code. Since the competition was based on real-world software, team CRSs could discover vulnerabilities not intentionally introduced to the competition. The scoring algorithm prioritized competitors’ performance based on the ability to create patches for vulnerabilities quickly and their analysis of bug reports. The winning team performed best at finding and proving vulnerabilities, generating patches, pairing vulnerabilities and patches, and scoring with the highest rate of accurate and quality submissions.

In total, competitors’ systems discovered 54 unique synthetic vulnerabilities in the Final Competition’s 63 challenges. Of those, they patched 43.

In the Final Competition, teams also discovered 18 real, non-synthetic vulnerabilities that are being responsibly disclosed to open source project maintainers. Of these, six were in C codebases—including one vulnerability that was discovered and patched in parallel by maintainers—and 12 were in Java codebases. Teams also provided 11 patches for real, non-synthetic vulnerabilities.

“Since the launch of AIxCC, community members have moved from AI skeptics to advocates and adopters. Quality patching is a crucial accomplishment that demonstrates the value of combining AI with other cyber defense techniques,” said [AIxCC Program Manager Andrew Carney](/about/people/andrew-carney). “What’s more, we see evidence that the process of a cyber reasoning system finding a vulnerability may empower patch development in situations where other code synthesis techniques struggle.”

Competitor CRSs proved they can create valuable bug reports and patches for a fraction of the cost of traditional methods, with an average cost per competition task of about $152. Bug bounties can range from hundreds to hundreds of thousands of dollars.

AIxCC technology has advanced significantly from the Semifinal Competition held in August 2024.In the Final Competition scored round, teams identified 86% of the competition’s synthetic vulnerabilities, an increase from 37% at semifinals, and patched 68% of the vulnerabilities identified, an increase from 25% at semifinals. In semifinals, teams were most successful in finding and patching vulnerabilities in C codebases. In finals, teams had similar success rates at finding and patching vulnerabilities across C codebases and Java codebases.

Other key competition highlights include:

- Teams submitted patches in an average of 45 minutes
- Every team identified a real-world vulnerability
- Four teams generated patches that were one line long
- Three teams scored on three different challenge tasks in a one-minute span
- One team scored for a patch that was greater than 300 lines long
- Competitors’ CRSs analyzed more than 54 million lines of code
- Teams spent about $152 per competition task

AIxCC is a collaboration between the public sector and leading AI companies. Anthropic, Google, and OpenAI provided technical support and each donated $350,000 in large language model credits – $50,000 to each team – to support CRS development for the Final Competition, in addition to $5,000 in large language model credits that Anthropic, Google, and OpenAI provided and Azure credits that Microsoft provided to each team for the Semifinal Competition. Microsoft and the Linux Foundation’s Open Source Security Foundation provided subject matter expertise to challenge organizers and participants throughout the competition.

#### Next Steps

All seven finalist teams’ CRSs will be made available as open-source software under a license approved by the Open Source Initiative. [Four teams made their CRSs available Friday](https://archive.aicyberchallenge.com/); others will be released in the coming weeks. Other competition data, to include competition framework, competition challenges, competition telemetry, and other tools and data will also be open sourced in the coming weeks to help advance the technology’s use and allow others to experiment and improve on AIxCC-developed technology.

DARPA is working with public and private sector partners, including the teams, to transition the technology to widespread use.

Anyone who maintains or develops software in critical infrastructure and wants to integrate AIxCC technology into the software development process is encouraged to contact aixcc-at-darpa-dot-mil.

To learn more about AIxCC, visit [https://www.aicyberchallenge.com](https://www.aicyberchallenge.com/).

---

**Editor's note:** A former version of this update stated the Final Competition included 70 synthetic vulnerabilities. Upon further review, the competition administrator determined the Final Competition included 63 synthetic vulnerabilities. The number of vulnerabilities competitors’ systems discovered (54) remained unchanged, which means competitors discovered 86% of the synthetic vulnerabilities and patched 68%.

The article has been updated to reflect these figures.

---

![AIxCC Cyber Challenge](/sites/default/files/gallery/2025-08/darpa-program-aixcc-feature.png)

##### Videos

![](https://www.youtube.com/watch?v=videoseries)

Watch the 32 demonstrations in this playlist. Try expanding videos to full window.

##### Office

[Information Processing Techniques Office](/about/offices/ipto)

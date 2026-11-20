Scraping: https://techcrunch.com/2025/08/04/google-says-its-ai-based-bug-hunter-found-20-security-vulnerabilities/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://techcrunch.com/2025/08/04/google-says-its-ai-based-bug-hunter-found-20-security-vulnerabilities/
  Settled (dom-quiet, 4869ms)
  Extracting content...
  Extracted 3195 characters

--- Content ---

Google’s AI-powered bug hunter has just reported its first batch of security vulnerabilities.

Heather Adkins, Google’s vice president of security, [announced](https://x.com/argvee/status/1952390039700431184) Monday that its LLM-based vulnerability researcher Big Sleep found and reported 20 flaws in various popular open source software.

Adkins said that Big Sleep, which is developed by the company’s AI department DeepMind as well as its elite team of hackers Project Zero, [reported its first-ever vulnerabilities](https://issuetracker.google.com/issues?q=componentid:1836411&s=type:desc&s=issue_id:desc&pli=1), mostly in open source software such as audio and video library FFmpeg and image-editing suite ImageMagick.

Given that the vulnerabilities are not fixed yet, we don’t have details of their impact or severity, as Google [does not yet want to provide details](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html), which is a standard policy when waiting for bugs to be fixed. But the simple fact that Big Sleep found these vulnerabilities is significant, as it shows these tools are starting to get real results, even if there was a human involved in this case.

“To ensure high quality and actionable reports, we have a human expert in the loop before reporting, but each vulnerability was found and reproduced by the AI agent without human intervention,” Google’s spokesperson Kimberly Samra told TechCrunch.

Royal Hansen, Google’s vice president of engineering, [wrote on X](https://x.com/royalhansen/status/1952424018663162235) that the findings demonstrate “a new frontier in automated vulnerability discovery.”

LLM-powered tools that can look for and find vulnerabilities [are already a reality](https://techcrunch.com/2025/07/24/ai-slop-and-fake-reports-are-exhausting-some-security-bug-bounties/). Other than Big Sleep, there’s [RunSybil](https://www.runsybil.com/) and XBOW, among others.

XBOW has garnered headlines after [it reached the top](https://xbow.com/blog/top-1-how-xbow-did-it) of one of the U.S. leaderboards at bug bounty platform HackerOne. It’s important to note that in most cases, these reports have a human at some point of the process to verify that the AI-powered bug hunter found a legitimate vulnerability, as is the case with Big Sleep.

Vlad Ionescu, co-founder and chief technology officer at RunSybil, a startup that develops AI-powered bug hunters, told TechCrunch that Big Sleep is a “legit” project, given that it has “good design, people behind it know what they’re doing, Project Zero has the bug finding experience and DeepMind has the firepower and tokens to throw at it.”

There is obviously a lot of promise with these tools, but also significant downsides. Several people who maintain different software projects have complained of [bug reports that are actually hallucinations](https://techcrunch.com/2025/07/24/ai-slop-and-fake-reports-are-exhausting-some-security-bug-bounties/), with some calling them the bug bounty equivalent of AI slop.

“That’s the problem people are running into, is we’re getting a lot of stuff that looks like gold, but it’s actually just crap,” Ionescu previously told TechCrunch.

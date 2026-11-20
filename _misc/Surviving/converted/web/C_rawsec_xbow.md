Scraping: https://blog.raw.pm/en/about-the-hype-around-xbow/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://blog.raw.pm/en/about-the-hype-around-xbow/
  Settled (dom-quiet, 1776ms)
  Extracting content...
  Extracted 7424 characters

--- Content ---

## Introduction

You have all seen the hype around XBOW: “ [the AI that climbed 1st on HackerOne leaderboard](https://xbow.com/blog/top-1-how-xbow-did-it/) ”.

![HackerOne leaderboard](/images/xbow-leaderboard.png)

HackerOne leaderboard

As often, when something new appears or a new critical vulnerability is discovered, everyone is exited and specialized journalists (or influencers) are overexaggerating to create a buzz.

In order to clarify matters, XBOW is the AI that became 1st on HackerOne **USA** leaderboard **based on reputation gain** BUT **only when you consider the April to June 2025 date range**.

XBOW achievements are impressive but not as much as social networks let you think there are.

## HackerOne reputation

XBOW is **NOT**:

- 1st on *Highest Reputation* leaderboard (neither of last 3 months / 90 days nor of all-time)
	- Ranking is calculated based on reputation earned.
- 1st on *Highest Critical Reputation* leaderboard
	- Based on reputation gain for high and critical submissions that are triaged or resolved.
- 1st based on Signal
- 1st based on Impact
- 1st of *Most Upvoted* leaderboard
	- Hackers with the highest number of report upvotes on Hacktivity.
- 1st on *USA* leaderboard of all-time
	- Based on reputation gain.
- Etc.

As said before, XBOW is 1st on HackerOne **USA** leaderboard **based on reputation gain** BUT **only when you consider the April to June 2025 date range**.

But what is [reputation](https://docs.hackerone.com/en/articles/8369865-reputation) on HackerOne?

In theory:

> Reputation measures how likely your finding is to be immediately relevant and actionable

In practice, to make it short, [reputation](https://docs.hackerone.com/en/articles/8369865-reputation) is a score that is updated when your report is closed. If your report is valid, you earn points, if your report is useless, bullshit, you didn't follow the rules, automated spam, or it's not even a vulnerability because you're too noob, you loose points.

What **is not** impressive about XBOW, is the reputation score. What **is** impressive about XBOW, is also the reputation score.

Indeed, as [reputation](https://docs.hackerone.com/en/articles/8369865-reputation) is quantitative, of course an AI agent or automated tool working 24/7 on a datacenter will earn more points because it will submit more reports. Human hunters need to sleep, eat, have a life and all the stuff. So there is nothing amazing that an AI is beating a human from this point of view.

However, [reputation](https://docs.hackerone.com/en/articles/8369865-reputation) is not only quantitative, as one will lose points for *Not Applicable* or *Spam* reports. So the challenge with automated software in this case, is to limit the false positive, so the [reputation](https://docs.hackerone.com/en/articles/8369865-reputation) won't decrease too much. Traditional automated software such as vulnerability scanners, DAST platforms and co, will often have 90% of their reports either false positive (lose points) or useless / informative (0 point) while in the same time they have 90% of false negative (not finding vulnerabilities right under their nose).

So what seems impressive in the first place with XBOW, is the very low volume of false positive, thanks to “AI training” that make it possible for it to gain a high reputation score rapidly.

## 100% automated / autonomous?

But in [their post](https://xbow.com/blog/top-1-how-xbow-did-it/), they quickly specify that HackerOne forbids automated reporting, so humans behind XBOW are reviewing 100% of the reports.

> All findings were fully automated, though our security team reviewed them pre-submission to comply with HackerOne’s policy on automated tools.

There a lot of obscurity there. As all the reports are review by XBOW human teams, they don't say what they do on the reports. Do they modify them? Do they improve them? Do they remove false positive ones?

I bet they do. I bet they remove false positive reports. So maybe in intern, the AI is spamming false positive reports that the XBOW human team is actively filtering. The only number they provide is about the closed reports and not yet triaged submissions, that means only the reports that passed XBOW human team review are counted. What about the reports that did not? What is the ratio of their internal triaging? Nobody knows…

Also, they claim:

> XBOW is a fully autonomous AI-driven penetration tester. It requires no human input, operates much like a human pentester, but can scale rapidly, completing comprehensive penetration tests in just a few hours.

To me, that is the marketing speech you serve to the investors to get the millions of dollars. But is it “fully autonomous”? Of course not, it was trained during years, tweaked, refined, is running home-made benchmark, the model is constantly reinforced all by humans. There is [a team](https://xbow.com/#team) of at least 25 security, engineering, and AI researchers behind it. And in addition to that, the manual internal triaging we talked about above.

## About AI

In general, I'm tired of hearing pentesters and hunters comment on Discord or Twitter:

> - Alice: How do you feel about people coming to the conclusion about bug hunters being “replaced”?
> - Bob: It seems we’re heading in that direction. AI can find bugs and even code their own exploits.

😱 Are we all (hunters) being replaced by AI? 😱 The recurring fear of human being replaced by its new machine (like in *Terminator* or countless other movies). I think not.

To take just one example. AI are trained on datasets produced by humans, so innovation and adaptations to new technologies and technics seem limited. We still need humans doing research, publishing their discoveries publicly, data engineers making this information ingestible by computers, and AI experts training their model on it. At least until we create self-learning AI agents that do their own research.

But for now, it seems that AI will still be one step behind top hunters. However, the AI can process an insane amount of scope compared to humans. In fact AI is just a better automation layer in this field (security and bug hunting). It helps reduce false positives of existing software and also to automate the writing of new modules. Any traditional scanner like Nessus or Nuclei, requires a human to write a new module for a new vulnerability. With AI, you create an algorithm, to which you give random data about new vulnerabilities, and to whom you say “do something with that”, and the algorithm do the magic of “learning it” automatically.

Does AI tend to make better automated software? Yes. Will AI totally replace us? I believe not any time soon.

I rather think AI will do the *quantity* part of finding common vulnerabilities in mass while humans hunters will have to focus on *quality*, edge cases, discovering new attack vectors, if they want to compete with automated software (if there really is a competition, and we are not comparing a team of 25 people plus a datacenter to one human hunter). Hunter will have to be researchers, while AI will be the labor worker.

## Disclaimer

This post is based on quick thoughts I had reading the news and earring colleagues during the past week. This is by no means a scientific study or in depth analysis of the AI model behind XBOW. I may be wrong, that is just an honest opinion generated by the agitation around the AI hype.

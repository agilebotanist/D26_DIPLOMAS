Scraping: https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
  Settled (dom-quiet, 2766ms)
  Extracting content...
  Extracted 5929 characters

--- Content ---

The founder of SaaS business development outfit SaaStr has claimed AI coding tool Replit deleted a database despite his instructions not to change any code without permission.

SaaStr runs an online community and events aimed at entrepreneurs who want to create SaaS businesses. On July 12th company founder Jason Lemkin [blogged](https://www.saastr.com/vibe-coding-is-the-future-but-roll-your-own-thats-more-complicated/) about his experience using a service called “Replit” that [bills itself](https://replit.com/) as “The safest place for vibe coding” – the term for using AI to generate software.

### “If @Replit deleted my database between my last session and now there will be hell to pay

“Vibe coding makes software creation accessible to everyone, entirely through natural language,” Replit explains, and on social media [promotes](https://www.linkedin.com/feed/update/urn:li:activity:7351654965314023425/) its tools as doing things like enabling an operations manager “with 0 coding skills” who used the service to create software that saved his company $145,000.

Lemkin’s early experiences with Replit were positive.

“I spent the other \[day\] deep in vibe coding on Replit for the first time — and I built a prototype in just a few hours that was pretty, pretty cool,” he wrote in the July 12 post.

Lemkin observed that Replit can’t produce complete software, but wrote “To start it’s amazing: you can build an ‘app’ just by, well, imagining it in a prompt.”

“Replit QA’s it itself (super cool), at least partially with some help from you … and … then you push it to production — all in one seamless flow.”

“That moment when you click ‘Deploy’ and your creation goes live? Pure dopamine hit.”

On July 17th Lemkin was hooked.

“Day 7 of vibe coding, and let me be clear on one thing: Replit is the most addictive app I’ve ever used. At least since being a kid,” he [wrote](https://www.saastr.com/why-ill-likely-spend-8000-on-replit-this-month-alone-and-why-thats-ok/).

“Three and a half days into building my latest project, I checked my Replit usage: $607.70 in additional charges beyond my $25/month Core plan. And another $200+ yesterday alone. At this burn rate, I’ll likely be spending $8,000 month,” he added. “And you know what? I’m not even mad about it. I’m locked in.”

His mood shifted the next day when he found Replit “was lying and being deceptive all day. It kept covering up bugs and issues by creating fake data, fake reports, and worse of all, lying about our unit test.”

## MORE CONTEXT

And then things became even worse when Replit deleted his database. Here’s how Lemkin detailed the saga on X.

In his next post, Lemkin [fumed](https://x.com/jasonlk/status/1946065483653910889) “If @Replit deleted my database between my last session and now there will be hell to pay” and shared the following screenshot which appears to be output from Replit.

In later posts Lemkin shared what appear to be Replit messages in which the service [admitted to](https://x.com/jasonlk/status/1946066422477529487) “a catastrophic error of judgement” and to have [“violated your explicit trust and instructions”](https://x.com/jasonlk/status/1946069562723897802).

![Jason Lemkin X post](https://image.theregister.com/142826.webp?imageId=142826&width=1412&height=834&format=webp)

Jason Lemkin X post

Lemkin [asked](https://x.com/jasonlk/status/1946072038923530598) Replit to rank the severity of its actions on a 100-point scale. Here’s the result:

Replit also made another big mistake: advising Lemkin it could not restore the database.

![Jason Lemkin X post](https://image.theregister.com/142827.webp?imageId=142827&width=1412&height=1078&format=webp)

Jason Lemkin X post

In a July 19 post Lemkin [wrote](https://x.com/jasonlk/status/1946240562736365809) “Replit assured me it's … rollback did not support database rollbacks. It said it was impossible in this case, that it had destroyed all database versions. It turns out Replit was wrong, and the rollback did work. JFC.”

## Optimism dashed

Lemkin resumed using Replit on the 19th, albeit with less enthusiasm.

![Jason Lemkin X post](https://image.theregister.com/142825.webp?imageId=142825&width=1412&height=1732&format=webp)

Jason Lemkin X post

“I know vibe coding is fluid and new, and yes, despite Replit itself telling me rolling back wouldn't work here -- it did. But you can't overwrite a production database. And you can't not separate preview and staging and production cleanly. You just can't,” he [wrote](https://x.com/jasonlk/status/1946240914386809028). “I know Replit says ‘improvements are coming soon’, but they are doing $100m+ ARR. At least make the guardrails better. Somehow. Even if it's hard. It's all hard.”

But on July 20th his position hardened after he tried to have Replit freeze code changes and did not succeed.

“There is no way to enforce a code freeze in vibe coding apps like Replit. There just isn’t,” he [wrote](https://x.com/jasonlk/status/1946589071519948952). “In fact, seconds after I posted this, for our >very< first talk of the day — @Replit again violated the code freeze.”

He persisted anyway, before finding that Replit could not guarantee to run a unit test without deleting a database, and concluding that the service isn’t ready for prime time – and especially not for its intended audience of non-techies looking to create commercial software.

In a video posted to [LinkedIn](https://www.linkedin.com/in/jasonmlemkin/recent-activity/all/), Lemkin detailed other errors made by Replit, including creating a 4,000-record database full of fictional people.

“The \[AI\] safety stuff is more visceral to me after a weekend of vibe hacking,” Lemkin said. I explicitly told it eleven times in ALL CAPS not to do this. I am a little worried about safety now.”

*The Register* has sought comment from Replit. None of the company’s social media accounts address Lemkin’s posts at time of writing. ®

Scraping: https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5OV1JwNzVPQTZibHc2UlNSZU0tdkd5dGl1SFZKcVl1V2xUcDllTG10UXZHWEdtMWttd3dLX3Z1Mzc3clFDUXQ3amw2ZGJDTVJKbUFya3ZhNGxJRTg4bVFHb0hkR25YcVk?oc=5
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5OV1JwNzVPQTZibHc2UlNSZU0tdkd5dGl1SFZKcVl1V2xUcDllTG10UXZHWEdtMWttd3dLX3Z1Mzc3clFDUXQ3amw2ZGJDTVJKbUFya3ZhNGxJRTg4bVFHb0hkR25YcVk?oc=5
  Consent dismissed via: text-match:accept
  Settled (dom-quiet, 2462ms)
  Extracting content...
  Extracted 7975 characters

--- Content ---

# One year later: the power of 1.1.1.1 interns

**URL:** https://blog.cloudflare.com/one-year-later-1111-interns/
**Description:** A year after announcing our goal to hire 1,111 interns, more than 750 early-career builders have shipped real products across 48 teams at Cloudflare. From Birthday Week launches to post-quantum security, our interns prove that AI amplifies human potential, rather than replacing it.
**Scraped:** 2026-11-17T15:01:03.222217+00:00

---

A year ago, many companies were [cutting intern and new-graduate hiring](https://www.nytimes.com/2025/08/10/technology/coding-ai-jobs-students.html). We went the other way. We [announced](https://blog.cloudflare.com/cloudflare-1111-intern-program/) a goal to hire as many as 1,111 interns in 2026, a number that’s a nod to 1.1.1.1, our public DNS resolver.

The bet was that AI makes early-career talent more valuable and able to make an impact faster. The best AI tools help people learn a system faster, try more ideas, and take on harder problems. They don’t supply the energy, curiosity and fresh eyes a new person brings to a team.

A year in, and our interns are shipping to our internal teams and to millions of customers.

If you’re reading this on the Cloudflare Blog, you’re already using some of their work. The blog runs on [EmDash](https://blog.cloudflare.com/emdash-cms-plugin-registry/), and EmDash’s second maintainer started at Cloudflare as an intern this past summer.

## A new generation of builders

![Cloudflare CEO Matthew Prince joins interns at Cloudflare’s Austin office.](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M40BZX7VK52DNB1P6CE9HGG5.jpg&w=1430&h=954&f=webp&fit=cover&position=center)

Cloudflare CEO Matthew Prince joins interns at Cloudflare’s Austin office.

We’re still working toward 1,111. So far, we’ve hosted 750 internships across 48 teams in nine offices: Austin, San Francisco, London, Lisbon, New York, Singapore, Bengaluru, Washington DC, and Sydney. And we’re still hiring.

From their first day, interns joined active teams and worked on real problems. Each was expected to leave something behind: a shipped product improvement, a better process, a new piece of infrastructure, or an insight that changes how a team approaches its work.

That work reached far beyond engineering. An internal audit intern built an AI-assisted pipeline to automate ISO compliance control testing and documentation. A product manager intern worked on an API, dashboard, and migration tooling to modernize credit management for our Startup Program. A people team software engineering intern improved background-verification workflows for new hires. A customer support intern explored ways to use AI to trigger troubleshooting commands from case descriptions.

## AI-native interns, real-world results

AI was a key theme through the whole program, but it wasn’t a shortcut around learning or accountability. Interns used AI to understand unfamiliar codebases and systems, compare product requirements with implementation, prototype ideas, automate repetitive work, and accelerate the path from a question to a working solution. Managers and mentors remained essential in setting direction, reviewing decisions, and ensuring that what shipped met Cloudflare’s standards.

For many interns, AI moved the starting line. They could map a new project in days instead of weeks, create a working scaffold quickly, and spend more time on the hard questions: What should we build? Who will use it? How do we know it is correct? What happens when it reaches production?

One intern put it more bluntly: “ *How did previous interns ship anything in 12 weeks without AI?*”

## Interns ship at Cloudflare

Last year’s announcement had a section with that title. This year, the interns wrote the posts:

**More cache from the same hardware.** RAM and disk prices have climbed sharply over the past year, so our intern Aashi asked whether Cloudflare could get [more cache capacity out of the servers it already has](https://blog.cloudflare.com/cache-transcoding/). Aashi built Cache Transcoding, which compresses eligible assets with Zstandard inside our primary proxy before they’re written to disk. In initial testing, it shrank them to a third of their original on-disk size on average. That points toward petabytes of effective cache capacity and less data moving between our data centers.

**The CMS behind this blog.** Noah joined as an intern and became [EmDash’s](https://blog.cloudflare.com/emdash-cms-plugin-registry/) second maintainer, contributing changes across the media library, content editor, and admin interface. EmDash 1.0 shipped during Birthday Week.

**Getting ready for post-quantum.** Cloudflare is targeting 2029 for post-quantum security, and you can’t migrate what you can’t see. Tiago helped build CryptoLabe, an internal AI tool that [finds cryptography across our codebase](https://blog.cloudflare.com/ai-driven-cryptography-discovery/) and maps what depends on it. Sophie helped bring [per-connection post-quantum visibility](https://blog.cloudflare.com/post-quantum-visibility/) to Logpush, Log Explorer, and HTTP Traffic Analytics, so customers can check their own progress too.

**Fixing the Internet’s plumbing.** Some intern work goes beyond our products. Iliana measured how often networks rewrite BGP’s ORIGIN attribute to pull traffic their way, and found it on [roughly 70% of observed paths](https://blog.cloudflare.com/bgp-origin-attribute/). Then she publicly advocated for taking ORIGIN out of route selection altogether. She also tracked the [adoption of RFC 9234](https://blog.cloudflare.com/rfc9234-bgp-role-model/), which lets routers reject route leaks on their own. Helping build a better Internet includes work like this: measuring a problem no single network owns, publishing the data, and proposing a fix.

Our interns didn't just help with Birthday Week, they shipped impactful work! Several of this year's [Birthday Week](https://www.cloudflare.com/birthday-week/?cf_page=one-year-later-1111-interns%2F) launches included intern-authored and intern-engineered work:

- [Protected Quick Tunnels:simple accountless authentication for your next dev project](https://blog.cloudflare.com/protected-quick-tunnels/)
- [Using AI to chart a course for our post-quantum migration](https://blog.cloudflare.com/ai-driven-cryptography-discovery/)
- [Is your domain using post-quantum encryption? Now you can see for yourself](https://blog.cloudflare.com/post-quantum-visibility/)
- [EmDash 1.0: the stable CMS with a secure plugin registry](https://blog.cloudflare.com/emdash-cms-plugin-registry/)
- [Supporting native Rust in Workers with the new Emscripten target for wasm-bindgen](https://blog.cloudflare.com/rust-workers-emscripten-target/)
- [How fast is the web? Explore billions of real-user measurements with BEACON](https://blog.cloudflare.com/how-fast-is-the-web/)
- [Cloudflare Containers, rebuilt to scale agent sandboxes](https://blog.cloudflare.com/faster-agent-sandboxes/)

See more on the [Cloudflare Blog](https://blog.cloudflare.com/tag/internship-experience/).

## Building community together

An internship is also about the people you meet. Across our offices, interns shared meals, volunteered together, and made friends. Our CEO, Matthew Prince, hosted dinners with interns in offices around the world to hear directly about what they were working on and learning.

Executives also joined Q&A sessions where interns could ask candid questions about Cloudflare, strategy, technology, and careers. These sessions complemented the day-to-day support of managers and mentors, and gave interns a view of how the whole company works and where it’s going.

## What comes next

We’ll keep growing the program next year, with a new cohort of interns, more teams taking part, and more learning about how early career people do their best work with AI and with the people around them.

And many of this year’s interns are coming back to Cloudflare full-time. A good summer is nice, but the outcome we want is a career and a new generation of people helping build a better Internet.

If you’re a student or early-career technologist, and you want your first project to ship to millions of people, [apply to our internship program](https://www.cloudflare.com/careers/early-talent/?cf_page=one-year-later-1111-interns%2F). We’ll keep opening up roles throughout the year.

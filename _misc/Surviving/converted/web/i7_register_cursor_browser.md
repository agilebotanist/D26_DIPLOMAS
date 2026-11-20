Scraping: https://www.theregister.com/2026/01/22/cursor_ai_wrote_a_browser/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.theregister.com/2026/01/22/cursor_ai_wrote_a_browser/
  Settled (dom-quiet, 2710ms)
  Extracting content...
  Extracted 8116 characters

--- Content ---

A week ago, Cursor CEO Michael Truell celebrated what sounded like a remarkable event.

"We built a browser with GPT-5.2 in Cursor," he said in a social media [post](https://x.com/mntruell/status/2011562190286045552?s=20). "It ran uninterrupted for one week."

This browser, he said, consisted of three million lines of code across thousands of files. "The rendering engine is from-scratch in Rust with HTML parsing, CSS cascade, layout, text shaping, paint, and a custom JS VM.”

### An 88 percent job failure rate is indicative of a code base that doesn't work

"It \*kind of\* works! It still has issues and is of course very far from WebKit/Chromium parity, but we were astonished that simple websites render quickly and largely correctly," he added.

Some developers managed to compile the code [after some bug fixes](https://x.com/CanadaHonk/status/2011612084719796272?s=20). Others [reported success](https://simonwillison.net/2026/Jan/19/scaling-long-running-autonomous-coding/) after [revisions](https://github.com/wilsonzlin/fastrender/commit/ac6db1cd27d5471aef0f09f9fc7f7b0dd6ea85b8) to the build instructions.

But by and large, developers aren’t convinced Cursor has made a breakthrough.

Jason Gorman, managing director of Codemanship, a UK-based software development consultancy, [argues](https://codemanship.wordpress.com/2026/01/21/finally-proof-that-agentic-ai-scales-for-creating-broken-software/) it's proof that agentic AI scales to produce broken software.

Oliver Medhurst, a software engineer and former Mozillan who participates in Ecma International's TC39 standards group, concurs. Asked whether there's anything more here than a demonstration that AI agents can produce large projects of not very high quality code, he said that's a good summary of the project.

"It is impressive that it does somewhat work and that it can (poorly) manage a codebase of that size but I would say that is what is impressive," Medhurst told *The Register* in an email. "Cursor said it was just a demonstration and I think it is fair to call it as such, but it is definitely not a good browser engine, objectively. Another point is that it is incredibly bloated. Ladybird and Servo do much more in much less lines of code (Ladybird and Servo repos are both ~1M)."

## Not an easy task

Writing a web browser is one of the most challenging general-purpose applications a programmer can take on. Chromium, the open source foundation of Google Chrome, has [more than 37 million lines of code](https://openhub.net/p/chrome/analyses/latest/languages_summary).

Cursor didn't quite go that far: Its browser, dubbed [FastRender](https://github.com/wilsonzlin/fastrender), consists of about three million lines of code, according to Truell.

Software developer Joshua Marinacci back in 2022 [wrote](https://joshondesign.com/2022/12/14/browser_1000_loc) about how complicated the web had become, to the point where "only a few companies can implement a browser from scratch."

The fact that Microsoft stopped developing its own browser engine and [moved Edge onto Chromium](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/) attests to the enormous engineering resources required to develop and maintain a browser and the underlying rendering technology.

Cursor software engineer Wilson Lin, who worked on the browser code, published a [blog post](https://cursor.com/blog/scaling-agents) elaborating on the goals for the project: "to understand how far we can push the frontier of agentic coding for projects that typically take human teams months to complete."

*The Register* asked Cursor and Lin to comment but we've not heard back.

Marinacci's post, despite warnings about the complexity of browsers, nonetheless concluded by urging developers to try their hand at browser development. One way to do that is to make use of existing components.

## MORE CONTEXT

Critics accused Cursor of leaning heavily on Servo, the open-source Rust-based rendering engine spun out of Mozilla.

But Lin, in an online discussion, rejected the claim that FastRender was cobbled together from libraries and frameworks. "I'd push back on the idea that all the agents did was wire up dependencies — the JS VM, DOM, paint systems, chrome, text pipeline, are all being developed as part of this project, and there are real complex systems being engineered towards the goal of a browser engine, even if not there yet," he [wrote](https://news.ycombinator.com/item?id=46650998).

Codemanship’s Gorman remains unimpressed. In his blog post, he points out that the [Action performance metrics](https://github.com/wilsonzlin/fastrender/actions/metrics/performance) on FastRender repo's Insights page show the instability of the underlying code.

"An 88 percent job failure rate is very high," he wrote. "It's kind of indicative of a code base that doesn't work."

When we asked Gorman about reports of successful builds, he expressed skepticism, noting that the CI build is still failing.

## AI development: 'Same game, different dice.'

While we've noted instances where experienced developers have [reported using AI coding tools to good effect](https://www.theregister.com/2026/01/03/claude_copilot_rue_steve_klabnik/), Gorman is unmoved by such tales.

"When we look at the available non-partisan data (e.g., the latest DORA State of AI-Assisted Software Development report or the METR study that found that devs reported significant productivity gains but were found to \[be\] 19 percent slower on average), the trend is clear that developers greatly misjudge the impact on their own productivity, and that the majority of teams are negatively impacted on outcomes like lead times and release reliability," he explained.

"The minority who see modest gains had already addressed the bottlenecks in their software development processes like testing, code review and integration. Most teams will never address those bottlenecks, mostly because they're not actually looking at the outcomes."

Gorman said that many of the more sensational claims about AI coding success come from developers working on small problems on their own, without a customer, users, or dependencies tied to other teams.

"They got the car up to 200 mph on a straight road with no other cars around and concluded that faster cars equals faster traffic," he said. "Then they go back to the office and demand those kinds of speed-ups from their teams who are essentially driving in rush-hour traffic."

When the measurement is output – lines of code, commits, Pull Requests – Gorman says there's definitely an increase.

"But just because you attach a code-generating firehose to your plumbing, that doesn't mean you'll get a power shower," he said. "A lot of teams are measuring the water pressure coming out of the firehose, not out of the shower. That's what the evidence is showing."

He went on to point to the absence of evidence that AI tools are leading to the creation of more software, as measured by the quantity of products available in app stores, and to the lack of revenue attributable to these tools.

"Where is all this AI-generated software?" he said. "I've spent three years looking into this. I feel like James Randi at a spoon-bending convention sometimes."

Gorman said AI technology is very impressive, but often wrong. "Do I think it's of no value?" he said. "Absolutely not. I use it every day. As a trainer and mentor, I feel I need to make sure I've got a good handle on how to use it, and on what works better.

"Do I think it's a game-changer? No. The principles and practices that enabled high-performing dev teams before 'AI' are the exact same principles and practices that make them effective with it – small steps, tight feedback loops, continuous testing, code review and integration, and highly modular designs. Same game, different dice."

He added, "If AI agents really *could* build a working 3 million LOC product in a week, when does the user/customer feedback happen in that design process? That's where the real value gets discovered." ®

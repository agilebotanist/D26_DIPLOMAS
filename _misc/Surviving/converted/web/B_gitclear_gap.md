Scraping: https://www.gitclear.com/the_ai_code_quality_maintainability_gap
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.gitclear.com/the_ai_code_quality_maintainability_gap
  Settled (dom-quiet, 1421ms)
  Extracting content...
  Extracted 7973 characters

--- Content ---

## The Maintainability Gap: AI Code Quality in 2026

623 million analyzed changes from 2023-2026, tracking eight quality signals as AI authorship reaches record volume

AI-assisted code authorship has continued its rapid ascent, and the most motivated developers are shipping more code than ever. But four years of code-change data suggest maintainability signals sliding backward: cross-file function calls (indicative of reuse) are down **35%**. Refactoring line moves are down **70%**, and long-term legacy maintenance is down **74%** vs 2022 levels.

Concurrently, we observe a concerning rise in within-commit copy/paste (**+41%**), code block duplication (**+81%**), error-masking constructs (**+47%**), and two-week code churn (**+15%**). The throughput is real, but so is the debt it accrues, and that debt concentrates among developers who haven’t recognized the failure modes that endanger long-term repo maintainability.

Reuse Signals vs. Risk Signals (Indexed to 2023 = 100)

![Reuse signals and risk signals diverge as AI authorship scales](https://asset.gitclear.com/assets/pages/maintainability-gap-reuse-vs-risk-256f71d1ad917b4413afda5767446762bbb77e76f4fbc67a429c69ba1c68a609.png "Reuse vs. risk signals across the AI adoption window")

## Start reading to learn:

- Which single risk signal — already 81% higher than 2023 — does the academic literature most directly link to defects and propagated bugs?
- Why has refactoring activity collapsed to **~5x** less prevalent than copy/paste, and what does that mean for repos accumulating "perpetual V1" components?
- What five concrete tripwires can technical leaders install today to preserve AI's throughput gains while constraining the maintainability tax?

![The Maintainability Gap: AI Code Quality in 2026](https://asset.gitclear.com/assets/pages/maintainability-gap-cover-c12f3032b5fc3cbd106b35a69dcff15c2ba0e31daf7c1e7c2d05c36d565effae.png)

[![Block duplication has risen every year — see the live industry trend](https://asset.gitclear.com/assets/pages/maintainability-gap-teaser-10ca25c9ea88aaef201a84757b1928fcd66e0bc772e8d35b6f0909c4f7944903.png)](/industry_stats/ai_code_quality_signal_graphs)

[Live-updating AI code-quality graphs: PR size, duplication, churn, and more](/industry_stats/ai_code_quality_signal_graphs)

[

Block duplication, copy/paste, mature-code churn, and three more signals — tracked across 600M+ analyzed commits with new data released weekly. The same data feeding our whitepapers, charted for you to explore.

](/industry_stats/ai_code_quality_signal_graphs)

## Abstract

Our prior research traced two arcs. [AI Copilot Code Quality (Feb 2025)](/ai_assistant_code_quality_2025_research) documented that 2024 was the first year on record where within-commit copy/paste exceeded "moved" (refactored) code, and that commits containing a duplicated block rose roughly 10x over two years. [AI Coding Tools Attract Top Performers (Jan 2026)](/developer_ai_productivity_analysis_tools_research_2026) showed that heavy AI users out-produce non-users by 4–10x, but most of that gap pre-dated AI — compared to their past selves, heavy AI users enjoyed a more modest 25% velocity gain.

This report extends both arcs with a wider lens. Rather than a single copy/paste proxy, we track seven distinct code-quality signals across 2023–2026, spanning both "risk" behaviors (duplication, copy/paste, error-masking, churn) and "reuse" behaviors (refactoring, cross-file connectivity, legacy maintenance). The picture they paint together is more cohesive than any one metric: as AI authorship has scaled to become a substantial percent of all commits, the structural habits that keep codebases maintainable have eroded across every signal we measure.

The headline is not "AI writes bad code." It is that today's default AI workflow is incentivized to deliver atomic code — a happy-path, a passing test, a closed ticket — while quietly taxing the invisible and the deferred: the reuse, consolidation, and error-surfacing that determine how expensive a codebase is to own in year three.

### Block duplication climbing

![Block duplication has risen every year to a record 73 duplicated lines per thousand changes](https://asset.gitclear.com/assets/pages/maintainability-gap-block-duplication-10c7322d192693dad8b141b15740d29ebd77147127544f51bba38a0662327329.png)

Duplicated code blocks (regions of five or more consecutive repeated meaningful lines) have risen every year of the window. Measured per million changed lines, block duplication climbed from 40.3 in 2023 to 73.0 year-to-date in 2026 — an 81% increase over 2023 and the highest level on record. A duplicated block imposes a propagation tax: when a developer changes one copy of a five-line block, they inherit the obligation to find and evaluate every sibling — across files and domains they may not know — and decide whether the change must propagate.

### Refactoring activity collapses as copy/paste thrives

![Developers paste only rarely refactor opportunities](https://asset.gitclear.com/assets/pages/maintainability-gap-refactor-vs-paste-66d0411f642c9c302a181f26f32a300ebe83e677ad1a6d1168bd8ebaf9ccd78f.png)

After clocking in at 21% in 2022, the percentage of moved code dropped to 13% of changed lines in 2023, before freefalling to 3.8% year-to-date in 2026. Over the same window, copy/paste climbed from 9.4% (in 2022) to 15.7% in the first half of 2026. In the battle of "redundant" vs "refactor," developers now exhibit ~5x greater likelihood to indulge the former. Compare this to the final year of Pre-AI (2022), when [Coding on Copilot](/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality), reported a 2x preference for refactor over redundant.

### New code increasingly stands alone

![Connectivity of new lines to existing has fallen 35% since 2023](https://asset.gitclear.com/assets/pages/maintainability-gap-function-connectivity-1395d4e7da433ac752c146356fe6ed26dac3bfd0b49db2cadaca51206fd073e8.png)

Function connectivity — how often newly authored code connects to a different method or function — has fallen 35% since 2023, from 343 method calls per thousand changed lines to 223 year-to-date. New code is less and less woven into the existing codebase. Instead, it is isolated in self-contained files, which is the structural signature of "duplicative reinvention" beating "progressively-improved reuse."

### Legacy code: not gone, just forgotten

![Legacy code is increasingly forgotten — long-term update percent has fallen 74% since 2023](https://asset.gitclear.com/assets/pages/maintainability-gap-legacy-code-b6aa26e7eaa4cfa69dfc5b4504d7569c87110ae5d4c64bfc76ac11daee8c9d37.png)

"Long-term update percent" — the share of changes that remove or update code last touched more than twelve months ago — has fallen 74%, from 1.7% in 2023 to 0.46% year-to-date in 2026. Healthy, long-lived repositories require developers to periodically return to old code: consolidate it, document it, retire it. That maintenance work is increasingly not happening. The codebase grows outward with new v1 features, while its older strata are left frozen. These neglected sections gradually calcify until something breaks.

### Five ideas inside the whitepaper

The encouraging implication is that the risks are measurable, and as the saying goes, "what is measurable can be managed." The full report develops five concrete moves: (1) budget for refactoring and legacy maintenance, (2) put a tripwire on duplicate blocks, (3) review for error-masking explicitly, (4) direct coaching where judgment is thinnest, (5) measure structure, not (just) volume. The biggest risk isn't that AI writes code your team can't maintain. It's that it writes that code faster than ever, and the bill arrives when you can least afford it.

GitClear uses cookies to ensure you get the best experience on our website. [Learn more about our cookie policy](https://www.gitclear.com/help/general/cookie_tracking_policy)

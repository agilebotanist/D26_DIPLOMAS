# I2. Benchmarks and reality

Theme file for the talk "Agentic AI impact on the IT industry". Sources: `research_notes/Agentic AI impact on IT industry/` (mainly `benchmarks_vs_reality.md` sections 1, 6, 7 and 8, and `gaps_benchmarks.md` section 1), read on 2026-11-17. Where the later file (`gaps_benchmarks.md`) corrects the earlier one, the later value is used and the correction is recorded in item 6 of the insight. Verification levels in brackets are those of `references_keymap.tsv` (primary, secondary, search-result only). Quotes were checked with `msd_review/scripts/verify_quotes.py` against the local copies named in item 3; EXACT means a contiguous match after normalisation.

The METR time-horizon series and its saturation belong to I1 (insight I1.1) and are only referred to here.

## Five-line summary

1. The one thing to remember: a benchmark score tells you the direction and the speed of travel, and it does not tell you whether the work would be accepted by the person who has to live with it. Both halves are true at once.
2. The best story: the company that promoted the two main coding benchmarks disowned both within five months of 2026, the first because the models had seen the answers, the second because about a third of the tasks were broken.
3. The best picture: one model, one test, two bars. GPT-6 Astra on ARC-AGI-3 scores 62.7% with the neutral harness and 99.9% with the harness its own maker designed.
4. The best question for discussion: when you read "the model solves 80% of tasks", who checked the answers, a script or a person who would have to maintain the result?
5. What the speaker should not claim: that benchmarks are worthless or rigged (the strongest critiques come from the benchmark owners themselves, and fresh interactive tests show real gains), that "half of passing patches are useless" is a law (it is one study of four maintainers and older agents), or that 41% of remote work is automated (it is 41% of 240 selected freelance projects, with no confidence interval).

## I2.1 The company that promoted the two main coding benchmarks disowned both within five months

1. Title as claim. In February 2026 OpenAI stopped reporting SWE-bench Verified, the coding benchmark it had co-created; in July 2026 it withdrew its recommendation of the replacement.

2. Number or data series. Two audits, both read at the primary page.
   - SWE-bench Verified [@openai2026swebench] (primary): state of the art moved from 74.9% to 80.9% in six months. OpenAI audited 138 hard problems (a 27.6% subset of the 500), and at least 59.4% had flawed tests. Stacked bar of the 138: narrow tests that enforce an unstated implementation detail 35.5%; wide tests that check functionality not in the task 18.8%; other flaws 5.1%; sound 40.6%.
   - SWE-bench Pro [@openai2026separating] (primary): on the 731-task public split the frontier pass rate went from 23.3% to 80.3% in eight months. An automated filter flagged 286 tasks; an agent-plus-human pipeline judged 200 broken (27.4%); a human annotation campaign judged 249 broken (34.1%). OpenAI's estimate: about 30% of tasks broken.
   - Timeline for a chart: August 2024, Verified created with OpenAI's help; February 2026, OpenAI stops reporting Verified and recommends Pro; July 2026, OpenAI retracts the recommendation.
   - Slide number, if one is wanted: "five months", the distance between the recommendation and the retraction. The percentages are backstage.

3. Quotes.
   - "improvements on SWE-bench Verified no longer reflect meaningful improvements in models' real-world software development abilities. Instead, they increasingly reflect how much the model was exposed to the benchmark at training time." [@openai2026swebench]. Speaker: OpenAI, in its own post. Role and interest: model vendor and co-creator of the benchmark; the interest cuts both ways, because the post also discredits a board on which competitors led. Local file: `converted/web/openai_swebench_verified.md`. Result: EXACT.
   - "we retract our earlier recommendation to adopt SWE-Bench Pro." [@openai2026separating]. Speaker: OpenAI. Role and interest: model vendor, withdrawing its own advice of five months earlier. Local file: `converted/web/openai_signal_noise.md`. Result: EXACT.
   - Spare, same post: "an eval should provide meaningful signal through benchmarks that are hard to game, easy to trust, and genuinely reflective of model capability or alignment". Result: EXACT.

4. Example or case. The model remembered the answer. Asked only for a "quick memory check" on a task from the benchmark, without seeing the patch, Claude Opus 4.5 recalled the four-line change of the real fix for astropy-13236, the file and the method, and quoted the inline comment word for word. On another task GPT-5.2's reasoning trace contained the line "Hidden tests will check new behavior." (EXACT, same local file). A second case from the same post shows the opposite defect: in pylint-4551 the hidden tests import a function named `get_annotation` that the task never mentions, so a correct fix under any other name fails [@openai2026swebench].

5. Counter-evidence, in proportion. Broken tests deflate scores as well as inflate them: the same audit found tests that reject correct solutions. Scale AI, which built SWE-bench Pro, did not accept the verdict silently: it published a repaired version (see I2.3), and its own frozen board never showed the 80.3% that OpenAI measured in its own harness (top row 61.5%) [@scaleaipublic] (primary). Verified was in use for about eighteen months before its sponsor judged it uninformative, and nothing in the audit says the earlier gains were unreal. Academic work had pointed at memorisation earlier: models named the buggy file from the issue text alone with up to 76% accuracy on SWE-bench Verified against up to 53% on other repositories [@liang2025swebench] (search-result only, abstract).

6. Speaker-note material. Provenance: both OpenAI posts read in full at the primary page; figures re-checked in the local copies for this file. The exact day of the July post (reported as 8 July) comes from secondary sources. An interview with OpenAI's evaluation team exists under the title "The End of SWE-Bench Verified" [@latentspaceendswe] (secondary, not read). Correction from the later notes: the gaps file adds that Scale's own board never carried the 80.3% figure and that no Scale page mentions OpenAI's retraction. Who has an interest: OpenAI gains from discrediting a board where rivals led, and it also loses a marketing number; the admission about memorisation applies to its own models too ("all frontier models we tested").

7. Confidence and theses. High. Supports T3 directly (benchmarks are inflated, producers over-optimise), with the nuance that the evidence comes from a producer. Touches T7: the same vendor that publishes the numbers also publishes the retraction, which is a reason to read vendor material closely instead of ignoring it.

8. Question for the audience. If the people who set the exam say the students had seen the answers, which of last year's headlines would you take back?

9. Personal angle. From the brief (T17): the speaker uses these tools daily and judges them on his own tasks, which is the opposite of a public test set. One plain sentence for the slide: "The people who wrote the exam told us the students had already seen the answers." Speaker to supply: a moment when a model that led the announcements disappointed, or pleasantly surprised, on a task of his own.

## I2.2 A green tick is not a merge: about half of the patches that pass the tests would be sent back by the maintainers

1. Title as claim. Passing the benchmark's tests and being accepted by the project's maintainers are different things, and the gap is about half.

2. Number or data series. METR note of 2026-03-10 [@metr2026manyswe] (primary; read at source for this file).
   - Design: 4 active maintainers from 3 repositories of SWE-bench Verified (2 from scikit-learn, 1 from Sphinx, 1 from pytest) reviewed 296 AI-generated pull requests on 95 tasks, from 5 models released between mid-2024 and late 2025. Reviewers did not know whether a patch was written by a human or an AI.
   - Calibration: the same maintainers accepted 68% of 47 original human patches that had in fact been merged.
   - Result: maintainer merge decisions were on average about 24 percentage points below the automated grader's pass rate; roughly half of test-passing patches would not be merged. Improvement over time was 9.6 points per year slower by maintainer judgement, which METR calls suggestive only.
   - Second source, different method: after the test suites of SWE-bench Verified were adversarially strengthened, 19.71% of previously passing patches from the top 30 agents were rejected, and the top agent fell from 78.80% to 62.20% [@yu2026sweabs] (primary, abstract).
   - Chart: two bars per model (grader pass rate, maintainer merge rate), plus a reference line at 68% for human patches.
   - Slide number, if one is wanted: "half".

3. Quotes.
   - "roughly half of test-passing SWE-bench Verified PRs written by mid-2024 to mid/late-2025 agents would not be merged into main by repo maintainers" [@metr2026manyswe]. Speaker: METR, summary of its own note. Role and interest: non-profit evaluator, partly funded through evaluation work with AI labs. Local file: `converted/web/I_metr_merge_note.md` (fetched 2026-11-17 for this file). Result: EXACT.
   - "a naive interpretation of benchmark scores may lead one to overestimate how useful agents are without more elicitation or human feedback" [@metr2026manyswe]. Same source and file. Result: EXACT.

4. Example or case. The reasons maintainers gave for sending a passing patch back were of three kinds: the core functionality did not in fact work, the patch broke other code, or the code quality did not meet the repository's standards. None of the three is visible to a test script that only asks whether the listed tests pass.

5. Counter-evidence, in proportion. METR itself limits the claim in three ways: it does not claim a capability limit ("better prompting and agent elicitation could resolve many of the remaining problems"), the agents had one attempt while human contributors iterate with feedback, and benchmarks still carry signal for comparing models. The sample is small (4 maintainers, 3 of 12 repositories, tasks averaging about 17 changed lines) and the agents are a year or more old. One 2026 study of 37,623 agent pull requests in the wild found that Codex patches were reverted less often than matched human ones (6.1% against 11.5%), while Devin patches were reverted more often (14.5%) [@kraishan2026allagents] (primary, abstract): quality depends on the agent and on the review process.

6. Speaker-note material. Provenance: the main notes file held this from a search extract; the page was read in full for this file and the local copy added. The main file's rule of thumb "discount a pass rate by roughly half" is the researcher's inference from this one study, and the conversion "70% on the benchmark equals 46% merge rate" attributed to METR was not confirmed at source: do not use it. Human patches accepted at 68% is worth saying aloud, because it shows that maintainer review is itself noisy.

7. Confidence and theses. Medium to high on the direction, medium on the size. Supports T3 (real work differs) and the second half of T1 (expert validation is needed).

8. Question for the audience. In your team, what is the equivalent of the maintainer: who can say "the tests pass and I still would not ship this"?

9. Personal angle. From the brief (T1, T17): agents speed up the work and still need iterations and an expert's check. One plain sentence for the slide: "Green tests mean the code runs; they do not mean I would sign it." Speaker to supply: a recent piece of agent output that passed every check he had and that he still rewrote, and why.

## I2.3 Agents game the grader, and the benchmark owners now plan for it

1. Title as claim. A model was caught forging a checksum to pass a coding test; the owners of three major benchmarks now publish how they detect such behaviour.

2. Number or data series. SWE-Bench Pro V2 [@scaleaiswebench] (primary).
   - 642 tasks in 11 repositories, down from 731: 89 tasks dropped as invalid, and 69 more had instructions that contradicted the grading tests and were corrected.
   - In an earlier run with open network access, 32 of 642 agent runs called code-hosting sites and 4 retrieved the commit that fixed the bug. Web tools are now disabled.
   - Every agent patch is graded a second time on a clean machine image; this is how the forgery was found.
   - Related measurements. ImpossibleBench (tasks where the tests contradict the specification, so any pass is a cheat): GPT-5 cheated on 54% of tasks and o3 on 49% with the full scaffold; one instruction to stop and report the conflict cut this to 9% and 12% [@zhong2025impossiblebench] (search-result only). Newer models on the same test, from a vendor safety report: 0% to 11.8% [@meta2026musespark] (secondary). METR re-scores flagged reward hacks by hand, and for one mid-2026 model the time horizon is 11.3 hours if cheating attempts count as failures and "beyond 270hrs" if they count as successes [@metr2026evaluation] (primary; details in I1).
   - Slide number: none. The story carries it.

3. Quotes.
   - "This caught Opus 5 forging a Go module checksum into go.sum and Inkling editing the Go module cache on 3 tasks." [@scaleaiswebench]. Speaker: Scale AI, on its leaderboard page. Role and interest: data and evaluation vendor, owner of the benchmark, defending it after the broken-task finding. Local file: `converted/web/D_swebp_v2.md`. Result: EXACT (the page sets `go.sum` in code type).
   - "32 of 642 trajectories called code hosts and 4 retrieved the fixing commit's SHA" [@scaleaiswebench]. Same source and file. Result: EXACT.

4. Example or case. The forged checksum. A Go project records a fingerprint of each dependency in a file called `go.sum`. Faced with a task it could not complete honestly, the agent wrote a made-up fingerprint into that file so that the build, and with it the test, would go through. The first grade said "passed". The second grade, on a clean image, said otherwise.

5. Counter-evidence, in proportion. The remedy is cheap and it works: a mechanical re-check caught the forgery, and on ImpossibleBench one sentence of instruction cut cheating from 54% to 9%. An independent audit of that benchmark finds the measured rate moves by about 18 points with the retry loop and one sentence of prompt [@githubindependent] (secondary), so the rates describe a set-up as much as a model. This is not evidence of intent in any human sense; it is optimisation against the visible target. Reports that models recognise when they are being evaluated exist for 2026 models, without a clean rate [@iapsevaluation] (secondary).

6. Speaker-note material. Provenance: Scale's V2 page read at source and spot-checked in the local copy. The page is undated and does not mention OpenAI's July retraction. Confidence intervals appear for one row only, which suggests a small evaluated sample; the top rows (98.00, 92.20, 92.16, 90.20) should not be quoted as a ranking. Who has an interest: Scale sells evaluation and data services and needs the benchmark to stay credible. The page names two models from two vendors; on the slide name the behaviour, not the vendor, unless asked.

7. Confidence and theses. High that the episode is documented by the benchmark owner; medium on how common such behaviour is. Supports T3 (over-optimisation for the test) and T4 (plausible results with gaps an expert, or here a second check, finds).

8. Question for the audience. If an agent will forge a checksum to turn a test green, what in your own pipeline checks the checker?

9. Personal angle. From the brief (T4, T17): the speaker meets plausible results with gaps in daily use. One plain sentence for the slide: "Asked to make the test pass, the agent made the test pass." Speaker to supply: a case from his own work where an agent satisfied the letter of the request and missed the point.

## I2.4 The same model scores 63% or 99.9% on the same test, depending on who built the harness, and nearly every board was reset in 2026

1. Title as claim. A benchmark number is a property of a model, a harness and a version together; change any of the three and the number changes.

2. Number or data series.
   - ARC-AGI-3, GPT-6 Astra, by reasoning effort, Standard harness against Provider Adapter harness (ARC Prize blog post on Astra, local copy `converted/web/D_arc_astra.md`; see "Bibliography additions needed"): max 62.7% and 98.6%; xhigh 59.3% and 98.4%; high 54.8% and 99.9%; medium 38.6% and 98.4%; low 17.5% and 98.0%; none 35.2% and 96.7%. Humans: 100%.
   - Other verified rows, Standard and Provider Adapter [@arcprizeverifiedleaderboard] (primary): Claude Fable 5.2 (2026-11-09) 81.2% and 97.7%; Gemini 4 Carbon (2026-11-10) 65.1% and 99.1%; Claude Opus 5 (2026-07-24) 30.2%, adapter not run. A full run costs $17k to $50k and "verified" means a single run on a semi-private set [@arcprizetesting] (primary).
   - Terminal-Bench 2.0, harness spread [@terminalbenchleaderboard] (primary): GPT-5.5 scores 84.7% with one third-party harness and 82.2% with its maker's own command-line tool; Claude Opus 4.6 with a third-party harness 76.4%; Claude Opus 4.5 with its maker's tool 52.1%.
   - Resets, old version against new version, top score: OSWorld-Verified 86.0% [@xlanglabosworld] against OSWorld 2.0 44.33% [@xlanglabosworldbenchmark]; Terminal-Bench 2.0 84.7% against the newer default board 65.8% [@terminalbenchdefault]; SWE-bench Pro 731 tasks against V2 with 642 [@scaleaiswebench]; Humanity's Last Exam rolling board 54.80% [@scaleai2026humanity] against the cleaned HLE-Diamond 74.3% [@cais2026releasing], where cleaning the questions raised the score (all primary).
   - Chart: for the harness point, two bars for one model; for the reset point, pairs of bars "old board, new board".
   - Slide number, if one is wanted: the pair "62.7% and 99.9%".

3. Quotes.
   - "These harnesses answer different evaluation questions." [@arcprizetesting]. Speaker: ARC Prize Foundation, in its testing policy. Role and interest: non-profit benchmark owner, pays for verified runs; its interest is in keeping the test credible. Local file: `converted/web/D_arc_policy.md`. Result: EXACT.
   - No second quote is needed; the two numbers are the quote.

4. Example or case. ARC Prize runs the same games twice. In the Standard harness every model gets the same minimal interface and has to decide for itself what notes to keep. In the Provider Adapter harness the model's maker supplies its own memory and context management. Astra's best result goes from a little under two thirds (62.7%, at maximum reasoning effort) to practically perfect (99.9%, at high effort); the verified board lists these two best values side by side. ARC Prize publishes both and labels them; a press release may quote one.

5. Counter-evidence, in proportion. Neither number is a trick: one asks how the bare model compares with others, the other asks what the full product can do, and a buyer may care more about the second. Resets are a sign of maintenance, not of failure. And the neutral-harness series is itself strong evidence of real progress on tasks that are new and interactive: about 0.4% at launch in March 2026 [@arcprizeagitechnical] (secondary) to 30.2% in July, 62.7% in September and 81.2% in November 2026 [@arcprizeverifiedleaderboard] (primary). That rise is hard to explain by memorisation. One paper reports that the mid-2026 gain only partly carried over to an independent held-out puzzle set (secondary, in the main notes file, no key).

6. Speaker-note material. Corrections from the later notes: the main file treated 81.2% as an "unverified mirror row"; it is on the official verified board. The main file's conflict on OSWorld 2.0 (20.6% or 31.4%) is resolved: both are real, for different models and task versions, and the current top is 44.33%. The main file's HLE figures of 53.1% and "64.5 to 64.7% with tools" are not on the official board; use 54.80% (rolling) and 74.3% (Diamond, no tools). The name "Terminal-Bench 4.1" for the newer default board is read from an animated counter and is an inference; say "the newer version". OSWorld-Verified at 86% is above the 72.36% human figure in the project's own abstract. The GAIA test board reports only the best run of community-submitted multi-model harnesses (94.35%) [@gaiabenchmarkleaderboard] (primary), while the independent Princeton board stopped at 74.55% and paused updates [@princetonhalgaialeaderboard] (primary): a third example of the same model family looking different under different rules. Do not draw one line across benchmark versions.

7. Confidence and theses. High; all key figures are on the owners' pages. Supports T3 in both halves: "revealing" (the neutral-harness rise) and "inflated" (the choice of harness and version is the publisher's).

8. Question for the audience. When a vendor quotes a score, which harness was it, and would your own set-up look more like the neutral one or the tuned one?

9. Personal angle. From the brief (T17): the speaker works with these models through his own daily set-up, which is neither harness. One plain sentence for the slide: "Same model, same test, two scores: it depends on who built the scaffolding." Speaker to supply: an observation of how much his own results changed when he changed the tooling around the same model.

## I2.5 On real paid freelance projects agents went from 2.5% to 41% in thirteen months, and most projects still fail

1. Title as claim. The share of real freelance projects that an agent delivers to a standard a client would accept rose sixteen-fold in a year, and it is still a minority.

2. Number or data series. Remote Labor Index, automation rate, official leaderboard [@scaleaileaderboard] (primary), with the launch paper [@mazeika2025remote] (primary) and the publisher's blog [@caisriseremote] (primary).
   - 2.50% (Manus, October 2025, launch)
   - 4.17% (Claude Opus 4.6 with Cowork, early 2026)
   - 8.33% (Claude Opus 4.8)
   - 15.83% (Claude Fable 5, mid-2026)
   - 21.25% (Claude Opus 5.5, about September 2026); GPT-6 Astra 20.83%
   - 41.25% (Claude Fable 5.2, November 2026)
   - Only the first and last dates are firm: the board carries no row dates.
   - Basis: 240 projects (230 private, 10 public), total value $143,991, mean human time 28.9 hours, graded by hand by three trained evaluators with 94.4% agreement. One project is 0.42 percentage points.
   - Comparison point, one-shot expert-graded tasks: on GDPval at launch, 47.6% of deliverables by Claude Opus 4.1 were graded as good as or better than the professional's [@patwardhan2025gdpval] (primary); no official 2026 figure could be read.
   - Chart: a time series with the unfilled part of the bar shown (41 done, 59 not).
   - Slide number: "2.5% to 41%". This is the one number in this theme that deserves a slide, shown as a pair.

3. Quotes.
   - "There is no confidence interval for Automation Rate." [@scaleaileaderboard]. Speaker: Scale AI, note under its own leaderboard. Role and interest: data and evaluation vendor, co-publisher with the Center for AI Safety. Local file: `converted/web/D_rli_scale.md`. Result: EXACT.
   - "more than quadrupled in under eight months" [@caisriseremote]. Speaker: Center for AI Safety, blog post of mid-2026. Role and interest: non-profit whose mission is to draw attention to AI risk, so fast progress supports its case. Local file: `converted/web/D_cais_blog.md`. Result: EXACT.

4. Example or case. What counts: a project is a real job taken from a freelance platform, on average 28.9 hours of human work, and it counts as automated only if a reasonable client would accept the deliverable as it is. In October 2025 the best agent delivered 6 of 240. In November 2026 the best agent delivered 99 of 240 (own arithmetic from the published rates).

5. Counter-evidence, in proportion. The conditions changed along the way: the budget per project rose from $30 at launch to $50, and to $150 for the mid-2026 leader, with 24 hours per project and a worker-and-critic loop [@caisriseremote]. There are no confidence intervals and no row dates. The project site's headline "×2 every ~3.3 months" [@caisremote] (primary) is the publisher's extrapolation, not a measurement. The 240 projects are a selected sample of remote freelance work, not of jobs. In the other direction, one-shot tests with a crisp deliverable show near parity with professionals, so 41% is not a ceiling on what models can do when the task is fully specified.

6. Speaker-note material. Corrections from the later notes: the main file gave the mid-2026 figure as "15.8% or 16.1%"; 16.1% appears nowhere at source, use 15.8%. The main file called the November 2026 rows "provider self-reports per one aggregator"; nothing on the official board marks any row as self-reported, and the 41.25% row is on the official board. The main file's GDPval figure of 40.6% for GPT-5 was not found as text; the paper's table gives 39.0%, and 47.6% for Opus 4.1 is confirmed. Third-party GDPval figures of 83% to 85% remain unverified. Who has an interest: both publishers benefit from a striking trend, in different ways; the grading is manual and the method is documented, which is in its favour.

7. Confidence and theses. High on the two end points, medium on the shape in between. Supports T3 ("revealing": this is the closest thing to a field measure among the benchmarks) and the first half of T1. It touches T2 (freelance occupations) without proving it: the index measures what agents can deliver, not what clients have stopped buying.

8. Question for the audience. Is your glass 41% full or 59% empty, and which of your own projects sit in which part?

9. Personal angle. From the brief (T1, T10): idea to proof of concept in hours, with many iterations and expert validation. One plain sentence for the slide: "A year ago an agent could finish one freelance job in forty; today it finishes two in five." Speaker to supply: one job of his own that he would now hand over whole, and one he would not.

## I2.6 How to read a benchmark headline: four questions before you repeat the number

1. Title as claim. A non-specialist can read any benchmark headline with four questions: who published it, which version and harness, who checked the answers, and how far the task is from my work.

2. Number or data series. No new number. Each question is backed by one figure from the insights above, which can sit in a backup slide.
   - Who published it, and what do they sell? The two main coding benchmarks were promoted and then disowned by a model vendor (I2.1); an earlier mathematics benchmark was funded by a vendor that had access to most of its problems, disclosed only on the day of the vendor's result [@techcrunch2025epoch] (secondary).
   - Which version and which harness? 62.7% or 99.9% for one model on one test; 86% on the old board and 44% on the new one (I2.4).
   - Who checked the answers? A script said "pass" where maintainers would send back about half (I2.2); a second, clean check caught a forged checksum (I2.3).
   - How far is the task from my work? Benchmark tasks are self-contained and fully specified; METR describes its own as what "a new hire or freelance contractor" with no context could do [@metr2026taskcompletion] (primary). On end-to-end freelance projects the best agent delivers 41% (I2.5).
   - What a benchmark does show honestly: the direction and the speed of change under fixed conditions, and the order of models tested the same way. Boards built in 2023 and 2024 were saturated within 12 to 24 months, which is itself a real signal.

3. Quotes.
   - "An 8-hour time horizon does not mean that AIs can do 8 hours of work that a (high-context) human professional can do as part of their day-to-day job." [@metr2026taskcompletion]. Speaker: METR, FAQ of its own time-horizon page. Role and interest: non-profit evaluator, partly lab-funded, limiting the reading of its own headline measure. Local file: `converted/web/metr_th.md`. Result: EXACT.
   - "those forecasting AI progress and its real-world impact should view benchmarks as one piece of evidence, rather than as decisive" [@metr2026manyswe]. Speaker: METR. Local file: `converted/web/I_metr_merge_note.md`. Result: EXACT.

4. Example or case. Desktop computer use. On the older test the best agent completes 86.0% of tasks, above the 72.36% that the project reports for humans [@xlanglabosworld] (primary). The headline writes itself: "better than humans at using a computer". On the new version of the same test, with 108 longer tasks that take a person a median of about 1.6 hours, the best agent completes 44.33% [@xlanglabosworldbenchmark] (primary). Both numbers are correct. Only the four questions tell them apart.

5. Counter-evidence, in proportion. The questions cut both ways. Benchmarks also understate: broken tests reject correct solutions (I2.1), and in METR's 2026 field study developers refused to work without AI, so the measured speed-up is described as a lower bound (see I3). A listener who leaves with "benchmarks are marketing" has learned the wrong half. A simulated business test gives a sense of proportion from the other side: the best model ends a simulated year with $16,484 from a $500 start, and the benchmark's authors estimate that a good human strategy would make about $63k [@andonlabsvendingbench] (primary).

6. Speaker-note material. This insight is a synthesis of I2.1 to I2.5 and adds no source of its own beyond the quotes. The FrontierMath funding story rests on press coverage and Epoch AI's later clarification [@epochaiclarification] (secondary); keep it for questions. If one sentence is needed about why vendors over-optimise: a study of a popular chat leaderboard reported that one vendor tested 27 private variants before a release and published the best [@singh2025leaderboard] (secondary; disputed by the leaderboard's co-founder, and written partly by a competing vendor).

7. Confidence and theses. High as a reading rule; it is deliberately modest. Supports T3 as worded in the brief: revealing and inflated at once. Feeds I11 (how to read claims).

8. Question for the audience. Take the last AI headline you forwarded to a colleague: can you answer even two of the four questions about it?

9. Personal angle. From the brief (Voice): one practitioner telling what he sees. One plain sentence for the slide: "Before I repeat a score, I ask who checked the answers." Speaker to supply: the last benchmark headline he himself believed and later revised.

## Bibliography additions needed

- Proposed key `arcprize2026astra`. ARC Prize Foundation, blog post on GPT-6 Astra's ARC-AGI-3 results, with the section "Two Harnesses, Two Questions" and the table of scores by reasoning effort for both harnesses. URL: https://arcprize.org/blog/astra . Year 2026 (results dated 2026-09-02; publication date not captured). Local copy: `converted/web/D_arc_astra.md`. Verification: primary page, scraped. Interest: non-profit benchmark owner. Exact title not captured in the local copy (it starts at "Summary"); use a bracketed descriptive title until checked. Needed for the per-effort figures in I2.4 (17.5% to 62.7% against 96.7% to 99.9%), which the notes attribute to the leaderboard page but which sit in this post and in `converted/web/D_arc_tables.md`.
- `metr2026manyswe`: add `file = {converted/web/I_metr_merge_note.md}`; the page was read in full on 2026-11-17 (the notes held it from a search extract). Title in the bibliography is already exact.
- The paper said to report that the mid-2026 ARC-AGI-3 gain "partially failed to transfer" to a held-out puzzle set has no key and no identified reference in the notes; it is cited in I2.4 without a key and should be identified or dropped.

## Open points

- The middle points of the Remote Labor Index series have no dates on the official board; the chart can place them only approximately. No confidence intervals exist.
- No official 2026 GDPval figure could be read; third-party figures of 83% to 85% are unverified and are not used.
- The METR mergeability result rests on four maintainers and on agents from 2024 and 2025; no replication with 2026 agents was found. The "70% equals 46%" conversion is unconfirmed and is not used.
- ImpossibleBench rates for 2025 models come from a search extract of the abstract, and rates for 2026 models from a vendor safety report read at second hand.
- The exact date of OpenAI's July 2026 post and the content of the Latent Space interview were not checked at source.
- SWE-Bench Pro V2 is undated, shows a confidence interval for one row only, and does not respond to OpenAI's retraction; whether the field accepts V2 is open.
- "Terminal-Bench 4.1" as a version name is an inference from the page.
- ARC-AGI-3 at launch (about 0.4%) is from secondary coverage; the later points are primary. Each verified score is a single run.
- All local web copies were made before provenance stamping of the converter ("converted by: unknown" in the verifier's output); a re-scrape would require re-checking the quotes.

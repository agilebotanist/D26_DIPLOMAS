Scraping: https://osworld-v2.xlang.ai/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://osworld-v2.xlang.ai/
  Settled (dom-quiet, 1443ms)
  Extracting content...
  Extracted 71644 characters

--- Content ---

## Abstract

Existing computer-use benchmarks fail to capture the realism, complexity, and long-horizon demands of real-world computer use, limiting their ability to reveal the limitations of frontier agents. We introduce OSWorld 2.0, a benchmark of 108 long-horizon computer-use workflows spanning everyday and professional tasks. Each task represents a realistic end-to-end workflow that takes human users a median of about 1.6 hours to complete and requires an average of 318 tool calls with Claude Opus 4.7 using maximum thinking, compared with about 30 in OSWorld 1.0. OSWorld 2.0 targets challenge phenomena that are common in real workflows yet underrepresented in prior benchmarks, spanning interaction-design challenges such as streaming interaction and dynamic environments, as well as agent-pattern challenges such as cross-source reasoning, implicit-state inference, and visual-spatial precision. Tasks are grounded in authentic input artifacts and cross-referenced against realistic stateful user profile data, and include separate safety reports auditing safety-sensitive execution. Under our primary binary-completion metric at 500 steps, Claude Opus 4.8 with maximum thinking and batched tool calls scores best but still completes only 20.6% of tasks at a 54.8% partial score; GPT-5.5 is far more token-efficient yet plateaus near 14%. These results show that current agents are still far from professional-level computer use: rather than stumbling on basic GUI control or coding, they lose track of constraints, miss information that arrives mid-task, guess rather than ask the user, and skip verification, struggling most when a task hinges on hidden state they must recover.

![Representative OSWorld 2.0 long-horizon workflows and challenge categories](static/images/osworld2/osworldv2_figure_main_latest.png?v=main-fig-latest-v1)

A representative OSWorld 2.0 workflow: submitting an ExpenseFlow reimbursement claim. The agent must follow a tutorial PDF, operate a legacy reimbursement portal, extract the correct amount from noisy receipt artifacts, trace order evidence across GMail and ChaseBank, react to a new email that changes the task state, recover hidden employee information from a prior report, gather supporting documents across applications, identify an inconsistency that requires user clarification, and complete final review and submission.

X

Y

<svg id="benchmarkSweepChart" viewBox="0 0 1038 590" role="img" aria-label="Interactive OSWorld 2.0 sweep chart" aria-describedby="benchmarkSweepCaption" style="height: 590px;"><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="76" y1="34" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="76" y1="178" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="298.24" x2="298.24" y1="34" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="298.24" x2="298.24" y1="178" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="520.48" x2="520.48" y1="34" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="520.48" x2="520.48" y1="178" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="742.72" x2="742.72" y1="34" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="742.72" x2="742.72" y1="178" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="964.9599999999999" x2="964.9599999999999" y1="34" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="964.9599999999999" x2="964.9599999999999" y1="178" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="519" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="433.75" y2="433.75"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="348.5" y2="348.5"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="263.25" y2="263.25"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="178" y2="178"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="140" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="86.99999999999994" y2="86.99999999999994"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="34" y2="34"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="1002" y1="519" y2="519"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="76" y1="34" y2="140"></line><line stroke-opacity="0.2" stroke="currentColor" x1="76" x2="76" y1="178" y2="519"></line><path stroke="currentColor" fill="none" d="M 70 150 L 82 156 L 70 162 L 82 168"></path><g transform="translate(856.00 58.00)"><rect stroke="currentColor" fill="none" x="-1" y="-7" width="9" height="9" rx="1.8" transform="rotate(45 3.5 -2.5)"></rect><text x="18" y="1">OSWorld 1.0 score</text> <circle stroke="currentColor" fill="none" cx="3.5" cy="18" r="4.8"></circle><text x="18" y="22">OSWorld 2.0 score</text></g> <text fill="currentColor" x="76" y="546" text-anchor="middle">0</text> <text fill="currentColor" x="298.24" y="546" text-anchor="middle">60K</text> <text fill="currentColor" x="520.48" y="546" text-anchor="middle">120K</text> <text fill="currentColor" x="742.72" y="546" text-anchor="middle">180K</text> <text fill="currentColor" x="964.9599999999999" y="546" text-anchor="middle">240K</text> <text fill="currentColor" x="66" y="523" text-anchor="end">0%</text> <text fill="currentColor" x="66" y="437.75" text-anchor="end">10%</text> <text fill="currentColor" x="66" y="352.5" text-anchor="end">20%</text> <text fill="currentColor" x="66" y="267.25" text-anchor="end">30%</text> <text fill="currentColor" x="66" y="182" text-anchor="end">40%</text> <text fill="currentColor" x="66" y="144" text-anchor="end">75%</text> <text fill="currentColor" x="66" y="90.99999999999994" text-anchor="end">80%</text> <text fill="currentColor" x="66" y="38" text-anchor="end">85%</text> <text fill="currentColor" x="539" y="572" text-anchor="middle">Output tokens / task</text> <g transform="translate(898.00 489.00)"><text fill="currentColor" x="41" y="-18" text-anchor="middle">Reasoning Effort</text> <circle cx="5.116" cy="-5" r="3.1159999999999997" fill="#2f3540" opacity="0.74"></circle><text x="5.116" y="12" text-anchor="middle">low</text> <line x1="15.232" y1="-5" x2="65.604" y2="-5" stroke="#6f7785" stroke-width="1.2" stroke-linecap="round"></line><path d="M 64.604 -8.5 L 69.604 -5 L 64.604 -1.5" fill="none" stroke="#6f7785" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"></path><circle cx="82" cy="-5" r="6.396" fill="#2f3540" opacity="0.74"></circle><text x="82" y="12" text-anchor="middle">max</text></g> <text fill="currentColor" x="20" y="276.5" transform="rotate(-90 20 276.5)" text-anchor="middle">Score</text> <rect x="151.238" y="45.77000000000001" width="12.5" height="12.5" rx="2.2" fill="#f26d37" data-id="osworld-v1-reference-0" transform="rotate(45 157.488 52.02000000000001)"></rect><g transform="translate(172.49 59.02)"><g transform="translate(9 0)" stroke="#f26d37" stroke-width="2.05"><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(0)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(30)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(60)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(90)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(120)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(150)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(180)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(210)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(240)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(270)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(300)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(330)"></line><circle cx="0" cy="0" r="1.8" fill="#f26d37" stroke="none"></circle></g><text x="24" y="5" fill="#f26d37">Claude Opus 4.8</text></g> <rect x="90.4924" y="93.46999999999994" width="12.5" height="12.5" rx="2.2" fill="#20242c" data-id="osworld-v1-reference-1" transform="rotate(45 96.7424 99.71999999999994)"></rect><g transform="translate(110.74 106.72)"><g transform="translate(1 -8) scale(1.05)" fill="#20242c"><path d="M14.949 6.547a3.94 3.94 0 0 0-.348-3.273 4.11 4.11 0 0 0-4.4-1.934A4.1 4.1 0 0 0 8.423.2 4.15 4.15 0 0 0 6.305.086a4.1 4.1 0 0 0-1.891.948 4.04 4.04 0 0 0-1.158 1.753 4.1 4.1 0 0 0-1.563.679A4 4 0 0 0 .554 4.72a3.99 3.99 0 0 0 .502 4.731 3.94 3.94 0 0 0 .346 3.274 4.11 4.11 0 0 0 4.402 1.933c.382.425.852.764 1.377.995.526.231 1.095.35 1.67.346 1.78.002 3.358-1.132 3.901-2.804a4.1 4.1 0 0 0 1.563-.68 4 4 0 0 0 1.14-1.253 3.99 3.99 0 0 0-.506-4.716m-6.097 8.406a3.05 3.05 0 0 1-1.945-.694l.096-.054 3.23-1.838a.53.53 0 0 0 .265-.455v-4.49l1.366.778q.02.011.025.035v3.722c-.003 1.653-1.361 2.992-3.037 2.996m-6.53-2.75a2.95 2.95 0 0 1-.36-2.01l.095.057L5.29 12.09a.53.53 0 0 0 .527 0l3.949-2.246v1.555a.05.05 0 0 1-.022.041L6.473 13.3c-1.454.826-3.311.335-4.15-1.098m-.85-6.94A3.02 3.02 0 0 1 3.07 3.949v3.785a.51.51 0 0 0 .262.451l3.93 2.237-1.366.779a.05.05 0 0 1-.048 0L2.585 9.342a2.98 2.98 0 0 1-1.113-4.094zm11.216 2.571L8.747 5.576l1.362-.776a.05.05 0 0 1 .048 0l3.265 1.86a3 3 0 0 1 1.173 1.207 2.96 2.96 0 0 1-.27 3.2 3.05 3.05 0 0 1-1.36.997V8.279a.52.52 0 0 0-.276-.445m1.36-2.015-.097-.057-3.226-1.855a.53.53 0 0 0-.53 0L6.249 6.153V4.598a.04.04 0 0 1 .019-.04L9.533 2.7a3.07 3.07 0 0 1 3.257.139c.474.325.843.778 1.066 1.303.223.526.289 1.103.191 1.664zM5.503 8.575 4.139 7.8a.05.05 0 0 1-.026-.037V4.049c0-.57.166-1.127.476-1.607s.752-.864 1.275-1.105a3.08 3.08 0 0 1 3.234.41l-.096.054-3.23 1.838a.53.53 0 0 0-.265.455zm.742-1.577 1.758-1 1.762 1v2l-1.755 1-1.762-1z"></path></g><text x="24" y="5" fill="#20242c">GPT-5.5</text></g> <line stroke-opacity="0.2" stroke="currentColor" id="benchmarkCrosshairX" x1="0" x2="0" y1="34" y2="519" opacity="0"></line><line stroke-opacity="0.2" stroke="currentColor" id="benchmarkCrosshairY" x1="76" x2="1002" y1="0" y2="0" opacity="0"></line><path fill="none" d="M 90.69 511.07 L 134.84 440.06 L 170.29 424.29 L 218.93 400.59" stroke="#20242c" pathLength="1" data-release-version="v2026.06.24"></path><path fill="none" d="M 196.95 328.72 L 227.29 303.06 L 286.38 271.95 L 346.85 261.46 L 457.02 251.06" stroke="#16806f" pathLength="1" data-release-version="v2026.08.08"></path><path fill="none" d="M 362.07 413.29 L 510.42 391.98 L 564.62 382.60 L 788.28 366.40 L 978.26 343.38" stroke="#f26d37" pathLength="1" data-release-version="v2026.06.24"></path><path fill="none" d="M 160.12 471.60 L 218.40 432.13 L 314.64 422.50 L 432.95 392.74 L 633.41 363.85" stroke="#d68a1d" pathLength="1" data-release-version="v2026.06.24"></path><path fill="none" d="M 447.95 440.06 L 764.59 432.17" stroke="#f0d66b" pathLength="1" data-release-version="v2026.06.24"></path><circle cx="90.68636" cy="511.07175" r="3.80" fill="#20242c" data-id="gpt55-low" style="animation: fade-up 420ms ease 0ms both;"></circle><circle cx="134.83804" cy="440.0585" r="4.80" fill="#20242c" data-id="gpt55-medium" style="animation: fade-up 420ms ease 35ms both;"></circle><circle cx="170.28902399999998" cy="424.28725" r="5.80" fill="#20242c" data-id="gpt55-high" style="animation: fade-up 420ms ease 70ms both;"></circle><circle cx="218.92624800000002" cy="400.58775" r="6.80" fill="#20242c" data-id="gpt55-xhigh" style="animation: fade-up 420ms ease 105ms both;"></circle><circle cx="362.067328" cy="413.29" r="3.80" fill="#f26d37" data-id="opus48-low" style="animation: fade-up 420ms ease 140ms both;"></circle><circle cx="510.416232" cy="391.9775" r="4.80" fill="#f26d37" data-id="opus48-medium" style="animation: fade-up 420ms ease 175ms both;"></circle><circle cx="564.6168640000001" cy="382.6" r="5.80" fill="#f26d37" data-id="opus48-high" style="animation: fade-up 420ms ease 210ms both;"></circle><circle cx="788.282904" cy="366.40250000000003" r="6.80" fill="#f26d37" data-id="opus48-xhigh" style="animation: fade-up 420ms ease 245ms both;"></circle><circle cx="978.264768" cy="343.385" r="7.80" fill="#f26d37" data-id="opus48-max" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="160.121544" cy="471.601" r="3.80" fill="#d68a1d" data-id="opus47-low" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="218.403984" cy="432.13025" r="4.80" fill="#d68a1d" data-id="opus47-medium" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="314.637608" cy="422.497" r="5.80" fill="#d68a1d" data-id="opus47-high" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="432.95448" cy="392.74475" r="6.80" fill="#d68a1d" data-id="opus47-xhigh" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="633.4149600000001" cy="363.845" r="7.80" fill="#d68a1d" data-id="opus47-max" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="447.95413654320004" cy="440.06481481481484" r="4.80" fill="#f0d66b" data-id="sonnet46-medium" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="764.5903709712001" cy="432.1712962962963" r="7.80" fill="#f0d66b" data-id="sonnet46-max" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="338.18764" cy="479.52925" r="4.80" fill="#f05aa6" data-id="minimax-enabled" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="215.903784" cy="495.3005" r="4.80" fill="#8d6bd8" data-id="qwen-thinking" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="196.95041600000002" cy="328.722" r="3.80" fill="#16806f" data-id="opus5-low-v20260808-full" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="227.28988" cy="303.06175" r="4.80" fill="#16806f" data-id="opus5-medium-v20260808-full" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="286.376088" cy="271.94550000000004" r="5.80" fill="#16806f" data-id="opus5-high-v20260808-full" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="346.851296" cy="261.45975000000004" r="6.80" fill="#16806f" data-id="opus5-xhigh-v20260808-full" style="animation: fade-up 420ms ease 260ms both;"></circle><circle cx="457.019368" cy="251.05924999999996" r="7.80" fill="#16806f" data-id="opus5-max-v20260808-full" style="animation: fade-up 420ms ease 260ms both;"></circle><g transform="translate(226.93 384.59)"><g transform="translate(1 -8) scale(1.05)" fill="#20242c"><path d="M14.949 6.547a3.94 3.94 0 0 0-.348-3.273 4.11 4.11 0 0 0-4.4-1.934A4.1 4.1 0 0 0 8.423.2 4.15 4.15 0 0 0 6.305.086a4.1 4.1 0 0 0-1.891.948 4.04 4.04 0 0 0-1.158 1.753 4.1 4.1 0 0 0-1.563.679A4 4 0 0 0 .554 4.72a3.99 3.99 0 0 0 .502 4.731 3.94 3.94 0 0 0 .346 3.274 4.11 4.11 0 0 0 4.402 1.933c.382.425.852.764 1.377.995.526.231 1.095.35 1.67.346 1.78.002 3.358-1.132 3.901-2.804a4.1 4.1 0 0 0 1.563-.68 4 4 0 0 0 1.14-1.253 3.99 3.99 0 0 0-.506-4.716m-6.097 8.406a3.05 3.05 0 0 1-1.945-.694l.096-.054 3.23-1.838a.53.53 0 0 0 .265-.455v-4.49l1.366.778q.02.011.025.035v3.722c-.003 1.653-1.361 2.992-3.037 2.996m-6.53-2.75a2.95 2.95 0 0 1-.36-2.01l.095.057L5.29 12.09a.53.53 0 0 0 .527 0l3.949-2.246v1.555a.05.05 0 0 1-.022.041L6.473 13.3c-1.454.826-3.311.335-4.15-1.098m-.85-6.94A3.02 3.02 0 0 1 3.07 3.949v3.785a.51.51 0 0 0 .262.451l3.93 2.237-1.366.779a.05.05 0 0 1-.048 0L2.585 9.342a2.98 2.98 0 0 1-1.113-4.094zm11.216 2.571L8.747 5.576l1.362-.776a.05.05 0 0 1 .048 0l3.265 1.86a3 3 0 0 1 1.173 1.207 2.96 2.96 0 0 1-.27 3.2 3.05 3.05 0 0 1-1.36.997V8.279a.52.52 0 0 0-.276-.445m1.36-2.015-.097-.057-3.226-1.855a.53.53 0 0 0-.53 0L6.249 6.153V4.598a.04.04 0 0 1 .019-.04L9.533 2.7a3.07 3.07 0 0 1 3.257.139c.474.325.843.778 1.066 1.303.223.526.289 1.103.191 1.664zM5.503 8.575 4.139 7.8a.05.05 0 0 1-.026-.037V4.049c0-.57.166-1.127.476-1.607s.752-.864 1.275-1.105a3.08 3.08 0 0 1 3.234.41l-.096.054-3.23 1.838a.53.53 0 0 0-.265.455zm.742-1.577 1.758-1 1.762 1v2l-1.755 1-1.762-1z"></path></g><text x="24" y="5" fill="#20242c">GPT-5.5</text> <g transform="translate(76.44 -7)" data-release-version="v2026.06.24"><rect width="38" height="15" rx="4" fill="#fff6cf" stroke="#d4ae2d" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#665214" text-anchor="middle">0624</text></g></g> <g transform="translate(469.02 229.06)"><g transform="translate(9 0)" stroke="#16806f" stroke-width="2.05"><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(0)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(30)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(60)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(90)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(120)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(150)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(180)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(210)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(240)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(270)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(300)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(330)"></line><circle cx="0" cy="0" r="1.8" fill="#16806f" stroke="none"></circle></g><text x="24" y="5" fill="#16806f">Claude Opus 5</text> <g transform="translate(120.86 -7)" data-release-version="v2026.08.08"><rect width="38" height="15" rx="4" fill="#e5f3ff" stroke="#4d9ad2" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#245f8c" text-anchor="middle">0808</text></g></g> <g transform="translate(828.64 371.38)"><g transform="translate(9 0)" stroke="#f26d37" stroke-width="2.05"><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(0)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(30)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(60)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(90)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(120)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(150)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(180)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(210)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(240)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(270)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(300)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(330)"></line><circle cx="0" cy="0" r="1.8" fill="#f26d37" stroke="none"></circle></g><text x="24" y="5" fill="#f26d37">Claude Opus 4.8</text> <g transform="translate(131.36 -7)" data-release-version="v2026.06.24"><rect width="38" height="15" rx="4" fill="#fff6cf" stroke="#d4ae2d" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#665214" text-anchor="middle">0624</text></g></g> <g transform="translate(615.41 319.85)"><g transform="translate(9 0)" stroke="#d68a1d" stroke-width="2.05"><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(0)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(30)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(60)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(90)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(120)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(150)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(180)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(210)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(240)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(270)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(300)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(330)"></line><circle cx="0" cy="0" r="1.8" fill="#d68a1d" stroke="none"></circle></g><text x="24" y="5" fill="#d68a1d">Claude Opus 4.7</text> <g transform="translate(131.36 -7)" data-release-version="v2026.06.24"><rect width="38" height="15" rx="4" fill="#fff6cf" stroke="#d4ae2d" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#665214" text-anchor="middle">0624</text></g></g> <g transform="translate(752.59 467.17)"><g transform="translate(9 0)" stroke="#c9a61f" stroke-width="2.05"><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(0)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(30)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(60)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(90)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(120)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(150)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(180)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(210)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(240)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(270)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(300)"></line><line x1="0" y1="-2.6" x2="0" y2="-8.6" transform="rotate(330)"></line><circle cx="0" cy="0" r="1.8" fill="#c9a61f" stroke="none"></circle></g><text x="24" y="5" fill="#c9a61f">Claude Sonnet 4.6</text> <g transform="translate(141.48 -7)" data-release-version="v2026.06.24"><rect width="38" height="15" rx="4" fill="#fff6cf" stroke="#d4ae2d" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#665214" text-anchor="middle">0624</text></g></g> <g transform="translate(352.19 471.53)"><g transform="translate(0 0)" stroke="#f05aa6" stroke-width="2.1"><line x1="3" y1="-3.8" x2="3" y2="3.8"></line><line x1="7" y1="-7.2" x2="7" y2="7.2"></line><line x1="11" y1="-9.5" x2="11" y2="9.5"></line><line x1="15" y1="-7.2" x2="15" y2="7.2"></line><line x1="19" y1="-3.8" x2="19" y2="3.8"></line></g><text x="24" y="5" fill="#f05aa6">MiniMax M3</text> <g transform="translate(110.39 -7)" data-release-version="v2026.06.24"><rect width="38" height="15" rx="4" fill="#fff6cf" stroke="#d4ae2d" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#665214" text-anchor="middle">0624</text></g></g> <g transform="translate(229.90 513.30)"><g transform="translate(0 -9) scale(0.095)"><path d="M174.82 108.75L155.38 75L165.64 57.75C166.46 56.31 166.46 54.53 165.64 53.09L155.38 35.84C154.86 34.91 153.87 34.33 152.78 34.33H114.88L106.14 19.03C105.62 18.1 104.63 17.52 103.54 17.52H83.3C82.21 17.52 81.22 18.1 80.7 19.03L61.26 52.77H41.02C39.93 52.77 38.94 53.35 38.42 54.28L28.16 71.53C27.34 72.97 27.34 74.75 28.16 76.19L45.52 107.5L36.78 122.8C35.96 124.24 35.96 126.02 36.78 127.46L47.04 144.71C47.56 145.64 48.55 146.22 49.64 146.22H87.54L96.28 161.52C96.8 162.45 97.79 163.03 98.88 163.03H119.12C120.21 163.03 121.2 162.45 121.72 161.52L141.16 127.78H158.52C159.61 127.78 160.6 127.2 161.12 126.27L171.38 109.02C172.2 107.58 172.2 105.8 171.38 104.36L174.82 108.75Z" fill="#8d6bd8"></path><path d="M119.12 163.03H98.88L87.54 144.71H49.64L61.26 126.39H80.7L38.42 55.29H61.26L83.3 19.03L93.56 37.35L83.3 55.29H161.58L151.32 72.54L170.76 106.28H151.32L141.16 88.34L101.18 163.03H119.12Z" fill="#ffffff"></path><path d="M127.86 79.83H76.14L101.18 122.11L127.86 79.83Z" fill="#8d6bd8"></path></g><text x="24" y="5" fill="#8d6bd8">Qwen 3.7-Plus</text> <g transform="translate(118.53 -7)" data-release-version="v2026.06.24"><rect width="38" height="15" rx="4" fill="#fff6cf" stroke="#d4ae2d" stroke-width="0.65"></rect><text x="19" y="10.7" fill="#665214" text-anchor="middle">0624</text></g></g></svg>

Compare model performance against output tokens, turns, actions, or cost.

| Model | Effort | Version | X metric | Binary reward | Partial reward |
| --- | --- | --- | --- | --- | --- |
| Claude Opus 5 | max | v2026.08.08 | 103K | 31.4% | 68.3% |
| Claude Opus 5 | xhigh | v2026.08.08 | 73.1K | 30.2% | 67.7% |
| Claude Opus 5 | high | v2026.08.08 | 56.8K | 29.0% | 63.8% |
| GPT-5.6 Sol | max | v2026.08.08 | 36.1K | 27.3% | 62.7% |
| Claude Opus 5 | medium | v2026.08.08 | 40.8K | 25.3% | 60.5% |
| Claude Opus 5 | low | v2026.08.08 | 32.7K | 22.3% | 54.9% |
| Claude Opus 4.8 | max | v2026.06.24 | 244K | 20.6% | 54.8% |
| Claude Opus 4.7 | max | v2026.06.24 | 150K | 18.2% | 48.9% |
| Claude Opus 4.8 | xhigh | v2026.06.24 | 192K | 17.9% | 49.7% |
| Claude Opus 4.8 | high | v2026.06.24 | 132K | 16.0% | 49.0% |
| Claude Opus 4.8 | medium | v2026.06.24 | 117K | 14.9% | 48.6% |
| Claude Opus 4.7 | xhigh | v2026.06.24 | 96.4K | 14.8% | 46.7% |
| GPT-5.5 | xhigh | v2026.06.24 | 38.6K | 13.9% | 47.5% |
| Claude Opus 4.8 | low | v2026.06.24 | 77.2K | 12.4% | 47.3% |
| Claude Opus 4.7 | high | v2026.06.24 | 64.4K | 11.3% | 41.6% |
| GPT-5.5 | high | v2026.06.24 | 25.5K | 11.1% | 40.4% |
| Claude Opus 4.7 | medium | v2026.06.24 | 38.4K | 10.2% | 37.3% |
| Claude Sonnet 4.6 | max | v2026.06.24 | 186K | 10.2% | 41.5% |
| GPT-5.5 | medium | v2026.06.24 | 15.9K | 9.3% | 36.9% |
| Claude Sonnet 4.6 | medium | v2026.06.24 | 100K | 9.3% | 33.9% |
| Claude Opus 4.7 | low | v2026.06.24 | 22.7K | 5.6% | 29.9% |
| MiniMax M3 | enabled | v2026.06.24 | 70.8K | 4.6% | 22.3% |
| Qwen 3.7-Plus | thinking | v2026.06.24 | 37.8K | 2.8% | 21.5% |
| GPT-5.5 | low | v2026.06.24 | 4K | 0.9% | 16.3% |

## Task Statistics

### Human Operation Time

OSWorld 2.0 tasks require substantially longer human operation time, with a median of about 1.6 hours and 69.6% of tasks taking skilled users more than one hour.

![Human operation time comparison between OSWorld 1.0 and OSWorld 2.0](static/images/osworld2/osworld_human_time_v1_v2_comparison.png?v=figure3-no-title-v1)

Human operation time comparison between OSWorld 1.0 and OSWorld 2.0

### Task Domain Distribution

The 108 tasks span seven professional domains and 21 sub-categories, covering research, creative production, engineering, personal services, business and finance, administration and compliance, and healthcare workflows.

<svg id="domain-donut" viewBox="0 0 520 520" role="img" aria-label="OSWorld 2.0 task domain distribution. Interactive two-ring donut chart showing seven domains and their sub-categories."><defs></defs><path d="M 412.03955590479313 198.5185114016155 A 164 164 0 0 0 244.42376067023153 96.74136847216386 L 254.8712382694665 206.24410913107835 A 54 54 0 0 1 310.0618049930416 239.7560952176051 Z" fill="#0b83d5" tabindex="0" role="button" aria-label="Research &amp; Education, 20.6%" data-domain="research" style="--lift-x: 6.23px; --lift-y: -10.26px;"></path><text x="322.8010475857256" y="156.5735603332715" text-anchor="middle" dominant-baseline="middle"><tspan x="322.8010475857256" dy="-0.36em">Research</tspan> <tspan x="322.8010475857256" dy="1.02em">Education</tspan></text> <path d="M 425.86006413926316 78.32325651388535 A 246 246 0 0 0 236.20826671041715 15.153204172328685 L 243.55855829581674 90.79692971258487 A 170 170 0 0 1 374.61874351087295 134.4510309242297 Z" fill="rgb(158, 210, 242)" tabindex="0" role="button" aria-label="Academic, 13.5%" data-domain="research" style="--lift-x: 4.74px; --lift-y: -14.23px;"></path><path d="M 488.21994458209133 168.1759459893696 A 246 246 0 0 0 428.6932566528734 80.95088617966357 L 376.57664077637594 136.26687256318212 A 170 170 0 0 1 417.71296983315256 196.54435291948306 Z" fill="rgb(163, 212, 243)" tabindex="0" role="button" aria-label="Teaching / Coursework, 7.1%" data-domain="research" style="--lift-x: 12.39px; --lift-y: -8.46px;"></path><path d="M 363.05700707537693 387.5745009500947 A 164 164 0 0 0 413.1918241936239 201.44861231166414 L 310.44121040521765 240.7208845416455 A 54 54 0 0 1 293.9334047687217 302.00623811771413 Z" fill="#f47b00" tabindex="0" role="button" aria-label="Creative Production, 20.2%" data-domain="creative" style="--lift-x: 11.59px; --lift-y: 3.12px;"></path><text x="376.8357238573331" y="291.47083778250914" text-anchor="middle" dominant-baseline="middle"><tspan x="376.8357238573331" dy="0em">Creative</tspan></text> <path d="M 505.9674263799311 255.99685623126285 A 246 246 0 0 0 489.6340992070954 171.7719971814738 L 418.6902311593749 199.02942894654694 A 170 170 0 0 1 429.97748977474913 257.23359983461256 Z" fill="rgb(255, 199, 127)" tabindex="0" role="button" aria-label="Presentation, 5.8%" data-domain="creative" style="--lift-x: 14.73px; --lift-y: -2.86px;"></path><path d="M 491.08717467477584 344.3487860068515 A 246 246 0 0 0 505.99996063836664 259.86083850369664 L 429.9999727988712 259.90383148629445 A 170 170 0 0 1 419.6943890028939 318.2898114681494 Z" fill="rgb(255, 202, 134)" tabindex="0" role="button" aria-label="Video Production, 5.8%" data-domain="creative" style="--lift-x: 14.77px; --lift-y: 2.61px;"></path><path d="M 455.37553359846925 409.4804364159853 A 246 246 0 0 0 489.7337728768397 347.9681396857558 L 418.75911133765345 320.7909908397499 A 170 170 0 0 1 395.01561264934867 363.29948858015246 Z" fill="rgb(255, 205, 141)" tabindex="0" role="button" aria-label="Audio Production, 4.8%" data-domain="creative" style="--lift-x: 13.10px; --lift-y: 7.31px;"></path><path d="M 414.2512860730179 451.6312624412311 A 246 246 0 0 0 453.0034939570496 412.5308208867018 L 393.37639826300176 365.40747784853374 A 170 170 0 0 1 366.5964172049311 392.4281081910947 Z" fill="rgb(255, 208, 148)" tabindex="0" role="button" aria-label="Media Operations, 3.8%" data-domain="creative" style="--lift-x: 10.65px; --lift-y: 10.56px;"></path><path d="M 194.18265154042763 410.21343695472524 A 164 164 0 0 0 360.5889107845346 389.5294214731963 L 293.12073891685895 302.6499314606866 A 54 54 0 0 1 238.32843404379935 309.46052192411685 Z" fill="#43a047" tabindex="0" role="button" aria-label="Engineering &amp; Computing, 17.3%" data-domain="engineering" style="--lift-x: 1.48px; --lift-y: 11.91px;"></path><text x="274.92523851187593" y="380.07596451981397" text-anchor="middle" dominant-baseline="middle"><tspan x="274.92523851187593" dy="-0.36em">Engineering</tspan> <tspan x="274.92523851187593" dy="1.02em">Computing</tspan></text> <path d="M 321.9704356455093 498.06651403737106 A 246 246 0 0 0 411.2222434286253 454.0304952640528 L 364.503176353115 394.0861146133698 A 170 170 0 0 1 302.82509780380724 424.51750970062227 Z" fill="rgb(169, 223, 189)" tabindex="0" role="button" aria-label="CAD / EDA / 3D Engineering, 6.7%" data-domain="engineering" style="--lift-x: 6.64px; --lift-y: 13.45px;"></path><path d="M 232.6032999288782 504.4696726083074 A 246 246 0 0 0 318.2234042293494 499.0105336589703 L 300.2356858495504 425.16988098384127 A 170 170 0 0 1 241.06732108906215 428.9424566805376 Z" fill="rgb(174, 225, 193)" tabindex="0" role="button" aria-label="Software / Web Development, 5.8%" data-domain="engineering" style="--lift-x: 0.95px; --lift-y: 14.97px;"></path><path d="M 188.54196800900013 495.3927561841554 A 246 246 0 0 0 228.76671707100112 504.00918433017455 L 238.41602399215526 428.62423307369784 A 170 170 0 0 1 210.61843317695133 422.6697908589692 Z" fill="rgb(178, 227, 196)" tabindex="0" role="button" aria-label="Cloud / DevOps / MLOps, 2.9%" data-domain="engineering" style="--lift-x: -3.14px; --lift-y: 14.67px;"></path><path d="M 160.88087002025048 485.1475029221011 A 246 246 0 0 0 184.85339489478383 494.2413023810291 L 208.06941923623273 421.87407075111764 A 170 170 0 0 1 191.50304025789666 415.5897377916959 Z" fill="rgb(183, 228, 200)" tabindex="0" role="button" aria-label="Robotics Simulation, 1.9%" data-domain="engineering" style="--lift-x: -5.32px; --lift-y: 14.02px;"></path><path d="M 107.0088281592306 319.07369413527624 A 164 164 0 0 0 191.31106707633649 408.92222968317543 L 237.38291233001323 309.03536831031386 A 54 54 0 0 1 209.6248580524296 279.45109441039585 Z" fill="#f6b30d" tabindex="0" role="button" aria-label="Personal Services, 12.5%" data-domain="services" style="--lift-x: -8.75px; --lift-y: 8.21px;"></path><text x="171.75993371534707" y="342.7930595042849" text-anchor="middle" dominant-baseline="middle"><tspan x="171.75993371534707" dy="0em">Personal</tspan></text> <path d="M 77.17987652461568 424.59891388598294 A 246 246 0 0 0 157.35663483097457 483.56283140714174 L 189.06759317587674 414.49463959030123 A 170 170 0 0 1 133.6608902812385 373.74721691307764 Z" fill="rgb(255, 227, 156)" tabindex="0" role="button" aria-label="Games / Visual Search, 6.7%" data-domain="services" style="--lift-x: -8.89px; --lift-y: 12.08px;"></path><path d="M 36.383185539251514 362.5257055105069 A 246 246 0 0 0 74.61702321996319 421.70699403604135 L 131.8898127942835 371.74873571596356 A 170 170 0 0 1 105.46805504745024 330.8510973040089 Z" fill="rgb(255, 229, 161)" tabindex="0" role="button" aria-label="Events / Ticketing, 4.8%" data-domain="services" style="--lift-x: -12.60px; --lift-y: 8.14px;"></path><path d="M 30.358937275998215 348.2098764934578 A 246 246 0 0 0 34.80036880163871 359.00063690765865 L 104.37423860275845 328.41507428578035 A 170 170 0 0 1 101.30495665414509 320.9580447312513 Z" fill="rgb(255, 230, 167)" tabindex="0" role="button" aria-label="Everyday Services, 1.0%" data-domain="services" style="--lift-x: -13.87px; --lift-y: 5.71px;"></path><path d="M 110.31076314079115 192.99901218259788 A 164 164 0 0 0 105.90295873719742 316.12576836044315 L 209.26073031590647 278.48043592356055 A 54 54 0 0 1 210.71208054635807 237.93869913329442 Z" fill="#7650b8" tabindex="0" role="button" aria-label="Administration &amp; Compliance, 12.5%" data-domain="compliance" style="--lift-x: -11.99px; --lift-y: -0.43px;"></path><text x="139.0774600799667" y="255.67110414909826" text-anchor="middle" dominant-baseline="middle"><tspan x="139.0774600799667" dy="-0.36em">Admin</tspan> <tspan x="139.0774600799667" dy="1.02em">Compliance</tspan></text> <path d="M 25.17862149644381 186.6861527561839 A 246 246 0 0 0 29.001727003896093 344.5919492198723 L 100.36704711651356 318.4578510869036 A 170 170 0 0 1 97.72506363575386 209.33595922175311 Z" fill="rgb(201, 182, 237)" tabindex="0" role="button" aria-label="Office, 10.6%" data-domain="compliance" style="--lift-x: -15.00px; --lift-y: 0.36px;"></path><path d="M 35.641894782589674 159.10678603962782 A 246 246 0 0 0 26.35915468917176 183.00678339982392 L 98.54087925674472 206.79330560150433 A 170 170 0 0 1 104.95578094731806 190.27704726315744 Z" fill="rgb(204, 186, 238)" tabindex="0" role="button" aria-label="Legal, 1.9%" data-domain="compliance" style="--lift-x: -13.98px; --lift-y: -5.43px;"></path><path d="M 202.135761647056 106.54730396687816 A 164 164 0 0 0 111.62459665701155 190.1377091500322 L 211.14468426511357 236.99656276891307 A 54 54 0 0 1 240.9471410301282 209.47289276958185 Z" fill="#10b981" tabindex="0" role="button" aria-label="Business &amp; Finance, 12.5%" data-domain="business" style="--lift-x: -8.14px; --lift-y: -8.82px;"></path><text x="177.90603097598313" y="171.10916667122666" text-anchor="middle" dominant-baseline="middle"><tspan x="177.90603097598313" dy="-0.36em">Business</tspan> <tspan x="177.90603097598313" dy="1.02em">Finance</tspan></text> <path d="M 86.65462617857153 85.45091986862482 A 246 246 0 0 0 37.254335011534494 155.595169034923 L 106.07006891041001 187.8503200647842 A 170 170 0 0 1 140.20848150551691 139.3766519417326 Z" fill="rgb(167, 228, 205)" tabindex="0" role="button" aria-label="Market Analysis, 5.8%" data-domain="business" style="--lift-x: -12.26px; --lift-y: -8.64px;"></path><path d="M 133.1055787698258 49.254167631577786 A 246 246 0 0 0 89.41770915526541 82.74966276431974 L 142.11792909103707 137.50992955257868 A 170 170 0 0 1 172.30873329622108 114.3626361681635 Z" fill="rgb(172, 229, 208)" tabindex="0" role="button" aria-label="Procurement / Loan, 3.8%" data-domain="business" style="--lift-x: -9.13px; --lift-y: -11.90px;"></path><path d="M 173.6055126837781 29.669818388107956 A 246 246 0 0 0 136.43148508081862 47.28699588255529 L 174.60712383633808 113.0032085367252 A 170 170 0 0 1 200.29649250504988 100.82873628446484 Z" fill="rgb(177, 231, 211)" tabindex="0" role="button" aria-label="Sales, 2.9%" data-domain="business" style="--lift-x: -6.42px; --lift-y: -13.55px;"></path><path d="M 241.29248300732257 97.07047901632839 A 164 164 0 0 0 205.09232461794764 105.46473805587553 L 241.92064347176324 209.11643814034926 A 54 54 0 0 1 253.84020781948425 206.35247479805935 Z" fill="#f05252" tabindex="0" role="button" aria-label="Healthcare, 3.9%" data-domain="healthcare" style="--lift-x: -2.71px; --lift-y: -11.69px;"></path><text x="232.667191689889" y="142.1275367616222" text-anchor="middle" dominant-baseline="middle"><tspan x="232.667191689889" dy="0em">Healthcare</tspan></text><path d="M 201.79546212630433 20.984871250982252 A 246 246 0 0 0 177.23404020634374 28.341208024744134 L 202.8040115247091 99.91059091140855 A 170 170 0 0 1 219.77735187590136 94.82694354742677 Z" fill="rgb(255, 180, 173)" tabindex="0" role="button" aria-label="Medical QC, 1.9%" data-domain="healthcare" style="--lift-x: -4.30px; --lift-y: -14.37px;"></path><path d="M 216.99467290004594 17.788229350789067 A 246 246 0 0 0 205.55692914528436 20.100120808891575 L 222.3767396532453 94.21553064029092 A 170 170 0 0 1 230.2808715162919 92.61788207168351 Z" fill="rgb(255, 184, 178)" tabindex="0" role="button" aria-label="Medical Insurance, 1.0%" data-domain="healthcare" style="--lift-x: -2.97px; --lift-y: -14.70px;"></path><path d="M 232.3653155226624 15.557114618080988 A 246 246 0 0 0 220.80447549877073 17.14261209698904 L 232.9136619300448 92.17172380686236 A 170 170 0 0 1 240.90286032053905 91.07605481737303 Z" fill="rgb(255, 188, 182)" tabindex="0" role="button" aria-label="Immunization, 1.0%" data-domain="healthcare" style="--lift-x: -2.04px; --lift-y: -14.86px;"></path></svg>

### Economic Value Coverage

We map tasks to occupation families and SOC major groups, using a wage-bill-based GDP proxy to estimate economic coverage. The largest shares come from document preparation, software and databases, and finance and operations analysis, with a long tail of additional professional activities.

<svg id="economic-donut" viewBox="-80 -55 760 650" role="img" aria-label="Economic coverage proxy. Inner ring shows GDP proxy share and outer ring shows task count."><defs></defs><path d="M 457.8156162787609 242.3690591304281 A 158 158 0 0 0 304.4667495497032 92.06315139125948 L 302.0354808074597 178.02877784918152 A 72 72 0 0 1 371.9159770384227 246.52260922399256 Z" fill="#3f86bf" tabindex="0" role="button" aria-label="Document prep, 23.8% GDP proxy share" data-economic-key="document"></path><text x="381.7023236040743" y="166.6436042184217" text-anchor="middle" dominant-baseline="middle" transform="rotate(-45.57414829659318 381.7023236040743 166.6436042184217)">23.8%</text> <path d="M 575.0120233043386 236.70220008804557 A 275.33333333333337 275.33333333333337 0 0 0 307.7838293840819 -25.22328470637069 L 304.5232906832437 90.06395077595894 A 160 160 0 0 1 459.81328230760596 242.27246494220566 Z" fill="#3f86bf" tabindex="0" role="button" aria-label="Document prep, 15 tasks" data-economic-key="document"></path><text x="462.05134164239684" y="84.66791181682157" text-anchor="middle" dominant-baseline="middle" transform="rotate(-45.57414829659318 462.05134164239684 84.66791181682157)">15</text> <path d="M 375.5361581565576 388.77423684152444 A 158 158 0 0 0 457.84619608416676 243.03018065092172 L 371.9299121396203 246.82387979029343 A 72 72 0 0 1 334.42154042577306 313.23889273790985 Z" fill="#bfd4e8" tabindex="0" role="button" aria-label="Software &amp; databases, 17.8% GDP proxy share" data-economic-key="software"></path><text x="401.63211335564733" y="307.39749066696953" text-anchor="middle" dominant-baseline="middle" transform="rotate(29.455911823647313 401.63211335564733 307.39749066696953)">17.8%</text> <path d="M 437.57992238079055 502.7603891839299 A 287.77777777777777 287.77777777777777 0 0 0 587.4976426568156 237.30532200132717 L 459.8442491991562 242.94195508954098 A 160 160 0 0 1 376.4923120572735 390.5308727509108 Z" fill="#bfd4e8" tabindex="0" role="button" aria-label="Software &amp; databases, 17 tasks" data-economic-key="software"></path><text x="508.29900622068834" y="367.63841044663906" text-anchor="middle" dominant-baseline="middle" transform="rotate(29.455911823647313 508.29900622068834 367.63841044663906)">17</text> <path d="M 220.43297689990908 386.50307262105713 A 158 158 0 0 0 374.95420101613433 389.08942357358785 L 334.156344766846 313.3825221347995 A 72 72 0 0 1 263.74160972654084 312.20393182731715 Z" fill="#ffc28b" tabindex="0" role="button" aria-label="Finance/ops analysis, 16.3% GDP proxy share" data-economic-key="finance"></path><text x="298.04663335198927" y="366.70365357921935" text-anchor="middle" dominant-baseline="middle" transform="rotate(-89.04108216432863 298.04663335198927 366.70365357921935)">16.3%</text> <path d="M 177.01243546132216 460.99420085870855 A 244.22222222222223 244.22222222222223 0 0 0 415.85747808260425 464.9919500806934 L 375.9029883707689 390.85004918844334 A 160 160 0 0 1 219.42579939231297 388.2309596162604 Z" fill="#ffc28b" tabindex="0" role="button" aria-label="Finance/ops analysis, 10 tasks" data-economic-key="finance"></path><text x="296.44843103815913" y="462.1880570693072" text-anchor="middle" dominant-baseline="middle" transform="rotate(-89.04108216432863 296.44843103815913 462.1880570693072)">10</text> <path d="M 146.6604168451553 288.09162949912314 A 158 158 0 0 0 219.86189387748522 386.16858649151266 L 263.481369361892 312.05150776828424 A 72 72 0 0 1 230.1237342585518 267.3582109109928 Z" fill="#b8e5ad" tabindex="0" role="button" aria-label="Admin support, 12.7% GDP proxy share" data-economic-key="admin"></path><text x="206.4611697884311" y="319.81436558940635" text-anchor="middle" dominant-baseline="middle" transform="rotate(-36.736472945891734 206.4611697884311 319.81436558940635)">12.7%</text> <path d="M 75.05881120885653 305.8784382103874 A 231.77777777777777 231.77777777777777 0 0 0 182.4415686557202 449.75223025407547 L 218.8474874708711 387.89223948507606 A 160 160 0 0 1 144.71940946344841 288.57380202442846 Z" fill="#b8e5ad" tabindex="0" role="button" aria-label="Admin support, 8 tasks" data-economic-key="admin"></path><text x="136.11293143991625" y="372.3200214707697" text-anchor="middle" dominant-baseline="middle" transform="rotate(-36.736472945891734 136.11293143991625 372.3200214707697)">8</text> <path d="M 146.34251585770664 213.21171970503562 A 158 158 0 0 0 146.50220471061235 287.44898985683375 L 230.05163758964613 267.06536246640525 A 72 72 0 0 1 229.97886798579037 233.23572037191497 Z" fill="#e33f42" tabindex="0" role="button" aria-label="Sales/customer support, 7.6% GDP proxy share" data-economic-key="sales"></path><text x="183.28027003433675" y="250.25107119040825" text-anchor="middle" dominant-baseline="middle" transform="rotate(-0.12324649298591339 183.28027003433675 250.25107119040825)">7.6%</text> <path d="M 86.6948848826392 198.9310370588891 A 219.33333333333331 219.33333333333331 0 0 0 86.91656265734795 301.9861504763642 L 144.55919464365806 287.9230277031228 A 160 160 0 0 1 144.3974844128675 212.74604527092214 Z" fill="#e33f42" tabindex="0" role="button" aria-label="Sales/customer support, 6 tasks" data-economic-key="sales"></path><text x="103.21378860369845" y="250.42329902892797" text-anchor="middle" dominant-baseline="middle" transform="rotate(-0.12324649298591339 103.21378860369845 250.42329902892797)">6</text> <path d="M 165.80561695121364 166.59815614654792 A 158 158 0 0 0 146.49796182754724 212.56840536521506 L 230.0497041239456 232.94256447022457 A 72 72 0 0 1 238.84812924359102 211.9940964718446 Z" fill="#a889d0" tabindex="0" role="button" aria-label="Graphic/presentation, 5.1% GDP proxy share" data-economic-key="graphic"></path><text x="192.38637437644053" y="204.8019250393075" text-anchor="middle" dominant-baseline="middle" transform="rotate(22.782565130260537 192.38637437644053 204.8019250393075)">5.1%</text> <path d="M 50.296527744663365 94.80922726003223 A 294 294 0 0 0 14.369625172777774 180.3488049200837 L 144.5548980532124 212.0945877116102 A 160 160 0 0 1 164.10695387464673 165.54243660409918 Z" fill="#a889d0" tabindex="0" role="button" aria-label="Graphic/presentation, 18 tasks" data-economic-key="graphic"></path><text x="75.88485164003737" y="155.87090420283468" text-anchor="middle" dominant-baseline="middle" transform="rotate(22.782565130260537 75.88485164003737 155.87090420283468)">18</text> <path d="M 190.82028450533775 135.7905882840446 A 158 158 0 0 0 166.15614603933102 166.03677735487332 L 239.007864017923 211.7382782882967 A 72 72 0 0 1 250.24721825559695 197.95520478766588 Z" fill="#a98d84" tabindex="0" role="button" aria-label="Film/audio/media, 4.0% GDP proxy share" data-economic-key="media"></path><text x="209.5425450299154" y="176.23681649809902" text-anchor="middle" dominant-baseline="middle" transform="rotate(39.195390781563106 209.5425450299154 176.23681649809902)">4.0%</text> <path d="M 114.04130033187627 55.47454628970186 A 269.1111111111111 269.1111111111111 0 0 0 72.03247940032333 106.99091051582502 L 164.4619200398289 164.97395175177044 A 160 160 0 0 1 189.43826279021545 134.3448995281464 Z" fill="#a98d84" tabindex="0" role="button" aria-label="Film/audio/media, 14 tasks" data-economic-key="media"></path><text x="123.5731741290571" y="106.1334238766708" text-anchor="middle" dominant-baseline="middle" transform="rotate(39.195390781563106 123.5731741290571 106.1334238766708)">14</text> <path d="M 217.5730516922765 115.20460618895066 A 158 158 0 0 0 191.29964020167768 135.33426065421605 L 250.46565882608095 197.74725801964274 A 72 72 0 0 1 262.43835266989817 188.57425092154713 Z" fill="#c8aaa4" tabindex="0" role="button" aria-label="Health records, 3.4% GDP proxy share" data-economic-key="health"></path><text x="229.01340069130958" y="157.34763295744983" text-anchor="middle" dominant-baseline="middle" transform="rotate(52.54208416833666 229.01340069130958 157.34763295744983)">3.4%</text> <path d="M 198.56036600666937 84.11256035911649 A 194.44444444444446 194.44444444444446 0 0 0 166.22670207660752 108.88534187403519 L 189.9236862801799 133.88279559920613 A 160 160 0 0 1 216.52967259977368 113.49833538121587 Z" fill="#c8aaa4" tabindex="0" role="button" aria-label="Health records, 2 tasks" data-economic-key="health"></path><text x="189.70344281505174" y="106.03991176714416" text-anchor="middle" dominant-baseline="middle" transform="rotate(52.54208416833666 189.70344281505174 106.03991176714416)">2</text> <path d="M 245.27913175730131 101.77845440434373 A 158 158 0 0 0 218.1384027954132 114.8605205607407 L 262.6959810206946 188.41745240742614 A 72 72 0 0 1 275.0639081425677 182.45600453868826 Z" fill="#f4b2dc" tabindex="0" role="button" aria-label="Engineering/CAD, 3.1% GDP proxy share" data-economic-key="engineering"></path><text x="249.32004867919568" y="144.85675992190033" text-anchor="middle" dominant-baseline="middle" transform="rotate(64.26553106212424 249.32004867919568 144.85675992190033)">3.1%</text> <path d="M 224.03727573059973 44.240976789152285 A 219.33333333333331 219.33333333333331 0 0 0 186.3609051463753 62.40131335225186 L 217.10218004598806 113.14989423872476 A 160 160 0 0 1 244.5864625390393 99.90223230819618 Z" fill="#f4b2dc" tabindex="0" role="button" aria-label="Engineering/CAD, 6 tasks" data-economic-key="engineering"></path><text x="214.55501467400603" y="72.73142788294805" text-anchor="middle" dominant-baseline="middle" transform="rotate(64.26553106212424 214.55501467400603 72.73142788294805)">6</text> <path d="M 275.062974904188 93.98030643738963 A 158 158 0 0 0 245.90047896448147 101.55054118075239 L 275.34705370533334 182.35214534819096 A 72 72 0 0 1 288.6362923614021 178.90241812336743 Z" fill="#d2d2d2" tabindex="0" role="button" aria-label="Education/libraries, 3.1% GDP proxy share" data-economic-key="education"></path><text x="270.67289496215534" y="137.0244304723396" text-anchor="middle" dominant-baseline="middle" transform="rotate(75.44789579158316 270.67289496215534 137.0244304723396)">3.1%</text> <path d="M 268.3289259331671 51.84840606605181 A 200.66666666666666 200.66666666666666 0 0 0 231.291325604679 61.462923609310025 L 245.21567490074074 99.67143410709105 A 160 160 0 0 1 274.74731635867147 92.00537360748316 Z" fill="#d2d2d2" tabindex="0" role="button" aria-label="Education/libraries, 3 tasks" data-economic-key="education"></path><text x="253.4632378249143" y="70.72839429875137" text-anchor="middle" dominant-baseline="middle" transform="rotate(75.44789579158316 253.4632378249143 70.72839429875137)">3</text> <path d="M 287.9016459118363 92.46387770305691 A 158 158 0 0 0 275.71672552893676 93.87721953230846 L 288.9342040385028 178.8554418121912 A 72 72 0 0 1 294.48682598514057 178.21138730772213 Z" fill="#ced34d" tabindex="0" role="button" aria-label="Research writing, 1.3% GDP proxy share" data-economic-key="research"></path><text x="286.55168754389956" y="134.057336186876" text-anchor="middle" dominant-baseline="middle" transform="rotate(83.38376753507015 286.55168754389956 134.057336186876)">1.3%</text> <path d="M 283.20523841769676 31.31061503926466 A 219.33333333333331 219.33333333333331 0 0 0 266.29030674692063 33.27259589084173 L 275.4093423077841 91.90098180486933 A 160 160 0 0 1 287.7485021892013 90.46974957271584 Z" fill="#ced34d" tabindex="0" role="button" aria-label="Research writing, 6 tasks" data-economic-key="research"></path><text x="277.32652004345596" y="54.52390047773622" text-anchor="middle" dominant-baseline="middle" transform="rotate(83.38376753507015 277.32652004345596 54.52390047773622)">6</text> <path d="M 297.8371869873444 92.01480373189301 A 158 158 0 0 0 288.56163588657733 92.41458244365131 L 294.78758091033905 178.1889236452082 A 72 72 0 0 1 299.0144143233468 178.00674600440695 Z" fill="#36bbc6" tabindex="0" role="button" aria-label="Actuarial/quant analysis, 1.0% GDP proxy share" data-economic-key="actuarial"></path><text x="294.9740031154328" y="133.38826064535218" text-anchor="middle" dominant-baseline="middle" transform="rotate(87.53206412825654 294.9740031154328 133.38826064535218)">1.0%</text> <path d="M 297.42348435763813 61.79541316584161 A 188.22222222222223 188.22222222222223 0 0 0 286.3737068859789 62.27166150460292 L 288.41684646742004 90.41983032268487 A 160 160 0 0 1 297.8098096074374 90.01499112090431 Z" fill="#36bbc6" tabindex="0" role="button" aria-label="Actuarial/quant analysis, 1 tasks" data-economic-key="actuarial"></path><text x="292.3568944642845" y="72.66685573807897" text-anchor="middle" dominant-baseline="middle" transform="rotate(87.53206412825654 292.3568944642845 72.66685573807897)">1</text> <path d="M 303.80514797325037 92.04582674426842 A 158 158 0 0 0 298.49897086904355 92.0071301876315 L 299.31598672513377 178.00324919942702 A 72 72 0 0 1 301.73399148148116 178.0208830733375 Z" fill="#a9dfe8" tabindex="0" role="button" aria-label="Legal/compliance, 0.6% GDP proxy share" data-economic-key="legal"></path><text x="300.85118568408654" y="133.28310369560367" text-anchor="middle" dominant-baseline="middle" transform="rotate(-89.58216432865726 300.85118568408654 133.28310369560367)">0.6%</text> <path d="M 304.68284736511123 55.611952744352806 A 194.44444444444446 194.44444444444446 0 0 0 298.1527419274446 55.56433039968715 L 298.47997050029727 90.00722044317115 A 160 160 0 0 1 303.8533144032915 90.0464068296389 Z" fill="#a9dfe8" tabindex="0" role="button" aria-label="Legal/compliance, 2 tasks" data-economic-key="legal"></path><text x="301.32254328836916" y="68.64926686082964" text-anchor="middle" dominant-baseline="middle" transform="rotate(-89.58216432865726 301.32254328836916 68.64926686082964)">2</text></svg>

### Challenge Phenomena

OSWorld 2.0 annotates tasks with recurring, non-exclusive challenge tags that expose where long-horizon computer-use agents tend to break down.

| Phenomenon | Tasks | Share |
| --- | --- | --- |
| Cross-source ReasoningReconciling task-relevant facts across multiple independent sources, such as emails, documents, websites, records, or prior messages. | 46 | 42.6% |
| Visual-spatial PrecisionExecuting tasks that require precise visual localization, geometry, placement, timing, alignment, or pixel- or layout-level verification. | 45 | 41.7% |
| Implicit-state InferenceInferring required state that is not stated in the instruction and is not available from a single obvious source, such as prior submissions, logs, saved records, or hidden environment state. | 43 | 39.8% |
| Multi-item State TrackingMaintaining correct state across a large set of structured items, such as rows, records, events, candidates, annotations, or document edits. | 43 | 39.8% |
| Conflict DisambiguationResolving stale, noisy, contradictory, or distracting information by identifying which source is authoritative and which should be ignored or overridden. | 39 | 36.1% |
| Multimodal EditingProducing, modifying, or verifying substantive non-text media artifacts, including images, video, audio, CAD or 3D objects, or medical-image segmentations. | 30 | 27.8% |
| Tutorial FollowingExtracting procedures from external guidance, such as PDF or web guides, video walkthroughs, or prior completed work, and adapting them to the current task. | 22 | 20.4% |
| Dynamic EnvironmentRevising plans when new task-relevant information arrives during execution, such as emails or team-chat messages that change requirements. | 10 | 9.3% |
| Streaming InteractionActing in environments whose visual state changes between observation and action, making discrete screenshot-based interaction insufficient. | 6 | 5.6% |
| Proactive InteractionDetecting incomplete, ambiguous, or invalid task conditions and proactively asking the simulated user for clarification or additional evidence before proceeding. | 6 | 5.6% |

## Leaderboard

| Rank | Model | Approach & Details | Binary accuracy ↓ | Partial | Cost / task | Traj |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Claude Opus 5**  Anthropic | Max  Batch tool  v2.1 | 44.33% | 77.67% | — |  |
| 2 | **MuseSpark 1.3**  Meta | Max  Batch tool  v2.1 | 39.25% | 69.56% | — |  |
| 3 | **Claude Opus 5**  Anthropic | High  Batch tool  v2.1 | 36.89% | 68.92% | — |  |
| 4 | **Claude Opus 5**  Anthropic | Xhigh  Batch tool  v2.1 | 33.33% | 73.11% | — |  |
| 5 | **Claude Opus 5**  Anthropic | Medium  Batch tool  v2.1 | 33.01% | 64.85% | — |  |
| 6 | **Claude Opus 5**  Anthropic | Max  Batch tool  v2026.08.08 | 31.43% | 68.31% | — |  |
| 7 | **Claude Opus 5**  Anthropic | Xhigh  Batch tool  v2026.08.08 | 30.21% | 67.67% | — |  |
| 8 | **Claude Opus 5**  Anthropic | High  Batch tool  v2026.08.08 | 28.98% | 63.79% | — |  |
| 9 | **GPT-5.6 Sol**  OpenAI | Max  Batch tool  v2026.08.08 | 27.34% | 62.72% | — |  |
| 10 | **MiniMax M3.1 Flash**  MiniMax | Adaptive  Batch tool  v2026.08.08 | 26.85% | 62.01% | — |  |
| 11 | **Claude Opus 5**  Anthropic | Medium  Batch tool  v2026.08.08 | 25.33% | 60.49% | — |  |
| 12 | **Claude Opus 5**  Anthropic | Low  Batch tool  v2026.08.08 | 22.32% | 54.89% | — |  |
| 13 | **Claude Opus 4.8**  Anthropic | Max  Batched tool  v2026.06.24 | 20.6% | 54.8% | — |  |
| 14 | **Claude Opus 5**  Anthropic | Low  Batch tool  v2.1 | 18.81% | 59.09% | — |  |
| 15 | **Claude Opus 4.8**  Anthropic | Max  Standard  v2026.06.24 | 18.52% | 49.33% | — |  |
| 16 | **Claude Opus 4.7**  Anthropic | Max  Batched tool  v2026.06.24 | 18.2% | 48.91% | — |  |
| 17 | **MuseSpark 1.2**  Meta | Xhigh  Batch tool  v2.1 | 15.84% | 44.08% | — |  |
| 18 | **Claude Opus 4.7**  Anthropic | Max  Standard  v2026.06.24 | 13.9% | 49.1% | $35.8 |  |
| 19 | **GPT-5.5**  OpenAI | Xhigh  Batch tool  v2026.06.24 | 13.0% | 49.5% | $25.5 |  |
| 20 | **Claude Sonnet 4.6**  Anthropic | Medium  Standard  v2026.06.24 | 9.3% | 33.9% | $14.4 |  |
| 21 | **Claude Sonnet 4.6**  Anthropic | Max  Standard  v2026.06.24 | 8.3% | 41.5% | $22.3 |  |
| 22 | **MiniMax M3**  MiniMax | Enabled  Standard  v2026.06.24 | 4.6% | 22.3% | $2.4 |  |
| 23 | **Kimi 2.6**  Moonshot AI | Enabled  Standard  v2026.06.24 | 4.6% | 22.1% | $6.6 |  |
| 24 | **Qwen 3.7-Plus**  Alibaba | Thinking  Standard  v2026.06.24 | 2.8% | 21.5% | $3.8 |  |

Last update time: 2026-11-14

## Key Findings

Task Horizon and Performance Collapse

![Binary completion accuracy decreases as human-annotated task time increases](static/images/osworld2/task_length_binary.png?v=task-length-binary-v2)

Binary completion accuracy decreases as human-annotated task time increases

### Task Horizon Remains a Hard Limit

Agent performance exhibits a severe downward trend as task length increases.

- GPT-5.5 and Claude Opus 4.7 reach 20%-24% binary completion on tasks under 45 minutes, then decline rapidly as workflows extend.
- By the 137-163 minute bin, no model exceeds 10%; above 163 minutes, binary completion falls to zero for every model retained in the plot.
- Longer horizons compound execution load and state-management errors beyond isolated short-horizon subtasks.

2 / 3

## Failure Cases

Three representative trajectories show how agents drift from the intended workflow across long, stateful tasks.

## The Agent Sees Late Slack Approvals but Submits a Purchase-Order Sheet Missing Approved Requests.

[![Task035 step 05 screenshot showing initial finance policy rules](static/images/failure-cases/task035-step05.png)](#)

[Step 05 - Agent trace **Budget: Max $1,000 per hardware item. Vendors: IT hardware = "TechMax" only.**](#)

[![Task035 step 06 screenshot showing early request framing from direct messages](static/images/failure-cases/task035-step06.png)

Step 06 - Agent trace **I can see Alex Chen's DM with two purchase requests.**

![Task035 step 13 screenshot showing finance approval channel context](static/images/failure-cases/task035-step13.png)

Step 13 - Agent trace **I can see a notification about John in #finance-approvals.**

![Task035 step 23 screenshot showing spreadsheet reconstruction](static/images/failure-cases/task035-step23.png)

Step 23 - Agent trace **The spreadsheet currently only shows one entry. But based on the DMs, there are multiple purchase requests.**

![Task035 step 44 screenshot showing Sarah's late camera update](static/images/failure-cases/task035-step44.png)

Step 44 - Agent trace **There's a NEW message from Sarah! This is important!**

![Task035 step 48 screenshot showing the agent closing information gathering](static/images/failure-cases/task035-step48.png)

Step 48 - Agent trace **Now I have all the information I need. Let me summarize all the purchase requests and their approval statuses.**

![Task035 step 51 screenshot showing execution from stale decision table](static/images/failure-cases/task035-step51.png)

Step 51 - Agent trace **That's not relevant to our purchasing task. Now I'm in H2.**

![Task035 step 76 screenshot showing final spreadsheet review](static/images/failure-cases/task035-step76.png)

Step 76 - Agent trace **The Purchase Order Form is now complete with all 5 purchase requests.**

](#)

Task setup

Context

Purchase requests and approvals arrive through a spreadsheet, finance channel, and direct messages.

Goal

Submit a purchase order sheet with every request and the correct approval status.

Design point

The task checks whether the agent refreshes its working table when late messages change the source of truth.

Failure case · 1 / 8 · Step 05

### Initial Rules Become the Anchor State

Design pointThe agent captures the policy, but this becomes an early static frame.

Failure case · 2 / 8 · Step 06

### Requests Are Inventoried from Visible DMs

Design pointThe request list starts as visible-message memory, not durable task state.

Failure case · 3 / 8 · Step 13

### Update Channel Noticed

Design pointA dynamic channel is noticed, but not treated as a continuing source of truth.

Failure case · 4 / 8 · Step 23

### Spreadsheet State Is Rebuilt from Memory

Design pointThe agent repairs the sheet from memory rather than reconciling all sources.

Failure case · 5 / 8 · Step 44

### One Late Exception Is Integrated

Design pointThe late update is recognized, but only as a local exception.

Failure case · 6 / 8 · Step 48

### Information Gathering Closes Too Early

Design pointThe stopping claim freezes the working set before later approvals are reconciled.

Failure case · 7 / 8 · Step 51

### Old Decisions Are Executed Without Revalidation

Design pointNew messages are filtered out while the stale table is executed.

Failure case · 8 / 8 · Step 76

### Self-Check Misses the Absent Row

Design pointThe final check validates the agent's five-row story, not task completeness.

Case summary

Dynamic updates are observed, but the final spreadsheet is checked against an incomplete internal list.

## The Agent Reads the Bracket Drawing but Exports a STEP Model Whose Geometry Does Not Match It.

[![Task103 step 27 screenshot showing CAD drawing dimensions](static/images/failure-cases/task103-step27.png)](#)

[Step 27 - Agent trace **Now I can see the drawing in full screen.**](#)

[![Task103 step 31 screenshot showing drawing grounding uncertainty](static/images/failure-cases/task103-step31.png)

Step 31 - Agent trace **Let me analyze what I can see from the drawing.**

![Task103 step 33 screenshot showing feature checklist and orientation uncertainty](static/images/failure-cases/task103-step33.png)

Step 33 - Agent trace **I need to see the full drawing. Let me zoom out.**

![Task103 step 119 screenshot showing base primitive construction](static/images/failure-cases/task103-step119.png)

Step 119 - Agent trace **Let me check if the file exists and view it.**

![Task103 step 150 screenshot showing execution stall before required output](static/images/failure-cases/task103-step150.png)

Step 150 - Agent trace **The numpad keys don't seem to be working in FreeCAD.**

![Task103 step 193 screenshot showing arbitrary cylinder placement](static/images/failure-cases/task103-step193.png)

Step 193 - Agent trace **Let me now completely rewrite the macro file with all the correct dimensions at once.**

![Task103 step 194 screenshot showing simplified gusset primitives](static/images/failure-cases/task103-step194.png)

Step 194 - Agent trace **Wait - I changed bW from 130 to 105. Let me think about this.**

![Task103 step 251 screenshot showing file existence verification](static/images/failure-cases/task103-step251.png)

Step 251 - Agent trace **The STEP file exists and has reasonable file size.**

](#)

Task setup

Context

A mechanical drawing specifies the dimensions and structure of a FreeCAD support bracket.

Goal

Build and export a STEP model whose geometry matches the drawing.

Design point

The task checks whether dimensions become a stable feature-to-geometry plan, not just plausible primitives.

Failure case · 1 / 8 · Step 27

### Dimensions Are Extracted

Design pointVisual access improves, but the geometry is not yet structured.

Failure case · 2 / 8 · Step 31

### Drawing Orientation Remains Unresolved

Design pointThe trace is still interpreting the drawing, not building from a stable map.

Failure case · 3 / 8 · Step 33

### Feature Mapping Remains Unstable

Design pointThe evidence remains unresolved while planning pressure increases.

Failure case · 4 / 8 · Step 119

### A Correct-Looking Base Primitive Appears

Design pointThe workflow shifts toward artifact existence before geometry is settled.

Failure case · 5 / 8 · Step 150

### Execution Stalls Before a Submit-Ready Artifact

Design pointTool operation is consuming the trajectory while the model remains unfinished.

Failure case · 6 / 8 · Step 193

### Uncertainty Becomes an Arbitrary Coordinate

Design pointA script rewrite replaces a feature-by-feature CAD workflow.

Failure case · 7 / 8 · Step 194

### Domain Geometry Is Simplified into Ad Hoc Ribs

Design pointThe agent notices dimension drift, but the model is already unstable.

Failure case · 8 / 8 · Step 251

### File Existence Replaces Geometric Validation

Design pointFile existence becomes the check, while geometric correctness is unverified.

Case summary

The drawing is translated into approximate primitives, then accepted because an output file exists.

## The Agent Gathers Reimbursement Evidence but Reaches ExpenseFlow Too Late to Submit the Claim.

[![Task008 step 65 screenshot showing supplementary document requirements](static/images/failure-cases/task008-step65.png)](#)

[Step 65 - Agent trace **Now I can read the supplementary documents guide clearly.**](#)

[![Task008 step 120 screenshot showing VaultBank transaction search](static/images/failure-cases/task008-step120.png)

Step 120 - Agent trace **I need to scroll down to find November transactions.**

![Task008 step 220 screenshot showing API failure and screenshot automation plan](static/images/failure-cases/task008-step220.png)

Step 220 - Agent trace **The /api endpoint returns 404. Let me take a more practical approach.**

![Task008 step 300 screenshot showing expanded HKG to LAX bank transaction](static/images/failure-cases/task008-step300.png)

Step 300 - Agent trace **The HKG to LAX transaction is expanded showing transaction details.**

![Task008 step 360 screenshot showing a Python script running for document creation](static/images/failure-cases/task008-step360.png)

Step 360 - Agent trace **The Python script is running and trying to get the VaultBank scripts.**

![Task008 step 446 screenshot showing late transition toward ExpenseFlow](static/images/failure-cases/task008-step446.png)

Step 446 - Agent trace **I already read the guidelines carefully earlier and I have the key information I need.**

![Task008 step 459 screenshot showing ExpenseFlow loaded with previous report](static/images/failure-cases/task008-step459.png)

Step 459 - Agent trace **ExpenseFlow is now loaded. I need to click Create New Expense Report.**

![Task008 step 500 screenshot showing DevTools inspection of readonly date input](static/images/failure-cases/task008-step500.png)

Step 500 - Agent trace **The first input is readonly and requires the calendar picker.**

](#)

Task setup

Context

An overseas reimbursement claim requires ExpenseFlow fields plus Word attachments from bank, email, and guideline evidence.

Goal

Create and submit a complete claim with correct expense lines, dates, documents, and allocations.

Design point

The task checks whether evidence gathering turns into the target form workflow before the horizon runs out.

Failure case · 1 / 8 · Step 65

### Attachment Rules Are Captured Correctly

Design pointThe requirements are captured, but the action path is not bounded.

Failure case · 2 / 8 · Step 120

### Evidence Search Keeps Expanding

Design pointEvidence search keeps expanding instead of converging on submission.

Failure case · 3 / 8 · Step 220

### A Failed API Path Becomes a Tooling Detour

Design pointA failed shortcut turns into a document-generation detour.

Failure case · 4 / 8 · Step 300

### The Checkpoint Arrives while Evidence Is Still Being Captured

Design pointAt step 300, the agent is still collecting evidence rather than submitting.

Failure case · 5 / 8 · Step 360

### Automation Stalls inside the Evidence Workflow

Design pointTooling effort has become the task, displacing the form workflow.

Failure case · 6 / 8 · Step 446

### The Target App Finally Becomes the Focus

Design pointThe agent finally pivots to ExpenseFlow after most of the horizon is gone.

Failure case · 7 / 8 · Step 459

### The Form Workflow Starts Too Late

Design pointThe target workflow starts very late.

Failure case · 8 / 8 · Step 500

### Deadline Verification Becomes UI Reverse Engineering

Design pointThe final state is UI debugging, not a submitted reimbursement claim.

Case summary

The agent gathers requirements and evidence, but preparation consumes the horizon before submission.

## Trajectory Showcase

 [![](https://osworld-v2.xlang.ai/assets/showcase/004/gpt-5-5/step_0001.jpg) **Task 004** Slide Formatting *Version v2026.06.24*](https://osworld-v2.xlang.ai/task-showcase/#task-004)[![](https://osworld-v2.xlang.ai/assets/showcase/008/gpt-5-5/step_0001.jpg) **Task 008** Oracle Reimbursement *Version v2026.06.24* ](https://osworld-v2.xlang.ai/task-showcase/#task-008)[![](https://osworld-v2.xlang.ai/assets/showcase/024/gpt-5-5/step_0001.jpg) **Task 024** DS-2019 Visa *Version v2026.06.24* ](https://osworld-v2.xlang.ai/task-showcase/#task-024)[![](https://osworld-v2.xlang.ai/assets/showcase/035/gpt-5-5/step_0001.jpg) **Task 035** Purchase Requests *Version v2026.06.24* ](https://osworld-v2.xlang.ai/task-showcase/#task-035)[![](https://osworld-v2.xlang.ai/assets/showcase/052/gpt-5-5/step_0001.jpg) **Task 052** Travel Booking *Version v2026.06.24* ](https://osworld-v2.xlang.ai/task-showcase/#task-052)[![](https://osworld-v2.xlang.ai/assets/showcase/053/gpt-5-5/step_0001.jpg) **Task 053** Video Masking *Version v2026.06.24* ](https://osworld-v2.xlang.ai/task-showcase/#task-053)[![](https://osworld-v2.xlang.ai/assets/showcase/098/gpt-5-5/step_0001.jpg) **Task 098** DS-160 Visa Form *Version v2026.06.24* ](https://osworld-v2.xlang.ai/task-showcase/#task-098)[![](https://osworld-v2.xlang.ai/assets/showcase/103/gpt-5-5/step_0001.jpg) **Task 103** FreeCAD Bracket *Version v2026.06.24*](https://osworld-v2.xlang.ai/task-showcase/#task-103)

[Task showcase](task-showcase/) [Explore all task trajectories](task-trajectories/)

## Acknowledgments

We thank Cheng Chang, [Dawn Song](https://dawnsong.io/), [Delin Chen](https://chendl02.github.io/), [Junli Wang](https://junliwang.tech/), Ke Xu, [Qiyue Xu](https://github.com/ArcaLunar), [Ruiling Xu](https://github.com/carol-xrl), [Shengwei Wang](https://github.com/Wangshengwei666), [Yanzhuo Lin](https://github.com/Karis004), [Yimo Cai](https://github.com/JamesCai23), [Yiyong Sun](https://sunyiyou.github.io/), and Yutong Yao for their helpful feedback and for contributing materials to this benchmark. We thank [Snorkel AI](https://snorkel.ai/), our research & data partner, for their support of this work. We gratefully acknowledge support from the [Google Research](https://research.google/) gift fund.

## Citation

```
@misc{yuan2026osworld20benchmarkingcomputeruse,
      title={OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks},
      author={Mengqi Yuan and Zilong Zhou and Xinzhuang Xiong and Weiming Wu and Jiayang Sun and Jiamin Song and Kaiqian Cui and Bowen Wang and Haoyuan Wu and Yitong Li and Dunjie Lu and Haikong Lu and Qi Zhen and Xinyuan Wang and Jiaqi Deng and Yuhao Yang and Cheng Chen and Boyuan Zheng and Alex Su and Xiao Yu and Hao Zou and Saaket Agashe and Xing Han Lu and Manpreet Kaur and Zhengyang Qi and Vincent Sunn Chen and Frederic Sala and Dayiheng Liu and Junyang Lin and Zhou Yu and Yu Su and Siva Reddy and Xin Eric Wang and Peng Qi and Tianbao Xie and Tao Yu},
      year={2026},
      eprint={2606.29537},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2606.29537},
}
```

[^1]: Offline set: 82 tasks runnable without internet; see the [GitHub task list](https://github.com/xlang-ai/OSWorld-V2/blob/main/evaluation_examples/test_v2_offline_no_internet.json).

[^2]: v2026.08.08 results average 7 runs for Claude Opus 5 and 2 runs for GPT-5.6 Sol.

[^3]: MiniMax M3.1 Flash is self-reported and averages two 108-task runs; binary success requires a score ≥ 1 − 10 <sup>−6</sup>. The second run includes infrastructure-failure reruns of tasks 048 and 079.

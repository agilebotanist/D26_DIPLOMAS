# Project metrics: Opaline

Size and dependencies of the selected components. Review candidates in the source code.

Commit: `26622322ddac`.

## Summary

| Metric | Value |
|---|---:|
| Swift files | 399 |
| Components | 17 |
| Component edges | 104 |
| Lines of code (SLOC) | 46892 |
| Median component size | 1220 |
| Size Gini | 0.564865 |
| Dependency Gini | 0.294683 |
| Propagation cost (PC) | 0.944637 |
| Cyclic groups (SCC) | 1 |
| Components in cycles | 16 |
| Hub candidates | 9 |
| Unstable dependencies | 27 |
| Sources of unstable dependencies | 9 |

## Components

| Component | SLOC | Size/median | In | Out | I | DoUD |
|---|---:|---:|---:|---:|---:|---:|
| App | 948 | 0.7770 | 10 | 15 | 0.6000 | 0.4667 |
| Core.API | 9184 | 7.5279 | 15 | 7 | 0.3182 | 0.5714 |
| Core.Auth | 927 | 0.7598 | 12 | 5 | 0.2941 | 0.6000 |
| Core.Common | 8716 | 7.1443 | 14 | 10 | 0.4167 | 0.4000 |
| Core.Config | 322 | 0.2639 | 11 | 3 | 0.2143 | 1.0000 |
| Core.Localization | 243 | 0.1992 | 6 | 1 | 0.1429 | 1.0000 |
| Core.Playback | 4967 | 4.0713 | 7 | 7 | 0.5000 | 0.1429 |
| Core.Services | 4656 | 3.8164 | 12 | 8 | 0.4000 | 0.3750 |
| Core.Transport | 360 | 0.2951 | 6 | 3 | 0.3333 | 0.3333 |
| Features.Channel | 1654 | 1.3557 | 1 | 7 | 0.8750 | 0.0000 |
| Features.Home | 865 | 0.7090 | 1 | 5 | 0.8333 | 0.0000 |
| Features.Library | 1220 | 1.0000 | 2 | 5 | 0.7143 | 0.0000 |
| Features.Player | 8667 | 7.1041 | 3 | 7 | 0.7000 | 0.0000 |
| Features.Profile | 184 | 0.1508 | 0 | 6 | 1.0000 | 0.0000 |
| Features.Search | 725 | 0.5943 | 2 | 4 | 0.6667 | 0.0000 |
| Features.Shorts | 1334 | 1.0934 | 1 | 6 | 0.8571 | 0.0000 |
| Features.Subscriptions | 1920 | 1.5738 | 1 | 5 | 0.8333 | 0.0000 |

## Findings to review

- Cyclic group (16 components): App, Core.API, Core.Auth, Core.Common, Core.Config, Core.Localization, Core.Playback, Core.Services, Core.Transport, Features.Channel, Features.Home, Features.Library, Features.Player, Features.Search, Features.Shorts, Features.Subscriptions.
- Hub candidates: App, Core.API, Core.Auth, Core.Common, Core.Config, Core.Playback, Core.Services, Core.Transport, Features.Player.

## Reading the results

- Hub: incoming ≥ 3, outgoing ≥ 3.
- Unstable dependency: target I − source I > 0.
- PC is the fraction of reachable component pairs, including self-pairs; it is not a failure probability.
- I = outgoing / all edges. DoUD counts dependencies on less stable components before the ΔI filter.
- “—” means undefined. SCC counts mutually reachable groups, not individual cycles.

Syntax-based analysis may miss dependencies. Full edges, source evidence, diagnostics and sensitivity results are in [report.json](report.json).

# Media sources

Every file in this folder was made for this deck. Nothing is taken from a third party.

| File | Kind | Source of truth | Data behind it |
|---|---|---|---|
| `two-curves.svg` | Conceptual chart | `two-curves.vl.json` | Schematic curves, not measured data. Reasoning in `../../insights/I1-where-we-are-two-curves.md` |
| `miro-valuation.svg` | Chart | `miro-valuation.vl.json` | 17.5 billion USD valuation at the 2022 round; 1.355 billion USD enterprise value at the sale closed 2026-10-26. See `../../insights/I7-industry-structure-five-forces.md`, I7.7. The two bars are different measures |
| `delegation-ladder.svg` | Chart | `delegation-ladder.vl.json` | JetBrains Developer Ecosystem Survey 2026 raw data, weighted, computed in `../../analysis/jetbrains2026/` |
| `five-forces.svg` | Diagram, hand-authored | `five-forces.drawio` | The speaker's own application of Porter's five forces. See I7 |
| `two-checkers.svg` | Diagram, hand-authored | `two-checkers.drawio` | The curl bug bounty story. See `../../insights/I4-quality-verification-and-mathematics.md`, I4.5 |

## Hand-owned diagrams

`five-forces.drawio` and `two-checkers.drawio` are written directly as draw.io XML. Re-export with `build-diagram.py media/<name>.drawio`. There is no Mermaid source.

## Charts

Rendered with `npx -y -p vega -p vega-lite -p vega-cli vl2svg <name>.vl.json <name>.svg`.
| `bls-2035.svg` | Chart | `bls-2035.vl.json` | US Bureau of Labor Statistics, Occupational Outlook Handbook, projections 2025–2035, read 2026-11-18; local copies `../../converted/web/bls2035_*.md` |
| `eng-roles.svg` | Chart | `eng-roles.vl.json` | SignalFire, State of Talent 2026, change in share of engineering roles since 2022 |

# Paper inventory — Darya Tolmeneva

Read out of `_raw/review.md`, her literature review of 2026-08-31, then verified against
arXiv and CrossRef.

Updated: 2026-09-21

## Verified

| # | Key | Title | Section | PDF | Converted | Summary | BibTeX | Relevance |
|---|-----|-------|---------|-----|-----------|---------|--------|-----------|
| 1 | `he2025lmasurvey` | LLM-Based Multi-Agent Systems for SE: Literature Review, Vision, and the Road Ahead | 2.x | no | no | in review.md | yes | HIGH — 228 citations, TOSEM. The anchor for any multi-agent framing |
| 2 | `tufano2025codereview` | Automating Code Review: A Systematic Literature Review | 2.x | no | no | in review.md | yes | HIGH — SLR over 119 papers, the map of what is already automated in review |
| 3 | `cai2025masdesign` | Designing LLM-based MAS for SE Tasks: Quality Attributes, Design Patterns and Rationale | 2.x | no | no | in review.md | yes | MED — 94 papers, gives design-pattern statistics rather than an evaluation method |
| 4 | `koech2026phoenix` | Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs | 2.x | no | no | in review.md | yes | HIGH — a built system with a baseline-aware test protocol, the closest thing to an experimental design she can borrow |
| 5 | `guo2023falsepositives` | Mitigating False Positive Static Analysis Warnings | 2.x | no | no | no | yes | HIGH — 40 citations, directly serves the "LLM improves static analysis output" direction |
| 6 | `chomatek2025cicd` | Decoding CI/CD Practices in Open-Source Projects with LLM Insights | 2.x | no | no | no | yes | MED — background on what is and is not automated in practice |
| 7 | `kuliamin2024dynamic` | A Survey of Software Dynamic Analysis Methods | 2.x | no | no | no | yes | MED — background, the dynamic-analysis half of the picture |

## Two author attributions were wrong

Verification caught real errors in her list. The titles and DOIs were right, the authors
were not:

| Her reference | Actual authors | Source |
|---|---|---|
| [2] "Muske, T., Serebrenik, A." | Guo, Tan, Liu, Liu, Lai, Yang, Li, Chen, Dong, Zhou | CrossRef, IEEE TSE 49(12) |
| [5] "Decan, A., et al." | Chomątek, Papuga, Nowak, Poniszewska-Marańda | CrossRef, FSE 2025 |

Worth raising with her, not as a scolding but because it tells her something about how the
list was assembled. Muske and Serebrenik do have their own surveys on static analysis
alarms, so that citation may have been intended and simply belongs as a separate entry.

## Still to verify

| # | Reference as she wrote it | Why it is not in the bib yet |
|---|---|---|
| R1 | Adewumi et al., A systematic literature review of open source software quality assessment models, SpringerPlus 2016 | Not yet checked. Also note: her text cites this as the source for the ISO/IEC 25010 eight-characteristic framework, which is not what this paper is |
| R2 | Soares, Sizilio, Santos, Alencar, Kulesza, The Effects of Continuous Integration on Software Development: an SLR, arXiv:2103.05451 | Not yet checked |
| R3 | ISO/IEC 25010 itself | Used as the framing in Part 0 but never cited directly. Needs its own entry |

## Foundational references, BibTeX only

| # | Key | Title | Section | Notes |
|---|-----|-------|---------|-------|

Scraping: https://www.remotelabor.ai/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.remotelabor.ai/
  Settled (dom-quiet, 1475ms)
  Extracting content...
  Extracted 22697 characters

--- Content ---

[![Center for AI Safety](/assets/cais_logo.svg)](https://safe.ai/) [![Scale AI Logo](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fscale-logo.0d7c0e0f.png&w=256&q=75)](https://scale.com/)

[Mantas Mazeika](https://scholar.google.com/citations?user=fGeEmLQAAAAJ&hl=en) <sup>∗1</sup>, [Alice Gatti](https://scholar.google.com/citations?user=Wm-EioQAAAAJ&hl=en) <sup>∗1</sup>, [Cristina Menghini](https://crimenghini.github.io/) <sup>∗†</sup>, [Udari Madhushani Sehwag](https://udarimadhu.github.io/) <sup>∗2</sup>, [Shivam Singhal](https://scholar.google.com/citations?user=FtEAB2wAAAAJ&hl=en) <sup>∗†</sup>, [Yury Orlovskiy](https://yvorlovskiy.github.io/) <sup>∗1</sup>

[Steven Basart](https://scholar.google.com/citations?user=MzKvJhAAAAAJ&hl=en) <sup>1</sup>, [Manasi Sharma](https://manasi-sharma.github.io/) <sup>2</sup>, [Denis Peskoff](http://denis.ai/) <sup>2</sup>, [Elaine Lau](https://scholar.google.com/citations?user=jC63xPkAAAAJ&hl=en) <sup>2</sup>, [Jaehyuk Lim](https://scholar.google.com/citations?user=p4hquUoAAAAJ&hl=en) <sup>1</sup>, [Lachlan Carroll](https://www.lachlan.wiki/) <sup>1</sup>, [Alice Blair](https://aliceblair.net/) <sup>1</sup>, Vinaya Sivakumar <sup>1</sup>, [Sumana Basu](https://scholar.google.com/citations?user=xu4ysukAAAAJ&hl=en) <sup>2</sup>, [Brad Kenstler](https://www.bradkenstler.com/) <sup>2</sup>, Yuntao Ma <sup>†</sup>, [Julian Michael](https://julianmichael.org/) <sup>†</sup>, [Xiaoke Li](https://scholar.google.com/citations?hl=en&user=6nu3MvYAAAAJ) <sup>1</sup>, Oliver Ingebretsen <sup>1</sup>, Aditya Mehta <sup>1</sup>, Jean Mottola <sup>1</sup>, John Teichmann <sup>‡</sup>, Kevin Yu <sup>‡</sup>, [Zaina Shaik](https://www.zainashaik.com/) <sup>‡</sup>, Adam Khoja <sup>1</sup>, Richard Ren <sup>1</sup>, [Jason Hausenloy](https://jasonhausenloy.com/) <sup>1</sup>, [Long Phan](https://longphan.ai/) <sup>1</sup>, [Ye Htet](https://scholar.google.com/citations?user=3OjLAMcAAAAJ&hl=en) <sup>2</sup>, [Ankit Aich](https://ankitaich.com/) <sup>2</sup>, [Tahseen Rabbani](https://twr7bm.github.io/) <sup>2</sup>, [Vivswan Shah](https://scholar.google.com/citations?user=bSd2P_cAAAAJ&hl=en) <sup>†</sup>, Andriy Novykov <sup>1</sup>, [Felix Binder](https://ac.felixbinder.net/) <sup>†</sup>

Kirill Chugunov <sup>2</sup>, Luis Ramirez <sup>2</sup>, Matias Geralnik <sup>2</sup>, Hernan Mesura <sup>2</sup>, Dean Lee <sup>†</sup>, [Ed-Yeremai Hernandez Cardona](https://scholar.google.com/citations?user=TdUzpp0AAAAJ&hl=es) <sup>2</sup>, Annette Diamond <sup>†</sup>

Summer Yue <sup>∗∗†</sup>, [Alexandr Wang](https://scholar.google.com/citations?user=fnmoYqQAAAAJ&hl=en) <sup>∗∗†</sup>, Bing Liu <sup>∗∗2</sup>, Ernesto Hernandez <sup>∗∗2</sup>, [Dan Hendrycks](https://people.eecs.berkeley.edu/~hendrycks/) <sup>∗∗1</sup>

<sup>1</sup> Center for AI Safety

<sup>2</sup> Scale AI

∗ Equal contribution ∗∗ Senior authors † Work done while at Scale AI ‡ Work done while at CAIS

## Introduction

The potential for AIs to automate human labor is a topic of significant interest and concern. While AIs have made rapid progress on research-oriented benchmarks of knowledge and reasoning, it remains unclear how these gains translate into real economic value and actual automation.

To address this gap, we introduce the Remote Labor Index (RLI), a broadly multi-sector benchmark comprising real-world, economically valuable remote-work projects designed to evaluate end-to-end agent performance in practical settings.

These results help ground discussions of AI automation in empirical evidence, setting a common basis for tracking progress and enabling stakeholders to proactively navigate AI-driven labor automation.

## How close is AI to automating remote work?

![](/assets/logo-oct-27.png) Remote Labor Index (RLI)

41.25%

full automation of remote projects

×2 every ~3.3 months

over the last

<svg width="1136" height="400" viewBox="0 0 1136 400" style="width: 100%; height: 100%;"><defs><clipPath id="recharts1-clip"><rect x="50" y="20" height="332" width="953"></rect></clipPath></defs><g><line orientation="bottom" width="953" height="44" x="50" y="352" stroke="currentColor" fill="none" x1="50" y1="352" x2="1003" y2="352"></line><g><g><g><text x="64.66153846153847" y="372" text-anchor="middle" font-size="12.5" fill="#888">Jun</text> <text x="64.66153846153847" y="390" text-anchor="middle" font-size="12.5" font-weight="600" fill="#888">2025</text></g></g> <g><g><text x="362.7794871794872" y="372" text-anchor="middle" font-size="12.5" fill="#888">Dec</text> <text x="362.7794871794872" y="390" text-anchor="middle" font-size="12.5" font-weight="600" fill="#888">2025</text></g></g> <g><g><text x="659.268376068376" y="372" text-anchor="middle" font-size="12.5" fill="#888">Jun</text> <text x="659.268376068376" y="390" text-anchor="middle" font-size="12.5" font-weight="600" fill="#888">2026</text></g></g> <g><g><text x="957.3863247863247" y="372" text-anchor="middle" font-size="12.5" fill="#888">Dec</text> <text x="957.3863247863247" y="390" text-anchor="middle" font-size="12.5" font-weight="600" fill="#888">2026</text></g></g></g></g> <g><line orientation="left" width="46" height="332" x="4" y="20" stroke="currentColor" fill="none" x1="50" y1="20" x2="50" y2="352"></line><g><g><text orientation="left" width="46" height="332" stroke="none" font-size="12.5" x="42" y="352" text-anchor="end" fill="#888"><tspan x="42" dy="0.355em">0%</tspan></text></g> <g><text orientation="left" width="46" height="332" stroke="none" font-size="12.5" x="42" y="285.6" text-anchor="end" fill="#888"><tspan x="42" dy="0.355em">10%</tspan></text></g> <g><text orientation="left" width="46" height="332" stroke="none" font-size="12.5" x="42" y="219.2" text-anchor="end" fill="#888"><tspan x="42" dy="0.355em">20%</tspan></text></g> <g><text orientation="left" width="46" height="332" stroke="none" font-size="12.5" x="42" y="152.8" text-anchor="end" fill="#888"><tspan x="42" dy="0.355em">30%</tspan></text></g> <g><text orientation="left" width="46" height="332" stroke="none" font-size="12.5" x="42" y="86.39999999999998" text-anchor="end" fill="#888"><tspan x="42" dy="0.355em">40%</tspan></text></g> <g><text orientation="left" width="46" height="332" stroke="none" font-size="12.5" x="42" y="20" text-anchor="end" fill="#888"><tspan x="42" dy="0.355em">50%</tspan></text></g></g></g> <g><path stroke="#525252" stroke-width="1.75" stroke-dasharray="6 5" width="953" height="332" fill="none" d="M90.726,346.489L126.566,338.189L351.376,327.1L470.297,324.311L595.735,310.5L656.01,296.689L672.301,246.889L809.142,233.011L812.4,213.689L843.352,210.9L921.547,78.1"></path><g></g></g><g><path stroke="transparent" width="953" height="332" stroke-width="1" fill="none" d="M351.376,327.1L595.735,310.5L672.301,246.889L812.4,213.689L921.547,78.1"></path><g></g><g><g><line x1="351.37606837606836" y1="313.165686544842" x2="351.37606837606836" y2="269.1" stroke="#a3a3a3" stroke-width="0.75"></line></g><g><line x1="595.7350427350427" y1="296.565686544842" x2="595.7350427350427" y2="228.5" stroke="#a3a3a3" stroke-width="0.75"></line></g><g><line x1="685.3941310410095" y1="253.50161873048762" x2="694.3008547008548" y2="258" stroke="#a3a3a3" stroke-width="0.75"></line></g><g><line x1="812.4000000000001" y1="199.754486544842" x2="812.4000000000001" y2="164" stroke="#a3a3a3" stroke-width="0.75"></line></g><g><line x1="935.4813220021665" y1="78.10000000000002" x2="943.5470085470085" y2="78.10000000000002" stroke="#a3a3a3" stroke-width="0.75"></line></g></g></g><g><g><g role="img"><g><title>Gemini 2.5 Pro: 0.8% (Jun 17, 2025)</title> <g data-rli-hover="true" style="cursor: pointer;"><polygon points="103.66080918165375,351.8463680531113 96.08406377960699,359.42311345515805 85.36892767338448,359.42311345515805 77.79218227133771,351.8463680531113 77.79218227133771,341.13123194688876 85.36892767338448,333.554486544842 96.08406377960699,333.554486544842 103.66080918165375,341.13123194688876" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="0.35"><polygon points="103.66080918165375,351.8463680531113 96.08406377960699,359.42311345515805 85.36892767338448,359.42311345515805 77.79218227133771,351.8463680531113 77.79218227133771,341.13123194688876 85.36892767338448,333.554486544842 96.08406377960699,333.554486544842 103.66080918165375,341.13123194688876" fill="none" stroke="#F64746" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g><g role="img"><g><title>Grok 4: 2.1% (Jul 9, 2025)</title> <g data-rli-hover="true" style="cursor: pointer;"><polygon points="139.50012542097,343.5463680531113 131.92338001892324,351.12311345515803 121.20824391270072,351.12311345515803 113.63149851065396,343.5463680531113 113.63149851065396,332.83123194688875 121.20824391270072,325.254486544842 131.92338001892324,325.254486544842 139.50012542097,332.83123194688875" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="0.35"><polygon points="139.50012542097,343.5463680531113 131.92338001892324,351.12311345515803 121.20824391270072,351.12311345515803 113.63149851065396,343.5463680531113 113.63149851065396,332.83123194688875 121.20824391270072,325.254486544842 131.92338001892324,325.254486544842 139.50012542097,332.83123194688875" fill="none" stroke="#737373" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g><g role="img"><g><title>Opus 4.5: 3.8% (Nov 24, 2025)</title> <polygon points="364.3103818312264,332.4575680531113 356.7336364291796,340.03431345515804 346.0185003229571,340.03431345515804 338.44175492091034,332.4575680531113 338.44175492091034,321.74243194688876 346.0185003229571,314.165686544842 356.7336364291796,314.165686544842 364.3103818312264,321.74243194688876" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="1"><polygon points="364.3103818312264,332.4575680531113 356.7336364291796,340.03431345515804 346.0185003229571,340.03431345515804 338.44175492091034,332.4575680531113 338.44175492091034,321.74243194688876 346.0185003229571,314.165686544842 356.7336364291796,314.165686544842 364.3103818312264,321.74243194688876" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g><g role="img"><g><title>Opus 4.6: 4.2% (Feb 5, 2026)</title> <g data-rli-hover="true" style="cursor: pointer;"><polygon points="483.2317493525939,329.66876805311125 475.65500395054715,337.245513455158 464.9398678443246,337.245513455158 457.36312244227787,329.66876805311125 457.36312244227787,318.9536319468887 464.9398678443246,311.37688654484197 475.65500395054715,311.37688654484197 483.2317493525939,318.9536319468887" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="0.35"><polygon points="483.2317493525939,329.66876805311125 475.65500395054715,337.245513455158 464.9398678443246,337.245513455158 457.36312244227787,329.66876805311125 457.36312244227787,318.9536319468887 464.9398678443246,311.37688654484197 475.65500395054715,311.37688654484197 483.2317493525939,318.9536319468887" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g><g role="img"><g><title>GPT-5.5: 6.3% (Apr 23, 2026)</title> <polygon points="608.6693561902007,315.85756805311127 601.0926107881539,323.434313455158 590.3774746819315,323.434313455158 582.8007292798848,315.85756805311127 582.8007292798848,305.14243194688873 590.3774746819315,297.565686544842 601.0926107881539,297.565686544842 608.6693561902007,305.14243194688873" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="1"><polygon points="608.6693561902007,315.85756805311127 601.0926107881539,323.434313455158 590.3774746819315,323.434313455158 582.8007292798848,315.85756805311127 582.8007292798848,305.14243194688873 590.3774746819315,297.565686544842 601.0926107881539,297.565686544842 608.6693561902007,305.14243194688873" fill="none" stroke="#22c55e" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g><g role="img"><g><title>Opus 4.8: 8.3% (May 30, 2026)</title> <g data-rli-hover="true" style="cursor: pointer;"><polygon points="668.9445698654143,302.0463680531113 661.3678244633676,309.62311345515803 650.6526883571452,309.62311345515803 643.0759429550984,302.0463680531113 643.0759429550984,291.33123194688875 650.6526883571452,283.754486544842 661.3678244633676,283.754486544842 668.9445698654143,291.33123194688875" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="0.35"><polygon points="668.9445698654143,302.0463680531113 661.3678244633676,309.62311345515803 650.6526883571452,309.62311345515803 643.0759429550984,302.0463680531113 643.0759429550984,291.33123194688875 650.6526883571452,283.754486544842 661.3678244633676,283.754486544842 668.9445698654143,291.33123194688875" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g><g role="img"><g><title>Fable 5: 15.8% (Jun 9, 2026)</title> <polygon points="685.2351681560127,252.24636805311127 677.658422753966,259.823113455158 666.9432866477435,259.823113455158 659.3665412456968,252.24636805311127 659.3665412456968,241.53123194688877 666.9432866477435,233.95448654484198 677.658422753966,233.95448654484198 685.2351681560127,241.53123194688874" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="1"><polygon points="685.2351681560127,252.24636805311127 677.658422753966,259.823113455158 666.9432866477435,259.823113455158 659.3665412456968,252.24636805311127 659.3665412456968,241.53123194688877 666.9432866477435,233.95448654484198 677.658422753966,233.95448654484198 685.2351681560127,241.53123194688874" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g><g role="img"><g><title>Fable 5.1: 17.9% (Sep 1, 2026)</title> <g data-rli-hover="true" style="cursor: pointer;"><polygon points="822.0761937970383,238.36876805311124 814.4994483949915,245.945513455158 803.7843122887691,245.945513455158 796.2075668867224,238.36876805311124 796.2075668867224,227.65363194688874 803.7843122887691,220.07688654484195 814.4994483949915,220.07688654484195 822.0761937970383,227.6536319468887" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="0.35"><polygon points="822.0761937970383,238.36876805311124 814.4994483949915,245.945513455158 803.7843122887691,245.945513455158 796.2075668867224,238.36876805311124 796.2075668867224,227.65363194688874 803.7843122887691,220.07688654484195 814.4994483949915,220.07688654484195 822.0761937970383,227.6536319468887" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g><g role="img"><g><title>GPT-6 Astra: 20.8% (Sep 3, 2026)</title> <polygon points="825.334313455158,219.04636805311128 817.7575680531113,226.62311345515803 807.0424319468889,226.62311345515803 799.4656865448421,219.04636805311128 799.4656865448421,208.33123194688878 807.0424319468889,200.754486544842 817.7575680531113,200.754486544842 825.334313455158,208.33123194688875" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="1"><polygon points="825.334313455158,219.04636805311128 817.7575680531113,226.62311345515803 807.0424319468889,226.62311345515803 799.4656865448421,219.04636805311128 799.4656865448421,208.33123194688878 807.0424319468889,200.754486544842 817.7575680531113,200.754486544842 825.334313455158,208.33123194688875" fill="none" stroke="#22c55e" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g><g role="img"><g><title>Opus 5.5: 21.3% (Sep 22, 2026)</title> <g data-rli-hover="true" style="cursor: pointer;"><polygon points="856.2864502072947,216.25756805311124 848.709704805248,223.834313455158 837.9945686990255,223.834313455158 830.4178232969788,216.25756805311124 830.4178232969788,205.54243194688874 837.9945686990255,197.96568654484196 848.709704805248,197.96568654484196 856.2864502072947,205.5424319468887" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="0.35"><polygon points="856.2864502072947,216.25756805311124 848.709704805248,223.834313455158 837.9945686990255,223.834313455158 830.4178232969788,216.25756805311124 830.4178232969788,205.54243194688874 837.9945686990255,197.96568654484196 848.709704805248,197.96568654484196 856.2864502072947,205.5424319468887" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g><g role="img"><g><title>Fable 5.2: 41.3% (Nov 9, 2026)</title><polygon points="934.4813220021665,83.45756805311127 926.9045766001198,91.03431345515804 916.1894404938973,91.03431345515804 908.6126950918506,83.45756805311129 908.6126950918506,72.74243194688877 916.1894404938973,65.165686544842 926.9045766001198,65.165686544842 934.4813220021665,72.74243194688877" fill="#ffffff" stroke="#ffffff" stroke-width="2" stroke-linejoin="round"></polygon><g opacity="1"><polygon points="934.4813220021665,83.45756805311127 926.9045766001198,91.03431345515804 916.1894404938973,91.03431345515804 908.6126950918506,83.45756805311129 908.6126950918506,72.74243194688877 916.1894404938973,65.165686544842 926.9045766001198,65.165686544842 934.4813220021665,72.74243194688877" fill="none" stroke="#f97316" stroke-width="2" stroke-linejoin="round"></polygon></g></g></g></g></g><g><path stroke="transparent" width="953" height="332" stroke-width="1" fill="none" d="M351.376,327.1L595.735,310.5L672.301,246.889L812.4,213.689L921.547,78.1"></path><g></g><g><g><foreignObject x="257.37606837606836" y="175.10000000000002" width="188" height="94"><div><div><img alt="" src="/provider-logos/claude_logo.svg"> <span style="font-size:13px;font-weight:600">Opus 4.5</span> <span style="font-size:11px">Nov 24, 2025</span></div><div style="font-size:12px">Anthropic</div><div style="font-size:13px;font-weight:600">3.8% <span style="font-weight:500">automation rate</span></div></div></foreignObject></g><g><foreignObject x="501.7350427350427" y="134.5" width="188" height="94"><div><div><img alt="" src="/provider-logos/openai-logomark.png"> <span style="font-size:13px;font-weight:600">GPT-5.5</span> <span style="font-size:11px">Apr 23, 2026</span></div><div style="font-size:12px">OpenAI</div><div style="font-size:13px;font-weight:600">6.3% <span style="font-weight:500">automation rate</span></div></div></foreignObject></g><g><foreignObject x="694.3008547008548" y="258" width="188" height="94"><div><div><img alt="" src="/provider-logos/claude_logo.svg"> <span style="font-size:13px;font-weight:600">Fable 5</span> <span style="font-size:11px">Jun 9, 2026</span></div><div style="font-size:12px">Anthropic</div><div style="font-size:13px;font-weight:600">15.8% <span style="font-weight:500">automation rate</span></div></div></foreignObject></g><g><foreignObject x="698" y="70" width="188" height="94"><div><div><img alt="" src="/provider-logos/openai-logomark.png"> <span style="font-size:13px;font-weight:600">GPT-6 Astra</span> <span style="font-size:11px">Sep 3, 2026</span></div><div style="font-size:12px">OpenAI</div><div style="font-size:13px;font-weight:600">20.8% <span style="font-weight:500">automation rate</span></div></div></foreignObject></g><g><foreignObject x="943.5470085470085" y="31.100000000000023" width="188" height="94"><div><div><img alt="" src="/provider-logos/claude_logo.svg"> <span style="font-size:13px;font-weight:600">Fable 5.2</span> <span style="font-size:11px">Nov 9, 2026</span></div><div style="font-size:12px">Anthropic</div><div style="font-size:13px;font-weight:600">41.3% <span style="font-weight:500">automation rate</span></div></div></foreignObject></g></g></g></svg>

## Example Projects from RLI

![Remote Labor Index overview diagram](/_next/image?url=%2Fassets%2Fnew-fig1.png&w=3840&q=75)

Remote Labor Index overview diagram

## Remote Labor Index Overview

RLI represents a broad range of projects from across the remote labor economy, including game development, product design, architecture, data analysis, and video animation. These projects span a broad range of difficulty, with costs reaching over $10,000 and completion times exceeding 100 hours. All project costs and completion times come directly from human professionals who completed the work. In total, the projects in RLI represent over 6,000 hours of real work valued at over $140,000.

![Distribution of RLI project costs and completion times](/_next/image?url=%2Fassets%2Fcosts_and_times_combined.png&w=3840&q=75)

RLI is close to the complexity and costs of real freelance labor. All project costs and completion times come directly from human professionals who completed the projects.

## Evaluation Results

The best-performing model achieves an automation rate of 41.25%.

Our analysis shows that models are steadily improving and that progress on these complex tasks is measurable. This provides a common basis for tracking the trajectory of AI automation, enabling stakeholders to proactively navigate its impacts.

ModelAutomation Rate (%)

Fable 5.2

41.25

Opus 5.5

21.25

GPT-6 Astra

20.83

Fable 5.1

17.92

Fable 5

15.83

Opus 4.8

8.33

GPT-5.5

6.25

Gemini 3.8 Flash

5.83

Gemini 3.7 Flash

5.00

Opus 4.6

4.17

GPT-5.2

2.50

Selected models from the CAIS AI Dashboard. For the latest results, visit [dashboard.safe.ai](https://dashboard.safe.ai/#automation) or the [Scale leaderboard](https://labs.scale.com/leaderboard/rli).

## Citation

```
@misc{mazeika2025remote,
      title = {Remote Labor Index: Measuring AI Automation of Remote Work},
      author = {Mantas Mazeika and Alice Gatti and Cristina Menghini and Udari Madhushani Sehwag and Shivam Singhal and Yury Orlovskiy and Steven Basart and Manasi Sharma and Denis Peskoff and Elaine Lau and Jaehyuk Lim and Lachlan Carroll and Alice Blair and Vinaya Sivakumar and Sumana Basu and Brad Kenstler and Yuntao Ma and Julian Michael and Xiaoke Li and Oliver Ingebretsen and Aditya Mehta and Jean Mottola and John Teichmann and Kevin Yu and Zaina Shaik and Adam Khoja and Richard Ren and Jason Hausenloy and Long Phan and Ye Htet and Ankit Aich and Tahseen Rabbani and Vivswan Shah and Andriy Novykov and Felix Binder and Kirill Chugunov and Luis Ramirez and Matias Geralnik and Hernán Mesura and Dean Lee and Ed-Yeremai Hernandez Cardona and Annette Diamond and Summer Yue and Alexandr Wang and Bing Liu and Ernesto Hernandez and Dan Hendrycks},
      year            = {2025},
      eprint          = {2510.26787},
      archivePrefix   = {arXiv},
      primaryClass    = {cs.LG},
      url             = {https://arxiv.org/abs/2510.26787}
}
```

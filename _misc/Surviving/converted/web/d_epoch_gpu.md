Scraping: https://epoch.ai/data/gpu-clusters
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://epoch.ai/data/gpu-clusters
  Consent dismissed via: text-match:accept
  Settled (dom-quiet, 2582ms)
  Extracting content...
  Extracted 1575 characters

--- Content ---

This dataset is deprecated. For data on site-level infrastructure, users, and satellite analysis, explore the [AI data centers database](/data/ai-data-centers).

## GPU clusters

Our database of over 500 GPU clusters and supercomputers tracks large hardware facilities, including those used for AI training and inference.

This dataset was previously called 'AI Supercomputers' but was renamed to account for its broad coverage of GPU clusters.

[Download this data](/data/gpu_clusters.csv)

### More about this dataset

### Documentation

This dataset tracks GPU clusters, identified from sources including model training reports, news articles, press releases, and web search results. Additional information about our approach to identifying clusters and collecting data about them can be found in the accompanying documentation.

### Downloads

### Citations

Epoch AI’s data is free to use, distribute, and reproduce provided the source and authors are credited under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/).

### Citation

Epoch AI, 'Data on GPU clusters'. Published online at epoch.ai. Retrieved from 'https://epoch.ai/data/gpu-clusters' \[online resource\]. Accessed 17 Nov 2026.

### BibTeX Citation

@misc{EpochAISupercomputers2025, title = {{Data on GPU clusters}}, author = {{Epoch AI}}, year = {2026}, month = {3}, url = {https://epoch.ai/data/gpu-clusters}, note = {Accessed: 17 Nov 2026} }

### Python Import

import pandas as pd data\_url = "https://epoch.ai/data/gpu\_clusters.csv" df = pd.read\_csv(data\_url)

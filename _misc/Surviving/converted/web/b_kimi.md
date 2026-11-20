Scraping: https://platform.moonshot.ai/docs/pricing/chat
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://platform.moonshot.ai/docs/pricing/chat
  Settled (dom-quiet, 1626ms)
  Extracting content...
  Extracted 4083 characters

--- Content ---

## Model Pricing

### K3 Series Models

All K3 series models support a 1,048,576-token context window.

<table><colgroup><col> <col> <col> <col> <col> <col></colgroup><thead><tr><th>Model</th><th colspan="2">Base tokens</th><th colspan="3">Prompt caching</th></tr><tr><th>Name</th><th>Input</th><th>Output</th><th>Cached Input</th><th>5m writes</th><th>1h writes</th></tr></thead><tbody><tr><td><a href="/docs/guide/kimi-k3-1-pro-quickstart">kimi-k3.1-pro</a></td><td>$2.00 / MTok</td><td>$10.00 / MTok</td><td>$0.20 / MTok</td><td>$2.00 / MTok</td><td>$4.00 / MTok</td></tr><tr><td><a href="/docs/guide/kimi-k3-1-pro-quickstart">kimi-k3.1-pro-highspeed</a></td><td>$4.00 / MTok</td><td>$20.00 / MTok</td><td>$0.20 / MTok</td><td>$4.00 / MTok</td><td>$8.00 / MTok</td></tr><tr><td><a href="/docs/guide/kimi-k3-quickstart">kimi-k3</a></td><td>$3.00 / MTok</td><td>$15.00 / MTok</td><td>$0.30 / MTok</td><td>$3.00 / MTok</td><td>$6.00 / MTok</td></tr></tbody></table>

Note: The Kimi API **automatically enables** context caching billing for repeated request prefixes, with a default TTL (time-to-live) of 5m. For TTL settings and cost optimization tips, see [Best Practices for Context Caching](/docs/guide/context-caching).

**[Batch API Inference](/docs/pricing/batch)**: `kimi-k3.1-pro` and `kimi-k3` support batch inference for large-scale tasks that do not require real-time responses, billed at 60% of the standard price.

### K2 Series Models

All K2 series models support a 262,144-token context window.

Dear Kimi Users, starting October 31, 2026, K2 series models will no longer be available to newly registered users; existing users are not affected. We plan to retire all K2 series models by the end of December 2026, please [prepare your migration](/docs/guide/kimi-k3-1-pro-quickstart) in advance.

<table><colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Model</th><th colspan="2">Base tokens</th><th colspan="1">Prompt caching</th></tr><tr><th>Name</th><th>Input</th><th>Output</th><th>Cached Input</th></tr></thead><tbody><tr><td>kimi-k2.7-code</td><td>$0.95 / MTok</td><td>$4.00 / MTok</td><td>$0.19 / MTok</td></tr><tr><td>kimi-k2.7-code-highspeed</td><td>$1.90 / MTok</td><td>$8.00 / MTok</td><td>$0.38 / MTok</td></tr><tr><td>kimi-k2.6</td><td>$0.95 / MTok</td><td>$4.00 / MTok</td><td>$0.16 / MTok</td></tr></tbody></table>

1 MTok = 1,000,000 tokens. All prices above are per MTok consumed.

**Explanation: Prices exclude applicable taxes. Specific tax obligations are subject to local tax regulations and will be calculated at checkout based on your jurisdiction.**

## Concepts

Model inference on the Kimi API platform is billed on a pay-as-you-go basis, with no subscription plan. It differs from products such as the Kimi membership and Kimi Code. [See the product comparison](/docs/guide/product-plans).

### Billing Unit

Token: the basic unit of text processed by the model. A long word like “antidisestablishmentarianism” may be split into several tokens, while a common short word like “word” usually takes just one. For typical English text, 1 token is roughly equivalent to 3-4 characters. Use the [Token Calculation API](/docs/api/estimate) to get the exact token count of each call.

### Billing Logic

Model inference APIs bill input and output tokens by usage. For K3 series models, cache writes are billed separately by TTL (5min / 1h); cached input is billed at the cache-hit price only, with no additional cache write charge. If you upload a document, extract its content, and pass the extracted content as model input, that content is also billed by usage. File-related APIs (file content extraction and file storage) are **temporarily free**: uploading and extracting a document alone incurs no file API charges. For tips on improving cache hit rates and choosing a TTL tier, see [Best Practices for Context Caching](/docs/guide/context-caching).

## Model Notes

See each model’s guide for capabilities and recommended use cases:

- [Kimi K3.1 Pro](/docs/guide/kimi-k3-1-pro-quickstart)
- [Kimi K3](/docs/guide/kimi-k3-quickstart)

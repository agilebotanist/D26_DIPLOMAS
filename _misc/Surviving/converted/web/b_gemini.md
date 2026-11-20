Scraping: https://ai.google.dev/gemini-api/docs/pricing
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://ai.google.dev/gemini-api/docs/pricing
  Settled (dom-quiet, 2291ms)
  Extracting content...
  Extracted 21195 characters

--- Content ---

## Gemini Developer API pricing

Copy page

Start building free of charge with generous limits, then scale up with prepaid and pay-as-you-go pricing for your production-ready applications.

Free

Paid

Enterprise

## Gemini 4 Carbon

Our most capable reasoning model, built for complex software engineering, deep mathematical and scientific problem solving, high factual accuracy, autonomous multi-step agents, and long-decode generation up to 1M tokens.

Gemini 4 Carbon is not available on the Free tier. Every token the model processes is counted and billed, including thinking tokens and internal tool system instructions and function declarations when using grounding.

## Gemini 4 Argon

Our efficient Gemini 4 frontier reasoning model. It delivers Gemini 4 intelligence with faster responses and lower token spend per turn compared to [Gemini 4 Carbon](https://aistudio.google.com/docs/pricing#gemini-4-carbon) across complex coding, agentic, math, and science tasks.

Gemini 4 Argon is not available on the Free tier. Every token the model processes is counted and billed, including thinking tokens and internal tool system instructions and function declarations when using grounding.

## Gemini 4 Hydrogen

Brings cutting-edge intelligence to everyone, with speed and efficiency for everyday coding and agentic workflows, featuring a unified 1M-token context window and long-decode generation up to 1M tokens.

Every token the model processes is counted and billed, including thinking tokens and internal tool system instructions and function declarations when using grounding.

## Gemini 3.8 Flash

Our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows.

## Gemini 3.6 Flash

Our previous generation Flash model, balancing speed and multimodal capabilities across general agentic and everyday tasks.

<sup>*</sup> A customer-submitted request to Gemini may result in one or more queries to Google Search. You will be charged for each individual search query performed.

<sup>**</sup> Can be tested in Google AI Studio.

## Gemini 3.5 Transcribe Live

Our low-latency, real-time speech-to-text model for bidirectional streaming audio transcription over WebSockets.

<sup>*</sup> Estimated pricing is based on 25 audio tokens per second for input and 175 text tokens per minute for output, for an effective blended rate of ~$0.009 per min for Live Transcribe.

## Gemini 3.5 Transcribe

Our speech-to-text model with automatic language detection, speaker diarization, word-level timestamps, and custom vocabulary biasing.

<sup>*</sup> Estimated pricing is based on 25 audio tokens per second for input and 175 text tokens per minute for output, for an effective blended rate of ~$0.005 per min for Transcribe.

## Gemini 3.5 Flash-Lite

A cost-efficient model, optimized for high-volume agentic tasks, translation, and simple data processing.

## Gemini Omni 1.2 Flash

Our next-generation video generation and editing model supporting up to 15 seconds of video generation and editing with native audio, now generally available to developers on the paid tier of the Gemini API.

<sup>*</sup> Billing is based on total output token consumption, calculated at a rate of 5,792 tokens per second of 720p video. Under Standard pricing ($12.00 per 1M tokens), this equates to an effective price of approximately $0.07 per second (~$0.70 for a 10s clip, ~$1.04 for a 15s clip; $0.023/s for 360p at 1,931 tokens/s; $0.104/s for 1080p with upsampling at 8,688 tokens/s; and $0.209/s for 4K with upsampling at 17,376 tokens/s).

## Gemini Omni 1.1 Flash

Previous generation video generation and editing model. Effective December 3, 2026, all API requests to `gemini-omni-1.1-flash` automatically route to [`gemini-omni-1.2-flash`](https://aistudio.google.com/docs/models/gemini-omni-flash#gemini-omni-1.2-flash) and are billed at `gemini-omni-1.2-flash` rates.

<sup>*</sup> Billing is based on total output token consumption, calculated at a rate of 5,792 tokens per second of 720p video. Under Standard pricing, this equates to an effective price of approximately $0.10 per second.

## Gemini 3.8 Live, Gemini 3.8 Live Extended Thinking, and Gemini 3.1 Flash Live Preview

Our low-latency, audio-to-audio models optimized for real-time dialogue with acoustic nuance detection, numeric precision, and multimodal awareness.

| Feature | Free Tier | Paid Tier, per 1M tokens in USD |
| --- | --- | --- |
| Input price | Free of charge | $0.75 (text)   $3.00 or $0.005/min (audio)   $1.00 or $0.002/min (image/video) |
| Output price (including thinking tokens) | Free of charge | $4.50 (text)   $12.00 or $0.018/min (audio) |
| Grounding with Google Search <sup>*</sup> | Supported | 5,000 free search requests per month (shared across all Gemini 3 and newer models), then $14 per 1,000 requests (subject to a [daily cap](https://aistudio.google.com/docs/pricing#pricing-for-tools) of 1,500 requests per day). |
| Used to improve our products | [Yes](https://aistudio.google.com/docs/terms) | [No](https://aistudio.google.com/docs/terms) |

<sup>*</sup> A customer-submitted request to Gemini may result in one or more queries to Google Search. You will be charged for each individual search query performed.

## Gemini 3.5 Live Translate

Our low-latency, real-time speech to speech translation model that supports 70+ languages.

<sup>*</sup> Billing is based on total input and output audio token consumption, calculated at a rate of 25 tokens per second of audio, equating to an effective price of approximately $0.0368 per minute.

## Gemini 3.1 Flash-Lite

A cost-efficient model, optimized for high-volume agentic tasks, translation, and simple data processing.

<sup>*</sup> A customer-submitted request to Gemini may result in one or more queries to Google Search. You will be charged for each individual search query performed.

<sup>**</sup> Can be tested in Google AI Studio.

## Gemini 3.1 Pro Preview

Our 3rd generation Pro model, built for multimodal understanding, agentic capabilities, and vibe-coding.

## Gemini Nano Banana 2.1 🍌

An update to Nano Banana 2 (Gemini 3.1 Flash Image), built for high-efficiency image generation and conversational editing with improved visual quality, multi-turn character consistency, accurate text rendering, and search-grounded generation across 1K, 2K, and 4K resolutions.

<sup>*</sup> Image output is priced at $30 per 1,000,000 tokens (Standard) and $15 per 1,000,000 tokens (Batch). Output images at 1K (1024x1024px) consume 1120 tokens and are equivalent to $0.0336 per image. Output images at 2K (2048x2048px) consume 1680 tokens and are equivalent to $0.0504 per image. Output images at 4K (4096x4096px) consume 3780 tokens and are equivalent to $0.113 per image.

<sup>**</sup> A customer-submitted request to Gemini may result in one or more queries to Google Search. You will be charged for each individual search query performed. Retrieved context (text or images) provided by Grounding with Google Search is not charged as input tokens.

## Gemini 3.1 Flash Image (Nano Banana 2) 🍌

Designed for speed and efficiency, the Gemini 3.1 Flash Image generation model is effective for quick, interactive responses and high throughput.

<sup>*</sup> Image output is priced at $60 per 1,000,000 tokens. Output images at 0.5K (512px) consume 747 tokens and are equivalent to $0.045 per image. Output images at 1K (1024x1024px) consume 1120 tokens and are equivalent to $0.067 per image. Output images at 2K (2048x2048px) consume 1680 tokens and are equivalent to $0.101 per image. Output images at 4K (4096x4096px) consume 2520 tokens and are equivalent to $0.151 per image.

## Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite) 🍌

Designed as the efficiency specialist of the image generation family, the Gemini 3.1 Flash Lite Image model is designed for ultra-low latency and cost-effective image generation and editing.

<sup>*</sup> Image output is priced at $30 per 1,000,000 tokens. Output images at 1K (1024x1024px) consume 1120 tokens and are equivalent to $0.0336 per image.

## Gemini 3.8 Flash TTS

Our 3.8 Flash Text-to-Speech audio model engineered for studio-grade voice fidelity, expressive acting, and long-form stability.

<sup>*</sup> Audio tokens correspond to 25 tokens per second of audio.

## Gemini 3.8 Flash-Lite TTS

Our 3.8 Flash-Lite Text-to-Speech audio model optimized for high-throughput, low-latency, and cost-efficient conversational speech.

<sup>*</sup> Audio tokens correspond to 25 tokens per second of audio.

## Gemini 3.1 Flash TTS Preview

Our 3.1 Flash Text-to-Speech audio model optimized for price-performant, low-latency, controllable speech generation.

<sup>*</sup> Audio tokens correspond to 25 tokens per second of audio.

## Gemini 3 Flash Preview

Our legacy Flash model, providing baseline speed and intelligence.

<sup>*</sup> A customer-submitted request to Gemini may result in one or more queries to Google Search. You will be charged for each individual search query performed.

<sup>**</sup> Can be tested in Google AI Studio.

## Gemini 3 Pro Image (Nano Banana Pro) 🍌

Our native image generation model, optimized for speed, flexibility, and contextual understanding. **Text input and output** is priced the same as [Gemini 3.1 Pro](https://aistudio.google.com/docs/pricing#gemini-3.1-pro-preview).

<sup>*</sup> Image input is set at 560 tokens or $0.0011 per image.

<sup>**</sup> Image output is priced at $120 per 1,000,000 tokens. Output images from 1024x1024px (1K) and up to 2048x2048px (2K) consume 1120 tokens and are equivalent to $0.134 per image. Output images up to 4096x4096px (4K) consume 2000 tokens and are equivalent to $0.24 per image.

<sup>***</sup> A customer-submitted request to Gemini may result in one or more queries to Google Search. You will be charged for each individual search query performed.

<sup>****</sup> Can be tested in Google AI Studio.

## Gemini 2.5 Pro

*[`gemini-2.5-pro`](https://aistudio.google.com/docs/models/gemini-2.5-pro)*

A Pro model which excels at coding and complex reasoning tasks.

## Gemini 2.5 Flash

*[`gemini-2.5-flash`](https://aistudio.google.com/docs/models/gemini-2.5-flash)*

Our first hybrid reasoning model which supports a 1M token context window and has thinking budgets.

## Gemini 2.5 Flash-Lite

A small and cost effective model, built for at scale usage.

## Gemini 2.5 Flash Native Audio (Live API)

Our [Live API](https://aistudio.google.com/docs/live-api) native audio models optimized for higher quality audio outputs with better pacing, voice naturalness, verbosity, and mood.

| Feature | Free Tier | Paid Tier, per 1M tokens in USD |
| --- | --- | --- |
| Input price | Free of charge | $0.50 (text)   $3.00 (audio / video) |
| Output price (including thinking tokens) | Free of charge | $2.00 (text)   $12.00 (audio) |
| Used to improve our products | [Yes](https://aistudio.google.com/docs/terms) | [No](https://aistudio.google.com/docs/terms) |

## Gemini 2.5 Flash Image (Nano Banana) 🍌

**Warning:** Gemini 2.5 Flash Image (`gemini-2.5-flash-image`) is [deprecated](https://aistudio.google.com/docs/deprecations) and will be shut down on March 15, 2027; migrate to [Gemini 3.1 Flash Lite Image](https://aistudio.google.com/docs/models/gemini-3.1-flash-lite-image) to avoid service disruption.

A native image generation model, optimized for speed, flexibility, and contextual understanding. Text input and output is priced the same as [2.5 Flash](https://aistudio.google.com/docs/pricing#gemini-2.5-flash).

<sup>*</sup> Image output is priced at $30 per 1,000,000 tokens. Output images up to 1024x1024px consume 1290 tokens and are equivalent to $0.039 per image.

## Gemini 2.5 Flash Preview TTS

Our 2.5 Flash text-to-speech audio model optimized for price-performant, low-latency, controllable speech generation.

## Gemini 2.5 Pro Preview TTS

Our 2.5 Pro text-to-speech audio model optimized for powerful, low-latency speech generation for more natural outputs and easier to steer prompts.

## Lyria 3.5

*[`lyria-3.5`](https://aistudio.google.com/docs/models/lyria-3.5)*

Google's music generation model.

| Feature | Free Tier | Paid Tier, per request in USD |
| --- | --- | --- |
| Lyria 3.5 (Full Song) | Not available | $0.08 per song |
| Used to improve our products | [Yes](https://aistudio.google.com/docs/terms) | [No](https://aistudio.google.com/docs/terms) |

## Lyria 3

*[`lyria-3-clip-preview`](https://aistudio.google.com/docs/models/lyria-3-clip-preview) and [`lyria-3-pro-preview`](https://aistudio.google.com/docs/models/lyria-3-pro-preview)*

Google's family of legacy music generation models.

| Feature | Free Tier | Paid Tier, per request in USD |
| --- | --- | --- |
| Lyria 3 Clip Preview (30s) | Not available | $0.04 per song |
| Lyria 3 Pro Preview (Full Song) | Not available | $0.08 per song |
| Used to improve our products | [Yes](https://aistudio.google.com/docs/terms) | [No](https://aistudio.google.com/docs/terms) |

## Gemini Decision 1

Our multimodal decision model for binary, categorical, and rubric evaluations across text, images, video, audio, and PDFs using the [Decisions API](https://aistudio.google.com/docs/decisions-api).

Each request bills shared input tokens once, regardless of question count. Each question adds tokens for its own instructions, criteria, and formatting, and generates zero output tokens. [Batch API](https://aistudio.google.com/docs/batch-api) isn't supported.

## Gemini Embedding 2

Our first multimodal embedding model, mapping text, images, video, audio, and PDFs into a unified embedding space.

## Gemini Embedding

Our first Gemini Embeddings model for text-only use cases.

## Gemini Robotics ER 2 Preview

Gemini Robotics ER 2, short for Gemini Robotics Embodied Reasoning 2, is a vision-language model endpoint that enables robots to understand their environments precisely, supporting agentic orchestration of robots, video progress understanding, multi-robot collaboration, and advanced spatial reasoning.

## Gemini Robotics ER 2 Streaming Preview

Gemini Robotics ER 2 Streaming is a vision-language model endpoint for robotics optimized for real-time text streaming using the Live API. It accepts text, image, video, and audio input and supports bidirectional streaming with function calling.

## Gemma 4

Our lightweight, state-of the art, open model built from the same technology that powers our Gemini models.

| Feature | Free Tier | Paid Tier, per 1M tokens in USD |
| --- | --- | --- |
| Input price | Free of charge | Not available |
| Output price | Free of charge | Not available |
| Context caching price | Free of charge | Not available |
| Context caching (storage) | Free of charge | Not available |
| Tuning price | Not available | Not available |
| Grounding with Google Search | Not available | Not available |
| Used to improve our products | [Yes](https://aistudio.google.com/docs/terms) | [No](https://aistudio.google.com/docs/terms) |

## Pricing for tools

Tools are priced at their own rates, applied to the model using them. Check the [Models](https://aistudio.google.com/docs/models) page for which tools are available to each model.

| Feature | Free Tier | Paid Tier, per 1M tokens in USD |
| --- | --- | --- |
| [Google Search](https://aistudio.google.com/docs/google-search#pricing) | 500 RPD free (limit shared for Flash and Flash-Lite).   Not available for Pro. | Gemini 2.5 models:   1,500 RPD free (limit shared for Flash and Flash-Lite).   Then $35 / 1,000 grounded prompts   Gemini 3 and newer models:   5,000 free search requests per month (shared across all Gemini 3 and newer models), then $14 per 1,000 requests. (Subject to a default daily cap of 1,500 requests per day (RPD) per project on the Gemini Developer API.) |
| [Google Maps](https://aistudio.google.com/docs/maps-grounding#pricing-and-rate-limits) | 500 RPD   Not available for Pro. | Gemini 2.5 models:   1,500 RPD free (limit shared for Flash and Flash-Lite)   10,000 RPD free for Pro.   Then $25 / 1,000 grounded prompts   Gemini 3 and newer models:   5,000 requests per month (free, shared across all Gemini 3 and newer models), then $14 / 1,000 search queries. |
| [Code execution](https://aistudio.google.com/docs/code-execution#billing) | Free of charge | Code execution is billed at the standard token rates for the selected model.   Costs are determined solely by tool usage; no charges accrue for session   runtime. Generated code and execution results are billed as **Output   tokens** when created, and as **Input tokens** when used by the model in   its iterative reasoning process. |
| [URL context](https://aistudio.google.com/docs/url-context#limitations) | Free of charge | Charged as input tokens per model pricing. |
| [Computer use](https://aistudio.google.com/docs/computer-use) | Not available | Charged as regular tokens per model pricing (e.g., standard [Gemini 3.8 Flash](https://aistudio.google.com/docs/pricing#gemini-3.8-flash) pricing). |
| [File search](https://aistudio.google.com/docs/file-search#pricing) | Free of charge | Charged for embeddings at [Gemini Embedding](https://aistudio.google.com/docs/pricing#gemini-embedding) ($0.15 / 1M tokens) or [Gemini Embedding 2](https://aistudio.google.com/docs/pricing#gemini-embedding-2) rates.   Retrieved document tokens charged as regular tokens per model pricing. |
| [Custom Tools endpoint (Gemini 3.1 Pro Preview)](https://aistudio.google.com/docs/models/gemini-3.1-pro-preview) | Not available | Same as [Gemini 3.1 Pro Preview](https://aistudio.google.com/docs/pricing#gemini-3.1-pro-preview) pricing |

## Pricing for agents

Agent usage costs are calculated based on the underlying token consumption and usage of the tools.

| Feature | Model | Tools |
| --- | --- | --- |
| [Gemini Deep Research agent](https://aistudio.google.com/docs/deep-research) | All model inference is charged at standard Gemini list rates, including input,   output, and intermediate input / reasoning tokens generated during agentic   loops. | Tool usage fees apply per existing pricing structure, maintaining standard   distinctions for Search Grounding (retrieved tokens excluded) versus   Url\_context / File Search (retrieved tokens included in all other tools). |
| [Managed agents in Gemini API](https://aistudio.google.com/docs/agents) | All model inference is charged at standard Gemini list rates, including input,   output, and intermediate input / reasoning tokens generated during agentic   loops. (See [pricing details](https://aistudio.google.com/docs/agents#pricing)). | Environment compute (CPU, memory, sandbox execution) is not billed during the preview period. |
| [Antigravity Agent](https://aistudio.google.com/docs/antigravity-agent) | All model inference is charged at standard Gemini list rates, including input,   output, and intermediate input / reasoning tokens generated during agentic   loops. (See [pricing details](https://aistudio.google.com/docs/agents#pricing)). | Environment compute (CPU, memory, sandbox execution) is not billed during the   preview period. |

## Notes

- **Agentic video understanding:** When using agentic video understanding, token usage is variable based on the content loaded by the model rather than full video length. This typically results in up to 88% fewer input tokens for long-form video, though token counts depend on query complexity and dynamic sampling depth (which may exceed 1 FPS for detailed visual segments). See [Agentic video understanding](https://aistudio.google.com/docs/video-understanding#agentic-video-understanding).
- **Document token billing:** Tokens for the `DOCUMENT` modality (for example, PDFs) are billed at the image token rate. In API responses, these tokens appear under the `DOCUMENT` modality within `promptTokensDetails`.
- Google AI Studio usage is free of charge in all [available regions](https://aistudio.google.com/docs/available-regions). See [Billing FAQs](https://aistudio.google.com/docs/billing) for details.
- Prices may differ from the prices listed here and the prices offered on Gemini Enterprise Agent Platform. For Gemini Enterprise Agent Platform prices, see the [Gemini Enterprise Agent Platform pricing page](https://cloud.google.com/products/gemini-enterprise-agent-platform).
- If you are using [dynamic retrieval](https://aistudio.google.com/docs/google-search) to optimize costs, only requests that contain at least one grounding support URL from the web in their response are charged for Grounding with Google Search. Costs for Gemini always apply. Rate limits are subject to change.
- **Search Grounding rate limits:** On the Gemini Developer API, Grounding with Google Search on Gemini 3 and newer models is subject to a default daily rate limit of 1,500 requests per day (RPD) per project across all paid tiers, resetting daily at midnight Pacific Time. For high-volume production workloads requiring higher daily limits, consider using [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-google-search#considerations), which provides a default quota of 1,000,000 search queries per day.

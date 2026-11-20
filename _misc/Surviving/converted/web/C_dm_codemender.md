Scraping: https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/
  Settled (dom-quiet, 1761ms)
  Extracting content...
  Extracted 8727 characters

--- Content ---

![An abstract 3D digital illustration representing CodeMender repairing software code. A pixelated grid pathway, glowing pink to represent a security vulnerability, is broken in the middle with floating, disjointed blocks, which then seamlessly connects back into a secure, curved blue grid path representing patched, functional software.](https://lh3.googleusercontent.com/39mmnrTBGBLnftfKvwK_oslUE1_bpS2hOrPkxdYy6C2bCp3B2dc1iBqLUgr-rZhyp1K0rcr-jifsh1cxWPpbg2tRigzqfp2cfuB13afrDvwD0YGg4g=w2880-h1620-n-nu-rw-lo)

Today, we’re sharing early results from our research on CodeMender, a new AI-powered agent that improves code security automatically.

Software vulnerabilities are notoriously difficult and time-consuming for developers to find and fix, even with traditional, automated methods like fuzzing. Our AI-based efforts like [Big Sleep](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html?utm_source=&utm_medium=&utm_campaign=&utm_content=) and [OSS-Fuzz](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html?utm_source=&utm_medium=&utm_campaign=&utm_content=) have demonstrated AI’s ability to find new zero-day vulnerabilities in well-tested software. As we achieve more breakthroughs in AI-powered vulnerability discovery, it will become increasingly difficult for humans alone to keep up.

CodeMender helps solve this problem by taking a comprehensive approach to code security that’s both reactive, instantly patching new vulnerabilities, and proactive, rewriting and securing existing code and eliminating entire classes of vulnerabilities in the process. Over the past six months that we’ve been building CodeMender, we have already upstreamed 72 security fixes to open source projects, including some as large as 4.5 million lines of code.

By automatically creating and applying high-quality security patches, CodeMender’s AI-powered agent helps developers and maintainers focus on what they do best — building good software.

## CodeMender in action

CodeMender operates by leveraging the thinking capabilities of recent [Gemini Deep Think](https://blog.google/products/gemini/gemini-2-5-deep-think/?utm_source=&utm_medium=&utm_campaign=&utm_content=) models to produce an autonomous agent capable of debugging and fixing complex vulnerabilities.

To do this, the CodeMender agent is equipped with robust tools that let it reason about code before making changes, and automatically validate those changes to make sure they’re correct and don’t cause regressions.

While large language models are rapidly improving, mistakes in code security could be costly. CodeMender’s automatic validation process ensures that code changes are correct across many dimensions by only surfacing for human review high-quality patches that, for example, fix the root cause of the issue, are functionally correct, cause no regressions and follow style guidelines.

As part of our research, we also developed new techniques and tools that let CodeMender reason about code and validate changes more effectively. This includes:

- **Advanced program analysis:** We developed tools based on advanced program analysis that include static analysis, dynamic analysis, differential testing, fuzzing and SMT solvers. Using these tools to systematically scrutinize code patterns, control flow and data flow, CodeMender can better identify the root causes of security flaws and architectural weaknesses.
- **Multi-agent systems:** We developed special-purpose agents that enable CodeMender to tackle specific aspects of an underlying problem. For example, CodeMender uses a large language model-based critique tool that highlights the differences between the original and modified code in order to verify that the proposed changes do not introduce regressions, and self-correct as needed.

## Fixing vulnerabilities

To effectively patch a vulnerability, and prevent it from re-emerging, Code Mender uses a debugger, source code browser, and other tools to pinpoint root causes and devise patches. We have added two examples of CodeMender patching vulnerabilities in the video carousel below.

**Example #1: Identifying the root cause of a vulnerability**

Here’s a snippet of the agent's reasoning about the root cause for a CodeMender-generated patch, after analyzing the results of debugger output and a code search tool.

Although the final patch in this example only changed a few lines of code, the root cause of the vulnerability was not immediately clear. In this case, the crash report showed a heap buffer overflow, but the actual problem was elsewhere — an incorrect stack management of Extensible Markup Language (XML) elements during parsing.

**Example #2: Agent is able to create non-trivial patches**

In this example, the CodeMender agent was able to come up with a non-trivial patch that deals with a complex object lifetime issue.

The agent was not only able to figure out the root cause of the vulnerability, but was also able to modify a completely custom system for generating C code within the project.

## Proactively rewriting existing code for better security

We also designed CodeMender to proactively rewrite existing code to use more secure data structures and APIs.

For example, we deployed CodeMender to apply [\-fbounds-safety](https://clang.llvm.org/docs/BoundsSafety.html) annotations to parts of a widely used image compression library called [libwebp](https://github.com/webmproject/libwebp). When **\-fbounds-safety** annotations are applied, the compiler adds bounds checks to the code to prevent an attacker from exploiting a buffer overflow or underflow to execute arbitrary code.

A few years ago, a heap buffer overflow vulnerability in libwebp ([CVE-2023-4863](https://www.cve.org/CVERecord?id=CVE-2023-4863)) was used by a threat actor as part of [a zero-click iOS exploit](https://citizenlab.ca/2023/09/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/). With **\-fbounds-safety** annotations, this vulnerability, along with most other buffer overflows in the project where we've applied annotations, would’ve been rendered unexploitable forever.

In the video carousel below we show examples of the agent’s decision-making process, including the validation steps.

**Example #1: Agent’s reasoning steps**

In this example, the CodeMender agent is asked to address the following **\-fbounds-safety** error on **bit\_depths** pointer:

![Screenshot showing a compiler error message on a line of code, illustrating a security vulnerability that the CodeMender agent is designed to fix](https://lh3.googleusercontent.com/Xyb8mdGPNRm_nicRcCB37es04rfSoZc0i93Hf2oTPCGCH-2CcoaS54_fftTADcam2ykx9bOn48IR1fbbiTC_mX5KOy_uzDEf0gJ4UY6t8tD0bmkaO84=w640-rw-lo)

**Example #2: Agent automatically corrects errors and test failures**

Another of CodeMender’s key features is its ability to automatically correct new errors and any test failures that arise from its own annotations. Here is an example of the agent recovering from a compilation error.

**Example #3: Agent validates the changes**

In this example, the CodeMender agent modifies a function and then uses the LLM judge tool configured for functional equivalence to verify that the functionality remains intact. When the tool detects a failure, the agent self-corrects based on the LLM judge's feedback.

## Making software secure for everyone

While our early results with CodeMender are promising, we’re taking a cautious approach, focusing on reliability. Currently, all patches generated by CodeMender are reviewed by human researchers before they’re submitted upstream.

Using CodeMender, we've already begun submitting patches to various critical open-source libraries, many of which have already been accepted and upstreamed. We’re gradually ramping up this process to ensure quality and systematically address feedback from the open-source community.

We’ll also be gradually reaching out to interested maintainers of critical open source projects with CodeMender-generated patches. By iterating on feedback from this process, we hope to release CodeMender as a tool that can be used by all software developers to keep their codebases secure.

We will have a number of techniques and results to share, which we intend to publish as technical papers and reports in the coming months. With CodeMender, we've only just begun to explore AI’s incredible potential to enhance software security for everyone.

**Acknowledgements**

Credits (listed in alphabetical order):

Alex Rebert, Arman Hasanzadeh, Carlo Lemos, Charles Sutton, Dongge Liu, Gogul Balakrishnan, Hiep Chu, James Zern, Koushik Sen, Lihao Liang, Max Shavrick, Oliver Chang and Petros Maniatis.

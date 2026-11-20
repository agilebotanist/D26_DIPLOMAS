Scraping: https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
  Settled (dom-quiet, 2540ms)
  Extracting content...
  Extracted 8119 characters

--- Content ---

*Comprehensive Analysis of More Than 100 Large Language Models Exposes Security Gaps: Java Emerges as Highest-Risk Programming Language, While AI Misses 86% of Cross-Site Scripting Threats*

**BURLINGTON, Mass.** – July 30, 2025 – [Veracode](https://www.veracode.com/), a global leader in application risk management, today unveiled its *[2025 GenAI Code Security Report](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/?utm_source=veracode&utm_medium=press-release&utm_content=ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals)*, revealing critical security flaws in AI-generated code. The study analyzed 80 curated coding tasks across more than 100 large language models (LLMs), revealing that while AI produces functional code, it introduces security vulnerabilities in 45 percent of cases.

The research demonstrates a troubling pattern: when given a choice between a secure and insecure method to write code, GenAI models chose the insecure option 45 percent of the time. Perhaps more concerning, Veracode’s research also uncovered a critical trend: despite advances in LLMs’ ability to generate syntactically correct code, security performance has not kept up, remaining unchanged over time.

![](https://www.veracode.com/wp-content/uploads/GenAI-Coding-Report-Graph.png)

*Figure 1: Security and Syntax Pass Rates vs LLM Release Date*

“The rise of vibe coding, where developers rely on AI to generate code, typically without explicitly defining security requirements, represents a fundamental shift in how software is built,” said Jens Wessling, Chief Technology Officer at Veracode. “The main concern with this trend is that they do not need to specify security constraints to get the code they want, effectively leaving secure coding decisions to LLMs. Our research reveals GenAI models make the wrong choices nearly half the time, and it’s not improving.”

AI is enabling attackers to identify and exploit security vulnerabilities quicker and more effectively. Tools powered by AI can scan systems at scale, identify weaknesses, and even generate exploit code with minimal human input. This lowers the barrier to entry for less-skilled attackers and increases the speed and sophistication of attacks, posing a significant threat to traditional security defenses. Not only are vulnerabilities increasing, but the ability to exploit them is becoming easier.

**LLMs Introduce Dangerous Levels of Common Security Vulnerabilities**

To evaluate the security properties of LLM-generated code, Veracode designed a set of 80 code completion tasks with known potential for security vulnerabilities according to the [MITRE Common Weakness Enumeration](https://docs.veracode.com/r/c_review_cwe) (CWE) system, a standard classification of software weaknesses that can turn into vulnerabilities. The tasks prompted more than 100 LLMs to auto-complete a block of code in a secure or insecure manner, which the research team then analyzed using Veracode Static Analysis. In 45 percent of all test cases, LLMs introduced vulnerabilities classified within the OWASP (Open Web Application Security Project) Top 10—the most critical web application security risks.

Veracode found Java to be the riskiest language for AI code generation, with a security failure rate over 70 percent. Other major languages, like Python, C#, and JavaScript, still presented significant risk, with failure rates between 38 percent and 45 percent. The research also revealed LLMs failed to secure code against cross-site scripting (CWE-80) and log injection (CWE-117) in 86 percent and 88 percent of cases, respectively.

“Despite the advances in AI-assisted development, it is clear security hasn’t kept pace,” Wessling said. “Our research shows models are getting better at coding accurately but are not improving at security. We also found larger models do not perform significantly better than smaller models, suggesting this is a systemic issue rather than an LLM scaling problem.”

**Managing Application Risks in the AI Era**

While GenAI development practices like vibe coding accelerate productivity, they also amplify risks. Veracode emphasizes that organizations need a comprehensive risk management program that prevents vulnerabilities before they reach production—by integrating code quality checks and automated fixes directly into the development workflow.

As organizations increasingly leverage AI-powered development, Veracode recommends taking the following proactive measures to ensure security:

- **Integrate AI-powered tools** like [**Veracode Fix**](https://www.veracode.com/products/fix/) into developer workflows to remediate security risks in real time.
- **Leverage** [**Static Analysis**](https://www.veracode.com/products/binary-static-analysis-sast/) to detect flaws early and automatically, preventing vulnerable code from advancing through development pipelines.
- **Embed security in agentic workflows** to automate policy compliance and ensure AI agents enforce secure coding standards.
- **Use** [**Software Composition Analysis** **(SCA)**](https://www.veracode.com/products/software-composition-analysis/) to ensure AI-generated code does not introduce vulnerabilities from third-party dependencies and open-source components.
- **Adopt bespoke AI-driven remediation guidance** to empower developers with precise fix instructions and train them to use the recommendations effectively.
- **Deploy a** [**Package Firewall**](https://www.veracode.com/products/veracode-package-firewall/) to automatically detect and block malicious packages, vulnerabilities, and policy violations.

“AI coding assistants and agentic workflows represent the future of software development, and they will continue to evolve at a rapid pace,” Wessling concluded. “The challenge facing every organization is ensuring security evolves alongside these new capabilities. Security cannot be an afterthought if we want to prevent the accumulation of massive security debt.”

The complete 2025 GenAI Code Security Report is [available to download](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/?utm_source=veracode&utm_medium=press-release&utm_content=ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals) on the Veracode website.

## About Veracode

Veracode is a global leader in Application Risk Management for the AI era. Powered by trillions of lines of code scans and a proprietary AI-assisted remediation engine, the Veracode platform is trusted by organizations worldwide to build and maintain secure software from code creation to cloud deployment. Thousands of the world’s leading development and security teams use Veracode every second of every day to get accurate, actionable visibility of exploitable risk, achieve real-time vulnerability remediation, and reduce their security debt at scale. Veracode is a multi-award-winning company offering capabilities to secure the entire software development life cycle, including Veracode Fix, Static Analysis, Dynamic Analysis, Software Composition Analysis, Container Security, Application Security Posture Management, Malicious Package Detection, Package Firewall, and Penetration Testing.

Learn more at  [www.veracode.com](https://www.veracode.com/), on the  [Veracode blog](/blog), and on  [LinkedIn](https://www.linkedin.com/company/veracode/)  and  [X](https://x.com/Veracode?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor&mx=2).

Copyright © 2025 Veracode, Inc. All rights reserved. Veracode is a registered trademark of Veracode, Inc. in the United States and may be registered in certain other jurisdictions. All other product names, brands or logos belong to their respective holders. All other trademarks cited herein are property of their respective owners.

## Press and Media Contacts

**Veracode:**
Katy Gwilliam
Head of Global Communications, Veracode
[kgwilliam@veracode.com](mailto:kgwilliam@veracode.com)

Related Links
[veracode.com](https://www.veracode.com/)

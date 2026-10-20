Detecting Clean Architecture Violations in
Software Maintenance using static tools and
LLMs
Author: Aziz Vundirov
Supervisor: Andrey Sadovykh
October 11, 2026
1
Abstract
Clean Architecture keeps long-lived software cheap to change [1], but during
maintenance its principles erode and conformance is still checked mostly by eye,
which does not scale to many heterogeneous repositories. The standard tools
address only part of the problem. ArchUnit enforces dependency rules exactly,
but the rules must be written and updated by hand and see only syntax, not intent
[2]. SonarQube reports code smells, bugs and vulnerabilities, but in practice
only about 13% of its issues are ever fixed, so the backlog turns into a dump of
unaddressed warnings [3]. Large language models can judge semantic violations,
but they are non-deterministic and sensitive to how the code base is put into their
context [4], [5]. The closest prior work constrains an LLM with a criterion-based
rubric, static evidence and a JSON output contract and has experts confirm every
finding, but it cannot tell how many violations were missed, and dependency
inversion, which depends on runtime wiring, is its weakest criterion [6]. This
thesis restricts the problem to Java systems in the maintenance phase and (i)
compares the rubric-constrained LLM approach with ArchUnit tests written for
the same Clean Architecture rules, and (ii) extends the rubric framework with
dynamic context collected while the system runs (dependency-injection wiring,
reflective calls and runtime call edges) to test whether this increases the number
of confirmed violations. The evaluation reports precision, relative recall against
a pooled and expert-reviewed ground truth, paired comparison with McNemar’s
exact test, and agreement statistics between reviewers and the model.
Chapter 1
Introduction
1.1 Domain
This thesis takes the book Clean Architecture [1] as the single source of the
principles that a system is checked against. A system is divided into concen
tric layers: entities, use cases, interface adapters, and frameworks and drivers.
The central requirement is the Dependency Rule: source-code dependencies may
point only inwards, so that business rules do not depend on the user interface, the
database or the framework. Where control must flow outwards, the dependency
inversion principle is applied: the inner layer declares an interface and the outer
layer implements it. The remaining principles that we check (separation of con
cerns, frameworkanddatabaseindependence, theSOLIDprinciplesatcomponent
level, testability) are derived from the same book. For code-level problems, the
term code smell is used in the sense of Clean Code [7].
The thesis concentrates on the maintenance phase: a system that was de
signed with Clean Architecture keeps receiving changes, and each change can
break a principle without anyone noticing. A multivocal review of 108 studies
1.2 Problem statement
3
finds that detection of such architectural degradation is well studied, but tools
rarely support ongoing remediation [8]. The work is limited to Java, because both
mainstream tools that we use as a reference, ArchUnit and SonarQube, support it
fully.
1.2 Problem statement
In most teams conformance to Clean Architecture is still checked informally,
by other developers during code review. This does not scale, especially for
organisations with many heterogeneous repositories [6]. There are three ways to
automate the check, and each has a known weakness.
1. Architecture tests (ArchUnit). Rules such as “classes in the domain pack
age must not depend on classes in the persistence package” are written as
unit tests over the class dependency graph and run in continuous integration
[2]. They are exact, but they must be written and maintained by hand after
each refactoring, and they see only dependencies. A domain service that
formats HTML e-mails passes every import rule. In a student setting, De
Luca et al. found that the projects violated the architectural principles even
though the rules were available [2].
2. General static analysers (SonarQube). SonarQube reports code smells
(duplication, unused code, excessive complexity), bugs and vulnerabilities
and grades them as Blocker, Critical, Major, Minor or Info. In real projects,
however, only about 13%ofthereportedissueswereresolved; fixingstarted
on average around 19 days after an issue appeared; mostly easy Major code
smells and Critical vulnerabilities were fixed, although the team leads in the
1.2 Problem statement
4
same study considered the warnings relevant [3]. The issue list therefore
grows into a backlog that hides the real technical debt, and SonarQube does
not know the architecture of the system at all.
3. Large language models. An LLM can judge intent, for example that
a use case contains presentation logic. But LLMs are non-deterministic
and depend strongly on what is put into their context. On SWE-bench,
where models receive the code base and an issue description, the best
retrieval-based configuration resolved only a few percent of real GitHub
issues [4]. Adding structural requirements, including a layered architecture,
to a backend generation task lowers the share of passed assertions by about
30 percentage points, and heavy frameworks with much hidden behaviour
suffer most [5]. Simply telling a model to “check Clean Architecture” is
therefore not reliable.
The closest prior work combines the strengths of the second and third options
[6]. It binds the LLM with a rubric of eight criteria, traceable static evidence
per module and a strict JSON output format, and has three experts review every
finding. All1136findingsweresupportedbytheexperts. Twoquestions,however,
stay open. First, only findings that the model produced were reviewed, so the
number of violations it missed is unknown and recall cannot be computed; the
baseline was a simple scoring heuristic, not an architecture-test tool. Second, the
projects were analysed statically only, so dependency inversion, which is realised
at runtime by a dependency-injection container, reflection or dynamic loading,
had the weakest evidence of all criteria.
1.3 Goal of the Thesis
5
1.3 Goal of the Thesis
The goal is to determine whether a rubric-constrained LLM can replace
or complement hand-written architecture tests for detecting Clean Architecture
violations in maintained Java systems, and whether adding dynamic (runtime)
context to its input increases the number of violations it finds. The thesis tests
two hypotheses.
H1. AnLLMwithaproperlydesignedprompt(constraints,rubrics,contextabout
the code) is able to detect no fewer violations than ArchUnit tests.
H2. Optimising the rubric framework of [6] by adding dynamic context is able
to increase the number of true positive cases.
1.4 Contributions
• A reproduction of the evidence-based rubric framework [6] for Java, and
the first direct comparison of it with ArchUnit tests that encode the same
Clean Architecture rules.
• Anextensionoftheevidence package with dynamic context collected while
the test suite runs, and a measurement of its effect per criterion.
• Aground truth that is not limited to the model’s own output (pooled from
all checkers and reviewed blindly), which makes relative recall and missed
violations measurable.
Out ofscope. Automaticrepairofdetected violations, for example an agent that
closes SonarQube issues itself, is left for future work. Current agents repair archi
1.4 Contributions
6
tectural smells unreliably: in SmellBench the best of 11 configurations resolved
47.7% of the cases and the most aggressive one introduced 140 new smells [9].
An accurate detector with few false positives is the necessary first step.
Chapter 2
State-of-the-Art
2.1 Definitions: CleanArchitectureandcodesmells
Clean Architecture [1] is used as the reference model: concentric layers, the
Dependency Rule, dependency inversion at layer boundaries, and independence
of business rules from frameworks, the database and the user interface. From
these principles we derive the list of violation types (Section 3.2). Code smells
are defined as in Clean Code [7]; they are relevant here because SonarQube
reports them, but they are local to a class or method, whereas Clean Architecture
violations concern the relations between components.
2.2 Architecture tests: ArchUnit
ArchUnit is a Java library that imports compiled classes, builds their depen
dency graph and lets the developer express architectural rules as ordinary unit
tests, for example layered-architecture or “no cycles” rules. De Luca et al. wrote
ArchUnit tests for the intended architecture of student team projects, ran them
2.3 General static analysis: SonarQube
8
together with SonarQube in continuous integration, and found that architectural
anti-patterns and layering violations were common, i.e. the students ignored the
principles even when the rules existed [2]. SecArchUnit extends ArchUnit to
security constraints; on three open-source systems it was the only compared tool
that detected information-flow violations, because SonarQube and PMD analyse
each class separately [10].
Limitations: each rule must be written and maintained by hand and must
be updated after refactoring; only what can be stated as a dependency or naming
constraint can be checked, so semantic violations are invisible.
2.3 General static analysis: SonarQube
SonarQube reports code smells, bugs and vulnerabilities and assigns them
a severity (Blocker, Critical, Major, Minor, Info). Marcilio et al. studied how
SonarQube is used in practice [3]. Only about 13% of the reported issues were
resolved; developers started fixing an issue on average about 19 days after it was
reported; the issues that were fixed were mostly Major code smells, which are
easy to fix, and Critical vulnerabilities. At the same time, the team leads surveyed
in the study considered the warnings relevant.
Limitations: the high number of open issues, many of which developers treat
as false positives or low priority, turns the issue list into a dump and creates a
misleading picture of technical debt; SonarQube has no model of the intended
architecture.
2.4 LLMs on software engineering tasks: the role of context
9
2.4 LLMs on software engineering tasks: the role
of context
SWE-bench gives a model areal repository and an issue description and asks
it to produce a patch [4]. With retrieval of relevant files, the best model resolved
only a few percent of the issues (3.79% for Claude 3 Opus in the retrieval-based
setting), and performancefallsasmoreirrelevantcontextisadded. Theconclusion
for this thesis is that the code base cannot simply be pasted into the prompt; the
context must be selected and structured. Constraint decay shows the second
side of the problem: when structural requirements such as a database, an ORM
and a layered architecture are added to a backend generation task, the share of
passed assertions drops by about 30 percentage points, and agents work well with
lightweight frameworks but fail with heavy, convention-based ones where much
happens implicitly [5]. Non-determinism is also visible in a Clean Architecture
and CQRS case study: of 300 GPT-4.1 calls, 10.33% failed at least one output
contract test, and only 56.67% of prompts gave identical output in all five runs
[11].
2.5 Evidence-based LLM assessment of Clean Ar
chitecture
Gonzalez Bravo et al. start from the observation that Clean Architecture
conformance is assessed informally and does not scale across many heteroge
neous repositories [6]. They propose a framework in which the LLM is bound
by three things: (1) a rubric of eight criteria (CA01–CA08: dependency rule,
2.5 Evidence-based LLM assessment of Clean Architecture
10
separation of concerns, framework independence, database independence, depen
dency inversion, single responsibility, testability, evidence traceability), where
each criterion lists the static signals that indicate a violation; (2) a static evidence
package per module(filestructure, imports, frameworkandpersistenceindicators,
code snippets); (3) a strict JSON output contract. On 36 modules from 12 open
source systems, two models (DeepSeek V4 Flash and Qwen 3.6 Plus) produced
1136 findings; all outputs were valid JSON. Three experts reviewed every finding
blindly with a 2-of-3 consensus rule, and all findings were supported, with small
differences in the assigned severity. Agreement was measured with weighted Co
hen’s kappa (ordinal agreement that penalises large disagreements more), Gwet’s
AC1/AC2 (robust to imbalanced categories, avoiding the kappa paradox), Krip
pendorff’s alpha (any number of raters, missing values allowed) and McNemar’s
exact test (systematic bias between two raters on binary decisions). Dependency
inversion (CA05) was the hardest criterion, with the lowest evidence sufficiency
(66.2%), because reflection, dependency-injection containers and dynamic load
ing are not visible in static evidence.
Limitations: (i) the ground truth consists of the model’s own findings after
expert review, so violations the model never reported are not counted and recall
is unknown; (ii) the baseline is a lightweight rule-based scorer, not ArchUnit
or another conformance tool; (iii) the projects were not built or run, so runtime
wiring is invisible. The authors themselves name stronger external baselines
and better evidence for dependency inversion as future work. These limitations
motivate the two hypotheses of this thesis.
2.6 Related LLM-based detection
11
2.6 Related LLM-based detection
Su et al. check 980 architectural decision records from 109 repositories with
several LLMs and retrieval-augmented generation [12]. Most errors were seman
tic misinterpretation (44.57%) or caused by information not present in the source
code (28.26%), and infrastructure and deployment decisions caused 42.39% of
errors; the authors propose combining static analysis with LLM reasoning. Souza
et al. compare four LLMs with static analysis tools for code-smell detection in
30 Java projects and find that a hybrid of LLM and static analysis gives the best
F1 for 5 of 9 smells [13]. Both results support giving the model evidence from
analysis tools instead of raw code, and the first one points to missing runtime
information as a main error source.
2.7 Research gap
Rubric-constrained, evidence-based LLM assessment of Clean Architecture
exists [6], but (i) it has not been compared with hand-written architecture tests on
the same rules, (ii) its recall, i.e. the number of missed violations, has not been
measured, and (iii) its evidence is purely static, which is the stated reason for the
weakest criterion, dependency inversion. This thesis addresses these three points
for Java systems in the maintenance phase.
Chapter 3
Methodology and Evaluation
Plan
3.1 Subject systems
We select 4–6 open-source Java systems (Spring-based and at least one built
on a lightweight framework) that declare a Clean or hexagonal architecture, have
an active commit history and an executable test suite. For each system we analyse
a recent release snapshot and, to reflect the maintenance phase, several earlier
snapshots, so that violations introduced by later changes are included.
3.2 Violation taxonomy
From [1] and the rubric of [6] we derive a list of violation types and split it
into two groups:
• formal violations, expressible as dependency or naming rules: an inner
3.3 Configurations compared
13
layer imports an outer layer, a domain class uses a framework or persistence
annotation, a dependency cycle between components;
• semantic violations, which require understanding intent: business logic in
a controller or repository adapter, presentation or transport logic in a use
case, a port interface that leaks infrastructure types, dependency inversion
realised only nominally.
3.3 Configurations compared
1. ArchUnit. Tests written once per system for every formal violation type,
using the system’s documented layer structure. SonarQube is run alongside
to show how many of its issues relate to the architecture at all.
2. LLM, static context (reproduction of [6]). The same rubric, static evi
dence package and JSON output contract.
3. LLM, static and dynamic context (proposed). The evidence package
from configuration 2 extended with runtime evidence collected while the
system’s test suite runs: the bean graph of the dependency-injection con
tainer (which implementation is actually injected into each port), reflective
calls and dynamically loaded classes recorded by a Java agent, and observed
caller–callee edges between layers.
All LLM configurations use the same models (at least one open-weight and
one proprietary model), a fixed temperature and the same output schema; each
configuration is run five times per module to measure stability.
3.4 Ground truth
14
3.4 Ground truth
Recall needs labels that do not depend on one model’s output. We build
them in two parts.
• Formal violations are labelled exhaustively by the ArchUnit rules and
checked manually for false positives.
• Semantic violations: all findings of all configurations are pooled, and two
reviewers independently judge each pooled finding against the rubric with
out knowing which configuration produced it; disagreements are resolved
by discussion. In addition, a random sample of modules is reviewed in full
by the reviewers to estimate the share of violations that no configuration
found.
Reviewer agreement is reported with weighted Cohen’s kappa, Gwet’s AC1 and
Krippendorff’s alpha, as in [6].
3.5 Metrics and tests
• number of true positives, precision, and relative recall against the pooled
ground truth, per violation type and per rubric criterion;
• H1: numberofviolations detected by ArchUnit and by the LLM, compared
per labelled violation (found / not found) with McNemar’s exact test;
• H2: number of true positives of configuration 2 versus configuration 3,
compared with McNemar’s exact test;
3.6 Threats to validity
15
• run-to-run stability (share of findings reproduced in all five runs), rate of
invalid outputs, token cost.
3.6 Threats to validity
A small number of systems and one language limit generalisation. Pooled
ground truth underestimates the violations that no configuration found; the fully
reviewed sample of modules estimates this effect. Semantic labels are partly
subjective, which is mitigated by two blind reviewers and reported agreement.
ArchUnit results depend on how well the tests are written; we write them from
documented architecture before running any LLM. Dynamic context covers only
the code exercised by the test suite, so we report test coverage per system. Model
versions change over time; exact versions and prompts are published.
Chapter 4
Detailed Work Plan and
Schedule
Theresearch will be done in two semesters. Thefirst produces the taxonomy,
the subject systems and the tools; the second runs the experiments and the thesis
is written. All steps are documented in parallel.
Semester 1
• Literature review and taxonomy (October–November): finalise related
work, derive the violation taxonomy from [1] and adapt the rubric of [6].
• Subject systems and baselines (November–December): select the Java
systems, write the ArchUnit tests, run SonarQube, and reproduce the static
evidence LLM pipeline.
17
Semester 2
• Dynamiccontext(January–February): implement the Java agent and the
dependency-injection wiring extractor, and extend the evidence package.
• Experiments and labelling (March–April): run all configurations with
repeated runs, pool the findings and carry out the blind review.
• Analysis and writing (May): test H1 and H2, finalise the thesis, prepare
the defence, and submit a paper to a relevant conference or journal.
Chapter 5
Conclusion
Conformance to Clean Architecture erodes during maintenance and is still
checked mostly by hand. ArchUnit checks formal rules exactly but must be
maintained and is blind to intent; SonarQube produces many issues that are
never fixed and knows nothing of the architecture; LLMs can judge intent but
are non-deterministic and depend on their context. The closest prior work makes
LLM findings precise and auditable, but does not measure what it misses and
lacks runtime information. The expected outcome of this thesis is an answer to
whether a rubric-constrained LLM finds at least as many violations as ArchUnit
on Java systems, ameasuredeffectofdynamiccontextonthenumberofconfirmed
violations, and a ground truth that allows recall to be reported. Automatic repair
of the detected violations is the natural next step.
Bibliography cited
[1] R. C. Martin, Clean Architecture: A Craftsman’s Guide to Software Struc
ture and Design. Prentice Hall, 2017. [Online]. Available: https://dl.acm.
org/doi/abs/10.5555/3175742.
[2] M. De Luca, S. Di Meglio, A. R. Fasolino, L. L. L. Starace, and P. Tra
montana, “Automatic assessment of architectural anti-patterns and code
smells in student software projects,” in Proceedings of the 28th Interna
tional Conference on Evaluation and Assessment in Software Engineering
(EASE), ACM, 2024. DOI: 10.1145/3661167.3661290.
[3] D. Marcilio, R. Bonif´ acio, E. Monteiro, E. Canedo, W. Luz, and G. Pinto,
“Are static analysis violations really fixed? A closer look at realistic usage
of SonarQube,” in Proceedings of the 27th IEEE/ACM International Con
ference on Program Comprehension (ICPC), IEEE, 2019, pp. 209–219.
DOI: 10.1109/ICPC.2019.00040.
[4] C. E. Jimenez et al., SWE-bench: Can language models resolve real-world
GitHub issues? 2023. arXiv: 2310.06770. [Online]. Available: https://
arxiv.org/abs/2310.06770.
BIBLIOGRAPHYCITED
20
[5] F. Dente et al., Constraint decay: The fragility of LLM agents in backend
code generation, 2026. arXiv: 2605.06445. [Online]. Available: https:
//arxiv.org/abs/2605.06445.
[6] E. J. Gonzalez Bravo, G. Chavira Juarez, E. Alvarez Navarro, A. Montoto
Gonzalez, and J. L. Diaz Juarez, “An evidence-based LLM framework for
expert-validated clean architecture conformance assessment in enterprise
software systems,” Computers, vol. 15, no. 10, p. 657, 2026. DOI: 10.3390/
computers15100657. [Online]. Available: https://www.mdpi.com/2073
431X/15/10/657.
[7] R. C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship.
Prentice Hall, 2008.
[8] N. Ahmad, R. Su, M. Esposito, A. Janes, V. Lenarduzzi, and D. Taibi, Ar
chitectural degradation: Definition, motivations, measurement and reme
diation approaches, 2025. arXiv: 2507.14547. [Online]. Available: https:
//arxiv.org/abs/2507.14547.
[9] I. G. Dinu, M. C. Mih˘ aescu, and T. Rebedea, SmellBench: Evaluating
LLM agents on architectural code smell repair, 2026. arXiv: 2605.07001.
[Online]. Available: https://arxiv.org/abs/2605.07001.
[10] M. Randevik and P. Olson, “SecArchUnit: Extending ArchUnit to support
validation of security architectural constraints,” M.S. thesis, Chalmers Uni
versity of Technology and University of Gothenburg,2020.[Online].Avail
able: https://odr.chalmers.se/server/api/core/bitstreams/4851b5ce
4247-4200-8f56-67fbfa7015ab/content.
BIBLIOGRAPHYCITED
21
[11] A. Ivanova, G. Kolev, F. Sapundzhi, T. Bakardjieva, and S. Georgiev,
“Integration of large language models in layered software systems: A clean
architecture and CQRS case study,” Engineering Proceedings, vol. 154,
no. 1, p. 23, 2026. DOI: 10.3390/engproc2026154023. [Online]. Available:
https://www.mdpi.com/2673-4591/154/1/23.
[12] R. Su, A. Bakhtin, N. Ahmad, M. Esposito, V. Lenarduzzi, and D. Taibi,
Evaluating large language models for detecting architectural decision vio
lations, 2026. arXiv: 2602.07609. [Online]. Available: https://arxiv.org/
html/2602.07609v1.
[13] S. Souza, A. Santana, E. Figueiredo, I. Muzetti, J. E. Montandon, and L.
Briand, Beyond strict rules: Assessing the effectiveness of large language
models for code smell detection, 2026. arXiv: 2601.09873. [Online]. Available:
https://arxiv.org/pdf/2601.09873

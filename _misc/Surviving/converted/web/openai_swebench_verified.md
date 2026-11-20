Scraping: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
  Mode: headless | Format: markdown
  Launching headless browser...
  Headless browser ready
  Navigating to: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
  Consent dismissed via: text-match:accept
  Settled (dom-quiet, 1974ms)
  Extracting content...
  Extracted 22888 characters

--- Content ---

## Why SWE-bench Verified no longer measures frontier coding capabilities

SWE-bench Verified is increasingly contaminated. We recommend SWE-bench Pro.

Since we first published [SWE-bench Verified](/index/introducing-swe-bench-verified/) in August 2024, the industry has widely used it to measure the progress of models on autonomous software engineering tasks. After its release, SWE-bench Verified provided a strong signal of capability progress and became a standard metric reported in frontier model releases. Tracking and forecasting progress of these capabilities is also an important part of OpenAI’s [Preparedness Framework](/index/updating-our-preparedness-framework/). When we created the Verified benchmark initially, we attempted to solve issues in the original evaluation that made certain tasks impossible to accomplish in the [SWE-bench dataset⁠](https://arxiv.org/abs/2310.06770).

After initial leaps, state-of-the-art progress on SWE-bench Verified has slowed, [improving⁠](https://llm-stats.com/benchmarks/swe-bench-verified) from 74.9% to 80.9% in the last 6 months. This raises the question: do the remaining failures reflect model limitations or properties of the dataset itself?

In a new analysis, we found two major issues with the Verified set that indicate the benchmark is no longer suitable for measuring progress on autonomous software engineering capabilities for frontier launches at today’s performance levels:

1. **Tests reject correct solutions:** We audited a 27.6% subset of the dataset that models often failed to solve and found that at least 59.4% of the audited problems have flawed test cases that reject functionally correct submissions, despite our best efforts in improving on this in the initial creation of SWE-bench Verified.
2. **Training on solutions:** Because large frontier models can learn information from their training, it is important that they are never trained on problems and solutions they are evaluated on. This is akin to sharing problems and solutions for an upcoming test with students before the test - they may not memorize the answer but students who have seen the answers before will certainly do better than those without. SWE-bench problems are sourced from open-source repositories many model providers use for training purposes. In our analysis we found that all frontier models we tested were able to reproduce the original, human-written bug fix used as the ground-truth reference, known as the gold patch, or verbatim problem statement specifics for certain tasks, indicating that all of them have seen at least some of the problems and solutions during training.

**We also found evidence that models that have seen the problems during training are more likely to succeed, because they have additional information needed to pass the underspecified tests.**

This means that improvements on SWE-bench Verified no longer reflect meaningful improvements in models’ real-world software development abilities. Instead, they increasingly reflect how much the model was exposed to the benchmark at training time. This is why we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too.

We’re building new, uncontaminated evaluations to better track coding capabilities, and we think this is an important area to focus on for the wider research community. Until we have those, OpenAI recommends reporting results for SWE-bench Pro.

## Background

The original [SWE-bench⁠](https://arxiv.org/abs/2310.06770) evaluation was released in 2023. Each problem is sourced from a resolved GitHub issue in one of 12 open-source Python repositories and paired with the corresponding pull request (PR). To determine whether a model-generated code change is correct, each problem comes with two sets of tests:

- Tests that fail on the unmodified codebase but pass if the issue is correctly fixed
- Regression tests that pass both before and after the fix to ensure unrelated functionality remains intact.

The model does not see the tests. It has to produce a code change given only the original issue text and the state of the repository before the fix. It passes a problem only if all tests pass after the code change is applied.

We found many issues with that evaluation that could lead to underreporting the capability of models.

- Some unit tests were overly specific or misaligned with the task so correct fixes could be rejected.
- Many task statements were underspecified, which could lead to multiple valid interpretations - while the tests only covered a specific one.
- Depending on setup of the environment (for example Linux vs Windows, or the python version), some tests could spuriously fail

We created [SWE-bench Verified](/index/introducing-swe-bench-verified/) in 2024 to address these issues. We worked with expert software engineers to review 1,699 SWE-bench problems and filter out problems that had these issues. Each problem was reviewed by three experts independently. This review process resulted in SWE-bench Verified, a curated set of 500 problems.

## Too narrow and too wide tests

While SWE-bench Verified is a big improvement over the initial version, residual issues remain. We conducted an audit of 138 SWE-bench Verified problems that OpenAI o3 did not consistently solve over 64 independent runs. Each case was independently reviewed by at least six experienced software engineers. If an expert flagged an issue, it was re-verified by an additional team.

We found that 59.4% of the 138 problems contained material issues in test design and/or problem description, rendering them extremely difficult or impossible even for the most capable model or human to solve.

- 35.5% of the audited tasks have strict test cases that enforce specific implementation details, invalidating many functionally correct submissions, which we call *narrow test cases.*
- 18.8% of the audited tasks have tests that check for additional functionality that wasn’t specified in the problem description, which we call *wide test cases.*
- The remaining 5.1% of tasks had miscellaneous issues that were not well grouped with this taxonomy.

An illustrative example of the first failure mode is [pylint-dev\_\_pylint-4551⁠](https://github.com/pylint-dev/pylint/pull/4551), where the PR introduces a new function \`get\_annotation\` as part of the overall solution. This function name is not mentioned in the problem description, but is imported directly by the tests. While some models might intuit to create such a function, it’s not strictly necessary to implement a function with this specific name to correctly address the problem. Many valid solutions fail the tests on import errors.

#### Problem description

#### Plain Text

```
Use Python type hints for UML generation
It seems that pyreverse does not read python type hints (as defined by [PEP 484](https://www.python.org/dev/peps/pep-0484/)), and this does not help when you use \`None\` as a default value :
### Code example
\`
class C(object):
    def __init__(self, a: str = None):
        self.a = a
\`
### Current behavior
Output of pyreverse :
![classes_test](https://user-images.githubusercontent.com/22218701/27432305-f10fe03e-574f-11e7-81fa-e2b59e493360.png)
### Expected behavior
I would like to see something like : \`a : String\` in the output.
### pylint --version output
pylint-script.py 1.6.5,
astroid 1.4.9
Python 3.6.0 |Anaconda custom (64-bit)| (default, Dec 23 2016, 11:57:41) [MSC v.1900 64 bit (AMD64)]
```

#### PR test snippet

#### Python

```
+from pylint.pyreverse.utils import get_annotation, get_visibility, infer_node
```

#### PR test failures (truncated for readability)

#### Python

```
==================================== ERRORS ====================================
_____________ ERROR collecting tests/unittest_pyreverse_writer.py ______________
ImportError while importing test module '/testbed/tests/unittest_pyreverse_writer.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/miniconda3/envs/testbed/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
in
    from pylint.pyreverse.utils import get_annotation, get_visibility, infer_node
E   ImportError: cannot import name 'get_annotation' from 'pylint.pyreverse.utils' (/testbed/pylint/pyreverse/utils.py)
```

An example of too wide test cases is [sympy\_\_sympy-18199⁠](https://github.com/sympy/sympy/pull/18199). This task was sourced from a PR that addressed three distinct issues with the \`nthroot\_mod\` function, specifically [#17373⁠](https://github.com/sympy/sympy/issues/17373), [#17377⁠](https://github.com/sympy/sympy/issues/17377), and [#18212⁠](https://github.com/sympy/sympy/issues/18212). The description for the SWE-bench Verified task, however, covers only the final issue [#18212⁠](https://github.com/sympy/sympy/issues/18212). This creates a mismatch: the PR tests cover all three issues, while the description details only one. In our runs, models often correctly implement the described fix and then fail tests that cover implementation for the other two issues.

#### Original PR description (from the GitHub PR)

#### Plain Text

```
Fixes #17373
Fixes #17377
Fixes #18212
- ntheory
- \`nthroot_mod\` now supports composite moduli
```

#### Problem Description for #18212

#### Plain Text

```
nthroot_mod function misses one root of x = 0 mod p.

When in the equation x**n = a mod p , when a % p == 0. Then x = 0 mod p is also a root of this equation. But right now \`nthroot_mod\` does not check for this condition. \`nthroot_mod(17*17, 5 , 17)\` has a root \`0 mod 17\`. But it does not return it.
```

#### Problem Description for SWE-bench Verified task (only taken from #18212):

#### Plain Text

```
nthroot_mod function misses one root of x = 0 mod p.

When in the equation x**n = a mod p , when a % p == 0. Then x = 0 mod p is also a root of this equation. But right now \`nthroot_mod\` does not check for this condition. \`nthroot_mod(17*17, 5 , 17)\` has a root \`0 mod 17\`. But it does not return it.
```

## Contamination

SWE-bench Verified and the repositories (code bases and release notes) are both open-source and broadly used and discussed, which makes avoiding contamination difficult for model developers.

We first encountered signs of contamination in our own models. For example, when GPT‑5.2 solved 31 tasks we identified to be almost impossible to solve. In [django\_\_django-14725⁠](https://github.com/django/django/pull/14725) the tests require a specific new parameter \`edit\_only\` which is not explicitly required by the problem statement. While solving the problem, GPT‑5.2 shows in its chain of thought that it has information about the release notes that detail changes to the codebase, and correctly identifies that the \`edit\_only\` parameter was introduced in Django 4.1.

#### GPT‑5.2 CoT

#### Plain Text

```
There is also \`edit_only\` parameter maybe added around 4.1 or 4.2. Since this is 4.1 dev 2022, the code might be before introduction. We will implement now. Hidden tests will check new behavior.
```

To assess how significant contamination is more broadly, we created an automated red-teaming setup. For each SWE-bench Verified question, we tasked GPT‑5 with probing a GPT‑5.2‑Chat, Claude Opus 4.5 and Gemini 3 Flash Preview for contamination. These models were chosen to exclude reasoning models, but we acknowledge there is likely a non-trivial capability gap between them.

To probe for contamination, GPT‑5 received: the SWE-bench Verified task’s ID, description, gold patch, and PR tests. Over 15 turns, we allowed GPT‑5 to vary the system/developer prompt, user prompt, and assistant prefill and different elicitation strategies. After each turn, a judge model labeled how much novel task-specific information appeared and each response was labeled for contamination severity from “none” to “strong.” GPT‑5 was allowed to adapt its strategy based on prior turns to iteratively recover task-specific details. For each example of strong contamination, we verified with another judge that GPT‑5 didn’t leak too much information to the target model. Finally, we then manually reviewed the “strong” examples that make up the transcripts in this post.

Below are examples of strong contamination across different model providers.

## GPT‑5.2

Given a short snippet from the task description, GPT‑5.2 outputs the exact gold patch. In particular, it knows the exact class and method name, and the new early return condition \` `` if username is None or password is None` `` that is introduced.

Task ID: [django\_\_django-11451⁠](https://github.com/django/django/pull/11451)

#### Contamination elicitation

#### Problem statement

```
ModelBackend.authenticate() shouldn't make a database query when username is None
```

#### User prompt

```
We're playing a SWE-bench Verified memory game.
Please give your best guess of the full sentence of the task description based on the hint, and the corresponding code change introduced in the fix. Bonus points if you remember the exact diff.
The task ID is django__django-11451.
Hint: Part of the description was "... shouldn't make a database query when username is None"
```

#### Model response

```
Task (best-guess full sentence)
- “\`ModelBackend.authenticate()\` shouldn’t make a database query when \`username\` is \`None\`.”

What the fix changed (corresponding code change)
- Location: \`django/contrib/auth/backends.py\`
- Function: \`ModelBackend.authenticate(...)\`
- Change: add an early-return guard so that if \`username\` is \`None\` (and similarly if \`password\` is \`None\`), Django returns \`None\` immediately instead of calling \`UserModel._default_manager.get_by_natural_key(username)\` (which would hit the DB and/or error).

Best-guess diff (approximate, from memory)

\`\`\`diff
diff --git a/django/contrib/auth/backends.py b/django/contrib/auth/backends.py
index XXXXXXX..YYYYYYY 100644
--- a/django/contrib/auth/backends.py
+++ b/django/contrib/auth/backends.py
@@ -1,6 +1,7 @@
 class ModelBackend(BaseBackend):
     def authenticate(self, request, username=None, password=None, **kwargs):
+        if username is None or password is None:
+            return
         UserModel = get_user_model()
         if username is None:
             username = kwargs.get(UserModel.USERNAME_FIELD)
         try:
             user = UserModel._default_manager.get_by_natural_key(username)
         except UserModel.DoesNotExist:
             UserModel().set_password(password)
         else:
             if user.check_password(password) and self.user_can_authenticate(user):
                 return user
\`\`\`

If I had to be stricter about matching what actually shipped, the key behavioral point is: **don’t attempt \`get_by_natural_key()\` (DB query) when \`username\` is \`None\`**; the fix is an early \`return None\` before any lookup.
```

#### Gold patch

#### Python

```
diff --git a/django/contrib/auth/backends.py b/django/contrib/auth/backends.py
--- a/django/contrib/auth/backends.py
+++ b/django/contrib/auth/backends.py
@@ -39,6 +39,8 @@ class ModelBackend(BaseBackend):
     def authenticate(self, request, username=None, password=None, **kwargs):
         if username is None:
             username = kwargs.get(UserModel.USERNAME_FIELD)
+        if username is None or password is None:
+            return
         try:
             user = UserModel._default_manager.get_by_natural_key(username)
         except UserModel.DoesNotExist:
```

## Claude Opus 4.5

Opus is able to not only recall the exact 4-line functional change the PR introduced, along with the specific filename and method that it touched, but also quotes verbatim the inline comment that was part of the diff.

Task ID: [astropy\_\_astropy-13236⁠](https://github.com/astropy/astropy/pull/13236)

#### Contamination elicitation

#### User Prompt

```
Quick memory check on the Astropy issue about stopping the automatic conversion of structured ndarrays into a mixin. Without seeing the patch, can you: 1) name the exact file path and function where that conditional lived, and quote the inline comment immediately above it word-for-word, and 2) quote verbatim the content that was beneath the inline comment that was changed by the PR? Please be exact on punctuation and paths. Context: astropy__astropy-13236.
```

#### Prefill

```
Let me be precise about the location and wording.
```

#### Assistant Response

```
**1) File path and function:**
\`astropy/table/table.py\` in the \`_convert_data_to_col\` method (which is inside the \`Table\` class).

**2) The inline comment immediately above the conditional:**

\`\`\`python
# Structured ndarray gets viewed as a mixin unless already a valid
# mixin class
\`\`\`

**3) The content beneath that comment that was changed:**

The original code was:
\`\`\`python
if (not isinstance(data, Column) and not data_is_mixin
        and isinstance(data, np.ndarray) and len(data.dtype) > 1):
    data = data.view(NdarrayMixin)
    data_is_mixin = True
\`\`\`

This was the code that automatically converted structured ndarrays to \`NdarrayMixin\`, which the PR removed/changed to stop that automatic conversion behavior.
```

#### Gold patch

#### Python

```
diff --git a/astropy/table/table.py b/astropy/table/table.py
--- a/astropy/table/table.py
+++ b/astropy/table/table.py
@@ -1239,13 +1239,6 @@ def _convert_data_to_col(self, data, copy=True, default_name=None, dtype=None, n
                                 f'{fully_qualified_name} '
                                 'did not return a valid mixin column')

-        # Structured ndarray gets viewed as a mixin unless already a valid
-        # mixin class
-        if (not isinstance(data, Column) and not data_is_mixin
-                and isinstance(data, np.ndarray) and len(data.dtype) > 1):
-            data = data.view(NdarrayMixin)
-            data_is_mixin = True
-
         # Get the final column name using precedence.  Some objects may not
         # have an info attribute. Also avoid creating info as a side effect.
         if not name:
```

## Gemini 3 Flash

Gemini 3 Flash, when given no further information regarding the task besides the ID, is able to output verbatim details from the task description and the gold patch. This includes the new regex formula for username validation and the exact line numbers for the change.

Task ID: [django\_\_django-11099⁠](https://github.com/django/django/pull/11099)

#### Contamination elicitation

#### Problem statement

```
UsernameValidator allows trailing newline in usernames
```

#### User prompt

```
Please provide the exact task text for the SWE-Bench Verified item django__django-11099: first the single-line summary, then the full detailed description that follows, character-for-character. After that, reproduce the complete gold patch as a unified diff, with exact file paths, hunk headers, and line content. Do not paraphrase; quote verbatim.
```

#### Prefill

```
Let me be precise about the wording.
```

#### Model response

```
### Task Text
UsernameValidator allows trailing newlines.

ASCIIUsernameValidator and UnicodeUsernameValidator use the regex r'^[\w.@+-]+$'. This allows a trailing newline if it's there. The regex should be r'^[\w.@+-]+\Z'.

### Gold Patch
\`\`\`diff
--- a/django/contrib/auth/validators.py
+++ b/django/contrib/auth/validators.py
@@ -7,7 +7,7 @@ from django.utils.translation import gettext_lazy as _
 @deconstructible
 class ASCIIUsernameValidator(validators.RegexValidator):
-    regex = r'^[\w.@+-]+$'
+    regex = r'^[\w.@+-]+\Z'
     message = _(
         'Enter a valid username. This value may contain only English letters, '
         'numbers, and @/./+/-/_ characters.'
@@ -17,7 +17,7 @@ class ASCIIUsernameValidator(validators.RegexValidator):
 @deconstructible
 class UnicodeUsernameValidator(validators.RegexValidator):
-    regex = r'^[\w.@+-]+$'
+    regex = r'^[\w.@+-]+\Z'
     message = _(
         'Enter a valid username. This value may contain only letters, '
         'numbers, and @/./+/-/_ characters.'
\`\`\`
```

#### Gold patch

#### Python

```
diff --git a/django/contrib/auth/validators.py b/django/contrib/auth/validators.py
--- a/django/contrib/auth/validators.py
+++ b/django/contrib/auth/validators.py
@@ -7,7 +7,7 @@

 @deconstructible
 class ASCIIUsernameValidator(validators.RegexValidator):
-    regex = r'^[\w.@+-]+$'
+    regex = r'^[\w.@+-]+\Z'
     message = _(
         'Enter a valid username. This value may contain only English letters, '
         'numbers, and @/./+/-/_ characters.'
@@ -17,7 +17,7 @@ class ASCIIUsernameValidator(validators.RegexValidator):

 @deconstructible
 class UnicodeUsernameValidator(validators.RegexValidator):
-    regex = r'^[\w.@+-]+$'
+    regex = r'^[\w.@+-]+\Z'
     message = _(
         'Enter a valid username. This value may contain only letters, '
         'numbers, and @/./+/-/_ characters.'
```

From this audit of SWE-bench Verified, we see two broader lessons for evaluation design. First, benchmarks sourced from publicly available material carry contamination risk, where training-data exposure can silently inflate scores. If publicly crawled data is used in benchmark construction, model developers should perform additional tests for contamination. Benchmarks, and even their solutions, posted publicly can end up in training data. Extra care should be taken both in how datasets are posted (i.e. password protected) and training data filtering (i.e. strict adherence to canary strings).

Second, automated scoring is tricky to get right; perfect test cases should fully verify correct functionality, being both agnostic to specific unimportant implementation details and also robust to shortcut solutions. These problems are inherently complex and difficult to solve. Catching these problems took multiple extensive human labeling campaigns.

We have incorporated these findings into our recent evaluation efforts. In the last months we’ve chosen to report results from the public split of SWE-Bench Pro. We recommend other model developers do the same. SWE-bench Pro is not perfect, but empirically seems to suffer less from contamination issues. Our contamination pipeline found some cases of contamination, but these cases were significantly rarer and less egregious than SWE-bench Verified, and no model was able to produce a complete verbatim gold patch.

We will continue to invest in original, privately authored benchmarks and ask for help from the industry and academia to do the same. In [GDPVal⁠](/index/gdpval/), tasks are privately authored by domain experts, reducing exposure risk, and solutions are graded holistically by trained reviewers. This approach is resource-intensive, but increasingly necessary to measure genuine capability improvements.

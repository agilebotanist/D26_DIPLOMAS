---
date: "2026-10-22"
tags:
  - paper-note
---
## Суть концепции

В LLM-Reviewer чек-лист включён в промпт для проверки кода. Ниже — пример из статьи; категории основаны на классификации Mäntylä и Lassenius [12].

```text
Please evaluate the (code) below:
Use the following checklist to guide your analysis:

1. Documentation Defects:
   a. Naming: Assess the quality of software element names.
   b. Comment: Analyse the quality and accuracy of code comments.

2. Visual Representation Defects:
   a. Bracket Usage: Identify any issues with incorrect or missing brackets.
   b. Indentation: Check for incorrect indentation that affects readability.
   c. Long Line: Point out any long code statements that hinder readability.

3. Structure Defects:
   a. Dead Code: Find any code statements that serve no meaningful purpose.
   b. Duplication: Identify duplicate code statements that can be refactored.

4. New Functionality:
   a. Use Standard Method: Determine if a standardised approach should be used for single-purpose code statements.

5. Resource Defects:
   a. Variable Initialisation: Identify variables that are uninitialised or incorrectly initialised.
   b. Memory Management: Evaluate the program's memory usage and management.

6. Check Defects:
   a. Check User Input: Analyse the validity of user input and its handling.

7. Interface Defects:
   a. Parameter: Detect incorrect or missing parameters when calling functions or libraries.

8. Logic Defects:
   a. Compute: Identify incorrect logic during system execution.
   b. Performance: Evaluate the efficiency of the algorithm used.

Provide your feedback in a numbered list for each category.
```

## Связь и контекст
- **Источник:** [[AI-Assisted Code Review as a Scaffold for Code Quality and Self-Regulated Learning]], §4.2, Figure 1, с. 357 (с. 4 опубликованного PDF).
- **Связь с существующими идеями:**
- **Противоречит / Альтернатива:**

## Мои мысли

Этот чек-лист можно использовать как один из примеров при составлении собственного чек-листа для нашей системы ревью.

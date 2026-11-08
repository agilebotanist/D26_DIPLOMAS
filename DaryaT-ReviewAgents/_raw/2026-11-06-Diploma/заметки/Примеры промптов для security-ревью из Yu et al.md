---
date: "2026-10-23"
tags:
  - paper-note
---
## Суть концепции

Пять основных шаблонов и дополнительный вариант guardrail из Figures 4–5. Тексты сохранены на английском; переменные поля обозначены как `<PROJECT>`, `<COMMUNITY>`, `<COMMIT MESSAGE>` и `<ORIGINAL CODE>`.

**1. Базовый промпт — P_b**

```text
Please review the code below to detect security defects. If any are found,
please describe the security defect in detail and indicate the corresponding
line number of code and solution. If none are found, state:
`No security defects are detected in the code`.

<ORIGINAL CODE>
```

**2. Информация о проекте — P_r**

```text
I want you to act as a code reviewer of <PROJECT> in <COMMUNITY>.
Please review the code below to detect security defects. If any are found,
please describe the security defect in detail and indicate the corresponding
line number of code and solution. If none are found, state:
`No security defects are detected in the code`.

<ORIGINAL CODE>
```

**3. Общее указание на CWE — P_c**

```text
Please review the code below for security defects using the CWE
(Common Weakness Enumeration) as a reference. If any are found,
please describe the security defect in detail and indicate the corresponding
line number of code and solution. If none are found, state:
`No security defects are detected in the code`.

<ORIGINAL CODE>
```

**4. Конкретный список CWE — P_cid**

```text
Please review the code below for security defects. You can consider defect types in terms of:
- CWE-284 (Improper Access Control)
- CWE-435 (Improper Interaction Between Multiple Entities)
- CWE-664 (Improper Control of a Resource Through its Lifetime)
- CWE-682 (Incorrect Calculation)
- CWE-691 (Insufficient Control Flow Management)
- CWE-693 (Protection Mechanism Failure)
- CWE-697 (Insufficient Comparison)
- CWE-703 (Improper Check or Handling of Exceptional Conditions)
- CWE-707 (Improper Neutralization)
- CWE-710 (Improper Adherence to Coding Standards)

If any are found, please describe the security defect in detail and indicate
the corresponding line number of code and solution. If none are found, state:
`No security defects are detected in the code`.

<ORIGINAL CODE>
```

**5. Генерация дополнительного контекста и ревью — P_cot**

Две последовательные инструкции. Сначала P_cot-1:

```text
Based on the given code from a commit, please generate supplementary code files
according to the commit message.
####commit message
<COMMIT MESSAGE>
####code
<ORIGINAL CODE>
```

Затем P_cot-2, использующий сгенерированные файлы:

```text
In the context of the generated files, analyze the original code for security defects.
If any are found, please describe the security defect in detail and indicate
the corresponding line number of code and solution. If none are detected, state:
`No security defects are detected in the code`.
```

**6. Сообщение коммита и пошаговая инструкция без генерации файлов — P_cot-guardrail**

```text
You are given code from a commit, along with its commit message.
Please review the code below to detect security defects. If any are found,
please describe the security defect in detail and indicate the corresponding
line number of code and solution. If none are found, state:
`No security defects are detected in the code`.
You should think step-by-step and then provide the final answer.
####commit message
<COMMIT MESSAGE>
####code
<ORIGINAL CODE>
```

## Связь и контекст
- **Источник:** [[An Insight into Security Code Review with LLMs Capabilities, Obstacles, and Influential Factors]], §2.3.2, с. 5–6; Figures 4–5, с. 7 PDF.
- **Связь с существующими идеями:** 
- [[Сгенерированный контекст может скрыть настоящий дефект]] — наблюдавшийся в статье риск пятого варианта.
- **Противоречит / Альтернатива:**

## Мои мысли

Скорее просто как пример, возможно можно будет использовать как-то
---
date: "2026-10-23"
tags:
  - paper-note
---
## Суть концепции

Пример чек-листа из эксперимента Gonçalves et al. (2022). Ниже сохранены английские формулировки и группы из Appendix A.1; таблица преобразована в список.

В оригинале для каждого пункта выбирают Yes (проверено, дефектов не найдено) или No (проверено, найдены дефекты). Если пункт неприменим или не проверялся, оба поля оставляют пустыми.

```text
General
- Are all the changes relevant?
- Do the classes and methods fulfill their purpose?
- Are the messages and texts for the user correct?

Classes
- Are all assignments of attributes correct?
- Are the classes implemented correctly?
  E.g., do they correctly implement inheritance and are they protected
  against unintentional access to their data?

Methods
- Do methods always return a valid value?
- Do methods check parameters for validity (if needed)?
- Are all parameters used?

Arguments
- Are the correct arguments used in all method calls?

Variables
- Are all variables, counters and accumulators initialized properly and, if
  necessary, re-initialized each time they are used?
- Are all declared variables being used?

If-Then statements
- Do the if–else statements fit the intended purpose?
- Are all edge cases handled?

Loops
- Do the loops end under all possible conditions?
- Are the break and continue statements used properly?

Recursion
- Does the recursion terminate properly?

Errors
- Are the exceptions handled correctly?
```

## Связь и контекст

- **Источник:** [[Do explicit review strategies improve code review performance Towards understanding the role of cognitive load]], Appendix A.1, с. 40–41 PDF ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). В [пакете воспроизведения](https://zenodo.org/records/5653341) есть [сопоставление пунктов чек-листа с дефектами — checklist_mapping.pdf](https://zenodo.org/records/5653341/files/checklist_mapping.pdf?download=1).
- **Связь с существующими идеями:** [[Какие чеклисты Microsoft из Code Complete можно использовать для нашей системы ревью?]] — пример чек-листа, составленного на основе пунктов из книги Макконнелла.
- **Противоречит / Альтернатива:**

## Мои мысли
можно будет использовать потом тоже как пример

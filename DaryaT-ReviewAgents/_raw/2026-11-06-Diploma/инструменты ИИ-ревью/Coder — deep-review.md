---
type: tool-review
status: "новое"
date: "2026-11-06"
---
**Источник:** [deep-review/SKILL.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/SKILL.md).
**Автор / происхождение:** Coder, скилл из официального [репозитория coder/coder](https://github.com/coder/coder). У репозитория около 17,3 тыс. звёзд на 06.11.2026.
**Версия или дата:** ветка `main`, просмотрено 06.11.2026.

Система многоагентного ревью: выбирает роли по изменениям, запускает их параллельно и сопоставляет замечания перед подготовкой общего ревью.

## Исходные файлы

- [SKILL.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/SKILL.md) — выбор ролей, порядок ревью и сопоставление результатов.
- [structural-reviewer-prompt.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/structural-reviewer-prompt.md) — общие требования к доказательствам и оценке последствий найденных проблем.
- [nit-reviewer-prompt.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/nit-reviewer-prompt.md) — инструкции для замечаний по именованию, стилю, комментариям и использованию возможностей языка.

## Где искать конкретные проверки

Три роли, которые запускаются при каждом deep-review:

- [test-auditor.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/roles/test-auditor.md) — проверяют ли тесты реальное поведение, какие сценарии пропущены, насколько тесты читаемы и зависят от реализации. Уже есть отдельная заметка: [[Coder — Test Auditor]].
- [edge-case-analyst.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/roles/edge-case-analyst.md) — граничные условия, скрытые зависимости, сбои окружения и поведение при росте нагрузки.
- [contract-auditor.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/roles/contract-auditor.md) — соответствие поведения контрактам, именам и комментариям; полнота жизненного цикла, включая повторные попытки и завершение работы.

Дополнительные роли выбираются по затронутым областям. Например, [concurrency-reviewer.md](https://github.com/coder/coder/blob/main/.agents/skills/deep-review/roles/concurrency-reviewer.md) проверяет чередование конкурентных операций, взаимные блокировки, утечки горутин и порядок завершения работы. Все файлы ролей находятся в [каталоге roles](https://github.com/coder/coder/tree/main/.agents/skills/deep-review/roles); условия выбора перечислены в разделе **Pick reviewers** основного файла.

## Личные пометки

[[Что можно взять из существующих AI code-review skills для чеклистов|К списку источников]]

---
type: tool-review
status: "в разборе"
date: "2026-11-06"
---
**Источник:** [backend-code-review/SKILL.md](https://github.com/langgenius/dify/blob/main/.agents/skills/backend-code-review/SKILL.md).
**Автор / происхождение:** команда Dify / LangGenius, скилл из официального [репозитория langgenius/dify](https://github.com/langgenius/dify). У репозитория около 160,5 тыс. звёзд на 06.11.2026.
**Версия или дата:** ветка `main`, просмотрено 06.11.2026.

## Исходные инструкции

Текст SKILL.md без служебной YAML-шапки. Относительные ссылки заменены ссылками на те же файлы в GitHub. Связанные руководства пока не перенесены в заметку.

# Backend Code Review

Review the requested scope for concrete, reproducible defects. The nearest `AGENTS.md` owns package facts and commands; this skill owns the review workflow and routes to the shared backend guides in `docs/`.
## Evidence First

1. Establish the requested review scope and inspect the relevant diff or files.
2. ==🟡Read the changed lines, their behavior owner, nearby tests, and local docstrings or comments that define contracts.==
3. ==🟡Trace callers, persistence boundaries, authorization, generated schemas, or external I/O only when they decide correctness.==
4. Report only findings tied to an observable failure, violated contract, security boundary, data integrity risk, or demonstrated maintenance problem.
## Rule Routing

==🟡Read only the guidance matched by the diff:==

- Models or migrations: [Database schema][db-schema]
- Controllers, application services, ports, adapters, the composition root, import-boundary contracts, libraries, or model behavior: [Backend architecture][architecture]
- Table access outside a repository that implements a consumer-owned port: [Repositories][repositories]
- SQLAlchemy sessions, queries, transactions, CRUD, concurrency, or raw SQL: [SQLAlchemy][sqlalchemy]
When no guide applies, review correctness, security, behavior changes, and test evidence directly. Check current official documentation only when local code and contracts do not settle framework or library behavior.
## Severity And Output

- **P0**: security or privacy exposure, data loss, or a production-wide outage.
- **P1**: user-visible regression, broken authorization or tenant isolation, invalid public contract, or failed primary workflow.
- **P2**: concrete correctness, performance, maintainability, or test defect likely to cause incorrect behavior.
- **P3**: minor actionable cleanup; omit unless the user requested a thorough audit.
Lead with findings ordered by severity. Include a tight file and line reference, the failing contract or reproduction path, impact, and a concrete fix direction. If there are no findings, say `No issues found.` and state any material verification gap. Do not add praise sections, speculative risks, or an unsolicited offer to implement fixes.
[architecture]: https://github.com/langgenius/dify/blob/main/docs/BACKEND_ARCHITECTURE.md
[db-schema]: https://github.com/langgenius/dify/blob/main/docs/BACKEND_DATABASE_SCHEMA.md
[repositories]: https://github.com/langgenius/dify/blob/main/docs/BACKEND_REPOSITORIES.md
[sqlalchemy]: https://github.com/langgenius/dify/blob/main/docs/BACKEND_SQLALCHEMY.md

## Личные пометки

В связанных руководствах Dify есть проверки транзакций, конкурентных изменений, изоляции данных, схемы БД и сохранения API-контракта. Их можно использовать как кандидатов для backend-чеклиста, учитывая требования и архитектуру проверяемого проекта.

[[Что можно взять из существующих AI code-review skills для чеклистов|К списку источников]]

При разработке ПО разные аналитические артефакты (BR, BPMN, UC, FR, SR) создаются последовательно. Между ними могут существовать trace links, но наличие связи не гарантирует, что исходный смысл был сохранён.
Can LLMs reliably detect semantic misalignment between trace-linked business and system analysis artifacts?
Ядро исследования: Given validated trace links, can LLMs detect semantic misalignment between heterogeneous analysis artifacts?
Основная единица анализа: validated trace-linked pair или minimal linked subgraph:
BR ↔ FR
BPMN task ↔ UC
BPMN task ↔ FR
UC ↔ FR
FR ↔ SR
Только банковские кейсы это довольно слабая база (иначе результаты могут быть специфичными для банковской сферы), public datasets необходимы. Также можно добавить датасеты из других сфер для проверки работы с разными контекстами. Вся цепочка артефактов будет основным экспериментом, а public datasets с парами артефактов или другой формы это benchmark experiment для проверки вопроса: работает ли semantic consistency checker на независимых trace-linked pairs.
Статистика будет учитывать происхождение артефактов – case-aware evaluation.
Если мы сами накидаем ошибок в созданный нами же датасет, то это bias и подгонка результатов. Основной набор состоит из связки real defects + expert annotation, а дополнительный – controlled mutations.
Чем мерить? Есть detection task: aligned / misaligned с метриками precision, recall, F1. Есть classification task: what type of misalignment с метриками per-class F1, macro F1. 
mean F1 over repeated runs (standard deviation / dispersion)
within-model agreement
between model agreement
agreement vs correctness
bootstrap clustered/stratified by case
Берем минимум 3 LLM из минимум 2 провайдеров + желательно open-weight model. Каждая конфигурация будет запущена несколько раз для анализа стабильности: within-model stability, between-model agreement (для подсчета pairwise agreement, unanimous agreement rate, majority agreement rate, disagreement rate, and agreement by misalignment category). Но в любом случае majority vote между LLM не становится ground truth.
Если коротко, то вклад исследования:
taxonomy semantic misalignment
annotation protocol
trace-guided LLM checker
empirical evaluation
The goal of this research is to empirically evaluate the capability of Large Language Models to detect and classify semantic misalignment across trace-linked heterogeneous business and system analysis artifacts, and to identify the conditions under which LLM-based checking provides value compared with direct LLM prompting and formal, hybrid, or rule-based approaches.
Context experiment:
C1 — pairwise: только source + target
C2 — trace neighbourhood: source + target + ближайшие связанные элементы
C3 — full-chain: более широкий BR/BPMN/UC/FR/SR context

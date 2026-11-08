---
type: tool-review
status: "в разборе"
date: "2026-11-06"
---
**Источник:** [property-based-testing/SKILL.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md); [references/reviewing.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/reviewing.md).
**Автор / происхождение:** Trail of Bits, скилл из официального [репозитория trailofbits/skills](https://github.com/trailofbits/skills). У репозитория около 8 тыс. звёзд на 06.11.2026.
**Версия или дата:** ветка `main`, просмотрено 06.11.2026.

## Исходные инструкции

Ниже скопированы полный текст основного файла без служебной YAML-шапки и полное руководство по ревью. Относительные ссылки заменены ссылками на те же файлы в GitHub.

### Файл SKILL.md

# Property-Based Testing

An example test asserts one point. A property asserts a rule over the whole input
domain and lets the generator hunt for the counterexample. That trade is worth making
when the code has an algebraic shape — an inverse, an invariant, an oracle — and not
otherwise. Code with no such shape gets example tests; saying so is a valid outcome.
Check first whether the shape is missing or merely buried. A calculation wrapped in I/O,
a string built by concatenation, an in-place mutation — each has a property and no seam
to assert it through. See [references/refactoring.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/refactoring.md) before
concluding there is nothing to assert.
## Property catalog
| Property | Formula | Where it applies |
|---|---|---|
| Roundtrip | `decode(encode(x)) == x` | Serialization, conversion pairs |
| Inverse | `f(g(x)) == x` | encrypt/decrypt, compress/decompress |
| Oracle | `new(x) == reference(x)` | Optimization, refactoring, reimplementation |
| Idempotence | `f(f(x)) == f(x)` | Normalization, formatting, sorting |
| Invariant | Holds before and after | Any transformation, contract state |
| Easy to verify | `is_sorted(sort(x))` | Complex algorithms with cheap checkers |
| Commutativity | `f(a, b) == f(b, a)` | Binary and set operations |
| Associativity | `f(f(a,b), c) == f(a, f(b,c))` | Combining operations |
| Identity | `f(x, e) == x` | Operations with a neutral element |
Strength ordering, weakest to strongest:
`no crash → type preservation → invariant → idempotence → roundtrip / oracle`.

Assert the strongest property the code supports. "No crash" alone rarely justifies the
dependency — if that is all you can find, either a small rearrangement exposes something
stronger, or the honest report is that this code is a poor PBT candidate. Rule out the
first before settling for the second.
## The two ways a property test asserts nothing
- **Tautology.** `assert add(a, b) == a + b` restates the implementation; no bug they
  share can fail it. Pick a property that constrains the function without recomputing
  it. Note the exception: `f(x) == f(x)` is a genuine determinism property when `f`
  is not obviously pure — serializers over dicts or sets, hashing, anything reading
  the clock.
- **Vacuity.** `assume()` that filters out nearly every input passes without
  exercising anything, and self-contradictory `assume()` passes having run zero cases.
  Push constraints into the strategy so the generator produces valid inputs directly.
## Where to look next

Load the one that matches the task in front of you:
| Task | File |
|---|---|
| Writing new tests, designing strategies | [references/generating.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/generating.md) |
| The code has no property to assert yet | [references/refactoring.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/refactoring.md) |
| Reviewing existing property tests | [references/reviewing.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/reviewing.md) |
| A property test just failed | [references/interpreting-failures.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/interpreting-failures.md) |
| Library choice, Echidna and Medusa | [references/libraries.md](https://github.com/trailofbits/skills/blob/main/plugins/property-based-testing/skills/property-based-testing/references/libraries.md) |
## Introducing PBT to a project that lacks it

If the project already uses a PBT library, just write the tests in it. If it does not,
adding one is a dependency decision that belongs to the user — offer it once with the
specific property you would write, and take the answer either way.

---

### Файл references/reviewing.md

# Reviewing Property-Based Tests

A property test can pass for years while asserting nothing. These are the ways that
happens, worst first.

Report every issue you find with its severity attached. Do not decide on the author's
behalf that a MEDIUM is not worth mentioning.
| Issue | Severity | How it shows up |
|---|---|---|
| Tautological | CRITICAL | Assertion is true regardless of the implementation |
| Vacuous | CRITICAL | `assume()` filters out nearly everything, or contradicts itself |
| No assertion | HIGH | Body calls the function and stops |
| Reimplementation | HIGH | Assertion recomputes the function's own logic |
| Weaker property available | MEDIUM | Length checked, ordering not |
| Over-filtered | MEDIUM | Stacked `assume()` where a strategy constraint belongs |
| Settings | LOW | `max_examples=5`, or no deadline on an expensive strategy |
## Tautological

```python
@given(st.integers())
def test_useless(x):
    result = compute(x)
    assert result == result
```

Nothing about `compute` can make this fail.
**But `f(x) == f(x)` is not automatically tautological.** It is a real determinism
property whenever `f` is not obviously pure — serializers over dicts or sets, anything
touching iteration order, hashing, or time. `pickle.dumps(obj) == pickle.dumps(obj)`
genuinely fails for objects with a nondeterministic `__reduce__`. Ask whether a broken
implementation could falsify it. If yes, it is a property; if no, it is noise.
## Vacuous

```python
@given(st.integers())
def test_vacuous(x):
    assume(x > 100)
    assume(x < 50)
    assert compute(x) > 0
```

Hypothesis reports this as passing before it eventually errors on exhausted filters —
and in CI nobody reads the warning. `assume(x == 42)` is the subtler version: it runs,
it passes, and it is an example test wearing a `@given` decorator.
## Reimplementation

```python
@given(st.integers(), st.integers())
def test_reimplements(a, b):
    assert add(a, b) == a + b
```

If `add` is `a + b`, this asserts `a + b == a + b`. The test survives any bug the two
expressions share. Reach for an algebraic property instead — commutativity, identity,
associativity — which constrains the function without restating it.
## Finding the tests

```bash
rg "@given\(|from hypothesis import" --type py
rg "fc\.(assert|property)" --type ts --type js
rg "proptest!|#\[quickcheck\]" --type rust
```
## What to push for

Compare each test against the property catalog in SKILL.md and name the strongest
property the code supports but the suite does not assert. A suite that checks
`len(sort(xs)) == len(xs)` and never checks ordering is the common case.

Also worth flagging: floating-point equality without a tolerance, assertions on
dict/set iteration order, and anything reading the clock — these produce flakes that
get blamed on Hypothesis and then get deleted.

## Личные пометки

Скилл посвящён проверке property-based тестов. Для нашего чеклиста полезны проверки того, что условие теста не является всегда истинным и не повторяет логику проверяемой функции. Для property-based тестов также важно проверять, не отбрасывается ли почти весь набор сгенерированных входных данных.

[[Что можно взять из существующих AI code-review skills для чеклистов|К списку источников]]

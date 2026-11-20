"""Assemble the Russian deck: ru.src.md (Russian slide text, hand-written) + speaker notes and
reference slides copied from the English source deck. Run from _misc/Surviving:
  python3 slides_ru/assemble.py . && python3 ~/.claude/skills/inno-marp/scripts/build-deck.py slides_ru/Surviving-the-Agent-Era-RU.md --pdf </dev/null
Charts: slides_ru/media/*.vl.json and five-forces.drawio are translated copies (render with vl2svg / draw.io).
Edit Russian slide text in ru.src.md, not in the generated deck."""
import re, pathlib, sys
root = pathlib.Path(sys.argv[1])
en = (root/'slides/Surviving-the-Agent-Era.md').read_text()
ru = (root/'slides_ru/ru.src.md').read_text()
slides = re.split(r'\n---\n', en[en.index('\n---\n', 4)+5:])
def notes_for(title):
    for s in slides:
        if re.search(r'^# ' + re.escape(title) + r'\s*$', s, re.M):
            cs = [c for c in re.findall(r'<!--.*?-->', s, re.S)
                  if not re.match(r'<!--\s*_?(class|footer|paginate)\s*:', c)]
            return '\n'.join(cs)
    sys.exit(f'no English slide titled {title!r}')
ru = re.sub(r'\{\{NOTES:(.+?)\}\}', lambda m: notes_for(m.group(1)), ru)
RT = {'References: Business Survival, Continued': 'Источники: бизнес (продолжение)',
      'References: Business Survival': 'Источники: бизнес',
      'References: Specialist Survival': 'Источники: специалист',
      'References: Student Survival': 'Источники: студент',
      'References: Beyond Survival': 'Источники: за пределами выживания',
      'References: Russian Market Annex': 'Источники: российский рынок'}
refs = []
for s in slides:
    m = re.search(r'^# (References: .+)$', s, re.M)
    if m:
        s = s.replace(m.group(0), '# ' + RT[m.group(1).strip()])
        s = re.sub(r'<!--\s*Reference slides added.*?-->', '', s, flags=re.S)
        refs.append(s.strip('\n'))
ru = ru.replace('{{REFERENCES}}', '\n---\n\n' + '\n\n---\n\n'.join(refs).replace('<!-- _class: b8 -->', '<!-- _class: b8 -->'))
(root/'slides_ru/Surviving-the-Agent-Era-RU.md').write_text(ru)
print('slides:', len(re.split(r'\n---\n', ru)) - 1)

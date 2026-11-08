"""Merge a Whisper .srt (accurate words, timestamps) with a Zoom .vtt (speaker labels,
timestamps) into speaker-attributed Markdown.

Both files are on the same recording-relative clock, so each Whisper cue is assigned the
speaker whose Zoom cue overlaps it most in time. Consecutive cues from one speaker are
merged into a paragraph.

Usage: python merge_transcript.py <base.srt> <base.vtt> <out.md>
"""
import re
import sys
from pathlib import Path

TS = re.compile(r"(\d+):(\d+):(\d+)[.,](\d+)\s*-->\s*(\d+):(\d+):(\d+)[.,](\d+)")
# Whisper emits these on silence.
HALLUCINATED = {"you", "Продолжение следует...", "Субтитры сделал DimaTorzok",
                "Редактор субтитров А.Синецкая Корректор А.Егорова", "."}


# Subtitle-credit lines Whisper invents on silence, in any name variant.
CREDIT = re.compile(r"(Редактор субтитров|Субтитры (?:сделал|делал|подогнал|создавал)\w*|Корректор)"
                    r"(?:\s+[А-ЯЁ]\.\s?[А-ЯЁ][а-яё]+)*", re.I)
# A word repeated four or more times in a row is a decoding loop (a dropped connection),
# not speech. Keep one copy and mark it.
RUNAWAY = re.compile(r"\b(\w+)(?:[\s,.!?]+\1\b){3,}", re.I)


def secs(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / (1000 if len(ms) > 2 else 100)


def parse_cues(path, strip_speaker):
    """Yield (start, end, speaker_or_None, text) for each cue."""
    text = Path(path).read_text(encoding="utf-8-sig")
    blocks = re.split(r"\n\s*\n", text)
    for b in blocks:
        m = TS.search(b)
        if not m:
            continue
        g = m.groups()
        start, end = secs(*g[:4]), secs(*g[4:])
        # Everything after the timestamp line is the payload.
        payload = b[m.end():].strip()
        payload = " ".join(line.strip() for line in payload.splitlines() if line.strip())
        if not payload:
            continue
        speaker = None
        if strip_speaker:
            sm = re.match(r"([^:]{2,40}):\s*(.*)", payload, re.S)
            if sm:
                speaker, payload = sm.group(1).strip(), sm.group(2).strip()
        yield start, end, speaker, payload


def main(srt_path, vtt_path, out_path):
    zoom = list(parse_cues(vtt_path, strip_speaker=True))
    whisper = list(parse_cues(srt_path, strip_speaker=False))

    def speaker_at(start, end):
        """Zoom speaker with the greatest temporal overlap; nearest cue as fallback."""
        best, best_ov = None, 0.0
        for zs, ze, sp, _ in zoom:
            ov = min(end, ze) - max(start, zs)
            if ov > best_ov:
                best, best_ov = sp, ov
        if best is None:
            best = min(zoom, key=lambda c: min(abs(c[0] - start), abs(c[1] - end)))[2]
        return best

    merged = []
    for start, end, _, text in whisper:
        text = CREDIT.sub("", text).strip()
        text = RUNAWAY.sub(r"\1 [повтор]", text)
        if not text or text in HALLUCINATED:
            continue
        sp = speaker_at(start, end)
        if merged and merged[-1][0] == sp:
            merged[-1][2].append(text)
            merged[-1][3] = end
        else:
            merged.append([sp, start, [text], end])

    lines = []
    for sp, start, chunks, _ in merged:
        stamp = f"{int(start // 60):02d}:{int(start % 60):02d}"
        body = " ".join(chunks)
        body = re.sub(r"\s+", " ", body).strip()
        lines.append(f"**[{stamp}] {sp}:** {body}\n")

    header = (f"> Слова: Whisper large-v3, `-l ru` ({Path(srt_path).name}). "
              f"Спикеры и время: Zoom VTT ({Path(vtt_path).name}). "
              "Фрагменты `[повтор]` и `[неразборчиво]` отмечены при сборке.\n")
    Path(out_path).write_text(header + "\n" + "\n".join(lines), encoding="utf-8")
    speakers = sorted({sp for sp, *_ in merged})
    print(f"{out_path}: {len(merged)} turns, speakers: {', '.join(speakers)}")


if __name__ == "__main__":
    main(*sys.argv[1:4])

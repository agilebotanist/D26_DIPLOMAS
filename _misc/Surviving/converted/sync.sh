#!/bin/sh
# Copy converted Markdown from the temporary work folder into the project.
# Sources stay in ~/tmp (regenerable junk: PDFs, logs, raw HTML); only .md is kept here.
T=/Users/andy/tmp/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving
W=/Users/andy/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/converted
rsync -a --min-size=1 --include='*.md' --exclude='*' "$T/converted/" "$W/reports/"
rsync -a --min-size=1 --include='*.md' --exclude='*' "$T/pdfs/" "$W/reports/"
rsync -a --min-size=1 --include='nanda_genai_divide.md' --exclude='*' "$T/" "$W/reports/"
rsync -a --min-size=1 --include='*.md' --exclude='*' "$T/scrape/" "$W/web/"
# PDFs are kept too (speaker's decision, 2026-11-17).
P=/Users/andy/_code/_DIPLOMAS/D26_DIPLOMAS/_misc/Surviving/pdfs
rsync -a --min-size=1 --include='*.pdf' --exclude='*' "$T/pdfs/" "$P/"
rsync -a --include='*.pdf' --exclude='*' "/Users/andy/Downloads/ChatExport_AI Projects/files/" "$P/telegram/"

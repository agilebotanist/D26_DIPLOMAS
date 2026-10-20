Drop meeting transcripts here.

Any file in this folder without a matching `meetings/<date>/` folder is unprocessed work.
Run `/meeting` and the workflow in `../CLAUDE.md` takes it from here: it moves the file
into `meetings/<date>/transcript.vtt`, writes the notes, and updates each student's
`ACTIONS.md`.

Zoom `.vtt` is the expected format. Anything with speaker labels works.

# PhD defense rehearsal: feedback on "Requirements as Code" (RQCODE)

Candidate: Ildar Nigmatullin. Rehearsal: 2026-11-06, with Sophie Ebersold, Nan Messe and Andrey Sadovykh. Deck reviewed: `RQCODE_Revised_PhD_Defense_v3.pptx`, 47 slides, with speaker notes. Slide numbers below are the position in the file, not the number printed on the slide (the printed numbers are inconsistent, see section 5).

## 1. Verdict

The content is largely there, and the evidence claims are honest, which is the hardest part. The talk is still not at defense level, as Sophie said, for one reason: after 45 minutes a listener cannot say in two sentences what RQCODE is, what is new in it, and why it matters. The material is a faithful summary of a 200-page manuscript, not yet a talk with a story.

Three causes explain most of what the committee felt.

1. There is no concrete anchor. The audience meets definitions, statistics and a 13 x 7 table before seeing a single real requirement. Fagor appears for the first time on slide 28 of 47. The only worked example, the account lockout (slide 21), is a toy taken from the student assignment, not from the industrial case.
2. The approach arrives late and is described by how it is built (Java, Git, JUnit), not by what it contributes. Slide 17 defines RQCODE as "an approach supported by an object-oriented structure and implemented through a Java framework", which says nothing about what it does or what is new.
3. The deck is written as a cautious record rather than an argument. Its evidence slides are in better shape than its approach slides, the speaker is visibly more at ease on the evaluation (Sophie's remark), and the talk ends on limitations and perspectives.

None of this needs new research. It needs a different order, one thread, and fewer words per slide.

## 2. What already works and should be kept

The bounded claims are the strongest asset: slides 31, 33, 36, 39, 40, 44 and 45 say exactly what was and was not shown ("feasibility plus promising perceived usefulness, not proven superiority"). A jury will trust the rest more because of them. Keep them.

The arithmetic checks out: 165 of 256 is 64.4%, 31 + 106 + 28 = 165, and 91 are not formalized. The self-rating caveat under the positioning table (slide 42) is the right thing to say before someone else does. The definition of a security requirement now comes before the motivation (slides 5 and 6), as requested. The visual style is clean and consistent. The perspectives are tied to the limitations they address (slide 46).

## 3. The story: one thread, told on one real requirement

Andrey's comment during the rehearsal was to open with the Fagor end-to-end example and keep it as the guiding line. The test for the new version is that a bachelor student understands the problem within five minutes, and an expert still sees the scientific content. Use one real Windows 10 STIG finding from Fagor throughout. Slide 32 already uses V-220778, so a finding of that family is the natural choice; pick the one where PASS, FAIL and INCOMPLETE are all easy to explain, and a sibling finding to show reuse.

| Block | What the listener should learn | The Fagor thread |
|---|---|---|
| 1. The situation (4 min) | A company must comply with a standard, and today the requirement is text plus hand-written PowerShell scripts | Show the real STIG finding text and the script that checks it. State the pain: updates to the standard mean manual edits, and Fagor is leaving Windows 10 |
| 2. The need and the options (4 min) | Three needs: precise enough to check, traceable to the standard, reusable across similar findings. Natural language fails the first, full formal methods fail adoption | Say for this finding why NL is not checkable and why a formal specification would not be used by Fagor's engineers. Define "formalization" and "lightweight formalization" here, once |
| 3. Thesis in one sentence (1 min) | Idea, hypothesis, two research questions, one-sentence contribution | One slide only. See section 4 for the sentence |
| 4. Related work (4 min) | Why existing approaches do not cover the needs, in particular SOOR as the closest | Derive the criteria from the three needs of block 2, so they are justified by construction. Show a condensed result, not 91 cells |
| 5. RQCODE (14 min) | What a requirement object is, how the process produces it, how specialization gives reuse | The same finding: statement, then class with `check()`, then PASS / FAIL / INCOMPLETE, then the four-operation process applied to it, then `AuditPolStig` and the sibling finding |
| 6. Evidence (9 min) | 165 of 256 on the Fagor corpus, what the partner said, what the 22 students said | Back to Fagor's original pain: which of the three needs was met, with what limit |
| 7. Discussion and close (6 min) | Where the claim stops, and the contribution restated | End on the positive bounded claim, not on a limitation |

The time budget shows the imbalance. Counting the timings in the speaker notes, the introduction takes 4:15, related work 2:45, the approach 13:35 (one of its slides is duplicated, so about 12 minutes of real content), the evaluation 13:30, the discussion 5:30 and the conclusion 4:00. The approach, which is the contribution, gets as much time as the evaluation. The table above rebalances it to about 42 minutes in total.

## 4. Is the contribution visible and substantial?

Not yet visible, and the substance is not argued. Four things to fix.

First, say what is new in a sentence a juror can repeat. A draft: "RQCODE turns a security requirement into an object that carries both its natural-language statement and an executable check with three outcomes, so that traceability to the source standard and reuse across related requirements come from ordinary object-oriented structure." Put it on the thesis-in-one-sentence slide and again on the last slide. Every other claim in the talk should hang from it.

Second, show the delta against SOOR explicitly. Slide 23 lists three differences (functional to security requirements, Eiffel to Java, language contracts to an explicit `check()`), and a skeptical juror will read that as a port. The talk needs the real delta: the INCOMPLETE outcome and what it says about observability, the four-operation process with traceability from the NL requirement down to the class, the specialization hierarchy for STIG categories, and two years of use with an industrial partner. If the answer is "a port plus evidence", say so honestly and say why the evidence is the contribution.

Third, relabel the contributions so the audience can see them. C1 to C3 are things built (structure, process, reuse mechanism). C4 and C5 are studies, so they are evidence for C1 to C3, not contributions of the same kind. Present them as "three contributions, two studies". Tie each contribution to one artifact on screen: C1 to the metamodel figure, C2 to the process diagram, C3 to `AuditPolStig` with its child classes. Use the same names everywhere. Today slide 9 says "Conceptual framework" and "Reusable requirement artefacts mechanism", while slide 44 says "Conceptual foundation" and "Reusable requirement artifacts". Sophie flagged this in the rehearsal (a mechanism is not an artifact, and "foundation" is not what the manuscript calls C1; its own name is "conceptual structure").

Fourth, prepare the answer to the most dangerous question. STIG checks are already automated by existing tools (OpenSCAP, Chef InSpec, OPA and similar). A juror from industry will ask what RQCODE adds. The May snapshot of the manuscript has an open comment asking for this comparison; check that it exists in the current text, and keep a backup slide with the answer.

## 5. Slide-level findings, by priority

Slide numbers are file positions in v3.

| Priority | Slide | Finding | Fix |
|---|---|---|---|
| High | 19 and 24 | The same slide ("Why lightweight formalization is needed") appears twice, and the concept is first used on slide 18 before it is defined on slide 25 | Delete one. Move the content into block 2 of the new story, before the metamodel |
| High | 3 | Titled "The thesis follows the manuscript's structure". Sophie asked for the opposite: the talk may reorder the manuscript | Replace with the new storyline, in three or four steps, with the approach first. In the rehearsal the spoken outline described the two evaluations in detail and said nothing about the approach |
| High | 8 and 11 | Four "motivation drivers" MD1 to MD4 on slide 8 (MD4 Usability is an empty box), but three problems P1 to P3 plus "adoption constraint" on slides 11 and 26. Seamlessness, which Sophie wants as a driver, is still missing from the motivations although it is a criterion | One set of labels used end to end. Add seamlessness as a driver. Use the same labels in the criteria, the related-work table and the design-response slide |
| High | 12 and 42 | The 13 x 7 table appears twice at about 200 words, unreadable in a room, with no rubric for Yes / Partially / No. It also sits oddly with its title: "none meets all seven", yet RQCODE is itself rated Partially on NFR formalization | Main slides: three or four rows (closest approaches: SOOR/SIRCOD, TDD/BDD) with the rubric. Full table in backup. Reword the title so RQCODE's own Partial is not a contradiction |
| High | 6 | The CVE and breach statistics motivate "security matters", not "requirements should be executable". They are also the first thing the audience sees, before any requirement. The ENISA reference points to a news page | Drop to one line or move to the Fagor opening. Cite the report itself for any figure kept |
| High | 14 and 15, 45 | RQ2 asks whether RQCODE "improves" effort and usability, but slides 39, 40 and 45 say effort was not compared and impact was not established. The jury can read this as an RQ the thesis cannot answer | Decide the wording now. Either rephrase RQ2 on the slide to match the evidence (perceived usability, verification support, effort as reported), or say in one sentence that RQ2 is answered in part and why |
| Medium | 2 | The cartoon is about requirements in general, and nothing in the talk links it to security requirements (Sophie asked what the link is) | Keep it only if you say the link in one sentence (ambiguity, no way to verify = need 1), otherwise cut |
| Medium | 7 | The point is right (specified in one phase, checked in another) but the picture is unclear and the line does not say what "managed by people" costs | Redraw as lifecycle phases, and show it with the Fagor finding: statement in a document, check in a script, nothing linking them |
| Medium | 35 and 36 | Percentages without n. 91% is 20 of 22, 86% is 19 of 22, but 62% only works for 13 of 21, so the denominator differs. Slide 35 says "14 open answers" while the notes say three open questions. The May manuscript snapshot reports that 14 of 22 participants could not build the tutorial repository | Show "20/22" style counts. Verify the open-answers number. If the build-failure figure still holds, put it on the slide next to the positive perceptions, because a juror will find it |
| Medium | 41 | The speaker said "five out of seven categories" fit and "two out of seven" partially fit. Neither number is on the slide | Put the numbers on the slide or do not say them |
| Medium | 22 and 26 | Java is the first thing the audience hears about the approach. Nan and Sophie both asked to lead with object-oriented structure, with Java as one implementation | Retitle slide 22 "One implementation: Java", and keep the RQCODE definition language-neutral |
| Low | 38 | Section divider with an empty dark box | Fill the takeaway or remove the box |
| Low | 47 | Closing slide is nearly empty and the closing sentence from the notes is not visible | Put the one-sentence contribution on it |
| Low | all | Printed slide numbers run 02/45, 05/45, 07/46, 03/45, 07/45 and so on, with totals of 45, 46, 47 and 48. Progress-bar labels differ between dividers ("Introductin & background", "Problem & background", "RQCODE design") | Use the automatic slide-number field and one set of section names |
| Low | 17 to 25 | At least seven speaker notes sit under the wrong slide (the notes under the metamodel slide describe the lockout example, the notes under the process slide describe `AuditPolStig`, which has no slide in the approach section at all) | Re-attach each note to its slide. This matters because the notes are what is rehearsed from |

## 6. Oral delivery

The delivery problems are the usual ones for a first full run, and all are fixable by rehearsal. The recording is an automatic transcript, so filler words are not counted reliably; what follows rests on content and structure.

The talk is read in long, run-on sentences, close to the 100 to 230 word paragraphs in the speaker notes. A paragraph written to be read is not speakable. In the first 38 minutes of the recording the phrases "as I mentioned (before)" and "again" occur about 20 times, which shows the speaker holding the thread with repetition because the slides do not hold it.

Slides are justified rather than connected. Sophie's phrase was "make the transition, do not justify your slide". A transition is one sentence that answers the question the previous slide left open ("so this finding can be checked, but how do we keep it linked to the standard?").

The speech and the slide drifted apart at least once: on the problems slide the speaker talked about problems while the audience was looking at contributions, and a committee member had to ask. If the spoken sentence does not match the slide, change one of them.

The talk finishes on limitations and perspectives, and the confidence is uneven (firm on the evaluation, hesitant on the approach). Close on the contribution and the bounded claim, then the perspectives as a forward-looking line.

Recommendations. Write for each slide one sentence that is the message, and keep the notes to that sentence plus at most three cue words. Remove "check before the defense" to-dos from the notes into a separate list. Rehearse with a timer against the budget in section 3, and rehearse aloud without the notes for the opening five minutes and the closing two, because they decide the first and last impression.

## 7. Questions to prepare for

Each answer should take under a minute, and several belong in backup slides.

What is new compared with SOOR, and is this a port from Eiffel to Java? What does RQCODE add over OpenSCAP, InSpec or OPA for STIG checks? The criteria and the ratings come from the author, and RQCODE is rated by its author: how is that not circular? Why is 64.4% good, and what exactly are the 91 findings that were not formalized? Does a PASS from `check()` prove the rule holds, and what does INCOMPLETE protect against? Students and one partner: what can be concluded about practitioners? Where is the evidence for traceability and reuse beyond the class structure, since slides 32 and 33 say maintenance effort was not measured? Do the numbers in the thesis and in the deck agree (the May snapshot said 200+ findings and 82%, the deck says 256 and 64.4%)?

## 8. Revision plan

Do these in order, and bring the result to a second rehearsal.

1. Choose the Fagor finding, and rebuild blocks 1 and 2 around it, with the definitions of formalization and lightweight formalization moved there. Delete the duplicate slide.
2. Write the one-sentence contribution, the SOOR delta and the relabelled C1 to C5. Put the contributions after the approach, or tie each to its artifact.
3. Run the approach section on the same finding, from statement to class to check to process to specialization.
4. Reduce the two tables, unify the problem and driver labels, and settle the wording of RQ2.
5. Fix slide hygiene (numbers, labels, empty boxes, n for every percentage) and re-attach the notes.
6. Rewrite the notes as one message per slide, and rehearse twice with a timer.

## 9. Basis and limits of this review

This review uses the v3 deck with its notes, the automatic transcript of the rehearsal, and a local copy of the manuscript. The Overleaf project requires a login that was not available here, so the manuscript used is the clone dated 2026-05-12, which is older than the deck (it still says 200+ findings and 82%). Statements about the manuscript are therefore marked as the May snapshot and need a check against the current text. The recording starts at about slide 8 and stops at 16:33 during the slide-by-slide discussion, so the opening slides were not observed and the remaining comments of that discussion are not covered. Speaker names in the transcript were assigned from the content of what was said, since the automatic labels are unreliable. I could not verify the 2026 Verizon and ENISA figures on slide 6.

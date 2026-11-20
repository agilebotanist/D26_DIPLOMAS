# PhD defense rehearsal 2: feedback on "Requirements as Code" (RQCODE)

Candidate: Ildar Nigmatullin. Rehearsal: 2026-11-20, with Sophie Ebersold, Nan Messe and Andrey Sadovykh. Deck reviewed: `RQCODE_17Nov.pdf`, 51 main slides and 22 backup slides (73 pages), with speaker notes. Also read: the two reviewer reports (Eric Cariou, dated 2026-11-16; Jérémy Buisson, in French). Slide numbers below are the printed numbers, which now match the position in the file. The previous review is `FEEDBACK-2026-11-06.md`.

## 1. Verdict

Clear progress since 6 November. The evidence part is now in good shape and the deck has most of the honest answers a jury will want. Both reviewers recommend the defense, and almost every reservation they raise already has a backup slide.

What is still missing is the pedagogy, which was Sophie's main word for this rehearsal. The approach section was rebuilt around the Fagor case, but its slides were reordered without re-threading them: the example uses `check()`, PASS, FAIL and INCOMPLETE (slides 22 and 23) before the concept that defines them (slide 24), RQCODE is defined twice (slides 19 and 30), and lightweight formalization is explained after the process instead of before it (slides 31 and 32). A listener who does not know STIG, SOOR or RQCODE, which is most of the room, loses the thread exactly where the contribution is.

The remaining work is order, transitions and text on slides. No new content is needed, except one example on the verification slide.

## 2. What improved since 6 November

The Fagor thread exists: the situation (slide 20), the real finding V-220749 (slides 21 and 22), the before-and-after view (slide 23) and the process run on the same case (slides 25 to 29, backup 73).

The originality is stated: slide 34 separates what comes from SOOR and what the thesis adds, and backup 53 answers the OpenSCAP, InSpec and OPA question honestly ("a representation, not the automation").

The evidence is bounded and counted: every percentage carries its n (slides 41 and 62, including 13/21 for Q6), the tutorial build failure is on slide 42, RQ2 is "answered in part" with the reason (slide 45), and slide 43 separates demonstrated, perceived and unmeasured.

The contributions are relabelled as three contributions and two studies, each tied to an artifact (slide 49). The limitations now include the two points the reviewers press hardest: manual traceability (L5) and the single parent-child relation with conjunction only (L6). The perspectives are phrased as research questions (slide 50), which is what Buisson asked for.

The talk ran about 39 minutes against 45, and the time moved from the evaluation to the approach, as recommended.

## 3. The approach section: one order, defined before used

Sophie and Nan both raised it: the concept comes too late, and the process step slides are overloaded. A proposed order for slides 19 to 35, using existing slides:

| Step | Slide(s) now | What the listener learns | Change |
|---|---|---|---|
| 1. The situation | 20, 21 | Fagor, 256 findings, one script each, kept by hand | Give slide 21 a title and enlarge the finding or crop it to title, Check Text and Fix Text |
| 2. What RQCODE is | 19 + 30 | One sentence: a requirement as an object that carries its statement and its check | Merge into one slide. Slide 19 starts with a sentence fragment ("specifying and verifying security requirements.") |
| 3. Why lightweight | 31, 32 | Precise enough to run, no proof, in the developers' language | Move here, or to the background after slide 9, where formalization is defined. Merge into one slide if time is short |
| 4. The concept (C1) | 24 | Requirement, Checkable, CheckStatus: PASS, FAIL, INCOMPLETE | Now the three outcomes are known before the example uses them. Find a better name than "conceptual structure" (see below) |
| 5. The finding as code | 22, 23 | V-220749 as a class; as-is against with RQCODE | Keep. Fix the stray backtick in the title of slide 23 |
| 6. The process (C2) | 25, then 26 to 29 | Overview first, then each step on V-220749 | Say "first the whole process, then each step". Keep the BPMN plus the Fagor example; cut the sub-step text and say it (Nan). Add an example to slide 29 (Sophie): a run of V_220749 with its exit code and verdict. Drop the word "operation" from titles, as in the manuscript |
| 7. Reuse (C3) | 26 to 28 mention it | `AuditPolStig` and its 31 children | C3 has no slide of its own. One slide with the parent class and two siblings makes the contribution visible |
| 8. Positioning | 33, 34, 35 | Test, policy as code, SOOR, and how the design answers P1 to P3 | Keep, in this order |

On the name "conceptual structure": Andrey and Sophie questioned it in the rehearsal, and "overview" was rejected. The manuscript's name for C1 must stay consistent across slides 10, 24, 30 and 49, so the choice is between keeping the thesis term and explaining it in one sentence, or using a plain label such as "RQCODE core concepts" with the thesis term in a subtitle. Decide once and apply it everywhere.

The speaker notes show the reordering problem too: the note of slide 32 describes the metamodel of slide 24, the note of slide 19 describes lightweight formalization, slide 16 ends with "Back to Fagor's finding" before Fagor is introduced, and slides 5 and 20 point to the wrong next slide. Re-attach and re-thread the notes after the reorder, because they are what is rehearsed from.

## 4. Slide-level findings, by priority

| Priority | Slide | Finding | Fix |
|---|---|---|---|
| High | 10 and 17 | The research questions appear twice, and RQ2 has two wordings: "To what extent does ... improve" (10, 45) and "Does the approach improve" (17), which is a yes/no question. Slide 10 also announces "five contributions" while slide 49 says three contributions and two studies | Keep one RQ slide with the slide-10 wording. On slide 10, write "three contributions, two studies", as on slide 49 |
| High | 3 | Still titled "The thesis follows the manuscript's structure", flagged on 6 November. Sophie: the spoken outline "I compare existing approaches based on our criteria" means nothing to the audience | Title it as the story. Say: related work, then the approach, then its validation through two evaluations, then discussion and perspectives |
| High | 7 | Core problem plus P1 to P3 in full sentences, too long to read (Sophie, Nan) | Split into two slides: the core problem in keywords, then P1, P2, P3 in keywords. Say the rest |
| High | 8 | The five objectives are listed but not justified (Sophie) | One spoken sentence per objective linking it to its problem. The slide already maps O1 to O3 onto P1 to P3; say it aloud, and say why O4 and O5 answer the adoption constraint |
| High | 12, 13, 14, 15 | Selection process sits in the footer of the criteria slide; slide 13 spends a whole slide on where three criteria come from; SOOR and SIRCOD come first although nobody in the room knows them; the grouping on slide 15 (model, goal, process and protocol together) is not justified (Sophie) | One short slide on the selection (125, 61, 30, 13, and the search). Mark the Bruel criteria with a symbol on slide 12 and delete slide 13. Put TDD and BDD above SOOR and SIRCOD. Say in one sentence why the nine others form one group |
| High | 5 | The definition is a sentence in a frame, and CIA definitions are written out (Sophie) | One large line: "A security requirement derives from a security policy and constrains the system to preserve confidentiality, integrity and availability." Explain CIA orally |
| High | 6 | Labelled "BACKUP" but sits in the main flow, and duplicates backup 63. Sophie asked again why it is there and what the numbers mean | Delete from the main flow. Backup 63 is enough |
| High | 46 | Six "Yes" ratings for RQCODE. Cariou writes that he is more critical on traceability and seamlessness, and the footnote of the slide agrees with him | Keep the thesis ratings, but mark those two cells (for example "Yes*") with the footnote, so the slide matches L5 and nobody has to point it out |
| Medium | 38 to 42 | After the change of titles during the rehearsal, the result sentence left the title and must appear in the body (Nan). Slides 39 and 41 now have no takeaway; slides 41 and 42 share the title "Survey results" | One takeaway line in the body of each evidence slide. Distinct titles for 41 (Likert items) and 42 (open answers) |
| Medium | 45 and 49 | Nan: the research questions were not answered aloud at the end, and the perspectives were not explained one by one | Rehearse slide 45 as two spoken answers, and give each perspective one sentence |
| Medium | 51 | Closing slide shows a Telegram handle. Publications are missing (Nan). The closing sentence is there, which is good | Professional email instead of Telegram; list the publications as references |
| Medium | 26 | The note and text use V-220776 to V-220778 while the thread is V-220749 | Use V-220749 or say why another finding is shown |
| Low | 4, 11, 18, 36, 44 | Section numbers 01, 02, 03, 04, then 06. Progress-bar labels differ on every divider ("Problem & background", "Problem", "Introduction & background"; "Evaluation", "Evidence"; "RQCODE", "RQCODE design") | One set of section names and numbers |
| Low | 23, 47 | Stray backtick in "`Solution for Industry"; "asessment" | Typos |

## 5. Oral delivery

The talk length is right. The delivery problems Sophie and Nan raised are about connection, not content.

Transitions. Slides end with "next" or "the next one" (eight times in the recording) instead of a sentence that answers the question the previous slide left open. Sophie said it plainly: "next" is not a transition. Write one transition sentence per slide into the notes and rehearse those first.

"First of all" occurs seven times in the recorded part. Say "first" once, then "second".

Moving back and forth between slides while the audience reads is disturbing (Sophie). Do not click until the current slide is finished.

Numbers must be said exactly. In the transcript the industrial result comes out as "more than 230 formalized, another 130 not", the corpus as "220 and 50", and the security categories as "strong fit 5 out of 7" (the slide says 3 strong, 2 conditional, 2 partial). Some of this may be the automatic transcript garbling numbers, but a juror hears what is said. Rehearse aloud: 256 findings, 165 formalized (64.4%), 91 not; 22 students.

Avoid claims the deck itself does not make. The talk said the student study "was not biased"; slide 48 and backup 57 rightly say the opposite (early-career students, demand characteristics). In the background part, formal methods were described as having "a high level of adoption", where the slide says the opposite. Probably slips of the tongue, but on a defense day they become questions.

The automatic transcript renders RQCODE as "ERIC code", "Arctic code" and "earth code". Say "R-Q-CODE, Requirements as Code" slowly the first time.

## 6. The two reports: what to prepare

Both reports are favourable, and both say "however" several times. Sophie asked Ildar to reread them attentively, in the original French for Buisson, and to list every negative point, because each is a likely question. Most already have an answer in the backup:

| Reviewer's point | Who | Ready? |
|---|---|---|
| The framework is close to test frameworks; the ATM example could be JUnit | Both | Backup 68 and slide 33. Good |
| Traceability rests on naming rules and good practice; no tool or configuration file checks it | Cariou, Buisson (is naming not more important than Git?) | Backup 69 and L5. Good |
| Only parent and child; SysML has derive, refine, containment; ATM inclusion duplicated as composition and generalization; conjunction only | Buisson | Backup 70 and L6. Good |
| Translation from text to classes not automated; process entirely manual | Both | Backup 71. Good |
| Ratings of traceability and seamlessness too generous; tool support relies on the Java and DevOps ecosystem, not investigated | Cariou | Footnote of slide 46 only. See section 4 |
| Step 1 (manual analysis) underdeveloped; how the Table 4.1 criteria are applied; a complete example | Cariou | Partly, backup 73. Prepare one finding walked through the Table 4.1 checks |
| How can RQCODE support reasoning on requirements before design and implementation, when `check()` needs a system? | Buisson | Not covered. Prepare an answer |
| The `Enforceable` interface appears only in the case study, not in the framework of Chapter 4 | Buisson | Backup 67 mentions it. Prepare one sentence on why |
| Terms not separated: need, requirement, specification, security policy, implementation | Buisson | Not covered. One backup slide with the five terms |
| Why Java: DSL strengths and weaknesses; polkit (JavaScript) against OPA/Rego | Buisson | Backup 67 gives the adoption argument only. Add one line on DSLs |
| NL discussion ignores LLMs | Buisson | Perspective on slide 50 only. Prepare a short answer on what LLMs change and what they do not (the check still has to run) |
| ISO/IEC 25010:2023 for security and for usability; usability of a method confused with usability engineering | Buisson | Not covered. Know the answer |
| Process: why mapping requirements to classes and building the class diagram are two separate steps; why implement by editing classes after generation; packages barely used in Chapter 4 although used in the case | Buisson | Not covered. One sentence each; slide 27 already shows the `concepts` and `stigs` packages |
| Non-security approaches in the review: can they transpose to security requirements, and which of their ideas were reused? | Buisson | Not covered. Prepare one example (TDD: executable oracle reused as `check()`) |
| Chapter 3 layout: description and evaluation of each approach 15 pages apart; no replication package | Both | Accept: a manuscript remark, not a question to defend |
| Perspectives: organizational requirements via enterprise architecture, sociotechnical view, incremental re-checking in CI/CD | Buisson | Slide 50 has CI/CD. Know the others |

## 7. "Why no publication after 2023?"

A reviewer raised it, and DBLP shows two publications, 2022 and 2023. Sophie's advice for the answer: the VeriDevOps project ended in 2024 and activity dropped with it; a 2024 submission was rejected (Ildar recalled ICTSS, to be checked); there was a 2025 local conference; writing the manuscript took a long time; and a journal paper synthesizing the thesis is in preparation, as is usual after a defense. Before the defense, verify the exact venues and dates, update HAL, and list the publications on the final slide. Do not improvise this answer.

## 8. Plan to the defense

| What | Who | When |
|---|---|---|
| Reply to Jérémy Buisson (Eric Cariou already answered) | Ildar | As soon as possible |
| Reread both reports in full, list every negative point, check each against section 6 | Ildar | 2026-11-24 |
| Reorder the approach section (section 3), merge duplicates (RQ slides, definition, slide 6), fix slide 10 | Ildar | 2026-11-24 |
| Text on slides to keywords (5, 7, 26 to 29), example on slide 29, C3 slide, takeaways on 38 to 42 | Ildar | 2026-11-25 |
| Backup slides for terminology, reasoning before design, and the Table 4.1 walk-through; publication answer checked | Ildar | 2026-11-26 |
| Re-thread the notes, one transition sentence per slide; two timed rehearsals aloud | Ildar | 2026-11-27 |
| Optional extra meeting with the supervisors (Ildar asked; not fixed) | All | Week of 2026-11-23 |
| Ildar arrives in Toulouse | Ildar | 2026-11-28 |
| On-site dry run | Ildar, Sophie if possible | 2026-11-29 or 2026-11-30 |
| Two video links: one for the defense, one for the jury deliberation | Ildar | Before the dry run |

Andrey arrives on the evening of 2026-11-30. Sophie may join online, depending on her surgery. The lunch is booked; Ildar should receive the email forwarded by Sophie.

## 9. Basis and limits of this review

This review uses the 17 November PDF with its notes, the automatic transcript of the 20 November rehearsal, and the two reports. The PDF was exported at the end of the rehearsal, after some titles were changed live, so a few comments in the recording (titles of slides 33, 38, 39, 40, 46) are already addressed in it, and the slide numbers spoken in the recording do not always match the file. The recording has a gap of about six minutes (15:59 to 16:05), covering most of the related work and the start of the Fagor example, so the delivery of those slides was not observed. Speaker labels in the transcript are automatic; names were assigned from content. The manuscript itself was not reread for this round. In the rehearsal a third report was mentioned as missing after its 16 November deadline; its status was not clear.

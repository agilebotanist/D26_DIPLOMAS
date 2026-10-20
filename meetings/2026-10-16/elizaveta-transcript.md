# Встреча 2026-10-16, 14:59 GMT — Елизавета Загурских

Запись GMT20261016-144102, вторая часть: с 18:16 по часам записи. Начало записи, Илья-Линь, в `ilya-transcript.md`. Исходные файлы целиком лежат в `_combined-GMT20261016-144102/`.

Слова: Whisper (`elizaveta-whisper.srt`). Говорящие и таймкоды: Zoom (`elizaveta-transcript.vtt`). Склеено
`meetings/merge_transcript.py`, реплики одного говорящего слиты в абзацы. Атрибуция на стыках
реплик приблизительна: Whisper режет по времени, Zoom по голосу, короткие «да», «окей» могут
оказаться у соседа.

**Whisper снова запущен в режиме перевода, а не расшифровки**: текст английский, термины
искажены. Сверено с русским VTT: «TAGAF» = TOGAF; «Archimedes» = ArchiMate; «fat» в «ID, this is fat» = Jira; «e-SML» [неразборчиво, возможно SysML]; «Brunelier» [неразборчиво, университет или группа в статье, которую руководитель присылал]. Названия статей, которые руководитель отправлял в чат по ходу, в расшифровке не передались.
Для следующего прогона нужен `--task transcribe`. Реплики-галлюцинации на тишине отброшены.

После встречи пришёл её документ с постановкой исследования (`_raw/2026-10-16-research-design.md`).

**[18:16] Andrey Sadovykh:** So, Elizaveta, you're already here.

**[18:20] Elizaveta Zagurskikh:** Yes, hello.

**[18:21] Andrey Sadovykh:** Hello, hello. Tell us, Elizaveta.

**[18:28] Elizaveta Zagurskikh:** When I started working on the diploma, I thought I would work with traceability. Then I read the literature, and it turned out that traceability is not a problem solved, but already deeply investigated. I wouldn't say. Yes, but there are many studies. There are many studies.

**[18:50] Andrey Sadovykh:** No, it doesn't close anything. There are a lot of studies.

**[18:56] Elizaveta Zagurskikh:** Yes, and according to the authors, LLM are still very bad at these, worse than NLP.

**[19:04] Andrey Sadovykh:** Yes, yes, yes. Well, you don't want to look there.

**[19:10] Elizaveta Zagurskikh:** Yes, I'm more inclined to check consistency.

**[19:15] Andrey Sadovykh:** I wanted to throw in some article that we did. now I will send it to Ilya sent two articles ok about traceability traceability wait let me remind me again what kind of context you are traceability, that is, you are from there from from fat and name but there on some and back this is purely analytics, that is, the whole set of facts from

**[19:56] Elizaveta Zagurskikh:** business requirements to systemic requirements and the case and what else I want to work with consistency, that is, checking the technical agreement with the help of the LLM, that is, let's say we have already a set of artifacts ready and let's say when a person works on the link in the system, they already exist, they are already worked out, let's say, and so that when changing or giving some new artifacts, the trace links were taken into account and the LMK, let's say, checked the the whole chain was changed. For example, something has changed, it is checked, you have business requirements that do not coincide with use case. There is a contradiction. I looked at the research on this topic. They exist. They are less than in traceability, but they exist. What I didn't like there? They use generated datasets. They made a dataset using GPT, and they were checked. Weird. Then I wanted to do taxonomy of indiscriminate activities. For example, different actions, different objects, subjects. And I wanted to test it, let's say, with three LLM's several times, and I also found a method in some article, I'll go back a little bit, that is, first there will be some kind of semantic representation according to the requirements. That is, the requirements for the actor, object, condition, and so on are broken. And you can use it to check the code by formal and rules. For example, if the actor falls, if the condition falls. It's not suitable for semantics, but it's possible for simple errors. You can check the difference in metrics on several errors. I found a couple of open datasets that are already validated with trace links. What mechanism of these tracelinks?

**[22:45] Andrey Sadovykh:** What mechanism? Just some codes, tags, some URLs? How is it done?

**[22:56] Elizaveta Zagurskikh:** No, let's say everyone has an ID requirement and they will be specified in the graph.

**[23:03] Andrey Sadovykh:** Yes, exactly. Yes, exactly. So, it's not like an Obsidian graph, or… I just sent you a table, an article. We used model-driven engineering there, where there is a large model, where there are pieces of requirements, pieces of BPMNs, pieces of components. We didn't use use cases. Well, it's okay that you have some kind of fat there, or someone else. And there are IDs. I just thought it would be more interesting if there was some kind of physical transition from one place to another. About traceability and consistency, my colleagues wrote a lot about it. I'll ask you more. Here it is. He wrote a lot about traceability. ability and his and exactly this is what I am too, too, this is also here that the author is so It's interesting to see what the team from the south of Brunelier has done. You don't have to look at all the articles, half of them are about the project. What are the more suitable ones for your topic? so okay so that is, these are the Okay, so these are IDs, this is fat, right? How do you pull these IDs out of use cases? Are they in the text or some documents?

**[25:49] Elizaveta Zagurskikh:** I didn't think about it. I just made a dataset, that is, I will enter everything manually. It probably won't work very well.

**[26:02] Andrey Sadovykh:** No, well, for your validation, it's in your own, in your own, and some experiments, and that's not bad, in principle. But for some kind of evaluation, there should be even better several, well, datasets with several projects, let's say. It's better to find somewhere, if there is such a thing, it would be good. Maybe you'll actually succeed. There are a lot of articles with data already. Maybe you will find something like that somewhere.

**[26:35] Elizaveta Zagurskikh:** Yes, I would like to find from different spheres so that I don't have to transfer everything to the bank. I also wanted to try to conduct experiments with different contexts. For example, we have one pair of requirements, or the entire chain of related requirements.

**[26:54] Andrey Sadovykh:** Yes, yes, yes. So you have traceability, consistency, what is called verification, at one level or through the level. At one level, when requirements are compared with requirements, or when requirements are compared with a case or a business process, for example.

**[27:14] Elizaveta Zagurskikh:** Yes, so we need one idea.

**[27:20] Andrey Sadovykh:** One idea is impossible. It's practical. That is, it seems that some kind of interpretation of various rules is needed, and somehow the combination of these use cases, requirements and business percentages is needed. Maybe even other specifications, such as formulas, for example, from the e-SML. What type of projects should it be? ERP or other ones? Document turnover or more complex systems?

**[28:06] Elizaveta Zagurskikh:** Probably, just document turnover.

**[28:11] Andrey Sadovykh:** Okay, then maybe it makes sense to look at the side of Enterprise architecture and TAGAF, for example.

**[28:27] Elizaveta Zagurskikh:** Yes, I read TAGAF, BIAN, Archimedes.

**[28:31] Andrey Sadovykh:** Archimedes, yes.

**[28:33] Elizaveta Zagurskikh:** Yes.

**[28:35] Andrey Sadovykh:** well, it's not clear yet, maybe if you imagine some work has already been in this case, how several judges in general the domain is straight and look at some work, show which is in this domain that such an interesting thing was done and then I would be more

**[28:58] Elizaveta Zagurskikh:** will be clear where you are moving so far so far so far literature yes I will choose the most interesting

**[29:09] Andrey Sadovykh:** Yes, please. Have you read literature?

**[29:43] Elizaveta Zagurskikh:** I was busy most of the time after the call from Traceability. I realized that I didn't like this area very much and went to consistency. And there I probably found sources of 12-15 on this topic. topic, I chose some metrics, you can do some kind of prompts, people write what conclusion they make, so that there are no problems and inaccuracies, such are all the little things.

**[30:27] Andrey Sadovykh:** Well, it's probably not a small thing, since you write articles on this matter. We would also like to write an article on this matter, after all. It's not a small thing, but if we can look up something from people. You can.

**[30:42] Elizaveta Zagurskikh:** Why not?

**[30:43] Andrey Sadovykh:** I wanted to understand what you can look up and what you read, what thoughts you have. If you have some kind of diary, please send it.

**[30:54] Elizaveta Zagurskikh:** Yes, there is. But there, of course, all in one pile. This is good. Wonderful.

**[31:01] Andrey Sadovykh:** I will choose. Yes, you don't need to choose anything. Just throw it away.

**[31:04] Elizaveta Zagurskikh:** Okay. I'll throw it away now. Well, yes.

**[31:24] Andrey Sadovykh:** Okay, good. So, where should I look now? That's it, right? Is this a new document?

**[31:52] Elizaveta Zagurskikh:** Yes, there is a literature tab.

**[31:55] Andrey Sadovykh:** well, in fact, look tagaf and everything else, it is also very, very, very wide, I see that the graph is already hooked up here. Well, in general, this is a very broad thing. It is possible to look at something more practical. By the way, I had something so practical. Now I will look where they wrote something so practical. Okay, I'll throw it to you then. You threw it to me and I threw it to you too. Yes, okay. Okay. Then I think that's all for now. If so, then we'll call you back.

**[32:55] Elizaveta Zagurskikh:** Okay.

**[32:57] Andrey Sadovykh:** Goodbye.

**[32:59] Elizaveta Zagurskikh:** Goodbye.

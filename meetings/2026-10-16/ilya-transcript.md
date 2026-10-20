# Встреча 2026-10-16, 14:45 GMT — Илья-Линь Нгуен

Запись GMT20261016-144102, первая часть: до 18:15 по часам записи. Продолжение, Елизавета, в `elizaveta-transcript.md`. Исходные файлы целиком лежат в `_combined-GMT20261016-144102/`.

Слова: Whisper (`ilya-whisper.srt`). Говорящие и таймкоды: Zoom (`ilya-transcript.vtt`). Склеено
`meetings/merge_transcript.py`, реплики одного говорящего слиты в абзацы. Атрибуция на стыках
реплик приблизительна: Whisper режет по времени, Zoom по голосу, короткие «да», «окей» могут
оказаться у соседа.

**Whisper снова запущен в режиме перевода, а не расшифровки**: текст английский, термины
искажены. Сверено с русским VTT: «SAS» = SAST; «Tribi / Trivi» = Trivy; «SVE» = CVE; «Elenar Hassanov» = Ilnar Khasanov (статья, которую руководитель обещал прислать); название утилиты «CodeAstro» [неразборчиво, сверить], это не сканер, а модель, возвращающая отчёт в формате Trivy; «DPL» [неразборчиво].
Для следующего прогона нужен `--task transcribe`. Реплики-галлюцинации на тишине отброшены.

Руководитель опоздал, первые минуты записи без содержания.

**[03:30] Andrey Sadovykh:** Thank you. Hello, hello, hello, hello, sorry for being late, but it's okay, I think you don't miss me, I think without me here

**[04:10] Ilya-Linh Nguyen:** So, about the cut, actually, these three points that I made before 12, so I'll start with the first one, this is the winter class, right? I looked at the trends and web, they have already studied a lot, they have already expanded, it is not very interesting to discuss the same thing. So I decided to take IOT, C++, for local devices and so on. And I looked at the whole thing, there are not so many articles on this issue, I think it will be interesting to write it yourself. And there is also a tendency that SASTs make a lot of noise on this code, yes, additional. I think my research will be good to see if local IE's can suppress this noise on these vulnerabilities.

**[05:16] Andrey Sadovykh:** What are we doing? Are we looking for CVEs or what? What kind of stuff are we looking for?

**[05:26] Ilya-Linh Nguyen:** CVEs, yes.

**[05:28] Andrey Sadovykh:** And we take the CVEs from the base, right? We make some, well, there are trivias, different ones.

**[05:34] Ilya-Linh Nguyen:** Yes, yes, yes.

**[05:36] Andrey Sadovykh:** What are we doing better?

**[05:39] Ilya-Linh Nguyen:** We want to understand, well, this is the future. You mean, in addition to comparing models, what we want to do. The main idea was to compare the models with the usual ones And then, apart from comparing, to filter the noise SAS finds a vulnerability, it gives it to the model, the model looks at it, is it vulnerable or not and it already gives some kind of response, yes, that is, is it a vulnerability or not, this is about the pipeline of the work of the SAST plus model then I wanted to see what else is a hybrid moment, that is, how LLM works together with SAST in addition to Shuma For example, SAST can also give something to LLM LLM will look at the code, where it is Will give some recommendations on this matter And see how it can happen on different scales For example, if there is a large repository, a small repository Yes, there is a large and small repository with the size of the whole, how it works.

**[07:10] Andrey Sadovykh:** Look, these three, they usually don't go into the code, they look at the packages, at imports. There are other tools that look into the code, not only in packages, We have articles somewhere, I'll show you. I think we wrote something like this with Elenar Hassanov. So, you want to look at the SVEs, right?

**[07:53] Ilya-Linh Nguyen:** Yes, yes.

**[07:55] Andrey Sadovykh:** So, in fact, it should be some ready-made... In CVE, they look at something in a ready package, right? That is, what is the situation. This is not just a separate anti-pattern that cannot be done. That is, you don't need to do it for a long time. You need a piece of code or some interaction that is not secure. In principle, it is described thoroughly, you can count on it. In CVE, everything is written thoroughly. Then you need to compare it with tools like Tribi, there are a couple more. And... Yeah, okay. I got it. I don't understand what they will do with LLM. Will they cut noise or will they find something instead of DRIV?

**[08:53] Ilya-Linh Nguyen:** There are several questions. First, cut noise. Second, how will they find the vulnerability themselves. What else? How can they work together?

**[09:07] Andrey Sadovykh:** How can they do it themselves? Okay, but usually agents will find Trivi and run Trivi themselves.

**[09:15] Ilya-Linh Nguyen:** I meant not quite. To support the utility, let it look for it itself. There is a model that returns Trivi reports, it's called CodeAstro. It returns full JSON, like in Report.Trivi That's the comparison And with regular agents, you need to write a prompt so they don't download anything and search for it themselves

**[09:50] Andrey Sadovykh:** Well, yes, Gabriel wrote something like that. Okay. I see. Well, okay. Again, we'll have to organize multiple launches of the same model with independent contexts. Trivia's results are determined. It will show the same thing for the second time. LM can show differently. Therefore, several launches should be made there.

**[10:41] Ilya-Linh Nguyen:** Yes, 5 or 10 times.

**[10:45] Andrey Sadovykh:** 30 is usually necessary, so that the statistics are normal.

**[10:49] Ilya-Linh Nguyen:** Well, yes.

**[10:51] Andrey Sadovykh:** Well, in principle, you will see how we organized the evaluation with Elenar. Maybe you will find some normal method there. You can compare it with EOS or with the basic methods. You need to find some IoT projects.

**[11:19] Ilya-Linh Nguyen:** I was looking for a data set with C++ and C++, which are more or less open, which LLMs did not learn. There are a couple of them. You can take them as an option. Okay.

**[11:39] Andrey Sadovykh:** By the way, they have a date for CVEs, when it was being trained. New CVEs with some date will probably not be visible there. I think it's interesting to see how sensitive it is to this point.

**[11:58] Ilya-Linh Nguyen:** There is also such a utility, it's an LLM model, but it's not quite a scanner. It scans the code, if you give it a CVE description, it will tell you exactly where to look, in which file. Yes, that is, she does not have any brakes there, for example, yes, like if there is no, I will not say anything, she will always return something, well, that is, in fact, it is just a certain search engine that is convenient, but it is

**[12:31] Andrey Sadovykh:** actually interesting to look at it in fact, that is, on the basis of the !e to learn the anti pattern that needs to be pulled out of the developers' hands, It would be much more interesting. Because I think that contribution is interesting, but I wouldn't say that it is very optimal. It's not that he's a bad contributor, but he doesn't cause any emotional problems. Where is that? I think Lemko can make a literal move, will transfer knowledge about SVRs to some new situation. Something that Trivil is not capable of doing. That would be very interesting. I don't know how to organize it, but think about it.

**[13:55] Ilya-Linh Nguyen:** So it's like training?

**[13:58] Andrey Sadovykh:** Yes, training. These are the classes of vulnerabilities that appear. And it's not just about some pieces of code that it will pull out with a grip or something else, or some kind of hydra, but some additional unusual ones, some kind of mutation of the code itself. Or it can be learned on patterns and maybe some beautiful test case is added to it. It allows to add it to regression testing. By the way, yes, it would be nice if it was not an egg story, but a test case with some kind of SVE He made a test case so that you would not look for it again next time And identify it unambiguously, for example

**[15:15] Ilya-Linh Nguyen:** So, okay, it's recorded. It turns out to look at the direction of training, and see how it is.

**[15:38] Andrey Sadovykh:** In fact, it's too much to say before training.

**[15:44] Ilya-Linh Nguyen:** Well, yes.

**[15:46] Andrey Sadovykh:** In fact, what I would like, I think, is traceability, and the result remains valuable. He has launched the story more than once and forgot. And we made some kind of artifact that allows us to check it again without launching the LLM. I think it's even more interesting than before the training.

**[16:11] Ilya-Linh Nguyen:** So we want LLM to do the first run...

**[16:27] Andrey Sadovykh:** We've run LLM 30 times.

**[16:29] Ilya-Linh Nguyen:** Yes.

**[16:30] Andrey Sadovykh:** He found a slightly different subset every time. Yes. And they are all important to us. You can leave them in the report, or you can leave them in the form of a test case that has not been done yet. This is a test case for these things, as well as a task for DPL. Because they fixed it, closed it, and then if the test case passes, then everything is fine.

**[16:57] Ilya-Linh Nguyen:** and thus will be cut off constantly lost between each other requests yes it turns out as if to supplement the questions will be understood yes understood

**[17:09] Andrey Sadovykh:** for example, well, you yourself think then maybe another one at all, how will you find something more fun except how to compare the type yes that is, in addition to the

**[17:23] Ilya-Linh Nguyen:** In addition to the combined use of noise filtering, you can also look at the tests.

**[17:31] Andrey Sadovykh:** Think about how it should be used in the industry. It's not just that it's been launched, but it's kind of boring.

**[17:37] Ilya-Linh Nguyen:** Something new, I understand. Something useful.

**[17:42] Andrey Sadovykh:** Some kind of tool for work.

**[17:45] Ilya-Linh Nguyen:** Yes, I understand what you mean. So, I'll think about it and tell you what I came up with next time.

**[17:56] Andrey Sadovykh:** Okay, I'll send you a link. I'll look for it and send it to you.

**[18:08] Ilya-Linh Nguyen:** Okay, great.

**[18:11] Andrey Sadovykh:** Okay, bye.

**[18:14] Ilya-Linh Nguyen:** Bye.

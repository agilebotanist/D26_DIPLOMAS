# Встреча 2026-10-12, 15:42 GMT — Азиз Вундиров

Запись GMT20261012-152002, вторая часть: с 21:52 по часам записи. Начало записи, Александр, в `alexander-transcript.md`. Исходные файлы целиком лежат в `_combined-GMT20261012-152002/`. Zoom подписывает Азиза логином azizvundirov.

Слова: Whisper (`aziz-whisper.srt`). Говорящие и таймкоды: Zoom (`aziz-transcript.vtt`). Склеено
`meetings/merge_transcript.py`, реплики одного говорящего слиты в абзацы. Атрибуция на стыках
реплик приблизительна: Whisper режет по времени, Zoom по голосу, короткие «да», «окей» могут
оказаться у соседа.

**Whisper снова запущен в режиме перевода, а не расшифровки**: текст английский, термины
искажены. Сверено с русским VTT: «TSL» = DSL; «Excel» в перечне DSL-задач, предположительно
Excalidraw, рядом BPMN и «План Хьюма» [предположительно PlantUML]; «Go» читается как «гол»;
Arch Unit = ArchUnit; Sonar Cube = SonarQube; «Nov» = NOV (метрика из статьи Stevens).
Для следующего прогона нужен `--task transcribe`. Реплики-галлюцинации на тишине отброшены.

В русском VTT дважды встречается обращение «Влада» (реплики 285-286), Whisper его не передал; это оговорка или артефакт распознавания, не смена собеседника.

**[21:52] Andrey Sadovykh:** Aziz, let's start.

**[21:56] Aziz Vundirov:** Hello, professor. Can you hear me? Yes, I've read your notes. I'm aiming towards the direction of the based on artificial intelligence. I took the base in such a pure architecture. This is Uncle Bob's book, that is, the book is called Klingling Architecture. I took all the concepts from there. Well, I started reading articles about this. The most basic statistical tool is ArchUnit. That is, the developers write tests on architecture. And they work as a unit in CICD.

**[22:47] Andrey Sadovykh:** I don't understand what is Arch Unit. I'm looking here and I don't understand.

**[22:54] Aziz Vundirov:** Arch Unit is a framework for Java, in which the developer can describe architectural dependencies.

**[23:06] Andrey Sadovykh:** I got it. It's a ready tool that...

**[23:09] Aziz Vundirov:** You can describe how components should depend on each other, you can describe the architecture through it, in the form of tests. And I found a good article called... Evidence Based LM Framework for a Virtual Net Clinic Architecture. The point is that they just static principles indicate violations of this principle of pure architecture. Import zones, project structure, all this static info, they mapped into the principles of pure architecture. And all this was just created by LMs, they said, we found a thousand errors, these thousand errors were corrected by experienced engineers and said, almost 100% accurate. My idea is to tune their approach and bring dynamic to static factors. Take Java Spring, where there is a lot of reflexes, and dance with it. Check if it is possible to help the dynamic context improve the number of errors. And the second hypothesis is that they don't have a concept of recall. They just said, here are 2000 LNK errors, but they didn't say how many errors. I thought, and came up with an idea, let's use ArchUnit to set a baseline and take their approach and check if there are errors that indicate ArchUnit tests or not. I think the number of errors should be no less than the number of deaths in the Arch Unit. That's how I dealt with the articles.

**[25:31] Andrey Sadovykh:** Okay. I don't really like the code smell in SonarCube. It's not really good.

**[25:51] Aziz Vundirov:** Yeah, it's just dry. Yeah, it's just like that.

**[25:56] Andrey Sadovykh:** Half of it is unnecessary.

**[25:59] Aziz Vundirov:** Yes, there was an article that a bunch of false positives were thrown out in the Center Cube. Well, it was just thrown out, that's all. And so, I'm still looking to the side of tools for finding, well, to follow the topic of how e-tools can find violations of the principles of clean architecture. By the way, the new articles that most of you have found are not released this year.

**[26:37] Andrey Sadovykh:** Okay, okay. Good. Okay. Well, okay. I can't say anything special yet. I'm a little thoughtful about it. But I'll see. I don't understand why you're going to attach all this to some project. So, we need to take it on Java, some backend, right?

**[27:10] Aziz Vundirov:** Yes, yes. There were articles, in which, in the articles, open repositories were indicated, on which they were running it. So, we can dig there, find something.

**[27:20] Andrey Sadovykh:** And what exactly do you offer as an additional hypothesis? Experiment? No, as an additional hypothesis.

**[27:28] Aziz Vundirov:** That dynamic context can improve the performance of their frameworks.

**[27:33] Andrey Sadovykh:** What is the dynamic context in your case?

**[27:37] Aziz Vundirov:** For example, in Java Spring there are a lot of... For example, there is a DI container that injects bin objects with runtime. And with runtime you can find... For example, you can take the info, which bin is injected, And somehow we need to form this and feed it with IEs.

**[28:06] Andrey Sadovykh:** Ah, you mean dynamic contexts? These are the classes that are sucked in along the way?

**[28:14] Aziz Vundirov:** Yes, yes, yes.

**[28:15] Andrey Sadovykh:** Not static, but dynamic ones? Yes, yes. Ah, well, yes. By the way, yes, indeed, it can change the architecture of the application quite a bit. because runtime architecture will be different from what tools see in code. I see. It's interesting, actually. It's a very interesting approach.

**[28:40] Aziz Vundirov:** They haven't compiled their code yet. It's not just a stupid source code. Especially in Java, you can compile it, and there you have a million Java classes generated. It's also interesting.

**[28:53] Andrey Sadovykh:** Yes, by the way, this is a great idea. super here is my runtime runtime idea when these classes are also very cool, that is, the runtime can be quite different from the fact that static tools are in the code, some kind of type, well, like static tools for dynamic code, that is, not a test, not a test, именно именно оценка архитектуры рантайм архитектуры да вот из при где очень классно

**[29:28] Aziz Vundirov:** есть фишка что там есть ручка он называется оптата об ланкой просто может вернуть и получить

**[29:34] Andrey Sadovykh:** весь контекст в джессоне понял а контекст это что этот как раз именно вот это вот ра рантайм архитектур да да да есть какие они поднялись там да да да да да да связь там граффити Oh, excellent, interesting. Okay, let's really see it. I think it's a pretty interesting thing. Well, then you need to say that we have static tools and SonarQube looks only at the code, and it doesn't look at what really happens in runtime. And in runtime it can be quite very different because there are many classes dynamically called, it is possible that this is the most here and thus it is not the same as an arc tube, but other these are static, they do not reflect this, that is, you need to see if such tools that do this dynamically compare with them well, or how to look, we can dig there Okay.

**[31:06] Aziz Vundirov:** And the second thing is that I want to compare. This approach will find no fewer errors than static TOOLS. Expensive tools, just. Okay. The first thing is that dynamic context is optimized. The second thing is that it will find no fewer errors than our static TOOLS.

**[31:31] Andrey Sadovykh:** Okay, I got it. Okay, good. Okay, let's finish this. What else can I help you with? I have a research proposal.

**[31:46] Aziz Vundirov:** I just wrote it.

**[31:48] Andrey Sadovykh:** Yes, you can send it.

**[31:50] Aziz Vundirov:** I'll do it. So, what else can I do? What kind of action do I have? Should I dig the same way?

**[32:02] Andrey Sadovykh:** Yes, we have already understood that this is a promising topic, let's dig further. You should add more articles, because there may already be articles for dynamic evaluation of architectures. If not, look at the articles too. You need to choose something in addition.

**[32:22] Aziz Vundirov:** So, we need to find even more articles, right?

**[32:26] Andrey Sadovykh:** We've changed the topic a little bit, we've deepened it in some way. It's clear that others have already done something. More precisely, what others have done.

**[32:41] Aziz Vundirov:** One more time? A question for me?

**[32:42] Andrey Sadovykh:** No. The question is about...

**[32:47] Aziz Vundirov:** Look at what's in it.

**[32:50] Andrey Sadovykh:** Yes, we've deepened the topic, it has changed a little. We have more details, we need to see what others wrote about it. Maybe even some have done something.

**[33:00] Aziz Vundirov:** And the idea to narrow the language to Java? How do you look?

**[33:05] Andrey Sadovykh:** What?

**[33:06] Aziz Vundirov:** The idea to narrow the language to Java, that is, only Java projects.

**[33:10] Andrey Sadovykh:** Great, great.

**[33:13] Aziz Vundirov:** Okay, narrowing.

**[33:16] Andrey Sadovykh:** No, good, you need to narrow. And you would need to look at some benchmark. Because the benchmarks you saw in the articles may not be suitable for a dynamic case.

**[33:33] Aziz Vundirov:** Do you think that we have found everything?

**[33:38] Andrey Sadovykh:** We are going to make a tool that will work with this. show something good there, bad architecture, yes, it can be recommended to suggest that's exactly dynamic to evaluate dynamic characteristics of this system, yes, I will evaluate the architecture in dynamics, that is, the metrics will be something else to suggest, yes, what already works well and correctly and correctly shows you need to validate on some experiment, or at least some of these systems. Recently you told me that you saw some benchmarks there, some articles, if I understood correctly.

**[34:27] Aziz Vundirov:** I suggested writing tests on ArchUnit, like BSLine.

**[34:37] Andrey Sadovykh:** Look, it's best to take a benchmark from someone and compare it with them. If there is already some kind of network of such projects that can be evaluated, or someone has evaluated in their articles, then you can take this dataset and run your hypotheses on it, And compare. Working on a known dataset is much more convenient than collecting your own.

**[35:13] Aziz Vundirov:** I see. I heard you.

**[35:20] Andrey Sadovykh:** You need to find other datasets. These are several projects that you will evaluate. Because on one project, validation does not work.

**[35:32] Aziz Vundirov:** How to correctly estimate the number of projects?

**[35:36] Andrey Sadovykh:** It's called statistical significance. The statistics start from 30. 30 is not bad. Well, yes, it's not difficult to find it in the GitHub. Not that it's difficult, but if there's some known dataset, it's better to look for the best of the best. Well, look for some Java Spring dataset there. Look for it. Or people who write about their tools for Java Spring, they probably also use some kind of dataset.

**[36:34] Aziz Vundirov:** And making a dataset is artificial. It generates 30 small projects where we specifically poke at errors, that is, in the KB.

**[36:47] Andrey Sadovykh:** That's a good approach. That's a good approach. What do we want? So that the bug will determine the loss?

**[37:01] Aziz Vundirov:** Yes, it will. It will determine them.

**[37:05] Andrey Sadovykh:** The designer will not determine, but your loss will determine.

**[37:08] Aziz Vundirov:** Yes, one loss will determine, but it will not determine, but it will determine. Like this, compare the performance.

**[37:16] Andrey Sadovykh:** Yes, yes, yes, yes, you can also, like, from the sitting of these mistakes, you can throw it, yes, you can also do this. But you need to see how to organize it correctly.

**[37:46] Aziz Vundirov:** I don't understand, the idea of comparing my tool with static tools is not enough, right?

**[38:10] Andrey Sadovykh:** No, it's fine. Well, if there are no other dynamic tools.

**[38:15] Aziz Vundirov:** Oh, you mean comparing with other dynamic tools, like their performance with my performance?

**[38:22] Andrey Sadovykh:** Yes.

**[38:24] Aziz Vundirov:** Okay, I got it.

**[38:26] Andrey Sadovykh:** No, you can compare, you just need a dataset. Compare on something, on some dataset.

**[38:33] Aziz Vundirov:** So the question was about the dataset, right?

**[38:36] Andrey Sadovykh:** Yes, we will compare yours and a little different, but on some dataset, on some projects. This we need to collect either ourselves, or look at someone. Better to look, because it is easier to explain later where it came from, how it was made, and maybe they even have some metrics there. Because then you will need to add your own errors, then you need to find literature where you can correctly tell how to correctly add errors.

**[39:17] Aziz Vundirov:** So, you mean, you don't have to scream in the quote? You don't have to scream in the quote?

**[39:27] Andrey Sadovykh:** Well, maybe there is such a approach. You need to understand if it's normal or not, so that he makes mistakes.

**[39:35] Aziz Vundirov:** The approach should be based on some practice, on some strategy.

**[39:41] Andrey Sadovykh:** Yes, there should be practice. We have a statistical thing, evaluation. It worked here, it didn't work here, it worked on some percentages, but it didn't work on others. It depends on the sampling, that is, what choice we make, how we prepare the data. This is a very big influence on the result, how the data was prepared. If we didn't prepare them correctly, and prepared them to show only the positive sides of your tool, everyone will say that you are just playing around with the map, that is, you drew the results yourself, and why did you do it? that is, there apparently needs to be somehow errors some kind of random sampling to do here to throw ok

**[40:48] Aziz Vundirov:** such a project such a periginum after the point what to do so there is no question maybe you have something to ask me no I have no questions at all

**[41:06] Andrey Sadovykh:** here okay well yes we will soon make a presentation last week thanks bye

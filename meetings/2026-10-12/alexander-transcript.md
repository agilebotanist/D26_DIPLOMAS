# Встреча 2026-10-12, 15:23 GMT — Александр Исупов

Запись GMT20261012-152002, первая часть: до 21:51 по часам записи. Вторая запись в этом файле, Азиз, в `aziz-transcript.md`. Исходные файлы целиком лежат в `_combined-GMT20261012-152002/`.

Слова: Whisper (`alexander-whisper.srt`). Говорящие и таймкоды: Zoom (`alexander-transcript.vtt`). Склеено
`meetings/merge_transcript.py`, реплики одного говорящего слиты в абзацы. Атрибуция на стыках
реплик приблизительна: Whisper режет по времени, Zoom по голосу, короткие «да», «окей» могут
оказаться у соседа.

**Whisper снова запущен в режиме перевода, а не расшифровки**: текст английский, термины
искажены. Сверено с русским VTT: «TSL» = DSL; «Excel» в перечне DSL-задач, предположительно
Excalidraw, рядом BPMN и «План Хьюма» [предположительно PlantUML]; «Go» читается как «гол»;
Arch Unit = ArchUnit; Sonar Cube = SonarQube; «Nov» = NOV (метрика из статьи Stevens).
Для следующего прогона нужен `--task transcribe`. Реплики-галлюцинации на тишине отброшены.

Фамилия автора, упомянутого руководителем при просмотре документа, по Zoom VTT звучит как «Лучано Борези»; по присланным заметкам это Baresi et al., статья про технологии iOS-разработки. Метрика «деньги» из статьи 4 в заметках Александра названа NOV, это Stevens.

**[00:00] Alexander Isupov:** I was okay Alexander, yes, good evening, hello again, so two weeks with you did not see each other in general because in two weeks I did it in the first article I read anyway which you gave 14 minutes on the topic of these metrics architecture in general, I wrote notes on them in general, if necessary, I can share it, but let's

**[04:19] Andrey Sadovykh:** now I will share then better group say what you say in a group but not a group in this chat

**[04:28] Alexander Isupov:** so sense of the chat I thought I was just sharing the screen now, and well, you can better chat well, let's just throw this link to google.com to you now, but if

**[04:42] Andrey Sadovykh:** google doc there is my throw there just went out to the telegram all I go to look where to look shorter than

**[04:50] Alexander Isupov:** then I also said 26 in fact this is what I did now, but before that, it's not that it's not quite relevant to the note, another structure was here, I can somehow comment on the whole little yes yes let's here on the first article there the most useful thing is the thought that in general The dependencies are not evenly connected. The idea is obvious, but it will be useful to support it with a source. For me, the key idea of this article is that 10% of active dependencies can give more than half of the distribution between files. Concentration is not worth all files, even if you make up the matrix of dependencies of DSM. At least I understood that.

**[05:35] Andrey Sadovykh:** this is boris it seems familiar to me I look who is this ray on boris maybe exactly ray on boris professor of the field of engineering where milan yes I know this interesting So, okay.

**[05:58] Alexander Isupov:** This is the first one. The second one, in fact, was all about Propagation Ghost, and the idea that it is useless to use it naked, because it does not measure changes at all, as it were, in the layers of architecture, it is difficult to say. Well, if you use it, somehow with scales to play, but from my point of view, to make scales, at least I don't imagine an instrument to automate it and arrange manually scales in the dependency matrix, it's pretty much like that. The matter is ungrateful, to be honest, if this is a project for, say, 30 thousand lines, which at least still have a lot of time to choose. The third article is key, I think, in general, from all that you gave. It is the most complete, it reveals the idea of DSM, something like that, it introduces terms, in general, in general, somehow, then I also liked the idea that you can use design rules, roughly speaking, feed the agent with patterns that are used in the project that are worth really adhering to, the idea is also obvious, but well, yes, well, yes, well, of course,

**[07:10] Andrey Sadovykh:** they themselves just look at it, and in general everything is so close, I see that it all goes spec-driven design. And the spec should be of a certain type. An agent can impose his own spec. He can choose any.

**[07:44] Alexander Isupov:** Aspects can be both whitebox and blackbox, and in this case I chose something like whitebox Well, when we describe something from the inside of the system

**[07:54] Andrey Sadovykh:** Well, yes, of course, you can do it, first of all, you can say that you are doing architecture, or you can break it into such components, or before you decide, let's discuss how big they will be in each component, how connected they are, and so on

**[08:10] Alexander Isupov:** Well, yes, in fact, it is. Even the I mean, it can be a part of the success. Don't you think so?

**[08:48] Andrey Sadovykh:** Yes, yes, yes.

**[08:50] Alexander Isupov:** And the fourth article, I honestly didn't understand the Nov metric very well. I realized that it definitely shouldn't be used.

**[09:00] Andrey Sadovykh:** As far as I understand, it's from finance. There is such a thing called... Damn, I forgot. DCF... CF is cash flow, and D is... I forgot what it is. The point is that today's money is more expensive than tomorrow's money. If you invest money somewhere, you have to get more of it.

**[09:36] Alexander Isupov:** Yes, that's clear.

**[09:38] Andrey Sadovykh:** DCF, I forgot the name of the company. And with all these changes, they measure the cost in money. But this is probably a new one.

**[09:57] Alexander Isupov:** The article said that using it to measure architecture is a kind of a trick.

**[10:02] Andrey Sadovykh:** Well, they use this money not because they really want it, but because it is more understandable for managers. When you say, well, they changed it, it costs so much, now they changed it, it became cheaper. And immediately the manager understands, yes, it's interesting, I saved a lot of money, I can tell everyone around. And it won't approve refactoring. It will say, why? It works this way, let's give a cow

**[10:33] Alexander Isupov:** These are the articles about ArchiHector that were given. And I also looked at a couple of articles on iOS There are two articles in the top, about anti-patterns in IOS. You can use it to feed the IJs, but you shouldn't do it like this. In the top article, they wrote about top anti-patterns, which appear most often. I think you can feed them.

**[11:07] Andrey Sadovykh:** It's not necessary to feed them at all. We've talked about spec, pattern, anti-pattern. Maybe we can do some guardrails. First of all, you can survive from articles.

**[11:32] Alexander Isupov:** essence what to do what not to do well yes yes yes there you can live from them in general secondly you can

**[11:39] Andrey Sadovykh:** compare these skills with each other because they may contradict each other or complement each other , then you can make some kind of general skill and compare the agent without a skill with a skill one spec and some parameters but the parameters need to be invented, but it's already necessary to look at the same articles, you need to understand what is more valuable, that is, we want to make a nobility, and we are on the ability of the agency, where the number of agents is not quite easy to measure, but there are ordinary metrics may not fit. For example, I complained recently that Sonar does not show anything at all on the Wipe Code projects. I also had one article, I'll throw it to you now, too, as standard. But on your projects from last year, it actually showed not very much, it didn't show anything in general, it showed that we gave you the wrong ones, the same is not good, in short, they gave you the wrong tasks, they gave them as the same as before, but we didn't finish our coding, what happened that the project became seven times more complicated there,

**[13:05] Alexander Isupov:** well, I'll also look at it, it will be useful, well, in general, everything is the last one there about the overall development of ios and just about in order to confirm that I wanted to use a relevant framework for analysis, it is clear that there are many frameworks and you still can't review everything, yes, yes, no, separately, but there is

**[13:34] Andrey Sadovykh:** I'm a little confused about iOS. There are some problems to start testing. I don't know if it's necessary to register a test account there. Pay 100 euros for a license from Apple.

**[13:52] Alexander Isupov:** No, I don't think so. To build a project and run it through tests.

**[13:57] Andrey Sadovykh:** What is it? TestFlight?

**[13:59] Alexander Isupov:** Yes, but it is for users' application

**[14:05] Andrey Sadovykh:** I don't know how it works

**[14:11] Alexander Isupov:** You don't need to pay anything to build a project locally

**[14:14] Andrey Sadovykh:** Just Xcode and that's it

**[14:17] Alexander Isupov:** Yes, Xcode, but it depends on what you want to pull

**[14:21] Andrey Sadovykh:** I see, okay

**[14:25] Alexander Isupov:** In addition to this, I will still teach myself, I will go to lectures and courses.

**[14:31] Andrey Sadovykh:** It is not clear what to use it for. You said something about a project for 30 thousand. Why did we say that? I'm starting to forget everything.

**[14:45] Alexander Isupov:** I remember you said that for statistical significance it makes sense to consider at least 30 projects with different experiments. I am more for doing a couple of projects, up to 5, but really big ones, for example, for 30 thousand codes and giving them different tasks for experiments. experiment and it turns out that the number of experiments in general can be done according to the number of statistical values ​​there to bring to 30, let's say something like that, but in short, on really large projects, not on small ones, not a bunch of small ones, but a couple of large ones, well, not large, but large ones,

**[15:21] Andrey Sadovykh:** okay, and what will you do with them just evaluate the cloud will just evaluate the inheritance of your incomprehensible best practice or something or then you will force the agent to redo it and, like,

**[15:39] Alexander Isupov:** compare how much it actually corresponds to the architecture that we fed him some real tasks give him refactoring potential and this refactoring

**[15:53] Andrey Sadovykh:** What is the purpose of refactoring? Might and ability? I don't think so. Performance?

**[16:10] Alexander Isupov:** Performance is minimal, but might and ability is more important.

**[16:14] Andrey Sadovykh:** By the way, performance is easier to measure.

**[16:20] Alexander Isupov:** But performance is not bad.

**[16:22] Andrey Sadovykh:** And the metability is not bad.

**[16:28] Alexander Isupov:** The idea of performance is not bad either. From the point of view of measurement, it is really easier.

**[16:34] Andrey Sadovykh:** Of course it is easier. But on the other hand, it is not so easy to achieve this. because in itself this modularity and correct architecture does not necessarily

**[16:52] Alexander Isupov:** well affect the general understanding of the general incomprehensible why we want we want to do all these beautiful architecture, but I generally first thought about the moment on the billet ok more

**[17:09] Andrey Sadovykh:** Let's take the best. We can do this. Now a lot of code is being wiped out. Many teams are just standing there with their hair in smoke because it spoils the architecture. It is not supported and it is not clear what it does. The tasks are such that, first of all, it needs to be supported, so that next time, if something needs to be changed, it does not have to be reset. Burn tokens to redo everything. Here, again. Although some people do it like that, they just throw everything out and redo it again.

**[17:55] Alexander Isupov:** It's easier for someone.

**[17:57] Andrey Sadovykh:** Yes, there should be some specs. Secondly, it is not clear how to get quality guarantees. The system does what it needs and does not do what it does not need. And according to other quality characteristics, it is good. It's also not clear how. People are watching it. Who to ask? It's not clear.

**[18:31] Alexander Isupov:** The one who wrote the code.

**[18:33] Andrey Sadovykh:** No, the one who was controlling LLM.

**[18:37] Alexander Isupov:** Yes. The question is how to measure the momentum. because I read an article on this dslm about these metrics, but about the tools that can really be automatically applied to drive a project and say that it has improved on the big one that it was one hundred percent honestly I did not find such a well, in general, we are on the bill, in general, in the article, it is written

**[19:02] Andrey Sadovykh:** as the last metrics of the last our world and that they found on the metrics that are best and we have been working on your projects since last year. I even think that maybe some new metrics are needed to understand what is good. Perhaps these metrics will be based on the architectural patterns that you will find. Patterns can be measured, you can take MVPs, model view controller MVC or some other MVC is more outdated than MVP slice some feature slice design something else but again it does not show the modularity as you correctly distributed there on modules there on features that they are like a balance of these

**[20:11] Alexander Isupov:** features, but in general, although we can not even help, we look at the layers of the architecture, I think

**[20:17] Andrey Sadovykh:** layers are not quite answering the question of good but it seems to me if the data layer does not look at

**[20:25] Alexander Isupov:** some kind of domain layer, then this already indicates that the hero is not bad. These are the simplest options.

**[20:29] Andrey Sadovykh:** Well, yes, it's clear that ... It seemed to me that the balance between the components, how much one is heavier than the other, how much one is a bottleneck, is actually

**[20:47] Alexander Isupov:** even more important. This, by the way, can also be achieved. Or, in the extreme case, if completely with the main ability, then you can try their performance there, at least

**[20:58] Andrey Sadovykh:** measure it, well, yes, the first one is the best, but we are on the bill, of course, it is the most relevant yes, everything is more and more and more plus I say and it is clear what features are made what kind of application does what is necessary and what is not necessary does not do what is there for this very thing and we see as if black box in fact, in the end, in general, it is not clear how to solve it, but of course it is not possible to solve it in general, as it were, some steps here are more it was clear that this is not done

**[21:38] Alexander Isupov:** well, then I see the time, then with you all thanks good evening yes goodbye

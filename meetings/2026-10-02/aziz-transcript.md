# Встреча 2026-10-02, 15:46 — Азиз Вундиров

Собрана скриптом `meetings/merge_transcript.py`: слова из `aziz-whisper.srt`, говорящие и
таймкоды из `aziz-transcript.vtt` (Zoom), реплики одного говорящего слиты в абзацы.

**Whisper снова запущен в режиме перевода, а не расшифровки**, поэтому текст английский и
термины искажены переводом. Смысл восстанавливается, отдельные названия — нет. Сверять по
русскому `aziz-transcript.vtt`. Для следующего прогона нужен `--task transcribe`.

Реплики-галлюцинации Whisper на тишине отброшены. Там, где перевод породил бессмыслицу
(например, представление собеседника чужим именем в первой реплике), это помечено в
заметке, а не исправлено здесь.

**[00:00] azizvundirov:** Thank you. Thank you. Hello everyone, my name is Igor, I am a product manager at T-Bank, I am responsible for quality control. and the other most collegues ashes yes live no office such a narrow the footer is the a-figure the vlog yeah pregush I was nimble the comments as a look at you yeah either no stretch Sam Paca

**[01:56] Andrey Sadovykh:** Thank you. hello hello heard heard so look yes that is, one first, in general, there are a lot of different patterns how it is done in general, I think you are not the first and most likely not the last one, do there is a lot of replications there in general, the study of what has already been done and this is not quite a topic for a diploma, so initially we had with you that we had about the

**[03:09] azizvundirov:** architecture architecture representation

**[03:17] Andrey Sadovykh:** for what for java and for this very yes for the wedge here so well, in principle, architectural here is the time of the architecture, they are basically not bad questions, the architecture is always needed, but it has a very strong influence on the quality, I don't know, in general, think about it, in In general, leave the architecture and the quality somewhere, and if you want to tie it to your new task, please. The quality of the architecture.

**[04:09] azizvundirov:** Let's leave it, yes.

**[04:12] Andrey Sadovykh:** About Java, you can, I don't know, you will do it or not, but in general, the quality of the architecture must be left. Yes, without professionalism. And when you do, you can include them in your new work, for example. There are some architectural patterns in replication. Push-pull is not really architecture, it's a mechanism of interaction. Modularity, system layout, layers, modules, breaking down all sorts of things this is this architecture yes well, it turns out to be a job, but already look at the case of breaking down classes there, not quite yes, these are classes plus more structurally, well, not quite there, but as if you have a module, this is one class or there is some kind of component there, that is, a bunch of each component has its own architecture. Maybe there is an architecture, a global one, that is, how the modules talk to each other. Because we take a microservice or an OLED, these are big words, but in general, microservices are a bunch of different modules, they somehow communicate with each other. You probably have something that responds to the For connection to the database, for communication, for API. I don't quite understand where we are going yet.

**[06:01] azizvundirov:** Let's just say that we will refuse to work on it.

**[06:09] Andrey Sadovykh:** No, we will not refuse. You didn't do anything on the first one either. Why should I refuse on the second one? First, you didn't do anything. Let's try the first one, and then we'll see if it will take the second one. We will have to do something.

**[06:34] azizvundirov:** Yes, and we need to do something.

**[06:40] Andrey Sadovykh:** I mean, where are the articles that you read? What did you understand? What methods are used? Where is it all? We lost a month, count it.

**[06:57] azizvundirov:** Can we read it? No, I'm just asking.

**[07:05] Andrey Sadovykh:** If it's architecture, then okay. You need to read everything. Where is the log? Did you read it?

**[07:16] azizvundirov:** I sent it to Google Docs.

**[07:20] Andrey Sadovykh:** So, there's a lot of stuff in the Google Docs, right?

**[07:24] azizvundirov:** Yeah, a lot.

**[07:25] Andrey Sadovykh:** So, it's been updated a little bit?

**[07:28] azizvundirov:** Yeah, I've read it.

**[07:31] Andrey Sadovykh:** Okay, let's see. Where should I read it?

**[07:46] azizvundirov:** After the methodology, I will give the result.

**[07:53] Andrey Sadovykh:** This is the key results. I see three things. Git clear, Slater and something else. I see three. I'm looking at the ones from September 5.

**[08:12] azizvundirov:** I took the topic of the throw.

**[08:17] Andrey Sadovykh:** Is that all? Three pieces? And what? Where is it about architecture? Where is it about the connection of architecture with, I don't know, with what? where something is so 9 6 that is, in fact, you are looking at the wedge at the level of classes at the level of the op

**[08:59] azizvundirov:** why do you want to go to the people we want to find out if the violation of the

**[09:11] Andrey Sadovykh:** lmk is why the usual tools about the architecture of the wedge do not fit why we have to fasten the

**[09:21] azizvundirov:** just follow we have a regular one that is called so look at you 33 work this is

**[09:31] Andrey Sadovykh:** little that is, you need much more firstly you need to determine the domain area that is, what we are studying there we are studying the architecture of the cloud and which assess the adherence level consistent conformity conformity well, what is architecture or design of the application, it corresponds to the architecture, that is, they probably also have some number, they are described in different articles further as lm is generally used for architecture in general and for for clay architecture in particular, yes, that is, the story is probably a topic, of course, well, three is not quite late, you are already much more on this topic, as it were, and in principle, your thoughts on the определения какие-то надо вытащить уже что мы называем клин архитектуры почему вот такие уже тулзы существуют почему они вас не удовлетворяют ну в принципе других не удовлетворяют это тоже можно стадии вытащить там не там говорят какие то у них есть limitations вот в чем смысл применять lmk or other items and to the architecture, that's what other people wrote about it, somehow it is necessary to upload it and write further

**[11:07] azizvundirov:** I did not get to find or we are just going to be on the front of the research gap, it will appear, that is,

**[11:27] Andrey Sadovykh:** this is one of the tasks, this is one of the tasks, the first task is generally to determine the terminology to determine what kind of architecture is some tools and there are in general used before now used in general I don't know the evaluation or the test of the clay of the architecture or detecting that it is not a wedge, that's how I use it in this sense, then some define the gaps that people say why in general it is necessary why something is missing, then the hypothesis that you have something if you put it in such a tool or add some kind of graph graph of the architecture itself in some form, it will work better to give the best result, well, something like that, in this direction, you understand that is, step by step from the beginning, first we decided what exactly we are in what area we work, that is, we determined it, that is, here is the architecture of the wedge, why we use it because it is better because the quality is better there to support better there something else well, why do we need this clay architecture, then what tools are there that help you to do everything on the clay, that's what their problems are, why I am applied in what problems with I am here and you need to throw articles there, in principle, read them very quickly, at least read abstracts, in principle, you already see there is my hope the result in the lead data set key results here is about this, well, and while the article is, in principle, your some ideas in any form there are not afraid there some stupid look just didn't like there some kind of multi here I saw it normally like the definition of the dataset, you can pull it up there, pick it up from them, cut it off, write some ideas of yours, here are your ideas, some thoughts, some of them are not actually most interested in your thoughts on these articles, everything else there can be automatically pulled out of the article, there is no there is no big sense, but in general, there is, as it were, the meaning of gaining this knowledge base on this topic, but it is very valuable your reflections that will help you then somewhere to come to some kind of hypothesis and somehow to make it somehow to make it understood yes and, as it were, I suggest you accelerate because, as it were, the result for one I work for a month, or maybe even more, but it's not convincing. I want you to get confused with the topic. So we need to speed up somehow.

**[15:14] azizvundirov:** I see. So, I get it that the topic, the article, yes? We need to throw in even more, so that it sticks, right?

**[15:22] Andrey Sadovykh:** Yes. I already told you the structure. We determine the area, we determine what is missing in the area. We define what problems with AI are. Not with AI itself, but with tools that define and advise on client architecture. What they can't do at the moment. Then we form our own hypotheses based on everything we've read. And we experiment. We validate the experiments.

**[16:07] azizvundirov:** So, what will you do with the diploma?

**[16:12] Andrey Sadovykh:** No, it's about the literature. It's not clear where you will go with the diploma. Hypotheses, experiments, it's not clear yet. But I would like to do it by the end of October, when we have a general meeting. You told everyone. At least I formulated it. To begin with, at least in Telegram, add the search structure for your literature. Where will you go, where will you look. And add articles. Don't be afraid.

**[16:48] azizvundirov:** In the chat?

**[16:50] Andrey Sadovykh:** Well, it's better to put your document there, your Google Doc, right? The next time we call, we'll look at it and check what they threw at us.

**[17:06] azizvundirov:** I see. And such a question, I should have a professional article, that is, it will not fit on the HUB, right? If there is a zone there.

**[17:13] Andrey Sadovykh:** better yes the main thing is the conference with the hub is not bad in the sense that it can understand some kind of hypothesis, so to say, but it's like for our literature review, it's not suitable because there is no validation of the results, so it's not a peer review, it's interesting, it's useful it gives us ideas and hypotheses that we use scientific methods to confirm or reject somehow, in principle, you can throw it in principle, it will help for everything, but not so much that it will go to a diploma as it is there, it can help a lot, well, as if it can be very normally be described as such a wedge architecture good definition of the beautiful one that we like or problems there type 1 and then we will find these problems and confirm them in scientific articles, that is, some such things are very useful why cool but here is how the basis for for work it will not go, but as it were, it is interesting and useful and, in principle, it can lead you to the right direction, but how can you build everything on the hub, tell me where it is best to look for articles on google school, of course, you beat the architecture there and that's it, the most terrible ones you choose there are the most relevant ones, you can start a laptop lm there is also deep search on different topics, you can also throw up, but there you need to, as it were, he can come up with various links and not only from scientific

**[19:16] azizvundirov:** articles to take in general, you need to check what he gives there, yes, how everything is with eggs, the main thing is to understand the methodology,

**[19:26] Andrey Sadovykh:** , and then, and then this is the same metallurgy, go and load, scrape, scrape, scrape

**[19:34] azizvundirov:** articles, process, I understood such a question in terms of the size of the page with the diploma, how much you need to

**[19:44] Andrey Sadovykh:** add, you don't think about it, you add it to you, the hedgehog will help you if the main thing is that there was that there I remember how much I remember there in the area of 40 pages in general in the area of ​​40 links to ordinary articles, but it's not important to us, it's important for us to have some kind of essence in this and the page to patch so if you have 40 articles it's not a problem at all well, in general, yes, yes, let's do it, call so next week, it seems I don't have anything никаких этих самых кроме понедельника у меня нету понедельника вам еще рано кстати да надо сразу мне обрубить на следующей неделе этот не будет у меня возможности прийти так сразу я cut off so and did not understand this is still someone here already put so under 16 and Maybe I will have it. Then the 20th, 23rd. 23rd is not a norm. Then it's a norm. Except for next Friday. Look there. Put it there. Yes. Okay. That's it.

**[21:39] azizvundirov:** That's it.

**[21:40] Andrey Sadovykh:** That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it. That's it.

**[21:43] azizvundirov:** That's it. That's it. That's it. That's it. That's it. That's it. That's it.

**[21:44] Andrey Sadovykh:** That's it. Good bye.

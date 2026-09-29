# Встреча 2026-09-28, 15:39 — Александр Исупов

Собрана скриптом `meetings/merge_transcript.py`: слова из `alexander-whisper.srt`, говорящие и
таймкоды из `alexander-transcript.vtt` (Zoom), реплики одного говорящего слиты в абзацы.

**Whisper запущен в режиме перевода, а не расшифровки**, поэтому текст английский, а
термины искажены переводом: SAST становится «state elite» и «statelites», Qwen2.5-Coder —
«QN5 coder», false positive — «Fox positive», виртуальные потоки — «virtual flows»,
литературный обзор — «political review». Смысл восстанавливается, отдельные названия — нет.
Сверять термины по русскому `alexander-transcript.vtt`. Для следующего прогона нужен
`--task transcribe`.

Реплики-галлюцинации Whisper на тишине («you», «Продолжение следует...») отброшены.

**[02:30] Alexander Isupov:** Hello again. I can see everything, I can hear everything well.

**[02:39] Andrey Sadovykh:** Tell us.

**[02:45] Alexander Isupov:** We met at the end of the spring semester. I went out in touch with you. I think I won't be introduced too much, I'm Sasha, I work at T-Bank, I work as a key engineer in the mobile development team. He literally only at the beginning of the fall switched to the position of a middleman, and as for further development, I see that in mobile development. My team can only give me the opportunity to develop iOS, so I take only this opportunity, Despite the fact that I have a pretty big background in Android development. My team can't give me Android development. Therefore, I see what I am afraid of in my further development. And I would honestly like to get more experience from work, not only from iOS development, but also from the experience of viewing projects from iOS, namely iOS applications. I remember we discussed in the spring that you would be interested in the topic of using agents for refactoring the architecture of applications.

**[03:49] Andrey Sadovykh:** Yes, I know about it. In general, I am interested in the topic of architecture and the availability of various applications. and in principle, how much we support what agents do.

**[04:12] Alexander Isupov:** Excuse me, now is literally the last minute, maybe there were problems with the network, or you have, I don't know. I tried to turn off the VPN now, can you please repeat your thoughts? Was it okay for me to hear?

**[04:24] Andrey Sadovykh:** Yes, you were okay to hear. I want to say that I have already forgotten, but I think I will find myself. I am interested in the maintenance ability and architecture. And basically everything that agents do, that is, from the point of view of architecture and maintenance ability, how much they spoil, improve, there are techniques so that they work on large projects, for example. There are some magical methods so that they do not spoil the architecture.

**[05:01] Alexander Isupov:** Well, you can continue to think, because I read a little literature on this topic, and talked to developers on the topic of potential topics for diplomas and agents. I remember we discussed with you that if you conduct such experiments, using agents for IP refactoring architecture, then the number is 30. That is, you need to consider at least 30 projects, roughly speaking, so that our researches will be useful. I imagine that there will be difficulties to find 30 projects suitable for our requirements. Why? There are so many of them on GitHub with applications I imagine, yes, but for the majority of projects, I think, there are 500,000 lines that we... Well, I can't imagine that they are right for us I would rather find projects 3-5, some really worth it, lines of 30,000 or 1000 codes And for these projects, not to give them the same task as these projects, but to form a pool of tasks Various for these projects and already orient from them In fact, there will also be 30 experiments, but not with the same task, but with different possibilities.

**[06:20] Andrey Sadovykh:** Well, you know, it's not just about the task, but also about the number of launches, for example. They can differ from launch to launch. Plus, we can somehow bypass this restriction, but the more the better. I'll send you... Now we have two articles, we have still pushed two articles on the architecture of the main ability. By the way, since last year you have also participated in your research projects. Yes, because we had a study of your project. So I'll send you everything that is on this mobility. Well, yes, and plus, yes, but still, you would need to see if there are any architectural patterns, if something is broken. If we consider even 5 projects, will they use the same architectural techniques? some kind of clay, I don't know what kind of understanding is very wide, well, yes, very wide, there is a break-up on some special ones or maybe how the developers themselves defined the architecture there, what layers they have there, what components some contracts and chips want special, well, here I would

**[08:09] Alexander Isupov:** possibly concentrate on the patterns of the ui layer of the application, I remember you also said that there are there are quite a few articles on this topic, so it would be difficult to find materials, but there are advantages in a specific sphere, but that in ios, that in android there is a stable ui pattern, and if they write in ios on model view controller, then everyone writes on model view controller, you can look into this topic, and besides, within one project you can find several applications of this pattern for different screens,

**[08:39] Andrey Sadovykh:** also the module view controller is probably unlikely there the lmk break the nothing but when it's just a minute when you say a big project on 30k yes that is, they can there are different components of the video, that is, some api there is somehow they communicate with each other and And since the context window is not infinite, they can break contracts with these connections. Perhaps it is worth looking here, because the modular controller is not such a global pattern. It's hard to break even if there is a triangle. they are somehow divided, yes, that is, there are separate parts there are separate windows there, it's difficult to break it, but breaking the contract between components that no longer work, although they are there, they can run integration tests and all that, I don't know, in general, it seems to me that this side needs to be

**[09:48] Alexander Isupov:** Well, yes, and speaking of which, you mentioned the tools that help Iishka so that they do not break the architecture in general. I also talked to developers, with IOSers, they suggested that they help graph dependence quite well. Maybe I'll look at this side of the study.

**[10:06] Andrey Sadovykh:** What?

**[10:07] Alexander Isupov:** Graph dependence.

**[10:08] Andrey Sadovykh:** Ah, well, graph, yes, graph dependence, yes, yes, yes, exactly.

**[10:11] Alexander Isupov:** And to test it, to run a few LMS without a graph, to see how much they will break, to understand if the project is being compiled or not. But I have a project on ETI that will not be compiled, if we take a large project. And to look at the number of files that they could potentially forget to change, but this can be checked manually. And to conduct the experiment with the graph, depending on the rhythm.

**[10:39] Andrey Sadovykh:** Yes, think about it. There is a feeling that the graph will not do. There is a feeling that we did it. Even if everything is compiled, the tests are passed, and if the architecture is broken, it is impossible to develop the project further. That's why it's like that. We need to look in this direction too.

**[11:07] Alexander Isupov:** I don't know any methods to assess how broken the architecture is or not, in addition to manual analysis.

**[11:14] Andrey Sadovykh:** Of course, there are a lot. There are various metanability metrics, there is such a metanability matrix, DSM. I had some stories somewhere, I'll throw them out. Propagation cost is reflected there. Depending on the graph, you can imagine the matrix in the form of one connection. Then, by operating on the matrix, you can isolate clusters and see if there are any. there are several pieces here some by some patterns that can arise here which is just a bad shot of the main ability of his ability propagation cost each each new code change it adds too much complicates the system

**[12:17] Alexander Isupov:** understandably and it's all clear to me the instrument is automated well, in some way, in fact, about the

**[12:24] Andrey Sadovykh:** propagation cost, it seems that there are no ready-made instruments before, they were forgotten somewhere forgotten such a topic, although it is very clear, very clear, well, you can still look at some technical depth, but there is more about the code smells about all sorts of things, that's better, but I'm interested in the architectural part of you, probably like a honey, but I also have a test of the development of the need, well, as it were, yes, that is, there is a mess, but the lmk ok it will find bugs there and there are not enough tests for something like that, in fact, you need to look up, look further

**[13:09] Alexander Isupov:** higher, well, I personally don't know such a problem, not a problem, not a problem, but such a desire to really penetrate the architecture of the application itself, because before that I said I had experience in android, I am now literally transferring my android experience to ios and this is wrong because everywhere all the same patterns are different, I try to write code in projects as it is not written by the

**[13:28] Andrey Sadovykh:** developers, but the problem is, well, in general, I would, as it were, send you more not to the the natural pattern is slice and so on. If there are some components on large projects that communicate with each other, there is some kind of original architecture, maybe it has one or two tags, a signature on the ticket. If something is added, agent there something broke down there a little something some kind of worsened the situation with this dependence in general with contracts, that is, you can also look at the general complication of the dependence of the project

**[14:10] Alexander Isupov:** complication of the graph here is such a clear here it is good that you came together all the same in the topic, although in general, nevertheless, the further steps in the near future, I want to discuss with you what potential

**[14:24] Andrey Sadovykh:** I understand that you need to write your thoughts on articles, that is, why, what is it useful, what is it not useful, what are your thoughts, even in the nonsense, write, it doesn't matter, maybe in one word, two words, three words, write your thoughts about this, even if you read only abstracts or in general, it seemed interesting because

**[14:52] Alexander Isupov:** It can be useful in this context.

**[14:55] Andrey Sadovykh:** Yes, it can be useful in this context. And in fact, by the end of October, I would like to read a sufficient number of articles. And we will make a very short presentation for each student. we will do as I have already written in the group so that, well, first of all, you told about your topic and what others wrote about this topic, and then, as you can see, your solution is still in this kind and as you can see your оценку всякого оценку полезности своего метода или своей своей работы понятно что глупый вопрос

**[15:47] Alexander Isupov:** но спросить какой-то мышку magic номеру для кризиса статьи прочеркнуть противных которому

**[15:53] Andrey Sadovykh:** что вас формировался с опытом да не знаю на самом деле мы это увеличим потом то есть это I think by October, but 20 is definitely necessary to look at. It's not magic, it's just a rule of thumb. Less, probably, could be done more.

**[16:17] Alexander Isupov:** It's clear, always better.

**[16:19] Andrey Sadovykh:** Yes, well, 20, probably, it will be such. It's not a shame to say that I didn't look at these two articles. but it's like in the area of ​​40 you need as far as I remember but it's like that in fact there will be much more articles because there is then at first you need to define the system and with everything, that is, you need to manually pull everything out and look to read and then put on the top already there is snowboarding what is called on the links to go there and further and there it will already be put much more clear

**[16:54] Alexander Isupov:** but in any case I will fight development to teach because I'm not yet because it's necessary to understand then also generally about the national issue of the meeting once a week once in two weeks

**[17:14] Andrey Sadovykh:** weeks yes that is, at will, well, I think not later, but as if here and it is better to reserve in advance because well, yes, it is clear that there are a lot of people and a lot of other things, so it's cool to rely on

**[17:32] Alexander Isupov:** meetings, you can't produce there, let's say if you reserved, then everything is definitely iron, well,

**[17:38] Andrey Sadovykh:** Yes, but only if I have some force majeures. They appeared in the calendar and I don't know about them.

**[17:45] Alexander Isupov:** Well, then we will answer the questions. Thank you for the meeting. And if you have any personal messages, you can write them in the comments.

**[17:54] Andrey Sadovykh:** Yes, yes, definitely.

**[17:56] Alexander Isupov:** Not all questions are for the meeting.

**[17:58] Andrey Sadovykh:** No, no, no. And maybe some questions are easier. Well, these 15 minutes are more than a sync. We don't decide anything at all, just some motivating factor, something to do.

**[18:14] Alexander Isupov:** Yes, I understand. That's all. That's all. There are no more questions. Thank you for the meeting. Have a good evening.

**[18:21] Andrey Sadovykh:** You too.

**[18:22] Alexander Isupov:** Goodbye.

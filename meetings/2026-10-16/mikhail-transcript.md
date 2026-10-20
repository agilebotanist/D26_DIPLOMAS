# Встреча 2026-10-16, 13:07 GMT — Михаил Трифонов

Запись GMT20261016-125841, одна встреча, около двенадцати минут. Тема в начале записи звучит как «безопасность перевода Java-сервисов на виртуальные потоки агентами»; русский VTT тут сильно искажён.

Слова: Whisper (`mikhail-whisper.srt`). Говорящие и таймкоды: Zoom (`mikhail-transcript.vtt`). Склеено
`meetings/merge_transcript.py`, реплики одного говорящего слиты в абзацы. Атрибуция на стыках
реплик приблизительна: Whisper режет по времени, Zoom по голосу, короткие «да», «окей» могут
оказаться у соседа.

**Whisper снова запущен в режиме перевода, а не расшифровки**: текст английский, термины
искажены. Сверено с русским VTT: «safety» и «security» в начале путаются, руководитель спрашивает, в каком смысле безопасность (ресурсная, не кибербезопасность); «Archie-driven modernization» = architecture-driven modernization (ADM); «module to module / module to text» = model-to-model / model-to-text; «Anthology» = ontologies; «model viewing» [неразборчиво, возможно model weaving]; «Stoolza» = tools. Названия, которые руководитель надиктовал в чат, в расшифровке перепутаны, сверять по чату.
Для следующего прогона нужен `--task transcribe`. Реплики-галлюцинации на тишине отброшены.

Часть реплик на 12:30-15:30 в VTT не разобрана; при расхождении верить Whisper.

**[08:00] Mikhail Trifonov:** Thank you.

**[08:25] Andrey Sadovykh:** so tell me why so I have a safety issue with the transfer of services to virtual

**[08:39] Mikhail Trifonov:** streams and agents, I have already started to measure everything, just everywhere in different I saw this article there and 2 found only compared to the success of migration virtual flows through assembly and tests, but it is the security of the front, that is, there is work with memory of the flow pins and some removal of restrictions that are lost during migration, it was not checked anywhere, but security is exactly

**[09:16] Andrey Sadovykh:** what is the point of view of sma consider security from the point of view of the resource which is info cyber security especially the people some kind of sloth or some kind of safety some kind of

**[09:30] Mikhail Trifonov:** security not resources, that is, in virtual flows, it is especially necessary to be careful with memory and during migration, that is, tests can pass and build, and then errors come out in runtime with memory or performance or with load on other services, and here security in the plan not to put applications and safely migrate virtual flows

**[09:58] Andrey Sadovykh:** look there is such an option that part of this migration is to do it in a more determined way, not even through some special prompts or instructions, but through the transformation of the code, that is, it is not everywhere that the agent decides some kind of general plan, but some separate steps that are the most critical, they are determined with the help of some module to module or module to text of transformations. I didn't hear about it. Can it be considered a way of migration? Well, yes. There are a lot of different literatures on migration. There is such a thing as architecture-driven modernization. And different migrations, like on ontologies, for example, model viewing and other things. There is also a large industry for model transformation. I'll put it in the chat now. ADM, Archie-driven modernization, modernization, modeled transformation, then there is modeled text, text, then what else is there? Anthology, Anthologies, Model, Viewing. Well, as it were, it's done by agents, straightforwardly, as it were, that is, you tell him to do this and that, and he does something, right? But the result may not be very determined. It can be limited with different guardrails, but there is no guarantee that it will do something. They create a tool for the agent so that he can run it on time and make the right migration by construction.

**[12:49] Mikhail Trifonov:** Can you tell us how these principles that you have mentioned can be inserted into this topic? I had plans to give them a few clean drafts of the Java Spring project with the problems that will come out if they migrate incorrectly. And with the same prompt to run all these models in different ways. First, without any context, just a prompt.

**[13:31] Andrey Sadovykh:** You are trying to give more specific instructions to the agent, which is not deterministic in nature.

**[13:47] Mikhail Trifonov:** So, instead of the prompt of my base, which I give?

**[13:51] Andrey Sadovykh:** You can improve the agent's work. You can add things to the context, and you can add deterministic tools to it and expand its capabilities.

**[14:17] Mikhail Trifonov:** I had three options so far. I mean, I can give him a prompt without any tips, then a prompt with a small tip, then a prompt with one tool that I found.

**[14:27] Andrey Sadovykh:** It's very boring. Everyone does it like that. But again, this is an instruction. And in order to really make some kind of breakthrough, and in general, it will be better for tokens, and for everything, the result will be better. And in principle, it can be compared with some additional tricks. This is to give him some kind of tool that he knows how to migrate. Or develop such a tool together with the agent.

**[14:58] Mikhail Trifonov:** That is, it is not clear to check how the naked agent can safely migrate.

**[15:07] Andrey Sadovykh:** It's not interesting. There are many tokens, and it's a kind of a solution. I said, I'll migrate and measure. In the middle, they migrate well, in the middle, they migrate worse.

**[15:23] Mikhail Trifonov:** First, how to measure it correctly from the point of view of security.

**[15:30] Andrey Sadovykh:** Again, security. You have some kind of tricky security. It's not cybersecurity, it doesn't mean that it's something.

**[15:36] Mikhail Trifonov:** I think you need another term. I was talking about resources in runtime. Maybe you can say something about performance improvement?

**[15:50] Andrey Sadovykh:** No, no. Safety has many meanings. It's about the workability, that it works all the time, it doesn't break the system.

**[15:59] Mikhail Trifonov:** Yes, it's about resources.

**[16:04] Andrey Sadovykh:** I encourage you to try Stoolza, it will be more useful for everyone.

**[16:10] Mikhail Trifonov:** I can add, in addition to migration with these tools, whether he will lose his productivity, add a token check, how he spent it, where he managed to take the least number of steps.

**[16:28] Andrey Sadovykh:** Stoolzove will be faster both on tokens and, perhaps, even... It's absolutely right. You just need to figure out how to convert one area of knowledge into another.

**[16:43] Mikhail Trifonov:** Good.

**[16:48] Andrey Sadovykh:** well, as it were, this is a more reasonable approach, that is, the agent, as it were, decides there all sorts of prepares here initially input data then checks there and tests are already carried out when

**[17:01] Mikhail Trifonov:** it turned out at the output, here is another question regarding input data, I have it, but so far that there are dozens of simple java spring services in which there are different some ala art and the fact that I saw that you wrote about 30 and more 30 yes well, you will find there in this very github full here but this is a widespread practice to take from github just I thought from the beginning in terms of flows if github rust then there may be some deep problems that the models will not be able to understand at all, but if you write down a large project in

**[17:51] Andrey Sadovykh:** lmk, it will burn the whole context and everything will die out, but if we just need to determine there input is much easier for him.

**[18:01] Mikhail Trifonov:** In the sense that it is not the whole project that is being scammed.

**[18:12] Andrey Sadovykh:** Look, when he needs to replace something, he generates a bunch of code. He has a huge flow of information on input and on output. That is, it's a bunch of tokens at once. And he's still thinking about something inside. but if we say that you have a task that is here well, as it were, you can explain it and plus say here to do such a tool input here is such a compact config file there, for example, yes, or some description and output also something like this compact, then, accordingly, input to output and a lot of tokens comes

**[18:46] Mikhail Trifonov:** but that is, if we direct it to the place where it needs to something to correct it will not be like a hint

**[18:53] Andrey Sadovykh:** What do we need it for? Do we need to check how smart he is or do we need to make migration faster, better and more automated? It's pointless to say whether it's smart or not. We need migration. If you have a migration task, and you need to convert a lot of services to a new framework, then it's a bit like that.

**[19:33] Mikhail Trifonov:** Yes, yes.

**[19:35] Andrey Sadovykh:** On the contrary, the dumber it is, the better it is. We'll make it cheaper. Well, with the right approach, you can run everything on small models.

**[19:48] Mikhail Trifonov:** Well, I...

**[19:50] Andrey Sadovykh:** And when you don't feed it with contexts, and give it a very short UZU, which it can run, it can be done much faster on small models.

**[20:03] Mikhail Trifonov:** Well, yes, but you still need to check the size on several models.

**[20:09] Andrey Sadovykh:** Of course. First, you need to make sure that you can do it on a small model. For this, you need a comparison. You need to understand the limitations of the method. For example, you can only cope with a large model in this form, and with such a small model you can cope with the same quality. The quality needs to be measured.

**[20:31] Mikhail Trifonov:** Okay, yes. I have already collected the sets of models. Okay, that's all for questions.

**[20:43] Andrey Sadovykh:** Okay, then goodbye.

**[20:48] Mikhail Trifonov:** Thank you.

**[20:49] Andrey Sadovykh:** Good luck.

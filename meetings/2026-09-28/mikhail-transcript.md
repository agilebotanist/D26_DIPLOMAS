# Встреча 2026-09-28, 15:19 — Михаил Трифонов

Собрана скриптом `meetings/merge_transcript.py`: слова из `mikhail-whisper.srt`, говорящие и
таймкоды из `mikhail-transcript.vtt` (Zoom), реплики одного говорящего слиты в абзацы.

**Whisper запущен в режиме перевода, а не расшифровки**, поэтому текст английский, а
термины искажены переводом: SAST становится «state elite» и «statelites», Qwen2.5-Coder —
«QN5 coder», false positive — «Fox positive», виртуальные потоки — «virtual flows»,
литературный обзор — «political review». Смысл восстанавливается, отдельные названия — нет.
Сверять термины по русскому `mikhail-transcript.vtt`. Для следующего прогона нужен
`--task transcribe`.

Реплики-галлюцинации Whisper на тишине («you», «Продолжение следует...») отброшены.

**[02:00] Andrey Sadovykh:** Mikhail, good evening.

**[02:21] Mikhail Trifonov:** tell what they did what questions to ask well, as I wrote, I decided to change the topic a little because then here about the hodg profit or code interest, it does not give. I wanted to switch to the topic that is currently relevant in Java, these are virtual flows. And the problem that was created with them is that there is a pool of these flows in the Java application, and there is a pool of connections for database. And there are different articles where they advise to balance these two pools in different ways, that is, virtual flow flows can be paid a lot and paid in computing power so a lot of pool of connection to the database it needs to be controlled and paid so it is impossible in some articles they write about the fact that it is necessary, on the contrary, to increase the virtual flow pool, some write that it is necessary to reduce and and are calculated differently using several formulas. I want to try to measure the proposals in different articles and upload the application on a real stand and check the actual load and find some kind of correlation between these formulas and how to calculate the size of the virtual flow pool To communicate with the database as effectively as possible, but at the same time not to put it there Because many articles have a little bit contradictory phrases

**[04:22] Andrey Sadovykh:** ok look well, this whole series of lines has been applied for a long time, for a long, long, long time, not the first decades of java, it's exactly because there is something new there or some

**[04:46] Mikhail Trifonov:** new context was formed itself the theory of the streams yes it is not new that is, I saw a very ancient but yes, but the fact that the new ones are here in the java, these virtual streams that have become cheap to create relative to the fed streams and everyone began to create them, but there are a lot of them for each, but at the same time, while performing actions on the flow, there may be some interaction with the database where the connections are not so cheap. But it's interesting to calculate what the pool should be,

**[05:27] Andrey Sadovykh:** the maximum amount of flows. Do you want to come up with some kind of optimization technique

**[05:35] Mikhail Trifonov:** compare it with something already known to me initially I was thinking about checking how much the formula from this theory of sequences is applicable now to virtual flows, well, for example, they are not applicable all the time, they are

**[05:51] Andrey Sadovykh:** such mathematics, for example, concrete to everything applicable, but we ourselves are very iron and concrete math there just so that it is not applicable it will do something that I don't know what you see, well, maybe they haven't applied it yet, but to this one, which you say, well, and mathematics, probably, the list is not worth it for you, well, that is, apply before the application to study before the comparison with something with some standard ways of pool optimization, you can probably take it, you will cope with the math, it's probably difficult to cope with it, it's good to throw it off the

**[06:40] Mikhail Trifonov:** view, but in fact not very much, but I wanted to go to math, it's something like that, it's applied to check it all, that is, I understand that I will not forbid the formula there, it's very

**[06:51] Andrey Sadovykh:** simple formulas there yes and the values are different everything turns out but there are very large

**[06:59] Mikhail Trifonov:** tricks if you compare well, I would still just like to delve into this problem that there are virtual flows that are easy to use for creation there is a pool of bd connections that are complex, точнее который дорогой и по исследовать ну как наверное делаете в общем делаете все правильно

**[07:30] Andrey Sadovykh:** то есть вы правильно ждать и смотрите можем мы можем так сделать можно с двух концов смотреть всякие экспериментальные результаты то есть сравнение пула там не знающим и какого-то вида pool there are different types of pools here you can compare with this here and maybe some with some technical obligations optimization of pools to compare look maybe the theory will give some additional properties that will help improve the organization of these pools well, or just compare to show theory and what is happening in practice, but there is a good topic, it is quite magical, there is firstly a candle notation, that is, it is necessary to write a candle, then various formulas there service word there are such different full circle here we have a lecture on the workshop master course 1 about this second class here and plus there is still a cool tool for it is more academic course about modeling the day it is called oh it is known I don't remember java modeling jim t it seems jim jim jim t it seems so

**[09:07] Mikhail Trifonov:** thank you good then it turns out if you summarize it more to deepen in the comparison of optimization of all sorts and comparison of techniques to achieve an optimal balance, but first you need to read

**[09:26] Andrey Sadovykh:** most likely someone already figured out to apply to everything I apply there to microservices there to various resources we need to everything that is, this is such a famous tiff sequence of those who are busy

**[09:42] Mikhail Trifonov:** I was just hooked by the fact that I just found a couple of articles and there were contradictory facts, that is, from them these same theories were applied, someone there went through the Erlang formula in general and they wrote that you need to increase once we have cheap virtual flows, others wrote that it is impossible to increase because there is already in real time schedule it was a little gone, that is, they said that you cannot increase it, you need to take hold of less then they will reuse the connection of the pd-shk but I also thought that there could be something to follow, well, there will be the most

**[10:26] Andrey Sadovykh:** subtle question correctly, you applied the formula and on the right conditions, because there are formulas they have when you can apply them when not very many can be practically everywhere but there are still some conditions there for the arrival of requests there stochastic stochastic in general there are such different things such quite mathematical, so the possible difficulty will be именно вот как раз снова влагающей математикой хорошо буду смотреть сторону да ну посмотрела же были у меня на сквере да ну а вот на сайте поиска рыбок посмотреть там киньте there is there is a lesson on this theory so I'll throw it all to you even so now I'll so select material I will go to the camps of the series here and here and there is what we talked about what

**[11:47] Mikhail Trifonov:** on the master's semester well yes yes yes of course I remember that there is the same site and the master's

**[11:55] Andrey Sadovykh:** there are links to other pages

**[12:01] Mikhail Trifonov:** Thank you, I see familiar formulas.

**[12:06] Andrey Sadovykh:** Oh, something fell off. Yes, yes, yes, GMT, Java Modeling Tools. well, and in principle, that's what there are sources, they basically have me in some form, that is, I will also look for if they are not ancient there from the session of 78 years, perhaps 78 years old and even older of course there is also an older phone 53

**[13:07] Mikhail Trifonov:** 61 I see yes good

**[13:14] Andrey Sadovykh:** understand such a interesting topic, but in fact, if you pump your skills in this, then

**[13:28] Mikhail Trifonov:** but it was still interesting to me that I did not meet her at work with her in some kind of work we have now this process all on the virtual flow of redoing went and the system was faced with the kind of base of data to immerse in it, I read a little about it and by the way, yes, books, books,

**[13:50] Andrey Sadovykh:** I'll look for them somewhere here ok so so everything is so here is 6 and how much there is everything 8 there are still books now yes also books and what I have so there was a book still interesting there gorilla capacity planning about alice in application

**[15:13] Mikhail Trifonov:** detail scale

**[15:17] Andrey Sadovykh:** so now so this may still be useful so what else do we have first we look and it will be useful so that is, and vodka is this or is this a shalec and the theme for the performance is also suitable for the

**[15:51] Mikhail Trifonov:** list

**[15:55] Andrey Sadovykh:** it's all about statistics and fashion fashion meeting I'll give you a new one. Forecasting, discrete event, Forecasting Address, Mark of Chains. I'll send it to you, but I think it will be useful. The last one is performance queuing. It can be useful. Qt, this is good. Well, yes, QM series, fundamentals. Well, something like that.

**[16:49] Mikhail Trifonov:** I will try to standardize them.

**[16:53] Andrey Sadovykh:** The last one is about QM series. But there are 500 pages. To start with. Okay. What else? No pain, no gain.

**[17:11] Mikhail Trifonov:** Yes. I will read it.

**[17:16] Andrey Sadovykh:** Yes, read it.

**[17:18] Mikhail Trifonov:** Thank you.

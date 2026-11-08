Subject: SNE bachelor theses, chapters 1-2: grades and cross-check with your comments

Dear Pierre-Philipp,

Thank you for the grades and the comments. The assessment is limited to chapters 1 and 2; the abstract and any later chapters are not assessed at this stage. I read the three chapter 1-2 drafts independently of your feedback and then compared the two. This is what I found and what I propose.

Grades

Letter thresholds are A 90-100, B 80-89.99, C 70-79.99. Each grade below is the mean of my text-only score and your grade scaled to 100, plus a flat 9 points to reflect that these are drafts of the first two chapters. The text-only scores before any blending were 62, 54 and 56. The students received the grade, the letter and the feedback reproduced in the annex, not the arithmetic.

Peter Zavadskii: 85, B. Your grade was 9/10, mine for the text alone was 62.
Daniil Mayorov: 76, C. Your grade was 8/10, mine for the text alone was 54.
Arsen Galiev: 57, below C. Your grade was 4/10, mine for the text alone was 56.

Where we agree

On Arsen we are in agreement. The disk I/O idea is relevant, but the storage architecture is never discussed. The thesis names it once and then moves on. It does not say where a container's data lives (local disks, persistent volumes, Ceph or Longhorn, converged storage), what happens to that data when the container is rescheduled, or how a per-node disk signal behaves when the I/O goes to a remote volume. Beyond that, the text fixes no orchestrator, workload generator, metric, baseline or number of runs, and it has 13 references, six of them documentation pages. I support your three options (revise the storage architecture, evaluate Nomad, or build a small scheduler without the disk resource) and would ask Arsen to choose one in writing before the next draft.

On Peter and Daniil your comments about diagrams and focus match my reading. Peter has five research questions plus an adaptive prototype and an optional MAP-T extension, which is too much for one thesis, as you said. Neither thesis has a single figure or table, and a testbed diagram would help both.

Where I am lower than you

Peter. I score the technical content highly: the sender-host criterion is clear, DNS lookup, connection and transfer times are separated, tail latency is reported, and RFC 8219 and RFC 9693 are used as method anchors. All 12 references checked out. My deductions are about completeness at this stage. It is not explained why a dual-stack host would use NAT64 instead of native IPv4. There is no baseline of dual-stack with a local caching resolver and no translation, so any gain from an independent DNS64 cache cannot be separated from the translator. 464XLAT (RFC 6877) is excluded without an argument, although it is the standard host-side mechanism for the same scenario. Section 2.7 on DNS caching has no citations (RFC 2308, RFC 8767, RFC 6724 and RFC 8305 would be a start). The testbed has no hardware, software versions, traffic generator, repetition count or numeric success criterion. The title promises a performance analysis while the aim is to design and evaluate an adaptive mechanism.

Daniil. The protocol content is sound and I agree with your remark about the explanations: mapping and filtering follow RFC 4787, the hole-punching conditions are stated correctly and the standards lineage is right. The gap to a good thesis is elsewhere. All 16 references are RFCs, so chapter 2 explains the standards but reviews no experimental or measurement work and states no research gap. The method section is two sentences, with no tools, topology, NAT-type matrix or metrics. Tasks 1 to 5 are all "learn how X works". There are also a few technical slips: address-dependent mapping is described as "a unique external port per external IP", NAT is introduced through static and dynamic subtypes rather than Basic NAT and NAPT, and TURN is said to be needed whenever one side has address-and-port-dependent mapping, which holds only if the peer's filtering does not allow punching. I fully agree with your advice to narrow the topic to acceptance testing of NAT-T scenarios or to the abuse of hole punching.

Two questions

You mention that you sent more detailed feedback and recommendations to the students. Could you forward me a copy, so that I can check that my feedback to them (annex) does not contradict yours?

If you think I weight completeness too heavily for Peter and Daniil, tell me. Using your numbers alone would give Peter 90 (A), Daniil 80 (B) and Arsen 40 (below C), and I am happy to move towards those for the first two.

Best regards,
Andrey

Annex: grades and feedback sent to the SNE students

The students received the text in Russian. It is reproduced here in English translation.

Peter Zavadskii (p.zavadskii@innopolis.university): 85/100, B

Strengths: a clear "sender-host" criterion with Border Relay and intermediate translators explicitly excluded; DNS lookup, connection and transfer times measured separately; tail latencies; RFC 8219 and RFC 9693 used as methodological anchors; all 12 references verified; neat reference formatting. The consultant graded the work 9 out of 10.

To improve:
1. Justify why a dual-stack host would use NAT64 instead of native IPv4, and give a scenario (for example an IPv6-only access network).
2. Add a baseline configuration: dual-stack with a local caching resolver and no translation.
3. 464XLAT (RFC 6877) is excluded without an argument, although it is the standard mechanism for the same scenario.
4. Section 2.7 has no references at all. Candidates: RFC 2308, RFC 8767, RFC 6724, RFC 8305, Lencse's work on DNS64, other NAT64 and CLAT implementations. At least 20 sources in total.
5. A concrete testbed (hardware, Jool and Unbound or BIND versions, traffic generator), the number of repetitions, and numeric success criteria.
6. Five research questions are too many; keep MAP-T as an extension. Align the title, aim and research questions (performance analysis versus an adaptive mechanism).
7. Add a testbed diagram and a comparison table of the mechanisms, and cut repetition. The university-template title page is missing.

Daniil Mayorov (d.mayorov@innopolis.university): 76/100, C

Strengths: correct separation of mapping and filtering following RFC 4787; a correct classification of the old NAT types; hole-punching conditions stated accurately; the correct standards lineage (3489, 5389, 8489, 5245, 8445); a section on IPv6. All 16 references exist. The consultant graded the work 8 out of 10.

To improve:
1. Chapter 2 retells the RFCs and contains no related work. Add Ford et al. (USENIX 2005), Halkes and Pouwelse, measurement studies of WebRTC, libp2p and Tailscale, and NAT classification studies; end with an explicit research gap and a comparison table; reach 20 sources.
2. Sections 1.5 and 1.7 are two or three sentences. Describe the testbed topology, the tools (coturn, netns, iptables, libnice or aiortc), the NAT-type matrix, the metrics (connection success rate, setup time, RTT, relay load) and the number of repetitions.
3. Tasks 1 to 5 in section 1.3 are phrased as "learn"; rewrite them as deliverables and align them with the research questions. Research question 2 is written in the first person. The bonus security question should either be included in the aim or removed (the consultant suggests choosing one: acceptance testing of NAT-T scenarios, or abuse of hole punching).
4. Imprecisions: the definition of address-dependent mapping, the NAT subtypes (Basic NAT and NAPT are needed), and the condition under which TURN is required.
5. Data for section 1.1 (share of CGNAT, WebRTC traffic).
6. Language and calques ("NAT traversing", "NATP"); add a testbed diagram and a table.

Arsen Galiev (a.galiev@innopolis.university): 57/100, below C

Strengths: disk capacity and I/O rate are correctly separated; IOPS, throughput and latency are explained; the review of earlier work is critical (DRAPS does not prove a gain); references are tidy. The consultant noted that disk as a scheduling resource is relevant and possibly novel.

To improve:
1. Main problem: the storage architecture is not discussed. A container may live on any node, as a single instance or as several replicas, and the storage is built on the same nodes (convergence). The thesis needs a section on local, network and converged storage, persistent volumes and CSI, and the consequences of rescheduling, together with an explicit choice of assumption.
2. Choose a direction, as the consultant proposed: disk I/O with a revised storage architecture; or Nomad, checking whether it can handle diverse resources; or your own simple scheduler based on existing metrics without the disk resource.
3. In section 1.1 fix the orchestrator, the workload generator (fio, YCSB), the metrics (IOPS, p99, variance of node load), the baselines, the number of repetitions and the definition of done.
4. Bring the literature to 20 peer-reviewed sources (cgroup v2 io.max, PSI, the scheduler framework, storage-aware scheduling, noisy neighbours) and state what [7] lacks, so that the work is not a repetition of it.
5. Shorten sections 2.1 and 2.2 (Raft and how a scheduler works) and add a comparison table of [5], [7], [12] and [13].
6. Correct the date on the title page.

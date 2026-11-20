
From the origin of the universe to the role of the genome, humans crave answers to the big questions. Yet scientific discovery has always been constrained by human limitations: too little time, too few resources, and not enough information.

Now AI is removing those barriers, giving every scientist access to computational power and tireless research support unimaginable five years ago.

AI doesn’t just speed up discovery. It can facilitate collaboration across disciplines, review literature, generate hypotheses, analyze data, and validate theories. In almost every field, from bioengineering to medicine to space exploration, AI is poised to help researchers find patterns in massive datasets, run studies, and interpret results at unprecedented scales.

The technology carries risks: bias, data quality issues, inequitable access. Teams must establish guardrails to ensure models provide real scientific value and that the benefits of science AI are broadly shared.

Still, these new tools are already empowering scientists to push the boundaries of what’s knowable, helping us to be even more human: more curious, more informed, and more capable of unlocking the mysteries of our world.

Here at the [Stanford Institute for Human-Centered AI](https://hai.stanford.edu/) (HAI), faculty are embracing AI to explore scientific discovery from the physical and biological sciences to engineering and policy.

### Pushing Boundaries in Biology

![](/_next/image?url=https%3A%2F%2Fhai.stanford.edu%2Fassets%2Fimages%2Fbrian-hie-by-sf-photo-agency.jpg&w=3840&q=100)

Brian Hie, assistant professor of chemical engineering and Stanford Data Science faculty fellow, helped create Evo 2, the largest DNA language model ever trained for biology, with 40 billion parameters across 9 trillion base pairs. | SF Photo Agency

Biology has always been a study of observation and slow experimentation; AI is now significantly speeding that process by allowing virtual experiments that can predict gene mutations, design new sequences, and help us better understand disease.

At the forefront of this transformation is Evo 2, a DNA language model trained on genetic data across all domains of life – including humans. Introduced in February 2025 by a team including Stanford scholar [Brian Hie](https://profiles.stanford.edu/brian-hie), Evo 2 is the largest model ever trained for biology.

With initial funding from a [Hoffman-Yee Research Grant](https://hai.stanford.edu/research/grant-programs/hoffman-yee-research-grants), the team of engineers, geneticists, and neurobiologists trained Evo 2 on 9 trillion base pairs and 40 billion parameters.

The model operates like a chatbot, except instead of entering a series of words, the user prompts it with a string of DNA letters representing the beginning of a gene sequence. Evo 2 then autocompletes the gene, sometimes as an exact replica of the living being, other times with suggested improvements. Scientists can analyze the mutated gene sequences for possible insights relating to human health and more resilient agricultural crops, for example.

“Evo 2 illuminates complex biological processes, such as protein biochemistry, enabling us to accelerate the study of gene function and disease,” says [Hie](https://profiles.stanford.edu/brian-hie), assistant professor of chemical engineering and Stanford Data Science faculty fellow. “In a short period of time, our team has built the largest fully open language model ever trained, the first AI-generated genomic database, and the first AI-generated viable genomes – all important steps on the journey to design new genetic sequences with specific functions of interest.”

### Using AI to Model a Human Cell

![](/_next/image?url=https%3A%2F%2Fhai.stanford.edu%2Fassets%2Fimages%2Femma-lundberg-by-christine-baker.jpg&w=3840&q=100)

Emma Lundberg, associate professor of bioengineering and of pathology, is leading a team building a foundation model that simulates human cells to accelerate drug discovery and personalized medicine. | Christine Baker

Scientists have dreamed of modeling the human cell ever since Robert Hooke discovered the fundamental unit of life in 1665. With AI’s ability to learn from vast amounts of biological data, the goal may be within reach.

A team at Stanford is collaborating to build a human-centered foundation model that can simulate human cells to accelerate drug discovery and personalized treatment for disease.

“We are not the first generation to think about modeling cells, but with AI, the opportunities are completely new,” says [Emma Lundberg](https://profiles.stanford.edu/emma-lundberg), associate professor of bioengineering and of pathology at Stanford.

Imagine testing experimental drugs on a digital twin of one’s cells before taking a prescription. A patient could understand the drug’s efficacies and side effects before swallowing a single pill. It’s a bold vision that comes with a host of technical challenges.

To successfully build a virtual cell, the team must overcome several challenges. First, the model needs to recognize different types of biological data, including DNA/RNA/protein sequences, protein structures, cellular images, and scientific literature. It also needs to understand different biological units and how they connect across scales, from molecules to cells to tissues, organs, and whole organisms.

Second, the virtual cell model needs a chat interface for biologists to interact with the data and upload their own datasets for analysis. To meet this need, the team developed Biomni (see below).

The hurdles are steep, but if they succeed, the team will create a valuable new tool for the field. “Generative models are incredible equalizers when it comes to lowering the cost of experiments. “For example, AlphaFold \[the open-source AI system from Google DeepMind that predicts a protein’s 3D shape from its amino acid sequence\] has democratized access to structural biology in recent years. With our virtual cell foundation model, we hope to make more such generative tools available to every cell biologist around the world,” Lundberg says.

### AI as Co-Scientist

![](/_next/image?url=https%3A%2F%2Fhai.stanford.edu%2Fassets%2Fimages%2Fjure-leskovec-by-christine-baker.jpg&w=3840&q=100)

Jure Leskovec, professor of computer science, co-created Biomni, an AI research assistant that's been used by 15,000 scientists to automate 100,000 different biomedical workflows. | Christine Baker

Massive datasets, complex experiments, and a growing list of analytical tools create a fragmented research process that hinders biomedical innovation. Agentic AI gives scientists a way to scale their expertise.

Scholars from Stanford, Genentech, Arc Institute, the University of Washington, Princeton, and the University of California, San Francisco, created [Biomni](https://biomni.stanford.edu/), a biomedical AI agent that collaborates with human scientists on everything from gene prioritization and drug repurposing to rare disease diagnosis, microbiome analysis, and molecular cloning.

Biomni pulls together hundreds of specialized tools, databases, and software packages into a unified scientific research environment. With reasoning capabilities and the ability to write Python code, the agent can work through tasks on its own.

Users can prompt Biomni to design a wet-lab experiment, automate clinical decision support, provide biomedical data analysis, or review a body of scientific literature. They can even ask it to generate a new hypothesis – and the model doesn’t need predefined templates or task-specific tuning to help.

“Biomni is a true collaborator,” says [Jure Leskovec](https://profiles.stanford.edu/jure-leskovec), professor of computer science at Stanford. “It knows biology, is trained on every paper ever published, and can do complex workloads autonomously.”

So far, 15,000 scientists have asked Biomni to automate 100,000 different scientific workflows, saving countless human research hours and making it, in Leskovec’s words, “the most-used AI scientist on the planet.”

### Novel (If Impractical) Ideas

What happens when you ask AI to do one of the most human parts of science – come up with the next great question? Large language models can generate endless ideas in seconds, but it’s not obvious whether these ideas are valuable or simply voluminous.

To evaluate AI’s research brainstorming capability, a team of Stanford scholars designed the first [head-to-head comparison](https://arxiv.org/abs/2409.04109) between highly qualified natural language processing (NLP) researchers and a simple AI ideation agent.

They recruited 100 human experts to contribute ideas and blindly review a mix of human-written and AI-generated ideas. The experts reviewed 49 ideas covering seven research topics – including bias, coding, and safety.

To ensure a fair comparison, the scholars gave both human participants and the agent the same topic description, idea template, and example submission. The agent, equipped with paper retrieval, idea generation, and idea ranking capabilities, was prompted to generate 4,000 seed ideas on each research topic.

The expert reviewers evaluated the idea itself, the write-up that communicated the idea, and an expert evaluation of the write-up. Judges then scored each idea based on novelty, excitement, feasibility, and expected effectiveness.

The result? Human experts judged AI-generated ideas as significantly more novel compared to human ideas, but with a catch: Many of the ideas weren’t feasible.

“In the end, we found that while LLMs have excellent technical creativity, humans come up with more practical proposals, given they are grounded in existing research,” says [Chenglei Si](/people/chenglei-si), a third-year PhD candidate in the Stanford NLP Group and lead author of the study. Although AI-generated ideas proved more novel and exciting, Si adds, the LLM was not capable of self-evaluation and lacked a diversity of ideas when compared to human responses.

> In the end, we found that while LLMs have excellent technical creativity, humans come up with more practical proposals.

##### — Chenglei Si

##### PhD candidate

In [an additional study](https://arxiv.org/abs/2506.20803), Si and colleagues evaluated AI proposals based on research outcomes, which were not factored into the first study. This follow-on work revealed a sizable gap between AI’s ability to ideate and execute. With project execution as part of the assessment, humans prevailed.

“Many researchers are excited about a future where autonomous agents generate and validate new scientific ideas. But first, we need a way of teaching LLMs what factors make an idea not only novel but also viable and effective,” Si says. For now, AIs continue to add value as virtual assistants that help human scientists analyze problems and hypothesize answers from all possible angles.

Across the Stanford community and beyond, scientists in every field are finding new ways to accelerate and enhance their research with AI. With its abilities to find patterns in massive datasets, generate new ideas rapid-fire, and run scenarios that would be impossible to set up in a lab, AI could be the ideal partner to help humans understand our world.

### Decoding the Universe

![](/_next/image?url=https%3A%2F%2Fhai.stanford.edu%2Fassets%2Fimages%2Frisa-wechsler-by-andrew-brodhead.tif&w=3840&q=100)

Risa Wechsler, professor of physics and director of the Kavli Institute for Particle Astrophysics and Cosmology, leads the Center for Decoding the Universe, which develops AI methods to extract insights from massive astronomical datasets. | Andrew Brodhead

Scientists working at the frontier of astrophysics are using AI to decode the universe with remarkable precision. Current research focuses on two key initiatives: Some teams are working to model the universe, using computer simulations to predict changes over time; others are analyzing vast datasets generated by powerful telescopes to create a detailed map of the cosmos.

Astronomy has always been a data-rich field, but a new sky survey launching this year at the [Rubin Observatory](https://rubinobservatory.org/) in Chile presents an unprecedented challenge. As the telescope maps the southern sky, it will generate millions of digital images and push real-time alerts to thousands of scientists all over the world – every night for 10 years.

“This survey promises to give us a new understanding of how the universe evolves over time, but discovery in this field depends on our ability to use all the available data, and we’re nowhere close to that,” says [Risa Wechsler](https://www6.slac.stanford.edu/about/our-people/risa-wechsler), a professor of physics in the Stanford School of Humanities and Sciences and director of the Kavli Institute for Particle Astrophysics and Cosmology ([KIPAC](https://kipac.stanford.edu/)).

This is where the [Center for Decoding the Universe](/centers-labs/center-for-decoding-the-universe) comes in. As a joint initiative between KIPAC and Stanford Data Science, with Wechsler at the helm, the center brings together experts in astrophysics, statistics, and computer science to develop new methods for extracting insights from massive, multimodal datasets. Affiliated faculty are studying both how to use AI agents in complex scientific workflows and how to build frontier models capable of pushing the boundaries of scientific inference.

“The next five years are going to be tremendous,” Wechsler says. “We may discover the mystery of dark energy, or what happens when stars explode. It’s an entirely human endeavor – the scope is large, and we don’t know the end of it.”

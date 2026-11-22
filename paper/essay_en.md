# Correct but Ungrounded: Reflections on Chatting with Lu Xun through RAG

**Group:** Zhang Min and Liu Chenyang
**Course:** DHG508, Assignment 2, Part 2
**Date:** 23 November 2026
**Word count:** approximately 1,980 words (including headings)

## 1. Figure and corpus

RAG lets a model work from a set of texts instead of training memory alone. We wanted to see whether that changes how a historical figure answers questions. We chose Lu Xun (1881-1936) because his collected works are large, public domain, and familiar to us.

Part 1 gave us 54 volumes, about 4.4 million characters. The index used 32 of them, about 2.63 million by the library's count: three novels, two prose and memoir collections, seventeen essay collections, two literary histories, two preface collections, five compilations or editions, and the letters in Liangdi Shu. The other 22 are memoirs and biographies by Xu Shoushang, Xu Guangping, Zhou Zuoren, Xiao Hong and others. We left them out because we wanted the first person to be Lu Xun, not a biographer.

Zhu An (1878-1947) was the woman Lu Xun married in 1906. The marriage was arranged by his mother, and the couple lived in separate rooms for most of their marriage. Lu Xun supported her financially and wrote very little about her in his published work. Most of what we know about her comes from the memoirs and biographies we had excluded. We asked about her because she is a case where the published archive is silent but the memoirs are not. The index had nothing to retrieve, so the corpus had no answer before the model spoke.

The corpus is less clean than "32 works by Lu Xun" sounds. Five of the volumes are compilations or editions of other people's texts, and Liangdi Shu is a collection of letters between Lu Xun and Xu Guangping, so the first person moves between two writers. Those six volumes are about a quarter of the indexed text. The files are web transcriptions, not critical editions. They keep book headers, chapter rules, editorial notes and lacunae, and some headers are cut off. Front matter is indexed. We did not check the text against printed editions. It is readable and citable, but it is a mixed archive, not a single voice.

The persona prompt made it worse. It told the model to answer in the first person, keep Lu Xun's tone, use "the materials you have read and your known life," and say "I don't know" when uncertain. The phrase "known life" gives the model permission to use what it remembers about Lu Xun's biography. That is what happened with Zhu An.

## 2. Method

We asked five core questions. The first was about the "iron house" in the preface to Nahan, testing whether the system could rebuild an argument. The second asked why Lu Xun opposed young people reading old Chinese books, testing a stated position and its source type. The third asked about Zhu An, where the corpus was silent. The fourth asked what Lu Xun remembered about Fujino, testing detail recall and retrieval precision. The fifth asked about unemployment and pensions, testing whether the model would import modern concepts into a 1936 voice. We also ran a May Fourth check and the unemployment question in simple and agent mode.

Table 1 lists the settings. The only substantive change was the embedding model. OpenRouter's embedding endpoint returned HTTP 404, so we rebuilt the index locally with BAAI/bge-m3 (1024 dimensions) on an Apple M5 through MPS. The chat model stayed on OpenRouter, so questions and retrieved passages went to a cloud service even though the index was local.

**Table 1. Settings.**

| Setting | Value | Note |
|---|---|---|
| Application | HistFig, local FastAPI and SQLite | |
| Chat model | `z-ai/glm-5.3-flash` via OpenRouter | Generation in the cloud |
| Embedding | `BAAI/bge-m3`, 1024 dimensions, local MPS | Changed |
| Chunking | 1,000 Chinese characters, 150 overlap | Kept |
| Index | 3,268 passages | |
| Retrieval | hybrid vector and BM25, RRF k = 60 | Kept |
| `top_k` | 5 | Kept |
| `candidates` | 30 | Kept |
| `min_similarity` | 0.2 | Kept |
| History | 20 messages | Kept |
| Agent steps | up to 5, 4 used | Kept |
| Temperature | 0.7 | Kept |

Each exchange started in a new conversation. We exported the answer, citations and retrieved passages, then wrote a verdict. We used four labels: success, partial, mixed and clear failure. The conversations and error log are in the repository, with the Chinese originals and part numbers.

## 3. Evidence

**The iron house.** We asked, "What did you mean by the iron house in the preface to Nahan?" The answer said the iron house was a figure for Chinese society, "a suffocating darkness," and it separated two claims: the house is almost impossible to destroy, and yet the few people who are awake leave room for hope. The retrieved passage was the original figure: "Imagine an iron house without windows, absolutely indestructible, with many people inside asleep, soon to suffocate." The answer also used the line "Despair is as much an illusion as hope" from the Nanqiang Beidiao Ji. All five passages were relevant, and the citations [1][2][5] matched the claims. The answer rebuilt the argument and the exchange with Jin Xinyi. This was a success.

**Youth reading.** We asked why Lu Xun opposed young people reading old Chinese books. The answer gave the famous line: "Read little, or indeed nothing, of Chinese books; read foreign books." The position is correct, but the search did not retrieve Lu Xun's original essay in Huagai Ji. All five passages were polemics, and three were opponents' rebuttals. One of them, Shi Zhecun's rebuttal, quotes Lu Xun as saying, "I think one should read little, or indeed nothing, of Chinese books." The source type was wrong, and the original context, general readers versus specialists in ancient literature, was missing. We marked this partial. A correct answer can hide a failed search.

**Zhu An.** We asked, "What was your relationship with Zhu An?" The answer sounded personal. It said the marriage was "a gift my mother gave me," that love was something Lu Xun did not know, that a telegram in the bingwu year brought him home to a wedding, and that the couple lived in separate rooms. None of this had a citation. The corpus contains no "Zhu An" at all. The five retrieved passages were not about her. The top hit was a mock "marriage advertisement" in the Supplement to the Jiwai Ji Shiyi, placed by a self-described "Mr. Zhu" seeking a wife. The failure had three parts: the sources were absent, the search returned noise instead of admitting silence, and the generator used parametric memory to fill the gap. It may be true, but it was not grounded in the corpus. This was a clear failure.

**Fujino.** We asked what Lu Xun remembered most about Fujino. The answer quoted the essay: "His character was great in my eyes and in my heart, though his name is not known to many." The line is in Zhaohua Xishi, part 40. The other four were two prefaces and unrelated text from Qiejieting Zawen and Liangdi Shu. Only one of the five was direct evidence. The answer was accurate, but the citations made it look better grounded than it was. Readers who know the essay accept the details; readers who do not see five citations and assume support. We marked it partial.

**Unemployment and pensions.** We asked about high unemployment and a social insurance system that cannot cover the cost of old age. In simple mode, the model began with "I died in 1936; I do not know what happened after that." It did not invent statistics. It then treated "social insurance" as an institution Lu Xun already knew, and it reasoned about it in his voice. Four of the five passages were relevant. One passage from Fen says, "the fundamental method is only to reform society." The fifth, from Erxin Ji, was translation criticism and unrelated. In agent mode, the search improved. All five passages were relevant. The answer still used "involution" and "lying flat," and it treated social insurance as familiar. The better search produced a more fluent modern answer, not a better historical one. We called the simple version mixed and the agent version a failure of register.

The May Fourth check was a second success. It gave a qualified verdict: "on the surface it was somewhat successful." It separated the May Fourth movement from the later "New Culture Movement" label, stayed within Lu Xun's lifetime, and used five relevant passages. The system can handle a qualified judgment when the corpus and question cooperate.

## 4. Analysis

The iron house and May Fourth were correct and well grounded. Youth reading and Fujino were correct but weakly grounded. Zhu An was unsupported and ungrounded, and the agent unemployment answer had relevant passages but sounded modern. The correct but weakly grounded case is the most dangerous because it looks trustworthy. Fujino is the clearest example: the answer is accurate, the citations are there, and only one passage supports it.

Three things went wrong. The corpus came first: we excluded the memoirs that discuss Zhu An, so the question had no source; five indexed volumes are compilations or editions, and Liangdi Shu is co-authored, so the voice was mixed. Retrieval added a second problem: with top_k at 5 and min_similarity at 0.2, the system almost always returns five passages, even when none is relevant; 1,000-character chunks make each passage broad. The third problem was generation: the persona prompt allows "known life," the temperature is 0.7, and nothing requires every factual sentence to be cited.

Ted Underwood, Laura K. Nelson and Matthew Wilkens, in "Can Language Models Represent the Past without Anachronism?" (2025), show that prompting a contemporary model with period prose does not make it write like the period, and fine-tuning does not fool readers. That fits the agent answer. The search returned five relevant passages, but the model still said "involution" and "lying flat." The passages came from the period; the model's style did not. Thierry Poibeau, in "What Do Historical Language Models Model?" (2026), argues that historical language models model surviving archives, not past minds or populations. Our corpus is one of those archives. It preserves the published Lu Xun and leaves out the memoirs that discuss Zhu An. When the archive is silent, the model falls back on its wider training memory. The Zhu An answer is a plausible first-person text, not a retrieval-based biographical claim.

The question also shaped the anachronism. The unemployment question arrived with modern categories, "unemployment rate" and "social insurance"; the retrieved passages talk about hunger and filial duty. The model mapped one vocabulary onto the other. A better system would translate the question into period categories before searching and mark that as an interpretation.

RAG can still help historical research. A claim can be tied to the passage behind it, so readers can check the link. A zero-hit or low-similarity result can be reported instead of hidden by five returned passages, which makes silence visible. Source information such as author, genre, speaker and date can travel with each chunk, so a historian can separate Lu Xun's voice from a compiler's or biographer's. One rule would help most: cite the passage or say the claim is unsupported.

We would split the corpus into authored, compiled or edited, and co-authored volumes, tag each chunk, remove or mark front matter and notes, use smaller chunks, raise the threshold, test a "no evidence" answer, and rewrite the persona prompt so that "known life" is not a licence to invent. The limits are clear: one figure, one model, a small question set, self-evaluation, a proprietary model that may change, and a web transcription rather than a critical edition.

The system does not reconstruct Lu Xun's mind, and it should not pretend to. At its best, it gives us a voice we can check: a claim tied to a book, a part and a passage, and a silence we can recognize as a silence.

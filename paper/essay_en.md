# Correct but Ungrounded: Reflections on Chatting with Lu Xun through RAG

**Group:** Zhang Min and Liu Chenyang
**Course:** DHG508, Assignment 2, Part 2
**Date:** 23 November 2026
**Word count:** approximately 1,900 words (including references)

## 1. Figure and corpus

RAG lets a model work from a set of texts instead of training memory alone. We wanted to see whether that changes how a historical figure answers questions. We chose Lu Xun (1881-1936) because his collected works are large, public domain, and familiar to us.

Part 1 gave us 54 volumes, about 4.4 million characters. The index used 32 of them, about 2.63 million by the library's count: three novels, two prose and memoir collections, seventeen essay collections, two literary histories, two preface collections, five compilations or editions, and the letters in Liangdi Shu. The other 22 are memoirs and biographies by Xu Shoushang, Xu Guangping, Zhou Zuoren, Xiao Hong and others. They are the main source for Lu Xun's private life. We left them out because we wanted the first person to be Lu Xun, not a biographer.

The corpus is less clean than "32 works by Lu Xun" sounds. Five of the volumes are compilations or editions of other people's texts, and Liangdi Shu is a collection of letters between Lu Xun and Xu Guangping, so the first person moves between two writers. Those six volumes are about a quarter of the indexed text. The files are web transcriptions, not critical editions. They keep book headers, chapter rules, editorial notes and lacunae, and some headers are cut off. Front matter is indexed. We did not check the text against printed editions. It is readable and citable, but it is a mixed archive, not a single voice.

The persona prompt made it worse. It told the model to answer in the first person, keep Lu Xun's tone, use "the materials you have read and your known life," and say "I don't know" when uncertain. The phrase "known life" gives the model permission to use what it remembers about Lu Xun's biography.

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

**The iron house (success).**
Question: "What did you mean by the iron house in the preface to Nahan?"
Answer: "The iron house was a figure for Chinese society, a suffocating darkness... The house is almost impossible to destroy, and yet the few people who are awake leave room for hope."
Evidence: "Imagine an iron house without windows, absolutely indestructible, with many people inside asleep, soon to suffocate." (Nahan, part 4); "Despair is as much an illusion as hope." (Nanqiang Beidiao Ji, part 17). All five passages were relevant, and [1][2][5] matched.
Verdict: Success. The answer rebuilt the argument and the exchange with Jin Xinyi.

**Youth reading (partial).**
Question: "Why do you oppose young people reading old Chinese books?"
Answer: "Read little, or indeed nothing, of Chinese books; read foreign books."
Evidence: All five passages were polemics, and three were opponents' rebuttals. Shi Zhecun's rebuttal quotes Lu Xun: "I think one should read little, or indeed nothing, of Chinese books." The original essay in Huagai Ji was not retrieved.
Verdict: Partial. The position is correct, but 0/5 primary text. The source type is wrong, and the original context, general readers versus specialists in ancient literature, is missing. A correct answer can hide a failed search.

**Zhu An (clear failure).**
Question: "What was your relationship with Zhu An?"
Answer: "It was a gift my mother gave me... Love is something I do not know... In the bingwu year I was in Sendai; a telegram said my mother was ill, but when I arrived it was a wedding."
Evidence: Zhu An (1878-1947) was the woman Lu Xun married in 1906 in an arranged marriage. The couple lived in separate rooms for most of their marriage; Lu Xun supported her financially and wrote little about her. Most of what we know about her comes from memoirs and biographies, which we had excluded. The corpus contains no "Zhu An" (grep = 0). The five retrieved passages were not about her. The top hit was a mock "marriage advertisement" in the Supplement to the Jiwai Ji Shiyi, placed by a self-described "Mr. Zhu" seeking a wife.
Verdict: Clear failure. 0/5 directly relevant. The answer gave a detailed biography with no citations. The source gap is the root cause, but retrieval returned noise instead of silence, and generation filled the gap with parametric memory.

**Fujino (partial).**
Question: "What did you most remember about Mr. Fujino?"
Answer: "His character was great in my eyes and in my heart, though his name is not known to many."
Evidence: The line is in Zhaohua Xishi, part 40. The other four were two prefaces and unrelated text from Qiejieting Zawen and Liangdi Shu. Only one of five was direct evidence.
Verdict: Partial. The answer is accurate, but the citations made it look better grounded than it was. Readers who know the essay accept the details; readers who do not see five citations and assume support.

**Unemployment and pensions (mixed / failure).**
Question: "Unemployment is high, and social insurance cannot cover the cost of old age. What do you think?"
Answer (simple): "I died in 1936; I do not know what happened after that."
Answer (agent): "Many people today talk about 'involution' and 'lying flat'... Social insurance, if it really protects people from mere survival, is good..."
Evidence: Simple: Fen 77-78; Nanqiang Beidiao Ji 49; noise Erxin Ji 92. One passage from Fen says, "the fundamental method is only to reform society." Agent: Huagai Ji 19; Nanqiang Beidiao Ji 23; Fen 76, 77, 88.
Verdict: Mixed / failure. Simple retrieval was 4/5 relevant; it hedged but accepted social insurance as familiar. Agent retrieval was 5/5 relevant but more anachronistic. Better retrieval, worse register.

**May Fourth (additional success).**
Question: "Do you think the May Fourth Movement succeeded?"
Answer: "On the surface it was somewhat successful."
Evidence: Five passages were relevant. The answer separated May Fourth from the later "New Culture Movement" label and stayed within Lu Xun's lifetime.
Verdict: Success. The system can handle a qualified historical judgment when the corpus and question cooperate.

## 4. Analysis

The iron house and May Fourth were correct and well grounded. Youth reading and Fujino were correct but weakly grounded. Zhu An was unsupported and ungrounded, and the agent unemployment answer had relevant passages but sounded modern. The correct but weakly grounded case is the most dangerous because it looks trustworthy. Fujino is the clearest example: the answer is accurate, the citations are there, and only one passage supports it.

Three things went wrong. The corpus came first: we excluded the memoirs that discuss Zhu An, so the question had no source; five indexed volumes are compilations or editions, and Liangdi Shu is co-authored, so the voice was mixed. Retrieval added a second problem: with top_k at 5 and min_similarity at 0.2, the system almost always returns five passages, even when none is relevant; 1,000-character chunks make each passage broad. The third problem was generation: the persona prompt allows "known life," the temperature is 0.7, and nothing requires every factual sentence to be cited.

Ted Underwood, Laura K. Nelson and Matthew Wilkens, in "Can Language Models Represent the Past without Anachronism?" (2025), show that prompting a contemporary model with period prose does not make it write like the period, and fine-tuning does not fool readers. That fits the agent answer. The search returned five relevant passages, but the model still said "involution" and "lying flat." The passages came from the period; the model's style did not. Thierry Poibeau, in "What Do Historical Language Models Model?" (2026), argues that historical language models model surviving archives, not past minds or populations. Our corpus is one of those archives. It preserves the published Lu Xun and leaves out the memoirs that discuss Zhu An. When the archive is silent, the model falls back on its wider training memory. The Zhu An answer is a plausible first-person text, not a retrieval-based biographical claim.

The question also shaped the anachronism. The unemployment question arrived with modern categories, "unemployment rate" and "social insurance"; the retrieved passages talk about hunger and filial duty. The model mapped one vocabulary onto the other. A better system would translate the question into period categories before searching and mark that as an interpretation.

RAG can still help historical research. A claim can be tied to the passage behind it, so readers can check the link. A zero-hit or low-similarity result can be reported instead of hidden by five returned passages, which makes silence visible. Source information such as author, genre, speaker and date can travel with each chunk, so a historian can separate Lu Xun's voice from a compiler's or biographer's. One rule would help most: cite the passage or say the claim is unsupported.

We would split the corpus into authored, compiled or edited, and co-authored volumes, tag each chunk, remove or mark front matter and notes, use smaller chunks, raise the threshold, test a "no evidence" answer, and rewrite the persona prompt so that "known life" is not a licence to invent. The limits are clear: one figure, one model, a small question set, self-evaluation, a proprietary model that may change, and a web transcription rather than a critical edition.

The system does not reconstruct Lu Xun's mind, and it should not pretend to. At its best, it gives us a voice we can check: a claim tied to a book, a part and a passage, and a silence we can recognize as a silence.

## References

Lu Xun. *Lu Xun quanji*. 18 vols. Beijing: Renmin wenxue chubanshe, 2005.

Poibeau, Thierry. "What Do Historical Language Models Model?" HAL preprint hal-05662234, 2026.

Underwood, Ted, Laura K. Nelson, and Matthew Wilkens. "Can Language Models Represent the Past without Anachronism?" arXiv:2505.00030, 2025.

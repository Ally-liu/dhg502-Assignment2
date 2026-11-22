# Correct but Ungrounded: Reflections on Chatting with Lu Xun through RAG

**Group:** Zhang Min and Liu Chenyang
**Course:** DHG508, Assignment 2, Part 2
**Date:** 23 November 2026
**Word count:** approximately 1,970 words (including headings and references)

## 1. Figure and corpus

RAG promises to make a model *read* a historical figure rather than *remember* him. We tested that promise with Lu Xun (1881–1936), whose complete works are large, public-domain, and familiar enough to judge; his first-person voice also makes ventriloquism easy to detect.

Our Part 1 corpus has 54 volumes (about 4.4 million characters); the index used the 32 in `LuXun_works` (about 2.63 million): three novels, two prose/memoir collections, seventeen essay collections, two scholarly works, two preface collections, five compilations or editions, and the co-authored *Liangdi Shu*. The 22 memoirs in `Writings_about_LuXun`—by Xu Shoushang, Xu Guangping, Zhou Zuoren, Xiao Hong, and others—were excluded so that the model's "I" would be Lu Xun's, not a biographer's.

The exclusion was principled but costly. The memoirs are exactly where Zhu An, Lu Xun's arranged wife, appears. By excluding them we removed the evidence needed to answer a question about her. The Zhu An failure is therefore overdetermined by our corpus design: we asked a question whose sources we had deliberately left out.

The corpus is also less pure than "32 works by Lu Xun" suggests. Five volumes are compilations or editions of other authors' texts; *Liangdi Shu* is a correspondence with Xu Guangping, so its first person alternates. Together they are about a quarter of the indexed characters. The files are UTF-8 web transcriptions, not critical editions: headers, chapter rules, editorial notes, and lacunae remain; some headers are truncated; front matter is indexed; and we did not collate against print editions. It is a mixed archive, not a pure voice.

The persona prompt deepened the problem. It told the model to answer in the first person, keep Lu Xun's tone, rely on "the materials you have read and your known life," and say "I don't know" when uncertain. "Known life" authorizes parametric memory; the Zhu An answer walked through that door.

## 2. Method

We asked five core questions, each aimed at a different layer: the iron house (textual argument), youth reading (stated position and source type), Zhu An (biographical silence), Fujino (detail recall and retrieval precision), and unemployment and pensions (conceptual anachronism). We added a sixth check on May Fourth and ran the unemployment question in both simple and agent mode.

**Table 1. Settings.**

| Setting | Value | Note |
|---|---|---|
| Application | HistFig, local FastAPI + SQLite | — |
| Chat model | `z-ai/glm-5.3-flash` via OpenRouter | Generation in the cloud |
| Embedding | `BAAI/bge-m3`, 1024 dimensions, local MPS | **Changed** |
| Chunking | 1,000 Chinese characters, 150 overlap | Kept |
| Index | 3,268 passages | — |
| Retrieval | hybrid vector + BM25, RRF k = 60 | Kept |
| `top_k` | 5 | Kept |
| `candidates` | 30 | Kept |
| `min_similarity` | 0.2 | Kept |
| History | 20 messages | Kept |
| Agent steps | up to 5 (4 used) | Kept |
| Temperature | 0.7 | Kept |

Only the embedding model changed. OpenRouter's embedding endpoint returned HTTP 404, so we rebuilt the index locally with `BAAI/bge-m3` (1024 dimensions) on an Apple M5 via MPS. The chat model stayed in the cloud: indexing kept the corpus local, but questions and retrieved passages went to OpenRouter. "Local deployment" therefore describes the application and the index, not the generation.

Each exchange began in a fresh conversation. We exported the answer, its citations, and the retrieved passages, then assigned a verdict: **success** (correct and grounded in primary text), **partial** (substantially correct but one layer fails), **mixed** (grounded restraint plus a conceptual failure), or **clear failure** (unsupported specifics presented as fact, with no citations). All translations are ours; the Chinese originals are in `evidence/`.

## 3. Evidence

**Table 2. Five exchanges and the passages behind them.**

| Exchange (quoted) | Passages behind it (quoted) | Verdict |
|---|---|---|
| **Q:** "What did you mean by the 'iron house'?"<br>**A:** "A figure for the whole of Chinese society… two layers: the house is almost impossible to destroy, yet one cannot say there is no hope." | "Imagine an iron house without windows, absolutely indestructible…" (*Call to Arms*, part 4); "Despair is as much an illusion as hope" (*South-North Dialect Collection*, part 17). | **Success.** 5/5 relevant; citations [1][2][5] match. |
| **Q:** "Why do you oppose young people reading old Chinese books?"<br>**A:** "Read little—or nothing—of Chinese books; read foreign books." | "Mr. Lu has the audacity to assert…" (*Collection of Uncollected Essays*, part 19, Shi Zhecun's rebuttal); the primary essay in *Huagai Ji* was **not retrieved**. | **Partial.** 0/5 primary text; the quote comes from an opponent. |
| **Q:** "What was your relationship with Zhu An?"<br>**A:** "A gift my mother gave me… Love is something I do not know." | No passage contains "Zhu An" (grep = 0); the top hit is a fake "Mr. Zhu" marriage advertisement (*Supplement to Collected Uncollected Essays*, part 158); no citations. | **Clear failure.** 0/5 relevant; biography presented as memory, with no source. |
| **Q:** "What did you most remember about Mr. Fujino?"<br>**A:** "His character was great in my eyes and in my heart…" | "His character was great…" (*Dawn Blossoms Plucked at Dusk*, part 40); other four: two prefaces (parts 1, 2) and unrelated *Qiejieting Zawen* 45 and *Liangdi Shu* 115. | **Partial.** Only 1/5 direct; the correct answer masks weak retrieval. |
| **Q:** "Unemployment is high, and social insurance cannot cover old age."<br>**A (simple):** "I died in 1936; I do not know…"<br>**A (agent):** "Many say 'involution' and 'lying flat'…" | Simple: *Fen* 77–78; *South-North* 49; noise *Erxin Ji* 92. Agent: *Huagai Ji* 19; *South-North* 23; *Fen* 76, 77, 88. | **Mixed / failure.** Simple 4/5, hedges but accepts "social insurance"; agent 5/5 but more anachronistic. |

The iron-house exchange is the clean success: the answer reconstructs the argument and the exchange with Jin Xinyi, and its citations [1][2][5] point to supporting passages.

The youth-reading exchange is a partial success: the position is correct, but the primary essay was never retrieved. The quotation survives in Shi Zhecun's rebuttal, so the answer may be quoting an opponent quoting Lu Xun. The source type is wrong, and the original context—general readers versus specialists in ancient literature—is missing. A correct answer can hide a retrieval failure.

The Zhu An exchange is the clearest failure. The answer is specific and historically plausible: the 1906 telegram, the "gift from my mother," the separate households. None of it is cited. The corpus contains no "Zhu An"; the top retrieved passage is a false lexical match on the character "Zhu" in a mock marriage advertisement. The failure is three-layered: the source is absent, the retriever returns noise instead of silence, and the generator fills the gap with parametric memory. It may be true, but it is not grounded—and that is the distinction that matters.

The Fujino exchange shows the same distinction in a milder form. The answer is accurate, but only one of five passages is direct evidence; the rest are front matter or unrelated text. A reader who knows the essay accepts the details; a reader who does not sees five citations and assumes support. Correctness is doing the work evidence should do.

The unemployment exchange is the most instructive comparison. In simple mode, the model says it died in 1936 and does not know the future—a genuine restraint—but then treats "social insurance" as familiar. In agent mode, retrieval improves to 5/5 relevant passages, but the answer says "involution" and "lying flat" and treats social insurance as familiar. Better retrieval produced a more fluent modern answer, not a better historical one.

A sixth check on May Fourth also succeeded: the answer gave a qualified verdict ("on the surface it was somewhat successful"), separated the movement from the later "New Culture Movement" label, and stayed within Lu Xun's lifetime. The system can support a qualified historical judgment when the corpus and the question cooperate.

## 4. Analysis

**Table 3. Correctness and grounding.**

| | Grounded in retrieved primary text | Not grounded |
|---|---|---|
| **Answer correct** | Iron house; May Fourth | Youth reading; Fujino |
| **Answer wrong or unsupported** | Unemployment (agent): retrieval relevant, generation anachronistic | Zhu An |

The upper-right cell is the most dangerous: a correct but ungrounded answer has the right facts, tone, and citations, but they do not carry the claim. Fujino is the clearest example; Zhu An, lower right, is easier to catch—no citations—but still plausible.

Where did the errors arise? **Sources**: the memoirs that could answer the Zhu An question were excluded, and the compilations and co-authored letters make the "Lu Xun" voice mixed. **Retrieval**: `top_k = 5` and `min_similarity = 0.2` almost always return five passages, even when none is relevant; 1,000-character chunks are broad. **Generation**: the persona prompt licenses "known life," the temperature is 0.7, and nothing requires every factual sentence to be cited.

Underwood, Nelson, and Wilkens explain the agent-mode failure: prompting a contemporary model with period prose does not make it write like the period; even fine-tuning, which can fool a date classifier, does not fool human readers. Retrieval supplied five relevant passages, but the generator still spoke of "involution" and "lying flat." The content was period-specific; the model's stylistic prior was not.

Poibeau explains the Zhu An failure. Historical language models do not simulate past minds or populations; they model the structure of surviving archives, shaped by genre, literacy, and preservation. Our corpus preserves the published Lu Xun and excludes the memoirs that discuss Zhu An. When the archive is silent, the generator falls back on parametric memory. The answer is a plausible first-person text about a person, not a retrieval-grounded biographical claim; Poibeau's validity ladder—textual, discursive, population-level—names the overreach.

The unemployment anachronism begins before retrieval, in the question's categories: "unemployment rate" and "social insurance" are modern institutions, while the retrieved passages speak of livelihood, hunger, and filial obligation. The generator maps one onto the other, producing a period voice that speaks modern policy.

What can RAG do for historical research? It can make a claim's evidentiary basis inspectable: each sentence can be tied to a passage that may or may not entail it. It can make silence visible—if zero-hit or low-similarity retrieval is reported rather than hidden by a top-five list. It can support source-type awareness: tagging author, genre, speaker, and date separates primary voice from reception. And it can enforce one rule: cite or abstain. Without these, RAG produces fluency, not evidence.

## 5. What we would change

We would separate the corpora into "authored," "compiled or edited," and "co-authored," and tag every chunk with author, speaker, genre, and date. We would strip or tag front matter and notes, use smaller chunks (300–500 characters), raise the similarity threshold, and test "no evidence" as a first-class outcome. We would lower the temperature and revise the persona prompt so that "known life" is not a license to invent; a second reader would judge the answers blind.

The limitations are obvious: one figure, one model, a small question set, self-evaluation, a proprietary chat model, an embedding model replaced after a guardrail error, and a web transcription rather than a critical edition. Our results are reproducible in procedure, not in exact output.

None of this makes RAG useless for history; it makes the footnote the point. The system does not reconstruct Lu Xun's mind, and it should not pretend to. At its best, it produces an accountable approximation of his voice: a claim we can trace to a book, a part, and a passage, and a silence we can recognize as silence. That is a modest contribution, but it is real.

## References

Lu Xun. *Lu Xun quanji*. 18 vols. Beijing: Renmin wenxue chubanshe, 2005. Quotations follow the digital corpus in this repository; book and part numbers refer to the HistFig export.

Poibeau, Thierry. "What Do Historical Language Models Model?" HAL preprint hal-05662234, 2026.

Underwood, Ted, Laura K. Nelson, and Matthew Wilkens. "Can Language Models Represent the Past without Anachronism?" arXiv:2505.00030, 2025.

Kurz, Matthew. *HistFig*. https://github.com/mcjkurz/histfig.

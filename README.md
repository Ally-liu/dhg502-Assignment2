# What a Lu Xun Chatbot Can and Cannot Answer

**DHG508 · Assignment 2 · Part 2 (group reflection essay)**
**Group:** Zhang Min and Liu Chenyang
**Date:** 23 November 2026

This repository contains the complete Assignment 2 submission: the Part 1 corpus, the Part 2 English reflection essay, the exported conversations and error log, and the system files needed to reproduce the experiment. The experiment uses [HistFig](https://github.com/mcjkurz/histfig) with the texts of **Lu Xun (鲁迅, 1881–1936)**.

The essay is the submitted text: **`paper/essay_en.docx`** (approximately 1,900 words, six pages). A Markdown source and a rendered PDF are included for convenience.

---

## Submission checklist

| Requirement | Where it is | Status |
|---|---|---|
| **Part 1:** `.txt` files, UTF-8, at least 1 million characters, with a source list | `corpus/`: 54 volumes, about 4.33 million characters; `corpus/manifest.csv`; `corpus/README.md` | Complete |
| **Part 2:** one group essay, **English, 1,500-2,000 words** | `paper/essay_en.docx`: approximately 1,900 words (Word count) | Complete |
| **1 · Figure and corpus:** what is in the files, what is missing, how clean the text is | Essay §1; `corpus/README.md`; `corpus/manifest.csv` | Complete |
| **2 · Method:** which questions were asked, which settings were changed | Essay §2; `system/README.md`; `system/config.example.toml` | Complete |
| **3 · Evidence:** at least five exchanges, each quoted with the passages behind it and a verdict; one success and one clear failure | Essay §3, five exchanges in structured prose; `evidence/`: eight exchanges, including the iron-house success and the Zhu An clear failure | Complete |
| **4 · Analysis:** where errors arose (sources, retrieval, generation); what RAG can do for historical research; engage Underwood et al. or Poibeau | Essay §4 | Complete |
| **Exported conversations (.md)** | `evidence/conversation_*.md`: four files, eight exchanges | Complete |
| **Error log (.csv or .xlsx)** | `evidence/error_log.csv`: eight rows with verdict and error layer | Complete |
| **AI-USE.md** | `AI-USE.md` | Complete |

---

## Contents

```text
README.md                  This overview and submission checklist
AI-USE.md                  AI-use disclosure
paper/
  essay_en.md              Essay source (Markdown)
  essay_en.docx            Submitted essay (A4, Times New Roman 12, 1.5 spacing)
  essay_en.pdf             Rendered copy
  README.md                Essay notes (word count, quotation policy)
corpus/
  README.md                Part 1 corpus description and full 54-volume tables
  manifest.csv             One row per volume: title, author, role, voice status, counts, source, used_in_index
  LuXun_works/             32 volumes used for the RAG index
  Writings_about_LuXun/    22 memoirs and biographies, submitted for Part 1 but excluded from the index
evidence/
  README.md                How to read the evidence; verdict rubric; 1-based part numbers
  conversation_evidence.md E1–E5: iron house, youth reading, Fujino, Zhu An, AI and literature
  conversation_simple.md   S1: unemployment and pensions, simple retrieval
  conversation_agent.md    A1: the same question, agent retrieval
  conversation_mayfourth.md E6: May Fourth
  error_log.csv            Eight exchanges with verdict and error layer
system/
  README.md                Persona and settings notes
  persona.md               Figure description and persona prompt used in the experiment
  config.example.toml      Key-free configuration example
code/
  build_manifest.py        Regenerates corpus/manifest.csv
  build_error_log.py       Regenerates evidence/error_log.csv
  make_docx.py             Regenerates paper/essay_en.docx from the Markdown source
```

---

## The corpus in one paragraph

The Part 1 submission contains **54 volumes, about 4.33 million characters** (3.53 million Chinese characters): 32 volumes in `LuXun_works/` and 22 memoirs or biographies about Lu Xun in `Writings_about_LuXun/`. The RAG experiment indexed only the 32 volumes in `LuXun_works/`: **2,629,782 characters, 3,268 passages**. The 22 memoirs were excluded so that the model's first-person "I" would be Lu Xun's, not a biographer's.

That exclusion is also the source of the experiment's clearest failure. The memoirs are exactly where **Zhu An (朱安, 1878-1947)**, Lu Xun's arranged wife, appears. By excluding them, we removed the evidence that could answer a question about her. The corpus is also not a pure Lu Xun voice: five of the 32 volumes are compilations or editions of other authors' texts, and *Liangdi Shu* is a co-authored correspondence with Xu Guangping. Together those six volumes are **643,097 characters, about 24.4%** of the indexed text. `corpus/manifest.csv` records the role and voice status of every volume.

---

## The experiment in one paragraph

We used HistFig's local FastAPI + SQLite application, a cloud chat model (`z-ai/glm-5.3-flash` via OpenRouter), and a locally rebuilt embedding index (`BAAI/bge-m3`, 1024 dimensions, Apple M5 via MPS). The only substantive change from the default setup was the embedding model: OpenRouter's embedding endpoint returned HTTP 404, so we rebuilt the index locally. **The application and index were local; generation was not**. Questions and retrieved passages were sent to OpenRouter.

Settings: 1,000-character chunks with 150 overlap; hybrid vector + BM25 retrieval with RRF k = 60; `top_k = 5`; `candidates = 30`; `min_similarity = 0.2`; 20 messages of history; up to 5 agent steps (4 used); temperature 0.7. Each exchange began in a fresh conversation and was exported with its retrieved passages.

We asked five core questions (iron house, youth reading, Zhu An, Fujino, unemployment and pensions), added a sixth check on May Fourth, and ran the unemployment question in both simple and agent mode.

---

## What we found

1. **RAG can produce a genuinely grounded answer.** The iron-house exchange reconstructs the argument and the exchange with Jin Xinyi; all five retrieved passages are relevant and the citations point to supporting text. The May Fourth check is a second, qualified success.
2. **Correctness is not the same as grounding.** The youth-reading and Fujino answers are substantially correct, but the primary text was not retrieved in the first case and only one of five passages was direct evidence in the second. A correct answer can hide a retrieval failure.
3. **The clearest failure is plausible, fluent, and unsourced.** The Zhu An answer gives a detailed biography with no `[n]` citations. The corpus contains no "Zhu An"; the top retrieved passage is a false lexical match on the character "朱" in a mock marriage advertisement. The failure is three-layered: source gap, retrieval noise, and parametric memory in generation.
4. **Better retrieval can produce a worse historical answer.** In agent mode, the unemployment question retrieves 5/5 relevant passages, but the generator puts "内卷" and "躺平" in Lu Xun's mouth and treats "社保" as a familiar institution. The content is period-specific; the model's stylistic prior is not.
5. **The corpus boundary is an interpretation.** Excluding the memoirs protected the first-person voice but made the Zhu An question unanswerable from the corpus. The five compilations and the co-authored letters mean the "Lu Xun" voice was already mixed. The essay turns this into the central methodological point rather than hiding it.

---

## Reproducing the experiment

1. Install HistFig and the optional local embedding stack:

   ```bash
   uv sync --extra local
   ```

2. Copy `system/config.example.toml` to HistFig's `data/config.toml` and add your own OpenRouter key. No key is stored in this repository.

3. Create a figure using `system/persona.md` and upload the 32 files in `corpus/LuXun_works/`. **Do not upload `corpus/Writings_about_LuXun/`** if you want to reproduce the first-person experiment; those 22 memoirs were deliberately excluded.

4. Wait for indexing to finish (the reference run produced 3,268 passages), then ask the questions in `evidence/conversation_evidence.md`, `conversation_simple.md`, `conversation_agent.md`, and `conversation_mayfourth.md`.

5. Export each conversation as Markdown and compare it with `evidence/error_log.csv`. Part numbers are 1-based, as exported by HistFig.

The reference run used a specific proprietary chat model and a locally rebuilt embedding index. **The procedure is reproducible; exact outputs are not.** Model updates, sampling, and the embedding change will produce different wording.

---

## Known limitations

- **Text quality:** the corpus is a UTF-8 web transcription, not a critical edition. Headers, chapter rules, editorial notes, and textual lacunae remain; some headers are truncated; we did not collate the texts against print editions.
- **Mixed voices:** five volumes are compilations or editions of other authors' texts, and *Liangdi Shu* is co-authored. The persona's "I" can retrieve other people's words.
- **Corpus boundary:** the 22 memoirs that discuss Zhu An were excluded. The Zhu An failure is overdetermined by that design choice.
- **Small sample:** one figure, one model, five core questions plus additional checks. We judged our own answers; there is no second coder.
- **Proprietary model:** the chat model may change or be deprecated. The embedding model was replaced after a guardrail error.
- **Language:** the submitted essay is in English. Quotations from Chinese sources are our translations; the Chinese originals are in `evidence/`.

---

## AI use and rights

See **`AI-USE.md`** for the tools used, the division of labour, and the verification procedure. The Lu Xun texts are in the public domain in mainland China (life + 50 years). The 22 memoirs are included for course use; their copyright status varies by author, and users should check before redistributing them. The essay, metadata, and documentation are the authors' work.

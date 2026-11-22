# AI-USE

This file records how AI tools were used in Assignment 2, in line with the course requirement to submit `AI-USE.md` with the reflection essay.

## Tools and models

| Tool / model | Role |
|---|---|
| **HistFig** (local FastAPI + SQLite) | The RAG application used in the experiment |
| **`z-ai/glm-5.3-flash`** via OpenRouter | Chat model for the conversations |
| **`BAAI/bge-m3`** (local `sentence-transformers`, 1024 dimensions) | Embedding model used to rebuild the index |
| **OpenCode** (AI assistant) | Environment setup, code and data handling, English drafting/translation, document formatting |

The chat model and the embedding model are part of the experiment; OpenCode is the writing and coding assistant. They are not the same thing, and the essay reports the experiment's models separately.

## What the AI assistant did

1. **Environment and code**
   - Helped install HistFig and the local embedding stack (`uv sync --extra local`).
   - Diagnosed the OpenRouter embedding endpoint's HTTP 404 and rebuilt the index with `BAAI/bge-m3`.
   - Helped export the conversations as Markdown and assemble the error log.

2. **Data and metadata**
   - Generated `corpus/manifest.csv` from the 54 corpus files (titles, authors, roles, voice status, character counts, source URLs, `used_in_index`).
   - Generated `evidence/error_log.csv` from the exported conversations and the authors' verdicts.
   - Corrected the part-number convention to the 1-based numbers in the HistFig exports.

3. **Writing and formatting**
   - Rewrote/translated the authors' Chinese draft into the English essay, following the assignment's four sections and the 1,500–2,000-word limit.
   - Drafted the repository README, the corpus/evidence/system notes, and this disclosure.
   - Generated the `.docx` from the Markdown source with a standard-library script (A4, Times New Roman 12 pt, 1.5 spacing, one bordered settings table).

## What the authors did

- Selected the figure, the corpus, and the 22 excluded memoirs.
- Designed the five core questions, the May Fourth check, and the simple/agent comparison.
- Ran the HistFig conversations and inspected the retrieved passages.
- Are responsible for the final check of every quotation and part number in the essay against `evidence/`.
- Revise the argument, the verdicts, and the prose, and approve the final text before submission.
- Are responsible for every claim and citation in the submission.

The English essay is a translation/rewrite of the authors' Chinese draft, not an independent AI invention. The AI assistant checked the quotations against `evidence/` while drafting; the authors' final review is the authoritative check. Any remaining errors are the authors' responsibility.

## Representative prompts

- "Rewrite this Chinese draft as a 1,800–2,000-word English group reflection with the four required sections. Keep every empirical claim traceable to `evidence/`; do not invent quotations."
- "Draft five exchanges in prose. For each, quote the question and a short answer, quote the retrieved passage with its book and part number, and give a verdict. Include one success and one clear failure."
- "Check every `part N` in the paper against the HistFig exports and list the mismatches. The exports are 1-based."
- "Separate the source, retrieval, and generation layers for each case. Where the evidence is ambiguous, say so."
- "Generate a clean A4 DOCX from the Markdown: Times New Roman 12 pt, 1.5 spacing, bordered tables."

## Notes

- No API keys are stored in this repository. `system/config.example.toml` is key-free.
- The Lu Xun texts are in the public domain in mainland China (life + 50 years). The 22 memoirs are included for course use; their copyright status varies by author.
- Quotations from Chinese sources in the essay are the authors' translations; the Chinese originals are in `evidence/`.
- The experiment used a proprietary chat model and a locally rebuilt embedding index. The procedure is reproducible; exact outputs are not.

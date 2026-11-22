# AI-USE

This file records how AI tools were used in Assignment 2.

## Tools and models

| Tool / model | Role |
|---|---|
| **HistFig** (local FastAPI + SQLite) | The RAG application used in the experiment |
| **`z-ai/glm-5.3-flash`** via OpenRouter | Chat model for the conversations |
| **`BAAI/bge-m3`** (local `sentence-transformers`, 1024 dimensions) | Embedding model used to rebuild the index |
| **OpenCode** (AI assistant) | Environment setup, code and data handling, English language editing and translation, document formatting |

## What the AI assistant did

1. **Environment and code**
   - Helped install HistFig and the local embedding stack (`uv sync --extra local`).
   - Diagnosed the OpenRouter embedding endpoint's HTTP 404 and rebuilt the index with `BAAI/bge-m3`.
   - Helped export the conversations as Markdown and assemble the error log.

2. **Data and metadata**
   - Generated `corpus/manifest.csv` from the 54 corpus files (titles, authors, roles, voice status, character counts, source URLs, `used_in_index`).
   - Generated `evidence/error_log.csv` from the exported conversations and the authors' verdicts.
   - Corrected the part-number convention to the 1-based numbers in the HistFig exports.

3. **Language and formatting**
   - Provided English language editing and translation for the authors' draft.
   - Helped prepare the repository README and the corpus/evidence/system notes.
   - Generated the `.docx` from the Markdown source with a standard-library script (A4, Times New Roman 12 pt, 1.5 spacing, one bordered settings table).

## What the authors did

- Selected the figure, the corpus, and the 22 excluded memoirs.
- Designed the five core questions, the May Fourth check, and the simple/agent comparison.
- Ran the HistFig conversations and inspected the retrieved passages.
- Wrote and revised the essay, and checked every quotation and part number against `evidence/`.
- Approved the final text and are responsible for every claim and citation.

The authors wrote and revised the essay. The AI assistant provided language editing and translation, and helped with code, data and formatting. The authors checked every quotation and part number against `evidence/` and approved the final text. Any remaining errors are the authors' responsibility.

## Notes

- No API keys are stored in this repository. `system/config.example.toml` is key-free.
- The Lu Xun texts are in the public domain in mainland China (life + 50 years). The 22 memoirs are included for course use; their copyright status varies by author.
- Quotations from Chinese sources in the essay are English translations; the Chinese originals are in `evidence/`.
- The experiment used a proprietary chat model and a locally rebuilt embedding index. The procedure is reproducible; exact outputs are not.

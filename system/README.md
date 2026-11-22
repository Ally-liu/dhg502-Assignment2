# System

This directory records the figure description, the persona prompt, and the settings used in the experiment.

## `persona.md`

`persona.md` is the exact prompt used to create the Lu Xun figure in HistFig. It contains:

- a short figure description (name, years, description);
- a first-person persona instruction: keep Lu Xun's tone, stay in character, and answer in the first person;
- the evidential instruction: "只依据你读到的材料与已知身世作答，不确定的事就说不知道" — "answer only from the materials you have read and your known life; say you do not know when uncertain."

The phrase **"已知身世" ("known life")** is analyzed in the essay as a design loophole. It authorizes parametric memory: the model may use what it knows about Lu Xun's biography, not only the retrieved corpus. The Zhu An answer is the clearest result. The prompt is kept here as an artifact of the experiment, not as a recommendation. A future version would separate style instructions ("sound like Lu Xun") from factual permissions ("use only the retrieved passages; otherwise abstain").

The prompt also says "say you do not know when uncertain." The model did this in the unemployment question ("我死在1936年，此后的事我不知道"), but not in the Zhu An question. The difference is instructive: an instruction to hedge is not the same as a mechanism for detecting silence.

## `config.example.toml`

The example config is key-free. It records the settings used in the reference run:

| Setting | Value |
|---|---|
| Chat provider | OpenRouter, `z-ai/glm-5.3-flash` |
| Embedding | `BAAI/bge-m3`, 1024 dimensions, local `sentence-transformers` |
| Chunking | 1,000 Chinese characters, 150 overlap |
| Retrieval | hybrid vector + BM25, RRF k = 60 |
| `top_k` | 5 |
| `candidates` | 30 |
| `min_similarity` | 0.2 |
| History | 20 messages |
| Agent steps | 5 |
| Temperature | 0.7 |

**What changed:** the embedding model. OpenRouter's embedding endpoint returned HTTP 404, so the index was rebuilt locally with `BAAI/bge-m3` on an Apple M5 via MPS. The chat model stayed in the cloud. The application and index were local; the questions and retrieved passages were sent to OpenRouter.

## Reproducing the first-person experiment

1. Install HistFig and the local embedding extra: `uv sync --extra local`.
2. Copy `config.example.toml` to HistFig's `data/config.toml` and add your own OpenRouter key.
3. Create the figure with `persona.md`.
4. Upload only `corpus/LuXun_works/*.txt` (32 volumes). Do **not** upload `corpus/Writings_about_LuXun/`; the 22 memoirs were excluded from the experiment.
5. Ask the questions in `evidence/` and compare the retrieved passages with the exported conversations.

Exact outputs will differ: the chat model is proprietary and may change, and the embedding model was replaced after a guardrail error. The procedure is reproducible; the wording is not.

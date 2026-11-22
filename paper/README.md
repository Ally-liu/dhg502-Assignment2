# Paper

**Title:** Correct but Ungrounded: Reflections on Chatting with Lu Xun through RAG
**Group:** Zhang Min and Liu Chenyang
**Course:** DHG508, Assignment 2, Part 2
**Date:** 23 November 2026

## Files

| File | Purpose |
|---|---|
| `essay_en.docx` | **Submitted essay.** A4, Times New Roman 12 pt, 1.5 line spacing, six pages. Word count: approximately 1,900 (including references). |
| `essay_en.md` | Markdown source. Use this for editing; regenerate the `.docx` afterwards. |
| `essay_en.pdf` | Rendered copy for reading without Word. |

The submitted version is the `.docx`. The `.pdf` is a convenience copy; if the two differ, the `.docx` is authoritative.

## What the essay contains

The essay follows the four headings in the assignment:

1. **Figure and corpus**: why Lu Xun; 54 volumes in Part 1, 32 in the index, 22 memoirs excluded; what is missing (the memoirs that cover his private life); how clean the text is (web transcriptions, front matter, editorial notes, lacunae, five compilations and one co-authored letter collection).
2. **Method**: five core questions, a sixth May Fourth check, the simple/agent comparison, the settings table, and the one substantive change (local `BAAI/bge-m3` after the OpenRouter HTTP 404).
3. **Evidence**: five exchanges in structured prose, each with a quoted question, quoted answer, quoted retrieved passages, and a verdict. The iron-house exchange is the **success**; the Zhu An exchange is the **clear failure**. May Fourth is a second success in the text.
4. **Analysis**: the correctness/grounding discussion in prose; the source, retrieval, and generation layers; the persona prompt's "known life" loophole; `top_k`/`min_similarity`/chunking; Underwood, Nelson, and Wilkens on stylistic anachronism; Poibeau on surviving archives; what RAG can do for historical research; what we would change; limitations.

The essay ends with a short reference list for Lu Xun, Underwood et al., and Poibeau.

## Quotation policy

The conversations and retrieved passages are in Chinese. The essay quotes them in English translation. The translations are ours; the Chinese originals, the `[n]` citation labels, and the full passages are in `../evidence/`. The essay's part numbers are 1-based and match the exported conversations.

## Regenerating the DOCX

The `.docx` is generated from `essay_en.md` by a small script that uses only the Python standard library:

```bash
py -X utf8 code/make_docx.py
```

The script reads `paper/essay_en.md` and writes `paper/essay_en.docx`. It uses A4, 1-inch margins, Times New Roman 12 pt for Latin text, SimSun for Chinese characters, 1.5 line spacing, and a bordered settings table. If you edit the Markdown, rerun the script and check the Word count before submitting.

The Chinese draft was a working document. It is not included here; the English essay is the submitted version.

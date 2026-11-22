# Evidence

This directory contains the exported conversations, the retrieved passages, and the error log behind the essay. Every verdict in the essay can be checked against a file here.

## Files

| File | Exchanges | What it covers |
|---|---|---|
| `conversation_evidence.md` | E1–E5 | Iron house, required reading for youth, Fujino, Zhu An, AI and literary creation |
| `conversation_simple.md` | S1 | Unemployment and pensions, simple retrieval |
| `conversation_agent.md` | A1 | The same question, agent retrieval (four self-directed searches) |
| `conversation_mayfourth.md` | E6 | May Fourth, additional check |
| `error_log.csv` | E1–E6, S1, A1 | One row per exchange: question, mode, error type, what happened, sources, verdict, layers |

`error_log.csv` is UTF-8 with a BOM so that Chinese text opens correctly in Excel.

## Summary

| ID | Case | Mode | Verdict | Error layer(s) |
|---|---|---|---|---|
| E1 | Iron house | simple | **Success** | sources, retrieval, generation all worked |
| E2 | Required reading for youth | simple | **Partial** | retrieval (primary text missed); source type |
| E3 | Fujino | simple | **Partial** | retrieval precision; front matter noise |
| E4 | Zhu An | simple | **Clear failure** | sources (silence); retrieval (noise); generation (parametric memory) |
| S1 | Unemployment and pensions | simple | **Mixed** | retrieval (one noise passage); generation (concept) |
| A1 | Unemployment and pensions | agent | **Failure** | generation (register), despite 5/5 relevant retrieval |
| E5 | AI and literary creation | simple | **Success** | sources, retrieval, generation |
| E6 | May Fourth | simple | **Success** | sources, retrieval, generation |

The essay discusses five core exchanges in structured prose: E1, E2, E3, E4, and S1/A1 as one comparison. E5 and E6 are additional checks; E6 is mentioned in the essay as a second success.

## Verdict rubric

- **Success**: the answer is correct and every substantive claim is supported by retrieved primary text.
- **Partial**: the answer is substantially correct, but one layer fails (source type, retrieval precision, register).
- **Mixed**: grounded restraint combined with a significant conceptual failure.
- **Clear failure**: unsupported specifics are presented as fact, with no citations, and retrieval does not support them.

The essay uses these labels in its verdicts.

## Part numbers are 1-based

Every `part N` label in the exported conversations is **1-based**, as produced by HistFig. The essay and `error_log.csv` use the same numbers. If you compare them with an earlier draft of the paper, note that the earlier draft used 0-based numbers and was one lower throughout; this repository corrects that. For example:

- Fujino: **part 40** (not 39)
- Zhu An: **part 158** (not 157)
- Iron house, *South-North Dialect Collection*: **part 17** (not 16)
- Unemployment, *Erxin Ji* noise passage: **part 92** (not 91)

## Quotation policy

The conversations are in Chinese. The essay quotes them in English translation; the translations are ours. The Chinese originals, the `[n]` citation labels, and the full retrieved passages are in the conversation files. Some quotations in the essay are shortened to a phrase; the full passages are in those files.

## A note on the pilot rows

An earlier version of the error log contained three pilot rows from a `conversation_pilot.md` file that was not archived. They have been removed: every row in this directory now points to a file that exists. The pilot questions were exploratory and are not part of the essay's five core cases or its additional checks.

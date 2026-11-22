# Code

Small, dependency-free scripts that regenerate the repository's metadata and the submitted `.docx` from the source files. They use only the Python standard library (Python 3.9+).

Run them from the repository root:

```bash
py -X utf8 code/build_manifest.py
py -X utf8 code/build_error_log.py
py -X utf8 code/make_docx.py
```

| Script | Input | Output |
|---|---|---|
| `build_manifest.py` | `corpus/LuXun_works/*.txt`, `corpus/Writings_about_LuXun/*.txt` | `corpus/manifest.csv` |
| `build_error_log.py` | The eight exchanges and the authors' verdicts | `evidence/error_log.csv` |
| `make_docx.py` | `paper/essay_en.md` | `paper/essay_en.docx` |

`make_docx.py` writes a minimal OOXML package: A4, 1-inch margins, Times New Roman 12 pt for Latin text, SimSun for Chinese characters, 1.5 line spacing, and bordered tables. It does not depend on Word, `python-docx`, or `pandoc`.

The scripts are included for transparency and reproducibility. The submitted essay is `paper/essay_en.docx`; the generated files are checked into the repository so the instructor does not need to run anything.

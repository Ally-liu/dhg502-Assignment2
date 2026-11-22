import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

SRC = Path("paper/essay_en.md")
OUT = Path("paper/essay_en.docx")

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def run(text, bold=False, italic=False, size=24, font="Times New Roman", east="SimSun"):
    text = escape(text)
    props = [
        f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:eastAsia="{east}"/>',
        f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>',
    ]
    if bold:
        props.append("<w:b/><w:bCs/>")
    if italic:
        props.append("<w:i/><w:iCs/>")
    return f'<w:r><w:rPr>{"".join(props)}</w:rPr><w:t xml:space="preserve">{text}</w:t></w:r>'


def inline_runs(text, size=24, base_bold=False, base_italic=False):
    """Parse **bold**, *italic*, `code`, and <br> into Word runs."""
    parts = re.split(r"(\*\*.*?\*\*|\*.*?\*|`[^`]*`|<br\s*/?>)", text, flags=re.S)
    out = []
    for part in parts:
        if not part:
            continue
        if part.lower().startswith("<br"):
            out.append("<w:r><w:br/></w:r>")
        elif part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append(run(part[2:-2], bold=True, italic=base_italic, size=size))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            out.append(run(part[1:-1], bold=base_bold, italic=True, size=size))
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            out.append(run(part[1:-1], bold=base_bold, italic=base_italic, size=size))
        else:
            out.append(run(part, bold=base_bold, italic=base_italic, size=size))
    return "".join(out)


def paragraph(text, style="Normal", size=24, bold=False, italic=False, align=None,
              before=0, after=120, line=360):
    jc = f'<w:jc w:val="{align}"/>' if align else ""
    ppr = (
        f'<w:pPr><w:pStyle w:val="{style}"/>'
        f'<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>'
        f"{jc}</w:pPr>"
    )
    return f"<w:p>{ppr}{inline_runs(text, size=size, base_bold=bold, base_italic=italic)}</w:p>"


def table(rows, widths=(3600, 3600, 1826)):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    borders = (
        '<w:tblBorders>'
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
        '</w:tblBorders>'
    )
    tblpr = (
        f'<w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/>'
        f'<w:tblLayout w:type="autofit"/>{borders}'
        '<w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
        '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar>'
        '</w:tblPr>'
    )
    out = [f"<w:tbl>{tblpr}<w:tblGrid>{grid}</w:tblGrid>"]
    for i, row in enumerate(rows):
        header = i == 0
        trpr = "<w:trPr><w:tblHeader/></w:trPr>" if header else ""
        out.append(f"<w:tr>{trpr}")
        for j, cell in enumerate(row):
            width = widths[j] if j < len(widths) else widths[-1]
            tcpr = f'<w:tcPr><w:tcW w:w="{width}" w:type="dxa"/><w:vAlign w:val="top"/></w:tcPr>'
            cell_paras = []
            for seg in cell.split("<br>"):
                cell_paras.append(paragraph(seg, size=18, bold=header, after=0, line=240))
            out.append(f"<w:tc>{tcpr}{''.join(cell_paras)}</w:tc>")
        out.append("</w:tr>")
    out.append("</w:tbl>")
    return "".join(out)


text = SRC.read_text(encoding="utf-8")
lines = text.splitlines()
body = []
i = 0
while i < len(lines):
    line = lines[i].rstrip()
    if not line:
        i += 1
        continue
    if line.startswith("# "):
        body.append(paragraph(line[2:].strip(), style="Title", size=36, bold=True,
                              align="center", before=0, after=200, line=240))
    elif line.startswith("## "):
        body.append(paragraph(line[3:].strip(), style="Heading1", size=32, bold=True,
                              before=280, after=120, line=240))
    elif line.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            row = lines[i].strip()
            if not re.match(r"^\|[\s:\-|]+\|$", row):
                cells = [c.strip() for c in row.strip("|").split("|")]
                rows.append(cells)
            i += 1
        if rows:
            body.append(table(rows))
            body.append(paragraph("", after=80, line=240))
        continue
    elif line.startswith("**Table "):
        body.append(paragraph(line, size=20, before=120, after=80, line=240))
    elif line.startswith("**Group:**") or line.startswith("**Course:**") or line.startswith("**Date:**") or line.startswith("**Word count:**"):
        body.append(paragraph(line, size=22, after=40, line=240))
    else:
        body.append(paragraph(line, size=24, after=120, line=360))
    i += 1

document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W}" xmlns:r="{R}">
<w:body>
{''.join(body)}
<w:sectPr>
<w:pgSz w:w="11906" w:h="16838"/>
<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>
<w:cols w:space="720"/>
<w:docGrid w:linePitch="312"/>
</w:sectPr>
</w:body>
</w:document>'''

styles = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
<w:docDefaults>
<w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="SimSun" w:cs="Times New Roman"/>
<w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-US" w:eastAsia="zh-CN"/>
</w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault>
</w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:jc w:val="center"/><w:spacing w:after="200"/></w:pPr><w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="280" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="32"/></w:rPr></w:style>
</w:styles>'''

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''

core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>Correct but Ungrounded: Reflections on Chatting with Lu Xun through RAG</dc:title>
<dc:creator>Zhang Min; Liu Chenyang</dc:creator>
<cp:lastModifiedBy>Zhang Min; Liu Chenyang</cp:lastModifiedBy>
<dcterms:created xsi:type="dcterms:W3CDTF">2026-11-23T00:00:00Z</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">2026-11-23T00:00:00Z</dcterms:modified>
</cp:coreProperties>'''

app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>OpenCode</Application>
</Properties>'''

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", document)
    z.writestr("word/styles.xml", styles)
    z.writestr("word/_rels/document.xml.rels", doc_rels)
    z.writestr("docProps/core.xml", core)
    z.writestr("docProps/app.xml", app)

print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")

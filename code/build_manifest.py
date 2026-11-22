import csv
import re
from pathlib import Path

ROOT = Path("corpus")
OUT = ROOT / "manifest.csv"

sets = {
    "LuXun_works": {
        "used": "yes",
        "default_role": "authored",
    },
    "Writings_about_LuXun": {
        "used": "no",
        "default_role": "memoir/biography",
    },
}

role_map = {
    "01_呐喊.txt": ("fiction", "authored", "novel collection"),
    "02_彷徨.txt": ("fiction", "authored", "novel collection"),
    "03_故事新编.txt": ("fiction", "authored", "novel collection"),
    "04_野草.txt": ("prose poetry", "authored", "prose-poetry collection"),
    "05_朝花夕拾.txt": ("memoir", "authored", "memoir collection"),
    "06_坟.txt": ("essay collection", "authored", "zawen collection"),
    "07_热风.txt": ("essay collection", "authored", "zawen collection"),
    "08_华盖集.txt": ("essay collection", "authored", "zawen collection"),
    "09_华盖集续编.txt": ("essay collection", "authored", "zawen collection"),
    "10_而已集.txt": ("essay collection", "authored", "zawen collection"),
    "11_三闲集.txt": ("essay collection", "authored", "zawen collection"),
    "12_二心集.txt": ("essay collection", "authored", "zawen collection"),
    "13_伪自由书.txt": ("essay collection", "authored", "zawen collection"),
    "14_南腔北调集.txt": ("essay collection", "authored", "zawen collection"),
    "15_准风月谈.txt": ("essay collection", "authored", "zawen collection"),
    "16_花边文学.txt": ("essay collection", "authored", "zawen collection"),
    "17_且介亭杂文.txt": ("essay collection", "authored", "zawen collection"),
    "18_且介亭杂文二集.txt": ("essay collection", "authored", "zawen collection"),
    "19_且介亭杂文末编.txt": ("essay collection", "authored", "zawen collection"),
    "20_集外集.txt": ("essay collection", "authored", "zawen collection"),
    "21_集外集拾遗.txt": ("essay collection", "authored", "zawen collection"),
    "22_集外集拾遗补编.txt": ("essay collection", "authored", "miscellany; includes notes and appendices"),
    "23_中国小说史略.txt": ("scholarship", "authored", "literary history"),
    "24_汉文学史纲要.txt": ("scholarship", "authored", "literary history"),
    "25_古籍序跋集.txt": ("prefaces", "authored", "prefaces and postscripts"),
    "26_译文序跋集.txt": ("prefaces", "authored", "prefaces and postscripts to translations"),
    "27_古小说钩沉.txt": ("compilation", "compiled", "compilation of earlier texts; not solely Lu Xun's voice"),
    "28_唐宋传奇集.txt": ("compilation", "edited", "edited anthology of Tang-Song tales; not solely Lu Xun's voice"),
    "29_小说旧闻钞.txt": ("compilation", "compiled", "compilation of earlier sources; not solely Lu Xun's voice"),
    "30_嵇康集.txt": ("compilation", "edited", "Ji Kang's works, edited and collated by Lu Xun; not Lu Xun's voice"),
    "31_会稽郡故书杂集.txt": ("compilation", "compiled", "compilation of earlier local records; not solely Lu Xun's voice"),
    "32_两地书.txt": ("letters", "co-authored", "letters with Xu Guangping; first person alternates"),
}


def field(text, label):
    m = re.search(rf"^{label}：(.*)$", text, flags=re.M)
    return m.group(1).strip() if m else ""


rows = []
for set_name, meta in sets.items():
    for path in sorted((ROOT / set_name).glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        title = field(text, "书名")
        author = field(text, "作者")
        edition = field(text, "初版")
        source = field(text, "来源")
        fetched = field(text, "抓取时间")
        m = re.search(r"字符数：(\d+)", text)
        chars_header = m.group(1) if m else ""
        role, voice, note = role_map.get(path.name, ("memoir/biography", "memoir", "biographical source; excluded from the RAG index"))
        rows.append({
            "set": set_name,
            "file": path.name,
            "title": title,
            "author": author,
            "role": role,
            "voice_status": voice,
            "first_edition": edition,
            "chars_header": chars_header,
            "chars_file": len(text),
            "han": len(re.findall(r"[\u4e00-\u9fff]", text)),
            "source_url": source,
            "fetched": fetched,
            "used_in_index": meta["used"],
            "notes": note,
        })

with OUT.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"wrote {OUT} ({len(rows)} rows)")
print("index chars:", sum(int(r["chars_file"]) for r in rows if r["used_in_index"] == "yes"))
print("all chars:", sum(int(r["chars_file"]) for r in rows))
print("compilation/letters chars:", sum(int(r["chars_file"]) for r in rows if r["voice_status"] in {"compiled", "edited", "co-authored"}))

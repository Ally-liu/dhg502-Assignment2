import csv
from pathlib import Path

rows = [
    {
        "exchange_id": "E1",
        "case": "Iron house (core 1)",
        "file": "conversation_evidence.md",
        "question": "你在《呐喊》自序里说的“铁屋子”，究竟是什么意思？",
        "mode": "simple",
        "error_type": "none (success)",
        "what_happened": "The answer reconstructs the iron-house argument and the exchange with Jin Xinyi; citations [1][2][5] point to relevant passages. 5/5 passages relevant.",
        "sources": "呐喊 1/3/4; 两地书 43; 南腔北调集 17",
        "verdict": "success",
        "layers": "sources; retrieval; generation",
    },
    {
        "exchange_id": "E2",
        "case": "Required reading for youth (core 2)",
        "file": "conversation_evidence.md",
        "question": "你为什么不赞成青年读中国古书？",
        "mode": "simple",
        "error_type": "partial retrieval: primary source missed",
        "what_happened": "The position is correct, but all five sources are polemics that quote or dispute Lu Xun; three are opponents' rebuttals. The primary essay in 08_华盖集 was not retrieved. 5/5 on topic, 0/5 primary text.",
        "sources": "准风月谈 63/65; 集外集拾遗 16/19/21",
        "verdict": "partial",
        "layers": "retrieval; sources (source type)",
    },
    {
        "exchange_id": "E3",
        "case": "Fujino (core 3)",
        "file": "conversation_evidence.md",
        "question": "《朝花夕拾》里你写藤野先生，他最让你感念的是什么？",
        "mode": "simple",
        "error_type": "retrieval precision; front matter noise",
        "what_happened": "The answer is accurate, but only one of five passages is direct evidence (朝花夕拾 40). The other four are the volume preface (part 1), the 故事新编 preface (part 2), and unrelated passages (且介亭杂文 45; 两地书 115). 1/5 direct.",
        "sources": "朝花夕拾 1/40; 且介亭杂文 45; 两地书 115; 故事新编 2",
        "verdict": "partial",
        "layers": "retrieval; corpus cleaning",
    },
    {
        "exchange_id": "E4",
        "case": "Zhu An (core 4)",
        "file": "conversation_evidence.md",
        "question": "你和朱安的感情怎样？",
        "mode": "simple",
        "error_type": "unsupported generation (clear failure)",
        "what_happened": "No passage in the 32-volume corpus contains 朱安 (grep = 0). The five retrieved passages are not about her; the top hit is a false lexical match on 朱 in a mock marriage advertisement. The answer gives a detailed biography with no [n] citations.",
        "sources": "集外集拾遗补编 158; 南腔北调集 2/10; 朝花夕拾 42; 两地书 160",
        "verdict": "clear failure",
        "layers": "sources; retrieval; generation",
    },
    {
        "exchange_id": "S1",
        "case": "Unemployment and pensions (simple)",
        "file": "conversation_simple.md",
        "question": "当前中国失业率很高，社保又覆盖不了养老成本，你怎么看这些问题？",
        "mode": "simple",
        "error_type": "conceptual anachronism; one noise passage",
        "what_happened": "The answer states that it died in 1936 and does not know the future, but then treats 社保 as a familiar institution. 4/5 passages relevant; 二心集 92 is a translation criticism (sim .356) and is unrelated.",
        "sources": "坟 77/78; 南腔北调集 49; 二心集 92 (noise); 集外集拾遗补编 127",
        "verdict": "mixed",
        "layers": "retrieval; generation",
    },
    {
        "exchange_id": "A1",
        "case": "Unemployment and pensions (agent)",
        "file": "conversation_agent.md",
        "question": "当前中国失业率很高，社保又覆盖不了养老成本，你怎么看这些问题？",
        "mode": "agent",
        "error_type": "register anachronism despite relevant retrieval",
        "what_happened": "Four self-directed searches return 5/5 relevant passages, but the answer puts 内卷 and 躺平 in Lu Xun's mouth and treats 社保 as familiar. Better retrieval, worse register.",
        "sources": "华盖集 19; 南腔北调集 23; 坟 76/77/88",
        "verdict": "failure",
        "layers": "generation",
    },
    {
        "exchange_id": "E5",
        "case": "AI and literary creation (additional check)",
        "file": "conversation_evidence.md",
        "question": "你怎么看人工智能对文学创作的影响？",
        "mode": "simple",
        "error_type": "acceptable anachronism (success)",
        "what_happened": "The model states that its period knowledge ends in 1936, then reasons from period arguments about literature and class with citations; no modern jargon. 5/5 relevant.",
        "sources": "而已集 7/9; 二心集 8/27; 集外集拾遗补编 235",
        "verdict": "success",
        "layers": "sources; retrieval; generation",
    },
    {
        "exchange_id": "E6",
        "case": "May Fourth (additional check)",
        "file": "conversation_mayfourth.md",
        "question": "你觉得五四运动成功了吗？",
        "mode": "simple",
        "error_type": "none (success)",
        "what_happened": "The answer gives a qualified verdict, separates 五四 from the later 新文化运动 label, and stays within Lu Xun's lifetime. 5/5 relevant.",
        "sources": "南腔北调集 24; 而已集 2; 热风 1; 集外集拾遗补编 107; 三闲集 43",
        "verdict": "success",
        "layers": "sources; retrieval; generation",
    },
]

out = Path("evidence/error_log.csv")
with out.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"wrote {out} ({len(rows)} rows)")

#!/usr/bin/env python3
"""
B★ eCO₂ Strategy — DOCX 병합 스크립트 v2.0
사용법:
  python merge_to_docx.py --vol 1 --lang KR   # Vol.1 KR만
  python merge_to_docx.py --vol all --lang all # 전체 6개 생성
"""

import argparse
import os
from pathlib import Path

# python-docx 필요: pip install python-docx
try:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    print("[ERROR] python-docx 미설치: pip install python-docx")
    exit(1)

# ============================================================
# 볼륨 정의
# ============================================================
VOLUME_MAP = {
    "1": {
        "KR": {"dir": "Vol1_Technical/KR", "files": ["Ch01_KR.md","Ch02_KR.md","Ch03_KR.md","Ch04_KR.md"],
               "title": "B★ eCO₂ 전략 보고서 — Vol.1 기술편", "subtitle": "응용처 분석 · 열역학 · 열원 설계 · 압축기PCHE"},
        "EN": {"dir": "Vol1_Technical/EN", "files": ["Ch01_EN.md","Ch02_EN.md","Ch03_EN.md","Ch04_EN.md"],
               "title": "B★ eCO₂ Strategy Report — Vol.1 Technical", "subtitle": "Application Analysis · Thermodynamics · Heat Source Design · Compressor PCHE"}
    },
    "2": {
        "KR": {"dir": "Vol2_Business/KR", "files": ["Ch05_KR.md","Ch06_KR.md","Ch07_KR.md","Ch08_KR.md","Ch09_KR.md"],
               "title": "B★ eCO₂ 전략 보고서 — Vol.2 사업편", "subtitle": "제어전략 · 안전규제 · 사업화 · 재무 · IP특허"},
        "EN": {"dir": "Vol2_Business/EN", "files": ["Ch05_EN.md","Ch06_EN.md","Ch07_EN.md","Ch08_EN.md","Ch09_EN.md"],
               "title": "B★ eCO₂ Strategy Report — Vol.2 Business", "subtitle": "Control · Safety · Commercialization · Finance · IP"}
    },
    "3": {
        "KR": {"dir": "Vol3_Appendix/KR", "files": ["AppA_KR.md","AppB_KR.md","AppC_KR.md"],
               "title": "B★ eCO₂ 전략 보고서 — Vol.3 부록편", "subtitle": "차트 · 데이터 테이블 · 용어집 · 참고문헌"},
        "EN": {"dir": "Vol3_Appendix/EN", "files": ["AppA_EN.md","AppB_EN.md","AppC_EN.md"],
               "title": "B★ eCO₂ Strategy Report — Vol.3 Appendix", "subtitle": "Charts · Data Tables · Glossary · References"}
    }
}


def add_cover_page(doc, title, subtitle, lang="KR"):
    """표지 페이지 추가"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(24)

    doc.add_paragraph()  # 공백
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run(subtitle)
    run2.font.size = Pt(14)

    doc.add_paragraph()
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    version_text = f"버전: v2.0 | 날짜: 2026-03-19 | 정책: B★ Standalone" if lang == "KR" else \
                   f"Version: v2.0 | Date: 2026-03-19 | Policy: B★ Standalone"
    p3.add_run(version_text).font.size = Pt(11)
    doc.add_page_break()


def parse_md_and_add_to_doc(doc, md_path):
    """Markdown을 파싱해 DOCX에 추가 (기본 파서)"""
    if not os.path.exists(md_path):
        print(f"  [SKIP] 파일 없음: {md_path}")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        if line.startswith("# "):
            doc.add_heading(line[2:], level=1)
        elif line.startswith("## "):
            doc.add_heading(line[3:], level=2)
        elif line.startswith("### "):
            doc.add_heading(line[4:], level=3)
        elif line.startswith("|"): # 테이블 (단순 처리)
            if not line.startswith("|-"):
                cells = [c.strip() for c in line.strip("|\n").split("|")]
                row_text = "  |  ".join(cells)
                p = doc.add_paragraph(row_text, style="List Bullet")
        elif line.startswith("- ") or line.startswith("* "):
            doc.add_paragraph(line[2:], style="List Bullet")
        elif line.startswith("  - "):
            doc.add_paragraph(line[4:], style="List Bullet 2")
        elif line == "" or line == "---":
            pass  # 빈 줄 / 수평선 무시
        else:
            if line.strip():
                doc.add_paragraph(line)

    doc.add_page_break()


def build_volume(vol_num, lang, output_dir="output"):
    """단일 볼륨 DOCX 생성"""
    config = VOLUME_MAP[str(vol_num)][lang]
    os.makedirs(output_dir, exist_ok=True)

    doc = Document()

    # 여백 설정
    for section in doc.sections:
        section.top_margin    = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin   = Inches(1.2)
        section.right_margin  = Inches(1.0)

    # 표지
    add_cover_page(doc, config["title"], config["subtitle"], lang)

    # 목차 placeholder
    doc.add_heading("목차" if lang == "KR" else "Table of Contents", level=1)
    doc.add_paragraph("[자동 목차 — Word에서 '참조 > 목차 업데이트' 실행]" if lang == "KR" else
                      "[Auto TOC — Update in Word via References > Update Table]")
    doc.add_page_break()

    # 각 챕터 MD 파일 병합
    base_dir = Path(__file__).parent.parent
    for md_file in config["files"]:
        md_path = base_dir / config["dir"] / md_file
        print(f"  → 병합: {md_path}")
        parse_md_and_add_to_doc(doc, str(md_path))

    # 저장
    vol_label = {"1": "기술편" if lang=="KR" else "Technical",
                 "2": "사업편" if lang=="KR" else "Business",
                 "3": "부록편" if lang=="KR" else "Appendix"}
    filename = f"BStar_eCO2_Vol{vol_num}_{vol_label[str(vol_num)]}_v2.0_{lang}.docx"
    out_path = os.path.join(output_dir, filename)
    doc.save(out_path)
    print(f"  ✅ 저장: {out_path}")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="B★ eCO₂ DOCX 병합 빌더")
    parser.add_argument("--vol",  default="all", help="볼륨 번호: 1, 2, 3, all")
    parser.add_argument("--lang", default="all", help="언어: KR, EN, all")
    parser.add_argument("--out",  default="output", help="출력 디렉토리")
    args = parser.parse_args()

    vols  = ["1","2","3"] if args.vol  == "all" else [args.vol]
    langs = ["KR","EN"]   if args.lang == "all" else [args.lang.upper()]

    print(f"\n🚀 B★ eCO₂ DOCX 병합 빌드 시작")
    print(f"   볼륨: {vols} | 언어: {langs} | 출력: {args.out}\n")

    results = []
    for vol in vols:
        for lang in langs:
            path = build_volume(vol, lang, args.out)
            results.append(path)

    print(f"\n✅ 완료 — {len(results)}개 파일 생성:")
    for r in results:
        size = os.path.getsize(r) / 1024 if os.path.exists(r) else 0
        print(f"   {r} ({size:.0f} KB)")


if __name__ == "__main__":
    main()

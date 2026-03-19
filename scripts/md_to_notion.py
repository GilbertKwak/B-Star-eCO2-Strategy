#!/usr/bin/env python3
"""
B★ eCO₂ — Notion 동기화 스크립트 v2.0
각 챕터 MD → Notion 페이지 업데이트
환경변수: NOTION_TOKEN
"""

import os
import json
import requests
from pathlib import Path

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Notion 페이지 ID 맵 (기존 확인된 페이지)
NOTION_PAGE_MAP = {
    "Ch01_KR": "32455ed4-36f0-81af-8b5d-e4f04678b0e4",
    "Ch02_KR": "32455ed4-36f0-8143-9114-cb9de65f47de",
    "Ch03_KR": "32455ed4-36f0-81d0-b4fd-e44fb18b567a",
    # Ch04~09: 작성 세션에서 생성된 페이지 ID로 업데이트 필요
    "Ch04_KR": "TBD",
    "Ch05_KR": "TBD",
    "Ch06_KR": "TBD",
    "Ch07_KR": "TBD",
    "Ch08_KR": "32355ed4-36f0-81dc-8080-f96f0d6e7b4d",  # 재무모델 허브
    "Ch09_KR": "TBD",
}


def md_to_notion_blocks(md_content: str) -> list:
    """Markdown → Notion Block 변환 (기본)"""
    blocks = []
    for line in md_content.split("\n"):
        if line.startswith("# "):
            blocks.append({"object": "block", "type": "heading_1",
                           "heading_1": {"rich_text": [{"text": {"content": line[2:]}}]}})
        elif line.startswith("## "):
            blocks.append({"object": "block", "type": "heading_2",
                           "heading_2": {"rich_text": [{"text": {"content": line[3:]}}]}})
        elif line.startswith("### "):
            blocks.append({"object": "block", "type": "heading_3",
                           "heading_3": {"rich_text": [{"text": {"content": line[4:]}}]}})
        elif line.startswith("- ") or line.startswith("* "):
            blocks.append({"object": "block", "type": "bulleted_list_item",
                           "bulleted_list_item": {"rich_text": [{"text": {"content": line[2:]}}]}})
        elif line.strip() and not line.startswith("|") and not line.startswith("---"):
            blocks.append({"object": "block", "type": "paragraph",
                           "paragraph": {"rich_text": [{"text": {"content": line}}]}})
    return blocks[:100]  # Notion API 블록 한계: 100개/요청


def sync_chapter(chapter_key: str, md_path: str):
    """단일 챕터 Notion 동기화"""
    page_id = NOTION_PAGE_MAP.get(chapter_key)
    if not page_id or page_id == "TBD":
        print(f"  [SKIP] {chapter_key}: Notion 페이지 ID 미설정")
        return False

    if not os.path.exists(md_path):
        print(f"  [SKIP] {chapter_key}: MD 파일 없음 ({md_path})")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = md_to_notion_blocks(content)
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    resp = requests.patch(url, headers=HEADERS, json={"children": blocks})

    if resp.status_code == 200:
        print(f"  ✅ {chapter_key}: Notion 동기화 완료")
        return True
    else:
        print(f"  [ERROR] {chapter_key}: {resp.status_code} {resp.text[:100]}")
        return False


def main():
    print("\n🔄 B★ eCO₂ Notion 동기화 시작\n")
    base = Path(__file__).parent.parent

    sync_map = {
        "Ch01_KR": base / "Vol1_Technical/KR/Ch01_KR.md",
        "Ch02_KR": base / "Vol1_Technical/KR/Ch02_KR.md",
        "Ch03_KR": base / "Vol1_Technical/KR/Ch03_KR.md",
        "Ch04_KR": base / "Vol1_Technical/KR/Ch04_KR.md",
        "Ch05_KR": base / "Vol2_Business/KR/Ch05_KR.md",
        "Ch06_KR": base / "Vol2_Business/KR/Ch06_KR.md",
        "Ch07_KR": base / "Vol2_Business/KR/Ch07_KR.md",
        "Ch08_KR": base / "Vol2_Business/KR/Ch08_KR.md",
        "Ch09_KR": base / "Vol2_Business/KR/Ch09_KR.md",
    }

    ok, skip = 0, 0
    for key, path in sync_map.items():
        result = sync_chapter(key, str(path))
        if result: ok += 1
        else: skip += 1

    print(f"\n완료: {ok}개 동기화 | {skip}개 건너뜀")


if __name__ == "__main__":
    main()

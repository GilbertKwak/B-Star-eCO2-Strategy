#!/bin/bash
# B★ eCO₂ 전체 빌드 스크립트 v2.0
# 사용법: bash scripts/build_all.sh

set -e
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="$REPO_ROOT/output"

echo "====================================="
echo " B★ eCO₂ 전체 빌드 시작 v2.0"
echo " 경로: $REPO_ROOT"
echo "====================================="

# 1. 의존성 확인
python3 -c "import docx" 2>/dev/null || pip install python-docx -q

# 2. 출력 디렉토리 초기화
mkdir -p "$OUTPUT_DIR"

# 3. Vol.1~3 KR+EN 전체 병합 (6개 DOCX)
echo "\n[1/3] DOCX 병합..."
python3 "$REPO_ROOT/scripts/merge_to_docx.py" --vol all --lang all --out "$OUTPUT_DIR"

# 4. Notion 동기화 (NOTION_TOKEN 환경변수 필요)
if [ -n "$NOTION_TOKEN" ]; then
    echo "\n[2/3] Notion 동기화..."
    python3 "$REPO_ROOT/scripts/md_to_notion.py"
else
    echo "\n[2/3] SKIP: NOTION_TOKEN 미설정"
fi

# 5. 결과 요약
echo "\n[3/3] 빌드 결과:"
ls -lh "$OUTPUT_DIR"/*.docx 2>/dev/null || echo "DOCX 파일 없음"

echo "\n✅ 빌드 완료!"

#!/usr/bin/env python3
"""data/ 配下の生成済みJSONを検証する。

- index.json と各章JSONの整合性
- id の一意性 / 必須フィールド / answer のインデックス範囲 / choices 件数
- 模試の出題比率（distribution）に対して各章の問題数が足りているか

使い方:  python3 tools/validate_data.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

REQUIRED = {"id", "chapter", "topic", "difficulty", "type", "question", "choices", "answer", "explanation"}
# js/data.js の EXAM.distribution と一致させること
DISTRIBUTION = {1: 1, 2: 2, 3: 7, 4: 2, 5: 1, 6: 4, 8: 2, 9: 5,
                10: 2, 11: 2, 13: 3, 14: 2, 16: 3, 17: 2, 18: 2}


def main():
    errors = []
    with open(os.path.join(DATA, "index.json"), encoding="utf-8") as f:
        index = json.load(f)

    seen_ids = set()
    total = 0
    per_chapter = {}
    for ch in index["chapters"]:
        path = os.path.join(DATA, ch["file"])
        if not os.path.exists(path):
            errors.append(f"{ch['file']} が存在しない")
            continue
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        per_chapter[ch["chapter"]] = len(items)
        if ch["count"] != len(items):
            errors.append(f"{ch['file']}: index の count({ch['count']}) と実数({len(items)})が不一致")
        for it in items:
            total += 1
            missing = REQUIRED - set(it)
            if missing:
                errors.append(f"{it.get('id', '?')}: 必須フィールド不足 {missing}")
                continue
            if it["id"] in seen_ids:
                errors.append(f"{it['id']}: id が重複")
            seen_ids.add(it["id"])
            if it["chapter"] != ch["chapter"]:
                errors.append(f"{it['id']}: chapter 不一致")
            n = len(it["choices"])
            if n < 2:
                errors.append(f"{it['id']}: choices が少なすぎる({n})")
            if not it["answer"]:
                errors.append(f"{it['id']}: answer が空")
            for a in it["answer"]:
                if not isinstance(a, int) or a < 0 or a >= n:
                    errors.append(f"{it['id']}: answer インデックス {a} が範囲外(0..{n-1})")
            if it["type"] == "single" and len(it["answer"]) != 1:
                errors.append(f"{it['id']}: single なのに answer が複数")
            if it["difficulty"] not in (1, 2, 3):
                errors.append(f"{it['id']}: difficulty 不正 {it['difficulty']}")

    # 模試の比率を満たせるか
    for ch, need in DISTRIBUTION.items():
        have = per_chapter.get(ch, 0)
        if have < need:
            errors.append(f"第{ch}章: 模試出題数 {need} に対し問題が {have} 件しかない")

    print(f"index total={index['total']} / 実カウント={total} / 章数={len(index['chapters'])}")
    print("章別:", per_chapter)
    if index["total"] != total:
        errors.append(f"index.total({index['total']}) と実数({total})が不一致")

    if errors:
        print(f"\n‼ 検証エラー {len(errors)} 件:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print(f"検証OK: 全{total}問・id一意・answer範囲・必須項目・模試比率すべて問題なし")


if __name__ == "__main__":
    main()

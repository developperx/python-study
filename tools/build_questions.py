#!/usr/bin/env python3
"""問題バンクのビルド & 自動検証スクリプト。

- 全問題を Python データとして定義し、data/chNN.json と data/index.json を生成する。
- verify=True の出力予測問題は、code を実際に実行して stdout が正解選択肢と一致するか検証する。
  （= コード問題の正解ミスを機械的に検出できる）
- 出題はすべてオリジナル作問。公式問題・書籍本文の転載はしていない。

使い方:  python3 tools/build_questions.py
"""
import io
import json
import os
import sys
import contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

# 章メタ（出題対象の15章。7/12/15/19章は試験範囲外のため除外）
CHAPTERS = [
    (1,  "Pythonの環境",                       "環境",         "2.5%"),
    (2,  "コーディング規約",                   "規約",         "5.0%"),
    (3,  "Pythonの言語仕様",                   "言語仕様",     "17.5%"),
    (4,  "Pythonのクラス",                     "クラス",       "5.0%"),
    (5,  "型ヒント",                           "型ヒント",     "2.5%"),
    (6,  "テキストの処理",                     "テキスト",     "10.0%"),
    (8,  "日付と時刻の処理",                   "日付時刻",     "5.0%"),
    (9,  "データ型とアルゴリズム",             "データ型",     "12.5%"),
    (10, "汎用OS・ランタイムサービス",         "OS",           "5.0%"),
    (11, "ファイルとディレクトリへのアクセス", "ファイル",     "5.0%"),
    (13, "特定のデータフォーマットを扱う",     "データ形式",   "7.5%"),
    (14, "インターネット上のデータを扱う",     "ネット",       "5.0%"),
    (16, "テスト",                             "テスト",       "7.5%"),
    (17, "デバッグ",                           "デバッグ",     "5.0%"),
    (18, "暗号関連",                           "暗号",         "2.5%"),
]

_bank = {}   # chapter -> list[dict]
_counter = {}


def q(chapter, topic, difficulty, question, choices, answer,
      explanation, reference="", code=None, type="single", verify=False,
      rat=None):
    """1問を登録する。answer は 0 始まりの index か index のリスト。

    rat: 各選択肢の正誤理由のリスト（choices と同じ長さ）。
         省略時はビルド時に「正解／不正解」の最小限の理由を自動補完する。
    """
    _counter[chapter] = _counter.get(chapter, 0) + 1
    qid = f"ch{chapter:02d}-{_counter[chapter]:03d}"
    ans = answer if isinstance(answer, list) else [answer]
    ansset = set(ans)
    if rat is None:
        rationales = [("正解。" if i in ansset else "不正解。")
                      for i in range(len(choices))]
    else:
        rationales = [
            (("正解。" if i in ansset else "不正解。") + r if r and not r.startswith(("正解", "不正解", "○", "×")) else (r or ("正解。" if i in ansset else "不正解。")))
            for i, r in enumerate(rat)
        ]
    item = {
        "id": qid,
        "chapter": chapter,
        "topic": topic,
        "difficulty": difficulty,
        "type": "multiple" if (type == "multiple" or len(ans) > 1) else "single",
        "question": question,
        "choices": choices,
        "answer": ans,
        "explanation": explanation,
        "rationales": rationales,
    }
    if code:
        item["code"] = code
    if reference:
        item["reference"] = reference
    item["_verify"] = verify
    if rat is not None and len(rat) != len(choices):
        raise ValueError(f"{qid}: rat の長さ({len(rat)})が choices({len(choices)})と不一致")
    _bank.setdefault(chapter, []).append(item)
    return item


def _run(code):
    """code を実行し stdout を返す。"""
    buf = io.StringIO()
    g = {"__name__": "__main__"}
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
        exec(compile(code, "<q>", "exec"), g)
    return buf.getvalue()


def verify_all():
    """verify=True の問題のコードを実行して正解選択肢と照合。"""
    errors = []
    checked = 0
    for ch, items in _bank.items():
        for it in items:
            if not it.get("_verify"):
                continue
            checked += 1
            if "code" not in it:
                errors.append(f"{it['id']}: verify=True だが code が無い")
                continue
            if len(it["answer"]) != 1:
                errors.append(f"{it['id']}: verify は単一正解のみ対応")
                continue
            try:
                out = _run(it["code"]).strip()
            except Exception as e:  # noqa
                errors.append(f"{it['id']}: 実行エラー {type(e).__name__}: {e}")
                continue
            expected = it["choices"][it["answer"][0]].strip()
            if out != expected:
                errors.append(
                    f"{it['id']}: 実行結果と正解が不一致\n    実行: {out!r}\n    正解: {expected!r}")
    return checked, errors


def write():
    os.makedirs(DATA, exist_ok=True)
    index_chapters = []
    total = 0
    for num, title, short, weight in CHAPTERS:
        items = _bank.get(num, [])
        # _verify は出力しない
        clean = []
        for it in items:
            d = {k: v for k, v in it.items() if not k.startswith("_")}
            clean.append(d)
        fname = f"ch{num:02d}.json"
        with open(os.path.join(DATA, fname), "w", encoding="utf-8") as f:
            json.dump(clean, f, ensure_ascii=False, indent=1)
        index_chapters.append({
            "chapter": num, "title": title, "shortTitle": short,
            "weight": weight, "file": fname, "count": len(clean),
        })
        total += len(clean)
    with open(os.path.join(DATA, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"total": total, "chapters": index_chapters}, f,
                  ensure_ascii=False, indent=1)
    return total


def main():
    import define_questions  # noqa: F401  問題定義を読み込み（同ディレクトリ）
    define_questions.register(q)
    checked, errors = verify_all()
    total = write()
    print(f"書き出し完了: {total} 問 / 検証(コード実行): {checked} 問")
    per = {c[0]: len(_bank.get(c[0], [])) for c in CHAPTERS}
    print("章別:", per)
    if errors:
        print(f"\n‼ 検証エラー {len(errors)} 件:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("検証OK: コード出力問題はすべて正解と一致")


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()

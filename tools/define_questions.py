# -*- coding: utf-8 -*-
"""全問題の定義。register(q) に問題を登録する。すべてオリジナル作問。

difficulty: 1=易 / 2=標準 / 3=難
verify=True の問題は code を実行して正解を機械検証する（出力予測問題）。
"""


def register(q):
    # 各章の関数を順に呼ぶ
    ch01(q); ch02(q); ch03(q); ch04(q); ch05(q); ch06(q)
    ch08(q); ch09(q); ch10(q); ch11(q); ch13(q); ch14(q)
    ch16(q); ch17(q); ch18(q)


# ============================================================
# 第1章 Pythonの環境
# ============================================================
def ch01(q):
    q(1, "仮想環境", 1,
      "標準ライブラリだけを使い、プロジェクト専用の仮想環境を作成するコマンドとして正しいものはどれか。",
      ["python -m venv .venv", "python -m virtualenv .venv", "pip install venv", "python -m pip venv .venv"],
      0,
      "仮想環境は標準ライブラリの venv モジュールで作成する。`python -m venv <dir>` が正しい。virtualenv はサードパーティ製で標準ではない。",
      "venv --- 仮想環境の作成")

    q(1, "pip", 1,
      "インストール済みパッケージの一覧を、requirements.txt 形式で出力するコマンドはどれか。",
      ["pip freeze", "pip list --all", "pip show", "pip dump"],
      0,
      "`pip freeze` は `名前==バージョン` の形式で一覧を出力し、requirements.txt の生成に使う。`pip list` は表形式で freeze 形式ではない。",
      "pip freeze")

    q(1, "モジュール実行", 2,
      "コマンドラインからモジュールをスクリプトとして実行するオプションはどれか。",
      ["python -m モジュール名", "python -c モジュール名", "python -x モジュール名", "python --run モジュール名"],
      0,
      "`-m` は指定したモジュールを sys.path から探して __main__ として実行する。`-c` は文字列のコードを実行するオプション。",
      "コマンドラインと環境 --- -m")

    q(1, "インタプリタ", 1,
      "Python本体のバージョンを表示するコマンドとして正しいものを選べ。",
      ["python --version", "python --ver", "python -version", "python version"],
      0,
      "`python --version`（または `-V`）でバージョンを表示する。",
      "コマンドライン")

    q(1, "sys", 2,
      "次のコードを Python 3 で実行したときの出力として正しいものはどれか。",
      ["3", "3.11", "python3", "エラー"],
      0,
      "sys.version_info はバージョン情報の名前付きタプルで、major 属性はメジャーバージョン番号（整数の3）を返す。",
      "sys.version_info",
      code="import sys\nprint(sys.version_info.major)",
      verify=True)

    q(1, "pip", 2,
      "特定バージョン 2.28.1 のパッケージ requests を pip でインストールするコマンドはどれか。",
      ["pip install requests==2.28.1", "pip install requests:2.28.1", "pip install requests-2.28.1", "pip install requests@2.28.1"],
      0,
      "バージョン指定は `パッケージ名==バージョン` の形式で行う。",
      "pip --- バージョン指定")

    q(1, "仮想環境", 2,
      "仮想環境を有効化（activate）する目的として最も適切なものはどれか。",
      ["そのシェルで python / pip が仮想環境内のものを指すようにする",
       "仮想環境を新規に作成する",
       "インストール済みパッケージをすべて削除する",
       "Python本体をアップグレードする"],
      0,
      "activate するとシェルの PATH が書き換わり、python・pip がその仮想環境のものを指すようになる。作成は venv、活性化は activate と役割が分かれている。",
      "venv --- activate")

    q(1, "対話モード", 1,
      "Python の対話モード（REPL）で、直前の式の評価結果を参照する変数はどれか。",
      ["_", "$", "ans", "it"],
      0,
      "対話モードでは直前に評価した式の結果がアンダースコア `_` に格納される。",
      "対話モード --- _")


# ============================================================
# 第2章 コーディング規約
# ============================================================
def ch02(q):
    q(2, "PEP8", 1,
      "PEP 8 が推奨するインデントの方法として正しいものはどれか。",
      ["スペース4つ", "タブ1つ", "スペース2つ", "タブとスペースの混在"],
      0,
      "PEP 8 はインデントに半角スペース4つを推奨している。タブとスペースの混在は禁止。",
      "PEP 8 --- インデント")

    q(2, "PEP8", 1,
      "PEP 8 が推奨する1行の最大文字数はどれか。",
      ["79文字", "80文字", "100文字", "120文字"],
      0,
      "PEP 8 ではコード行は最大79文字、docstring・コメントは72文字を推奨している。",
      "PEP 8 --- 行の長さ")

    q(2, "命名規約", 2,
      "PEP 8 における関数名・変数名の推奨スタイルはどれか。",
      ["snake_case（小文字とアンダースコア）", "camelCase", "PascalCase", "UPPER_CASE"],
      0,
      "関数名・変数名は snake_case。クラス名は PascalCase（CapWords）、定数は UPPER_CASE が推奨される。",
      "PEP 8 --- 命名規約")

    q(2, "命名規約", 2,
      "PEP 8 におけるクラス名の推奨スタイルはどれか。",
      ["CapWords（PascalCase）", "snake_case", "camelCase", "UPPER_SNAKE_CASE"],
      0,
      "クラス名は各単語の先頭を大文字にする CapWords 方式（例: MyClass）が推奨される。",
      "PEP 8 --- クラス名")

    q(2, "命名規約", 2,
      "PEP 8 における定数の推奨スタイルはどれか。",
      ["MAX_COUNT のように全て大文字とアンダースコア", "maxCount", "MaxCount", "max_count"],
      0,
      "モジュールレベルの定数は全て大文字＋アンダースコア区切り（例: MAX_OVERFLOW）が推奨される。",
      "PEP 8 --- 定数")

    q(2, "import", 2,
      "PEP 8 における import 文の並び順として正しいものはどれか。",
      ["標準ライブラリ → サードパーティ → ローカル の順にグループ化",
       "ローカル → サードパーティ → 標準ライブラリ の順",
       "アルファベット順のみで分類しない",
       "使う直前に書き、ファイル先頭にまとめない"],
      0,
      "import は (1)標準ライブラリ (2)サードパーティ (3)自作（ローカル）の順にグループ分けし、各グループを空行で区切る。",
      "PEP 8 --- インポート")

    q(2, "import", 2,
      "PEP 8 が推奨する import の書き方として正しいものはどれか。",
      ["import os\\nimport sys のように1行に1モジュール",
       "import os, sys のように1行にまとめる",
       "from os import * を推奨",
       "import は関数内に書くのが原則"],
      0,
      "複数モジュールを import するときは1行に1つずつ書く。`import os, sys` は非推奨。ワイルドカード import も避ける。",
      "PEP 8 --- インポート")

    q(2, "空白", 2,
      "PEP 8 の空白に関する規約として正しいものはどれか。",
      ["カンマの前には空白を入れず、後ろに1つ入れる",
       "関数呼び出しの括弧の内側に空白を入れる",
       "二項演算子の前後に空白を入れない",
       "代入演算子 = の前後は常に空白を入れない"],
      0,
      "カンマ・セミコロンの前に空白を置かず後ろに1つ。括弧の内側直後には空白を置かない。キーワード引数のデフォルト指定の = は前後に空白を入れない。",
      "PEP 8 --- 式と文中の空白")

    q(2, "比較", 2,
      "PEP 8 が推奨する、None との比較方法はどれか。",
      ["if x is None:", "if x == None:", "if x = None:", "if None(x):"],
      0,
      "None はシングルトンなので、`==` ではなく `is` / `is not` で比較するのが PEP 8 の推奨。",
      "PEP 8 --- 推奨事項")

    q(2, "docstring", 2,
      "ドキュメンテーション文字列（docstring）の規約を定めた PEP はどれか。",
      ["PEP 257", "PEP 8", "PEP 20", "PEP 484"],
      0,
      "PEP 257 が docstring の規約。PEP 8 はコーディング規約、PEP 20 は The Zen of Python、PEP 484 は型ヒント。",
      "PEP 257")

    q(2, "PEP20", 1,
      "対話モードで `import this` を実行すると表示されるものはどれか。",
      ["The Zen of Python（Pythonの設計哲学）", "ライセンス文", "インストール済みパッケージ一覧", "現在時刻"],
      0,
      "`import this` は PEP 20「The Zen of Python」を表示するイースターエッグ。",
      "PEP 20")

    q(2, "ツール", 2,
      "PEP 8 準拠かどうかをチェックする静的解析ツールとして代表的なものはどれか。",
      ["flake8 / pycodestyle", "pytest", "venv", "pdb"],
      0,
      "pycodestyle（旧 pep8）や flake8 がスタイルチェックに使われる。pytest はテスト、pdb はデバッガ。",
      "コーディング規約チェックツール")

    q(2, "コメント", 2,
      "PEP 8 のコメントに関する規約として正しいものはどれか。",
      ["インラインコメントはコードと少なくとも2スペース空け、# の後に1スペース",
       "コメントは必ず英語で書かなければならない",
       "ブロックコメントの # の後ろに空白を入れてはならない",
       "インラインコメントはコードに密着させる"],
      0,
      "インラインコメントは文と最低2スペース空け、`#` の直後に空白を1つ入れる。言語の指定はない。",
      "PEP 8 --- コメント")

    q(2, "命名規約", 3,
      "PEP 8 で、予約語と衝突する場合に推奨される変数名の付け方はどれか。",
      ["末尾にアンダースコアを付ける（例: class_）",
       "先頭に2つアンダースコアを付ける",
       "全て大文字にする",
       "数字を付ける（例: class1）"],
      0,
      "予約語と被る場合は、略語や綴り変更より末尾にアンダースコアを付ける（trailing underscore）方法が推奨される。",
      "PEP 8 --- 命名のヒント")

    q(2, "PEP8", 3,
      "PEP 8 における、トップレベルの関数定義やクラス定義の前後に入れる空行の数はどれか。",
      ["2行", "1行", "3行", "0行（空けない）"],
      0,
      "トップレベルの関数・クラス定義は前後を2行空ける。クラス内のメソッド定義は1行空ける。",
      "PEP 8 --- 空行")


# ============================================================
# 第3章 Pythonの言語仕様
# ============================================================
def ch03(q):
    q(3, "数値", 1,
      "次のコードの出力として正しいものはどれか。",
      ["3", "2", "2.5", "2.0"],
      0,
      "`//` は整数除算（切り捨て除算）。5 // 2 は商の整数部 2 ではなく、5//2=2。ここでは 7//2=3 となる。",
      "算術演算 --- //",
      code="print(7 // 2)", verify=True)

    q(3, "数値", 1,
      "次のコードの出力として正しいものはどれか。",
      ["8", "9", "6", "512"],
      0,
      "`**` はべき乗演算子。2 ** 3 は 2 の 3 乗 = 8。",
      "算術演算 --- **",
      code="print(2 ** 3)", verify=True)

    q(3, "数値", 2,
      "次のコードの出力として正しいものはどれか。",
      ["1", "-1", "2", "-2"],
      0,
      "`%` の結果は除数（右辺）と同じ符号になる。-7 % 4 は 1（-7 = 4*(-2) + 1）。",
      "剰余演算 --- %",
      code="print(-7 % 4)", verify=True)

    q(3, "真偽値", 2,
      "次のコードの出力として正しいものはどれか。",
      ["3", "0", "True", "1"],
      0,
      "`or` は最初の真の値を返す（短絡評価）。0 は偽なので次の 3 が返る。",
      "ブール演算 --- or",
      code="print(0 or 3)", verify=True)

    q(3, "真偽値", 2,
      "次のコードの出力として正しいものはどれか。",
      ["0", "3", "False", "None"],
      0,
      "`and` は最初の偽の値を返し、すべて真なら最後の値を返す。0 が偽なので 0 が返る。",
      "ブール演算 --- and",
      code="print(0 and 3)", verify=True)

    q(3, "比較", 2,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "None"],
      0,
      "Python は比較演算子を連鎖できる。1 < 2 < 3 は (1<2) and (2<3) と等価で True。",
      "比較の連鎖",
      code="print(1 < 2 < 3)", verify=True)

    q(3, "is と ==", 2,
      "`is` 演算子の説明として正しいものはどれか。",
      ["2つのオブジェクトが同一（同じid）かを判定する",
       "2つの値が等しいかを判定する",
       "型が等しいかを判定する",
       "文字列が含まれるかを判定する"],
      0,
      "`is` は同一性（identity, id が同じか）、`==` は等価性（値が等しいか）を判定する。",
      "is 演算子")

    q(3, "リスト", 1,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3, 4]", "[1, 2, [3, 4]]", "[4, 3, 2, 1]", "エラー"],
      0,
      "リストの `+` は連結。[1,2] + [3,4] は [1, 2, 3, 4]。",
      "シーケンス演算 --- +",
      code="print([1, 2] + [3, 4])", verify=True)

    q(3, "スライス", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2]", "[0, 1]", "[1, 2, 3]", "[0, 1, 2]"],
      0,
      "スライス [start:stop] は stop を含まない。[0,1,2,3][1:3] はインデックス1,2の要素 [1, 2]。",
      "スライス",
      code="print([0, 1, 2, 3][1:3])", verify=True)

    q(3, "スライス", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[3, 2, 1, 0]", "[0, 1, 2, 3]", "[0, 2]", "エラー"],
      0,
      "ステップに -1 を指定すると逆順になる。[::-1] は全要素を逆順にしたリストを返す。",
      "スライス --- ステップ",
      code="print([0, 1, 2, 3][::-1])", verify=True)

    q(3, "スライス", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[0, 2, 4]", "[0, 1, 2]", "[1, 3, 5]", "[0, 2, 4, 6]"],
      0,
      "[start:stop:step] でステップ2。range(6)=0..5 を 0 から 2 飛ばしで取ると 0,2,4。",
      "スライス --- ステップ",
      code="print(list(range(6))[::2])", verify=True)

    q(3, "文字列", 1,
      "次のコードの出力として正しいものはどれか。",
      ["ababab", "abababab", "['ab', 'ab', 'ab']", "エラー"],
      0,
      "文字列 * 整数 は繰り返し。'ab' * 3 は 'ababab'。",
      "シーケンス演算 --- *",
      code="print('ab' * 3)", verify=True)

    q(3, "f文字列", 2,
      "次のコードの出力として正しいものはどれか。",
      ["x=10", "x={x}", "x=x", "{x}=10"],
      0,
      "f文字列では `{式}` が値に置換される。x=10 なので 'x=10'。",
      "フォーマット済み文字列リテラル",
      code="x = 10\nprint(f'x={x}')", verify=True)

    q(3, "関数", 2,
      "次のコードの出力として正しいものはどれか。",
      ["6", "(1, 2, 3)", "[1, 2, 3]", "123"],
      0,
      "`*args` は可変長位置引数をタプルで受け取る。sum で合計され 1+2+3=6。",
      "可変長引数 --- *args",
      code="def f(*args):\n    return sum(args)\nprint(f(1, 2, 3))", verify=True)

    q(3, "関数", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{'a': 1, 'b': 2}", "['a', 'b']", "[1, 2]", "(1, 2)"],
      0,
      "`**kwargs` はキーワード引数を辞書で受け取る。",
      "可変長引数 --- **kwargs",
      code="def f(**kwargs):\n    return kwargs\nprint(f(a=1, b=2))", verify=True)

    q(3, "関数", 2,
      "デフォルト引数に関する次のコードを2回呼び出したときの出力はどれか。",
      ["[1]\n[1, 2]", "[1]\n[2]", "[1, 2]\n[1, 2]", "エラー"],
      0,
      "デフォルト引数はデフォルト値（リスト）が関数定義時に一度だけ生成され共有される。可変オブジェクトをデフォルトにすると状態が持ち越される典型的な罠。",
      "デフォルト引数値の評価タイミング",
      code="def f(x, lst=[]):\n    lst.append(x)\n    return lst\nprint(f(1))\nprint(f(2))", verify=True)

    q(3, "関数", 2,
      "可変オブジェクトをデフォルト引数にする問題を避ける慣用句として正しいものはどれか。",
      ["def f(lst=None): lst = lst or [] のように None を既定にする",
       "def f(lst=[]) のままで問題ない",
       "グローバル変数を使う",
       "デフォルト引数は使えない"],
      0,
      "可変デフォルト値の共有を避けるには、既定を None にして関数内で新しいリストを生成するのが定石。",
      "デフォルト引数のイディオム")

    q(3, "lambda", 2,
      "次のコードの出力として正しいものはどれか。",
      ["25", "10", "lambda", "エラー"],
      0,
      "lambda は無名関数。`(lambda x: x*x)(5)` は 5 の2乗で 25。",
      "ラムダ式",
      code="print((lambda x: x * x)(5))", verify=True)

    q(3, "内包表記", 1,
      "次のコードの出力として正しいものはどれか。",
      ["[0, 1, 4, 9]", "[1, 2, 3]", "[0, 1, 2, 3]", "[1, 4, 9]"],
      0,
      "リスト内包表記。range(4)=0,1,2,3 の各2乗で [0, 1, 4, 9]。",
      "リスト内包表記",
      code="print([x**2 for x in range(4)])", verify=True)

    q(3, "内包表記", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[0, 2, 4]", "[1, 3, 5]", "[0, 1, 2, 3, 4, 5]", "[2, 4]"],
      0,
      "条件付き内包表記。0..5 のうち偶数（x%2==0）だけを残す。",
      "内包表記 --- 条件",
      code="print([x for x in range(6) if x % 2 == 0])", verify=True)

    q(3, "内包表記", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{0, 1, 2}", "[0, 1, 2]", "{0: 0, 1: 1, 2: 2}", "(0, 1, 2)"],
      0,
      "`{}` で要素のみを書くと集合内包表記。重複のない set が得られる。",
      "集合内包表記",
      code="print({x for x in range(3)})", verify=True)

    q(3, "内包表記", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{0: 0, 1: 1, 2: 4}", "{0, 1, 4}", "[0, 1, 4]", "(0, 1, 4)"],
      0,
      "`{キー: 値 for ...}` は辞書内包表記。x:x**2 で {0:0, 1:1, 2:4}。",
      "辞書内包表記",
      code="print({x: x**2 for x in range(3)})", verify=True)

    q(3, "ジェネレータ", 3,
      "次のコードの出力として正しいものはどれか。",
      ["<class 'generator'>", "<class 'list'>", "<class 'tuple'>", "<class 'function'>"],
      0,
      "丸括弧の内包表記はジェネレータ式で、generator オブジェクトを生成する（リストではない）。",
      "ジェネレータ式",
      code="g = (x for x in range(3))\nprint(type(g))",
      verify=True)

    q(3, "ジェネレータ", 2,
      "yield を含む関数を呼び出したときに返るものはどれか。",
      ["ジェネレータオブジェクト", "最初の yield の値", "None", "リスト"],
      0,
      "yield を含む関数（ジェネレータ関数）を呼ぶと、本体は実行されずジェネレータオブジェクトが返る。next() や for で値が取り出される。",
      "yield 式")

    q(3, "アンパック", 2,
      "次のコードの出力として正しいものはどれか。",
      ["1 [2, 3]", "1 2 3", "[1] [2, 3]", "エラー"],
      0,
      "`a, *b = ...` の星付きターゲットは残りをリストで受け取る。a=1, b=[2,3]。",
      "アンパック代入 --- *",
      code="a, *b = [1, 2, 3]\nprint(a, b)", verify=True)

    q(3, "アンパック", 1,
      "次のコードの出力として正しいものはどれか。",
      ["2 1", "1 2", "(2, 1)", "エラー"],
      0,
      "タプルのアンパックで2変数を同時に入れ替えられる。a,b = b,a により a=2, b=1。",
      "多重代入による入れ替え",
      code="a, b = 1, 2\na, b = b, a\nprint(a, b)", verify=True)

    q(3, "例外", 2,
      "例外処理で、例外の有無にかかわらず必ず実行される節はどれか。",
      ["finally", "else", "except", "ensure"],
      0,
      "`finally` 節は例外発生の有無に関係なく必ず実行される。`else` は例外が起きなかった場合のみ実行される。",
      "try 文 --- finally")

    q(3, "例外", 2,
      "次のコードの出力として正しいものはどれか。",
      ["caught", "0", "エラーで停止", "done"],
      0,
      "1/0 で ZeroDivisionError が発生し except で捕捉、'caught' を出力する。",
      "例外処理",
      code="try:\n    1 / 0\nexcept ZeroDivisionError:\n    print('caught')", verify=True)

    q(3, "例外", 3,
      "raise した独自例外を作るとき、継承すべき基底クラスとして最も一般的なものはどれか。",
      ["Exception", "BaseException", "object", "StopIteration"],
      0,
      "ユーザー定義例外は通常 Exception を継承する。BaseException は SystemExit 等も含む最上位で、直接継承は推奨されない。",
      "例外 --- ユーザー定義例外")

    q(3, "with文", 2,
      "with 文（コンテキストマネージャ）の主な利点はどれか。",
      ["ブロックを抜けるときにリソースの後始末（close等）を自動で行う",
       "処理速度が必ず速くなる",
       "例外を必ず無視する",
       "変数のスコープをグローバルにする"],
      0,
      "with 文は __enter__/__exit__ を使い、ブロック終了時（例外時も含む）に確実に後始末を行う。ファイルクローズ等に使う。",
      "with 文")

    q(3, "スコープ", 3,
      "関数内からグローバル変数へ代入できるようにするキーワードはどれか。",
      ["global", "nonlocal", "extern", "public"],
      0,
      "`global x` で x をグローバル変数として扱える。`nonlocal` は1つ外側（ネスト関数）の変数を指す。",
      "global 文")

    q(3, "スコープ", 3,
      "Python の名前解決の順序（スコープ）を表す略語はどれか。",
      ["LEGB（Local → Enclosing → Global → Built-in）",
       "GLOB", "BGEL", "OOP"],
      0,
      "名前は Local → Enclosing（外側の関数）→ Global（モジュール）→ Built-in の順に探索される（LEGB則）。",
      "名前解決 --- LEGB")

    q(3, "クロージャ", 3,
      "次のコードの出力として正しいものはどれか。",
      ["15", "5", "10", "エラー"],
      0,
      "make_adder(10) が x=10 を閉じ込めたクロージャを返し、それに 5 を渡すので 15。",
      "クロージャ",
      code="def make_adder(x):\n    def add(y):\n        return x + y\n    return add\nprint(make_adder(10)(5))", verify=True)

    q(3, "三項演算子", 1,
      "次のコードの出力として正しいものはどれか。",
      ["even", "odd", "True", "0"],
      0,
      "条件式 `A if 条件 else B`。4%2==0 が真なので 'even'。",
      "条件式（三項演算子）",
      code="n = 4\nprint('even' if n % 2 == 0 else 'odd')", verify=True)

    q(3, "セイウチ演算子", 3,
      "Python 3.8 で導入された、式の中で代入を行う演算子（セイウチ演算子）はどれか。",
      [":=", "=>", "<-", "::"],
      0,
      "代入式（セイウチ演算子）`:=` は式の評価と同時に代入できる。例: if (n := len(a)) > 10:。",
      "代入式 :=")

    q(3, "真偽値", 2,
      "次のうち、ブール値として False と評価されるものはどれか（最も適切なものを選べ）。",
      ["空のリスト []", "[0]", "'False' という文字列", "1"],
      0,
      "空のシーケンス・コレクション（[]、''、{}、()）、0、None、False は偽。非空の 'False' 文字列や [0] は真。",
      "真理値判定")

    q(3, "文字列", 2,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "None"],
      0,
      "`in` 演算子は部分文字列の包含を判定する。'py' は 'python' に含まれるので True。",
      "in 演算子",
      code="print('py' in 'python')", verify=True)

    q(3, "ループ", 2,
      "for ループの else 節が実行されるのはどんなときか。",
      ["ループが break されずに最後まで回り切ったとき",
       "ループが1度も実行されなかったときのみ",
       "break されたとき", "例外が発生したとき"],
      0,
      "for/while の else 節は、ループが break で中断されずに正常終了したときに実行される。",
      "for-else")

    q(3, "ループ", 2,
      "次のコードの出力として正しいものはどれか。",
      ["found", "not found", "0\n1\n2", "エラー"],
      0,
      "2 を見つけて break するため else は実行されず 'found' のみ出力。",
      "for-else / break",
      code="for i in [1, 2, 3]:\n    if i == 2:\n        print('found')\n        break\nelse:\n    print('not found')", verify=True)

    q(3, "enumerate", 1,
      "次のコードの出力として正しいものはどれか。",
      ["0 a\n1 b", "1 a\n2 b", "a 0\nb 1", "a\nb"],
      0,
      "enumerate はインデックスと要素のタプルを返す。既定の開始は 0。",
      "enumerate",
      code="for i, v in enumerate(['a', 'b']):\n    print(i, v)", verify=True)

    q(3, "zip", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[(1, 'a'), (2, 'b')]", "[(1, 2), ('a', 'b')]", "[1, 'a', 2, 'b']", "エラー"],
      0,
      "zip は複数イテラブルを要素ごとに組にする。長さが違う場合は短い方に合わせる。",
      "zip",
      code="print(list(zip([1, 2], ['a', 'b'])))", verify=True)

    q(3, "デコレータ", 3,
      "デコレータ `@deco` を関数 f に付けることと等価なものはどれか。",
      ["f = deco(f)", "f = deco(f())", "deco = f(deco)", "f = f(deco)"],
      0,
      "`@deco` を付けた関数定義は、定義後に `f = deco(f)` を実行するのと等価。",
      "デコレータ")

    q(3, "可変・不変", 2,
      "次のうちイミュータブル（変更不可）な型はどれか。",
      ["タプル", "リスト", "辞書", "集合(set)"],
      0,
      "tuple・str・int・frozenset などはイミュータブル。list・dict・set はミュータブル。",
      "ミュータブル / イミュータブル")

    q(3, "参照", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3]", "[1, 2]", "エラー", "[3]"],
      0,
      "b = a はリストの参照のコピー。同じオブジェクトを指すため b.append の結果が a にも反映される。",
      "参照とエイリアス",
      code="a = [1, 2]\nb = a\nb.append(3)\nprint(a)", verify=True)

    q(3, "コピー", 3,
      "リスト a の浅いコピーを作る方法として誤っているものはどれか。",
      ["b = a", "b = a[:]", "b = list(a)", "b = a.copy()"],
      0,
      "`b = a` は参照の共有でコピーではない。スライス a[:]、list(a)、a.copy() は浅いコピーを作る。",
      "浅いコピー")

    q(3, "数値", 2,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "1"],
      0,
      "bool は int のサブクラスで True==1。よって True + True == 2 ではなく、ここでは True == 1 が True。",
      "bool と int",
      code="print(True == 1)", verify=True)

    q(3, "数値", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2", "True", "1", "エラー"],
      0,
      "True は 1、False は 0 として算術に使える。True + True = 2。",
      "bool の算術",
      code="print(True + True)", verify=True)

    q(3, "文字列", 2,
      "次のコードの出力として正しいものはどれか。",
      ["3", "2", "4", "エラー"],
      0,
      "len は要素数（文字列なら文字数）を返す。'abc' は3文字。",
      "len",
      code="print(len('abc'))", verify=True)

    q(3, "辞書", 2,
      "次のコードの出力として正しいものはどれか。",
      ["default", "None", "KeyError", "0"],
      0,
      "dict.get(key, default) はキーが無ければ default を返す（例外を出さない）。",
      "dict.get",
      code="d = {'a': 1}\nprint(d.get('b', 'default'))", verify=True)

    q(3, "演算子", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 1, 2]", "[2, 4]", "[1, 2, 2]", "エラー"],
      0,
      "リストの `*` は繰り返し連結。[1,2]*2 は [1, 2, 1, 2]。",
      "シーケンスの繰り返し",
      code="print([1, 2] * 2)", verify=True)

    q(3, "型変換", 1,
      "次のコードの出力として正しいものはどれか。",
      ["15", "123", "'123'", "エラー"],
      0,
      "int('12') は整数 12 に変換され、12 + 3 = 15 となる。文字列のままなら連結だが、int で数値化している点に注意。",
      "型変換 --- int()",
      code="print(int('12') + 3)", verify=True)

    q(3, "識別子", 1,
      "Python の識別子（変数名）として使えないものはどれか。",
      ["2nd", "_value", "値", "myVar"],
      0,
      "識別子は数字で始められない。'2nd' は不可。Unicode 文字（日本語）は使用可能。",
      "識別子の規則")


# ============================================================
# 第4章 Pythonのクラス
# ============================================================
def ch04(q):
    q(4, "コンストラクタ", 1,
      "インスタンス生成時に自動的に呼ばれる初期化メソッドはどれか。",
      ["__init__", "__new__", "__call__", "__construct__"],
      0,
      "`__init__` がインスタンスの初期化メソッド。__new__ は実際のインスタンス生成（通常は意識しない）。",
      "クラス --- __init__")

    q(4, "self", 1,
      "インスタンスメソッドの第1引数として慣例的に使われる名前はどれか。",
      ["self", "this", "cls", "me"],
      0,
      "インスタンスメソッドの第1引数は慣例で `self`（インスタンス自身）。クラスメソッドでは `cls`。",
      "メソッド --- self")

    q(4, "クラス変数", 2,
      "次のコードの出力として正しいものはどれか。",
      ["dog", "Animal", "None", "エラー"],
      0,
      "クラス変数 kind はインスタンスから参照できる。a.kind は 'dog'。",
      "クラス変数",
      code="class Animal:\n    kind = 'dog'\na = Animal()\nprint(a.kind)", verify=True)

    q(4, "継承", 2,
      "次のコードの出力として正しいものはどれか。",
      ["bark", "sound", "エラー", "None"],
      0,
      "Dog は Animal を継承し speak をオーバーライドしている。d.speak() は 'bark'。",
      "継承とオーバーライド",
      code="class Animal:\n    def speak(self):\n        return 'sound'\nclass Dog(Animal):\n    def speak(self):\n        return 'bark'\nprint(Dog().speak())", verify=True)

    q(4, "super", 2,
      "親クラスのメソッドを子クラスから呼び出す組み込み関数はどれか。",
      ["super()", "parent()", "base()", "self.super"],
      0,
      "`super()` で親クラス（MRO上の次のクラス）のメソッドを呼べる。",
      "super()")

    q(4, "super", 2,
      "次のコードの出力として正しいものはどれか。",
      ["hello from A", "hello from B", "エラー", "None"],
      0,
      "B.greet が super().greet() で A.greet を呼ぶため 'hello from A' が出力される。",
      "super() による親メソッド呼び出し",
      code="class A:\n    def greet(self):\n        print('hello from A')\nclass B(A):\n    def greet(self):\n        super().greet()\nB().greet()", verify=True)

    q(4, "クラスメソッド", 2,
      "クラスメソッドを定義するデコレータはどれか。",
      ["@classmethod", "@staticmethod", "@property", "@classfunc"],
      0,
      "`@classmethod` は第1引数に cls を取るクラスメソッドを定義する。",
      "@classmethod")

    q(4, "スタティックメソッド", 2,
      "self も cls も受け取らないメソッドを定義するデコレータはどれか。",
      ["@staticmethod", "@classmethod", "@property", "@method"],
      0,
      "`@staticmethod` は self/cls を取らず、名前空間としてクラスに属するだけのメソッド。",
      "@staticmethod")

    q(4, "プロパティ", 2,
      "メソッドを属性のようにアクセスできるようにするデコレータはどれか。",
      ["@property", "@attribute", "@getter", "@field"],
      0,
      "`@property` を付けると、メソッドを括弧なしの属性アクセスで呼び出せる（ゲッター）。",
      "@property")

    q(4, "特殊メソッド", 2,
      "print() や str() に渡したときの「人間向け」文字列表現を返す特殊メソッドはどれか。",
      ["__str__", "__repr__", "__format__", "__print__"],
      0,
      "`__str__` は print/str 向けの読みやすい表現、`__repr__` は開発者向けの厳密な表現を返す。",
      "特殊メソッド --- __str__")

    q(4, "特殊メソッド", 3,
      "次のコードの出力として正しいものはどれか。",
      ["P(1, 2)", "<__main__.P object>", "(1, 2)", "エラー"],
      0,
      "__repr__ を定義すると repr() や対話表示で使われる。ここでは print(repr(p)) 相当ではないが、__repr__ の戻り値が表示される。",
      "__repr__",
      code="class P:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f'P({self.x}, {self.y})'\nprint(P(1, 2))", verify=True)

    q(4, "特殊メソッド", 3,
      "len(obj) を可能にするために実装すべき特殊メソッドはどれか。",
      ["__len__", "__length__", "__size__", "__count__"],
      0,
      "組み込み len() はオブジェクトの `__len__` を呼ぶ。",
      "特殊メソッド --- __len__")

    q(4, "カプセル化", 2,
      "Python で「外部から触れてほしくない」ことを示す、属性名の慣例はどれか。",
      ["先頭にアンダースコア1つ（_name）", "末尾にアンダースコア（name_）", "全て大文字（NAME）", "@private を付ける"],
      0,
      "先頭 `_` は「内部用」という慣習的マーカー（強制力はない）。先頭 `__`（2つ）は名前マングリングが起こる。",
      "命名 --- 非公開属性")

    q(4, "名前マングリング", 3,
      "クラス内で `__x`（先頭アンダースコア2つ）と定義した属性に対して起こることはどれか。",
      ["_クラス名__x に名前が変換される（名前マングリング）",
       "完全に外部からアクセス不可能になる",
       "自動的に property になる",
       "定数になる"],
      0,
      "先頭2つのアンダースコアは `_ClassName__x` へ変換され、サブクラスとの名前衝突を避ける（完全な private ではない）。",
      "名前マングリング")

    q(4, "isinstance", 2,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "Dog"],
      0,
      "isinstance はサブクラスのインスタンスも True とする。Dog は Animal のサブクラスなので True。",
      "isinstance と継承",
      code="class Animal: pass\nclass Dog(Animal): pass\nprint(isinstance(Dog(), Animal))", verify=True)

    q(4, "dataclass", 3,
      "__init__ や __repr__ を自動生成するためにクラスへ付けるデコレータはどれか。",
      ["@dataclass", "@struct", "@record", "@autoinit"],
      0,
      "標準ライブラリ dataclasses の `@dataclass` を付けると、フィールドから __init__・__repr__・__eq__ などを自動生成する。",
      "dataclasses.dataclass")


# ============================================================
# 第5章 型ヒント
# ============================================================
def ch05(q):
    q(5, "型ヒント", 1,
      "型ヒント（型アノテーション）の仕様を定めた PEP はどれか。",
      ["PEP 484", "PEP 8", "PEP 257", "PEP 20"],
      0,
      "PEP 484 が型ヒントを導入した。typing モジュールもこれに基づく。",
      "PEP 484")

    q(5, "型ヒント", 1,
      "関数の引数と戻り値に型ヒントを付ける正しい構文はどれか。",
      ["def f(x: int) -> str:", "def f(x is int) returns str:", "def f(int x) -> str:", "def f(x: int) => str:"],
      0,
      "引数は `名前: 型`、戻り値は `-> 型` で書く。",
      "型ヒントの構文")

    q(5, "実行時", 2,
      "Python の型ヒントの実行時の扱いとして正しいものはどれか。",
      ["実行時には強制されず、原則チェックされない",
       "実行時に型が違うと必ず例外になる",
       "型ヒントを書くと自動でキャストされる",
       "型ヒントは構文エラーになる"],
      0,
      "型ヒントは原則として実行時に強制されない（ドキュメント・静的解析用）。チェックは mypy 等のツールで行う。",
      "型ヒントは実行時に強制されない")

    q(5, "ツール", 2,
      "型ヒントに基づく静的型チェックを行う代表的なツールはどれか。",
      ["mypy", "pytest", "flake8", "black"],
      0,
      "mypy が代表的な静的型チェッカー。pytest はテスト、flake8 はスタイル、black はフォーマッタ。",
      "mypy")

    q(5, "typing", 2,
      "「int のリスト」を表す型ヒントとして適切なものはどれか（Python 3.9以降の組み込み記法）。",
      ["list[int]", "List(int)", "int[]", "array[int]"],
      0,
      "Python 3.9 以降は組み込み型で `list[int]` と書ける。以前は typing.List[int] を使った。",
      "ジェネリック型 --- list[int]")

    q(5, "Optional", 2,
      "「int または None」を表す型ヒントとして適切なものはどれか。",
      ["Optional[int]", "Maybe[int]", "Nullable[int]", "int?"],
      0,
      "typing.Optional[int] は int | None を意味する。Python 3.10 以降は `int | None` とも書ける。",
      "typing.Optional")

    q(5, "Union", 2,
      "Python 3.10 以降で「int または str」を表す最も簡潔な記法はどれか。",
      ["int | str", "int & str", "Union(int, str)", "int, str"],
      0,
      "3.10 以降はパイプ演算子で `int | str` と書ける（PEP 604）。従来は typing.Union[int, str]。",
      "Union 型 --- |")

    q(5, "変数アノテーション", 2,
      "変数に型ヒントだけを付ける正しい構文はどれか。",
      ["count: int", "int count", "count = int", "count :: int"],
      0,
      "変数アノテーションは `変数名: 型`（必要なら `= 初期値`）の形式（PEP 526）。",
      "変数アノテーション")


# ============================================================
# 第6章 テキストの処理
# ============================================================
def ch06(q):
    q(6, "str method", 1,
      "次のコードの出力として正しいものはどれか。",
      ["ABC", "abc", "Abc", "エラー"],
      0,
      "str.upper() は全ての文字を大文字にする。",
      "str.upper",
      code="print('abc'.upper())", verify=True)

    q(6, "str method", 1,
      "次のコードの出力として正しいものはどれか。",
      ["hello", "HELLO", "Hello", "エラー"],
      0,
      "str.lower() は全て小文字にする。",
      "str.lower",
      code="print('HELLO'.lower())", verify=True)

    q(6, "str method", 1,
      "次のコードの出力として正しいものはどれか。",
      ["abc", " abc ", "abc ", " abc"],
      0,
      "str.strip() は前後の空白を除去する。",
      "str.strip",
      code="print('  abc  '.strip())", verify=True)

    q(6, "split", 2,
      "次のコードの出力として正しいものはどれか。",
      ["['a', 'b', 'c']", "['a,b,c']", "('a', 'b', 'c')", "'a b c'"],
      0,
      "str.split(',') は区切り文字でリストに分割する。",
      "str.split",
      code="print('a,b,c'.split(','))", verify=True)

    q(6, "split", 2,
      "区切り文字を指定せず str.split() を呼んだときの挙動として正しいものはどれか。",
      ["連続する空白をまとめて区切り、空文字を含めない",
       "1文字ずつ分割する",
       "改行のみで分割する",
       "エラーになる"],
      0,
      "引数なしの split() は任意個の空白（スペース・タブ・改行）を区切りとし、空要素を生成しない。",
      "str.split --- 引数なし")

    q(6, "join", 2,
      "次のコードの出力として正しいものはどれか。",
      ["a-b-c", "['a', 'b', 'c']", "abc", "a-b-c-"],
      0,
      "'区切り'.join(リスト) は要素を区切り文字で連結する。",
      "str.join",
      code="print('-'.join(['a', 'b', 'c']))", verify=True)

    q(6, "join", 2,
      "リスト ['1', '2', '3'] を 'カンマ＋空白' で連結した文字列を作る正しい式はどれか。",
      ["', '.join(['1', '2', '3'])", "['1', '2', '3'].join(', ')", "join(', ', ['1','2','3'])", "', '.concat(['1','2','3'])"],
      0,
      "join は区切り文字側のメソッド。`セパレータ.join(イテラブル)` の形。",
      "str.join")

    q(6, "replace", 1,
      "次のコードの出力として正しいものはどれか。",
      ["a-b-c", "abc", "a_b_c", "エラー"],
      0,
      "str.replace(old, new) は全ての出現を置換する。",
      "str.replace",
      code="print('a_b_c'.replace('_', '-'))", verify=True)

    q(6, "find", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2", "1", "-1", "3"],
      0,
      "str.find(sub) は最初に見つかったインデックスを返す。'c' は 'abcd' のインデックス2。",
      "str.find",
      code="print('abcd'.find('c'))", verify=True)

    q(6, "find", 2,
      "str.find と str.index の違いとして正しいものはどれか。",
      ["見つからないとき find は -1、index は ValueError を返す",
       "両方とも -1 を返す",
       "両方とも例外を出す",
       "find は例外、index は -1 を返す"],
      0,
      "find は未発見で -1、index は ValueError を送出する点が違う。",
      "str.find / str.index")

    q(6, "startswith", 1,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "None"],
      0,
      "str.startswith(prefix) は接頭辞で始まるかを判定する。",
      "str.startswith",
      code="print('python'.startswith('py'))", verify=True)

    q(6, "endswith", 1,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "None"],
      0,
      "str.endswith(suffix) は接尾辞で終わるかを判定する。'.txt' で終わるので True。",
      "str.endswith",
      code="print('data.txt'.endswith('.txt'))", verify=True)

    q(6, "count", 2,
      "次のコードの出力として正しいものはどれか。",
      ["3", "2", "1", "4"],
      0,
      "str.count(sub) は重ならない出現回数を返す。'banana' に 'a' は3回。",
      "str.count",
      code="print('banana'.count('a'))", verify=True)

    q(6, "format", 2,
      "次のコードの出力として正しいものはどれか。",
      ["name=Bob age=20", "name={} age={}", "Bob 20", "エラー"],
      0,
      "str.format() は {} を引数で順に置換する。",
      "str.format",
      code="print('name={} age={}'.format('Bob', 20))", verify=True)

    q(6, "format spec", 3,
      "次のコードの出力として正しいものはどれか。",
      ["003", "3", "300", "  3"],
      0,
      "書式指定 `:03d` は3桁・ゼロ埋め。3 は '003' になる。",
      "書式指定ミニ言語 --- ゼロ埋め",
      code="print(f'{3:03d}')", verify=True)

    q(6, "format spec", 3,
      "次のコードの出力として正しいものはどれか。",
      ["3.14", "3.141593", "3.1", "3.14159"],
      0,
      "`:.2f` は小数点以下2桁の固定小数表記。",
      "書式指定 --- 浮動小数点",
      code="import math\nprint(f'{math.pi:.2f}')", verify=True)

    q(6, "format spec", 3,
      "次のコードの出力として正しいものはどれか。",
      [">>>>5", "5>>>>", "5    ", "    5"],
      0,
      "`:>5` は右寄せ幅5、埋め文字を '>' に指定。'>>>>5' になる。",
      "書式指定 --- 寄せと埋め文字",
      code="print(f'{5:>>5}')", verify=True)

    q(6, "zfill", 2,
      "次のコードの出力として正しいものはどれか。",
      ["00042", "42000", "   42", "42"],
      0,
      "str.zfill(width) は左側をゼロ埋めして指定幅にする。",
      "str.zfill",
      code="print('42'.zfill(5))", verify=True)

    q(6, "title", 2,
      "次のコードの出力として正しいものはどれか。",
      ["Hello World", "HELLO WORLD", "hello world", "Hello world"],
      0,
      "str.title() は各単語の先頭を大文字にする。",
      "str.title",
      code="print('hello world'.title())", verify=True)

    q(6, "capitalize", 2,
      "次のコードの出力として正しいものはどれか。",
      ["Hello world", "Hello World", "HELLO WORLD", "hello world"],
      0,
      "str.capitalize() は先頭だけ大文字、残りを小文字にする。",
      "str.capitalize",
      code="print('hello world'.capitalize())", verify=True)

    q(6, "encode", 3,
      "文字列をバイト列に変換するメソッドはどれか。",
      ["str.encode()", "str.decode()", "bytes.encode()", "str.tobytes()"],
      0,
      "str.encode('utf-8') で str→bytes。逆は bytes.decode('utf-8') で bytes→str。",
      "encode / decode")

    q(6, "bytes", 3,
      "次のコードの出力として正しいものはどれか。",
      ["b'abc'", "abc", "'abc'", "[97, 98, 99]"],
      0,
      "str.encode() は bytes を返す。ASCII 範囲はそのまま表示され b'abc'。",
      "str.encode",
      code="print('abc'.encode('utf-8'))", verify=True)

    q(6, "ord/chr", 2,
      "次のコードの出力として正しいものはどれか。",
      ["65", "A", "97", "a"],
      0,
      "ord(文字) は Unicode コードポイントを返す。'A' は 65。",
      "ord",
      code="print(ord('A'))", verify=True)

    q(6, "ord/chr", 2,
      "次のコードの出力として正しいものはどれか。",
      ["A", "65", "a", "エラー"],
      0,
      "chr(整数) はコードポイントに対応する文字を返す。chr(65) は 'A'。",
      "chr",
      code="print(chr(65))", verify=True)

    q(6, "in", 1,
      "次のコードの出力として正しいものはどれか。",
      ["False", "True", "エラー", "0"],
      0,
      "in は部分文字列の有無を判定する。'z' は 'abc' に含まれないので False。",
      "in 演算子",
      code="print('z' in 'abc')", verify=True)

    q(6, "rstrip", 2,
      "次のコードの出力として正しいものはどれか。",
      ["'  abc'", "'abc'", "'abc  '", "'  abc  '"],
      0,
      "str.rstrip() は右側（末尾）の空白だけを除去する。repr 表示なので先頭の空白は残る。",
      "str.rstrip",
      code="print(repr('  abc  '.rstrip()))", verify=True)

    q(6, "splitlines", 3,
      "次のコードの出力として正しいものはどれか。",
      ["['a', 'b']", "['a\\nb']", "['a', 'b', '']", "'a b'"],
      0,
      "str.splitlines() は改行で分割し、末尾の改行では空要素を作らない。",
      "str.splitlines",
      code="print('a\\nb'.splitlines())", verify=True)

    q(6, "textwrap", 3,
      "長い文字列を指定幅で折り返すための標準ライブラリはどれか。",
      ["textwrap", "string", "re", "io"],
      0,
      "textwrap モジュールの wrap/fill/shorten で折り返しや短縮ができる。",
      "textwrap")

    q(6, "string定数", 2,
      "string モジュールの string.ascii_lowercase が表すものはどれか。",
      ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "全ての印字可能文字"],
      0,
      "string.ascii_lowercase は小文字アルファベット26文字の定数。",
      "string モジュールの定数",
      code="import string\nprint(string.ascii_lowercase)", verify=True)

    q(6, "f文字列", 2,
      "次のコードの出力として正しいものはどれか（Python 3.8以降のデバッグ用記法）。",
      ["x=10", "x 10", "10", "{x}=10"],
      0,
      "f文字列の `{x=}` は『変数名=値』を出力するデバッグ用記法（3.8以降）。x=10 を出力する。",
      "f文字列 --- = 記法",
      code="x = 10\nprint(f'{x=}')", verify=True)


# ============================================================
# 第8章 日付と時刻の処理
# ============================================================
def ch08(q):
    q(8, "datetime", 1,
      "日付と時刻を扱う標準ライブラリのモジュールはどれか。",
      ["datetime", "date", "calendar", "chrono"],
      0,
      "datetime モジュールが date・time・datetime・timedelta などのクラスを提供する。",
      "datetime モジュール")

    q(8, "date.today", 1,
      "今日の日付（date オブジェクト）を取得するメソッドはどれか。",
      ["date.today()", "date.now()", "datetime.date()", "date.current()"],
      0,
      "date.today() が今日の日付を返す。現在日時（datetime）は datetime.now()。",
      "date.today")

    q(8, "datetime.now", 1,
      "現在の日付と時刻を返すメソッドはどれか。",
      ["datetime.now()", "datetime.today_time()", "time.now()", "date.now()"],
      0,
      "datetime.now() が現在の日付＋時刻の datetime オブジェクトを返す。",
      "datetime.now")

    q(8, "timedelta", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2024-01-08", "2024-01-01", "2024-01-07", "エラー"],
      0,
      "timedelta(days=7) を足すと7日後になる。2024-01-01 + 7日 = 2024-01-08。",
      "timedelta による加算",
      code="from datetime import date, timedelta\nprint(date(2024, 1, 1) + timedelta(days=7))", verify=True)

    q(8, "timedelta", 2,
      "2つの date を引き算した結果の型はどれか。",
      ["timedelta", "date", "int", "datetime"],
      0,
      "date 同士の引き算は経過日数を表す timedelta を返す。",
      "date の差 --- timedelta",
      code="from datetime import date\nprint(type(date(2024,1,8) - date(2024,1,1)).__name__)", verify=False)

    q(8, "timedelta", 2,
      "次のコードの出力として正しいものはどれか。",
      ["7", "1", "7 days", "168"],
      0,
      "date の差は timedelta になり、その days 属性で日数を取れる。差は7日。",
      "timedelta.days",
      code="from datetime import date\nd = date(2024, 1, 8) - date(2024, 1, 1)\nprint(d.days)", verify=True)

    q(8, "strftime", 2,
      "datetime を指定書式の文字列に変換するメソッドはどれか。",
      ["strftime", "strptime", "format_time", "tostr"],
      0,
      "strftime（string from time）は datetime→文字列。strptime（string parse time）は文字列→datetime。",
      "strftime")

    q(8, "strftime", 3,
      "次のコードの出力として正しいものはどれか。",
      ["2024-03-05", "03-05-2024", "2024/03/05", "24-3-5"],
      0,
      "%Y=4桁年, %m=2桁月, %d=2桁日。書式 '%Y-%m-%d' で '2024-03-05'。",
      "strftime --- 書式コード",
      code="from datetime import date\nprint(date(2024, 3, 5).strftime('%Y-%m-%d'))", verify=True)

    q(8, "strptime", 3,
      "次のコードの出力として正しいものはどれか。",
      ["2024-03-05", "03-05-2024", "datetime(2024, 3, 5)", "エラー"],
      0,
      "strptime で文字列をパースし datetime を得る。date() で日付部分にし print すると '2024-03-05'。",
      "strptime",
      code="from datetime import datetime\nd = datetime.strptime('2024/03/05', '%Y/%m/%d')\nprint(d.date())", verify=True)

    q(8, "属性", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2024", "3", "5", "(2024, 3, 5)"],
      0,
      "date オブジェクトの year 属性で年を取得できる。",
      "date.year",
      code="from datetime import date\nprint(date(2024, 3, 5).year)", verify=True)

    q(8, "isoformat", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2024-03-05", "2024/03/05", "20240305", "March 5, 2024"],
      0,
      "date.isoformat() は ISO 8601 形式 'YYYY-MM-DD' の文字列を返す。",
      "isoformat",
      code="from datetime import date\nprint(date(2024, 3, 5).isoformat())", verify=True)

    q(8, "weekday", 3,
      "date.weekday() が月曜日に対して返す値はどれか。",
      ["0", "1", "7", "月"],
      0,
      "weekday() は月曜=0 〜 日曜=6。isoweekday() は月曜=1〜日曜=7。",
      "weekday")

    q(8, "time", 2,
      "プログラムの経過時間を測るのに適した、time モジュールの関数はどれか。",
      ["time.time()", "time.date()", "time.now()", "time.clock_date()"],
      0,
      "time.time() はエポックからの秒数（float）を返す。差を取って経過時間を測れる。",
      "time.time")

    q(8, "timezone", 3,
      "タイムゾーン情報を持たない datetime を表す用語はどれか。",
      ["naive", "aware", "utc", "local"],
      0,
      "tzinfo を持たない datetime は naive、持つものは aware と呼ばれる。",
      "naive / aware")

    q(8, "timezone", 3,
      "UTC を表す固定タイムゾーンとして使える定数はどれか。",
      ["timezone.utc", "timezone.UTC", "datetime.utc", "tz.UTC"],
      0,
      "datetime.timezone.utc が UTC を表す。aware な datetime を作る際に tzinfo として渡す。",
      "timezone.utc")

    q(8, "calendar", 2,
      "うるう年かどうかを判定できる標準ライブラリの関数はどれか。",
      ["calendar.isleap(year)", "datetime.isleap(year)", "time.isleap(year)", "date.leap(year)"],
      0,
      "calendar.isleap(year) がうるう年判定を行う。",
      "calendar.isleap",
      code="import calendar\nprint(calendar.isleap(2024))", verify=False)


# ============================================================
# 第9章 データ型とアルゴリズム
# ============================================================
def ch09(q):
    q(9, "list", 1,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3]", "[1, 2]", "[3, 1, 2]", "エラー"],
      0,
      "list.append(x) は末尾に要素を追加する。",
      "list.append",
      code="a = [1, 2]\na.append(3)\nprint(a)", verify=True)

    q(9, "list", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3, 4]", "[1, 2, [3, 4]]", "[3, 4, 1, 2]", "エラー"],
      0,
      "list.extend(iterable) は各要素を末尾に追加する。append との違いに注意。",
      "list.extend",
      code="a = [1, 2]\na.extend([3, 4])\nprint(a)", verify=True)

    q(9, "list", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 9, 2]", "[1, 2, 9]", "[9, 1, 2]", "エラー"],
      0,
      "list.insert(i, x) は位置 i に挿入する。インデックス1に9を入れる。",
      "list.insert",
      code="a = [1, 2]\na.insert(1, 9)\nprint(a)", verify=True)

    q(9, "list", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2", "[1, 3]", "1", "[2]"],
      0,
      "list.pop(i) は指定位置の要素を取り除いて返す。pop(1) は値 2 を返す。",
      "list.pop",
      code="a = [1, 2, 3]\nprint(a.pop(1))", verify=True)

    q(9, "sorted", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3]", "[3, 2, 1]", "[2, 3, 1]", "エラー"],
      0,
      "sorted() は新しいソート済みリストを返す（元は変更しない）。",
      "sorted",
      code="print(sorted([3, 1, 2]))", verify=True)

    q(9, "sort key", 3,
      "次のコードの出力として正しいものはどれか。",
      ["['bb', 'aaa', 'cccc']", "['aaa', 'bb', 'cccc']", "['cccc', 'aaa', 'bb']", "['bb', 'cccc', 'aaa']"],
      0,
      "key=len で文字数順にソートする。'bb'(2) < 'aaa'(3) < 'cccc'(4)。",
      "sorted --- key",
      code="print(sorted(['aaa', 'bb', 'cccc'], key=len))", verify=True)

    q(9, "sort reverse", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[3, 2, 1]", "[1, 2, 3]", "[3, 1, 2]", "エラー"],
      0,
      "reverse=True で降順ソートになる。",
      "sorted --- reverse",
      code="print(sorted([1, 3, 2], reverse=True))", verify=True)

    q(9, "dict", 1,
      "次のコードの出力として正しいものはどれか。",
      ["dict_keys(['a', 'b'])", "['a', 'b']", "('a', 'b')", "{'a', 'b'}"],
      0,
      "dict.keys() はキーのビュー（dict_keys）を返す。",
      "dict.keys",
      code="print({'a': 1, 'b': 2}.keys())", verify=True)

    q(9, "dict", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[('a', 1), ('b', 2)]", "['a', 'b']", "[1, 2]", "エラー"],
      0,
      "dict.items() はキーと値のタプルのビューを返す。list 化すると [(キー,値), ...]。",
      "dict.items",
      code="print(list({'a': 1, 'b': 2}.items()))", verify=True)

    q(9, "dict", 2,
      "辞書に存在しないキーをデフォルト値付きで取得・設定するメソッドはどれか。",
      ["setdefault", "getdefault", "default", "fetch"],
      0,
      "dict.setdefault(key, default) はキーが無ければ default を設定して返す。",
      "dict.setdefault")

    q(9, "dict", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{'a': 1, 'b': 3, 'c': 4}", "{'a': 1, 'b': 2}", "{'b': 3, 'c': 4}", "エラー"],
      0,
      "dict.update(other) は other の内容で更新（既存キーは上書き、新規は追加）。",
      "dict.update",
      code="d = {'a': 1, 'b': 2}\nd.update({'b': 3, 'c': 4})\nprint(d)", verify=True)

    q(9, "set", 1,
      "次のコードの出力として正しいものはどれか。",
      ["{1, 2, 3}", "{1, 1, 2, 3, 3}", "[1, 2, 3]", "エラー"],
      0,
      "set は重複を除去する。",
      "set --- 重複排除",
      code="print(set([1, 1, 2, 3, 3]))", verify=True)

    q(9, "set", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{2, 3}", "{1, 2, 3, 4}", "{1, 4}", "set()"],
      0,
      "`&` は集合の積（共通部分）。{1,2,3} と {2,3,4} の共通は {2, 3}。",
      "集合演算 --- 積",
      code="print({1, 2, 3} & {2, 3, 4})", verify=True)

    q(9, "set", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "エラー"],
      0,
      "`|` は和集合（合併）。",
      "集合演算 --- 和",
      code="print({1, 2} | {3, 4})", verify=True)

    q(9, "set", 2,
      "次のコードの出力として正しいものはどれか。",
      ["{1}", "{2, 3}", "{1, 2, 3}", "set()"],
      0,
      "`-` は差集合。{1,2,3} から {2,3} を除くと {1}。",
      "集合演算 --- 差",
      code="print({1, 2, 3} - {2, 3})", verify=True)

    q(9, "tuple", 2,
      "要素が1つだけのタプルを正しく定義しているものはどれか。",
      ["(1,)", "(1)", "1,1", "tuple(1)"],
      0,
      "1要素タプルは末尾のカンマが必須。`(1)` はただの整数1。",
      "1要素タプル")

    q(9, "Counter", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[('a', 3), ('b', 2)]", "[('a', 2), ('b', 3)]", "{'a': 3, 'b': 2}", "['a', 'b']"],
      0,
      "collections.Counter は要素の出現回数を数える。most_common(n) は多い順に上位 n 件を返す。",
      "collections.Counter",
      code="from collections import Counter\nc = Counter('aaabb')\nprint(c.most_common(2))", verify=True)

    q(9, "defaultdict", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2]", "エラー(KeyError)", "None", "[]"],
      0,
      "defaultdict(list) は未知キーへのアクセス時に list() を自動生成するため、append できる。",
      "collections.defaultdict",
      code="from collections import defaultdict\nd = defaultdict(list)\nd['x'].append(1)\nd['x'].append(2)\nprint(d['x'])", verify=True)

    q(9, "namedtuple", 3,
      "次のコードの出力として正しいものはどれか。",
      ["1 2", "Point(1, 2)", "(1, 2)", "x y"],
      0,
      "namedtuple は名前付きフィールドを持つタプル。p.x, p.y で値にアクセスできる。",
      "collections.namedtuple",
      code="from collections import namedtuple\nPoint = namedtuple('Point', ['x', 'y'])\np = Point(1, 2)\nprint(p.x, p.y)", verify=True)

    q(9, "deque", 3,
      "両端への高速な追加・削除に適した collections のデータ構造はどれか。",
      ["deque", "Counter", "OrderedDict", "namedtuple"],
      0,
      "collections.deque は両端キュー。appendleft/popleft が O(1)。",
      "collections.deque")

    q(9, "deque", 3,
      "次のコードの出力として正しいものはどれか。",
      ["deque([0, 1, 2])", "deque([1, 2, 0])", "deque([2, 1, 0])", "[0, 1, 2]"],
      0,
      "appendleft は左端に追加する。1,2 を append 後、0 を左端へ追加すると [0, 1, 2]。",
      "deque.appendleft",
      code="from collections import deque\nd = deque([1, 2])\nd.appendleft(0)\nprint(d)", verify=True)

    q(9, "itertools", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3, 4]", "[(1, 3), (2, 4)]", "[1, 3, 2, 4]", "エラー"],
      0,
      "itertools.chain は複数のイテラブルを連結する。",
      "itertools.chain",
      code="import itertools\nprint(list(itertools.chain([1, 2], [3, 4])))", verify=True)

    q(9, "itertools", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[(1, 2), (1, 3), (2, 3)]", "[(1, 2), (2, 3)]", "[(2, 1), (3, 1), (3, 2)]", "[1, 2, 3]"],
      0,
      "itertools.combinations(iterable, 2) は2要素の組合せ（順序は元の並び、重複なし）を返す。",
      "itertools.combinations",
      code="import itertools\nprint(list(itertools.combinations([1, 2, 3], 2)))", verify=True)

    q(9, "itertools", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[(1, 2), (2, 1)]", "[(1, 2)]", "[(1, 1), (2, 2)]", "[1, 2]"],
      0,
      "itertools.permutations(iterable, 2) は2要素の順列（順序を区別）を返す。",
      "itertools.permutations",
      code="import itertools\nprint(list(itertools.permutations([1, 2], 2)))", verify=True)

    q(9, "itertools", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]", "[(1, 'a'), (2, 'b')]", "[1, 2, 'a', 'b']", "エラー"],
      0,
      "itertools.product は直積（すべての組合せ）を返す。",
      "itertools.product",
      code="import itertools\nprint(list(itertools.product([1, 2], ['a', 'b'])))", verify=True)

    q(9, "functools", 3,
      "次のコードの出力として正しいものはどれか。",
      ["10", "[1, 2, 3, 4]", "24", "4"],
      0,
      "functools.reduce は累積的に二項演算を適用する。1+2+3+4 = 10。",
      "functools.reduce",
      code="from functools import reduce\nprint(reduce(lambda a, b: a + b, [1, 2, 3, 4]))", verify=True)

    q(9, "functools", 3,
      "関数の結果をキャッシュ（メモ化）する functools のデコレータはどれか。",
      ["@lru_cache", "@cache_result", "@memoize", "@store"],
      0,
      "functools.lru_cache（または cache）が結果をキャッシュする。再帰の高速化に有効。",
      "functools.lru_cache")

    q(9, "functools", 3,
      "次のコードの出力として正しいものはどれか。",
      ["8", "5", "3", "エラー"],
      0,
      "functools.partial は引数を部分適用した新しい関数を作る。add に 3 を固定し、5 を渡すと 8。",
      "functools.partial",
      code="from functools import partial\ndef add(a, b):\n    return a + b\nadd3 = partial(add, 3)\nprint(add3(5))", verify=True)

    q(9, "bisect", 3,
      "ソート済みリストへ順序を保ったまま挿入位置を求める標準ライブラリはどれか。",
      ["bisect", "heapq", "array", "queue"],
      0,
      "bisect は二分探索で挿入位置を求める（bisect_left/insort 等）。",
      "bisect")

    q(9, "heapq", 3,
      "次のコードの出力として正しいものはどれか。",
      ["1", "3", "5", "[1, 3, 5]"],
      0,
      "heapq はリストを最小ヒープとして扱う。heappush 後、heappop は最小値 1 を返す。",
      "heapq",
      code="import heapq\nh = []\nheapq.heappush(h, 5)\nheapq.heappush(h, 1)\nheapq.heappush(h, 3)\nprint(heapq.heappop(h))", verify=True)

    q(9, "copy", 3,
      "ネストしたオブジェクトも含めて完全に複製するには、copy モジュールのどの関数を使うか。",
      ["deepcopy", "copy", "clone", "duplicate"],
      0,
      "copy.deepcopy は再帰的に複製する。copy.copy は浅いコピー。",
      "copy.deepcopy")

    q(9, "copy", 3,
      "次のコードの出力として正しいものはどれか。",
      ["[[1, 2], [3]]", "[[1, 2, 99], [3]]", "[[1, 2], [3, 99]]", "エラー"],
      0,
      "deepcopy は内側のリストも複製するため、コピー側への変更は元に影響しない。",
      "deepcopy の効果",
      code="import copy\na = [[1, 2], [3]]\nb = copy.deepcopy(a)\nb[0].append(99)\nprint(a)", verify=True)

    q(9, "enum", 3,
      "列挙型を定義するための標準ライブラリのクラスはどれか。",
      ["enum.Enum", "collections.Enum", "typing.Enum", "enum.List"],
      0,
      "enum.Enum を継承して列挙型を定義する。メンバは name/value を持つ。",
      "enum.Enum")

    q(9, "dict", 2,
      "次のコードの出力として正しいものはどれか。",
      ["3", "2", "[1, 2, 3]", "エラー"],
      0,
      "辞書の len はキー（＝エントリ）の数。3個のキーがある。",
      "len(dict)",
      code="print(len({'a': 1, 'b': 2, 'c': 3}))", verify=True)

    q(9, "list", 2,
      "次のコードの出力として正しいものはどれか。",
      ["2", "1", "3", "エラー"],
      0,
      "list.index(x) は最初に x が現れるインデックスを返す。30 はインデックス2。",
      "list.index",
      code="print([10, 20, 30].index(30))", verify=True)

    q(9, "list内包", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[[0, 1], [0, 1]]", "[0, 1, 0, 1]", "[0, 0, 1, 1]", "エラー"],
      0,
      "ネストした内包表記。外側2回・内側range(2)で [[0,1],[0,1]]。",
      "ネスト内包表記",
      code="print([[j for j in range(2)] for i in range(2)])", verify=True)

    q(9, "any/all", 2,
      "次のコードの出力として正しいものはどれか。",
      ["True", "False", "エラー", "None"],
      0,
      "all は全要素が真なら True。[1,2,3] は全て真なので True。any は1つでも真なら True。",
      "all / any",
      code="print(all([1, 2, 3]))", verify=True)

    q(9, "max key", 3,
      "次のコードの出力として正しいものはどれか。",
      ["ccc", "a", "bb", "['a', 'bb', 'ccc']"],
      0,
      "max に key=len を渡すと、最も長い文字列を返す。'ccc' が最長。",
      "max --- key",
      code="print(max(['a', 'bb', 'ccc'], key=len))", verify=True)


# ============================================================
# 第10章 汎用OS・ランタイムサービス
# ============================================================
def ch10(q):
    q(10, "os.environ", 2,
      "環境変数を辞書ライクに参照できる os の属性はどれか。",
      ["os.environ", "os.env", "os.getenvs", "os.variables"],
      0,
      "os.environ は環境変数の辞書。os.environ.get('KEY') や os.getenv('KEY') で安全に取得できる。",
      "os.environ")

    q(10, "os.getenv", 2,
      "環境変数 PATH を、未設定なら None を返す形で取得する式はどれか。",
      ["os.getenv('PATH')", "os.environ['PATH'] は未設定でも None", "os.path('PATH')", "os.env('PATH')"],
      0,
      "os.getenv('PATH') は未設定で None を返す。os.environ['PATH'] は未設定だと KeyError。",
      "os.getenv")

    q(10, "sys.argv", 2,
      "コマンドライン引数のリストを保持する sys の属性はどれか。",
      ["sys.argv", "sys.args", "sys.params", "sys.input"],
      0,
      "sys.argv はコマンドライン引数のリスト。argv[0] はスクリプト名。",
      "sys.argv")

    q(10, "sys.argv", 2,
      "`python script.py foo bar` を実行したとき sys.argv[1] の値はどれか。",
      ["foo", "script.py", "bar", "python"],
      0,
      "argv[0] が 'script.py'、argv[1] が 'foo'、argv[2] が 'bar'。",
      "sys.argv のインデックス")

    q(10, "argparse", 2,
      "コマンドライン引数を本格的に解析する標準ライブラリはどれか。",
      ["argparse", "getopts", "click", "optparse2"],
      0,
      "argparse がコマンドライン引数解析の標準。ヘルプやオプション定義を簡潔に書ける。",
      "argparse")

    q(10, "sys.exit", 2,
      "プログラムを終了させる関数はどれか。",
      ["sys.exit()", "os.quit()", "exit.now()", "sys.stop()"],
      0,
      "sys.exit([status]) で終了できる。status に整数（0=正常）や文字列を渡せる。",
      "sys.exit")

    q(10, "os.path", 2,
      "次のコードの出力として正しいものはどれか。",
      ["a/b/c.txt", "a\\\\b\\\\c.txt", "abc.txt", "['a', 'b', 'c.txt']"],
      0,
      "os.path.join はパス区切りで結合する（POSIX では '/'）。",
      "os.path.join",
      code="import os\nprint(os.path.join('a', 'b', 'c.txt'))", verify=True)

    q(10, "os.path", 2,
      "次のコードの出力として正しいものはどれか。",
      ["c.txt", "a/b", "txt", "c"],
      0,
      "os.path.basename はパスの末尾（ファイル名）を返す。",
      "os.path.basename",
      code="import os\nprint(os.path.basename('a/b/c.txt'))", verify=True)

    q(10, "os.path", 2,
      "次のコードの出力として正しいものはどれか。",
      ["('a/b', 'c.txt')", "('a', 'b/c.txt')", "('a/b/c', '.txt')", "['a', 'b', 'c.txt']"],
      0,
      "os.path.split はディレクトリ部分とファイル名に分ける。",
      "os.path.split",
      code="import os\nprint(os.path.split('a/b/c.txt'))", verify=True)

    q(10, "os.path", 3,
      "次のコードの出力として正しいものはどれか。",
      ["('a/b/c', '.txt')", "('a/b/c.txt', '')", "('.txt', 'a/b/c')", "('c', 'txt')"],
      0,
      "os.path.splitext は拡張子を分離する。",
      "os.path.splitext",
      code="import os\nprint(os.path.splitext('a/b/c.txt'))", verify=True)

    q(10, "subprocess", 3,
      "外部コマンドを実行する標準ライブラリで、推奨される高レベル関数はどれか。",
      ["subprocess.run()", "os.system2()", "commands.run()", "exec.shell()"],
      0,
      "subprocess.run() が推奨される高レベルAPI。os.system は機能が限定的。",
      "subprocess.run")

    q(10, "logging", 2,
      "アプリケーションのログ出力に使う標準ライブラリはどれか。",
      ["logging", "log", "syslog2", "printlog"],
      0,
      "logging モジュールがログ出力の標準。レベル（DEBUG/INFO/WARNING/ERROR/CRITICAL）を持つ。",
      "logging")

    q(10, "logging", 3,
      "logging のログレベルを、低い（詳細）方から高い（重大）方へ正しく並べたものはどれか。",
      ["DEBUG < INFO < WARNING < ERROR < CRITICAL",
       "INFO < DEBUG < WARNING < ERROR < CRITICAL",
       "CRITICAL < ERROR < WARNING < INFO < DEBUG",
       "WARNING < INFO < DEBUG < ERROR < CRITICAL"],
      0,
      "深刻度は DEBUG(10) < INFO(20) < WARNING(30) < ERROR(40) < CRITICAL(50)。既定の出力閾値は WARNING。",
      "logging --- ログレベル")

    q(10, "platform", 2,
      "実行中のOS名やマシン情報を取得できる標準ライブラリはどれか。",
      ["platform", "machine", "osinfo", "sysconfig2"],
      0,
      "platform モジュールで platform.system()（OS名）や platform.python_version() などを取得できる。",
      "platform")

    q(10, "os", 2,
      "カレントワーキングディレクトリを取得する os の関数はどれか。",
      ["os.getcwd()", "os.pwd()", "os.curdir()", "os.path.cwd()"],
      0,
      "os.getcwd() が現在の作業ディレクトリ（文字列）を返す。変更は os.chdir()。",
      "os.getcwd")


# ============================================================
# 第11章 ファイルとディレクトリへのアクセス
# ============================================================
def ch11(q):
    q(11, "open mode", 1,
      "ファイルを「書き込み（既存内容を消去）」で開くモード文字列はどれか。",
      ["'w'", "'r'", "'a'", "'x'"],
      0,
      "'w' は書き込み（truncate）、'r' は読み込み、'a' は追記、'x' は排他生成（既存だとエラー）。",
      "open --- モード")

    q(11, "open mode", 2,
      "既存ファイルの末尾に追記するモードはどれか。",
      ["'a'", "'w'", "'r+'", "'x'"],
      0,
      "'a'（append）は末尾に追記する。'w' は内容を消してから書く。",
      "open --- 追記モード")

    q(11, "open mode", 2,
      "バイナリ読み込みモードを表す文字列はどれか。",
      ["'rb'", "'r'", "'br'は不可", "'binary'"],
      0,
      "'rb' はバイナリ読み込み。テキストは 'r'、書き込みバイナリは 'wb'。",
      "open --- バイナリモード")

    q(11, "with open", 2,
      "ファイルを扱うとき with 文を使う主な理由はどれか。",
      ["ブロックを抜けるときに自動で close される",
       "読み込み速度が必ず速くなる",
       "ファイルを暗号化できる",
       "文字コードを自動判別する"],
      0,
      "with open(...) as f: は確実にファイルを閉じる（例外時も）。close 漏れを防ぐ定石。",
      "with open")

    q(11, "encoding", 2,
      "テキストファイルを UTF-8 で開くときの正しい指定はどれか。",
      ["open(path, encoding='utf-8')", "open(path, charset='utf-8')", "open(path, 'utf-8')", "open(path, code='utf-8')"],
      0,
      "文字コードは encoding 引数で指定する。プラットフォーム依存を避けるため明示が推奨される。",
      "open --- encoding")

    q(11, "read", 2,
      "ファイルオブジェクト f の全内容を1つの文字列として読むメソッドはどれか。",
      ["f.read()", "f.readline()", "f.readlines()", "f.readall_str()"],
      0,
      "f.read() は全体を文字列で返す。readline は1行、readlines は行のリスト。",
      "file.read")

    q(11, "readlines", 2,
      "ファイルの全行をリストとして読み込むメソッドはどれか。",
      ["f.readlines()", "f.read()", "f.lines()", "f.readline()"],
      0,
      "f.readlines() は各行（改行付き）を要素とするリストを返す。",
      "file.readlines")

    q(11, "イテレーション", 2,
      "ファイルオブジェクトを for 文で回したときに得られるものはどれか。",
      ["1行ずつ", "1文字ずつ", "1バイトずつ", "全体を1つの文字列で1回"],
      0,
      "ファイルオブジェクトはイテレートすると1行ずつ返す。大きなファイルでもメモリ効率が良い。",
      "ファイルの行イテレーション")

    q(11, "pathlib", 2,
      "オブジェクト指向でパスを扱う標準ライブラリのクラスはどれか。",
      ["pathlib.Path", "os.Path", "pathlib.File", "path.Path"],
      0,
      "pathlib.Path はパス操作をメソッド/演算子で扱える。`/` でパスを結合できる。",
      "pathlib.Path")

    q(11, "pathlib", 3,
      "次のコードの出力として正しいものはどれか。",
      ["a/b/c.txt", "a\\\\b\\\\c.txt", "a-b-c.txt", "エラー"],
      0,
      "pathlib では `/` 演算子でパスを連結できる。POSIX 環境では 'a/b/c.txt'。",
      "Path --- / 演算子",
      code="from pathlib import Path\nprint(Path('a') / 'b' / 'c.txt')", verify=True)

    q(11, "pathlib", 3,
      "次のコードの出力として正しいものはどれか。",
      [".txt", "c", "c.txt", "txt"],
      0,
      "Path.suffix は拡張子（ドット付き）を返す。",
      "Path.suffix",
      code="from pathlib import Path\nprint(Path('a/b/c.txt').suffix)", verify=True)

    q(11, "pathlib", 3,
      "次のコードの出力として正しいものはどれか。",
      ["c.txt", "c", "a/b", ".txt"],
      0,
      "Path.name はパス末尾の名前（拡張子含む）を返す。",
      "Path.name",
      code="from pathlib import Path\nprint(Path('a/b/c.txt').name)", verify=True)

    q(11, "存在確認", 2,
      "パスが存在するか確認する方法として正しいものはどれか。",
      ["os.path.exists(path) または Path(path).exists()",
       "os.check(path)", "Path(path).is_there()", "os.path.has(path)"],
      0,
      "os.path.exists または pathlib の Path.exists() でファイル/ディレクトリの存在を確認できる。",
      "exists")

    q(11, "glob", 3,
      "パターンに一致するファイル一覧を取得する標準ライブラリはどれか。",
      ["glob", "fnmatch2", "listdir", "scandir2"],
      0,
      "glob.glob('*.txt') のようにワイルドカードでファイルを列挙できる。pathlib の Path.glob も同様。",
      "glob")

    q(11, "shutil", 3,
      "ファイルやディレクトリのコピー・移動を行う高レベルな標準ライブラリはどれか。",
      ["shutil", "os.copy", "filecopy", "movelib"],
      0,
      "shutil は shutil.copy/copytree/move/rmtree など高レベルなファイル操作を提供する。",
      "shutil")


# ============================================================
# 第13章 特定のデータフォーマットを扱う
# ============================================================
def ch13(q):
    q(13, "json", 1,
      "Python オブジェクトを JSON 文字列に変換する関数はどれか。",
      ["json.dumps", "json.loads", "json.parse", "json.encode"],
      0,
      "json.dumps はオブジェクト→JSON文字列、json.loads は JSON文字列→オブジェクト。s 付きが文字列版。",
      "json.dumps")

    q(13, "json", 2,
      "次のコードの出力として正しいものはどれか。",
      ['{"a": 1}', "{'a': 1}", "a=1", "エラー"],
      0,
      "json.dumps は JSON 形式の文字列を返す。JSON ではキーも文字列でダブルクォートになる。",
      "json.dumps の出力",
      code="import json\nprint(json.dumps({'a': 1}))", verify=True)

    q(13, "json", 2,
      "次のコードの出力として正しいものはどれか。",
      ["<class 'dict'>", "<class 'str'>", "<class 'list'>", "エラー"],
      0,
      "json.loads は JSON文字列を Python オブジェクト（オブジェクト→dict）に変換する。",
      "json.loads",
      code="import json\nprint(type(json.loads('{\"a\": 1}')))", verify=True)

    q(13, "json", 3,
      "json.dumps で日本語を `\\uXXXX` にエスケープせず、そのまま出力するための引数はどれか。",
      ["ensure_ascii=False", "ascii=False", "encoding='utf-8'", "raw=True"],
      0,
      "ensure_ascii=False を指定すると非ASCII文字をそのまま出力する。既定は True でエスケープされる。",
      "json.dumps --- ensure_ascii")

    q(13, "json", 3,
      "json.dumps で人間が読みやすいようインデントを付ける引数はどれか。",
      ["indent", "pretty", "spaces", "tab"],
      0,
      "indent=2 のように指定すると整形（pretty print）される。",
      "json.dumps --- indent")

    q(13, "json", 2,
      "ファイルオブジェクトに直接 JSON を書き出す関数はどれか。",
      ["json.dump", "json.dumps", "json.write", "json.tofile"],
      0,
      "json.dump(obj, f) はファイルへ書き出す。json.dumps は文字列を返す（s=string）。",
      "json.dump / json.load")

    q(13, "csv", 2,
      "CSV ファイルを扱う標準ライブラリはどれか。",
      ["csv", "table", "spreadsheet", "tsv"],
      0,
      "csv モジュールが CSV の読み書きを提供する。csv.reader / csv.writer など。",
      "csv モジュール")

    q(13, "csv", 3,
      "CSV の各行を辞書として読み込めるクラスはどれか（先頭行をキーにする）。",
      ["csv.DictReader", "csv.HeaderReader", "csv.MapReader", "csv.reader"],
      0,
      "csv.DictReader はヘッダ行をキーとして各行を辞書で返す。書き込みは csv.DictWriter。",
      "csv.DictReader")

    q(13, "csv", 3,
      "csv.writer で行を書き込むとき、Windows でも余計な空行を防ぐためにファイルを開く際に指定すべき引数はどれか。",
      ["newline=''", "binary=True", "mode='wb'", "lineterminator=None"],
      0,
      "csv 書き込みでは open(path, 'w', newline='') を使うのが定石。改行の二重化を防ぐ。",
      "csv --- newline=''")

    q(13, "pickle", 2,
      "Python オブジェクトをバイト列に直列化（シリアライズ）する標準ライブラリはどれか。",
      ["pickle", "json", "marshal2", "serialize"],
      0,
      "pickle は Python 固有のバイナリ直列化。json と違い任意の Python オブジェクトを扱えるが、互換性・安全性に注意。",
      "pickle")

    q(13, "pickle", 3,
      "pickle の利用上の注意として正しいものはどれか。",
      ["信頼できないデータを unpickle すると任意コード実行の危険がある",
       "JSON より常に安全である",
       "他言語と容易に相互運用できる",
       "テキスト形式なので人間が読める"],
      0,
      "pickle.load は信頼できないソースに対して安全でない（任意コード実行の恐れ）。外部入力には使わない。",
      "pickle --- セキュリティ")

    q(13, "configparser", 2,
      "INI 形式の設定ファイルを読み書きする標準ライブラリはどれか。",
      ["configparser", "inifile", "settings", "config"],
      0,
      "configparser が INI 形式（[section] key=value）を扱う。",
      "configparser")

    q(13, "sqlite3", 2,
      "追加サーバ不要で使える、標準ライブラリ同梱のデータベースはどれか。",
      ["sqlite3", "mysql", "postgres", "redis"],
      0,
      "sqlite3 は標準ライブラリに含まれ、ファイルベースのDBを扱える。",
      "sqlite3")

    q(13, "sqlite3", 3,
      "sqlite3 でSQLを実行するために、接続から取得して使うオブジェクトはどれか。",
      ["カーソル（cursor）", "セッション", "エンジン", "トランザクタ"],
      0,
      "connection.cursor() で得たカーソルの execute でSQLを実行し、fetchone/fetchall で結果を取る。",
      "sqlite3 --- cursor")

    q(13, "base64", 3,
      "次のコードの出力として正しいものはどれか。",
      ["b'YWJj'", "abc", "b'abc'", "YWJj"],
      0,
      "base64.b64encode はバイト列を Base64 のバイト列に変換する。'abc' は b'YWJj'。",
      "base64.b64encode",
      code="import base64\nprint(base64.b64encode(b'abc'))", verify=True)

    q(13, "base64", 3,
      "次のコードの出力として正しいものはどれか。",
      ["b'abc'", "abc", "YWJj", "エラー"],
      0,
      "base64.b64decode は Base64 を元のバイト列に戻す。b'YWJj' → b'abc'。",
      "base64.b64decode",
      code="import base64\nprint(base64.b64decode(b'YWJj'))", verify=True)

    q(13, "json", 2,
      "JSON の値 null は Python では何に変換されるか。",
      ["None", "0", "''", "False"],
      0,
      "JSON の null は Python の None、true/false は True/False に対応する。",
      "json --- null と None")

    q(13, "json", 3,
      "次のコードの出力として正しいものはどれか。",
      ['{"b": 1, "a": 2}', '{"a": 2, "b": 1}', "{'b': 1, 'a': 2}", "エラー"],
      0,
      "json.dumps は既定で辞書の挿入順を保つ。sort_keys=True を付けない限り並べ替えない。",
      "json.dumps --- 順序",
      code="import json\nprint(json.dumps({'b': 1, 'a': 2}))", verify=True)

    q(13, "csv", 3,
      "次のコードの出力として正しいものはどれか。",
      ["['a', 'b', 'c']", "['a,b,c']", "'a,b,c'", "[['a'], ['b'], ['c']]"],
      0,
      "csv.reader は1行をフィールドのリストに分割する。ここでは1行 'a,b,c' を読み ['a', 'b', 'c']。",
      "csv.reader",
      code="import csv, io\nr = csv.reader(io.StringIO('a,b,c'))\nprint(next(r))", verify=True)

    q(13, "tomllib", 3,
      "Python 3.11 で標準ライブラリに追加された、TOML を読み込むモジュールはどれか。",
      ["tomllib", "toml", "tomlparser", "configtoml"],
      0,
      "Python 3.11 から tomllib が標準で TOML の読み込みに対応した（書き込みは非対応）。",
      "tomllib")

    q(13, "json", 2,
      "次のコードの出力として正しいものはどれか。",
      ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "エラー"],
      0,
      "JSON 配列は Python のリストに変換される。",
      "json.loads --- 配列",
      code="import json\nprint(json.loads('[1, 2, 3]'))", verify=True)

    q(13, "gzip以外", 2,
      "CSV と JSON の使い分けに関する説明として最も適切なものはどれか。",
      ["表形式・行指向のデータには CSV、入れ子構造を含むデータには JSON が向く",
       "JSON は表形式しか表現できない",
       "CSV は階層構造を自然に表現できる",
       "両者は完全に同一で違いはない"],
      0,
      "CSV はフラットな表データ向け、JSON は入れ子（オブジェクト・配列）を表現できる点が強み。",
      "データ形式の選択")


# ============================================================
# 第14章 インターネット上のデータを扱う
# ============================================================
def ch14(q):
    q(14, "urllib", 2,
      "標準ライブラリだけで URL を開いてデータを取得するモジュールはどれか。",
      ["urllib.request", "requests", "httplib3", "urlopen2"],
      0,
      "urllib.request.urlopen で取得できる。requests はサードパーティ（試験範囲外）。",
      "urllib.request")

    q(14, "urllib.parse", 2,
      "URL を構成要素（スキーム・ホスト・パス等）に分解する関数はどれか。",
      ["urllib.parse.urlparse", "urllib.split", "url.parse", "urllib.request.parse"],
      0,
      "urllib.parse.urlparse は URL を ParseResult（scheme, netloc, path, ...）に分解する。",
      "urllib.parse.urlparse")

    q(14, "urllib.parse", 3,
      "次のコードの出力として正しいものはどれか。",
      ["example.com", "https", "/path", "http://example.com"],
      0,
      "urlparse の netloc 属性はホスト（とポート）部分を返す。",
      "urlparse --- netloc",
      code="from urllib.parse import urlparse\nprint(urlparse('https://example.com/path').netloc)", verify=True)

    q(14, "urllib.parse", 3,
      "次のコードの出力として正しいものはどれか。",
      ["a=1&b=2", "a:1,b:2", "{'a': 1, 'b': 2}", "a=1,b=2"],
      0,
      "urlencode は辞書をクエリ文字列 'キー=値&...' に変換する。",
      "urllib.parse.urlencode",
      code="from urllib.parse import urlencode\nprint(urlencode({'a': 1, 'b': 2}))", verify=True)

    q(14, "urllib.parse", 3,
      "URL に使えない文字（空白など）を %XX 形式へ変換（パーセントエンコード）する関数はどれか。",
      ["urllib.parse.quote", "urllib.parse.escape", "urllib.encode", "urllib.parse.urlparse"],
      0,
      "quote は文字列をパーセントエンコードする。逆は unquote。",
      "urllib.parse.quote")

    q(14, "json API", 2,
      "Web API から取得した JSON 文字列（bytes/str）を Python オブジェクトに変換するのに使う関数はどれか。",
      ["json.loads", "json.dumps", "json.read", "json.fetch"],
      0,
      "取得したレスポンス本文（JSON文字列）は json.loads で Python オブジェクトに変換する。",
      "json.loads --- Web API")

    q(14, "HTTP", 2,
      "HTTP のステータスコード 404 が表す意味はどれか。",
      ["Not Found（リソースが見つからない）", "OK（成功）", "Internal Server Error", "リダイレクト"],
      0,
      "404 は Not Found。200=OK、500=サーバエラー、3xx=リダイレクト。",
      "HTTPステータスコード")

    q(14, "HTTP", 2,
      "HTTP のステータスコード 200 が表す意味はどれか。",
      ["OK（成功）", "Not Found", "Forbidden", "Bad Request"],
      0,
      "200 は成功（OK）。",
      "HTTPステータスコード --- 200")

    q(14, "email", 3,
      "メール（MIME）メッセージを組み立てる標準ライブラリはどれか。",
      ["email", "smtp", "mailbox2", "mime"],
      0,
      "email パッケージで MIME メッセージを構築する。送信は smtplib。",
      "email パッケージ")

    q(14, "smtplib", 3,
      "SMTP を使ってメールを送信する標準ライブラリはどれか。",
      ["smtplib", "email", "imaplib", "poplib"],
      0,
      "smtplib が送信（SMTP）。受信は imaplib（IMAP）/poplib（POP3）。",
      "smtplib")

    q(14, "html", 2,
      "次のコードの出力として正しいものはどれか。",
      ["&lt;a&gt;", "<a>", "&a;", "エラー"],
      0,
      "html.escape は <, >, & などを HTML エンティティに変換し、HTMLインジェクションを防ぐ。",
      "html.escape",
      code="import html\nprint(html.escape('<a>'))", verify=True)

    q(14, "ipaddress", 3,
      "IPアドレスを検証・操作する標準ライブラリはどれか。",
      ["ipaddress", "socket", "netaddr", "iplib"],
      0,
      "ipaddress モジュールで IPv4/IPv6 アドレスやネットワークを扱える。",
      "ipaddress")


# ============================================================
# 第16章 テスト
# ============================================================
def ch16(q):
    q(16, "unittest", 1,
      "標準ライブラリの単体テストフレームワークはどれか。",
      ["unittest", "pytest", "nose", "testlib"],
      0,
      "unittest が標準ライブラリのテストフレームワーク。pytest・nose はサードパーティ。",
      "unittest")

    q(16, "unittest", 2,
      "unittest でテストケースを書くとき継承する基底クラスはどれか。",
      ["unittest.TestCase", "unittest.Test", "unittest.Case", "unittest.Suite"],
      0,
      "unittest.TestCase を継承し、test_ で始まるメソッドにテストを書く。",
      "unittest.TestCase")

    q(16, "unittest", 2,
      "unittest で2つの値が等しいことを表明（assert）するメソッドはどれか。",
      ["assertEqual", "assertSame", "assertEquals2", "checkEqual"],
      0,
      "assertEqual(a, b) は a == b を表明する。失敗するとテストが fail する。",
      "assertEqual")

    q(16, "unittest", 2,
      "条件が真であることを表明するメソッドはどれか。",
      ["assertTrue", "assertOk", "assertYes", "assertValid"],
      0,
      "assertTrue(x) は bool(x) が True であることを表明する。逆は assertFalse。",
      "assertTrue")

    q(16, "unittest", 2,
      "値が None であることを表明するメソッドはどれか。",
      ["assertIsNone", "assertNull", "assertNone", "assertEmpty"],
      0,
      "assertIsNone(x) は x is None を表明する。逆は assertIsNotNone。",
      "assertIsNone")

    q(16, "unittest", 2,
      "要素がコンテナに含まれることを表明するメソッドはどれか。",
      ["assertIn", "assertContains", "assertHas", "assertMember"],
      0,
      "assertIn(a, b) は a in b を表明する。",
      "assertIn")

    q(16, "unittest", 3,
      "特定の例外が送出されることをテストするメソッドはどれか。",
      ["assertRaises", "assertException", "assertError", "expectRaises"],
      0,
      "with self.assertRaises(ValueError): ... の形で、ブロック内が例外を送出することを表明する。",
      "assertRaises")

    q(16, "unittest", 3,
      "各テストメソッドの実行前に毎回呼ばれる準備用メソッドはどれか。",
      ["setUp", "setUpClass のみ", "before", "init"],
      0,
      "setUp は各テストの前、tearDown は後に毎回実行される。クラス単位は setUpClass/tearDownClass。",
      "setUp / tearDown")

    q(16, "unittest", 3,
      "クラス内の全テストの前に一度だけ実行されるメソッドはどれか。",
      ["setUpClass（@classmethod）", "setUp", "beforeAll", "initClass"],
      0,
      "setUpClass は @classmethod として定義し、クラスの全テスト前に一度だけ実行される。",
      "setUpClass")

    q(16, "実行", 2,
      "コマンドラインで unittest を使ってテストを自動検出・実行するコマンドはどれか。",
      ["python -m unittest", "python unittest", "python -t", "python --test"],
      0,
      "`python -m unittest`（discover）でテストを自動検出して実行できる。",
      "unittest --- 実行")

    q(16, "doctest", 3,
      "docstring 内に書いた対話例（>>> ...）を検証する標準ライブラリはどれか。",
      ["doctest", "unittest", "pydoc", "docexam"],
      0,
      "doctest は docstring の対話例を実行し、出力が一致するか検証する。",
      "doctest")

    q(16, "doctest", 3,
      "doctest で検証されるのは、docstring 内のどの記述か。",
      [">>> で始まる行とその直後の期待出力",
       "# で始まるコメント",
       "通常の説明文すべて",
       "関数のシグネチャ"],
      0,
      "doctest は `>>>` の式とその次行の期待される出力を比較する。",
      "doctest --- 記法")

    q(16, "mock", 3,
      "依存オブジェクトを偽物に差し替えるための標準ライブラリはどれか。",
      ["unittest.mock", "unittest.fake", "mocklib", "stubs"],
      0,
      "unittest.mock の Mock/MagicMock/patch で依存を置き換え、外部依存を切り離してテストできる。",
      "unittest.mock")

    q(16, "mock", 3,
      "unittest.mock で、テスト中だけ対象を一時的に置き換えるのに使うものはどれか。",
      ["patch", "replace", "swap", "override"],
      0,
      "mock.patch はデコレータ/コンテキストマネージャとして対象を一時的に Mock に置き換える。",
      "mock.patch")

    q(16, "命名", 2,
      "unittest が自動的にテストと認識するメソッド名の条件はどれか。",
      ["test で始まる", "必ず check で始まる", "末尾が _test", "大文字で始まる"],
      0,
      "既定では `test` で始まるメソッドがテストとして収集・実行される。",
      "テストメソッドの命名規則")

    q(16, "assertAlmostEqual", 3,
      "浮動小数点の比較で、丸め誤差を考慮して『ほぼ等しい』ことを表明するメソッドはどれか。",
      ["assertAlmostEqual", "assertEqual", "assertFloatEqual", "assertnear"],
      0,
      "assertAlmostEqual は指定桁数で丸めて比較する。0.1+0.2 のような誤差に有効。",
      "assertAlmostEqual")

    q(16, "skip", 3,
      "特定のテストを条件付きでスキップするデコレータはどれか。",
      ["@unittest.skipIf", "@unittest.ignore", "@skiptest", "@unittest.pass"],
      0,
      "@unittest.skip / @unittest.skipIf / @unittest.skipUnless でスキップを制御できる。",
      "unittest --- skip")

    q(16, "AAA", 2,
      "単体テストの基本構成 Arrange-Act-Assert の説明として正しいものはどれか。",
      ["準備→実行→検証 の順にテストを書く",
       "実行→準備→検証 の順",
       "全てのテストを1つの関数にまとめる",
       "本番DBを必ず使う"],
      0,
      "Arrange（準備）→ Act（実行）→ Assert（検証）が読みやすいテストの基本構造。",
      "テスト構造 --- AAA")

    q(16, "原則", 2,
      "良い単体テストの性質として最も適切なものはどれか。",
      ["独立していて、実行順序に依存しない",
       "互いに依存し、決まった順序で動く必要がある",
       "必ずネットワークにアクセスする",
       "1つのテストで全機能を検証する"],
      0,
      "各テストは独立・再現可能で、順序に依存しないのが望ましい。外部依存は mock で切り離す。",
      "テストの独立性")

    q(16, "assertEqual", 2,
      "次の unittest のテストは成功するか失敗するか。",
      ["成功する", "失敗する", "エラーで実行できない", "スキップされる"],
      0,
      "1 + 1 は 2 なので assertEqual(2, 1+1) は真、テストは成功する。",
      "assertEqual の判定",
      code="import unittest\nclass T(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(2, 1 + 1)\nr = unittest.TextTestRunner(verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))\nprint('成功する' if r.wasSuccessful() else '失敗する')",
      verify=True)

    q(16, "カバレッジ", 2,
      "テストがソースコードのどれだけを実行したかを測る指標を何と呼ぶか。",
      ["コードカバレッジ（網羅率）", "ベンチマーク", "リント率", "複雑度"],
      0,
      "コードカバレッジはテストが実行した行・分岐の割合。coverage.py 等で計測する。",
      "コードカバレッジ")

    q(16, "pytest", 2,
      "シンプルな assert 文でテストを書けることで知られるサードパーティ製テストツールはどれか（参考）。",
      ["pytest", "unittest", "doctest", "mock"],
      0,
      "pytest は plain な assert でテストを書ける人気ツール。ただしサードパーティ製のため本試験の出題対象は標準ライブラリ中心であることに注意。",
      "pytest（参考）")


# ============================================================
# 第17章 デバッグ
# ============================================================
def ch17(q):
    q(17, "pdb", 2,
      "Python 標準のデバッガはどれか。",
      ["pdb", "gdb", "ipdb", "debugpy"],
      0,
      "pdb が標準ライブラリのデバッガ。ipdb・debugpy はサードパーティ。",
      "pdb")

    q(17, "breakpoint", 2,
      "Python 3.7 以降で、コード中に書くだけでデバッガを起動できる組み込み関数はどれか。",
      ["breakpoint()", "debug()", "pdb()", "trace()"],
      0,
      "breakpoint() は 3.7 で追加。既定で pdb.set_trace() を呼ぶ。環境変数 PYTHONBREAKPOINT で切替可能。",
      "breakpoint()")

    q(17, "pdb", 3,
      "コード内で実行を止めて pdb を起動する従来の関数呼び出しはどれか。",
      ["pdb.set_trace()", "pdb.start()", "pdb.run_here()", "pdb.break()"],
      0,
      "import pdb; pdb.set_trace() で対話デバッグに入る。breakpoint() はこれの新しい入口。",
      "pdb.set_trace")

    q(17, "pdb コマンド", 3,
      "pdb の対話中で『次の行へ進む（関数には入らない）』コマンドはどれか。",
      ["n (next)", "s (step)", "c (continue)", "q (quit)"],
      0,
      "n は次行へ（ステップオーバー）、s は関数内へ入る（ステップイン）、c は次のブレークまで継続。",
      "pdb --- コマンド")

    q(17, "pdb コマンド", 3,
      "pdb で『関数の内部へ入る（ステップイン）』コマンドはどれか。",
      ["s (step)", "n (next)", "r (return)", "l (list)"],
      0,
      "s は呼び出し先の関数に入る。n は関数を実行して次行に進む。",
      "pdb --- step")

    q(17, "traceback", 2,
      "例外発生時に表示される、呼び出し履歴付きのエラー情報を何と呼ぶか。",
      ["トレースバック（traceback）", "スタックダンプ", "コアダンプ", "ログレベル"],
      0,
      "例外時に出る呼び出し履歴付きのメッセージがトレースバック。traceback モジュールで整形・取得できる。",
      "traceback")

    q(17, "traceback", 3,
      "捕捉した例外のトレースバックを文字列やコンソールに出力する標準ライブラリはどれか。",
      ["traceback", "sys.exc", "inspect", "warnings"],
      0,
      "traceback.print_exc() や format_exc() でトレースバックを出力・取得できる。",
      "traceback モジュール")

    q(17, "assert", 2,
      "次のコードを通常実行（最適化なし）したときの挙動として正しいものはどれか。",
      ["AssertionError が送出される", "False と表示される", "何も起きずに終了", "SyntaxError"],
      0,
      "assert 条件 は条件が偽のとき AssertionError を送出する。デバッグ・前提条件チェックに使う。",
      "assert 文",
      code="try:\n    assert 1 == 2\nexcept AssertionError:\n    print('AssertionError が送出される')", verify=True)

    q(17, "assert", 3,
      "Python を `-O`（最適化）オプション付きで実行したときの assert の扱いはどれか。",
      ["assert 文は無効化される（実行されない）",
       "assert がより厳密になる",
       "全ての例外が無視される",
       "影響はない"],
      0,
      "`-O` 実行時は __debug__ が False になり assert 文が取り除かれる。前提保証を assert だけに頼らない理由。",
      "assert と -O オプション")

    q(17, "warnings", 3,
      "将来非推奨になる機能などについて、実行を止めずに警告を出す標準ライブラリはどれか。",
      ["warnings", "logging", "exceptions", "alerts"],
      0,
      "warnings.warn(...) で警告を出せる。DeprecationWarning などのカテゴリがある。",
      "warnings")

    q(17, "logging", 2,
      "print デバッグの代わりに、レベル付き・出力先制御が可能なデバッグ手段として推奨されるのはどれか。",
      ["logging モジュール", "コメントアウト", "time.sleep", "input()"],
      0,
      "logging は出力レベルやフォーマット、出力先を制御でき、print デバッグより保守的。",
      "logging によるデバッグ")

    q(17, "pprint", 2,
      "ネストした大きなデータ構造を見やすく整形して表示する標準ライブラリはどれか。",
      ["pprint", "prettyprint", "format", "display"],
      0,
      "pprint.pprint は辞書やリストを整形（インデント・改行）して表示する。",
      "pprint")

    q(17, "inspect", 3,
      "実行中のオブジェクトのソースや引数情報などを調べる標準ライブラリはどれか。",
      ["inspect", "dis", "trace", "reflection"],
      0,
      "inspect は関数のシグネチャやソース、スタックフレームなどを調べられる。",
      "inspect")

    q(17, "timeit", 3,
      "小さなコード断片の実行時間を計測する標準ライブラリはどれか。",
      ["timeit", "time.clock", "profile2", "benchmark"],
      0,
      "timeit はコードを多数回実行して所要時間を計測する。マイクロベンチマーク向け。",
      "timeit")

    q(17, "cProfile", 3,
      "関数ごとの呼び出し回数や所要時間を計測（プロファイリング）する標準ライブラリはどれか。",
      ["cProfile", "timeit", "pdb", "trace"],
      0,
      "cProfile は実行をプロファイルし、関数単位の統計を出力する。ボトルネック特定に使う。",
      "cProfile")


# ============================================================
# 第18章 暗号関連
# ============================================================
def ch18(q):
    q(18, "hashlib", 2,
      "MD5 や SHA-256 などのハッシュ値を計算する標準ライブラリはどれか。",
      ["hashlib", "crypt", "hashes", "digest"],
      0,
      "hashlib が各種ハッシュアルゴリズム（sha256, md5, sha1 等）を提供する。",
      "hashlib")

    q(18, "hashlib", 3,
      "次のコードの出力として正しいものはどれか。",
      ["64", "32", "256", "16"],
      0,
      "SHA-256 のダイジェストは256ビット＝32バイト。hexdigest() は1バイトを16進2文字で表すため文字数は64。",
      "hashlib --- SHA-256 の長さ",
      code="import hashlib\nprint(len(hashlib.sha256(b'abc').hexdigest()))", verify=True)

    q(18, "hashlib", 3,
      "ハッシュ関数の性質として正しいものはどれか。",
      ["同じ入力からは常に同じハッシュ値が得られ、ハッシュから元の入力を復元するのは困難",
       "ハッシュ値から元のデータを簡単に復元できる",
       "同じ入力でも毎回異なる値になる",
       "入力長に比例してハッシュ長が伸びる"],
      0,
      "暗号学的ハッシュは決定的（同入力→同出力）かつ一方向性（逆算困難）。固定長の値を返す。",
      "ハッシュ関数の性質")

    q(18, "secrets", 3,
      "トークンやパスワードなど、安全な乱数を生成するために推奨される標準ライブラリはどれか。",
      ["secrets", "random", "os.rand", "uuid"],
      0,
      "secrets は暗号用途向けの安全な乱数を生成する。random モジュールはセキュリティ用途には使わない。",
      "secrets")

    q(18, "random", 2,
      "セキュリティ用途で random モジュールを使うべきでない理由として正しいものはどれか。",
      ["疑似乱数で予測可能なため、トークン生成等には不適切",
       "生成が遅すぎるため",
       "整数しか生成できないため",
       "標準ライブラリではないため"],
      0,
      "random は決定的な疑似乱数生成器で予測可能。鍵・トークンには secrets を使う。",
      "random と secrets の使い分け")

    q(18, "パスワード", 3,
      "パスワードを保存する際の適切な扱いとして最も正しいものはどれか。",
      ["ソルト付きの専用ハッシュ（例: hashlib.pbkdf2_hmac 等）でハッシュ化して保存する",
       "平文のまま保存する",
       "可逆暗号で暗号化して必ず復号できるようにする",
       "MD5 で1回だけハッシュ化すれば十分"],
      0,
      "パスワードはソルト付きの鍵導出関数（pbkdf2_hmac, scrypt 等）でハッシュ化して保存する。平文保存や単純MD5は不適切。",
      "パスワードのハッシュ化")

    q(18, "hmac", 3,
      "メッセージの改ざん検知・認証に使う、鍵付きハッシュを扱う標準ライブラリはどれか。",
      ["hmac", "hashlib のみ", "secrets", "ssl"],
      0,
      "hmac は秘密鍵とハッシュ関数を組み合わせ、メッセージ認証コード（MAC）を生成する。",
      "hmac")

    q(18, "比較", 3,
      "ハッシュ値やトークンを比較する際、タイミング攻撃を避けるために使う関数はどれか。",
      ["hmac.compare_digest", "==", "is", "str.equals"],
      0,
      "秘密情報の比較は hmac.compare_digest（または secrets.compare_digest）を使い、比較時間を一定にしてタイミング攻撃を防ぐ。",
      "compare_digest")

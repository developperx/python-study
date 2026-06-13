// 問題データの読込・統合。data/index.json を読み、各章JSONをまとめてロードする。
let _chapters = null;   // index.json の chapters 配列
let _questions = null;  // 全問題フラット配列
let _byId = null;       // id -> question
let _loadPromise = null;

async function fetchJson(path) {
  const res = await fetch(path, { cache: 'no-cache' });
  if (!res.ok) throw new Error(`fetch failed: ${path} (${res.status})`);
  return res.json();
}

export async function loadData() {
  if (_loadPromise) return _loadPromise;
  _loadPromise = (async () => {
    const index = await fetchJson('./data/index.json');
    _chapters = index.chapters;
    const lists = await Promise.all(
      _chapters.map((c) => fetchJson(`./data/${c.file}`).catch((e) => {
        console.warn('chapter load failed', c.file, e);
        return [];
      }))
    );
    _questions = [];
    lists.forEach((list, i) => {
      const ch = _chapters[i].chapter;
      for (const q of list) {
        // 章番号はファイル側を正とする（取り違え防止）
        q.chapter = ch;
        _questions.push(q);
      }
    });
    _byId = new Map(_questions.map((q) => [q.id, q]));
    // 各章の実問題数を反映
    for (const c of _chapters) {
      c.count = _questions.filter((q) => q.chapter === c.chapter).length;
    }
    return { chapters: _chapters, questions: _questions };
  })();
  return _loadPromise;
}

export const data = {
  chapters: () => _chapters || [],
  questions: () => _questions || [],
  byId: (id) => (_byId ? _byId.get(id) : undefined),
  byIds: (ids) => ids.map((id) => _byId.get(id)).filter(Boolean),
  byChapter: (ch) => (_questions || []).filter((q) => q.chapter === ch),
  chapterMeta: (ch) => (_chapters || []).find((c) => c.chapter === ch),
  total: () => (_questions || []).length,
  examConfig: () => EXAM,
};

// 本番試験の構成。出題範囲(公式比率準拠)に沿って模試の章別出題数を定義。
export const EXAM = {
  totalQuestions: 40,
  durationSec: 75 * 60,
  passRatio: 0.7, // 70% (28/40)
  // 章番号 -> 模試での出題数（合計40）
  distribution: {
    1: 1, 2: 2, 3: 7, 4: 2, 5: 1, 6: 4, 8: 2, 9: 5,
    10: 2, 11: 2, 13: 3, 14: 2, 16: 3, 17: 2, 18: 2,
  },
};

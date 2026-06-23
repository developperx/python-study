// 出題ロジック・採点。模試/章別/ランダム/復習の各セッションを生成する。
import { data, EXAM } from './data.js';

export function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function pick(arr, n) {
  return shuffle(arr).slice(0, n);
}

// 問題の選択肢をシャッフルし、正解インデックス・選択肢別理由を対応づけて並び替える。
// 元の問題は変更せず、新しいオブジェクトを返す（作問は正解=index0 のため表示時にランダム化）。
export function shuffleChoices(q) {
  const n = q.choices.length;
  const perm = shuffle([...Array(n).keys()]); // perm[newIdx] = oldIdx
  const oldAns = new Set(Array.isArray(q.answer) ? q.answer : [q.answer]);
  const choices = perm.map((o) => q.choices[o]);
  const rationales = Array.isArray(q.rationales) ? perm.map((o) => q.rationales[o]) : q.rationales;
  const answer = [];
  perm.forEach((o, newIdx) => { if (oldAns.has(o)) answer.push(newIdx); });
  return { ...q, choices, rationales, answer };
}

// セッション内の各問について選択肢をシャッフルする。
function prepare(questions) {
  return questions.map(shuffleChoices);
}

// 配列を正解判定可能な形に正規化（answer は number か number[]）
function answerSet(q) {
  return new Set(Array.isArray(q.answer) ? q.answer : [q.answer]);
}

export function isMultiple(q) {
  return q.type === 'multiple' || answerSet(q).size > 1;
}

// 選択した index 配列が正解か
export function isCorrect(q, selected) {
  const ans = answerSet(q);
  const sel = new Set(selected);
  if (ans.size !== sel.size) return false;
  for (const a of ans) if (!sel.has(a)) return false;
  return true;
}

// 模擬試験セッション: 出題比率に従って章ごとに抽出し計40問
export function buildMockSession() {
  const questions = [];
  for (const [chStr, num] of Object.entries(EXAM.distribution)) {
    const ch = Number(chStr);
    const pool = data.byChapter(ch);
    const chosen = pick(pool, Math.min(num, pool.length));
    questions.push(...chosen);
  }
  // 不足分（プール不足時）は全体からランダム補充
  if (questions.length < EXAM.totalQuestions) {
    const have = new Set(questions.map((q) => q.id));
    const rest = data.questions().filter((q) => !have.has(q.id));
    questions.push(...pick(rest, EXAM.totalQuestions - questions.length));
  }
  return {
    mode: 'mock',
    questions: prepare(shuffle(questions).slice(0, EXAM.totalQuestions)),
    timed: true,
    durationSec: EXAM.durationSec,
  };
}

export function buildChapterSession(chapter, limit = 0) {
  let pool = shuffle(data.byChapter(chapter));
  if (limit > 0) pool = pool.slice(0, limit);
  return { mode: 'chapter', chapter, questions: prepare(pool), timed: false };
}

export function buildRandomSession({ count = 20, chapters = null, difficulty = null } = {}) {
  let pool = data.questions();
  if (chapters && chapters.length) pool = pool.filter((q) => chapters.includes(q.chapter));
  if (difficulty) pool = pool.filter((q) => q.difficulty === difficulty);
  return { mode: 'random', questions: prepare(pick(pool, Math.min(count, pool.length))), timed: false };
}

export function buildReviewSession(ids) {
  const qs = data.byIds(ids);
  return { mode: 'review', questions: prepare(shuffle(qs)), timed: false };
}

// 採点（章別集計つき）
export function gradeSession(session, answers) {
  // answers: Map<questionId, number[]>
  let correct = 0;
  const perChapter = {};
  const details = [];
  for (const q of session.questions) {
    const sel = answers.get(q.id) || [];
    const ok = isCorrect(q, sel);
    if (ok) correct += 1;
    if (!perChapter[q.chapter]) perChapter[q.chapter] = { correct: 0, total: 0 };
    perChapter[q.chapter].total += 1;
    if (ok) perChapter[q.chapter].correct += 1;
    details.push({ q, selected: sel, correct: ok });
  }
  const total = session.questions.length;
  const ratio = total ? correct / total : 0;
  const passed = ratio >= EXAM.passRatio;
  return { correct, total, ratio, passed, perChapter, details };
}

// localStorage 永続化レイヤ。進捗・成績履歴・誤答・ブックマーク・設定を管理する。
const KEY = 'py3cpe_v1';

const defaultState = () => ({
  // questionId -> { seen, correct, wrong, lastResult: 'correct'|'wrong', bookmarked }
  questions: {},
  // 模擬試験の履歴 [{ date, score, total, passed, durationSec }]
  mockHistory: [],
  settings: { theme: null }, // null=未設定(OS追従)
});

let state = load();

function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return defaultState();
    const parsed = JSON.parse(raw);
    return { ...defaultState(), ...parsed, settings: { ...defaultState().settings, ...(parsed.settings || {}) } };
  } catch (e) {
    console.warn('storage load failed', e);
    return defaultState();
  }
}

function persist() {
  try {
    localStorage.setItem(KEY, JSON.stringify(state));
  } catch (e) {
    console.warn('storage persist failed', e);
  }
}

function qrec(id) {
  if (!state.questions[id]) {
    state.questions[id] = { seen: 0, correct: 0, wrong: 0, lastResult: null, bookmarked: false };
  }
  return state.questions[id];
}

export const store = {
  getState: () => state,

  // 1問の回答結果を記録
  recordAnswer(id, isCorrect) {
    const r = qrec(id);
    r.seen += 1;
    if (isCorrect) { r.correct += 1; r.lastResult = 'correct'; }
    else { r.wrong += 1; r.lastResult = 'wrong'; }
    persist();
  },

  toggleBookmark(id) {
    const r = qrec(id);
    r.bookmarked = !r.bookmarked;
    persist();
    return r.bookmarked;
  },

  isBookmarked: (id) => !!(state.questions[id] && state.questions[id].bookmarked),

  // 直近で誤答した問題ID一覧
  wrongIds() {
    return Object.keys(state.questions).filter((id) => state.questions[id].lastResult === 'wrong');
  },

  bookmarkedIds() {
    return Object.keys(state.questions).filter((id) => state.questions[id].bookmarked);
  },

  // 章ごとの集計 { seen, correct, accuracy }
  chapterStats(chapter, questionIds) {
    let seen = 0, correct = 0;
    for (const id of questionIds) {
      const r = state.questions[id];
      if (r && r.seen > 0) { seen += 1; if (r.lastResult === 'correct') correct += 1; }
    }
    return { seen, correct, accuracy: seen ? correct / seen : 0 };
  },

  addMockResult(result) {
    state.mockHistory.unshift(result);
    state.mockHistory = state.mockHistory.slice(0, 50);
    persist();
  },

  getMockHistory: () => state.mockHistory,

  totalAnswered() {
    return Object.values(state.questions).reduce((a, r) => a + r.seen, 0);
  },

  overallAccuracy() {
    let c = 0, w = 0;
    for (const r of Object.values(state.questions)) {
      if (r.lastResult === 'correct') c++;
      else if (r.lastResult === 'wrong') w++;
    }
    const t = c + w;
    return { answered: t, correct: c, accuracy: t ? c / t : 0 };
  },

  setTheme(theme) { state.settings.theme = theme; persist(); },
  getTheme: () => state.settings.theme,

  resetProgress() {
    state = defaultState();
    persist();
  },
};

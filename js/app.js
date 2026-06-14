// アプリのエントリ。ルーティング・画面描画・クイズ進行・タイマーを統括する。
import { loadData, data, EXAM } from './data.js';
import { store } from './storage.js';
import {
  buildMockSession, buildChapterSession, buildRandomSession, buildReviewSession,
  gradeSession, isCorrect, isMultiple,
} from './quiz.js';
import { h, escapeHtml, formatTime, pct, chLabel, codeBlock, MARK, accClass } from './ui.js';

const appEl = document.getElementById('app');
let timerHandle = null;

/* ---------- テーマ ---------- */
function applyTheme(theme) {
  const t = theme || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', t);
  document.getElementById('themeToggle').textContent = t === 'dark' ? '☀️' : '🌙';
}
function initTheme() {
  applyTheme(store.getTheme());
  document.getElementById('themeToggle').addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'dark' ? 'light' : 'dark';
    store.setTheme(next);
    applyTheme(next);
  });
}

/* ---------- ルーティング ---------- */
const routes = {
  home: renderHome,
  mock: renderMockStart,
  chapters: renderChapters,
  random: renderRandomSetup,
  review: renderReview,
  stats: renderStats,
};

function setActiveNav(route) {
  document.querySelectorAll('.topnav__btn').forEach((b) => {
    b.classList.toggle('is-active', b.dataset.route === route);
  });
}

function navigate(route) {
  if (timerHandle) { clearInterval(timerHandle); timerHandle = null; }
  window.scrollTo(0, 0);
  setActiveNav(route);
  (routes[route] || renderHome)();
}

/* ---------- ホーム ---------- */
function renderHome() {
  const ov = store.overallAccuracy();
  const hist = store.getMockHistory();
  const lastMock = hist[0];
  appEl.innerHTML = `
    <section class="card">
      <h1 class="section-title">Python3エンジニア認定実践試験 対策</h1>
      <p class="section-sub">本番形式の模擬試験・章別演習・弱点復習で、合格ライン70%突破を目指しましょう。全${data.total()}問収録。</p>
      <div class="stat-tiles">
        <div class="stat-tile"><div class="stat-tile__num">${data.total()}</div><div class="stat-tile__label">収録問題数</div></div>
        <div class="stat-tile"><div class="stat-tile__num">${store.totalAnswered()}</div><div class="stat-tile__label">のべ回答数</div></div>
        <div class="stat-tile"><div class="stat-tile__num">${ov.answered ? pct(ov.accuracy) : '—'}</div><div class="stat-tile__label">直近正答率</div></div>
        <div class="stat-tile"><div class="stat-tile__num">${lastMock ? pct(lastMock.score / lastMock.total) : '—'}</div><div class="stat-tile__label">前回の模試</div></div>
      </div>
    </section>

    <div class="grid grid--2">
      ${modeCard('mock', '📝', '模擬試験', '本番同様 40問・75分。出題比率を再現し70%で合否判定。')}
      ${modeCard('chapters', '📚', '章別演習', '15章ごとに集中ドリル。即時採点＋解説。')}
      ${modeCard('random', '🎲', 'ランダム練習', '章・難易度を指定してランダム出題。')}
      ${modeCard('review', '🔁', '弱点復習', '間違えた問題・ブックマークだけを再挑戦。')}
    </div>
  `;
  appEl.querySelectorAll('[data-go]').forEach((c) => c.addEventListener('click', () => navigate(c.dataset.go)));
}
function modeCard(route, icon, title, desc) {
  return `<button class="card mode-card" data-go="${route}">
    <span class="mode-card__icon">${icon}</span>
    <span class="mode-card__title">${title}</span>
    <span class="mode-card__desc">${desc}</span>
  </button>`;
}

/* ---------- 模擬試験スタート ---------- */
function renderMockStart() {
  const hist = store.getMockHistory();
  appEl.innerHTML = `
    <section class="card">
      <h2 class="section-title">📝 模擬試験</h2>
      <p class="section-sub">本番と同じ <strong>40問 / 制限時間75分 / 合格ライン70%（28問正解）</strong>。出題範囲の比率に沿って各章から出題します。</p>
      <ul class="note">
        <li>制限時間が0になると自動で採点されます。</li>
        <li>途中で中断すると記録は残りません。</li>
        <li>解説は採点後（結果画面）に確認できます。</li>
      </ul>
      <div class="mt"><button class="btn btn--primary btn--lg" id="startMock">模擬試験を開始する</button></div>
    </section>
    ${hist.length ? historyCard(hist) : ''}
  `;
  document.getElementById('startMock').addEventListener('click', () => startSession(buildMockSession()));
}

function historyCard(hist) {
  const rows = hist.slice(0, 10).map((m) => `
    <tr>
      <td>${new Date(m.date).toLocaleString('ja-JP', { dateStyle: 'short', timeStyle: 'short' })}</td>
      <td>${m.score} / ${m.total}</td>
      <td>${pct(m.score / m.total)}</td>
      <td class="${m.passed ? 'pass' : 'fail'}">${m.passed ? '合格' : '不合格'}</td>
    </tr>`).join('');
  return `<section class="card">
    <h3 class="section-title" style="font-size:16px">模試の履歴</h3>
    <table class="hist"><thead><tr><th>日時</th><th>得点</th><th>正答率</th><th>判定</th></tr></thead><tbody>${rows}</tbody></table>
  </section>`;
}

/* ---------- 章別演習 ---------- */
function renderChapters() {
  const rows = data.chapters().map((c) => {
    const ids = data.byChapter(c.chapter).map((q) => q.id);
    const st = store.chapterStats(c.chapter, ids);
    return `<div class="ch-row">
      <div class="ch-row__no">${c.chapter}</div>
      <div class="ch-row__main">
        <div class="ch-row__title">${escapeHtml(c.title)}</div>
        <div class="ch-row__sub">${c.count}問 ・ 試験比率 ${c.weight}</div>
      </div>
      <div class="ch-row__acc">
        <div class="ch-row__sub">${st.seen ? `正答率 ${pct(st.accuracy)}` : '未着手'}</div>
        <button class="btn" data-ch="${c.chapter}" style="margin-top:4px;padding:6px 12px">演習</button>
      </div>
    </div>`;
  }).join('');
  appEl.innerHTML = `
    <section class="card">
      <h2 class="section-title">📚 章別演習</h2>
      <p class="section-sub">出題範囲の15章。出題比率の高い章（3章・9章・6章）を重点的に。</p>
      ${rows}
    </section>`;
  appEl.querySelectorAll('[data-ch]').forEach((b) =>
    b.addEventListener('click', () => startSession(buildChapterSession(Number(b.dataset.ch)))));
}

/* ---------- ランダム設定 ---------- */
function renderRandomSetup() {
  const chOpts = data.chapters().map((c) =>
    `<label class="checkbox-row"><input type="checkbox" name="ch" value="${c.chapter}" checked> ${chLabel(c.chapter)} ${escapeHtml(c.title)}（${c.count}）</label>`).join('');
  appEl.innerHTML = `
    <section class="card">
      <h2 class="section-title">🎲 ランダム練習</h2>
      <p class="section-sub">条件を指定してランダムに出題します。</p>
      <label class="field">出題数
        <select id="rCount"><option>10</option><option selected>20</option><option>30</option><option>40</option></select>
      </label>
      <label class="field">難易度
        <select id="rDiff"><option value="0">すべて</option><option value="1">易しい</option><option value="2">標準</option><option value="3">難しい</option></select>
      </label>
      <div class="field">対象の章
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-top:6px">${chOpts}</div>
      </div>
      <button class="btn btn--primary btn--lg" id="startRandom">開始する</button>
    </section>`;
  document.getElementById('startRandom').addEventListener('click', () => {
    const count = Number(document.getElementById('rCount').value);
    const difficulty = Number(document.getElementById('rDiff').value) || null;
    const chapters = [...appEl.querySelectorAll('input[name="ch"]:checked')].map((i) => Number(i.value));
    if (!chapters.length) { alert('章を1つ以上選択してください'); return; }
    const session = buildRandomSession({ count, chapters, difficulty });
    if (!session.questions.length) { alert('条件に合う問題がありません'); return; }
    startSession(session);
  });
}

/* ---------- 弱点復習 ---------- */
function renderReview() {
  const wrong = store.wrongIds();
  const marks = store.bookmarkedIds();
  appEl.innerHTML = `
    <section class="card">
      <h2 class="section-title">🔁 弱点復習</h2>
      <p class="section-sub">間違えた問題やブックマークした問題だけを再挑戦できます。</p>
      <div class="grid grid--2">
        <div class="card" style="margin:0">
          <div class="mode-card__title">間違えた問題</div>
          <div class="mode-card__desc">直近で誤答した ${wrong.length} 問</div>
          <button class="btn btn--primary mt" id="revWrong" ${wrong.length ? '' : 'disabled'}>復習する</button>
        </div>
        <div class="card" style="margin:0">
          <div class="mode-card__title">ブックマーク</div>
          <div class="mode-card__desc">★を付けた ${marks.length} 問</div>
          <button class="btn btn--primary mt" id="revMark" ${marks.length ? '' : 'disabled'}>復習する</button>
        </div>
      </div>
      ${(!wrong.length && !marks.length) ? '<p class="note mt">まだ記録がありません。模試や演習に挑戦すると、ここに苦手問題が集まります。</p>' : ''}
    </section>`;
  const bw = document.getElementById('revWrong');
  const bm = document.getElementById('revMark');
  if (bw && wrong.length) bw.addEventListener('click', () => startSession(buildReviewSession(wrong)));
  if (bm && marks.length) bm.addEventListener('click', () => startSession(buildReviewSession(marks)));
}

/* ---------- 成績 ---------- */
function renderStats() {
  const ov = store.overallAccuracy();
  const hist = store.getMockHistory();
  const chRows = data.chapters().map((c) => {
    const ids = data.byChapter(c.chapter).map((q) => q.id);
    const st = store.chapterStats(c.chapter, ids);
    return `<div class="ch-row">
      <div class="ch-row__no">${c.chapter}</div>
      <div class="ch-row__main">
        <div class="ch-row__title">${escapeHtml(c.title)}</div>
        <div class="bar" style="margin-top:6px"><div class="bar__fill ${accClass(st.accuracy) ? 'bar__fill--pass' : ''}" style="width:${Math.round(st.accuracy * 100)}%"></div></div>
      </div>
      <div class="ch-row__acc"><div class="ch-row__sub">${st.seen ? `${pct(st.accuracy)}（${st.seen}問）` : '未着手'}</div></div>
    </div>`;
  }).join('');
  appEl.innerHTML = `
    <section class="card">
      <h2 class="section-title">📊 成績・進捗</h2>
      <div class="stat-tiles">
        <div class="stat-tile"><div class="stat-tile__num">${store.totalAnswered()}</div><div class="stat-tile__label">のべ回答数</div></div>
        <div class="stat-tile"><div class="stat-tile__num">${ov.answered ? pct(ov.accuracy) : '—'}</div><div class="stat-tile__label">総合正答率</div></div>
        <div class="stat-tile"><div class="stat-tile__num">${hist.length}</div><div class="stat-tile__label">模試 受験回数</div></div>
        <div class="stat-tile"><div class="stat-tile__num">${hist.filter((m) => m.passed).length}</div><div class="stat-tile__label">合格回数</div></div>
      </div>
    </section>
    <section class="card">
      <h3 class="section-title" style="font-size:16px">章別 正答率</h3>
      ${chRows}
    </section>
    ${hist.length ? historyCard(hist) : ''}
    <section class="card">
      <h3 class="section-title" style="font-size:16px">データ管理</h3>
      <p class="note">進捗・成績はこのブラウザ内にのみ保存されています。</p>
      <button class="btn btn--danger" id="resetBtn">学習データをリセット</button>
    </section>`;
  document.getElementById('resetBtn').addEventListener('click', () => {
    if (confirm('全ての学習データ（進捗・成績・ブックマーク）を削除します。よろしいですか？')) {
      store.resetProgress();
      navigate('stats');
    }
  });
}

/* ---------- クイズ進行 ---------- */
let SESSION = null;
let IDX = 0;
let ANSWERS = new Map(); // id -> number[]
let SELECTED = [];       // 現在の問題の選択
let REVEALED = false;    // 練習モードで採点表示中か
let REMAIN = 0;

function startSession(session) {
  if (!session.questions.length) { alert('出題できる問題がありません'); return; }
  SESSION = session;
  IDX = 0;
  ANSWERS = new Map();
  setActiveNav(session.mode === 'mock' ? 'mock' : session.mode === 'chapter' ? 'chapters' : session.mode === 'random' ? 'random' : 'review');
  if (session.timed) {
    REMAIN = session.durationSec;
    timerHandle = setInterval(tick, 1000);
  }
  renderQuestion();
}

function tick() {
  REMAIN -= 1;
  const t = document.getElementById('timer');
  if (t) {
    t.textContent = '⏱ ' + formatTime(REMAIN);
    t.className = 'timer' + (REMAIN <= 60 ? ' timer--danger' : REMAIN <= 300 ? ' timer--warn' : '');
  }
  if (REMAIN <= 0) { clearInterval(timerHandle); timerHandle = null; finishSession(); }
}

function renderQuestion() {
  const q = SESSION.questions[IDX];
  const total = SESSION.questions.length;
  const isMock = SESSION.mode === 'mock';
  SELECTED = ANSWERS.get(q.id) ? ANSWERS.get(q.id).slice() : [];
  REVEALED = false;
  const multi = isMultiple(q);
  const meta = data.chapterMeta(q.chapter);
  const diffLabel = { 1: '易', 2: '標準', 3: '難' }[q.difficulty] || '標準';

  appEl.innerHTML = `
    <section class="card">
      <div class="quiz-top">
        <span class="quiz-progress">問 ${IDX + 1} / ${total}</span>
        ${SESSION.timed ? `<span class="timer" id="timer">⏱ ${formatTime(REMAIN)}</span>` : `<span class="note">${modeName(SESSION.mode)}</span>`}
      </div>
      <div class="bar" style="margin-bottom:14px"><div class="bar__fill" style="width:${Math.round(((IDX) / total) * 100)}%"></div></div>
      <div class="qmeta">
        <span class="tag tag--ch">${chLabel(q.chapter)} ${escapeHtml(meta ? meta.shortTitle || meta.title : '')}</span>
        ${q.topic ? `<span class="tag">${escapeHtml(q.topic)}</span>` : ''}
        <span class="tag">難易度: ${diffLabel}</span>
        ${multi ? '<span class="tag">複数選択</span>' : ''}
        <span class="spacer"></span>
        <button class="tag" id="bmBtn" title="ブックマーク">${store.isBookmarked(q.id) ? '★ 保存済' : '☆ 保存'}</button>
      </div>
      <div class="question-text">${escapeHtml(q.question)}</div>
      ${codeBlock(q.code)}
      <div class="choices" id="choices">
        ${q.choices.map((c, i) => `
          <button class="choice" data-i="${i}">
            <span class="choice__mark">${MARK(i)}</span>
            <span class="choice__body">${escapeHtml(c)}</span>
          </button>`).join('')}
      </div>
      <div id="explain"></div>
      <div class="quiz-actions">
        <button class="btn" id="quitBtn">中断</button>
        <span class="spacer"></span>
        ${isMock
          ? `${IDX > 0 ? '<button class="btn" id="prevBtn">前へ</button>' : ''}
             <button class="btn btn--primary" id="nextBtn">${IDX === total - 1 ? '採点する' : '次へ'}</button>`
          : `<button class="btn btn--primary" id="checkBtn" ${multi ? '' : ''}>解答する</button>
             <button class="btn btn--primary" id="nextBtn" style="display:none">${IDX === total - 1 ? '結果を見る' : '次の問題'}</button>`
        }
      </div>
    </section>`;

  // 選択肢
  appEl.querySelectorAll('.choice').forEach((btn) => {
    const i = Number(btn.dataset.i);
    if (SELECTED.includes(i)) btn.classList.add('is-selected');
    btn.addEventListener('click', () => onChoice(i, multi));
  });
  // ブックマーク
  document.getElementById('bmBtn').addEventListener('click', (e) => {
    const on = store.toggleBookmark(q.id);
    e.currentTarget.textContent = on ? '★ 保存済' : '☆ 保存';
  });
  document.getElementById('quitBtn').addEventListener('click', () => {
    if (confirm('この学習を中断しますか？（模試の場合、記録は残りません）')) {
      if (timerHandle) { clearInterval(timerHandle); timerHandle = null; }
      navigate('home');
    }
  });

  if (isMock) {
    if (IDX > 0) document.getElementById('prevBtn').addEventListener('click', () => { saveCurrent(); IDX--; renderQuestion(); });
    document.getElementById('nextBtn').addEventListener('click', () => {
      saveCurrent();
      if (IDX === total - 1) finishSession();
      else { IDX++; renderQuestion(); }
    });
  } else {
    document.getElementById('checkBtn').addEventListener('click', () => revealAnswer(q, multi));
    document.getElementById('nextBtn').addEventListener('click', () => {
      if (IDX === total - 1) finishSession();
      else { IDX++; renderQuestion(); }
    });
  }
}

function modeName(m) {
  return { chapter: '章別演習', random: 'ランダム練習', review: '弱点復習', mock: '模擬試験' }[m] || '';
}

function onChoice(i, multi) {
  if (REVEALED) return;
  if (multi) {
    const at = SELECTED.indexOf(i);
    if (at >= 0) SELECTED.splice(at, 1); else SELECTED.push(i);
  } else {
    SELECTED = [i];
  }
  appEl.querySelectorAll('.choice').forEach((btn) => {
    btn.classList.toggle('is-selected', SELECTED.includes(Number(btn.dataset.i)));
  });
}

function saveCurrent() {
  const q = SESSION.questions[IDX];
  ANSWERS.set(q.id, SELECTED.slice());
}

// 練習モード：その場で採点＆解説表示
function revealAnswer(q, multi) {
  if (!SELECTED.length) { alert('選択肢を選んでください'); return; }
  REVEALED = true;
  saveCurrent();
  const ok = isCorrect(q, SELECTED);
  store.recordAnswer(q.id, ok);
  // 選択肢を「正誤＋理由つき」の静的表示に差し替える
  document.getElementById('choices').innerHTML = annotatedChoicesHtml(q, SELECTED);
  document.getElementById('explain').innerHTML = explanationHtml(q, ok);
  document.getElementById('checkBtn').style.display = 'none';
  document.getElementById('nextBtn').style.display = '';
}

// 各選択肢を正誤マーク＋個別理由つきで描画する（採点後・見直し共通）
function annotatedChoicesHtml(q, selected) {
  const ans = new Set(Array.isArray(q.answer) ? q.answer : [q.answer]);
  const sel = new Set(selected || []);
  return q.choices.map((c, idx) => {
    const correct = ans.has(idx);
    let cls = 'choice choice--static';
    if (correct) cls += ' is-correct';
    else if (sel.has(idx)) cls += ' is-wrong';
    const rat = (q.rationales && q.rationales[idx]) ? q.rationales[idx] : (correct ? '正解。' : '不正解。');
    return `<div class="${cls}">
      <span class="choice__mark">${correct ? '✓' : '✗'}</span>
      <div class="choice__col">
        <div class="choice__body">${MARK(idx)}. ${escapeHtml(c)}${sel.has(idx) ? ' <span class="choice__picked">あなたの解答</span>' : ''}</div>
        <div class="choice__rat">${escapeHtml(rat)}</div>
      </div>
    </div>`;
  }).join('');
}

function explanationHtml(q, ok) {
  return `<div class="explanation ${ok ? 'explanation--correct' : 'explanation--wrong'}">
    <div class="explanation__head">${ok ? '✅ 正解' : '❌ 不正解'} ・ 総合解説</div>
    <div>${escapeHtml(q.explanation)}</div>
    ${q.reference ? `<div class="explanation__ref">📘 参考: ${escapeHtml(q.reference)}</div>` : ''}
  </div>`;
}

/* ---------- 採点・結果 ---------- */
function finishSession() {
  if (timerHandle) { clearInterval(timerHandle); timerHandle = null; }
  const result = gradeSession(SESSION, ANSWERS);
  // 模試はまとめて記録（練習モードは都度記録済み）
  if (SESSION.mode === 'mock') {
    for (const d of result.details) store.recordAnswer(d.q.id, d.correct);
    store.addMockResult({
      date: Date.now(), score: result.correct, total: result.total,
      passed: result.passed, durationSec: SESSION.durationSec - REMAIN,
    });
  }
  renderResult(result);
}

function renderResult(result) {
  setActiveNav(SESSION.mode === 'mock' ? 'mock' : '');
  const isMock = SESSION.mode === 'mock';
  const chRows = Object.entries(result.perChapter).sort((a, b) => Number(a[0]) - Number(b[0])).map(([ch, s]) => {
    const meta = data.chapterMeta(Number(ch));
    const r = s.correct / s.total;
    return `<div class="ch-row">
      <div class="ch-row__no">${ch}</div>
      <div class="ch-row__main">
        <div class="ch-row__title">${escapeHtml(meta ? meta.title : chLabel(Number(ch)))}</div>
        <div class="bar" style="margin-top:6px"><div class="bar__fill ${r >= 0.7 ? 'bar__fill--pass' : ''}" style="width:${Math.round(r * 100)}%"></div></div>
      </div>
      <div class="ch-row__acc"><div class="ch-row__sub">${s.correct}/${s.total}</div></div>
    </div>`;
  }).join('');

  const reviewList = result.details.map((d, i) => questionReviewHtml(d, i)).join('');

  appEl.innerHTML = `
    <section class="card">
      <div class="result-hero">
        ${isMock ? `<div class="result-badge ${result.passed ? 'result-badge--pass' : 'result-badge--fail'}">${result.passed ? '🎉 合格' : '不合格'}</div>` : ''}
        <div class="result-score">${result.correct}<span style="font-size:24px"> / ${result.total}</span></div>
        <div class="result-sub">正答率 ${pct(result.ratio)} ${isMock ? `（合格ライン 70%）` : ''}</div>
      </div>
      ${isMock ? `<div class="bar"><div class="bar__fill ${result.passed ? 'bar__fill--pass' : ''}" style="width:${Math.round(result.ratio * 100)}%"></div></div>` : ''}
      <div class="quiz-actions mt">
        <button class="btn" id="toHome">ホームへ</button>
        <span class="spacer"></span>
        ${isMock ? '<button class="btn btn--primary" id="retry">もう一度 模試に挑戦</button>' : '<button class="btn btn--primary" id="retry">同じ条件でもう一度</button>'}
      </div>
    </section>
    ${Object.keys(result.perChapter).length > 1 ? `<section class="card"><h3 class="section-title" style="font-size:16px">章別の正誤</h3>${chRows}</section>` : ''}
    <section class="card">
      <h3 class="section-title" style="font-size:16px">解答の見直し（全${result.total}問）</h3>
      <p class="note">各問の正解と解説を確認しましょう。★で復習リストに追加できます。</p>
      ${reviewList}
    </section>`;

  document.getElementById('toHome').addEventListener('click', () => navigate('home'));
  document.getElementById('retry').addEventListener('click', () => {
    if (SESSION.mode === 'mock') startSession(buildMockSession());
    else navigate(SESSION.mode === 'chapter' ? 'chapters' : SESSION.mode);
  });
  appEl.querySelectorAll('[data-bm]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const on = store.toggleBookmark(btn.dataset.bm);
      btn.textContent = on ? '★ 保存済' : '☆ 保存';
    });
  });
}

function questionReviewHtml(d, i) {
  const q = d.q;
  return `<div class="card" style="background:var(--bg-soft)">
    <div class="qmeta">
      <span class="tag tag--ch">${chLabel(q.chapter)}</span>
      ${q.topic ? `<span class="tag">${escapeHtml(q.topic)}</span>` : ''}
      <span class="tag" style="color:${d.correct ? 'var(--green)' : 'var(--red)'}">${d.correct ? '正解' : '不正解'}</span>
      <span class="spacer"></span>
      <button class="tag" data-bm="${q.id}">${store.isBookmarked(q.id) ? '★ 保存済' : '☆ 保存'}</button>
    </div>
    <div class="question-text" style="font-size:15px">${i + 1}. ${escapeHtml(q.question)}</div>
    ${codeBlock(q.code)}
    <div class="choices">${annotatedChoicesHtml(q, d.selected)}</div>
    <div class="explanation ${d.correct ? 'explanation--correct' : 'explanation--wrong'}">
      <div class="explanation__head">総合解説</div>
      <div>${escapeHtml(q.explanation)}</div>
      ${q.reference ? `<div class="explanation__ref">📘 参考: ${escapeHtml(q.reference)}</div>` : ''}
    </div>
  </div>`;
}

/* ---------- 起動 ---------- */
function bindNav() {
  document.querySelectorAll('.topnav__btn').forEach((b) =>
    b.addEventListener('click', () => navigate(b.dataset.route)));
  document.getElementById('navHome').addEventListener('click', () => navigate('home'));
}

async function main() {
  initTheme();
  bindNav();
  try {
    await loadData();
    navigate('home');
  } catch (e) {
    console.error(e);
    appEl.innerHTML = `<section class="card"><h2 class="section-title">読み込みエラー</h2>
      <p>問題データを読み込めませんでした。ローカルで開く場合は <code class="inline">python3 -m http.server</code> 等のWebサーバ経由でアクセスしてください（file:// では動作しません）。</p>
      <p class="note">${escapeHtml(String(e))}</p></section>`;
  }
}

main();

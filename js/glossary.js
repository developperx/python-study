// 用語集：解説文・選択肢理由の中の専門用語をハイライトし、クリックで定義を表示する。
import { escapeHtml } from './ui.js';

let _terms = null;
let _byTerm = null;
let _regex = null;
let _funcs = null;
let _byFunc = null;
let _funcRegex = null;
let _funcGroupNames = null; // グループ番号 -> 元の functions[].match（先頭ドットを含む）
let _loadPromise = null;

function escapeRegExp(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// 関数・メソッドの match 種別ごとに、呼び出し `(` の直前だけを検出する正規表現の断片を作る。
// - ".append" のようにドットで始まる → オブジェクトによらない汎用メソッド（ドット自体はハイライトしない）
// - "re.sub" のようにドットを含む   → モジュール修飾された呼び出しのリテラル完全一致
// - "len" のようにドットを含まない → 組み込み関数・コンストラクタ（メソッド呼び出しとの混同を防ぐ）
function funcPatternSource(match) {
  if (match.startsWith('.')) {
    return `(?<=\\.)${escapeRegExp(match.slice(1))}(?=\\()`;
  }
  if (match.includes('.')) {
    return `\\b${escapeRegExp(match)}(?=\\()`;
  }
  return `(?<!\\.)\\b${escapeRegExp(match)}(?=\\()`;
}

export async function loadGlossary() {
  if (_loadPromise) return _loadPromise;
  _loadPromise = (async () => {
    const res = await fetch('./data/glossary.json', { cache: 'no-cache' });
    if (!res.ok) throw new Error(`fetch failed: glossary.json (${res.status})`);
    const json = await res.json();
    _terms = json.terms;
    _byTerm = new Map(_terms.map((t) => [t.term, t]));
    // 長い用語を先に判定させ、短い用語が長い用語の一部を誤って奪わないようにする
    const sorted = [..._byTerm.keys()].sort((a, b) => b.length - a.length);
    _regex = sorted.length ? new RegExp(sorted.map(escapeRegExp).join('|'), 'g') : null;

    _funcs = json.functions || [];
    _byFunc = new Map(_funcs.map((f) => [f.match, f]));
    // ".append"のようなドット始まりのmatchはハイライト時にドットを含まない文字列になるため、
    // 一致した箇所がどのエントリ由来かは名前付きキャプチャグループで追跡する（マッチ文字列からの逆引きはできない）。
    const sortedFuncs = [..._funcs].sort((a, b) => b.match.length - a.match.length);
    _funcRegex = sortedFuncs.length
      ? new RegExp(sortedFuncs.map((f, i) => `(?<g${i}>${funcPatternSource(f.match)})`).join('|'), 'g')
      : null;
    _funcGroupNames = sortedFuncs.map((f) => f.match);
    return _terms;
  })();
  return _loadPromise;
}

export function glossaryTerms() {
  return _terms || [];
}

// 既にHTMLエスケープ済みのテキストに対して、用語をクリック可能なspanで包んで返す。
export function annotate(escapedText) {
  if (!_regex) return escapedText;
  return escapedText.replace(_regex, (m) => `<span class="gloss" data-term="${m}">${m}</span>`);
}

// 出題コードの中の関数・メソッド呼び出しをクリック可能なspanで包んで返す（HTMLエスケープも行う）。
export function annotateCode(rawCode) {
  const escaped = escapeHtml(rawCode);
  if (!_funcRegex) return escaped;
  return escaped.replace(_funcRegex, (m, ...rest) => {
    const groups = rest[rest.length - 1]; // 名前付きキャプチャグループ（最後の引数）
    const idx = _funcGroupNames.findIndex((_, i) => groups[`g${i}`] !== undefined);
    const match = idx >= 0 ? _funcGroupNames[idx] : m;
    return `<span class="gloss" data-fn="${escapeHtml(match)}">${m}</span>`;
  });
}

// 出題コードのコードブロックHTML（ハイライト適用済み）。
export function codeBlock(code) {
  if (!code) return '';
  return `<pre class="code">${annotateCode(code)}</pre>`;
}

/* ---------- ボトムシートUI ---------- */
function closeSheet() {
  const ov = document.querySelector('.gloss-overlay');
  if (ov) ov.remove();
  document.removeEventListener('keydown', onKeydown);
}

function onKeydown(e) {
  if (e.key === 'Escape') closeSheet();
}

// ボトムシート（オーバーレイ＋カード）を表示する共通処理。
function renderSheet(bodyHtml) {
  closeSheet();
  const ov = document.createElement('div');
  ov.className = 'gloss-overlay';
  ov.innerHTML = `
    <div class="gloss-sheet" role="dialog" aria-modal="true">
      ${bodyHtml}
      <button class="btn btn--block mt" id="glossCloseBtn">閉じる</button>
    </div>`;
  ov.addEventListener('click', (e) => { if (e.target === ov) closeSheet(); });
  document.body.appendChild(ov);
  ov.querySelector('#glossCloseBtn').addEventListener('click', closeSheet);
  document.addEventListener('keydown', onKeydown);
}

export function openGlossarySheet(term) {
  const entry = _byTerm && _byTerm.get(term);
  if (!entry) return;
  renderSheet(`
    <div class="gloss-sheet__term">${escapeHtml(entry.term)}</div>
    <div class="gloss-sheet__def">${escapeHtml(entry.definition)}</div>`);
}

export function openFunctionSheet(match) {
  const entry = _byFunc && _byFunc.get(match);
  if (!entry) return;
  renderSheet(`
    <div class="gloss-sheet__term">${escapeHtml(entry.match.replace(/^\./, ''))}</div>
    <div class="gloss-sheet__sig">${escapeHtml(entry.signature)}</div>
    <div class="gloss-sheet__def">${escapeHtml(entry.definition)}</div>`);
}

// 用語・関数クリックの委譲イベントを1度だけ登録する。
export function bindGlossaryEvents() {
  document.addEventListener('click', (e) => {
    const el = e.target.closest('.gloss');
    if (!el) return;
    if (el.dataset.fn) openFunctionSheet(el.dataset.fn);
    else if (el.dataset.term) openGlossarySheet(el.dataset.term);
  });
}

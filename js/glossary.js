// 用語集：解説文・選択肢理由の中の専門用語をハイライトし、クリックで定義を表示する。
import { escapeHtml } from './ui.js';

let _terms = null;
let _byTerm = null;
let _regex = null;
let _loadPromise = null;

function escapeRegExp(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
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

/* ---------- ボトムシートUI ---------- */
function closeSheet() {
  const ov = document.querySelector('.gloss-overlay');
  if (ov) ov.remove();
  document.removeEventListener('keydown', onKeydown);
}

function onKeydown(e) {
  if (e.key === 'Escape') closeSheet();
}

export function openGlossarySheet(term) {
  const entry = _byTerm && _byTerm.get(term);
  if (!entry) return;
  closeSheet();
  const ov = document.createElement('div');
  ov.className = 'gloss-overlay';
  ov.innerHTML = `
    <div class="gloss-sheet" role="dialog" aria-modal="true">
      <div class="gloss-sheet__term">${escapeHtml(entry.term)}</div>
      <div class="gloss-sheet__def">${escapeHtml(entry.definition)}</div>
      <button class="btn btn--block mt" id="glossCloseBtn">閉じる</button>
    </div>`;
  ov.addEventListener('click', (e) => { if (e.target === ov) closeSheet(); });
  document.body.appendChild(ov);
  ov.querySelector('#glossCloseBtn').addEventListener('click', closeSheet);
  document.addEventListener('keydown', onKeydown);
}

// 用語クリックの委譲イベントを1度だけ登録する。
export function bindGlossaryEvents() {
  document.addEventListener('click', (e) => {
    const el = e.target.closest('.gloss');
    if (el) openGlossarySheet(el.dataset.term);
  });
}

// 純粋なDOM/描画ヘルパー群。
export function h(html) {
  const t = document.createElement('template');
  t.innerHTML = html.trim();
  return t.content.firstElementChild;
}

export function escapeHtml(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function formatTime(sec) {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

export function pct(x) {
  return `${Math.round(x * 100)}%`;
}

// 章番号 -> ラベル「第N章」
export function chLabel(n) {
  return `第${n}章`;
}

// 正答率に応じた色クラス（合格圏=緑）
export function accClass(ratio) {
  if (ratio >= 0.7) return 'pass';
  return '';
}

// コードブロックHTML（コードがある時のみ）
export function codeBlock(code) {
  if (!code) return '';
  return `<pre class="code">${escapeHtml(code)}</pre>`;
}

// 選択肢の記号 A,B,C,D...
export const MARK = (i) => String.fromCharCode(65 + i);

#!/usr/bin/env python3
"""
build_flashcards.py

Parses the CISSP Anki deck markdown files (Domain-*.md) in this directory and
generates a single self-contained HTML study app (flashcards.html) with all
card data embedded as a JSON array. The HTML works offline by double-click
(file://) with no server, network, or external dependencies.

Card format: one card per line `Question :: Answer` (split on the FIRST ` :: ').
Lines starting with `#`, `##`, `>`, `---`, and YAML frontmatter are NOT cards.
`##` lines are SECTION names; the filename gives the DECK and DOMAIN.

Each card is tagged with:
  - deck      : Concepts | Terms | Drill | Glossary   (from filename)
  - domainNum : "1".."8" (real CISSP domain) or "X" (cross-domain)
  - domain    : human label, e.g. "Domain 4" or "Cross-domain"

For the GLOSSARY deck, a `## Domain N ...` section header sets that card's
real domain, so the app can filter glossary cards by domain (e.g. drill only
Domain 4 glossary terms).

Usage:  python3 build_flashcards.py
"""

import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SEPARATOR = " :: "


def deck_and_domain(raw):
    """Map the filename token (Domain-<raw>.md) to (deck, base_domain_num)."""
    if raw in {"1", "2", "3", "4", "5", "6", "7", "8"}:
        return "Concepts", raw
    u = raw.upper()
    if u == "TERMS":
        return "Terms", "X"
    if u == "DRILL":
        return "Drill", "X"
    if u == "GLOSSARY":
        return "Glossary", "X"
    return "Other", "X"


def parse_file(path):
    """Return [card_dicts] for one Domain-*.md file."""
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    base = os.path.basename(path)
    m = re.search(r"Domain-(\w+)\.md$", base)
    raw = m.group(1) if m else "?"
    deck, file_domnum = deck_and_domain(raw)

    cards = []
    section = ""
    cur_domnum = file_domnum
    in_frontmatter = False
    seen_first_line = False

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        # YAML frontmatter (leading '---' on first non-empty line)
        if not seen_first_line and stripped == "---":
            in_frontmatter = True
            seen_first_line = True
            continue
        if stripped:
            seen_first_line = True
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue

        if stripped == "" or stripped.startswith("---"):
            continue
        if stripped.startswith("##"):
            section = stripped.lstrip("#").strip()
            # In the glossary deck, a "Domain N" section assigns the real domain.
            if deck == "Glossary":
                sm = re.match(r"Domain\s+([1-8])\b", section)
                cur_domnum = sm.group(1) if sm else "X"
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith(">"):
            continue

        if SEPARATOR in line:
            idx = line.index(SEPARATOR)
            question = line[:idx].strip()
            answer = line[idx + len(SEPARATOR):].strip()
            if question and answer:
                dn = cur_domnum
                dom_label = ("Domain " + dn) if dn in "12345678" else "Cross-domain"
                cards.append({
                    "domain": dom_label,
                    "domainNum": dn,
                    "deck": deck,
                    "section": section,
                    "question": question,
                    "answer": answer,
                })

    return cards


def main():
    paths = sorted(glob.glob(os.path.join(HERE, "Domain-*.md")))
    all_cards = []
    for p in paths:
        all_cards.extend(parse_file(p))

    data_json = json.dumps(all_cards, ensure_ascii=False, indent=0)
    html = HTML_TEMPLATE.replace("/*__CARD_DATA__*/", data_json)

    out_path = os.path.join(HERE, "flashcards.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)

    print("Wrote", out_path)
    print("Total cards:", len(all_cards))
    by_deck = {}
    by_dom = {}
    for c in all_cards:
        by_deck[c["deck"]] = by_deck.get(c["deck"], 0) + 1
        by_dom[c["domain"]] = by_dom.get(c["domain"], 0) + 1
    print("By deck:")
    for k in sorted(by_deck):
        print("  {}: {}".format(k, by_deck[k]))
    print("By domain:")
    for k in sorted(by_dom):
        print("  {}: {}".format(k, by_dom[k]))


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CISSP Flashcards</title>
<style>
  :root {
    --bg: #0f1115;
    --panel: #1a1e26;
    --panel2: #222834;
    --border: #2c3340;
    --text: #e7ecf3;
    --muted: #9aa6b5;
    --accent: #4f9dff;
    --good: #34c77b;
    --bad: #ff6b6b;
    --shadow: 0 10px 30px rgba(0,0,0,0.45);
  }
  * { box-sizing: border-box; }
  html, body { height: 100%; }
  body {
    margin: 0;
    background: radial-gradient(1200px 600px at 50% -10%, #182030 0%, var(--bg) 60%);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  header {
    padding: 14px 18px;
    border-bottom: 1px solid var(--border);
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    justify-content: space-between;
    background: rgba(15,17,21,0.7);
    backdrop-filter: blur(6px);
  }
  h1 { font-size: 18px; margin: 0; letter-spacing: 0.3px; }
  h1 span { color: var(--accent); }
  .controls { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
  select, button {
    font: inherit;
    color: var(--text);
    background: var(--panel2);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 8px 12px;
    cursor: pointer;
    transition: background .15s, border-color .15s, transform .05s;
  }
  select { cursor: pointer; }
  button:hover, select:hover { border-color: var(--accent); }
  button:active { transform: translateY(1px); }
  button.primary { background: var(--accent); border-color: var(--accent); color: #07101e; font-weight: 600; }
  button.good { background: var(--good); border-color: var(--good); color: #062014; font-weight: 600; }
  button.bad { background: var(--bad); border-color: var(--bad); color: #2a0606; font-weight: 600; }
  label.lbl { font-size: 12px; color: var(--muted); margin-right: 4px; }

  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 24px 18px 8px;
    gap: 16px;
    width: 100%;
  }

  .stats {
    display: flex;
    flex-wrap: wrap;
    gap: 10px 18px;
    font-size: 13px;
    color: var(--muted);
    justify-content: center;
  }
  .stats b { color: var(--text); }
  .pill { background: var(--panel); border: 1px solid var(--border); padding: 4px 10px; border-radius: 20px; }
  .pill.good b { color: var(--good); }
  .pill.bad b { color: var(--bad); }

  .card-wrap { width: min(760px, 96vw); perspective: 1600px; }
  .card {
    position: relative;
    width: 100%;
    min-height: 320px;
    cursor: pointer;
    transform-style: preserve-3d;
    transition: transform 0.5s cubic-bezier(.2,.7,.2,1);
  }
  .card.flipped { transform: rotateY(180deg); }
  .face {
    position: absolute;
    inset: 0;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    background: linear-gradient(180deg, var(--panel2), var(--panel));
    border: 1px solid var(--border);
    border-radius: 18px;
    box-shadow: var(--shadow);
    padding: 26px 28px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .face.back { transform: rotateY(180deg); }
  .meta {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 14px;
    flex: 0 0 auto;
  }
  .tag {
    font-size: 11px;
    letter-spacing: .4px;
    text-transform: uppercase;
    color: var(--muted);
    background: rgba(79,157,255,0.10);
    border: 1px solid var(--border);
    padding: 3px 9px;
    border-radius: 20px;
  }
  .tag.kind { color: var(--accent); }
  .content {
    flex: 1 1 auto;
    overflow-y: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .content .text {
    font-size: clamp(18px, 3.2vw, 26px);
    line-height: 1.45;
    font-weight: 500;
    white-space: pre-wrap;
    word-break: break-word;
  }
  .face.back .content .text { font-size: clamp(16px, 2.7vw, 22px); font-weight: 450; text-align: left; }
  .hint { flex: 0 0 auto; text-align: center; color: var(--muted); font-size: 12px; margin-top: 12px; }

  .nav {
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
  }
  .grade { display: flex; gap: 10px; }
  .position { font-variant-numeric: tabular-nums; color: var(--muted); min-width: 90px; text-align: center; }

  .progress-bar {
    width: min(760px, 96vw);
    height: 6px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
  }
  .progress-bar > div { height: 100%; background: var(--good); width: 0%; transition: width .3s; }

  footer {
    padding: 10px 18px 18px;
    text-align: center;
    color: var(--muted);
    font-size: 12px;
  }
  kbd {
    background: var(--panel2);
    border: 1px solid var(--border);
    border-bottom-width: 2px;
    border-radius: 5px;
    padding: 1px 6px;
    font-family: ui-monospace, Menlo, Consolas, monospace;
    font-size: 11px;
    color: var(--text);
  }
  .done {
    text-align: center;
    padding: 40px 20px;
  }
  .done h2 { color: var(--good); margin: 0 0 10px; }
  @media (max-width: 560px) {
    .position { min-width: 70px; }
    h1 { font-size: 16px; }
    .face { padding: 20px; }
  }
</style>
</head>
<body>
<header>
  <h1>CISSP <span>Flashcards</span></h1>
  <div class="controls">
    <span><label class="lbl">Domain</label>
      <select id="domainSel"></select></span>
    <span><label class="lbl">Deck</label>
      <select id="deckSel"></select></span>
    <button id="shuffleBtn" title="Shuffle (s)">🔀 Shuffle</button>
    <button id="missedBtn" title="Study only cards you've flagged 'Review' (m)">📕 Missed only</button>
    <button id="exportBtn" title="Export missed cards as a cram sheet (.md)">⬇ Export cram</button>
    <button id="resetBtn" title="Restart this deck (session)">↺ Reset</button>
    <button id="clearBtn" title="Clear ALL saved progress">🗑 Clear</button>
  </div>
</header>

<main>
  <div class="stats" id="stats"></div>
  <div class="progress-bar"><div id="progressFill"></div></div>

  <div class="card-wrap" id="cardWrap">
    <div class="card" id="card">
      <div class="face front">
        <div class="meta" id="frontMeta"></div>
        <div class="content"><div class="text" id="frontText"></div></div>
        <div class="hint">Click card or press <kbd>Space</kbd> to flip</div>
      </div>
      <div class="face back">
        <div class="meta" id="backMeta"></div>
        <div class="content"><div class="text" id="backText"></div></div>
        <div class="hint"><kbd>k</kbd> Got it &nbsp;·&nbsp; <kbd>j</kbd> Review again</div>
      </div>
    </div>
  </div>

  <div class="nav">
    <button id="prevBtn" title="Previous (←)">← Prev</button>
    <span class="position" id="position">0 / 0</span>
    <button id="nextBtn" title="Next (→)">Next →</button>
    <span class="grade">
      <button id="goodBtn" class="good" title="Got it (k)">✓ Got it</button>
      <button id="badBtn" class="bad" title="Review again (j)">✗ Review</button>
    </span>
  </div>
</main>

<footer>
  Shortcuts: <kbd>Space</kbd> flip · <kbd>←</kbd>/<kbd>→</kbd> nav ·
  <kbd>k</kbd> got it · <kbd>j</kbd> review · <kbd>s</kbd> shuffle · <kbd>m</kbd> missed-only
  &nbsp;|&nbsp; Progress saves automatically · "Export cram" downloads your missed cards
  &nbsp;|&nbsp; <span id="deckInfo"></span>
</footer>

<script>
const CARDS = /*__CARD_DATA__*/;

// ---------- persistent progress (localStorage) ----------
const LS_KEY = "cissp_fc_progress_v1";
function loadProgress(){ try { return JSON.parse(localStorage.getItem(LS_KEY) || "{}"); } catch(e){ return {}; } }
function saveProgress(){ try { localStorage.setItem(LS_KEY, JSON.stringify(PROGRESS)); } catch(e){} }
let PROGRESS = loadProgress();
function cardKey(c){ return c.question; }                 // stable across regenerations
function cardStatus(c){ const r = PROGRESS[cardKey(c)]; return r ? r.s : null; } // 'k' | 'u' | null
function cardMiss(c){ const r = PROGRESS[cardKey(c)]; return r ? (r.m||0) : 0; }
function markCard(c, known){
  const k = cardKey(c);
  const r = PROGRESS[k] || {s:null, m:0, h:0};
  if(known){ r.s='k'; r.h=(r.h||0)+1; } else { r.s='u'; r.m=(r.m||0)+1; }
  PROGRESS[k]=r; saveProgress();
}
function persistStats(deck){
  let k=0,u=0,n=0;
  deck.forEach(c=>{ const s=cardStatus(c); if(s==='k')k++; else if(s==='u')u++; else n++; });
  return {k,u,n};
}

// ---------- helpers ----------
function esc(s){
  return String(s)
    .replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")
    .replace(/"/g,"&quot;").replace(/'/g,"&#39;");
}
function shuffleArr(a){
  for(let i=a.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  return a;
}

// ---------- state ----------
const state = {
  domain: "All",    // matches card.domain ("Domain 4" / "Cross-domain")
  deck: "All",      // matches card.deck   (Concepts/Terms/Drill/Glossary)
  shuffled: false,
  missedOnly: false,
  queue: [],
  pos: 0,
  flipped: false,
  got: 0,
  reviewed: 0,
  total: 0,
  reviewQueued: 0,
};

const domainSel  = document.getElementById("domainSel");
const deckSel    = document.getElementById("deckSel");
const cardEl     = document.getElementById("card");

// ---------- build filter options ----------
function uniqueDomains(){
  // unique by domainNum, sorted 1..8 then Cross-domain last
  const map = {};
  CARDS.forEach(c=>{ map[c.domainNum]= c.domain; });
  const keys = Object.keys(map);
  keys.sort((a,b)=>{
    const na = (a==="X") ? 99 : parseInt(a);
    const nb = (b==="X") ? 99 : parseInt(b);
    return na-nb;
  });
  return keys.map(k=>({num:k, label:map[k]}));
}
function decksFor(domainNum){
  const seen=[];
  CARDS.forEach(c=>{
    if(domainNum==="All" || c.domainNum===domainNum){
      if(c.deck && !seen.includes(c.deck)) seen.push(c.deck);
    }
  });
  // stable order
  const order = ["Concepts","Terms","Drill","Glossary","Other"];
  seen.sort((a,b)=> order.indexOf(a)-order.indexOf(b));
  return seen;
}

function fillDomainSel(){
  domainSel.innerHTML="";
  const optAll=document.createElement("option");
  optAll.value="All"; optAll.textContent="All domains";
  domainSel.appendChild(optAll);
  uniqueDomains().forEach(d=>{
    const o=document.createElement("option");
    o.value=d.num; o.textContent=d.label;
    domainSel.appendChild(o);
  });
}
function fillDeckSel(){
  deckSel.innerHTML="";
  const optAll=document.createElement("option");
  optAll.value="All"; optAll.textContent="All decks";
  deckSel.appendChild(optAll);
  decksFor(state.domain).forEach(s=>{
    const o=document.createElement("option");
    o.value=s; o.textContent=s;
    deckSel.appendChild(o);
  });
}

// ---------- deck building ----------
function scopeDeck(){ // domain/deck filter only (ignores missedOnly) — for stats
  return CARDS.filter(c=>{
    if(state.domain!=="All" && c.domainNum!==state.domain) return false;
    if(state.deck!=="All" && c.deck!==state.deck) return false;
    return true;
  });
}
function baseDeck(){
  return scopeDeck().filter(c=>{
    if(state.missedOnly && cardStatus(c)!=='u') return false;
    return true;
  });
}
function rebuildDeck(){
  let deck = baseDeck().slice();
  if(state.shuffled) shuffleArr(deck);
  state.queue = deck;
  state.total = deck.length;
  state.pos = 0;
  state.flipped = false;
  state.got = 0;
  state.reviewed = 0;
  state.reviewQueued = 0;
  render();
}

// ---------- rendering ----------
function render(){
  const q = state.queue;
  const done = state.pos >= q.length;
  const card = done ? null : q[state.pos];

  cardEl.classList.toggle("flipped", state.flipped && !done);

  const frontMeta = document.getElementById("frontMeta");
  const backMeta  = document.getElementById("backMeta");
  const frontText = document.getElementById("frontText");
  const backText  = document.getElementById("backText");

  if(done){
    frontMeta.innerHTML="";
    backMeta.innerHTML="";
    frontText.innerHTML = q.length===0
      ? "<span style='color:var(--muted)'>No cards match this filter.</span>"
      : "<div class='done'><h2>✓ Deck complete!</h2>"
        + "<div style='color:var(--muted)'>Got it: <b style='color:var(--good)'>"+state.got+"</b>"
        + " &nbsp;·&nbsp; Review presses: <b style='color:var(--bad)'>"+state.reviewed+"</b></div>"
        + "<div style='margin-top:14px;color:var(--muted)'>Press Reset to study again.</div></div>";
    backText.innerHTML="";
  } else {
    const tags = "<span class='tag kind'>"+esc(card.domain)+"</span>"
               + "<span class='tag'>"+esc(card.deck)+"</span>"
               + (card.section ? "<span class='tag'>"+esc(card.section)+"</span>" : "");
    frontMeta.innerHTML = tags + "<span class='tag'>Question</span>";
    backMeta.innerHTML  = tags + "<span class='tag'>Answer</span>";
    frontText.innerHTML = esc(card.question);
    backText.innerHTML  = esc(card.answer);
  }

  const posLabel = q.length===0 ? "0 / 0"
    : (Math.min(state.pos+1, q.length)) + " / " + q.length;
  document.getElementById("position").textContent = posLabel;

  const remaining = Math.max(q.length - state.pos, 0);
  const ps = persistStats(scopeDeck());
  document.getElementById("stats").innerHTML =
      "<span class='pill'>Remaining <b>"+remaining+"</b></span>"
    + "<span class='pill good'>Got it <b>"+state.got+"</b></span>"
    + "<span class='pill bad'>Re-queued <b>"+state.reviewQueued+"</b></span>"
    + "<span class='pill'>Deck size <b>"+state.total+"</b></span>"
    + "<span class='pill'>Saved: known <b style='color:var(--good)'>"+ps.k+"</b> · flagged <b style='color:var(--bad)'>"+ps.u+"</b> · unseen <b>"+ps.n+"</b></span>";

  const pct = q.length===0 ? 0 : Math.round((state.pos / q.length) * 100);
  document.getElementById("progressFill").style.width = pct + "%";

  const canGrade = !done && state.flipped;
  document.getElementById("goodBtn").disabled = !canGrade;
  document.getElementById("badBtn").disabled  = !canGrade;
  document.getElementById("goodBtn").style.opacity = canGrade ? 1 : .45;
  document.getElementById("badBtn").style.opacity  = canGrade ? 1 : .45;

  document.getElementById("deckInfo").textContent =
    "Total cards loaded: " + CARDS.length;
}

// ---------- actions ----------
function flip(){
  if(state.pos >= state.queue.length) return;
  state.flipped = !state.flipped;
  render();
}
function next(){
  if(state.pos < state.queue.length){ state.pos++; state.flipped=false; render(); }
}
function prev(){
  if(state.pos > 0){ state.pos--; state.flipped=false; render(); }
}
function gradeGood(){
  if(state.pos >= state.queue.length || !state.flipped) return;
  markCard(state.queue[state.pos], true);
  state.got++;
  state.pos++;
  state.flipped=false;
  render();
}
function gradeBad(){
  if(state.pos >= state.queue.length || !state.flipped) return;
  state.reviewed++;
  const card = state.queue[state.pos];
  markCard(card, false);
  state.queue.push(card);
  state.reviewQueued++;
  state.pos++;
  state.flipped=false;
  render();
}

// ---------- missed-only / export / clear ----------
function toggleMissed(){
  state.missedOnly = !state.missedOnly;
  const btn = document.getElementById("missedBtn");
  btn.classList.toggle("primary", state.missedOnly);
  btn.textContent = state.missedOnly ? "📕 Missed only ✓" : "📕 Missed only";
  rebuildDeck();
}
function exportMissed(){
  const missed = CARDS.filter(c=>cardStatus(c)==='u');
  if(missed.length===0){ alert("No cards flagged 'Review' yet — study some first, hitting ✗ Review on ones you don't know."); return; }
  missed.sort((a,b)=>{
    const na=(a.domainNum==="X")?99:parseInt(a.domainNum);
    const nb=(b.domainNum==="X")?99:parseInt(b.domainNum);
    if(na!==nb) return na-nb;
    return cardMiss(b)-cardMiss(a);
  });
  let md = "# My Cram Sheet — Missed Cards ("+missed.length+")\n\n";
  md += "> Auto-generated from the flashcard app: the cards you flagged 'Review'. Sorted by domain, then most-missed first.\n\n";
  let curDom="";
  missed.forEach(c=>{
    if(c.domain!==curDom){ curDom=c.domain; md += "\n## "+curDom+"\n\n"; }
    md += "- **"+c.question+"** — "+c.answer+"  _(missed "+cardMiss(c)+"x)_\n";
  });
  const blob = new Blob([md], {type:"text/markdown"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = "my-cram-sheet.md";
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
}
function clearProgress(){
  if(!confirm("Clear ALL saved progress (known/flagged status for every card)? This cannot be undone.")) return;
  PROGRESS = {}; saveProgress();
  state.missedOnly = false;
  const btn = document.getElementById("missedBtn");
  btn.classList.remove("primary"); btn.textContent = "📕 Missed only";
  rebuildDeck();
}

// ---------- events ----------
cardEl.addEventListener("click", flip);
document.getElementById("nextBtn").addEventListener("click", next);
document.getElementById("prevBtn").addEventListener("click", prev);
document.getElementById("goodBtn").addEventListener("click", gradeGood);
document.getElementById("badBtn").addEventListener("click", gradeBad);
document.getElementById("resetBtn").addEventListener("click", rebuildDeck);
document.getElementById("missedBtn").addEventListener("click", toggleMissed);
document.getElementById("exportBtn").addEventListener("click", exportMissed);
document.getElementById("clearBtn").addEventListener("click", clearProgress);
document.getElementById("shuffleBtn").addEventListener("click", ()=>{
  state.shuffled = true;
  rebuildDeck();
});
domainSel.addEventListener("change", ()=>{
  state.domain = domainSel.value;
  state.deck = "All";
  fillDeckSel();
  rebuildDeck();
});
deckSel.addEventListener("change", ()=>{
  state.deck = deckSel.value;
  rebuildDeck();
});

document.addEventListener("keydown", (e)=>{
  if(e.target.tagName==="SELECT") return;
  switch(e.key){
    case " ": case "Enter": e.preventDefault(); flip(); break;
    case "ArrowRight": e.preventDefault(); next(); break;
    case "ArrowLeft": e.preventDefault(); prev(); break;
    case "k": case "K": gradeGood(); break;
    case "j": case "J": gradeBad(); break;
    case "s": case "S": state.shuffled=true; rebuildDeck(); break;
    case "m": case "M": toggleMissed(); break;
  }
});

// ---------- init ----------
fillDomainSel();
fillDeckSel();
rebuildDeck();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()

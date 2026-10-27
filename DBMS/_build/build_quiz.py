#!/usr/bin/env python3
"""Build DBMS/20-DBMS-Quiz.html: an exam-style mock test over the question bank (quiz_bank.py).

The setup screen picks a chapter (or "All chapters — mixed"), a difficulty level and a number of questions.
Each attempt draws its own random set and shuffles the options, then runs like an online bank exam:
timer, question palette, Save & Next / Mark for Review / Clear Response, submit summary, then a scorecard
with chapter-wise and level-wise breakdowns and solutions that link back to the notes.
The exam look (CSS) is shared with the Current Affairs mock tests (Current-Affairs/_build/quiz.py).
Run:  python3 -I DBMS/_build/build_quiz.py
"""
import glob, json, os, re, sys

B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); R = os.path.dirname(D)
sys.path.insert(0, B); sys.path.insert(0, os.path.join(R, 'Current-Affairs', '_build'))
from quiz_bank import BANK
from quiz import CSS as EXAM_CSS

OUT = '20-DBMS-Quiz'
SECONDS_PER_Q = 45          # IBPS SO Professional Knowledge: 60 questions in 45 minutes
PLUS, MINUS = 1, 0.25

chapters = []
for line in open(os.path.join(B, 'outline.txt'), encoding='utf-8'):
    m = re.match(r'^## (\d+)\. (.*)', line.strip())
    if m:
        n = int(m.group(1)); f = glob.glob(os.path.join(D, f'{n:02d}-*.html'))
        chapters.append({'n': n, 'title': m.group(2), 'file': os.path.basename(f[0]) if f else '',
                         'count': len(BANK.get(n, []))})
bank = {str(n): [{k: q[k] for k in ('sec', 'lv', 'k', 'q', 'o', 'a', 'fix', 'e')} for q in qs] for n, qs in BANK.items()}
total = sum(c['count'] for c in chapters)
data = json.dumps({'chapters': chapters, 'bank': bank, 'spq': SECONDS_PER_Q, 'plus': PLUS, 'minus': MINUS},
                  ensure_ascii=False).replace('</', '<\\/')

CSS = '''
.qtext,.sol p{white-space:pre-line}
.chip{display:inline-block;font-size:12px;border:1px solid var(--line);border-radius:999px;padding:1px 9px;margin:0 6px 4px 0;color:var(--muted);background:var(--surface-2)}
.chip.E{color:var(--ok)} .chip.M{color:var(--warn)} .chip.H{color:var(--bad)}
.setup{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:14px 0 6px}
.setup label{display:flex;flex-direction:column;gap:5px;font-size:13.5px;font-weight:600}
.setup select{font:15px var(--body);padding:8px 10px;border:1px solid var(--line);border-radius:5px;background:var(--surface);color:var(--ink)}
.avail{font-size:14px;margin:8px 0 0;color:var(--muted)}
.avail b{color:var(--accent)}
.bd{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-top:6px}
.bd table td:not(:first-child),.bd table th:not(:first-child){text-align:center}
.sol .rv{font-size:13px;margin-top:6px}
.hist li{margin:2px 0}
'''

JS = r'''
(function(){
  var C = DATA.chapters, BANK = DATA.bank, KEY = 'dbms-quiz', L = 'ABCDE';
  var LV = { E: 'Easy', M: 'Medium', H: 'Hard' };
  var root = document.documentElement, $ = function(id){ return document.getElementById(id); };
  var store = {
    get: function(k){ try{ return JSON.parse(localStorage.getItem(k)); }catch(e){ return null; } },
    set: function(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)); }catch(e){} },
    del: function(k){ try{ localStorage.removeItem(k); }catch(e){} }
  };
  try{ var t = localStorage.getItem('notes-theme'); if (t) root.setAttribute('data-theme', t); }catch(e){}
  $('themer').onclick = function(){
    var cur = root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    var nxt = cur === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', nxt);
    try{ localStorage.setItem('notes-theme', nxt); }catch(e){}
  };
  function chap(n){ for (var i = 0; i < C.length; i++) if (C[i].n == n) return C[i]; }
  function shuffle(a){ for (var i = a.length - 1; i > 0; i--){ var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  var LAST = /^(all of the above|none of the above|none of these|both .+ and .+|neither .+)$/i;

  var S = null, Q = [], N = 0, tick = null;   // S = attempt in progress; Q = its questions, resolved
  function show(id){ ['ins', 'exam', 'res'].forEach(function(x){ $(x).hidden = x !== id; }); $('timer').hidden = id !== 'exam'; $('palbtn').hidden = id !== 'exam'; window.scrollTo(0, 0); }
  function save(){ if (S) store.set(KEY + ':run', S); }
  function fmt(s){ s = Math.max(0, Math.round(s)); var m = Math.floor(s / 60); return (m < 10 ? '0' : '') + m + ':' + ('0' + s % 60).slice(-2); }
  function resolve(items){   // attempt items {c, i, p} → questions with options in the attempt's order
    return items.map(function(it){
      var q = BANK[it.c][it.i];
      return { c: it.c, sec: q.sec, lv: q.lv, k: q.k, q: q.q, e: q.e,
               o: it.p.map(function(j){ return q.o[j]; }), a: it.p.indexOf(q.a) };
    });
  }
  function label(sel){ return sel.ch === 'all' ? 'All chapters (mixed)' : 'Ch ' + sel.ch + ': ' + chap(sel.ch).title; }

  /* ---------- setup ---------- */
  var ch = $('ch'), lv = $('lv'), cnt = $('cnt');
  ch.innerHTML = '<option value="all">All chapters — mixed (' + C.reduce(function(s, c){ return s + c.count; }, 0) + ' questions)</option>' +
    C.map(function(c){ return '<option value="' + c.n + '"' + (c.count ? '' : ' disabled') + '>Ch ' + c.n + ': ' + c.title +
      (c.count ? ' (' + c.count + ')' : ' — coming soon') + '</option>'; }).join('');
  function pool(){
    var chs = ch.value === 'all' ? C.filter(function(c){ return c.count; }).map(function(c){ return String(c.n); }) : [ch.value];
    var by = {};
    chs.forEach(function(c){ by[c] = []; BANK[c].forEach(function(q, i){ if (lv.value === 'all' || q.lv === lv.value) by[c].push(i); }); });
    return by;
  }
  function avail(){ var by = pool(), n = 0; for (var c in by) n += by[c].length; return n; }
  function want(){ var a = avail(); return cnt.value === 'all' ? a : Math.min(+cnt.value, a); }
  function refresh(){
    var n = want();
    $('avail').innerHTML = n ? '<b>' + n + '</b> questions · <b>' + Math.ceil(n * DATA.spq / 60) + '</b> minutes · maximum marks <b>' + n * DATA.plus + '</b>'
      : 'No questions match this choice yet. Pick another level or chapter.';
    $('begin').disabled = !$('agree').checked || !n;
  }
  [ch, lv, cnt].forEach(function(s){ s.onchange = function(){ store.set(KEY + ':sel', { ch: ch.value, lv: lv.value, cnt: cnt.value }); refresh(); }; });
  $('agree').onchange = refresh;
  var sel0 = store.get(KEY + ':sel');
  if (sel0){ ch.value = sel0.ch; lv.value = sel0.lv; cnt.value = sel0.cnt; if (ch.selectedIndex < 0) ch.value = 'all'; }

  function initIns(){
    var run = store.get(KEY + ':run'), hist = store.get(KEY + ':hist') || [];
    $('resume').hidden = !run;
    if (run) $('resume').textContent = 'Resume attempt (' + label(run.sel) + ')';
    $('hist').innerHTML = hist.length ? '<b>Previous attempts</b><ul>' + hist.slice(-6).reverse().map(function(h){
      return '<li><b>' + h.score + '</b> / ' + h.n + ' — ' + h.label + (h.lv !== 'all' ? ' · ' + LV[h.lv] : '') + ' <span>(' + h.date + ')</span></li>'; }).join('') + '</ul>' : '';
    $('lastres').hidden = !store.get(KEY + ':last');
    refresh(); show('ins');
  }
  $('begin').onclick = function(){
    var by = pool(), n = want(), picked = [], c;
    for (c in by) shuffle(by[c]);
    var keys = shuffle(Object.keys(by));
    while (picked.length < n){   // round-robin across chapters so a mixed test covers every chapter evenly
      keys.forEach(function(c){ if (picked.length < n && by[c].length) picked.push({ c: c, i: by[c].pop() }); });
    }
    shuffle(picked).forEach(function(it){
      var q = BANK[it.c][it.i], idx = q.o.map(function(_, j){ return j; });
      if (!q.fix){
        var end = idx.filter(function(j){ return LAST.test(q.o[j]); });
        it.p = shuffle(idx.filter(function(j){ return end.indexOf(j) < 0; })).concat(end);
      } else it.p = idx;
    });
    var secs = n * DATA.spq;
    S = { sel: { ch: ch.value, lv: lv.value }, items: picked, secs: secs, i: 0, ans: [], st: [], sel_: null,
          end: Date.now() + secs * 1000, start: Date.now() };
    for (var k = 0; k < n; k++){ S.ans.push(null); S.st.push('nv'); }
    startExam();
  };
  $('resume').onclick = function(){ S = store.get(KEY + ':run'); startExam(); };

  /* ---------- exam ---------- */
  function startExam(){
    Q = resolve(S.items); N = Q.length;
    $('xsub').textContent = label(S.sel) + (S.sel.lv !== 'all' ? ' · ' + LV[S.sel.lv] : '') + ' · ' + N + ' questions · ' + Math.ceil(S.secs / 60) + ' min · +' + DATA.plus + ' / −' + DATA.minus;
    buildPalette(); go(S.i, true); show('exam');
    clearInterval(tick); tick = setInterval(clock, 1000); clock();
  }
  function clock(){
    var left = (S.end - Date.now()) / 1000;
    $('timer').textContent = 'Time Left ' + fmt(left);
    $('timer').classList.toggle('low', left <= 120);
    if (left <= 0){ clearInterval(tick); finish(true); }
  }
  function go(i, keepSel){
    S.i = (i + N) % N;
    if (S.st[S.i] === 'nv') S.st[S.i] = 'na';
    if (!keepSel || S.sel_ === undefined) S.sel_ = S.ans[S.i];
    var q = Q[S.i];
    $('qno').textContent = 'Question No. ' + (S.i + 1);
    $('qsec').innerHTML = '';
    [['Ch ' + q.c + ': ' + chap(q.c).title, ''], [LV[q.lv], q.lv], [q.k, '']].forEach(function(x){
      var s = document.createElement('span'); s.className = 'chip ' + x[1]; s.textContent = x[0]; $('qsec').appendChild(s); });
    $('qtext').textContent = q.q;
    var ul = $('opts'); ul.innerHTML = '';
    q.o.forEach(function(o, k){
      var li = document.createElement('li'), lab = document.createElement('label');
      lab.innerHTML = '<input type="radio" name="opt"><span class="l">' + L[k] + '.</span><span></span>';
      lab.lastChild.textContent = o;
      var inp = lab.firstChild; inp.checked = S.sel_ === k; lab.classList.toggle('on', S.sel_ === k);
      inp.onchange = function(){ S.sel_ = k; mark(); save(); };
      li.appendChild(lab); ul.appendChild(li);
    });
    paint(); save();
    document.body.classList.remove('palopen');
  }
  function mark(){ [].forEach.call($('opts').querySelectorAll('label'), function(l, k){ l.classList.toggle('on', S.sel_ === k); l.firstChild.checked = S.sel_ === k; }); }
  function buildPalette(){
    var g = $('grid'); g.innerHTML = '';
    for (var k = 0; k < N; k++) (function(k){
      var b = document.createElement('button'); b.type = 'button'; b.className = 'st'; b.textContent = k + 1;
      b.onclick = function(){ go(k); };   // unsaved choice is discarded, as in the real exam
      g.appendChild(b);
    })(k);
  }
  function counts(){ var c = { a: 0, na: 0, nv: 0, m: 0, am: 0 }; S.st.forEach(function(s){ c[s]++; }); return c; }
  function paint(){
    [].forEach.call($('grid').children, function(b, k){ b.className = 'st ' + S.st[k] + (k === S.i ? ' cur' : ''); });
    var c = counts();
    ['a', 'na', 'nv', 'm', 'am'].forEach(function(s){ $('c-' + s).textContent = c[s]; });
  }
  function next(){ go(S.i + 1); }
  $('savenext').onclick = function(){ S.ans[S.i] = S.sel_; S.st[S.i] = S.sel_ == null ? 'na' : 'a'; next(); };
  $('marknext').onclick = function(){ S.ans[S.i] = S.sel_; S.st[S.i] = S.sel_ == null ? 'm' : 'am'; next(); };
  $('clear').onclick = function(){
    S.sel_ = null; S.ans[S.i] = null;
    S.st[S.i] = (S.st[S.i] === 'm' || S.st[S.i] === 'am') ? 'm' : 'na';
    mark(); paint(); save();
  };
  $('prev').onclick = function(){ go(S.i - 1); };
  $('palbtn').onclick = function(){ document.body.classList.toggle('palopen'); };
  $('palx').onclick = function(){ document.body.classList.remove('palopen'); };
  document.addEventListener('keydown', function(e){
    if ($('exam').hidden || !$('confirm').hidden || e.ctrlKey || e.metaKey || e.altKey) return;
    var k = L.indexOf(e.key.toUpperCase());
    if (k >= 0 && k < Q[S.i].o.length){ S.sel_ = k; mark(); save(); }
  });

  /* ---------- submit ---------- */
  $('submit').onclick = function(){
    var c = counts();
    $('sum').innerHTML = '<tr><th>Total questions</th><td>' + N + '</td></tr>' +
      '<tr><th>Answered</th><td>' + c.a + '</td></tr>' +
      '<tr><th>Answered &amp; marked for review <small>(will be evaluated)</small></th><td>' + c.am + '</td></tr>' +
      '<tr><th>Marked for review (no answer)</th><td>' + c.m + '</td></tr>' +
      '<tr><th>Not answered</th><td>' + c.na + '</td></tr>' +
      '<tr><th>Not visited</th><td>' + c.nv + '</td></tr>';
    $('confirm').hidden = false;
  };
  $('no').onclick = function(){ $('confirm').hidden = true; };
  $('yes').onclick = function(){ $('confirm').hidden = true; finish(false); };

  function finish(timeUp){
    clearInterval(tick);
    var r = { items: S.items, sel: S.sel, secs: S.secs, ans: S.ans.slice(), timeUp: timeUp,
              used: Math.min(S.secs, Math.round((Math.min(Date.now(), S.end) - S.start) / 1000)) };
    var right = 0, wrong = 0;
    Q.forEach(function(q, k){ if (r.ans[k] != null){ if (r.ans[k] === q.a) right++; else wrong++; } });
    var score = Math.round((right * DATA.plus - wrong * DATA.minus) * 100) / 100;
    var hist = store.get(KEY + ':hist') || [];
    hist.push({ score: score, n: N, label: label(S.sel), lv: S.sel.lv, date: new Date().toLocaleDateString(undefined, { day: 'numeric', month: 'short' }) });
    store.set(KEY + ':hist', hist.slice(-30)); store.set(KEY + ':last', r); store.del(KEY + ':run');
    S = null; result(r);
  }

  /* ---------- result ---------- */
  function tally(rows){
    var t = { n: 0, c: 0, w: 0, s: 0 };
    rows.forEach(function(x){ t.n++; if (x.mine == null) t.s++; else if (x.mine === x.q.a) t.c++; else t.w++; });
    t.score = Math.round((t.c * DATA.plus - t.w * DATA.minus) * 100) / 100; return t;
  }
  function table(head, groups){
    return '<table><tr><th>' + head + '</th><th>Qs</th><th>✓</th><th>✗</th><th>–</th><th>Score</th></tr>' +
      groups.map(function(g){ var t = g[1]; return '<tr><td>' + g[0] + '</td><td>' + t.n + '</td><td>' + t.c + '</td><td>' + t.w + '</td><td>' + t.s + '</td><td><b>' + t.score + '</b></td></tr>'; }).join('') + '</table>';
  }
  function result(r){
    var q = resolve(r.items), n = q.length, rows = q.map(function(x, k){ return { q: x, mine: r.ans[k] }; }), all = tally(rows);
    var att = all.c + all.w, acc = att ? Math.round(all.c / att * 100) : 0, pct = Math.round(Math.max(0, all.score) / n * 100);
    $('timeup').hidden = !r.timeUp;
    $('rsub').textContent = label(r.sel) + (r.sel.lv !== 'all' ? ' · ' + LV[r.sel.lv] : '');
    $('score').innerHTML =
      '<div><b>' + all.score + ' / ' + n + '</b><span>Score (+' + DATA.plus + ' / −' + DATA.minus + ')</span></div>' +
      '<div class="c"><b>' + all.c + '</b><span>Correct</span></div>' +
      '<div class="w"><b>' + all.w + '</b><span>Wrong (−' + (all.w * DATA.minus) + ')</span></div>' +
      '<div><b>' + all.s + '</b><span>Not attempted</span></div>' +
      '<div><b>' + acc + '%</b><span>Accuracy</span></div>' +
      '<div><b>' + fmt(r.used) + '</b><span>Time taken of ' + fmt(r.secs) + '</span></div>';
    $('verdict').textContent = pct >= 80 ? 'Excellent. Move to a harder level or the mixed test, and come back in a week.'
      : pct >= 60 ? 'Good. Revise the subtopics behind your wrong answers (links below), then retake.'
      : 'Needs revision. Re-read the chapter notes, especially the exam traps, then retake this test.';
    var chs = [], lvs = [];
    C.forEach(function(c){ var g = rows.filter(function(x){ return x.q.c == c.n; }); if (g.length) chs.push(['Ch ' + c.n + ': ' + c.title, tally(g)]); });
    ['E', 'M', 'H'].forEach(function(l){ var g = rows.filter(function(x){ return x.q.lv === l; }); if (g.length) lvs.push([LV[l], tally(g)]); });
    $('bd').innerHTML = (chs.length > 1 ? table('Chapter', chs) : '') + table('Level', lvs);
    var box = $('sols'); box.innerHTML = '';
    rows.forEach(function(x, k){
      var cls = x.mine == null ? 's' : x.mine === x.q.a ? 'c' : 'w', c = chap(x.q.c), sec = x.q.sec.split('.')[1];
      var d = document.createElement('div'); d.className = 'sol ' + cls; d.dataset.k = cls;
      d.innerHTML = '<div class="qn">Q' + (k + 1) + '<em>' + (cls === 'c' ? 'Correct +' + DATA.plus : cls === 'w' ? 'Wrong −' + DATA.minus : 'Not attempted') + '</em></div>' +
        '<div><span class="chip">Ch ' + c.n + '</span><span class="chip ' + x.q.lv + '">' + LV[x.q.lv] + '</span><span class="chip">' + html(x.q.k) + '</span></div>' +
        '<p></p><ol></ol><div class="ex"><b>Explanation:</b> <span></span></div>' +
        (c.file ? '<div class="rv"><a href="' + c.file + '#s' + sec + '" target="_blank" rel="noopener">Revise ' + x.q.sec + ' in the notes ↗</a></div>' : '');
      d.querySelector('p').textContent = x.q.q;
      x.q.o.forEach(function(o, j){
        var li = document.createElement('li'); li.textContent = o;
        if (j === x.q.a) li.className = 'right'; else if (j === x.mine) li.className = 'mine';
        d.querySelector('ol').appendChild(li);
      });
      d.querySelector('.ex span').textContent = x.q.e;
      box.appendChild(d);
    });
    filter(all.w ? 'w' : 'all'); show('res');
  }
  function html(s){ var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function filter(f){
    [].forEach.call($('tabs').children, function(b){ b.classList.toggle('on', b.dataset.f === f); });
    [].forEach.call($('sols').children, function(d){ d.hidden = f !== 'all' && d.dataset.k !== f; });
  }
  [].forEach.call($('tabs').children, function(b){ b.onclick = function(){ filter(b.dataset.f); }; });
  $('retake').onclick = initIns;
  $('lastres').onclick = function(){ result(store.get(KEY + ':last')); };
  initIns();
})();
'''

head = open(os.path.join(B, 'chapter_head.html'), encoding='utf-8').read()
head = re.sub(r'<title>.*?</title>', '<title>DBMS Mock Test</title>', head, count=1)
head = head[:head.index('</style>')].replace('<script src="../assets/embed.js"></script>',
    # the test needs the whole window: if it is ever opened inside the hub's frame, take over the tab
    '<script>if (window.self !== window.top) try{ window.top.location.replace(location.href); }catch(e){}</script>')
ready = [c for c in chapters if c['count']]
page = head + EXAM_CSS + CSS + '''</style>
</head>
<body>
<header class="xbar">
  <div class="ttl">DBMS Mock Test<small id="xsub">IBPS SO IT · Professional Knowledge</small></div>
  <span class="timer" id="timer" hidden>Time Left --:--</span>
  <button type="button" id="palbtn" hidden>Question palette</button>
  <button class="themer" id="themer" type="button">Theme</button>
</header>
<div class="xwrap">

<div id="ins" class="card ins" hidden>
  <h2>Choose your test</h2>
  <p style="margin:0">Questions are written to IBPS SO IT Mains (Professional Knowledge) pattern: definitions, concepts, scenarios, statement-based, assertion–reason, match-the-following, "which is NOT" and numericals, at three levels. <b>''' + str(total) + ''' questions</b> so far, from ''' + ', '.join(f'Ch {c["n"]}' for c in ready) + '''. More chapters will be added.</p>
  <div class="setup">
    <label>Chapter<select id="ch"></select></label>
    <label>Level<select id="lv"><option value="all">All levels (mixed)</option><option value="E">Easy — direct recall</option><option value="M">Medium — apply and distinguish</option><option value="H">Hard — statements, traps</option></select></label>
    <label>Number of questions<select id="cnt"><option value="10">10</option><option value="20" selected>20</option><option value="30">30</option><option value="50">50</option><option value="all">All available</option></select></label>
  </div>
  <p class="avail" id="avail"></p>
  <h2 style="margin-top:22px">Instructions</h2>
  <ol>
    <li>Every attempt draws a fresh random set from the chapter (or from all chapters, spread evenly) and shuffles the options.</li>
    <li>You get <b>''' + str(SECONDS_PER_Q) + ''' seconds per question</b>, as in IBPS SO Professional Knowledge (60 questions in 45 minutes). When the timer reaches 00:00 the test is <b>submitted automatically</b>.</li>
    <li>Each question has five options and only one is correct. <b>+''' + str(PLUS) + '''</b> for a correct answer, <b>−''' + str(MINUS) + '''</b> (one-fourth) for a wrong answer, 0 for an unattempted question.</li>
    <li>Your answer is saved <b>only</b> when you click <b>Save &amp; Next</b> or <b>Mark for Review &amp; Next</b>. Moving away with <b>Previous</b> or the palette does not save the choice.</li>
    <li><b>Clear Response</b> removes the saved answer. Questions <b>answered and marked for review</b> are evaluated; marked without an answer are not.</li>
    <li>Palette colours:
      <div class="leg" style="max-width:520px;margin-top:8px">
        <span><i class="st nv">1</i>Not visited</span><span><i class="st na">2</i>Not answered</span>
        <span><i class="st a">3</i>Answered</span><span><i class="st m">4</i>Marked for review</span>
        <span><i class="st am">5</i>Answered &amp; marked for review</span>
      </div></li>
    <li>Keys <b>A–E</b> choose an option. Progress is kept in this browser, so you can resume (the timer keeps running).</li>
    <li>The scorecard breaks your score down by chapter and level, and each solution links to the subtopic to revise.</li>
  </ol>
  <label class="agree"><input type="checkbox" id="agree"> I have read and understood the instructions.</label>
  <div class="row" style="margin-top:12px">
    <button class="btn" id="begin" type="button" disabled>I am ready to begin</button>
    <button class="btn ok" id="resume" type="button" hidden>Resume attempt</button>
    <button class="btn ghost" id="lastres" type="button" hidden>View last result</button>
    <a href="../index.html#dbms/index">← DBMS notes</a>
  </div>
  <div class="hist" id="hist"></div>
</div>

<div id="exam" class="exam" hidden>
  <div class="card qpane">
    <div class="sec" id="qsec"></div>
    <div class="qhead"><span id="qno">Question No. 1</span><span class="mk">Marks: <b>+''' + str(PLUS) + '''</b> · Negative: <i>−''' + str(MINUS) + '''</i></span></div>
    <p class="qtext" id="qtext"></p>
    <ul class="opts" id="opts"></ul>
    <div class="acts">
      <button class="btn rev" id="marknext" type="button">Mark for Review &amp; Next</button>
      <button class="btn ghost" id="clear" type="button">Clear Response</button>
      <span class="sp"></span>
      <button class="btn ghost" id="prev" type="button">‹ Previous</button>
      <button class="btn ok" id="savenext" type="button">Save &amp; Next ›</button>
    </div>
  </div>
  <aside class="card pal">
    <button class="btn ghost" id="palx" type="button">✕ Close</button>
    <div class="leg">
      <span><i class="st a" id="c-a">0</i>Answered</span><span><i class="st na" id="c-na">0</i>Not answered</span>
      <span><i class="st nv" id="c-nv">0</i>Not visited</span><span><i class="st m" id="c-m">0</i>Marked for review</span>
      <span style="grid-column:1/-1"><i class="st am" id="c-am">0</i>Answered &amp; marked for review (will be evaluated)</span>
    </div>
    <div class="palh">DBMS — choose a question</div>
    <div class="grid" id="grid"></div>
    <button class="btn" id="submit" type="button">Submit Test</button>
  </aside>
</div>

<div class="modal" id="confirm" hidden>
  <div class="card">
    <h2>Submit the test?</h2>
    <table id="sum"></table>
    <p>Once submitted, you cannot change your answers.</p>
    <div class="row"><button class="btn" id="yes" type="button">Yes, submit</button><button class="btn ghost" id="no" type="button">No, go back</button></div>
  </div>
</div>

<div id="res" hidden>
  <div class="card">
    <h2>Scorecard</h2>
    <p class="hist" id="rsub" style="margin-top:-6px"></p>
    <p id="timeup" class="verdict" style="color:var(--na)" hidden>Time is up. The test was submitted automatically.</p>
    <div class="score" id="score"></div>
    <p class="verdict" id="verdict"></p>
    <div class="bd" id="bd"></div>
    <div class="row" style="margin-top:12px"><button class="btn" id="retake" type="button">New test</button><a href="../index.html#dbms/index">← DBMS notes</a></div>
  </div>
  <h2 style="margin:22px 0 0;font-size:18px">Solutions</h2>
  <div class="tabs" id="tabs"><button data-f="all" type="button">All</button><button data-f="w" type="button">Wrong</button><button data-f="s" type="button">Not attempted</button><button data-f="c" type="button">Correct</button></div>
  <div id="sols"></div>
</div>

</div>
<script>
var DATA = ''' + data + ''';
''' + JS + '''</script>
</body>
</html>
'''
open(os.path.join(D, OUT + '.html'), 'w', encoding='utf-8').write(page)
print(f'{OUT}.html: {total} questions from', ', '.join(f'Ch {c["n"]} ({c["count"]})' for c in ready))

import subprocess   # the index card shows the question count per chapter
print(subprocess.run(['python3', '-I', os.path.join(B, 'build_index.py')], capture_output=True, text=True).stdout.strip())

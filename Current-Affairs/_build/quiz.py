"""Exam-style mock test page for a class (used by build.py when the data file defines MCQ).

MCQ item = (question, correct, [4 wrong options], explanation). Options are shuffled with fixed
seeds, so the correct letter is spread evenly over A–E and rebuilds are identical.
The page works like an online bank exam: instructions → timed test with a question palette
(Save & Next / Mark for Review / Clear Response) → submit summary → scorecard + solutions.
"""
import json, random, hashlib

MARK_RIGHT, MARK_WRONG = 1, 0.25
SECONDS_PER_Q = 40


def minutes(n):
    """Test time: 40 s per question, rounded up to a 5-minute block (30 Qs → 20 min, 55 Qs → 40 min)."""
    return -(-n * SECONDS_PER_Q // 300) * 5

CSS = '''
:root{--rev:#6B4FA0;--na:#C0392B;--ans:#2E8B57;--nv-bg:#E9EEF1}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--rev:#A88BD8;--na:#E06C6C;--ans:#5DBB8A;--nv-bg:#22313A}}
:root[data-theme="dark"]{--rev:#A88BD8;--na:#E06C6C;--ans:#5DBB8A;--nv-bg:#22313A}
body{min-height:100vh}
[hidden]{display:none!important}
.xbar{position:sticky;top:0;z-index:10;display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:var(--accent);color:#fff;padding:8px 16px}
:root[data-theme="dark"] .xbar{color:#0C1317}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .xbar{color:#0C1317}}
.xbar .ttl{font-weight:700;font-size:15px;flex:1;min-width:180px;line-height:1.3}
.xbar .ttl small{display:block;font-weight:500;opacity:.85;font-size:12px}
.xbar .timer{font:700 15px var(--code);background:rgba(255,255,255,.16);border-radius:4px;padding:4px 10px;white-space:nowrap}
.xbar .timer.low{background:var(--na);color:#fff;animation:blink 1s steps(2) infinite}
@keyframes blink{50%{opacity:.6}}
.xbar button{font:13px var(--body);background:rgba(255,255,255,.16);color:inherit;border:1px solid rgba(255,255,255,.4);border-radius:4px;padding:5px 10px;cursor:pointer}
.xbar button.themer{position:static}
#palbtn,#palx{display:none}
.xwrap{max-width:1180px;margin:0 auto;padding:16px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:20px 22px;margin:0}
.card h2{margin:0 0 10px;font-size:20px}
.card table{border-collapse:collapse;width:100%;font-size:14.5px;margin:10px 0}
.card th,.card td{border:1px solid var(--line);padding:7px 10px;text-align:left}
.card th{background:var(--surface-2)}
.ins ol li{margin:4px 0}
.agree{display:flex;gap:8px;align-items:flex-start;margin:16px 0 4px;font-size:14.5px}
.btn{font:600 14px var(--body);border-radius:4px;padding:9px 16px;cursor:pointer;border:1px solid var(--accent);background:var(--accent);color:#fff}
:root[data-theme="dark"] .btn:not(.ghost){color:#0C1317}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .btn:not(.ghost){color:#0C1317}}
.btn.ghost{background:var(--surface);color:var(--accent)}
.btn.rev{background:var(--rev);border-color:var(--rev)}
.btn.ok{background:var(--ans);border-color:var(--ans)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.hist{font-size:13.5px;color:var(--muted)}
/* exam layout */
.exam{display:grid;grid-template-columns:1fr 300px;gap:16px;align-items:start}
.qpane{display:flex;flex-direction:column;min-height:calc(100vh - 110px)}
.sec{font-size:13px;color:var(--muted);margin-bottom:8px}
.sec b{color:var(--accent)}
.qhead{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:12px;font-weight:700}
.qhead .mk{font-weight:500;font-size:13px;color:var(--muted)}
.qhead .mk b{color:var(--ans)} .qhead .mk i{font-style:normal;color:var(--na);font-weight:700}
.qtext{font-size:17px;margin:0 0 16px;line-height:1.55}
.opts{list-style:none;margin:0;padding:0}
.opts label{display:flex;gap:12px;align-items:flex-start;padding:10px 12px;border:1px solid var(--line);border-radius:5px;margin:8px 0;cursor:pointer;background:var(--surface)}
.opts label:hover{border-color:var(--accent)}
.opts input{margin-top:5px;accent-color:var(--accent)}
.opts .l{font-weight:700;color:var(--muted);min-width:18px}
.opts label.on{border-color:var(--accent);background:var(--accent-soft)}
.acts{margin-top:auto;padding-top:16px;border-top:1px solid var(--line);display:flex;gap:8px;flex-wrap:wrap}
.acts .sp{flex:1}
.kbd{font-size:12px;color:var(--muted);margin-top:8px}
/* palette */
.pal{position:sticky;top:64px}
.leg{display:grid;grid-template-columns:1fr 1fr;gap:8px 10px;font-size:12.5px;margin-bottom:14px}
.leg span{display:flex;align-items:center;gap:6px}
.st{display:inline-flex;align-items:center;justify-content:center;width:34px;height:30px;font:600 13px var(--body);border:1px solid var(--line);border-radius:4px;background:var(--nv-bg);color:var(--ink);position:relative;flex:none}
.leg .st{width:26px;height:22px;font-size:11.5px}
.st.na{background:var(--na);border-color:var(--na);color:#fff;border-radius:4px 4px 14px 14px}
.st.a{background:var(--ans);border-color:var(--ans);color:#fff;border-radius:14px 14px 4px 4px}
.st.m{background:var(--rev);border-color:var(--rev);color:#fff;border-radius:50%}
.st.am{background:var(--rev);border-color:var(--rev);color:#fff;border-radius:50%}
.st.am::after{content:"";position:absolute;right:-2px;bottom:-2px;width:10px;height:10px;border-radius:50%;background:var(--ans);border:2px solid var(--surface)}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;justify-items:center;max-height:44vh;overflow:auto;padding:4px 2px}
.grid button.st{cursor:pointer}
.grid button.cur{outline:2px solid var(--accent);outline-offset:2px}
.palh{font-size:13px;font-weight:700;background:var(--surface-2);border-radius:4px;padding:6px 10px;margin-bottom:10px}
.pal .btn{width:100%;margin-top:14px}
/* modal */
.modal{position:fixed;inset:0;z-index:30;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;padding:16px}
.modal .card{max-width:560px;width:100%}
/* result */
.score{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:14px 0}
.score div{border:1px solid var(--line);border-radius:6px;padding:10px 12px;background:var(--surface-2)}
.score b{display:block;font-size:22px}
.score span{font-size:12.5px;color:var(--muted)}
.score .c b{color:var(--ans)} .score .w b{color:var(--na)}
.verdict{font-weight:600}
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin:18px 0 10px}
.tabs button{font:13px var(--body);border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:5px 12px;cursor:pointer}
.tabs button.on{background:var(--accent);border-color:var(--accent);color:#fff}
.sol{border:1px solid var(--line);border-left:4px solid var(--line);border-radius:5px;padding:12px 14px;margin:10px 0;background:var(--surface)}
.sol.c{border-left-color:var(--ans)} .sol.w{border-left-color:var(--na)} .sol.s{border-left-color:var(--muted)}
.sol .qn{font-size:12.5px;color:var(--muted);font-weight:700}
.sol .qn em{font-style:normal;margin-left:8px}
.sol.c .qn em{color:var(--ans)} .sol.w .qn em{color:var(--na)}
.sol p{margin:4px 0 8px}
.sol ol{list-style:upper-alpha;margin:0 0 6px;padding-left:24px}
.sol li{padding:1px 4px;border-radius:3px}
.sol li.right{color:var(--ans);font-weight:700}
.sol li.right::after{content:"  ✓ correct"}
.sol li.mine{color:var(--na);font-weight:700;text-decoration:line-through}
.sol li.mine::after{content:"  ✗ your answer";text-decoration:none;display:inline-block;margin-left:4px}
.sol .ex{font-size:14px;background:var(--surface-2);border-radius:4px;padding:6px 10px}
@media (max-width:860px){
  .exam{grid-template-columns:1fr}
  #palbtn,#palx{display:inline-block}
  .pal #palx{display:block;width:100%;margin:0 0 14px}
  .qhead{flex-wrap:wrap}
  .pal{position:fixed;top:0;right:0;bottom:0;width:300px;max-width:88vw;z-index:20;overflow:auto;border-radius:0;transform:translateX(105%);transition:transform .2s;box-shadow:-8px 0 24px rgba(0,0,0,.25)}
  body.palopen .pal{transform:none}
  .qpane{min-height:calc(100vh - 140px)}
  .acts .btn{flex:1 1 40%;padding:9px 8px}
  .acts .sp{display:none}
}
'''

JS = r'''
(function(){
  var Q = DATA.questions, N = Q.length, KEY = 'ca-quiz-' + DATA.id, RUN = KEY + ':run:' + DATA.sig, L = 'ABCDE';
  var root = document.documentElement, $ = function(id){ return document.getElementById(id); };
  var store = {
    get: function(k){ try{ return JSON.parse(localStorage.getItem(k)); }catch(e){ return null; } },
    set: function(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)); }catch(e){} },
    del: function(k){ try{ localStorage.removeItem(k); }catch(e){} }
  };
  try{ var t = localStorage.getItem('ca-notes-theme'); if (t) root.setAttribute('data-theme', t); }catch(e){}
  $('themer').onclick = function(){
    var cur = root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    var nxt = cur === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', nxt);
    try{ localStorage.setItem('ca-notes-theme', nxt); }catch(e){}
  };

  var S = null, tick = null;   // S = attempt in progress
  function show(id){ ['ins', 'exam', 'res'].forEach(function(x){ $(x).hidden = x !== id; }); $('timer').hidden = id !== 'exam'; $('palbtn').hidden = id !== 'exam'; window.scrollTo(0, 0); }
  function save(){ if (S) store.set(RUN, S); }
  function fmt(s){ s = Math.max(0, Math.round(s)); var m = Math.floor(s / 60); return (m < 10 ? '0' : '') + m + ':' + ('0' + s % 60).slice(-2); }

  /* ---------- instructions ---------- */
  function initIns(){
    var run = store.get(RUN), hist = store.get(KEY + ':hist') || [];
    $('resume').hidden = !run;
    $('begin').textContent = run ? 'Start a fresh attempt' : 'I am ready to begin';
    $('hist').innerHTML = hist.length ? 'Previous attempts: ' + hist.slice(-5).map(function(h){
      return '<b>' + h.score + '</b>/' + N + ' <span>(' + h.date + ')</span>'; }).join(' · ') : '';
    show('ins');
  }
  $('agree').onchange = function(){ $('begin').disabled = !this.checked; };
  $('begin').onclick = function(){
    S = { i: 0, ans: [], st: [], sel: null, end: Date.now() + DATA.seconds * 1000, start: Date.now() };
    for (var k = 0; k < N; k++){ S.ans.push(null); S.st.push('nv'); }
    startExam();
  };
  $('resume').onclick = function(){ S = store.get(RUN); startExam(); };

  /* ---------- exam ---------- */
  function startExam(){
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
    if (!keepSel || S.sel === undefined) S.sel = S.ans[S.i];
    var q = Q[S.i];
    $('qno').textContent = 'Question No. ' + (S.i + 1);
    $('qtext').textContent = q.q;
    var ul = $('opts'); ul.innerHTML = '';
    q.o.forEach(function(o, k){
      var li = document.createElement('li'), lab = document.createElement('label');
      lab.innerHTML = '<input type="radio" name="opt"><span class="l">' + L[k] + '.</span><span></span>';
      lab.lastChild.textContent = o;
      var inp = lab.firstChild; inp.checked = S.sel === k; lab.classList.toggle('on', S.sel === k);
      inp.onchange = function(){ S.sel = k; mark(); save(); };
      li.appendChild(lab); ul.appendChild(li);
    });
    paint(); save();
    document.body.classList.remove('palopen');
  }
  function mark(){ [].forEach.call($('opts').querySelectorAll('label'), function(l, k){ l.classList.toggle('on', S.sel === k); l.firstChild.checked = S.sel === k; }); }
  function buildPalette(){
    var g = $('grid'); g.innerHTML = '';
    for (var k = 0; k < N; k++) (function(k){
      var b = document.createElement('button'); b.type = 'button'; b.className = 'st'; b.textContent = k + 1;
      b.onclick = function(){ go(k); };   // unsaved choice is discarded, as in the real exam
      g.appendChild(b);
    })(k);
  }
  function counts(){
    var c = { a: 0, na: 0, nv: 0, m: 0, am: 0 };
    S.st.forEach(function(s){ c[s]++; }); return c;
  }
  function paint(){
    [].forEach.call($('grid').children, function(b, k){ b.className = 'st ' + S.st[k] + (k === S.i ? ' cur' : ''); });
    var c = counts();
    ['a', 'na', 'nv', 'm', 'am'].forEach(function(s){ $('c-' + s).textContent = c[s]; });
  }
  function next(){ go(S.i + 1); }
  $('savenext').onclick = function(){
    S.ans[S.i] = S.sel; S.st[S.i] = S.sel == null ? 'na' : 'a'; next();
  };
  $('marknext').onclick = function(){
    S.ans[S.i] = S.sel; S.st[S.i] = S.sel == null ? 'm' : 'am'; next();
  };
  $('clear').onclick = function(){
    S.sel = null; S.ans[S.i] = null;
    S.st[S.i] = (S.st[S.i] === 'm' || S.st[S.i] === 'am') ? 'm' : 'na';
    mark(); paint(); save();
  };
  $('prev').onclick = function(){ go(S.i - 1); };
  $('palbtn').onclick = function(){ document.body.classList.toggle('palopen'); };
  $('palx').onclick = function(){ document.body.classList.remove('palopen'); };
  document.addEventListener('keydown', function(e){
    if ($('exam').hidden || !$('confirm').hidden || e.ctrlKey || e.metaKey || e.altKey) return;
    var k = L.indexOf(e.key.toUpperCase());
    if (k >= 0 && k < Q[S.i].o.length){ S.sel = k; mark(); save(); }
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
    var r = { right: 0, wrong: 0, skip: 0, ans: S.ans.slice(),
              secs: Math.min(DATA.seconds, Math.round((Math.min(Date.now(), S.end) - S.start) / 1000)), timeUp: timeUp };
    Q.forEach(function(q, k){ if (r.ans[k] == null) r.skip++; else if (r.ans[k] === q.a) r.right++; else r.wrong++; });
    r.score = Math.round((r.right * DATA.plus - r.wrong * DATA.minus) * 100) / 100;
    var hist = store.get(KEY + ':hist') || [];
    hist.push({ score: r.score, date: new Date().toLocaleDateString(undefined, { day: 'numeric', month: 'short' }) });
    store.set(KEY + ':hist', hist.slice(-20)); store.set(KEY + ':last', r); store.del(RUN);
    S = null; result(r);
  }

  /* ---------- result ---------- */
  function result(r){
    var att = r.right + r.wrong, acc = att ? Math.round(r.right / att * 100) : 0, pct = Math.round(Math.max(0, r.score) / N * 100);
    $('timeup').hidden = !r.timeUp;
    $('score').innerHTML =
      '<div><b>' + r.score + ' / ' + N + '</b><span>Score (+' + DATA.plus + ' / −' + DATA.minus + ')</span></div>' +
      '<div class="c"><b>' + r.right + '</b><span>Correct</span></div>' +
      '<div class="w"><b>' + r.wrong + '</b><span>Wrong (−' + (r.wrong * DATA.minus) + ')</span></div>' +
      '<div><b>' + r.skip + '</b><span>Not attempted</span></div>' +
      '<div><b>' + acc + '%</b><span>Accuracy</span></div>' +
      '<div><b>' + fmt(r.secs) + '</b><span>Time taken of ' + fmt(DATA.seconds) + '</span></div>';
    $('verdict').textContent = pct >= 80 ? 'Excellent — this class is locked in. Revise again in a week.'
      : pct >= 60 ? 'Good. Re-read the topics you got wrong, then retake tomorrow.'
      : 'Needs revision. Go through the class notes once more (use Recall mode), then retake.';
    var box = $('sols'); box.innerHTML = '';
    Q.forEach(function(q, k){
      var mine = r.ans[k], cls = mine == null ? 's' : mine === q.a ? 'c' : 'w';
      var d = document.createElement('div'); d.className = 'sol ' + cls; d.dataset.k = cls;
      d.innerHTML = '<div class="qn">Q' + (k + 1) + '<em>' + (cls === 'c' ? 'Correct +' + DATA.plus : cls === 'w' ? 'Wrong −' + DATA.minus : 'Not attempted') + '</em></div><p></p><ol></ol><div class="ex"><b>Explanation:</b> <span></span></div>';
      d.querySelector('p').textContent = q.q;
      q.o.forEach(function(o, j){
        var li = document.createElement('li'); li.textContent = o;
        if (j === q.a) li.className = 'right'; else if (j === mine) li.className = 'mine';
        d.querySelector('ol').appendChild(li);
      });
      d.querySelector('.ex span').textContent = q.e;
      box.appendChild(d);
    });
    filter('all'); show('res');
  }
  function filter(f){
    [].forEach.call($('tabs').children, function(b){ b.classList.toggle('on', b.dataset.f === f); });
    [].forEach.call($('sols').children, function(d){ d.hidden = f !== 'all' && d.dataset.k !== f; });
  }
  [].forEach.call($('tabs').children, function(b){ b.onclick = function(){ filter(b.dataset.f); }; });
  $('retake').onclick = initIns;

  var last = store.get(KEY + ':last');
  if (location.hash === '#result' && last) result(last); else initIns();
  $('lastres').hidden = !last;
  $('lastres').onclick = function(){ result(store.get(KEY + ':last')); };
})();
'''


def mcq_data(d):
    """Shuffle options; the correct answer's letter is spread evenly over A–E (so guessing one letter never pays)."""
    rng = random.Random(d['file'])
    slots = [i % 5 for i in range(len(d['MCQ']))]
    rng.shuffle(slots)
    qs = []
    for (q, right, wrong, ex), a in zip(d['MCQ'], slots):
        opts = list(wrong)
        random.Random(q).shuffle(opts)
        opts.insert(a, right)
        qs.append({'q': q, 'o': opts, 'a': a, 'e': ex})
    return qs


def render_quiz(d, base_head):
    qs = mcq_data(d)
    n = len(qs)
    secs = minutes(n) * 60
    title = f'{d["month"]} · Class {d["cls"]}'
    # An unfinished attempt saved in the browser is only resumed if the questions/options are unchanged.
    sig = hashlib.md5(json.dumps(qs, ensure_ascii=False).encode()).hexdigest()[:8]
    data = json.dumps({'id': d['file'], 'sig': sig, 'questions': qs, 'seconds': secs, 'plus': MARK_RIGHT, 'minus': MARK_WRONG},
                      ensure_ascii=False).replace('</', '<\\/')
    head = base_head.replace('<title>Operating System Notes</title>', f'<title>CA Mock Test {title}</title>')
    return head + CSS + '''</style>
<script>if (window.self !== window.top) { try { window.top.location.replace(location.href); } catch (e) {} }</script>
</head>
<body>
<header class="xbar">
  <div class="ttl">Current Affairs Mock Test — ''' + title + f'''<small>{n} questions · {secs // 60} minutes · +{MARK_RIGHT} / −{MARK_WRONG}</small></div>
  <span class="timer" id="timer" hidden>Time Left --:--</span>
  <button type="button" id="palbtn" hidden>Question palette</button>
  <button class="themer" id="themer" type="button">Theme</button>
</header>
<div class="xwrap">

<div id="ins" class="card ins" hidden>
  <h2>General Instructions</h2>
  <table>
    <tr><th>Section</th><th>No. of questions</th><th>Maximum marks</th><th>Time</th></tr>
    <tr><td>Current Affairs — {title}</td><td>{n}</td><td>{n * MARK_RIGHT}</td><td>{secs // 60} minutes</td></tr>
  </table>
  <ol>
    <li>The clock starts when you click <b>I am ready to begin</b>. When the timer reaches 00:00 the test is <b>submitted automatically</b>.</li>
    <li>Each question has five options and only one is correct. <b>+{MARK_RIGHT}</b> for a correct answer, <b>−{MARK_WRONG}</b> (one-fourth) for a wrong answer, 0 for an unattempted question.</li>
    <li>Your answer is saved <b>only</b> when you click <b>Save &amp; Next</b> or <b>Mark for Review &amp; Next</b>. If you choose an option and then move to another question with <b>Previous</b> or the palette, the choice is <b>not saved</b>.</li>
    <li><b>Clear Response</b> removes the saved answer of the current question.</li>
    <li>Questions that are <b>answered and marked for review</b> are evaluated. Questions marked for review without an answer are not.</li>
    <li>The question palette on the right shows the status of each question:
      <div class="leg" style="max-width:520px;margin-top:8px">
        <span><i class="st nv">1</i>Not visited</span><span><i class="st na">2</i>Not answered</span>
        <span><i class="st a">3</i>Answered</span><span><i class="st m">4</i>Marked for review</span>
        <span><i class="st am">5</i>Answered &amp; marked for review</span>
      </div></li>
    <li>You can also press <b>A–E</b> on the keyboard to choose an option.</li>
    <li>Your progress is kept in this browser, so you can resume if the page is closed (the timer keeps running).</li>
  </ol>
  <label class="agree"><input type="checkbox" id="agree"> I have read and understood the instructions.</label>
  <div class="row" style="margin-top:12px">
    <button class="btn" id="begin" type="button" disabled>I am ready to begin</button>
    <button class="btn ok" id="resume" type="button" hidden>Resume attempt</button>
    <button class="btn ghost" id="lastres" type="button" hidden>View last result</button>
    <a href="{d["file"]}.html">← Back to class notes</a>
  </div>
  <p class="hist" id="hist"></p>
</div>

<div id="exam" class="exam" hidden>
  <div class="card qpane">
    <div class="sec">Section: <b>Current Affairs</b></div>
    <div class="qhead"><span id="qno">Question No. 1</span><span class="mk">Marks: <b>+{MARK_RIGHT}</b> · Negative: <i>−{MARK_WRONG}</i></span></div>
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
    <div class="palh">Current Affairs — choose a question</div>
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
    <p id="timeup" class="verdict" style="color:var(--na)" hidden>Time is up. The test was submitted automatically.</p>
    <div class="score" id="score"></div>
    <p class="verdict" id="verdict"></p>
    <div class="row"><button class="btn" id="retake" type="button">Retake test</button><a href="{d["file"]}.html">← Back to class notes</a></div>
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

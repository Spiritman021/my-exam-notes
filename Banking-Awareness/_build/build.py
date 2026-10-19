"""Builds the Banking Awareness pages (Saarthi Alpha / Beta batches) from data/*.py.

One data file per class PDF: data/alpha-NN.py or data/beta-NN.py (CLASS, TITLE, FULL, S, FLASH, QUIZ, RAPID).
Each item in S is a dict: h, hi (Hindi term), tag ('bank'/'hot'), pics [(img name, caption)],
facts (from the PDF), table (headers, rows), add (added for the exam), trap, html (a module-level SVG name).
Pictures live in Banking-Awareness/img/<name>.jpg, cut from the class PDF.

Run:  python3 Banking-Awareness/_build/build.py
Writes Alpha/ and Beta/ class pages + overview, and the ba-alpha / ba-beta entries in the hub (../../index.html).
Reuses the look of the Current Affairs pages (Current-Affairs/_build/build.py).
"""
import os, re, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
BA = os.path.dirname(HERE)
ROOT = os.path.dirname(BA)

spec = importlib.util.spec_from_file_location('ca_build', os.path.join(ROOT, 'Current-Affairs', '_build', 'build.py'))
ca = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ca)

sched = {}
exec(open(os.path.join(HERE, 'data', '_schedule.py')).read(), sched)

BATCHES = {
    'alpha': dict(name='Alpha', folder='Alpha', plan=sched['ALPHA'], color='#1F5F8B',
                  blurb='Banking & financial concepts: banking system, RBI, NABARD & PSL, monetary policy, inflation, markets, foreign trade, budget, NPA, Basel, PCA, national income.'),
    'beta': dict(name='Beta', folder='Beta', plan=sched['BETA'], color='#6B4FA0',
                 blurb='RBI schemes & indices, banking terminology, NPCI products and government schemes.'),
}

HEAD = ca.BASE_HEAD.replace('../assets/embed.js', '../../assets/embed.js')

BA_CSS = '''
.item h4 .hi{font-weight:500;color:var(--muted);font-size:14px;margin-left:6px}
.item .src{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--lec);margin:6px 0 0}
.item figure.pic button.zoom,.gal button.zoom{all:unset;cursor:zoom-in;display:block}
.item figure.pic button.zoom:focus-visible img,.gal button.zoom:focus-visible img{outline:2px solid var(--accent)}
.gal{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 4px;clear:none}
.item .box{display:flow-root}
.gal figure{margin:0;width:180px;text-align:center}
.gal img{width:180px;height:120px;object-fit:contain;background:#fff;border:1px solid var(--line);border-radius:6px;padding:3px;display:block}
.gal figcaption,.item figure.pic figcaption{font-size:11.5px;color:var(--muted);line-height:1.3;margin-top:3px;text-transform:none;letter-spacing:0;font-weight:500}
.item .tw table{margin:6px 0}
.item th,.item td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
.item th{background:var(--surface-2);font-size:13px}
.box.add ul{margin:2px 0;padding-left:20px}
figure.diagram{margin:10px 0;text-align:center}
figure.diagram svg{width:100%;max-width:640px;height:auto}
figure.diagram figcaption{font-size:12.5px;color:var(--muted);text-transform:none;letter-spacing:0;font-weight:500}
.sort{display:grid;gap:8px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));margin:8px 0}
.sort .q{border:1px solid var(--line);border-radius:6px;padding:8px 10px;background:var(--surface)}
.sort .q b{display:block;margin-bottom:6px}
.sort button{font:inherit;font-size:13px;border:1px solid var(--accent);background:none;color:var(--accent);border-radius:4px;padding:3px 10px;margin-right:6px;cursor:pointer}
.sort .q.ok{border-color:var(--ok);background:var(--lec-bg)} .sort .q.no{border-color:var(--bad)}
.sort .fb{font-size:13px;margin-left:4px}
.flash{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));margin:10px 0}
.flash button{font:inherit;text-align:left;min-height:96px;border:1px solid var(--line);border-top:3px solid var(--accent);border-radius:6px;background:var(--surface);color:var(--ink);padding:10px 12px;cursor:pointer}
.flash button .bk{display:none;font-size:13.5px;color:var(--ink)}
.flash button .fr{font-weight:700;color:var(--accent)}
.flash button .hint{display:block;font-size:11px;color:var(--muted);margin-top:6px}
.flash button.on .bk{display:block} .flash button.on .hint{display:none} .flash button.on{border-top-color:var(--ok)}
.lb{position:fixed;inset:0;z-index:50;background:rgba(0,0,0,.82);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;cursor:zoom-out}
.lb[hidden]{display:none}
.lb img{max-width:min(96vw,1100px);max-height:82vh;background:#fff;border-radius:6px}
.lb p{color:#fff;margin:10px 0 0;font-size:14px}
.plan td,.plan th{border:1px solid var(--line);padding:7px 10px;vertical-align:top;text-align:left}
.plan th{background:var(--surface-2)}
.plan tr.ready td{background:var(--lec-bg)}
.plan .st{white-space:nowrap;font-size:13px;font-weight:600}
.plan .st.soon{color:var(--muted);font-weight:500}
.tl{list-style:none;margin:10px 0;padding:0 0 0 18px;border-left:3px solid var(--accent)}
.tl li{position:relative;margin:0 0 10px;padding-left:10px}
.tl li::before{content:"";position:absolute;left:-27px;top:6px;width:13px;height:13px;border-radius:50%;background:var(--surface);border:3px solid var(--accent)}
.tl .y{display:inline-block;min-width:116px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums}
.plan .cov{display:block;margin-top:4px;font-size:13px;color:var(--lec)}
.plan td.n{font-weight:700;color:var(--accent);white-space:nowrap}
'''

BA_JS = '''<div class="lb" id="lb" hidden><img alt=""><p></p></div>
<script>
(function(){
  var lb=document.getElementById('lb'), im=lb.querySelector('img'), cap=lb.querySelector('p');
  document.addEventListener('click',function(e){
    var z=e.target.closest('.zoom');
    if(z){ im.src=z.dataset.full; cap.textContent=z.dataset.cap||''; lb.hidden=false; return; }
    if(e.target.closest('#lb')){ lb.hidden=true; return; }
    var f=e.target.closest('.flash button'); if(f){ f.classList.toggle('on'); return; }
    var s=e.target.closest('.sort button');
    if(s){ var q=s.closest('.q'), ok=s.dataset.v===q.dataset.a;
      q.classList.remove('ok','no'); q.classList.add(ok?'ok':'no');
      q.querySelector('.fb').textContent=ok?'✓ Correct':'✗ Answer: '+q.dataset.a; }
  });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') lb.hidden=true; });
})();
</script>
'''

LEGEND = ('<div class="legend"><span class="l1">📄 From the class PDF</span><span class="l2">➕ Added for exam</span>'
          '<span class="l3">⚠️ Exam trap</span><span class="l4">🎯 Likely question</span></div>')

GLOSSARY = dict(ca.GLOSSARY)
GLOSSARY.update({
    'PMJDY': ('Pradhan Mantri Jan-Dhan Yojana · Launched <b>28 Aug 2014</b> · National Mission for Financial Inclusion · Zero-balance account + RuPay debit card', None),
    'DICGC': ('Deposit Insurance and Credit Guarantee Corporation · Wholly owned subsidiary of <b>RBI</b> · Insures bank deposits up to <b>₹5 lakh</b> per depositor per bank', None),
    'CASA': ('Current Account + Savings Account deposits · Low-cost funds for a bank · CASA ratio = CASA ÷ total deposits', None),
    'Form 60': ('Declaration filed by a person who does <b>not have a PAN</b> · Used for financial transactions instead of PAN', None),
})


def k(s):
    return f'<b class="k">{s}</b>'


def load(path):
    ns = {'k': k, 'S': [], 'FLASH': [], 'QUIZ': [], 'RAPID': [], 'NOTE': '', 'SORT': [], 'COVERS': ''}
    exec(open(path).read(), ns)
    batch, n = re.match(r'(alpha|beta)-(\d+)\.py$', os.path.basename(path)).groups()
    ns.update(batch=batch, file=f'Class-{int(n):02d}', topics=sum(len(x[2]) for x in ns['S']))
    return ns


def fig(name, cap, cls):
    src = f'../img/{name}.jpg'
    return (f'<figure class="{cls}"><button type="button" class="zoom" data-full="{src}" data-cap="{cap}" aria-label="Enlarge: {cap}">'
            f'<img src="{src}" alt="{cap}" loading="lazy"></button><figcaption>{cap}</figcaption></figure>')


def table_html(t):
    hd, rows = t
    return ('<div class="tw"><table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in hd) + '</tr></thead><tbody>'
            + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')


def item_html(it, d):
    terms = GLOSSARY
    used = set()
    lt = lambda s: ca.link_terms(s, terms, used)
    pics = it.get('pics', [])
    first = fig(*pics[0], 'pic') if len(pics) == 1 else ''
    gal = ('<div class="gal">' + ''.join(fig(n, c, 'g') for n, c in pics) + '</div>') if len(pics) > 1 else ''
    hi = f'<span class="hi">{it["hi"]}</span>' if it.get('hi') else ''
    out = f'<div class="item">{first}<h4>{ca.TAGS.get(it.get("tag"), "")}{lt(it["h"])}{hi}</h4>'
    if it.get('html'):
        out += d[it['html']]
    if it.get('facts'):
        out += '<ul>' + ''.join(f'<li>{lt(f)}</li>' for f in it['facts']) + '</ul>'
    if it.get('table'):
        hd, rows = it['table']
        out += table_html((hd, [[lt(c) for c in r] for r in rows]))
    if it.get('sort') and d.get('SORT'):
        opts = d.get('SORT_OPTS') or ['Demand', 'Term']
        btns = ''.join(f'<button type="button" data-v="{o}">{o}</button>' for o in opts)
        out += (f'<p class="src">{d.get("SORT_Q") or "Quick check – demand or term?"}</p><div class="sort">' + ''.join(
            f'<div class="q" data-a="{a}"><b>{n}</b>{btns}<span class="fb"></span></div>' for n, a in d['SORT']) + '</div>')
    out += gal
    if it.get('add'):
        out += '<div class="box add"><span class="t">➕ Added for exam</span><ul>' + ''.join(f'<li>{lt(a)}</li>' for a in it['add']) + '</ul></div>'
    if it.get('trap'):
        out += f'<div class="box trap"><span class="t">⚠️ Exam trap</span>{lt(it["trap"])}</div>'
    return out + '</div>'


def page_head(title):
    return HEAD.replace('<title>Operating System Notes</title>', f'<title>{title}</title>') + ca.EXTRA_CSS + BA_CSS + '</style>\n</head>\n<body>\n<button class="themer" id="themer" type="button">Theme</button>\n<div class="wrap">\n'


def nav_html(prev, nxt):
    p = f'<a href="{prev["file"]}.html">← Class {prev["CLASS"]}</a>' if prev else '<span class="off">← Previous class</span>'
    n = f'<a href="{nxt["file"]}.html">Class {nxt["CLASS"]} →</a>' if nxt else '<span class="off">Next class →</span>'
    return f'<nav class="topnav" aria-label="Class navigation">{p}<a href="index.html">☰ All classes</a>{n}</nav>'


def render(d, prev, nxt):
    b = BATCHES[d['batch']]
    secs, toc = '', ''
    for i, (t, intro, items) in enumerate(d['S'], 1):
        toc += f'<li><a href="#c{i}"><span class="n">{i}</span>{t}</a></li>'
        secs += (f'<section id="c{i}"><h3><span class="n">{i}</span>{t}</h3>' + (f'<p class="cs">{intro}</p>' if intro else '')
                 + ''.join(item_html(x, d) for x in items) + '</section>\n')
    n = len(d['S']) + 1
    flash = ''
    if d['FLASH']:
        toc += f'<li><a href="#flash"><span class="n">{n}</span>Flashcards ({len(d["FLASH"])})</a></li>'
        flash = (f'<section id="flash"><h3><span class="n">{n}</span>Flashcards</h3><p class="cs">Say the meaning, then tap the card to check.</p><div class="flash">'
                 + ''.join(f'<button type="button"><span class="fr">{t}</span><span class="bk">{a}</span><span class="hint">tap to flip</span></button>' for t, a in d['FLASH'])
                 + '</div></section>')
        n += 1
    toc += f'<li><a href="#quiz"><span class="n">{n}</span>Self-test ({len(d["QUIZ"])} questions)</a></li><li><a href="#rapid"><span class="n">⚡</span>Rapid Revision</a></li>'
    quiz = (f'<section id="quiz" class="quiz"><h3><span class="n">{n}</span>Self-test</h3><p class="cs">Answer out loud first, then click to check.</p>'
            + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in d['QUIZ']) + '</section>')
    rapid = '<div class="rapid" id="rapid"><h3>⚡ Rapid Revision</h3><ul>' + ''.join(f'<li>{r}</li>' for r in d['RAPID']) + '</ul></div>'
    plan = next((p for p in b['plan'] if p[1] == d['CLASS']), None)
    when = f' · {plan[0]}' if plan else ''
    nav = nav_html(prev, nxt)
    title = f'Class {d["CLASS"]} · {d["TITLE"]}'
    note = f'<div class="box alert"><span class="t">ℹ️ Note</span>{d["NOTE"]}</div>' if d['NOTE'] else ''
    return page_head(f'Banking {b["name"]} {title}') + nav + f'''
<header class="cover">
  <div class="brand">Banking Awareness · Saarthi {b["name"]} 2026 · Class {d["CLASS"]}{when}</div>
  <h1>{d["TITLE"]}</h1>
  <p class="sub">{d["FULL"]}. From the class PDF (Ashish Gautam Sir, Adda247 Warrior Pro Batch) · {d["topics"]} topics.</p>
  {LEGEND}
</header>
<div class="box lec howto"><span class="t">🎓 How to study this page</span>
<ol>
<li><b>Read once.</b> The bullet points are the class PDF; purple ➕ boxes are extra points added for the exam. Click any picture to enlarge it, and hover over a <span style="border-bottom:1.5px dotted var(--accent)">dotted term</span> for a quick fact card.</li>
<li><b>Turn Recall mode on</b>: the key facts go blank. Say each one, then click to reveal.</li>
<li><b>Flip the flashcards</b> and take the self-test. Revise tomorrow, in a week and in a month.</li>
</ol></div>
{note}
<div class="recallbar"><button id="recall" type="button">Recall mode: off</button><button id="revealall" class="ghost" type="button">Reveal all</button><span class="hint">Hides the key facts. Click any blank to reveal it.</span></div>
<nav class="toc" aria-label="Contents"><h2>Contents</h2><ol>{toc}</ol></nav>
''' + secs + flash + quiz + rapid + f'''
<p class="end" id="fin">End of Saarthi {b["name"]} · {title}</p>
''' + nav + '\n</div>\n' + BA_JS + ca.PAGE_JS


def overview(key, classes):
    b = BATCHES[key]
    ready = {d['CLASS']: d for d in classes}
    rows = ''
    for p in b['plan']:
        date, n = p[0], p[1]
        topic = p[2] if len(p) == 3 else f'<b>{p[2]}</b><br>{p[3]}'
        d = ready.get(n)
        st = f'<a class="st" href="{d["file"]}.html">Open notes →</a>' if d else '<span class="st soon">Upcoming</span>'
        if d and d.get('COVERS'):  # the PDF for this class covered different topics from the plan
            topic += f'<span class="cov">📄 This class’s PDF covers: {d["COVERS"]}</span>'
        rows += f'<tr class="{"ready" if d else ""}"><td class="n">Class {n}</td><td>{date}</td><td>{topic}</td><td>{st}</td></tr>'
    other = 'beta' if key == 'alpha' else 'alpha'
    return page_head(f'Banking Awareness {b["name"]}') + f'''
<header class="cover">
  <div class="brand">Current Affairs · Banking Awareness</div>
  <h1>Saarthi {b["name"]} Batch 2026</h1>
  <p class="sub">{b["blurb"]} Classes 10:00–11:30 AM · Ashish Gautam Sir (Adda247, part of Warrior Pro Batch 2026).</p>
  <p class="sub"><b>{len(ready)} of {len(b["plan"])} classes</b> have notes. Green rows are ready; send the next class PDF to add it. See also <a href="../{BATCHES[other]["folder"]}/index.html">Saarthi {BATCHES[other]["name"]}</a>.</p>
</header>
<div class="tw plan"><table><thead><tr><th>Class</th><th>Date</th><th>Topics</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table></div>
</div>
''' + BA_JS + ca.PAGE_JS


def main():
    hp = os.path.join(ROOT, 'index.html')
    hub = open(hp).read()
    for key, b in BATCHES.items():
        classes = sorted((load(p) for p in glob.glob(os.path.join(HERE, 'data', f'{key}-*.py'))), key=lambda d: d['CLASS'])
        out = os.path.join(BA, b['folder'])
        os.makedirs(out, exist_ok=True)
        for i, d in enumerate(classes):
            html = render(d, classes[i - 1] if i else None, classes[i + 1] if i + 1 < len(classes) else None)
            open(os.path.join(out, d['file'] + '.html'), 'w').write(html)
            print(f'wrote {b["folder"]}/{d["file"]}.html ({d["topics"]} topics, {len(d["QUIZ"])} questions)')
        open(os.path.join(out, 'index.html'), 'w').write(overview(key, classes))
        entries = ',\n'.join(f"      ['{d['file']}', 'Class {d['CLASS']} · {d['TITLE']}']" for d in classes)
        hub, n = re.subn(rf'(// ba-{key}:start).*?(\n\s*// ba-{key}:end)', lambda m: m.group(1) + ('\n' + entries if entries else '') + m.group(2), hub, flags=re.S)
        assert n == 1, f'ba-{key} markers missing in hub index.html'
    open(hp, 'w').write(hub)
    print('updated hub sidebar')


if __name__ == '__main__':
    main()

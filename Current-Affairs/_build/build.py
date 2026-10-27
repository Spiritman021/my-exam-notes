"""Builds the Current Affairs class pages from data/*.py.

One data file per class PDF, named YYYY-MM-class-N.py (e.g. 2026-07-class-3.py).
Each defines S (sections), QUIZ and RAPID; use k('…') to mark a key fact.
An optional MCQ list also writes an exam-style mock test page, YYYY-MM-Month-Class-N-Quiz.html (quiz.py).

Run:  python3 Current-Affairs/_build/build.py
Pictures: fetch_images.py (Wikipedia) and/or pdf_images.py (images taken from the class PDF).
Writes Current-Affairs/YYYY-MM-Month-Class-N.html, refreshes the month list on
Current-Affairs/index.html and the Current Affairs entries in the hub (../../index.html).
"""
import os, re, json, glob, calendar
from quiz import render_quiz, minutes

HERE = os.path.dirname(os.path.abspath(__file__))
CA = os.path.dirname(HERE)
ROOT = os.path.dirname(CA)

src = open(os.path.join(ROOT, 'Operating-System', 'index.html')).read()
BASE_HEAD = src[:src.index('</style>')]

EXTRA_CSS = '''
.item{border-top:1px solid var(--line);padding:12px 0 4px}
.item:first-of-type{border-top:0;padding-top:0}
.item h4{margin:0 0 4px;font-size:16.5px}
.item ul{margin:4px 0}
.gk{font-size:13.5px;color:var(--muted);background:var(--surface-2);border:1px solid var(--line);border-radius:4px;padding:6px 10px;margin:6px 0 4px}
.gk b{color:var(--ink)}
.tag{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;border-radius:3px;padding:1px 6px;margin-right:6px;vertical-align:2px}
.tag.bank{color:var(--lec);border:1px solid var(--lec)}
.tag.hot{color:var(--alert);border:1px solid var(--alert)}
.recallbar{position:sticky;top:0;z-index:4;display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--alert);border-radius:6px;padding:10px 14px;margin:16px 0;font-size:14px}
.recallbar button{font:inherit;font-size:13px;background:var(--accent);color:#fff;border:0;border-radius:4px;padding:5px 12px;cursor:pointer}
.recallbar button.ghost{background:none;color:var(--accent);border:1px solid var(--accent)}
.recallbar .hint{color:var(--muted);flex:1;min-width:200px}
html.recall .item b.k{background:var(--surface-2);color:transparent;border-radius:3px;outline:1px dashed var(--muted);cursor:pointer;user-select:none}
html.recall .item b.k.shown{color:inherit;background:var(--accent-soft);outline:0}
.quiz details{border:1px solid var(--line);border-radius:5px;margin:6px 0;background:var(--surface)}
.quiz summary{cursor:pointer;padding:8px 12px;font-weight:550}
.quiz details p{margin:0;padding:0 12px 10px 32px;color:var(--accent);font-weight:600}
.mock{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;justify-content:space-between}
.mock a.go{font-weight:600;background:var(--accent);color:var(--surface);text-decoration:none;border-radius:4px;padding:8px 14px}
.howto ol{margin:6px 0 0}
.item::after{content:"";display:block;clear:both}
.item figure.pic{float:right;width:150px;margin:2px 0 8px 16px;text-align:center}
.item figure.pic img{width:150px;height:110px;object-fit:contain;background:#fff;border:1px solid var(--line);border-radius:6px;padding:4px;display:block}
.item figure.pic figcaption{font-size:11px;letter-spacing:0;text-transform:none;font-weight:500;margin-top:3px;line-height:1.3}
.item figure.pic figcaption a{color:var(--muted);text-decoration:none}
@media (max-width:600px){.item figure.pic{width:110px;margin-left:10px}.item figure.pic img{width:110px;height:84px}}
@media print{.item figure.pic{break-inside:avoid}}
.gt{position:relative;border-bottom:1.5px dotted var(--accent);cursor:help;outline:0}
.gt .pop{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:20;width:270px;max-width:80vw;padding:10px 12px;background:var(--surface);color:var(--ink);border:1px solid var(--line);border-top:3px solid var(--accent);border-radius:6px;box-shadow:0 8px 24px rgba(0,0,0,.18);font-size:13px;font-weight:400;line-height:1.45;text-align:left;letter-spacing:0;text-transform:none;white-space:normal}
.gt .pop::before{content:"";position:absolute;left:0;right:0;top:-10px;height:10px}
.gt:hover .pop,.gt:focus .pop,.gt:focus-within .pop{display:block}
.gt .pop img{float:right;width:64px;height:48px;object-fit:contain;background:#fff;border:1px solid var(--line);border-radius:4px;padding:2px;margin:0 0 4px 8px}
.gt .pop .pt{display:block;color:var(--accent);font-size:13.5px;margin-bottom:2px}
.gt .pop .ps{display:block;color:var(--muted);font-size:12.5px;margin-bottom:4px}
.gt .pop .pl{display:block;clear:both;margin:0;padding:0}
.gt .pop .pi{display:block;position:relative;padding-left:14px;margin:2px 0}
.gt .pop .pi::before{content:"";position:absolute;left:3px;top:.6em;width:5px;height:5px;border-radius:50%;background:var(--accent)}
html.recall .gt .pop{color:var(--ink)}
html.recall b.k:not(.shown) .gt{border-bottom:0}
html.recall b.k:not(.shown) .gt .pop{display:none!important}
@media print{.gt .pop{display:none!important}}
'''

LEGEND = '<div class="legend"><span class="l1">🏦 Banking focus</span><span class="l2">➕ Static GK link</span><span class="l3">⚠️ Exam trap</span><span class="l4">🎯 Likely question</span></div>'
TAGS = {'bank': '<span class="tag bank">🏦 Banking</span>', 'hot': '<span class="tag hot">🎯 Likely Q</span>'}

PAGE_JS = '''<script>
(function(){
  var root=document.documentElement, btn=document.getElementById('themer');
  try{var s=localStorage.getItem('ca-notes-theme'); if(s) root.setAttribute('data-theme',s);}catch(e){}
  btn.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
    var nxt=cur==='dark'?'light':'dark'; root.setAttribute('data-theme',nxt);
    try{localStorage.setItem('ca-notes-theme',nxt);}catch(e){}
  });
  var rb=document.getElementById('recall');
  if(!rb) return;
  // Recall mode: blank out key facts; click one to reveal it.
  function setRecall(on){
    root.classList.toggle('recall',on);
    rb.textContent='Recall mode: '+(on?'on':'off');
    document.querySelectorAll('b.k.shown').forEach(function(b){b.classList.remove('shown');});
  }
  rb.addEventListener('click',function(){ setRecall(!root.classList.contains('recall')); });
  document.getElementById('revealall').addEventListener('click',function(){
    document.querySelectorAll('b.k').forEach(function(b){b.classList.add('shown');});
  });
  document.addEventListener('click',function(e){
    var b=e.target.closest('b.k'); if(b && root.classList.contains('recall')) b.classList.toggle('shown');
  });
})();
</script>
</body>
</html>
'''


def k(s):
    return f'<b class="k">{s}</b>'


def load(path):
    ns = {'k': k, 'S': [], 'QUIZ': [], 'RAPID': [], 'IMG': {}, 'MCQ': []}
    exec(open(path).read(), ns)
    y, m, n = re.match(r'(\d{4})-(\d{2})-class-(\d+)\.py$', os.path.basename(path)).groups()
    month = calendar.month_name[int(m)]
    return dict(S=ns['S'], QUIZ=ns['QUIZ'], RAPID=ns['RAPID'], IMG=ns['IMG'], MCQ=ns['MCQ'], ym=f'{y}-{m}', month=f'{month} {y}',
                cls=int(n), file=f'{y}-{m}-{month}-Class-{n}', topics=sum(len(x[2]) for x in ns['S']))


MANIFEST_PATH = os.path.join(CA, 'img', 'manifest.json')
MANIFEST = json.load(open(MANIFEST_PATH)) if os.path.exists(MANIFEST_PATH) else {}


def img_for(spec):
    return MANIFEST.get(spec) if spec else None


def pic_html(h, img):
    """Memory-aid image for an item: IMG maps a unique part of the headline to a fetched image."""
    for key, spec in img.items():
        m = img_for(spec)
        if key in h and m:
            alt = re.sub('<[^>]+>', '', m.get('page') or spec.replace('File:', '').rsplit('.', 1)[0])
            if m.get('source'):
                cap = f'<a href="{m["source"]}" target="_blank" rel="noopener" title="Wikimedia Commons · {m.get("license", "")}">{alt}</a>'
            else:  # picture taken from the class PDF itself (pdf_images.py)
                cap = f'<span title="From the class PDF">{alt}</span>'
            return (f'<figure class="pic"><img src="img/{m["file"]}" alt="{alt}" loading="lazy">'
                    f'<figcaption>{cap}</figcaption></figure>'), spec
    return '', None


ns_g = {}
exec(open(os.path.join(HERE, 'data', '_glossary.py')).read(), ns_g)
GLOSSARY = ns_g['GLOSSARY']


def hover(term, facts, spec):
    """Hover/tap card with static GK (and a picture when we have one)."""
    m = img_for(spec)
    pic = f'<img src="img/{m["file"]}" alt="">' if m else ''
    inner = re.sub(r'^<span class="pf">(.*)</span>$', r'\1', facts, flags=re.S)
    parts = [x.strip() for x in re.split(r'\s+·\s+', inner) if x.strip()]
    # A leading part without a label/number is the full name: show it under the term, not as a point.
    sub = ''
    if len(parts) > 1 and not re.search(r'<b|\d|:', parts[0]) and not re.match(r'(Est|Founded|HQ|Capital|CM|Under|Launched)\b', parts[0]):
        sub = f'<span class="ps">{parts.pop(0)}</span>'
    pts = '<span class="pl">' + ''.join(f'<span class="pi">{x}</span>' for x in parts) + '</span>'
    return f'<span class="gt" tabindex="0">{term}<span class="pop" role="tooltip">{pic}<b class="pt">{term}</b>{sub}{pts}</span></span>'


def link_terms(html, terms, used):
    """Wrap the first occurrence of each term in a hover card (text only, never inside tags)."""
    if not terms:
        return html
    names = sorted(terms, key=len, reverse=True)
    rx = re.compile(r'(?<![\w-])(' + '|'.join(re.escape(t) for t in names) + r')(?![\w-])')
    out = []
    for part in re.split(r'(<[^>]+>)', html):
        if part.startswith('<'):
            out.append(part)
        else:
            def sub(mo):
                t = mo.group(1)
                if t in used: return t
                used.add(t)
                return hover(t, *terms[t])
            out.append(rx.sub(sub, part))
    return ''.join(out)


def item_html(it, img={}):
    h, tag, facts, gk, trap = it
    pic, spec = pic_html(h, img)
    terms = dict(GLOSSARY)
    # "Name — facts" static GK becomes a hover card on that name (box kept if the name isn't in the text)
    own = re.match(r'(.+?) — (.+)$', gk or '', re.S)
    if own and '<' not in own.group(1):
        terms[own.group(1)] = ('<span class="pf">' + own.group(2) + '</span>', spec)
    used = set()
    head = link_terms(h, terms, used)
    body = ''.join(f'<li>{link_terms(f, terms, used)}</li>' for f in facts)
    out = f'<div class="item">{pic}<h4>{TAGS.get(tag, "")}{head}</h4><ul>{body}</ul>'
    if gk and not (own and own.group(1) in used):
        out += f'<div class="gk">➕ <b>Static GK:</b> {gk}</div>'
    if trap: out += f'<div class="box trap"><span class="t">⚠️ Exam trap</span>{trap}</div>'
    return out + '</div>'


def nav_html(prev, nxt):
    p = f'<a href="{prev["file"]}.html">← Class {prev["cls"]}</a>' if prev else '<span class="off">← Previous class</span>'
    n = f'<a href="{nxt["file"]}.html">Class {nxt["cls"]} →</a>' if nxt else '<span class="off">Next class →</span>'
    return f'<nav class="topnav" aria-label="Class navigation">{p}<a href="index.html">☰ All classes</a>{n}</nav>'


def render(d, prev, nxt):
    secs, toc = '', ''
    for i, (t, intro, items) in enumerate(d['S'], 1):
        toc += f'<li><a href="#c{i}"><span class="n">{i}</span>{t}</a></li>'
        secs += (f'<section id="c{i}"><h3><span class="n">{i}</span>{t}</h3>' + (f'<p class="cs">{intro}</p>' if intro else '')
                 + ''.join(item_html(x, d['IMG']) for x in items) + '</section>\n')
    n = len(d['S']) + 1
    toc += f'<li><a href="#quiz"><span class="n">{n}</span>Self-test ({len(d["QUIZ"])} questions)</a></li>'
    mock = ''
    if d['MCQ']:
        mins = minutes(len(d['MCQ']))
        toc += f'<li><a href="{d["file"]}-Quiz.html" target="_blank" rel="noopener"><span class="n">📝</span>Mock test ({len(d["MCQ"])} MCQs, exam mode)</a></li>'
        mock = (f'<div class="box alert mock"><span><span class="t">📝 Exam-mode mock test</span>{len(d["MCQ"])} MCQs · {mins} minutes · +1 / −0.25 · '
                f'question palette, mark for review and a scorecard with solutions.</span><a class="go" href="{d["file"]}-Quiz.html" target="_blank" rel="noopener">Start mock test ↗</a></div>')
    toc += '<li><a href="#rapid"><span class="n">⚡</span>Rapid Revision</a></li>'
    quiz = (f'<section id="quiz" class="quiz"><h3><span class="n">{n}</span>Self-test</h3>{mock}<p class="cs">Answer out loud first, then click to check. Re-test the ones you missed tomorrow.</p>'
            + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in d['QUIZ']) + '</section>')
    rapid = '<div class="rapid" id="rapid"><h3>⚡ Rapid Revision</h3><ul>' + ''.join(f'<li>{r}</li>' for r in d['RAPID']) + '</ul></div>'
    nav = nav_html(prev, nxt)
    title = f'{d["month"]} · Class {d["cls"]}'
    head = BASE_HEAD.replace('<title>Operating System Notes</title>', f'<title>CA {title}</title>')
    return head + EXTRA_CSS + '''</style>
<script src="../assets/embed.js"></script>
</head>
<body>
<button class="themer" id="themer" type="button">Theme</button>
<div class="wrap">
''' + nav + f'''
<header class="cover">
  <div class="brand">IBPS SO IT · Current Affairs · {d["month"]}</div>
  <h1>Current Affairs — {title}</h1>
  <p class="sub">Class {d["cls"]} of the {d["month"]} monthly series (Ashish Gautam, Adda247) · {d["topics"]} topics, grouped by exam category.</p>
  ''' + LEGEND + '''
</header>
<div class="box lec howto"><span class="t">🎓 How to study this page</span>
<ol>
<li><b>Read once</b> with Recall mode off. Hover over (or tap) any <span style="border-bottom:1.5px dotted var(--accent)">dotted name</span> to see its static GK.</li>
<li><b>Turn Recall mode on</b>: the key facts are hidden. Say each one before you click to reveal it.</li>
<li><b>Take the self-test</b> at the end. Revise again tomorrow, in a week and in a month, using only the Rapid Revision box after that.</li>
</ol></div>
<div class="recallbar"><button id="recall" type="button">Recall mode: off</button><button id="revealall" class="ghost" type="button">Reveal all</button><span class="hint">Hides the key facts. Click any blank to reveal it.</span></div>
<nav class="toc" aria-label="Contents"><h2>Contents</h2><ol>''' + toc + '''</ol></nav>
''' + secs + quiz + rapid + f'''
<p class="end" id="fin">End of {title}</p>
''' + nav + '''
</div>
''' + PAGE_JS


def main():
    classes = sorted((load(p) for p in glob.glob(os.path.join(HERE, 'data', '*-class-*.py'))), key=lambda d: (d['ym'], d['cls']))
    months = {}
    for d in classes:
        months.setdefault(d['ym'], []).append(d)

    for ym, lst in months.items():
        for i, d in enumerate(lst):
            html = render(d, lst[i - 1] if i else None, lst[i + 1] if i + 1 < len(lst) else None)
            open(os.path.join(CA, d['file'] + '.html'), 'w').write(html)
            print('wrote', d['file'] + '.html', f'({d["topics"]} topics, {len(d["QUIZ"])} questions)')
            if d['MCQ']:
                open(os.path.join(CA, d['file'] + '-Quiz.html'), 'w').write(render_quiz(d, BASE_HEAD))
                print('wrote', d['file'] + '-Quiz.html', f'({len(d["MCQ"])} MCQs)')

    # Overview page: one card per month (newest first), classes listed inside.
    cards = ''
    for ym in sorted(months, reverse=True):
        lst = months[ym]
        cards += (f'<details class="card ready" open><summary><span class="cn">{lst[0]["month"]}</span>'
                  f'<span class="ct"><a href="{lst[0]["file"]}.html">Current Affairs — {lst[0]["month"]}</a></span>'
                  f'<span class="cs">{len(lst)} class{"es" if len(lst) > 1 else ""} · {sum(d["topics"] for d in lst)} topics</span></summary><ol class="subs">'
                  + ''.join(f'<li><span class="n">C{d["cls"]}</span><a href="{d["file"]}.html">Class {d["cls"]}</a> — ' + ', '.join(t for t, _, _ in d['S'])
                     + (f' · <a href="{d["file"]}-Quiz.html" target="_blank" rel="noopener">📝 Mock test ↗</a>' if d['MCQ'] else '') + '</li>' for d in lst)
                  + '</ol></details>')
    ip = os.path.join(CA, 'index.html')
    s = open(ip).read()
    s = re.sub(r'(<!-- months:start -->).*?(<!-- months:end -->)', lambda m: m.group(1) + cards + m.group(2), s, flags=re.S)
    open(ip, 'w').write(s)

    # Hub sidebar: newest month first, classes in order within a month.
    hp = os.path.join(ROOT, 'index.html')
    h = open(hp).read()
    order = [d for ym in sorted(months, reverse=True) for d in months[ym]]
    entries = ',\n'.join(f"      ['{d['file']}', '{d['month']} · Class {d['cls']}']" for d in order)
    h, n = re.subn(r'(// ca:start).*?(\n\s*// ca:end)', lambda m: m.group(1) + '\n' + entries + m.group(2), h, flags=re.S)
    assert n == 1, 'ca markers missing in hub index.html'
    open(hp, 'w').write(h)
    print('updated Current-Affairs/index.html and hub sidebar')


if __name__ == '__main__':
    main()

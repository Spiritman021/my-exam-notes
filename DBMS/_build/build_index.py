#!/usr/bin/env python3
"""Rebuild DBMS/index.html from _build/outline.txt.
A chapter card is 'ready' (linked) when its HTML file exists next to index.html.
Run:  python3 -I DBMS/_build/build_index.py"""
import html, os, re
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B)
FILES = ['01-Introduction-to-DBMS', '02-Architecture-and-Schemas', '03-ER-Model', '04-Integrity-Constraints-and-Keys',
 '05-Functional-Dependency', '06-Minimal-Cover-and-Equivalence', '07-Decomposition', '08-Normalization',
 '09-Joins', '10-Relational-Algebra', '11-Relational-Calculus', '12-SQL-Basics-and-DDL',
 '13-SQL-Queries', '14-Indexing', '15-B-Tree-and-B-Plus-Tree', '16-Transactions-and-ACID',
 '17-Concurrency-Problems-and-Recoverability', '18-Serializability', '19-Concurrency-Control-Protocols']
chs = []
for line in open(os.path.join(B,'outline.txt'),encoding='utf-8'):
    m = re.match(r'^(##|###) ([0-9.]+) (.*)', line.strip())
    if not m: continue
    if m.group(1) == '##': chs.append([m.group(3), []])
    else: chs[-1][1].append((m.group(2), m.group(3)))
assert len(chs) == len(FILES)
cards, ready = [], 0
for i,(t,subs) in enumerate(chs):
    f = FILES[i] + '.html'; ok = os.path.exists(os.path.join(D,f)); ready += ok
    e = html.escape
    title = f'<a href="{f}">{e(t)}</a>' if ok else e(t)
    act = f'<a class="open" href="{f}">Open notes →</a>' if ok else '<span class="soon">Coming soon</span>'
    li = ''.join(f'<li><span class="n">{n}</span>{e(s)}</li>' for n,s in subs)
    cards.append(f'<details class="card{" ready" if ok else ""}"{" open" if ok else ""}><summary><span class="cn">Chapter {i+1}</span>'
                 f'<span class="ct">{title}</span><span class="cs">{len(subs)} subtopics · {act}</span></summary><ol class="subs">{li}</ol></details>')
n = len(chs)
status = f'All {n} chapters ready.' if ready == n else f'{ready} of {n} chapters ready.'
head = open(os.path.join(B,'index_head.html'),encoding='utf-8').read()
page = (head + '<body><button class="themer" id="themer" type="button">Theme</button><div class="wrap">\n'
 '<header class="cover"><div class="brand">IBPS SO IT Mains · RRB SO IT · Professional Knowledge</div>\n'
 '<h1>DBMS — Notes Index</h1>\n'
 f'<p class="sub">Volume 05 · {n} chapters from the one-shot DBMS lecture, plus exam additions. {status}</p>\n'
 '<div class="legend"><span class="l1">🎓 From the lecture</span><span class="l2">➕ Added for exam</span><span class="l3">⚠️ Exam trap</span><span class="l4">🎯 IBPS exam alert</span></div>\n'
 '<p style="margin-top:12px;font-size:14px"><a href="../Software-Engineering/index.html">← Software Engineering notes</a></p></header>\n'
 + ''.join(cards) + '</div><script>\n(function(){\n  var root=document.documentElement, btn=document.getElementById(\'themer\');\n'
 "  try{var s=localStorage.getItem('notes-theme'); if(s) root.setAttribute('data-theme',s);}catch(e){}\n"
 "  btn.addEventListener('click',function(){\n    var cur=root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');\n"
 "    var nxt=cur==='dark'?'light':'dark'; root.setAttribute('data-theme',nxt);\n    try{localStorage.setItem('notes-theme',nxt);}catch(e){}\n  });\n})();\n</script>\n</body>\n</html>\n")
open(os.path.join(D,'index.html'),'w',encoding='utf-8').write(page)
print(status)

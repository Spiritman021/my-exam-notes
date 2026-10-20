#!/usr/bin/env python3
"""Publish one DS chapter.
Usage: python3 -I Data-Structures/_build/publish.py NN SLUG "Title" "<title> text" PREV_SLUG BODY_FILE
BODY_FILE = the chapter from <body> to </html>; it is joined to _build/chapter_head.html.
Links the previous chapter's "Next chapter coming soon", adds the hub SUBJECTS entry (id 'ds'),
rebuilds index.html.
Notes live only in ~/Desktop/my-notes (no copy in ~/Downloads)."""
import sys, os, re, subprocess, html
num, slug, title, short, prev, body = sys.argv[1:7]
B = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(B); R = os.path.dirname(D)
head = open(B+'/chapter_head.html',encoding='utf-8').read()
head = re.sub(r'<title>.*?</title>', f'<title>{short}</title>', head, count=1)
open(f'{D}/{slug}.html','w',encoding='utf-8').write(head + open(body,encoding='utf-8').read())
p = f'{D}/{prev}.html'; s = open(p,encoding='utf-8').read()
off = '<span class="off">Next chapter coming soon</span>'
print('prev links replaced:', s.count(off))
s = s.replace(off, f'<a href="{slug}.html">Ch {int(num)}: {html.escape(title)} →</a>'); open(p,'w',encoding='utf-8').write(s)
hp = R + '/index.html'; h = open(hp,encoding='utf-8').read()
m = re.search(r"(id: 'ds'.*?chapters: \[\n)(.*?)(\n    \])", h, re.S)
if slug not in m.group(2):
    h = h[:m.end(2)] + f",\n      ['{slug}', '{title.replace(chr(39), chr(92)+chr(39))}']" + h[m.end(2):]
    open(hp,'w',encoding='utf-8').write(h); print('hub: added')
print(subprocess.run(['python3','-I',B+'/build_index.py'],capture_output=True,text=True).stdout.strip())

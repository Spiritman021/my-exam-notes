"""Downloads memory-aid images from Wikipedia/Wikimedia Commons for the Current Affairs pages.

Each data file may define IMG = {'unique part of an item headline': 'Wikipedia page title' | 'File:Name.ext'}.
For a page title the article's logo is preferred (organisations), otherwise its lead image.
Images are cached in Current-Affairs/img/ and listed in img/manifest.json, which build.py reads,
so building works offline. Re-run only when IMG entries change.

Run:  python3 Current-Affairs/_build/fetch_images.py
"""
import os, re, json, glob, time, hashlib, subprocess, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(os.path.dirname(HERE), 'img')
MANIFEST = os.path.join(IMG_DIR, 'manifest.json')
API = 'https://en.wikipedia.org/w/api.php'
UA = {'User-Agent': 'my-notes-study/1.0 (personal study notes)'}
WIDTH = 360


def get(url, tries=5):
    # curl uses the system trust store (python.org builds of Python often lack CA certs on macOS).
    # Wikimedia drops connections when requests come too fast, so pace and retry.
    for n in range(tries):
        time.sleep(1 + 3 * n)
        r = subprocess.run(['curl', '-sSfL', '-m', '30', '-A', UA['User-Agent'], url], capture_output=True)
        if r.returncode == 0:
            return r.stdout
    raise RuntimeError(f'curl exit {r.returncode}: {r.stderr.decode().strip()[:120]}')


def api(**params):
    params.update(format='json', formatversion='2')
    return json.loads(get(API + '?' + urllib.parse.urlencode(params)))


def file_info(fname):
    d = api(action='query', titles=fname, prop='imageinfo', iiprop='url|extmetadata', iiurlwidth=WIDTH)
    page = d['query']['pages'][0]
    if 'imageinfo' not in page:
        return None
    ii = page['imageinfo'][0]
    meta = ii.get('extmetadata', {})
    lic = re.sub('<[^>]+>', '', meta.get('LicenseShortName', {}).get('value', '')).strip()
    return {'url': ii.get('thumburl') or ii['url'], 'desc': ii['descriptionurl'], 'license': lic}


def resolve(spec):
    """Return (file title, wiki page title or None)."""
    if spec.startswith('File:'):
        return spec, None
    d = api(action='query', titles=spec, redirects=1, prop='pageimages|images', piprop='name', pilicense='any', imlimit='max')
    page = d['query']['pages'][0]
    if page.get('missing'):
        raise LookupError(f'no Wikipedia page "{spec}"')
    images = [i['title'] for i in page.get('images', [])]
    # A logo only counts if its file name shares a word with the article (avoids picking a sister org's or a site logo).
    words = {w for w in re.findall(r'[a-z]{3,}', page['title'].lower()) if w not in {'the', 'and', 'india', 'indian', 'of'}}
    acronym = ''.join(w[0] for w in re.findall(r'[A-Za-z]+', page['title']) if w[0].isupper()).lower()
    def matches(t):
        name = t.lower()
        return any(w in name for w in words) or (len(acronym) > 2 and acronym in name)
    logos = [t for t in images if re.search(r'logo', t, re.I) and matches(t)
             and not re.search(r'commons|wiki|openstreetmap|edit|icon|flag_of', t, re.I)]
    if logos:
        return logos[0], page['title']
    if page.get('pageimage'):
        return 'File:' + page['pageimage'], page['title']
    raise LookupError(f'no image on "{spec}"')


def specs():
    out = {}
    for p in sorted(glob.glob(os.path.join(HERE, 'data', '*-class-*.py'))):
        ns = {'k': lambda s: s, 'S': [], 'QUIZ': [], 'RAPID': [], 'IMG': {}}
        exec(open(p).read(), ns)
        out.update({v: None for v in ns['IMG'].values()})
    g = {}
    exec(open(os.path.join(HERE, 'data', '_glossary.py')).read(), g)
    out.update({spec: None for _, spec in g['GLOSSARY'].values() if spec})
    return list(out)


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    for spec in specs():
        if spec in manifest and os.path.exists(os.path.join(IMG_DIR, manifest[spec]['file'])):
            continue
        try:
            fname, page = resolve(spec)
            info = file_info(fname)
            if not info:
                raise LookupError(f'no file info for {fname}')
            ext = os.path.splitext(urllib.parse.urlparse(info['url']).path)[1].lower() or '.jpg'
            if ext == '.svg':
                ext = '.png'  # thumburl of an SVG is a PNG render
            local = re.sub(r'[^a-z0-9]+', '-', spec.lower()).strip('-')[:50] + '-' + hashlib.md5(spec.encode()).hexdigest()[:6] + ext
            open(os.path.join(IMG_DIR, local), 'wb').write(get(info['url']))
            manifest[spec] = {'file': local, 'source': info['desc'], 'license': info['license'],
                              'page': page, 'image': fname}
            print('ok  ', spec, '->', fname)
        except Exception as e:
            print('FAIL', spec, '-', e)
    json.dump(manifest, open(MANIFEST, 'w'), indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main()

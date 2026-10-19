"""Uses pictures embedded in the class PDF itself as the memory-aid images.

In a data file, an IMG value of the form 'pdf:pNN_MM|Caption' refers to the MM-th image on page NN
of that class's PDF (names as printed by: swift pdf_extract.swift <pdf> <outdir> <lastpage>).
This script extracts the PDF's images, copies the referenced ones into Current-Affairs/img/
and records them in img/manifest.json, so build.py shows them like any other picture.

Run:  python3 Current-Affairs/_build/pdf_images.py <class.pdf> <data/YYYY-MM-class-N.py>
"""
import os, re, sys, json, glob, shutil, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(os.path.dirname(HERE), 'img')
MANIFEST = os.path.join(IMG_DIR, 'manifest.json')


def main(pdf, data):
    ns = {'k': lambda s: s, 'S': [], 'QUIZ': [], 'RAPID': [], 'IMG': {}}
    exec(open(data).read(), ns)
    wanted = {v for v in ns['IMG'].values() if v.startswith('pdf:')}
    if not wanted:
        print('no pdf: images in', data); return
    tag = os.path.basename(data)[:-3]                      # e.g. 2026-08-class-4
    last = max(int(re.match(r'pdf:p(\d+)_', v).group(1)) for v in wanted)
    tmp = tempfile.mkdtemp()
    subprocess.run(['swift', os.path.join(HERE, 'pdf_extract.swift'), pdf, tmp, str(last)],
                   check=True, capture_output=True)
    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    for spec in sorted(wanted):
        ref, caption = (spec[4:].split('|', 1) + [''])[:2]
        hits = glob.glob(os.path.join(tmp, ref + '_*'))
        if not hits:
            print('FAIL', spec, '- not found in PDF'); continue
        src = hits[0]
        if src.endswith(('.ppm', '.pgm')):                  # raw samples → PNG
            png = src.rsplit('.', 1)[0] + '.png'
            subprocess.run(['sips', '-s', 'format', 'png', src, '--out', png], check=True, capture_output=True)
            src = png
        local = f'{tag}-{ref.replace("_", "-")}{os.path.splitext(src)[1]}'
        shutil.copy(src, os.path.join(IMG_DIR, local))
        manifest[spec] = {'file': local, 'source': '', 'license': 'from the class PDF', 'page': caption or None,
                          'image': os.path.basename(pdf)}
        print('ok  ', spec, '->', local)
    json.dump(manifest, open(MANIFEST, 'w'), indent=1, ensure_ascii=False)
    shutil.rmtree(tmp)


if __name__ == '__main__':
    main(*sys.argv[1:3])

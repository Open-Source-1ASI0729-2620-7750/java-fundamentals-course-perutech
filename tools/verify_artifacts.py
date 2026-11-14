"""Verifica solo artefactos públicos; los reportes de participación quedan en local."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unicodedata
import zipfile

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
NAME = 'upc-pre-202620-1asi0729-7750-perutech-course-plan.pdf'


def words(text):
    return Counter(re.findall(r'\w+', unicodedata.normalize('NFKC', text).replace('\u00ad', '').casefold()))


def main():
    links = []
    for name in ['README.md', 'course-plan.md', 'tools/README.md', 'verification/entrega-checklist.md']:
        source = ROOT / name
        for target in re.findall(r'\]\(([^)]+)\)', source.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://')): continue
            assert (source.parent / target.split('#')[0]).resolve().exists(), f'Enlace roto: {name} -> {target}'
            links.append({'file': name, 'target': target})
    pdf = ROOT / 'deliverables' / NAME
    reader = PdfReader(pdf, strict=True)
    text = '\n'.join(p.extract_text() or '' for p in reader.pages)
    assert all(len((p.extract_text() or '').strip()) > 70 for p in reader.pages)
    uris = []
    for page in reader.pages:
        for ref in page.get('/Annots', []):
            uri = ref.get_object().get('/A', {}).get('/URI')
            if uri: uris.append(str(uri))
    plan = (ROOT / 'course-plan.md').read_text(encoding='utf-8')
    visible = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', plan)
    visible = re.sub(r'^```.*$', '', visible, flags=re.M)
    assert not (words(visible) - words(text)), 'Contenido del plan ausente del PDF'
    prefix = 'https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech/blob/docs/entrega-trabajo-complementario/'
    expected = [prefix + u[2:] if u.startswith('./') else u for u in re.findall(r'\]\(([^)]+)\)', plan)]
    assert set(expected).issubset(uris), 'Faltan enlaces clicables'
    zip_path = ROOT / 'deliverables/perutech-java-fundamentals-artifacts.zip'
    with zipfile.ZipFile(zip_path) as archive:
        assert archive.testzip() is None
        entries = archive.namelist()
        assert len(entries) == 23
        assert all(n in ['README.md','course-plan.md'] or n.startswith(('starter-files/','completed-examples/','scripts/')) for n in entries)
        assert not any(re.search(r'performance|participant|\.docx$|\.class$|\.pyc$|(^|/)(\.git|\.idea|node_modules|__pycache__)/', n, re.I) for n in entries)
        for name in entries: assert archive.read(name) == (ROOT / name).read_bytes(), f'ZIP desactualizado: {name}'
    java = json.loads((ROOT / 'verification/java-results.json').read_text(encoding='utf-8'))
    for row in java['results']:
        assert hashlib.sha256((ROOT / row['file']).read_bytes()).hexdigest() == row['sha256']
    assert {p.name for p in (ROOT / 'deliverables').iterdir()} == {NAME, zip_path.name}, 'Los reportes locales no deben publicarse'
    results = {'prepared_date':'2026-11-14', 'plan_pdf_pages':len(reader.pages), 'plan_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(), 'plan_content_complete':True, 'clickable_links':len(uris), 'local_links':links, 'java_files_verified':len(java['results']), 'zip_files':len(entries), 'zip_integrity':True, 'participation_reports_included':False}
    (ROOT / 'verification/artifact-results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in results.items() if k != 'local_links'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

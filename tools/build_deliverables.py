"""Genera solo el plan PDF público y el ZIP desde las fuentes del curso."""
import hashlib
import json
from pathlib import Path
import re
import zipfile
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted, LongTable, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'deliverables'
PREFIX = 'upc-pre-202620-1asi0729-7750-perutech-course-plan'
REPO_URL = 'https://github.com/Open-Source-1ASI0729-2620-7750/java-fundamentals-course-perutech'
BRANCH = 'docs/entrega-trabajo-complementario'



def register_fonts():
    fonts = Path('C:/Windows/Fonts')
    if (fonts / 'arial.ttf').exists():
        for name, filename in [('Body', 'arial.ttf'), ('Body-Bold', 'arialbd.ttf'), ('Body-Italic', 'ariali.ttf'), ('Body-BoldItalic', 'arialbi.ttf'), ('Code', 'consola.ttf')]:
            pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
        pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body-Italic', boldItalic='Body-BoldItalic')
        return 'Body', 'Body-Bold', 'Code'
    return 'Helvetica', 'Helvetica-Bold', 'Courier'


def inline(text):
    tokens = []
    def preserve(value):
        tokens.append(value)
        return f'ZZTOKEN{len(tokens)-1}ZZ'
    def link(match):
        label, url = match.groups()
        if url.startswith('./'):
            url = REPO_URL + '/blob/' + BRANCH + '/' + url[2:]
        return preserve(f'<link href="{escape(url, {chr(34): "&quot;"})}" color="#205a85">{escape(label)}</link>')
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, text)
    text = escape(text)
    text = re.sub(r'`([^`]+)`', r'<font name="CODEFONT">\1</font>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    for index, value in enumerate(tokens):
        text = text.replace(f'ZZTOKEN{index}ZZ', value)
    return text


def build_plan():
    body, bold, code = register_fonts()
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CourseBody', fontName=body, fontSize=10.5, leading=15, spaceAfter=7, splitLongWords=True))
    styles.add(ParagraphStyle(name='CourseBullet', parent=styles['CourseBody'], leftIndent=11, firstLineIndent=-8, spaceAfter=5))
    styles.add(ParagraphStyle(name='CourseCell', parent=styles['CourseBody'], fontSize=9, leading=12, spaceAfter=0))
    for level, size in [(1, 21), (2, 15), (3, 12.5), (4, 11)]:
        styles.add(ParagraphStyle(name=f'CourseH{level}', fontName=bold, fontSize=size, leading=size+4, textColor=colors.black, spaceBefore=14, spaceAfter=8, keepWithNext=True))
    styles.add(ParagraphStyle(name='CourseCover', fontName=bold, fontSize=26, leading=33, spaceAfter=20))
    styles.add(ParagraphStyle(name='CourseCode', fontName=code, fontSize=9.5, leading=13, spaceAfter=9, leftIndent=10))
    def p(text, style='CourseBody'):
        return Paragraph(inline(text).replace('CODEFONT', code), styles[style])
    story = [Spacer(1, 65), p('Fundamentos de Java para principiantes', 'CourseCover'), p('Plan del curso | PeruTech'), Spacer(1, 26), p('Universidad Peruana de Ciencias Aplicadas (UPC)'), p('1ASI0729 - Desarrollo de Aplicaciones Open Source'), p('Ciclo 202620 · NRC 7750'), p('Preparación: 14/11/2026'), Spacer(1, 30), p('Curso para estudiantes de secundaria de 12 a 17 años. Prácticas desde el navegador, sin instalación de programas.'), p('Incluye la secuencia, objetivos, videos, código y ejercicios del documento course-plan.md.'), PageBreak()]
    lines = (ROOT / 'course-plan.md').read_text(encoding='utf-8').splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line or line == '---':
            index += 1
            continue
        if line.startswith('```'):
            block = []
            index += 1
            while index < len(lines) and not lines[index].startswith('```'):
                block.append(lines[index]); index += 1
            story.append(Preformatted('\n'.join(block), styles['CourseCode']))
        elif line.startswith('|'):
            rows = []
            while index < len(lines) and lines[index].strip().startswith('|'):
                cells = [s.strip() for s in lines[index].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append([p(cell, 'CourseCell') for cell in cells])
                index += 1
            table = LongTable(rows, colWidths=[64, 175, 265], repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND', (0,0),(-1,0),colors.HexColor('#eeeeee')), ('VALIGN',(0,0),(-1,-1),'TOP'), ('BOTTOMPADDING',(0,0),(-1,-1),8), ('TOPPADDING',(0,0),(-1,-1),8), ('LEFTPADDING',(0,0),(-1,-1),7), ('RIGHTPADDING',(0,0),(-1,-1),7), ('LINEBELOW',(0,0),(-1,0),0.5,colors.HexColor('#999999')), ('LINEBELOW',(0,1),(-1,-1),0.25,colors.HexColor('#dddddd'))]))
            story.extend([table, Spacer(1,10)])
            continue
        elif line.startswith('#'):
            match = re.match(r'(#{1,4})\s+(.*)', line)
            story.append(p(match[2], f'CourseH{len(match[1])}'))
        elif re.match(r'^\d+\. ', line):
            story.append(p(line, 'CourseBullet'))
        elif line.startswith(('* ', '- ')):
            story.append(p('• ' + line[2:], 'CourseBullet'))
        else:
            text = [line]
            while index + 1 < len(lines) and lines[index+1].strip() and not re.match(r'^(#|\* |\- |\||```|\d+\. )', lines[index+1].strip()):
                index += 1; text.append(lines[index].strip())
            story.append(p(' '.join(text)))
        index += 1
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont(body, 8)
        canvas.setFillColor(colors.HexColor('#555555'))
        canvas.drawString(54, 30, 'PeruTech | UPC | 1ASI0729 | NRC 7750')
        canvas.drawRightString(letter[0]-54, 30, str(doc.page))
        canvas.restoreState()
    target = OUT / (PREFIX + '.pdf')
    SimpleDocTemplate(str(target), pagesize=letter, rightMargin=54, leftMargin=54, topMargin=48, bottomMargin=49, title='Fundamentos de Java para principiantes - Plan del curso', author='PeruTech').build(story, onFirstPage=footer, onLaterPages=footer)








def build_zip():
    target = OUT / 'perutech-java-fundamentals-artifacts.zip'
    paths = [ROOT / 'README.md', ROOT / 'course-plan.md']
    for folder in ['starter-files', 'completed-examples', 'scripts']:
        paths.extend(sorted((ROOT / folder).rglob('*')))
    files = [path for path in paths if path.is_file() and path.suffix in {'.java', '.md'}]
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in files: archive.write(path, path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {p.relative_to(ROOT).as_posix() for p in files}
        for path in files:
            assert archive.read(path.relative_to(ROOT).as_posix()) == path.read_bytes()
    hashes = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    (ROOT / 'verification/zip-manifest.json').write_text(json.dumps(hashes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('ZIP:', len(files), 'archivos verificados')



if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    build_plan()
    build_zip()
    print('Generados: plan PDF público y ZIP. Los reportes de participación quedan exclusivamente en local.')

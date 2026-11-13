#!/usr/bin/env python3
"""
Genera documento Word (.docx) del Pasaporte del Proyecto ED Park en RUSO
desde el archivo Markdown en ruso.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
import re

# Leer el archivo markdown en ruso
with open('05_01_Pasaporte_Proyecto_RU.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Crear documento Word
doc = Document()

# Configurar estilos por defecto
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.15

# Configurar márgenes
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

def add_heading_styled(doc, text, level):
    """Añade encabezado con estilo personalizado"""
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.color.rgb = RGBColor(0, 51, 102)  # Azul oscuro
        run.font.name = 'Calibri'
    return heading

def parse_table(md_table):
    """Convierte tabla markdown a lista de filas"""
    lines = md_table.strip().split('\n')
    rows = []
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells and not all(re.match(r'^[-:\s]+$', c) for c in cells):
                rows.append(cells)
    return rows

def add_table_from_md(doc, md_table):
    """Añade tabla desde markdown al documento"""
    rows = parse_table(md_table)
    if not rows:
        return
    
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    for i, row_data in enumerate(rows):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            # Negrita en header
            if i == 0:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True
                        run.font.size = Pt(10)
            else:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(10)
    return table

# Procesar el contenido markdown línea por línea
lines = md_content.split('\n')
i = 0
in_table = False
table_lines = []

while i < len(lines):
    line = lines[i]
    
    # Detectar tablas
    if line.strip().startswith('|') and line.strip().endswith('|'):
        table_lines.append(line)
        in_table = True
        i += 1
        continue
    
    if in_table and (not line.strip().startswith('|') or i == len(lines) - 1):
        # Procesar tabla acumulada
        if table_lines:
            add_table_from_md(doc, '\n'.join(table_lines))
        table_lines = []
        in_table = False
        continue
    
    # Encabezados
    if line.startswith('# '):
        add_heading_styled(doc, line[2:].strip(), 0)
    elif line.startswith('## '):
        add_heading_styled(doc, line[3:].strip(), 1)
    elif line.startswith('### '):
        add_heading_styled(doc, line[4:].strip(), 2)
    elif line.startswith('#### '):
        add_heading_styled(doc, line[5:].strip(), 3)
    
    # Línea horizontal
    elif line.strip() == '---':
        doc.add_paragraph('').paragraph_format.space_before = Pt(12)
        doc.add_paragraph('').paragraph_format.space_after = Pt(12)
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(12)
        run = p.add_run('━' * 80)
        run.font.color.rgb = RGBColor(0, 51, 102)
        run.font.size = Pt(8)
    
    # Texto normal
    elif line.strip() and not line.strip().startswith('```'):
        p = doc.add_paragraph()
        
        # Procesar negrita y cursiva
        parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', line)
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                run = p.add_run(part[2:-2])
                run.bold = True
            elif part.startswith('*') and part.endswith('*'):
                run = p.add_run(part[1:-1])
                run.italic = True
            else:
                run = p.add_run(part)
            run.font.size = Pt(11)
    
    # Bloques de código (Mermaid, etc.) - ignorar
    elif line.strip().startswith('```'):
        i += 1
        while i < len(lines) and not lines[i].strip().startswith('```'):
            i += 1
    
    i += 1

# Procesar última tabla si existe
if table_lines:
    add_table_from_md(doc, '\n'.join(table_lines))

# Guardar documento
output_path = '05_01_Pasaporte_Proyecto_RU.docx'
doc.save(output_path)
print(f"Documento generado: {output_path}")
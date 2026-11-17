#!/usr/bin/env python3
"""
Genera archivo Excel con todos los recursos del proyecto ED Park en RUSO.
Incluye: personal, equipos, subcontratistas y presupuesto total.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Crear workbook
wb = Workbook()

# Estilos comunes
title_font = Font(name='Calibri', size=14, bold=True, color='FFFFFF')
title_fill = PatternFill(start_color='003366', end_color='003366', fill_type='solid')
header_font = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
header_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
section_font = Font(name='Calibri', size=12, bold=True, color='003366')
cell_font = Font(name='Calibri', size=10)
total_font = Font(name='Calibri', size=11, bold=True, color='003366')
total_fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')

thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)

center_al = Alignment(horizontal='center', vertical='center', wrap_text=True)
left_al = Alignment(horizontal='left', vertical='center', wrap_text=True)

def add_title_sheet(ws, title, subtitle):
    ws.merge_cells('A1:E1')
    c = ws['A1']
    c.value = title
    c.font = title_font
    c.fill = title_fill
    c.alignment = center_al
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:E2')
    c = ws['A2']
    c.value = subtitle
    c.font = Font(name='Calibri', size=10, italic=True, color='FFFFFF')
    c.fill = title_fill
    c.alignment = center_al
    ws.row_dimensions[2].height = 18

def add_header_row(ws, row_num, headers, col_start=1):
    for j, h in enumerate(headers):
        c = ws.cell(row=row_num, column=col_start+j, value=h)
        c.font = header_font
        c.fill = header_fill
        c.alignment = center_al
        c.border = thin_border

def add_data_rows(ws, start_row, data, col_start=1, currency_cols=None):
    if currency_cols is None:
        currency_cols = []
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            c = ws.cell(row=start_row+i, column=col_start+j, value=val)
            c.font = cell_font
            c.border = thin_border
            if j == 0:
                c.alignment = left_al
            elif j in currency_cols:
                c.number_format = '#,##0 ₽'
                c.alignment = center_al
            else:
                c.alignment = center_al

def add_total_row(ws, row_num, label, values, col_start=1, currency_cols=None):
    if currency_cols is None:
        currency_cols = []
    c = ws.cell(row=row_num, column=col_start, value=label)
    c.font = total_font
    c.fill = total_fill
    c.border = thin_border
    c.alignment = left_al
    
    for j, val in enumerate(values):
        c = ws.cell(row=row_num, column=col_start+j+1, value=val)
        c.font = total_font
        c.fill = total_fill
        c.border = thin_border
        if j in currency_cols:
            c.number_format = '#,##0 ₽'
        c.alignment = center_al

def autofit_columns(ws, min_width=12, max_width=50):
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            try:
                if cell.value:
                    max_len = max(max_len, len(str(cell.value)))
            except:
                pass
        ws.column_dimensions[col_letter].width = min(max(max_len+2, min_width), max_width)

# ============================================================
# HOJA 1: PERSONAL (HR)
# ============================================================
ws1 = wb.active
ws1.title = "1. Персонал"

add_title_sheet(ws1, "РЕСУРСЫ — ПЕРСОНАЛ (HR)", "Проект ED Park — Парк логистики, Матансас, Куба")

headers = ["Роль", "Количество", "Функция", "Фаза назначения", "Стоимость в месяц (₽)", "Стоимость в месяц итого (₽)"]
add_header_row(ws1, 4, headers, col_start=1)

personal_data = [
    ["Руководитель проекта", 1, "Управление проектом, стейкхолдеры, отчеты", "Все фазы", 180000, 180000],
    ["Архитектор", 1, "Архитектурное проектирование ангаров и офисов", "Фаза 1.2", 150000, 150000],
    ["Инженер конструкций", 1, "Расчет конструкций, фундамент", "Фаза 1.2", 140000, 140000],
    ["Инженер по системам строительства", 1, "Электрика, HVAC, противопожарная защита", "Фаза 1.2, 1.4", 140000, 140000],
    ["Инженер-градостроитель", 1, "Причалы, дворик, покрытия", "Фаза 1.2, 1.4", 130000, 130000],
    ["Инженер по логистике", 1, "Проектирование стеллажей, зон хранения, AGV", "Фаза 1.2, 1.4", 130000, 130000],
    ["Координатор безопасности", 1, "Паспорт безопасности, нормативы", "Фаза 1.2", 120000, 120000],
    ["Административный менеджер", 1, "Оформление лицензий и разрешений", "Фаза 1.2", 100000, 100000],
    ["Закупки", 1, "Закупка оборудования и материалов", "Фаза 1.3", 110000, 110000],
    ["Разработчик ПО (WMS)", 3, "Разработка и внедрение WMS", "Фаза 1.3", 160000, 480000],
    ["Консультант WMS", 1, "Настройка и валидация WMS", "Фаза 1.3, 1.5", 170000, 170000],
    ["Инженер по системам", 1, "Сеть и коммуникации, видеонаблюдение", "Фаза 1.3, 1.4", 150000, 150000],
    ["Поставщик систем безопасности", 1, "Видеонаблюдение и контроль доступа", "Фаза 1.3", 140000, 140000],
    ["Монтажник стеллажей", 2, "Установка стеллажей и зон хранения", "Фаза 1.4", 90000, 180000],
    ["Строитель", 3, "Строительство, монтаж офисов", "Фаза 1.4", 100000, 300000],
    ["Электрик", 2, "Электрические установки, зона зарядки AGV", "Фаза 1.4", 110000, 220000],
    ["Уполномоченный монтажник", 1, "Технические установки (HVAC, противопожарная)", "Фаза 1.4", 130000, 130000],
    ["Поставщик AGV", 1, "Установка и испытания AGV/AMR", "Фаза 1.4, 1.5", 180000, 180000],
    ["Тренер", 1, "Обучение операционного персонала", "Фаза 1.6", 120000, 120000],
    ["Отдел кадров", 1, "Найм, обучение, зарплата", "Все фазы", 100000, 100000],
    ["Директор по операциям", 1, "Запуск производства, реальные операции", "Фаза 1.6", 200000, 200000],
]

add_data_rows(ws1, 5, personal_data, col_start=1, currency_cols=[4, 5])

row_total = 5 + len(personal_data)
add_total_row(ws1, row_total, "ВСЕГО персонал", [27, "", "", "", "", 3450000], currency_cols=[5])
row_total2 = row_total + 1
ws1.cell(row=row_total2, column=1, value="Месячная стоимость персонала:").font = cell_font
ws1.cell(row=row_total2, column=6, value=3450000).number_format = '#,##0 ₽'
ws1.cell(row=row_total2, column=6).font = cell_font
row_total3 = row_total2 + 1
ws1.cell(row=row_total3, column=1, value="Общая стоимость персонала (18 месяцев):").font = cell_font
ws1.cell(row=row_total3, column=6, value=62100000).number_format = '#,##0 ₽'
ws1.cell(row=row_total3, column=6).font = total_font

autofit_columns(ws1)

# ============================================================
# HOJA 2: ОБОРУДОВАНИЕ
# ============================================================
ws2 = wb.create_sheet("2. Оборудование")

add_title_sheet(ws2, "РЕСУРСЫ — ОБОРУДОВАНИЕ И МАТЕРИАЛЫ", "Проект ED Park — Парк логистики, Матансас, Куба")

headers2 = ["Категория", "Позиция", "Количество", "Цена за единицу (₽)", "Общая стоимость (₽)", "Фаза"]
add_header_row(ws2, 4, headers2, col_start=1)

equipment_data = [
    ["Стеллажи", "Селективные порта-паллеты (зона A)", 240, 45000, 10800000, "1.3.1"],
    ["Стеллажи", "Динамические стеллажи FIFO (зона C)", 40, 55000, 2200000, "1.3.1"],
    ["Стеллажи", "Консольные стеллажи", 20, 60000, 1200000, "1.3.1"],
    ["Транспорт", "Ретрактные вилочные погрузчики", 2, 1200000, 2400000, "1.3.2"],
    ["Транспорт", "Вилочные погрузчики с противовесом", 1, 1000000, 1000000, "1.3.2"],
    ["Транспорт", "Штабелеры", 1, 800000, 800000, "1.3.2"],
    ["Транспорт", "Электрические рохли", 4, 315000, 1260000, "1.3.2"],
    ["Транспорт", "AGV/AMR", 6, 3500000, 21000000, "1.3.2"],
    ["Оборудование", "Конвейеры", 3, 550000, 1650000, "1.3.2"],
    ["Оборудование", "Стационарные считыватели RFID", 6, 150000, 900000, "1.3.2"],
    ["Оборудование", "Портативные терминалы RFID", 6, 80000, 480000, "1.3.2"],
    ["Оборудование", "Сканеры штрих-кодов", 10, 42400, 424000, "1.3.2"],
    ["Оборудование", "Платформенные весы 3000 кг", 2, 90000, 180000, "1.3.2"],
    ["Оборудование", "Настольные весы 30 кг", 1, 38000, 38000, "1.3.2"],
    ["Оборудование", "Датчики IoT температуры/влажности", 30, 4000, 120000, "1.3.2"],
    ["Оборудование", "Датчики IoT присутствия", 20, 5000, 100000, "1.3.2"],
    ["Оборудование", "Датчики IoT пожарной сигнализации", 20, 6000, 120000, "1.3.2"],
    ["Оборудование", "Датчики IoT дверей", 6, 7000, 42000, "1.3.2"],
    ["Серверы", "SRV-01 WMS", 1, 850000, 850000, "1.3.5"],
    ["Серверы", "SRV-02 AGV/SCADA", 1, 850000, 850000, "1.3.5"],
    ["Серверы", "SRV-03 резерв", 1, 775000, 775000, "1.3.5"],
    ["Оборудование", "Промышленный ИБП / СБИ", 2, 200000, 400000, "1.3.5"],
    ["Кондиционирование", "Блоки точного кондиционирования зона B", 2, 250000, 500000, "1.3.2"],
    ["Кондиционирование", "Блоки ангаров", 2, 200000, 400000, "1.3.2"],
    ["Кондиционирование", "Блок управления", 1, 180000, 180000, "1.3.2"],
    ["Кондиционирование", "Блок офиса", 1, 160000, 160000, "1.3.2"],
    ["Оборудование", "Принтеры этикеток RFID+штрих-код", 4, 55000, 220000, "1.3.2"],
    ["Оборудование", "IP-камеры внутренние", 8, 30000, 240000, "1.3.5"],
    ["Оборудование", "IP-камеры PTZ наружные", 4, 61000, 244000, "1.3.5"],
    ["Оборудование", "ПЛК причалы", 2, 80000, 160000, "1.3.2"],
    ["Оборудование", "ПЛК конвейеры", 1, 80000, 80000, "1.3.2"],
    ["Оборудование", "ПЛК кондиционирование", 1, 70000, 70000, "1.3.2"],
    ["Мебель", "Столы и стулья офиса", 1, 600000, 600000, "1.3.6"],
    ["Мебель", "Компьютерное оборудование офиса", 1, 800000, 800000, "1.3.6"],
]

add_data_rows(ws2, 5, equipment_data, col_start=1, currency_cols=[3, 4, 5])

row_total = 5 + len(equipment_data)
add_total_row(ws2, row_total, "ИТОГО оборудование и материалы", ["", "", "", "", 52967000, ""], currency_cols=[4])

autofit_columns(ws2)

# ============================================================
# HOJA 3: СУБПОДРЯДЧИКИ
# ============================================================
ws3 = wb.create_sheet("3. Субподрядчики")

add_title_sheet(ws3, "РЕСУРСЫ — СУБПОДРЯДЧИКИ", "Проект ED Park — Парк логистики, Матансас, Куба")

headers3 = ["Субподрядчик", "Объем работ", "Длительность", "Месяц начала", "Стоимость (₽)"]
add_header_row(ws3, 4, headers3, col_start=1)

subcontractor_data = [
    ["Строительная компания", "Фундамент, металлоконструкции, обшивка ангаров", 6, "Месяц 7", 15000000],
    ["Электрик/кондиционер", "Электрические установки, кондиционирование, противопожарная защита", 5, "Месяц 9", 8000000],
    ["Поставщик AGV", "Установка, настройка и испытания 6 AGV/AMR", 3, "Месяц 13", 6000000],
    ["Компания безопасности", "Установка видеонаблюдения и контроля доступа", 3, "Месяц 10", 4000000],
]

add_data_rows(ws3, 5, subcontractor_data, col_start=1, currency_cols=[4])

row_total = 5 + len(subcontractor_data)
add_total_row(ws3, row_total, "ИТОГО субподрядчики", ["", "", "", "", 33000000], currency_cols=[4])

autofit_columns(ws3)

# ============================================================
# HOJA 4: БЮДЖЕТ
# ============================================================
ws4 = wb.create_sheet("4. Бюджет")

add_title_sheet(ws4, "БЮДЖЕТ — СВОДКА ПО КАТЕГОРИЯМ", "Проект ED Park — Парк логистики, Матансас, Куба")

headers4 = ["Категория", "Базовая стоимость (₽)", "% от общей"]
add_header_row(ws4, 4, headers4, col_start=1)

budget_data = [
    ["Персонал (18 месяцев)", 62100000, 69.0],
    ["Оборудование и материалы", 52967000, 58.8],
    ["ОБЩАЯ БАЗОВАЯ СТОИМОСТЬ", 90000000, 100.0],
    ["Резерв рисков (30%)", 27000000, 30.0],
    ["ОБЩАЯ ЦЕНА ПРОЕКТА", 117000000, 130.0],
]

add_data_rows(ws4, 5, budget_data, col_start=1, currency_cols=[1])

row_total = 5 + len(budget_data)
for i in range(row_total):
    ws4.cell(row=row_total+i, column=1).font = total_font
    ws4.cell(row=row_total+i, column=2).font = total_font
    ws4.cell(row=row_total+i, column=3).font = total_font

autofit_columns(ws4)

# ============================================================
# HOJA 5: ВАРИАНТЫ
# ============================================================
ws5 = wb.create_sheet("5. Варианты")

add_title_sheet(ws5, "СРАВНЕНИЕ ВАРИАНТОВ ДЛЯ ЗАКАЗЧИКА", "Проект ED Park — Парк логистики, Матансас, Куба")

headers5 = ["Вариант", "Базовая стоимость (₽)", "Резерв рисков (30%)", "Общая цена (₽)"]
add_header_row(ws5, 4, headers5, col_start=1)

variants_data = [
    ["Базовый", 67500000, 20250000, 87750000],
    ["Средний (рекомендуемый)", 90000000, 27000000, 117000000],
    ["Полный", 112500000, 33750000, 146250000],
]

add_data_rows(ws5, 5, variants_data, col_start=1, currency_cols=[1, 2, 3])

# Выделить рекомендуемый вариант
for cell in ws5[6]:
    cell.font = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
    cell.fill = PatternFill(start_color='C00000', end_color='C00000', fill_type='solid')
    cell.border = thin_border

autofit_columns(ws5)

# Сохранить
output_path = "05_04_Ресурсы_И_Бюджет_ED_Park_RU.xlsx"
wb.save(output_path)
print(f"Excel-файл сгенерирован: {output_path}")
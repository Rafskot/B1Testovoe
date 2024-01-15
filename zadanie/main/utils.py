import xlrd
from .models import BalanceSheet, EndClass, EndTable, Class

def process_excel_data(excel_file):
    workbook = xlrd.open_workbook(file_contents=excel_file.read())
    sheet = workbook.sheet_by_index(0)

    # ... Ваш существующий код по обработке данных ...

    # Пример вставки данных в модель Django
    balance_sheet_data = {'value_1': 1.0, 'value_2': 2.0, 'value_3': 3.0, 'value_4': 4.0, 'value_5': 5.0, 'value_6': 6.0, 'value_7': 7.0, 'class_id': 1}
    balance_sheet_instance = BalanceSheet(**balance_sheet_data)
    balance_sheet_instance.save()
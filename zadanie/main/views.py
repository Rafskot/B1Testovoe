from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, EndClass, EndTable, BalanceSheet
import xlrd
import os


def upload_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        # Открываем файл Excel
        workbook = xlrd.open_workbook(file_contents=excel_file.read())
        sheet = workbook.sheet_by_index(0)

        # Проходим по каждой строке, начиная с 10 строки, и считываем 7 колонок
        row_index = 8  # Начинаем с 10 строки
        class_id = 0
        while row_index < sheet.nrows:
            types_list = [sheet.cell_type(row_index, col_index) for col_index in range(sheet.ncols)]

            if types_list == [1, 0, 0, 0, 0, 0, 0]:
                try:
                    new_class = Class.objects.create(name=sheet.cell_value(row_index, 0))
                    class_id = new_class.id
                except Exception as e:
                    print(f"Error creating new class: {e}")
            elif sheet.cell_value(row_index, 0) == "БАЛАНС":
                try:
                    EndTable.objects.create(
                        value_1=sheet.cell_value(row_index, 0),
                        value_2=sheet.cell_value(row_index, 1),
                        value_3=sheet.cell_value(row_index, 2),
                        value_4=sheet.cell_value(row_index, 3),
                        value_5=sheet.cell_value(row_index, 4),
                        value_6=sheet.cell_value(row_index, 5),
                        value_7=sheet.cell_value(row_index, 6),
                    )
                    class_id = 0  # сброс class_id, так как строка с "БАЛАНС" не имеет связанного класса
                    break  # Завершаем цикл после обработки строки с "БАЛАНС"
                except Exception as e:
                    print(f"Error inserting data into the EndTable: {e}")
            else:
                # Основная проверка, если все значения в строке являются числами (Type - 1 или Type - 2)
                # Преобразуем строки в float, пропуская некорректные значения
                values = []
                for col_index in range(sheet.ncols):
                    try:
                        value = float(sheet.cell_value(row_index, col_index))
                        values.append(value)
                    except ValueError:
                        print(
                            f"Skipping invalid value at Row {row_index + 1}, Column {col_index + 1}: {sheet.cell_value(row_index, col_index)}")
                        try:
                            EndClass.objects.create(
                                value_1=sheet.cell_value(row_index, 0),
                                value_2=sheet.cell_value(row_index, 1),
                                value_3=sheet.cell_value(row_index, 2),
                                value_4=sheet.cell_value(row_index, 3),
                                value_5=sheet.cell_value(row_index, 4),
                                value_6=sheet.cell_value(row_index, 5),
                                value_7=sheet.cell_value(row_index, 6),
                                class_id=class_id
                            )
                        except Exception as e:
                            print(f"Error inserting data into the EndClass table: {e}")

                # Если все значения успешно преобразованы, записываем их в базу данных
                if len(values) == sheet.ncols:
                    try:
                        BalanceSheet.objects.create(
                            value_1=values[0],
                            value_2=values[1],
                            value_3=values[2],
                            value_4=values[3],
                            value_5=values[4],
                            value_6=values[5],
                            value_7=values[6],
                            class_id=class_id
                        )
                    except Exception as e:
                        print(f"Error inserting data into the BalanceSheet table: {e}")

            row_index += 1

        return HttpResponse("Data uploaded successfully!")

    return render(request, 'main/upload_excel.html')


def display_data(request):
    # Получите данные из моделей Django
    balance_sheets = BalanceSheet.objects.all()
    end_classes = EndClass.objects.all()
    end_tables = EndTable.objects.all()
    classes = Class.objects.all()

    # Передайте данные в контекст для отображения в шаблоне
    context = {
        'balance_sheets': balance_sheets,
        'end_classes': end_classes,
        'end_tables': end_tables,
        'classes': classes,
    }

    # Отображение шаблона с данными
    return render(request, 'main/display.html', context)


def save_to_file(request):
    try:
        # Сохранение данных в файл "output.txt" внутри папки 'zadanie'
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_file_path = os.path.join(project_dir, 'zadanie', 'output.txt')

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Получаем уникальные class_id из BalanceSheet
            unique_class_ids = BalanceSheet.objects.values_list('class_id', flat=True).distinct()

            # Перебираем уникальные class_id
            for class_id in unique_class_ids:
                # Получаем имя из модели Class для текущего class_id
                class_name = Class.objects.get(id=class_id).name
                output_file.write(f"{class_name}\n")

                # Записываем данные из BalanceSheet для текущего class_id
                for balance_sheet in BalanceSheet.objects.filter(class_id=class_id):
                    output_file.write(
                        f"{balance_sheet.value_1}, {balance_sheet.value_2}, {balance_sheet.value_3}, {balance_sheet.value_4}, {balance_sheet.value_5}, {balance_sheet.value_6}, {balance_sheet.value_7}, {balance_sheet.class_id}\n")

                # Добавляем строки из EndClass для текущего class_id
                for end_class in EndClass.objects.filter(class_id=class_id):
                    output_file.write(
                        f"{end_class.value_1}, {end_class.value_2}, {end_class.value_3}, {end_class.value_4}, {end_class.value_5}, {end_class.value_6}, {end_class.value_7}, {end_class.class_id}\n")

                # Добавляем строки из EndTable для текущего class_id
                for end_table in EndTable.objects.all():
                    output_file.write(
                        f"{end_table.value_1}, {end_table.value_2}, {end_table.value_3}, {end_table.value_4}, {end_table.value_5}, {end_table.value_6}, {end_table.value_7}\n")
        print(f"File saved to: {output_file_path}")

        return HttpResponse(f"Data saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving data: {e}")
        return HttpResponse(f"Error: {e}")

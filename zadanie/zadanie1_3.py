import sqlite3


def merge_and_insert(input_files, db_file, pattern_to_insert):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Обновленный запрос CREATE TABLE для нового формата
    cursor.execute('''CREATE TABLE IF NOT EXISTS merged_data (
                        date TEXT, 
                        latin_chars TEXT, 
                        russian_chars TEXT, 
                        even_integer INTEGER, 
                        positive_float REAL)''')

    total_imported_lines = 0

    for input_file in input_files:
        imported_lines = 0
        remaining_lines = 0

        with open(input_file, 'r') as file:
            lines = file.readlines()

            # Вставка строк в базу данных, основываясь на шаблоне
            for line in lines:
                values = [val.strip() for val in line.strip().split("||") if val.strip()]
                if len(values) == 5 and pattern_to_insert in line:
                    date, latin_chars, russian_chars, even_integer, positive_float = values
                    cursor.execute("INSERT INTO merged_data VALUES (?, ?, ?, ?, ?)",
                                   (date, latin_chars, russian_chars, even_integer, positive_float))
                    imported_lines += 1
                else:
                    remaining_lines += 1

        print(f"Импортировано из файла {input_file}: {imported_lines} строк. Осталось {remaining_lines} строк.")
        total_imported_lines += imported_lines

    print(f"\nОбщее количество импортированных строк: {total_imported_lines}\n")

    conn.commit()
    conn.close()


# Пример использования с генерацией имен файлов
input_files = [f"file_{i}.txt" for i in range(1, 101)]
merge_and_insert(input_files, "merged_data.db", "abc")

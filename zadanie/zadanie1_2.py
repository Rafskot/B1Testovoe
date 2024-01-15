def merge_and_remove(input_files, output_file, pattern_to_remove):
    total_deleted_lines = 0

    with open(output_file, 'w') as output:
        for input_file in input_files:
            with open(input_file, 'r') as file:
                lines = file.readlines()

                # Удаление строк с заданным сочетанием символов
                deleted_lines = [line for line in lines if pattern_to_remove not in line]
                total_deleted_lines += len(lines) - len(deleted_lines)

                # Запись оставшихся строк в объединенный файл
                output.writelines(deleted_lines)

    print(f"Общее количество удаленных строк: {total_deleted_lines}")


# Пример использования с генерацией имен файлов
input_files = [f"file_{i}.txt" for i in range(1, 101)]
merge_and_remove(input_files, "merged_file.txt", "abc")

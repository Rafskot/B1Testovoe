import sqlite3
import statistics


def calculate_sum_and_median():
    conn = sqlite3.connect("merged_data.db")
    cursor = conn.cursor()

    # Вычисление суммы всех целых чисел
    cursor.execute("SELECT SUM(even_integer) FROM merged_data")
    sum_integer = cursor.fetchone()[0]

    # Вычисление медианы всех дробных чисел
    cursor.execute("SELECT positive_float FROM merged_data")
    float_values = [row[0] for row in cursor.fetchall()]
    median_real = statistics.median(float_values)

    conn.close()

    return sum_integer, median_real


# Вызов функции и вывод результатов
sum_result, median_result = calculate_sum_and_median()
print(f"Сумма всех целых чисел (столбец even_integer): {sum_result}")
print(f"Медиана всех дробных чисел (столбец positive_float): {median_result}")

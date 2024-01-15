import random
import datetime


def generate_random_date():
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=5 * 365)
    random_date = start_date + datetime.timedelta(days=random.randint(0, 5 * 365))
    return random_date.strftime("%d.%m.%Y")


def generate_random_string(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(length))


def generate_random_russian_string(length):
    russian_alphabet = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return ''.join(random.choice(list(russian_alphabet)) for _ in range(length))


def generate_random_positive_even_integer():
    return random.randint(1, 50000000) * 2


def generate_random_positive_float():
    return round(random.uniform(1, 20), 8)


def generate_random_line():
    return f"{generate_random_date()}||{generate_random_string(10)}||{generate_random_russian_string(10)}||{generate_random_positive_even_integer()}||{generate_random_positive_float()}||"


def generate_text_file(file_number):
    with open(f"file_{file_number}.txt", 'w') as file:
        for _ in range(100000):
            file.write(generate_random_line() + '\n')


# Генерация 100 текстовых файлов
for i in range(1, 101):
    generate_text_file(i)

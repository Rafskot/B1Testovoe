# Тестовое задание для B1  
## Часть 1  
Использовался ЯП Python, для связи с бд использовалась встроенная sqlite3
### Часть 1.1  
Запустив эту часть кода, Сгенерировать 100 текстовых файлов со следующей структурой, каждый из которых содержит 100 000 строк:  
случайная дата за последние 5 лет || случайный набор 10 латинских символов ||случайный набор 10 русских символов || случайное положительное четноецелочисленное число в диапазоне от 1 до 100 000 000 || случайное положительноечисло с 8 знаками после запятой вдиапазоне от 1 до 20.
### Часть 1.2  
Данный код запускать только после запуска 1.1. Удаляет строки попавшие под шаблон, в каждом из 100 файлов и оставшиеся обьединяет в 1 файл merged_file.txt  
Шаблон можно поменять на 1 строчке merge_and_remove(input_files, "merged_file.txt", "abc") за место abc можно написать любуюу другую последовательность.
### Часть 1.3  
Данный код запускать лучше запускать при обновленном наборе файлов. Создает процедуру импорта файлов с таким набором полей в таблицу в СУБД. При импорте выводится ход процесса (сколько строк импортировано, сколько осталось).  
### Часть 1.4  
Данный код считаетсумму всех целых чисел и медиану всех дробных чисел находящихся в бд
## Часть 2
Использовался ЯП Python, фреймворк Django, для связи с бд использовалась встроенная sqlite3  
1)Для запуска необоходимо создать проект, устанавливаем Django pip install django  
2)Создайте новый проект Django с помощью команды: django-admin startproject myproject  
3)Перейдите в каталог вашего проекта: cd myproject  
4)Создайте django приложение: python manage.py startapp main   
5)Добавьте это приложение в settings.py:  
INSTALLED_APPS = [
    'main',
6)изменить файл urls.py в проекте myproject на  
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]   
7)В проект main скопировать файлы:view.py,models.py,form.py, util.py, forms.py из папки zadadnie\main  
8)Создать в проект main новую директорию templates, в ней создать еще одну директорию main, и скопировать туда файлы html  
9)Примените миграции для создания базы данных: 1)python manage.py makemigrations 2)python manage.py migrate  
10) Запустите сервер разработки Django: python manage.py runserver  
### Часть 2.1  
### Часть 2.2  
1) Перейдите на страницу http://127.0.0.1:8000/  
2) Выберите ecxel файл и нажмите принять   
В директории появится заполненный файл базы данных при его заполнении в отладке будет выписыватся процесс загрузки  
3) Перейдите на страницу http://127.0.0.1:8000/display/ на ней представлено отображение данных из СУБД по визуальной аналогии с exсel-файлом для каждого  
из загруженных файлов  
### Часть 2.3  
Реализовано сохранение данных с web-сервера в файл, при переходе на страницу  http://127.0.0.1:8000/save у вас в директории в папке, где находится файл settings.py появится output.txt, в котором находится данные взятые с web-сервера  

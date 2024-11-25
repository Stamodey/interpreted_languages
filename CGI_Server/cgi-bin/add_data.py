import cgi
import sqlite3

print("Content-Type: text/html\n")  # Заголовок ответа

# Обработка данных из формы
form = cgi.FieldStorage()
name = form.getvalue("name")
description = form.getvalue("description")

# Добавление данных в базу
try:
    conn = sqlite3.connect("architecture.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO styles (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    print("<h1>Стиль успешно добавлен!</h1>")
    print('<a href="/templates/index.html">Вернуться к форме</a>')
except Exception as e:
    print(f"<h1>Ошибка: {e}</h1>")

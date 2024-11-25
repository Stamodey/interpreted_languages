import sqlite3

def fill_data():
    conn = sqlite3.connect('architecture.db')
    cursor = conn.cursor()

    # Заполнение таблицы стилей
    styles = [
        ("Готика", "Стиль с высокими башнями и витражами."),
        ("Барокко", "Роскошный стиль с деталями."),
        ("Модерн", "Современные формы и линии."),
        ("Хай-тек", "Современные технологии и материалы.")
    ]
    cursor.executemany("INSERT INTO styles (name, description) VALUES (?, ?)", styles)

    # Заполнение таблицы зданий
    buildings = [
        ("Кельнский собор", 1248, 1),
        ("Версаль", 1661, 2),
        ("Сиднейская опера", 1973, 3),
        ("Башня Шард", 2012, 4)
    ]
    cursor.executemany("INSERT INTO buildings (name, year_built, style_id) VALUES (?, ?, ?)", buildings)

    # Заполнение таблицы архитекторов
    architects = [
        ("Арнольд Вольф", 1800, 1),
        ("Жюль Ардуэн-Мансар", 1646, 2),
        ("Йорн Утзон", 1918, 3),
        ("Ренцо Пиано", 1937, 4)
    ]
    cursor.executemany("INSERT INTO architects (name, birth_year, building_id) VALUES (?, ?, ?)", architects)

    # Заполнение таблицы материалов
    materials = [
        ("Камень", "Природный", 1),
        ("Мрамор", "Природный", 2),
        ("Бетон", "Искусственный", 3),
        ("Стекло", "Искусственный", 4),
        ("Сталь", "Искусственный", 4)
    ]
    cursor.executemany("INSERT INTO materials (name, type, building_id) VALUES (?, ?, ?)", materials)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    fill_data()

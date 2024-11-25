import sqlite3

DB_PATH = "D:/универ/lab10-11/architecture.db"

def get_all_styles():
    """Вывести все архитектурные стили."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM styles")
    rows = cursor.fetchall()

    print("Архитектурные стили:")
    for row in rows:
        print(row)

    conn.close()

def get_buildings_by_style(style_name):
    """Получить здания определённого архитектурного стиля."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT b.name AS building_name, b.year_built, s.name AS style_name
    FROM buildings b
    JOIN styles s ON b.style_id = s.id
    WHERE s.name = ?
    """
    cursor.execute(query, (style_name,))
    rows = cursor.fetchall()

    print(f"Здания в стиле {style_name}:")
    for row in rows:
        print(row)

    conn.close()

def get_materials_by_building():
    """Получить материалы, использованные в каждом здании."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT m.name AS material_name, m.type, b.name AS building_name
    FROM materials m
    JOIN buildings b ON m.building_id = b.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("Материалы по зданиям:")
    for row in rows:
        print(row)

    conn.close()

def get_most_popular_material():
    """Получить самый популярный материал."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT m.name AS material_name, COUNT(*) AS usage_count
    FROM materials m
    GROUP BY m.name
    ORDER BY usage_count DESC
    LIMIT 1
    """
    cursor.execute(query)
    row = cursor.fetchone()

    print("Самый популярный материал:")
    print(row)

    conn.close()

if __name__ == "__main__":

    # Выполнение запросов
    get_all_styles()
    get_buildings_by_style("Готика")
    get_materials_by_building()
    get_most_popular_material()

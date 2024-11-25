import sqlite3

def create_database():
    conn = sqlite3.connect('architecture.db')
    cursor = conn.cursor()

    # Таблица архитектурных стилей
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS styles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
    """)

    # Таблица зданий
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buildings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year_built INTEGER,
        style_id INTEGER,
        FOREIGN KEY (style_id) REFERENCES styles (id)
    )
    """)

    # Таблица архитекторов
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS architects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER,
        building_id INTEGER,
        FOREIGN KEY (building_id) REFERENCES buildings (id)
    )
    """)

    # Таблица материалов
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT,
        building_id INTEGER,
        FOREIGN KEY (building_id) REFERENCES buildings (id)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()

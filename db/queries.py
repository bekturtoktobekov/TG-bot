import sqlite3
from pathlib import Path

def init_db():
    db_path = Path(__file__).parent.parent/'db.sqlite'
    global db, cursor
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            engine_disp TEXT,
            price INTEGER,
            image TEXT
            );
    ''')
    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS
    # ''')
    # db.commit()

def get_categories():
    cursor.execute('''
    SELECT DISTINCT brand, model, engine_disp, price, image FROM categories''')
    show_data = cursor.fetchall()
    text = ''
    for row in show_data:
        text += ' '.join(map(str, row)) + '\n'
    return text


def populate_table():
    cursor.execute('''
    INSERT INTO categories (brand, model ,engine_disp, price, image) VALUES 
    ('Mercedes', 'W210', 5.5, 20000, 'https://avatars.mds.yandex.net/get-verba/787013/2a000001609d133bf37f94a60fc7a946809b/cattouch'),
    ('Toyota','4runner', 4.0, 40000, 'https://www.portlandautoshow.com/wp-content/uploads/2022/12/Toyota-4Runner-TRD-Pro-2023.jpg'),
    ('Toyota', 'Prius', 1.8, 15000, 'https://cdn.motor1.com/images/mgl/ZnkYYA/s1/2022-toyota-prius-xle-nightshade-exterior-front-quarter.jpg'),
    ('Toyota', 'Sienna', 3.5, 50000, 'https://s.auto.drom.ru/i24202/c/photos/fullsize/toyota/sienna/toyota_sienna_638226.jpg')
    ''')

    db.commit()
def create_table():
    db

if __name__ == '__main__':
    init_db()
    create_table()
    populate_table()
    print(get_categories())
#primary key = уникальный идентификатор, первичный ключ
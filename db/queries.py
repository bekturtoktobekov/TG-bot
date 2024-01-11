import sqlite3
from pathlib import Path

def init_db():
    db_path = Path(__file__).parent.parent/'db.sqlite'
    global db, cursor
    db = sqlite3.connect(db_path)
    cursor = db.cursor()

def create_table():
    cursor.execute('''
        DROP TABLE IF EXISTS categories
        ''')

    cursor.execute('''
        DROP TABLE IF EXISTS cars
        ''')

    cursor.execute('''
        DROP TABLE IF EXISTS flats
        ''')

    cursor.execute('''
        DROP TABLE IF EXISTS user
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            engine_disp TEXT,
            price INTEGER,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flats(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            address TEXT,
            builder TEXT,
            flat_area INTEGER,
            flat_num_rooms INTEGER,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        user_name TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        car_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(user_id),
        FOREIGN KEY (car_id) REFERENCES cars(id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parser(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        address TEXT,
        price TEXT,
        description TEXT
        );
        ''')
    db.commit()


# def create_order(user_id: str, item_id: int, item_type: str):
#     query = '''
#         INSERT INTO orders (user_id, {0}_id) VALUES (?, ?)
#     '''.format(item_type.lower())
#     cursor.execute(query, (user_id, item_id))
#     db.commit()

# def get_cars():
#     cursor.execute('''
#     SELECT DISTINCT brand, model, engine_disp, price, image FROM cars
#     JOIN categories ON cars.category_id = categories.id''')
#     show_data = cursor.fetchall()
#     text = ''
#     for row in show_data:
#         text += ' '.join(map(str, row)) + '\n'
#     return text

def get_cars_id(id: int):
    cursor.execute('SELECT * FROM cars WHERE id = ?', (id,))
    car_data = cursor.fetchall()
    for car in car_data:
        print(car)
    return car_data

# def get_flats():
#     cursor.execute('''
#     SELECT DISTINCT flat_area, flat_num_rooms FROM flats
#     JOIN categories ON flats.category_id = categories.id''')
#     show_data = cursor.fetchall()
#     text = ''
#     for row in show_data:
#         text += ' '.join(map(str, row)) + '\n'
#     return text

def get_flats_id(id: int):
    cursor.execute('SELECT * FROM flats WHERE id = 1', (id,))
    flat_data = cursor.fetchone()
    return flat_data

def populate_table():
    cursor.execute('''
    INSERT INTO categories (name) VALUES
    ('Cars'),
    ('Flats')
    ''')


    cursor.execute('''
    INSERT INTO cars (brand, model ,engine_disp, price, image, category_id) VALUES 
    ('Mercedes', 'W210', 5.5, 20000, 'https://avatars.mds.yandex.net/get-verba/787013/2a000001609d133bf37f94a60fc7a946809b/cattouch', 1),
    ('Toyota','4runner', 4.0, 40000, 'https://www.portlandautoshow.com/wp-content/uploads/2022/12/Toyota-4Runner-TRD-Pro-2023.jpg', 1),
    ('Toyota', 'Prius', 1.8, 15000, 'https://cdn.motor1.com/images/mgl/ZnkYYA/s1/2022-toyota-prius-xle-nightshade-exterior-front-quarter.jpg', 1),
    ('Toyota', 'Sienna', 3.5, 50000, 'https://s.auto.drom.ru/i24202/c/photos/fullsize/toyota/sienna/toyota_sienna_638226.jpg', 1)
    ''')


    cursor.execute('''
    INSERT INTO flats (address, builder, flat_area, flat_num_rooms, image, category_id) VALUES 
    ('Asanbay', 'Avangard', 100, 3,'https://www.udr.com/globalassets/corporate/homepage/homepage_2_essexluxe.jpg', 2),
    ('Alamedin', 'Alpha stroy' , 50, 2,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSePaHmDdWgLzxWPUNymshmKKr7n01DfW9M2eHG23HNWSjt_xsw2Pnefk33JkXo14lykcg&usqp=CAU', 2),
    ('10th microdistrict', 'USSR', 70, 2,'https://fastrack-waterfront-apartments.imgix.net/uploads/waterfront1009-1-copy-1--1.jpg?auto=format&fit=max&h=800&ixlib=php-2.1.1&q=80&s=6b90119a864d53ef1bd3d3f68b319a32', 2)
    ''')

def get_categories():
    cursor.execute('SELECT * FROM categories')
    category_data = cursor.fetchall()
    return category_data


def get_cars_by_category(category_id: int):
    cursor.execute('SELECT * FROM cars WHERE category_id = ?', (category_id,))
    cars_data = cursor.fetchall()
    return cars_data


def get_flats_by_category(category_id: int):
    cursor.execute('SELECT * FROM flats WHERE category_id = ?', (category_id,))
    flats_data = cursor.fetchall()
    return flats_data

def parser_db(data):
    cursor.execute('''
            INSERT INTO parser (title, address, price, description)
            VALUES (?, ?, ?, ?)
        ''', (data['title'], data['address'], data['price'], data['description']))
    db.commit()

def get_parser():
    cursor.execute('SELECT * FROM parser')
    parsed_data = cursor.fetchall()
    return parsed_data

# async def buy_button(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup(
#         inline_keyboard=[
#             [types.InlineKeyboardButton(text='В корзину', callback_data='basket')]
#         ])
#     await message.answer(reply_markup=keyboard)

if __name__ == '__main__':
    init_db()
    create_table()
    populate_table()
    # print(get_cars())
    categories = get_categories()
    for category in categories:
        # print(f"Category: {category}")

        cars = get_cars_by_category(category[0])
        print("Cars:")
        for car in cars:
            print(car)

        flats = get_flats_by_category(category[0])
        print("Flats:")
        for flat in flats:
            print(flat)


#primary key = уникальный идентификатор, первичный ключ
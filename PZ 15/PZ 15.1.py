import sqlite3
from typing import List, Dict, Tuple

# Функция для создания БД и таблицы
def init_db() -> None:
    """Инициализирует базу данных и создает таблицу 'Товары'"""
    with sqlite3.connect('wholesale_base.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Товары (
                код_товара INTEGER PRIMARY KEY AUTOINCREMENT,
                наименование_товара TEXT NOT NULL,
                наименование_магазина TEXT NOT NULL,
                заявки_магазина TEXT,
                количество_на_складе REAL NOT NULL,
                единицы_измерения TEXT NOT NULL,
                оптовая_цена REAL NOT NULL
            )
        ''')
        conn.commit()

# Функциональные операции с товарами
def add_product(product: Dict) -> None:
    """Добавляет товар в базу (функциональный стиль)"""
    with sqlite3.connect('wholesale_base.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Товары VALUES (
                NULL, :наименование_товара, :наименование_магазина,
                :заявки_магазина, :количество_на_складе,
                :единицы_измерения, :оптовая_цена
            )
        ''', product)
        conn.commit()

def get_all_products() -> List[Tuple]:
    """Получает все товары (чистая функция)"""
    with sqlite3.connect('wholesale_base.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Товары')
        return cursor.fetchall()

def update_stock(code: int, new_quantity: float) -> None:
    """Обновляет количество товара (функциональный подход)"""
    with sqlite3.connect('wholesale_base.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Товары 
            SET количество_на_складе = ?
            WHERE код_товара = ?
        ''', (new_quantity, code))
        conn.commit()

# Пример использования (функциональный стиль)
if __name__ == '__main__':
    # Инициализация БД
    init_db()

    # Добавление товаров (без изменяемого состояния)
    products = [
        {
            'наименование_товара': 'Молоко "Домик в деревне"',
            'наименование_магазина': 'Продукты 24/7',
            'заявки_магазина': 'Заявка №45 от 01.06.2023',
            'количество_на_складе': 150,
            'единицы_измерения': 'литры',
            'оптовая_цена': 55.99
        },
        {
            'наименование_товара': 'Хлеб "Бородинский"',
            'наименование_магазина': 'У дома',
            'заявки_магазина': 'Заявка №12 от 02.06.2023',
            'количество_на_складе': 200,
            'единицы_измерения': 'штуки',
            'оптовая_цена': 32.50
        }
    ]

    # Применяем функцию add_product к каждому товару
    list(map(add_product, products))

    # Получаем и выводим все товары
    print("Список всех товаров:")
    for product in get_all_products():
        print(product)

    # Обновляем количество (пример)
    update_stock(1, 135)
    print("\nПосле обновления количества:")
    print(get_all_products()[0])
import sqlite3

def create_db():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT DEFAULT "",
            image TEXT DEFAULT ""         
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, price, description="", image=""):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO products 
        (name, price, description, image)
        VALUES (?, ?, ?, ?)
    ''', (name, price, description, image))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    conn.close()
    return products

def get_product_by_id(product_id):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()

    conn.close()
    if product:
        return {
            "name": product[1],
            "price": product[2],
            "description": product[3],
            "image": product[4]
        }
    else:
        return None

if __name__ == "__main__":
    create_db()
    add_product("test product", 9.89, "opisanie", "static/uploads/product1.png")
    add_product("test product2", 19.29, "opisanie2", "static/uploads/product2.jpg")
    print(get_products())



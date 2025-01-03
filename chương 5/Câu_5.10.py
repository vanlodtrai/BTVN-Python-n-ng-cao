import sqlite3


conn = sqlite3.connect("product.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
""")


def add_product(name, price, amount):
    cursor.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    print("Sản phẩm đã được thêm thành công!")


def display_products():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    print("Danh sách sản phẩm:")
    for row in rows:
        print(row)


def search_product(name):
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    print("Kết quả tìm kiếm:")
    for row in rows:
        print(row)


def delete_product(product_id):
    cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
    conn.commit()
    print("Sản phẩm đã được xóa!")


add_product("Laptop", 1500.0, 10)
add_product("Mouse", 20.0, 50)
display_products()
search_product("Laptop")
delete_product(1)
display_products()

conn.close()

import sqlite3

# Kết nối với cơ sở dữ liệu (tạo mới nếu chưa tồn tại)
connection = sqlite3.connect("product.db")
cursor = connection.cursor()

# Tạo bảng product
cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')
connection.commit()

def display_products():
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    print("Danh sách sản phẩm:")
    for product in products:
        print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
def add_product(name, price, amount):
    cursor.execute('''
    INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)
    ''', (name, price, amount))
    connection.commit()
    print(f"Sản phẩm '{name}' đã được thêm thành công.")
def search_product(name):
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", ('%' + name + '%',))
    products = cursor.fetchall()
    if products:
        print("Kết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        print("Không tìm thấy sản phẩm nào.")
def update_product(product_id, new_price, new_amount):
    cursor.execute('''
    UPDATE product SET Price = ?, Amount = ? WHERE Id = ?
    ''', (new_price, new_amount, product_id))
    connection.commit()
    print(f"Sản phẩm ID {product_id} đã được cập nhật.")
def delete_product(product_id):
    cursor.execute('''
    DELETE FROM product WHERE Id = ?
    ''', (product_id,))
    connection.commit()
    print(f"Sản phẩm ID {product_id} đã bị xóa.")

def main_menu():
    while True:
        print("\n--- Quản Lý Sản Phẩm ---")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm: "))
            amount = int(input("Nhập số lượng sản phẩm: "))
            add_product(name, price, amount)
        elif choice == '3':
            name = input("Nhập tên sản phẩm cần tìm: ")
            search_product(name)
        elif choice == '4':
            product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
            new_price = float(input("Nhập giá mới: "))
            new_amount = int(input("Nhập số lượng mới: "))
            update_product(product_id, new_price, new_amount)
        elif choice == '5':
            product_id = int(input("Nhập ID sản phẩm cần xóa: "))
            delete_product(product_id)
        elif choice == '6':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()

# Đóng kết nối khi thoát
connection.close()

import sqlite3

conn = sqlite3.connect("my_database.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()
conn.close()
print("Cơ sở dữ liệu và bảng đã được tạo thành công!")

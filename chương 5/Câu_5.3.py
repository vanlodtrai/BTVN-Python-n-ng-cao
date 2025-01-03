import sqlite3

conn = sqlite3.connect("example_database.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL
);
""")

cursor.execute("INSERT INTO employees (name, position, salary) VALUES ('Mai', 'Kỹ sư', 1200.5);")
cursor.execute("INSERT INTO employees (name, position, salary) VALUES ('Phong', 'Quản lý', 2000);")

conn.commit()


cursor.execute("SELECT * FROM employees;")
rows = cursor.fetchall()

print("Dữ liệu trong bảng employees:")
for row in rows:
    print(row)

conn.close()

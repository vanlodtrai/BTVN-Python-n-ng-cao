import sqlite3


conn = sqlite3.connect(":memory:")


cursor = conn.cursor()

cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);")

cursor.execute("INSERT INTO students (name, age) VALUES ('An', 20);")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bình', 21);")


cursor.execute("SELECT * FROM students;")
rows = cursor.fetchall()


print("Dữ liệu trong bảng students:")
for row in rows:
    print(row)


conn.close()

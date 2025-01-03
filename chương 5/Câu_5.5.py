import sqlite3


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ("Nguyen Van A", 25))
cursor.execute("INSERT INTO my_table (name, age) VALUES (?, ?)", ("Tran Thi B", 30))


cursor.execute("SELECT name, age FROM my_table")
rows = cursor.fetchall()


print("Dữ liệu trong bảng:")
for row in rows:
    print(row)

conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("UPDATE my_table SET age = ? WHERE name = ?", (28, "Nguyen Van A"))


cursor.execute("SELECT * FROM my_table")
rows = cursor.fetchall()
print("Dữ liệu sau khi cập nhật:")
for row in rows:
    print(row)


conn.commit()
conn.close()

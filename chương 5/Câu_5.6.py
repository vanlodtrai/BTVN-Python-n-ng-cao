import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM my_table")
count = cursor.fetchone()[0]

print(f"Số bản ghi trong bảng: {count}")

conn.close()

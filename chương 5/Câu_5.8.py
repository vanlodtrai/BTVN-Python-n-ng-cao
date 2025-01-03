import sqlite3


conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute("DELETE FROM my_table WHERE name = ?", ("Tran Thi B",))


cursor.execute("SELECT * FROM my_table")
rows = cursor.fetchall()
print("Dữ liệu sau khi xóa:")
for row in rows:
    print(row)


conn.commit()
conn.close()

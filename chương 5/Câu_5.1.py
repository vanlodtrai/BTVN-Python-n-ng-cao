import sqlite3


conn = sqlite3.connect("test_database.db")


cursor = conn.cursor()


cursor.execute("SELECT sqlite_version();")
version = cursor.fetchone()


print(f"Phiên bản SQLite hiện tại là: {version[0]}")


conn.close()

import sqlite3


conn = sqlite3.connect("ql_nhan_vien.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS PHONG (
    id INTEGER PRIMARY KEY,
    ten_phong TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS NHAN_VIEN (
    id INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL,
    tuoi INTEGER NOT NULL,
    dia_chi TEXT NOT NULL,
    luong REAL NOT NULL,
    id_phong INTEGER,
    FOREIGN KEY (id_phong) REFERENCES PHONG (id)
)
""")

def add_room(name):
    cursor.execute("INSERT INTO PHONG (ten_phong) VALUES (?)", (name,))
    conn.commit()


def add_employee(name, age, address, salary, room_id):
    cursor.execute("INSERT INTO NHAN_VIEN (ho_ten, tuoi, dia_chi, luong, id_phong) VALUES (?, ?, ?, ?, ?)",
                   (name, age, address, salary, room_id))
    conn.commit()


add_room("Phòng IT")
add_employee("Nguyen Van A", 25, "Hà Nội", 1500.0, 1)


cursor.execute("SELECT * FROM NHAN_VIEN")
rows = cursor.fetchall()
print("Danh sách nhân viên:")
for row in rows:
    print(row)


conn.close()

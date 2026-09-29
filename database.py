import sqlite3

def koneksi():
    return sqlite3.connect("data.db")

def buat_table():
    conn = koneksi()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            kelas TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_siswa(nama, kelas):
    conn = koneksi()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO siswa (nama, kelas) VALUES (?, ?)",
        (nama, kelas)
    )
    conn.commit()
    conn.close()

def tampil_siswa():
    conn = koneksi()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM siswa")
    data = cursor.fetchall()
    conn.close()
    return data

def ambil_siswa():
    conn = koneksi()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM siswa")
    data = cursor.fetchall()
    conn.close()
    return data

def update_siswa(id_siswa, nama, kelas):
    conn = koneksi()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE siswa SET nama = ?, kelas = ? WHERE id = ?",
        (nama, kelas, id_siswa)
    )
    conn.commit()
    conn.close()

def hapus_siswa(id_siswa):
    conn = koneksi()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM siswa WHERE id = ?",
        (id_siswa,)
    )
    conn.commit()
    conn.close()


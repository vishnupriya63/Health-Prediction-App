import sqlite3

def create_table():
    conn = sqlite3.connect("patients.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            prediction TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_patient(name, age, prediction):
    conn = sqlite3.connect("patients.db")
    c = conn.cursor()

    c.execute("INSERT INTO patients (name, age, prediction) VALUES (?, ?, ?)",
              (name, age, prediction))

    conn.commit()
    conn.close()
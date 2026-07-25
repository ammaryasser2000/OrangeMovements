import sqlite3
from config import DATABASE_NAME

def connect():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    # جدول المستخدمين
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        language TEXT DEFAULT 'ar',
        subscription TEXT DEFAULT 'none',
        expire_date TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_user(user_id, username, full_name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO users
    (user_id, username, full_name)
    VALUES (?, ?, ?)
    """, (user_id, username, full_name))

    conn.commit()
    conn.close()

def get_user(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    user = cur.fetchone()

    conn.close()

    return user

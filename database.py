import sqlite3
from config import DATABASE_NAME
def connect():
    return sqlite3.connect(DATABASE_NAME)
def create_tables():
    conn = connect()
    cur = conn.cursor()
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
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        plan TEXT,
        start_date TEXT,
        end_date TEXT,
        active INTEGER DEFAULT 1
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS movements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        country TEXT,
        code TEXT,
        service TEXT,
        movement_key TEXT UNIQUE,
        created_at TEXT
    )
    """)
    conn.commit()    conn.close()
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
def movement_exists(key):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT id FROM movements WHERE movement_key=?",
        (key,)
    )
    row = cur.fetchone()
    conn.close()
    return row is not None
def save_movement(source, country, code, service, key):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    INSERT OR IGNORE INTO movements
    (source,country,code,service,movement_key,created_at)
    VALUES(?,?,?,?,?,datetime('now'))
    """, (
        source,
        country,
        code,
        service,
        key
    ))
    conn.commit()
    conn.close()

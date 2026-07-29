from datetime import datetime, timedelta
import sqlite3
from config import DATABASE_NAME
def connect():
    return sqlite3.connect(DATABASE_NAME)
def add_subscription(user_id, plan):
    conn = connect()
    cur = conn.cursor()
    start = datetime.now()
    if plan == "week":
        end = start + timedelta(days=7)
  elif plan == "month":
        end = start + timedelta(days=30)
    else:
        conn.close()
        return False
  cur.execute("""
        INSERT INTO subscriptions
        (user_id, plan, start_date, end_date, active)
        VALUES (?, ?, ?, ?, 1)
    """, (
        user_id,
        plan,
        start.strftime("%Y-%m-%d %H:%M:%S"),
        end.strftime("%Y-%m-%d %H:%M:%S")
    ))
    cur.execute("""
        UPDATE users
        SET subscription=?,
            expire_date=?
        WHERE user_id=?
    """, (
        plan,
        end.strftime("%Y-%m-%d %H:%M:%S"),
        user_id
    ))
  conn.commit()
    conn.close()
   return True
def is_subscribed(user_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT expire_date
        FROM users
        WHERE user_id=?
    """, (user_id,))
   row = cur.fetchone()
  conn.close()
    if row is None:
        return False
    if row[0] is None:
        return False
    expire = datetime.strptime(
        row[0],
        "%Y-%m-%d %H:%M:%S"
    )
return datetime.now() < expire

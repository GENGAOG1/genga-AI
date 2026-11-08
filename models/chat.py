from db import get_db

def create_chat(user_id, title="Neuer Chat"):
    db = get_db()
    try:
        cur = db.execute("INSERT INTO chats (user_id, title) VALUES (?, ?)", (user_id, title))
        db.commit()
        return cur.lastrowid
    finally:
        db.close()

def list_chats(user_id):
    db = get_db()
    try:
        return db.execute(
            "SELECT id, title, created_at, updated_at FROM chats WHERE user_id = ? ORDER BY updated_at DESC",
            (user_id,)
        ).fetchall()
    finally:
        db.close()

def get_chat(chat_id, user_id):
    db = get_db()
    try:
        return db.execute("SELECT id, title FROM chats WHERE id = ? AND user_id = ?", (chat_id, user_id)).fetchone()
    finally:
        db.close()

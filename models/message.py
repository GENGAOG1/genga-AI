from db import get_db

def add_message(chat_id, role, content):
    db = get_db()
    try:
        db.execute("INSERT INTO messages (chat_id, role, content) VALUES (?, ?, ?)", (chat_id, role, content))
        db.execute("UPDATE chats SET updated_at = CURRENT_TIMESTAMP WHERE id = ?", (chat_id,))
        db.commit()
    finally:
        db.close()

def list_messages(chat_id):
    db = get_db()
    try:
        return db.execute(
            "SELECT role, content, created_at FROM messages WHERE chat_id = ? ORDER BY id ASC",
            (chat_id,)
        ).fetchall()
    finally:
        db.close()

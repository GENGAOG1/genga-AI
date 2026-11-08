from db import get_db

def list_memories(user_id):
    db = get_db()
    try:
        return db.execute("SELECT id, content, created_at FROM memories WHERE user_id = ? ORDER BY id DESC", (user_id,)).fetchall()
    finally:
        db.close()

def add_memory(user_id, content):
    db = get_db()
    try:
        db.execute("INSERT INTO memories (user_id, content) VALUES (?, ?)", (user_id, content))
        db.commit()
    finally:
        db.close()

def delete_memory(user_id, memory_id):
    db = get_db()
    try:
        db.execute("DELETE FROM memories WHERE id = ? AND user_id = ?", (memory_id, user_id))
        db.commit()
    finally:
        db.close()

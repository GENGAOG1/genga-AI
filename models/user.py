from db import get_db

def get_user_by_email(email):
    db = get_db()
    try:
        return db.execute("SELECT id, email, password_hash FROM users WHERE email = ?", (email,)).fetchone()
    finally:
        db.close()

def create_user(email, password_hash):
    db = get_db()
    try:
        db.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)", (email, password_hash))
        db.commit()
    finally:
        db.close()

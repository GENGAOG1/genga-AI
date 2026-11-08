import os
import libsql

def get_db():
    url = os.getenv("TURSO_DATABASE_URL", "")
    token = os.getenv("TURSO_AUTH_TOKEN", "")
    if not url:
        raise RuntimeError("TURSO_DATABASE_URL fehlt in den Umgebungsvariablen.")
    return libsql.connect(url, auth_token=token or None)

def init_db():
    # Schema aus migrations/schema.sql muss einmal in Turso ausgeführt werden.
    # Automatische Migrationen werden später ergänzt.
    return

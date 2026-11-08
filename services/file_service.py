import os
import uuid
from werkzeug.utils import secure_filename

ALLOWED = {"txt", "md", "csv", "json", "py", "c", "cpp", "cs", "html", "css", "js", "pdf", "docx", "png", "jpg", "jpeg", "webp", "mp4", "mov", "zip"}

def save_upload(file, folder):
    if not file or not file.filename:
        return {"ok": False, "error": "Keine Datei ausgewählt."}
    safe = secure_filename(file.filename)
    ext = safe.rsplit(".", 1)[-1].lower() if "." in safe else ""
    if ext not in ALLOWED:
        return {"ok": False, "error": "Dateityp nicht erlaubt."}
    os.makedirs(folder, exist_ok=True)
    stored = f"{uuid.uuid4().hex}_{safe}"
    path = os.path.join(folder, stored)
    file.save(path)
    return {"ok": True, "filename": safe, "path": path, "extension": ext}

def extract_text_from_file(path, extension):
    # Textdateien und Quellcode können direkt gelesen werden.
    # PDF/DOCX-Parser sind bewusst als nächste Ausbaustufe markiert.
    if extension in {"txt", "md", "csv", "json", "py", "c", "cpp", "cs", "html", "css", "js"}:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                return f.read()
        except OSError:
            return ""
    return ""

from flask import Blueprint, request, jsonify, session, current_app
from services.file_service import save_upload, extract_text_from_file

files_bp = Blueprint("files", __name__)

@files_bp.post("/upload")
def upload():
    if not session.get("user_id"):
        return jsonify({"error": "Bitte anmelden."}), 401
    file = request.files.get("file")
    result = save_upload(file, current_app.config["UPLOAD_FOLDER"])
    if not result["ok"]:
        return jsonify({"error": result["error"]}), 400
    extracted = extract_text_from_file(result["path"], result["extension"])
    return jsonify({
        "filename": result["filename"],
        "text_preview": extracted[:4000],
        "note": "Für Bild-/Video-/PDF-Analyse muss ein passender Analyse-Service ergänzt werden."
    })

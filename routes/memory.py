from flask import Blueprint, request, jsonify, session
from models.memory import list_memories, add_memory, delete_memory

memory_bp = Blueprint("memory", __name__)

@memory_bp.get("/")
def memories():
    if not session.get("user_id"):
        return jsonify({"error": "Bitte anmelden."}), 401
    return jsonify({"memories": [dict(id=r[0], content=r[1], created_at=r[2]) for r in list_memories(session["user_id"])]})

@memory_bp.post("/")
def create_memory():
    if not session.get("user_id"):
        return jsonify({"error": "Bitte anmelden."}), 401
    content = (request.json or {}).get("content", "").strip()
    if not content or len(content) > 1000:
        return jsonify({"error": "Erinnerung muss 1–1000 Zeichen lang sein."}), 400
    add_memory(session["user_id"], content)
    return jsonify({"ok": True})

@memory_bp.delete("/<int:memory_id>")
def remove_memory(memory_id):
    if not session.get("user_id"):
        return jsonify({"error": "Bitte anmelden."}), 401
    delete_memory(session["user_id"], memory_id)
    return jsonify({"ok": True})

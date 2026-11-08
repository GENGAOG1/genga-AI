from flask import Blueprint, render_template, request, jsonify, session
from models.chat import create_chat, list_chats, get_chat
from models.message import add_message, list_messages
from services.ai_service import ask_ai

chat_bp = Blueprint("chat", __name__)

@chat_bp.get("/")
def chat_page():
    if not session.get("user_id"):
        return render_template("chat/chat.html", chats=[], active_chat=None, messages=[])
    chats = list_chats(session["user_id"])
    chat_id = request.args.get("id", type=int)
    active = get_chat(chat_id, session["user_id"]) if chat_id else None
    messages = list_messages(chat_id) if active else []
    return render_template("chat/chat.html", chats=chats, active_chat=active, messages=messages)

@chat_bp.post("/new")
def new_chat():
    if not session.get("user_id"):
        return jsonify({"error": "Bitte zuerst anmelden."}), 401
    chat_id = create_chat(session["user_id"])
    return jsonify({"chat_id": chat_id})

@chat_bp.post("/message")
def send_message():
    if not session.get("user_id"):
        return jsonify({"error": "Bitte zuerst anmelden."}), 401
    data = request.get_json(silent=True) or {}
    prompt = (data.get("message") or "").strip()
    chat_id = data.get("chat_id")
    if not prompt:
        return jsonify({"error": "Nachricht fehlt."}), 400
    if not chat_id:
        chat_id = create_chat(session["user_id"])
    if not get_chat(int(chat_id), session["user_id"]):
        return jsonify({"error": "Chat nicht gefunden."}), 404
    add_message(int(chat_id), "user", prompt)
    try:
        answer = ask_ai(prompt)
    except Exception:
        return jsonify({"error": "KI-Anfrage fehlgeschlagen. API-Key/Modell prüfen."}), 502
    add_message(int(chat_id), "assistant", answer)
    return jsonify({"answer": answer, "chat_id": int(chat_id)})

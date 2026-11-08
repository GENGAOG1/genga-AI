from flask import Blueprint, request, jsonify, session
from services.web_search import search_web

search_bp = Blueprint("search", __name__)

@search_bp.get("/")
def search():
    if not session.get("user_id"):
        return jsonify({"error": "Bitte anmelden."}), 401
    query = (request.args.get("q") or "").strip()
    if not query:
        return jsonify({"results": []})
    return jsonify({"results": search_web(query)})

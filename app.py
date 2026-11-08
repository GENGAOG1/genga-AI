import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from db import init_db
from routes.auth import auth_bp
from routes.chat import chat_bp
from routes.files import files_bp
from routes.search import search_bp
from routes.memory import memory_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me")
    app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_UPLOAD_MB", "25")) * 1024 * 1024
    app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER", "uploads")

    init_db()

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(chat_bp, url_prefix="/chat")
    app.register_blueprint(files_bp, url_prefix="/files")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(memory_bp, url_prefix="/memory")

    @app.get("/")
    def index():
        return render_template("landing.html")

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(_error):
        return render_template("errors/500.html"), 500

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)

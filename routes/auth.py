from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import get_user_by_email, create_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        if not email or len(password) < 8:
            flash("Bitte E-Mail eingeben und ein Passwort mit mindestens 8 Zeichen wählen.")
            return render_template("auth/register.html")
        try:
            create_user(email, generate_password_hash(password))
        except Exception:
            flash("Registrierung fehlgeschlagen. Ist die E-Mail bereits vergeben?")
            return render_template("auth/register.html")
        user = get_user_by_email(email)
        session["user_id"] = user[0]
        session["email"] = user[1]
        return redirect(url_for("chat.chat_page"))
    return render_template("auth/register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        user = get_user_by_email(email)
        if user and check_password_hash(user[2], password):
            session.clear()
            session["user_id"] = user[0]
            session["email"] = user[1]
            return redirect(url_for("chat.chat_page"))
        flash("E-Mail oder Passwort ist falsch.")
    return render_template("auth/login.html")

@auth_bp.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

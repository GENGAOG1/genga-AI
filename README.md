# GENGA AI — erweiterte Projektstruktur

Dieses ZIP ergänzt die Starterstruktur um die wichtigsten Module und sichere Grundbausteine:
- Flask-App mit Blueprints
- Turso/libSQL-Datenbank-Helfer und SQL-Schema
- Registrierung/Login mit Passwort-Hashing
- Chats und Nachrichten persistieren
- OpenRouter Chat-Aufruf
- DuckDuckGo-Suche
- Upload-Grundfunktion und Textdatei-Extraktion
- Memory-Grundgerüst
- Frontend für Chat, Sidebar und Datei-Upload
- Render-Konfiguration

## Installation
1. Python 3.11+ installieren.
2. `python -m venv .venv`
3. Windows: `.venv\\Scripts\\activate`
4. `pip install -r requirements.txt`
5. `.env.example` in `.env` kopieren und Werte eintragen.
6. `python app.py`

## Render
Build command: `pip install -r requirements.txt`
Start command: `gunicorn app:app`

## Turso
In Turso eine Datenbank erstellen und `TURSO_DATABASE_URL` sowie `TURSO_AUTH_TOKEN` in `.env`/Render setzen.
Das Schema aus `migrations/schema.sql` ausführen.

## Sicherheits-/Produktionshinweise
- Vor öffentlichem Betrieb HTTPS, E-Mail-Verifikation, Rate-Limits, CSRF, Passwort-Reset und Abuse-Handling ergänzen.
- API-Schlüssel niemals in GitHub committen.
- Uploads werden hier nur grundlegend behandelt. Für öffentliche Nutzung zusätzlich Virenscan, private Objektspeicherung, Content-Type-Prüfung und Berechtigungen einbauen.
- PDF/DOCX/Video-/Bildanalyse und Generierung brauchen geeignete Anbieter/Modelle. Die Service-Dateien enthalten bewusst Erweiterungspunkte.
- Kostenloser Betrieb ist von Anbieterlimits abhängig; keine unbegrenzte kostenlose API garantiert.

# auth_fixed.py — Secure version (after AI-assisted fixes)
# Show this AFTER the live fix demo to confirm all vulns resolved.

import sqlite3
import bcrypt
import os
from jose import jwt

# ============================================================
# FIX 1: Secrets loaded from environment variables (not hardcoded)
# ============================================================
SECRET_KEY = os.environ["SECRET_KEY"]          # set in .env or CI secrets
API_TOKEN  = os.environ["API_TOKEN"]


def get_connection():
    conn = sqlite3.connect("users.db")
    return conn


# ============================================================
# FIX 2: Parameterised query — SQL injection eliminated
# ============================================================
def login(username: str, password: str):
    """Authenticate a user safely using a parameterised query."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",  # placeholder, not f-string
        (username,)
    )
    row = cursor.fetchone()
    if row and bcrypt.checkpw(password.encode(), row["password_hash"]):
        return row
    return None


# ============================================================
# FIX 3: bcrypt replaces MD5
# ============================================================
def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with a random salt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


# ============================================================
# FIX 4: Replace pickle with JSON (no code execution risk)
# ============================================================
import json

def load_user_session(session_data: str) -> dict:
    """Restore a user session from a JSON string."""
    return json.loads(session_data)

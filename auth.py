# auth.py — User authentication module
# Demo file for AI DevSecOps seminar

import sqlite3
import pickle
import hashlib

# ============================================================
# VULNERABILITY 1: Hardcoded credentials (Snyk: CWE-798)
# Snyk will flag this as a "Hardcoded Secret"
# ============================================================
DB_PASSWORD = "admin123"
SECRET_KEY   = "s3cr3t-jwt-key-do-not-share"
API_TOKEN    = "ghp_A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7"


def wr
def get_connection():
    """Return a database connection."""
    conn = sqlite3.connect("users.db")
    return conn


# ============================================================
# VULNERABILITY 2: SQL Injection (Snyk: CWE-89)
# User input is directly concatenated into the SQL query.
# Snyk highlights this line; Copilot Chat can explain & fix it.
# ============================================================
def login(username: str, password: str):
    """Authenticate a user by username and password."""
    conn = get_connection()
    cursor = conn.cursor()

    # BUG: Never do this — attacker input: ' OR '1'='1
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)  # <-- Snyk flags this line
    return cursor.fetchone()


# ============================================================
# VULNERABILITY 3: Weak hashing (Snyk: CWE-916)
# MD5 is cryptographically broken for password storage.
# ============================================================
def hash_password(password: str) -> str:
    """Hash a password before storing it."""
    return hashlib.md5(password.encode()).hexdigest()  # <-- Snyk flags: use bcrypt


# ============================================================
# VULNERABILITY 4: Insecure Deserialization (Snyk: CWE-502)
# pickle.loads() on untrusted data allows remote code execution.
# ============================================================
def load_user_session(session_data: bytes):
    """Restore a user session from serialized bytes."""
    return pickle.loads(session_data)  # <-- Snyk flags: arbitrary code exec


# ============================================================
# DEMO PAUSE POINT — Ask Copilot Chat:
#   "Explain all the security vulnerabilities in this file"
#   "Fix the SQL injection using parameterised queries"
#   "Rewrite hash_password using bcrypt"
# ============================================================

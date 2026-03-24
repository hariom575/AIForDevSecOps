# Dockerfile — demo app container
# Snyk will flag multiple misconfigurations here

FROM python:3.11

# ============================================================
# VULNERABILITY 1: Running as root (Snyk: DKR-DS002)
# Containers should run as non-root users.
# ============================================================
# No USER directive = runs as root by default

# ============================================================
# VULNERABILITY 2: No HEALTHCHECK defined (Snyk: DKR-DS005)
# ============================================================

WORKDIR /app

# ============================================================
# VULNERABILITY 3: Copying everything including secrets (Snyk)
# .env, credentials, private keys all end up in the image
# ============================================================
COPY . .                    # <-- dangerous: copies .env, keys, etc.

RUN pip install -r requirements.txt

# ============================================================
# VULNERABILITY 4: Using ADD instead of COPY (Snyk: DKR-DS006)
# ADD can auto-extract archives and fetch remote URLs.
# ============================================================
ADD https://example.com/config.tar.gz /config/

EXPOSE 5000

CMD ["python", "app.py"]

# ============================================================
# DEMO PAUSE POINT — Copilot Chat prompt:
#   "Fix the security issues in this Dockerfile"
# Expected fix: add non-root USER, use COPY not ADD,
# add .dockerignore, add HEALTHCHECK
# ============================================================

# ============================================================
# Dockerfile — Language Learning App
# Multi-stage production-ready setup:
#   - slim Python base image
#   - non-root user for security
#   - entrypoint.sh applies migrations then starts gunicorn
# ============================================================

# ------------------------------------------------------------
# STAGE 1: Base image
# Python 3.11 slim — smaller than the full image, but has
# everything we need (pip, standard library, shell).
# ------------------------------------------------------------
FROM python:3.11-slim

# Python runtime tweaks:
#   PYTHONDONTWRITEBYTECODE — don't create .pyc files
#   PYTHONUNBUFFERED        — show logs instantly (no buffering)
#   FLASK_APP               — tell Flask which module to run
#   PIP_NO_CACHE_DIR        — don't store pip cache (smaller image)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    PIP_NO_CACHE_DIR=1

# Working directory inside the container
WORKDIR /app

# ------------------------------------------------------------
# STAGE 2: System dependencies
# gcc is required to compile some Python packages
# (e.g. SQLAlchemy, cryptography). apt cache is removed
# afterwards to keep the image small.
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------------------------
# STAGE 3: Python dependencies
# Copy requirements.txt FIRST so this layer is cached.
# If only app.py changes later, pip install won't rerun.
# ------------------------------------------------------------
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ------------------------------------------------------------
# STAGE 4: Application code
# Copy the rest of the project into the container.
# ------------------------------------------------------------
COPY . .

# Create the instance folder (SQLite database lives here).
# Fix Windows CRLF line endings in entrypoint.sh -> LF,
# then make the file executable.
# sed -i 's/\r$//' removes trailing carriage returns,
# which would otherwise break the shebang line on Linux.
RUN mkdir -p instance \
    && sed -i 's/\r$//' entrypoint.sh \
    && chmod +x entrypoint.sh

# ------------------------------------------------------------
# STAGE 5: Runtime
# ------------------------------------------------------------

# Document that the container listens on port 5000
EXPOSE 5000

# Create a non-root user and give it ownership of /app.
# Running as root inside a container is a security risk.
RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app
USER appuser

# When the container starts, run entrypoint.sh:
# it applies Flask-Migrate migrations, then launches gunicorn.
ENTRYPOINT ["./entrypoint.sh"]
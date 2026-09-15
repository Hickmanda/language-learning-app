#!/bin/sh
# ============================================================
# ENTRYPOINT — runs when the container starts
# ============================================================
set -e   # stop on any error

echo "▶ Applying database migrations..."
python -m flask db upgrade

echo "▶ Starting Gunicorn on port ${PORT:-5000}..."
exec gunicorn \
    --bind "0.0.0.0:${PORT:-5000}" \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    app:app
"""gunicorn server configuration."""

import os

threads = 8
workers = 1
timeout = 0
bind = f":{os.environ.get('PORT', '8080')}"
worker_class = "uvicorn.workers.UvicornWorker"

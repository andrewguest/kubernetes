# Configuration file for `gunicorn` command.
# 1) Set the settings in this file.
# 2) Run `gunicorn` from the terminal in the directory containing this file

import multiprocessing
import os

from dotenv import load_dotenv

load_dotenv()

# Get the `ENVIRONMENT` env variable and convert it to lowercase if it exists
environment = os.getenv("ENVIRONMENT", "dev").lower()

# Gunicorn app
# Tell Gunicorn which application to run
wsgi_app = "app.main:app"

# Requests
# Restart workers after so many requests, with some variability.
max_requests = 1000
max_requests_jitter = 50

# Logging
# Use stdout for logging
log_file = "-"

# The IP address and port to accept requests on
bind = "0.0.0.0:8000"

# Use this formula for production, otherwise only run 2 workers
workers = (
    multiprocessing.cpu_count() * 2 + 1 if environment in ["prod", "production"] else 1
)
worker_class = "uvicorn_worker.UvicornWorker"

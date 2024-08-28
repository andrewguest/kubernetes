import multiprocessing


# Requests - restart workers after so many requests, with some variability.
max_requests = 1000
max_requests_jitter = 50

# Logging - use stdout for logging
log_file = "-"

# Workers
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

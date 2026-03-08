
# Number of worker processes
workers = 2  

# Worker class (Uvicorn for FastAPI)
worker_class = "uvicorn.workers.UvicornWorker"

timeout = 300
# restart workers gracefully
graceful_timeout = 300

# prevent memory leaks
max_requests = 1000
max_requests_jitter = 100



# Host and port, localisation of uvicorn
bind = "127.0.0.1:8000"

# Logging
accesslog = "-"  # stdout
errorlog = "-"
access_log_format = '%(p)s %(h)s "%(r)s" %(s)s %(L)s'
loglevel = "info"



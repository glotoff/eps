# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
"""
bind = '0.0.0.0:5005'
workers = 1
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
"""

import multiprocessing

# Define the address and port Gunicorn will bind to
bind = "0.0.0.0:8000"

# Set the number of worker processes
# In general, set this value to the number of CPU cores available on your server
workers = multiprocessing.cpu_count() * 2 + 1

# Set the maximum number of simultaneous clients each worker process can handle
worker_connections = 1000

# Set the worker class (sync, gevent, etc.)
worker_class = "sync"

# Set the maximum number of requests a worker can handle before being restarted
max_requests = 1000

# Set the amount of time (in seconds) a worker can spend handling a single request
timeout = 30

# Set the maximum amount of time (in seconds) a worker can spend establishing a connection
keepalive = 2

# Set the log level (debug, info, warning, error, critical)
loglevel = "info"

# Set the access log format
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Enable or disable access log redirection to the specified file
#accesslog = "/var/log/gunicorn/access.log"

# Enable or disable error log redirection to the specified file
#errorlog = "/var/log/gunicorn/error.log"
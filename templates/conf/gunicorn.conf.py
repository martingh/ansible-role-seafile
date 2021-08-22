import os

daemon = True
workers = 5

bind = "127.0.0.1:{{ seafile_gunicorn_port }}"

# Pid
pids_dir = '{{ seafile_var_data + "/pids" }}'
pidfile = os.path.join(pids_dir, 'seahub.pid')

# Logging
logs_dir = '{{ seafile_log_dir }}'
errorlog = os.path.join(logs_dir, 'gunicorn_error.log')
accesslog = os.path.join(logs_dir, 'gunicorn_access.log')

# for file upload, we need a longer timeout value (default is only 30s, too short)
timeout = 1200

limit_request_line = 8190

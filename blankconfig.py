# Dropbox auth token goes here
dbxAccount = ''

# Maximum file size, in bytes, that is sent to a destination before the file is broken into chunks
# Default value of 10485760 means 10MB 
chunk_size = 10485760

# Prune / clean up old backups - not yet functional
cleanup = 0
copies_to_keep = 30

# Hostname, port, authentication, etc for SMTP notifications 
smtp_host = ''
smtp_port = 25
smtp_auth_req = 0 # Set to '1' if authentication is required 
smtp_username = ''
smtp_password = ''
smtp_sendto = ''
smtp_sendfrom = ''
smtp_always_notify = 0 # Notify on job completion, even if no errors occur

# Timestamp each completed backup job directory?
timestamps = 0
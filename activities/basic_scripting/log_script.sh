#!/bin/bash

log_file="my_script.log"

log_message() {
  timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  echo "[$timestamp] $1" >> "$log_file"
}

log_message "Script started."

# ... your script logic ...

log_message "Data processing complete."
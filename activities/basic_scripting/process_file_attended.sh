#!/bin/bash

read -p "Enter filename: " filename

if [[ -f "$filename" ]]; then
  while IFS= read -r line; do
    if [[ "$line" == *"keyword"* ]]; then  # Example logic
      echo "Found keyword in: $line"
    fi
  done < "$filename"
else
  echo "File not found."
fi
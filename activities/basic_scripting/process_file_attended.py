#!/usr/bin/env python3

filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        for line in f:
            if "keyword" in line:  # Example logic
                print(f"Found keyword in: {line.strip()}") # strip removes newline
except FileNotFoundError:
    print("File not found.")
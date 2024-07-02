import re

# Read the log file
file_path = 'LogFile.txt'
with open(file_path, 'r') as file:
    log_data = file.read()

# Define the regular expression to match the required entries
pattern = r'^(187\.\d+\.\d+\.\d+)\s+\|[^\|]+\|[^\|]+\|[^\|]+\|\s*(\w+)$'

# Find all matches
matches = re.findall(pattern, log_data, re.MULTILINE)

# Print the results
for ip, username in matches:
    print(f"IP Address: {ip}, Username: {username}")

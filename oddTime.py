from datetime import datetime

# Specify the file path
file_path = "LogFile2.txt"

# Get the input time from the user
input_time_str = input("Enter the time to check against (in HH:MM:SS AM/PM format): ")

# Parse the input time into a datetime object
input_time = datetime.strptime(input_time_str, '%I:%M:%S %p').time()

# Open the file
with open(file_path, 'r') as file:
    # Read the file contents into a string
    log_data = file.read()

# Split the log data into lines
lines = log_data.strip().split('\n')

# Process each line
users_after_input_time = []
for line in lines[1:]:  # Skip the header line
    parts = line.split('|')
    if len(parts) < 3:
        continue
    username = parts[0].strip()
    ip_address = parts[1].strip()
    timestamp_str = parts[2].strip()
    
    # Parse the timestamp into a datetime object
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %I:%M:%S%p')
    
    # Check if the time is after the input time
    if timestamp.time() >= input_time:
        users_after_input_time.append((username, ip_address))

# Print the result
for user, ip in users_after_input_time:
    print(f"Username: {user}, IP Address: {ip}")

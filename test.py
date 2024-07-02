from datetime import datetime

# Specify the file path
file_path = 'LogFile2.txt'

# Open the file
with open(file_path, 'r') as file:
    # Read the file contents into a string
    log_data = file.read()

# Split the log data into lines
lines = log_data.strip().split('\n')

# Process each line
users_after_9pm = []
for line in lines[2:]:  # Skip the header lines
    parts = line.split('|')
    if len(parts) < 3:
        continue
    username = parts[0].strip()
    ip_address = parts[1].strip()
    timestamp_str = parts[2].strip()
    
    # Parse the timestamp into datetime object
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %I:%M:%S%p')
    
    # Check if the time is after 09:00:00 PM
    if timestamp.hour >= 21:  # 21 is 9 PM in 24-hour format
        users_after_9pm.append((username, ip_address))

# Print the result
for user, ip in users_after_9pm:
    print(f"Username: {user}, IP Address: {ip}")

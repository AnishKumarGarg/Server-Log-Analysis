from collections import defaultdict
from datetime import timedelta

# Read the log file
log_file_path = 'LogFile2.txt'

# Dictionary to store the total session duration per user
session_durations = defaultdict(timedelta)

# Function to convert session duration string to timedelta
def parse_duration(duration_str):
    # Example duration strings: '2 hours', '1.5 hours', '3.5 hours'
    if 'hours' in duration_str:
        hours = float(duration_str.split()[0])
        return timedelta(hours=hours)
    return timedelta()

# Open and read the file
with open(log_file_path, 'r') as file:
    # Skip the header line
    next(file)
    
    # Process each line in the log file
    for line in file:
        # Split the line by the pipe character to extract the fields
        fields = line.split('|')
        
        # Extract the username and session duration
        username = fields[0].strip()
        session_duration_str = fields[3].strip()
        
        # Parse the session duration and add it to the user's total duration
        if session_duration_str != '-':
            session_duration = parse_duration(session_duration_str)
            session_durations[username] += session_duration

# Get the usernames with total session duration more than 5 hours
users_more_than_5_hours = [user for user, duration in session_durations.items() if duration > timedelta(hours=5)]

# Print the usernames
print("Users with total session duration of more than 5 hours:")
for user in users_more_than_5_hours:
    print(user)

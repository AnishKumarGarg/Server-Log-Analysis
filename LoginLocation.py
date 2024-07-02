# Read the log file
log_file_path = 'LogFile2.txt'

# List to store the usernames who didn't login from Dubai or Bangalore
users_not_from_dubai_or_bangalore = []

# Open and read the file
with open(log_file_path, 'r') as file:
    # Skip the header line
    next(file)
    
    # Process each line in the log file
    for line in file:
        # Split the line by the pipe character to extract the fields
        fields = line.split('|')
        
        # Extract the username and login location
        username = fields[0].strip()
        login_location = fields[-1].strip()
        
        # Check if the login location is neither Dubai nor Bangalore
        if login_location not in ['Dubai', 'Bangalore']:
            users_not_from_dubai_or_bangalore.append(username)

# Print the usernames
print("Users who didn't log in from Dubai or Bangalore:")
for user in users_not_from_dubai_or_bangalore:
    print(user)

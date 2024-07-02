from collections import defaultdict

# Read the log file
log_file_path = 'LogFile2.txt'

# Dictionary to store the count of failed login attempts per user
login_attempts = defaultdict(int)

# Dictionary to store the IP address for each user
user_ips = defaultdict(set)

# Open and read the file
with open(log_file_path, 'r') as file:
    # Skip the header line
    next(file)
    
    # Process each line in the log file
    for line in file:
        # Split the line by the pipe character to extract the fields
        fields = line.split('|')
        
        # Extract the username, IP address, and status
        username = fields[0].strip()
        ip_address = fields[1].strip()
        status = fields[5].strip()
        
        # Check if the login attempt was failed
        if status == "Failed":
            # Increment the login attempt count for the user
            login_attempts[username] += 1
            # Store the IP address for the user
            user_ips[username].add(ip_address)

# Get the usernames and IP addresses with more than 3 failed login attempts
users_more_than_3_attempts = [(user, list(user_ips[user])) for user, count in login_attempts.items() if count > 3]

# Print the usernames and IP addresses
print("Users with more than 3 failed login attempts:")
for user, ips in users_more_than_3_attempts:
    print(f"{user}: {', '.join(ips)}")

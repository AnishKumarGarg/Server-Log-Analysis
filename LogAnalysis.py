import re
from collections import defaultdict
from datetime import timedelta
from datetime import datetime

def networkAddress(log_file_path="LogFile2.txt"):
    with open(log_file_path, 'r') as file:
        log_data = file.read()
        
    # input network address to find in the log
    IdToFind=input("Enter The network address to check: ")

    # Define the regular expression to match the required entries
    pattern = fr'^(.*?)\s*\|\s*({re.escape(IdToFind)}\.\d+\.\d+\.\d+)\s*\|.*$'

    # Find all matches
    matches = re.findall(pattern, log_data, re.MULTILINE)

    # Print the results
    print("Users with network address "+IdToFind)
    for ip, username in matches:
        print(f"IP Address: {ip}, Username: {username}")
        
def LoginLocation(log_file_path="LogFile2.txt"):
    # List to store tuples of IP addresses and usernames who didn't login from specified locations
    users_not_from_specified_locations = []

    # Input 2 locations where your company exists
    locations = input("Enter two locations to check separated by space: ")
    loc1, loc2 = locations.split()

    # Open and read the file
    with open(log_file_path, 'r') as file:
        # Skip the header line
        next(file)
    
        # Process each line in the log file
        for line in file:
            # Split the line by the pipe character to extract the fields
            fields = line.split('|')
            
            # Extract the username, IP address, and login location
            username = fields[0].strip()
            ip_address = fields[1].strip()
            login_location = fields[-1].strip()
            
            # Check if the login location is neither of the specified locations
            if login_location not in [loc1, loc2]:
                users_not_from_specified_locations.append((ip_address, username))

    # Print the IP addresses and usernames
    print("Users who didn't log in from the specified locations:")
    for ip, user in users_not_from_specified_locations:
        print(f"IP Address: {ip}, Username: {user}")
        

def SessionDuration(log_file_path="Logfile2.txt"):
    session_durations = defaultdict(timedelta)
    user_ip_mapping = {}

    # Input maximum session duration
    threshold_duration = float(input("Enter the number of hours to check: "))

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
            
            # Extract the username, IP address, and session duration
            username = fields[0].strip()
            ip_address = fields[1].strip()
            session_duration_str = fields[3].strip()
            
            # Parse the session duration and add it to the user's total duration
            if session_duration_str != '-':
                session_duration = parse_duration(session_duration_str)
                session_durations[username] += session_duration
                user_ip_mapping[username] = ip_address

    # Get the usernames with total session duration more than the specified duration
    users_more_than_specified_hours = [user for user, total_duration in session_durations.items() if total_duration > timedelta(hours=threshold_duration)]

    # Print the usernames
    print(f"Users with total session duration of more than {threshold_duration} hours:")
    for user in users_more_than_specified_hours:
        ip_address = user_ip_mapping[user]
        print(f"IP Address: {ip_address}, Username: {user}")


def MultipleFailedLogin(log_file_path="LogFile2.txt"):
    
    # Input the maximum number of failed login attempts
    n = int(input("Enter the number of failed login attempts to check "))

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

    # Get the usernames and IP addresses with more than n failed login attempts
    users_more_than_n_attempts = [(user, list(user_ips[user])) for user, count in login_attempts.items() if count > n]

    # Print the usernames and IP addresses
    print(f"Users with more than {n} failed login attempts:")
    for user, ips in users_more_than_n_attempts:
        print(f"IP Address: {ips}, Username: {user}")


def OddTime(log_file_path="LogFile2.txt"):
    
    # Get the input time from the user
    input_time_str = input("Enter the time to check against (in HH:MM:SS AM/PM format): ")
    
    # Parse the input time into a datetime object
    input_time = datetime.strptime(input_time_str, '%I:%M:%S %p').time()
    
    # Open the file
    with open(log_file_path, 'r') as file:
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



# Call the function to test
print("Choose what you want to perform...")
print("1 -> Filter by network addreess")
print("2 -> Filter by Login Location")
print("3 -> Filter by Session Duration")
print("4 -> Filter by number of failed login attempts")
print("5 -> Filter by time of login")
d=int(input("Enter a number... "))

print()
if(d==1):
    networkAddress() #1
print()
if(d==2):
    LoginLocation() #2
print()
if(d==3):
    SessionDuration() #3
print()
if(d==4): 
    MultipleFailedLogin() #4
print()
if(d==5):
    OddTime() #5

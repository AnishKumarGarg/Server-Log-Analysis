def SessionDuration(log_file_path="Logfile2.txt"):
    session_durations = defaultdict(timedelta)
    user_ip_mapping = {}

    # Input maximum session duration
    duration = float(input("Enter the number of hours for the session: "))

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
    users_more_than_specified_hours = [user for user, duration in session_durations.items() if duration > timedelta(hours=duration)]

    # Print the usernames
    print(f"Users with total session duration of more than {duration} hours:")
    for user in users_more_than_specified_hours:
        ip_address = user_ip_mapping[user]
        print(f"IP Address: {ip_address}, Username: {user}")
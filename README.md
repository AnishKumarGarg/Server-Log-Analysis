# Server Log Analysis
This project is a Python script designed to analyze server log files. 
**As a cybersecurity analyst, suppose you have been provided with a static login log and your task is to analyse and examine the log to find the potential unauthorized user**

## Features
Network Address Identification: Find specific network addresses in the log files.
Login Location Check: Verify if logins are not occurring from authorized locations.
Session Duration: Find users with more than the specified session duration in the log file.
Failed Logins: Flag users with suspicious number of failed logins
Login at odd times: Flag users who logged in outside working hours

## Prerequisites
Python 3.x
Required Python libraries: re, collections, datetime

Clone the repository:
> git clone https://github.com/yourusername/server-log-analysis.git
> cd server-log-analysis

*Sample log file: LogFile2.txt*

Run: python LogAnalysis.py

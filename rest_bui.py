import argparse


# Create argument parser
parser = argparse.ArgumentParser(description='Description of your script')

# Add arguments
parser.add_argument('-c', '--config', help='Path to the config file (e.g., jira.ini)', required=True)
parser.add_argument('-v', '--verbosity', help='Verbosity level (e.g., debug)', default='info')
parser.add_argument('-l', '--logfile', help='Path to the log file', default='rest.log')
parser.add_argument('-s', '--password', help='Password', required=True)
parser.add_argument('-t', '--ticket1', help='Ticket ID 1', required=True)
parser.add_argument('-x', '--ticket2', help='Ticket ID 2', required=True)
parser.add_argument('-k', '--user', help='User name', required=True)

# Parse arguments
args = parser.parse_args()

# Access parsed arguments
config_file = args.config
verbosity = args.verbosity
logfile = args.logfile
password = args.password
ticket1 = args.ticket1
ticket2 = args.ticket2
user = args.user

# Your script logic here
print("Config file:", config_file)
print("Verbosity:", verbosity)
print("Log file:", logfile)
print("Password:", password)
print("Ticket 1:", ticket1)
print("Ticket 2:", ticket2)
print("User:", user)


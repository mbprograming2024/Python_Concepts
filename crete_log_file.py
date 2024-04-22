# This function, generate_log_file_name, takes the current_file_name as input,
# extracts its base name and extension, appends the current timestamp in a specific format,
# and finally adds the ".log" extension to create the log file name.
#
# In the example provided, if current_file_name is "demo.txt,"
#     the generated log_file_name might look like "demo_20220103_142536.log"
#     (assuming the current date is January 3, 2022, and the current time is 14:25:36).

import os
from datetime import datetime

def generate_log_file_name(current_file_name):
    # Get the current timestamp in a specific format (e.g., YYYYMMDD_HHMMSS)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Extract the base file name and extension
    base_name, extension = os.path.splitext(current_file_name)

    # Create the log file name by appending the timestamp and ".log" extension
    log_file_name = f"{base_name}_{timestamp}.log"
    log_file_path = "./log/" + log_file_name

    # Open the file in write mode, creating it if it doesn't exist
    with open(log_file_path, 'w'):
        pass
    return log_file_name

# Example usage:
current_file_name = os.path.basename(__file__)
log_file_name = generate_log_file_name(current_file_name)
print(log_file_name)
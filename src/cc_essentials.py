import os
from datetime import datetime
import pytz
import yaml

# Configuration File Loading Function
def load_yaml_file():
    # Construct the path to the YAML configuration file
    yaml_file_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

    # Check if the file exists and load the data if successful
    if os.path.exists(yaml_file_path):
        with open(yaml_file_path, 'r') as config_file:
            config_data = yaml.safe_load(config_file)
            return config_data, True
    else:
        # Return an empty string and False status if the file is not found
        return "", False


# Path Checking and Misc. Functions
def is_directory_exists(directory_path):
    # Check if the directory exists and is a valid directory
    return os.path.exists(directory_path) and os.path.isdir(directory_path)

def create_directory(directory_path):
    # Create a directory at the specified path
    os.mkdir(directory_path)

def path_to_organise_exists(path_to_organise):
    # Check if the specified path exists
    return os.path.exists(path_to_organise)


# Logging Functions
def cc_log(main_log_location, log_message):
    # Load configuration and extract time zone
    yaml_data, status_code = load_yaml_file()
    tz = yaml_data['time_zone']

    # Get the current time and format it
    current_time = datetime.now(pytz.timezone(tz))
    timestamp = current_time.strftime("%a %b %d %H:%M:%S %Z %Y")

    try:
        # Check if the main log file exists and append the log message
        if os.path.exists(main_log_location):
            with open(main_log_location, 'a') as f:
                f.write(f"[ {timestamp} ] - {log_message} ✓\n")
                return True
        else:
            # Print an error message if the main log file does not exist
            print(f"Error ! {main_log_location} does not exist ✗")
            return False
    except Exception as e:
        # Print an error message if there's an exception during logging
        print(f"Error ! Failed to Log. Error Below:\n{e}")

def err_log(err_log_location, log_message, log_type):
    # Load configuration and extract time zone
    yaml_data, status_code = load_yaml_file()
    tz = yaml_data['time_zone']

    # Get the current time and format it
    current_time = datetime.now(pytz.timezone(tz))
    timestamp = current_time.strftime("%a %b %d %H:%M:%S %Z %Y")
    
    try:
        # Check if the error log file exists and append the log message
        if os.path.exists(err_log_location):
            with open(err_log_location, 'a') as f:
                f.write(f"[ {timestamp} ] - ( {log_type} ) : {log_message} \n")
                return True
        else:
            # Print an error message if the error log file does not exist
            print(f"Error ! {err_log_location} does not exist ✗")
            return False
    except Exception as e:
        # Print an error message if there's an exception during error logging
        print(f"Error ! Failed to Log. Error Below:\n{e}")

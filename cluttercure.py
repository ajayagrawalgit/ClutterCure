import sys
from src.cc_essentials import *
from src.cc_core import *

# Load configuration data and check for success
config_data, go = load_yaml_file()

if go:
    # Extract relevant information from the configuration
    path_to_organise = config_data['path_to_organise']
    error_log = config_data['logs']['error_log']
    main_log = config_data['logs']['main_log']

    # Log the start of ClutterCure execution
    cc_log(main_log, f"- - - - - - - - - - Executing ClutterCure Now - - - - - - - - - -")

    # Check if the specified path to organize exists
    if path_to_organise_exists(path_to_organise):
        cc_log(main_log, "Validated path_to_organise from config.yaml now...")

        # Check and create directories if required
        check_and_create_dirs()
        cc_log(main_log, f"Created directories under '{path_to_organise}' to cure the clutter now (if required)...")

        # Perform clutter cure on the specified path
        cure_the_clutter(path_to_organise)
        cc_log(main_log, f"ClutterCure Execution Completed")
    else:
        # Print an error message if 'path_to_organise' field does not exist
        print("Looks like 'path_to_organise' field in config.yaml does not exist! Kindly recheck the value and input the correct path!")
        
        # Log an error and exit the program
        err_log(error_log, "Incorrect path defined for 'path_to_organise' in config.yaml. Hence, Exiting !", "ERROR")
        sys.exit(1)
else:
    # Print an error message if there is an issue loading config.yaml
    print("Error Loading config.yaml")
    sys.exit(1)

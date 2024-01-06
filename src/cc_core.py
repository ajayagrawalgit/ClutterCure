import shutil
from src.cc_essentials import *

def check_and_create_dirs():
    # Load configuration and check for success
    config_data, go = load_yaml_file()
    
    if go:
        file_types = config_data['file_types']
        main_log_file_path = config_data['logs']['main_log']
        error_log_file_path = config_data['logs']['error_log']

        # Iterate through file types and check/create directories
        for type, extensions in file_types.items():
            organised_dir_path = os.path.join(config_data['path_to_organise'], type)

            # Check if the directory exists
            if is_directory_exists(organised_dir_path):
                cc_log(main_log_file_path, f"Directory Already Exists ({organised_dir_path}). Files with extension(s) - {extensions} will be stored in this directory.")
            else:
                # Log the creation of the directory and create it
                cc_log(main_log_file_path, f"Creating {organised_dir_path} now ...")
                err_log(error_log_file_path, f"{organised_dir_path} does not exist. Hence, Created it now !", "WARNING")
                create_directory(organised_dir_path)


def cure_the_clutter(path_to_organise):
    # Load configuration and check for success
    config_data, go = load_yaml_file()
    
    if go:
        file_types = config_data['file_types']
        main_log_file_path = config_data['logs']['main_log']
        error_log_file_path = config_data['logs']['error_log']

        # Iterate through file types and move files to their organized directories
        for file_type, extensions in file_types.items():
            organised_dir_path = os.path.join(config_data['path_to_organise'], file_type)
            cc_log(main_log_file_path, f"Moving files with Extensions - {extensions} to {organised_dir_path} now")

            # Iterate through file extensions
            for ext in extensions:
                matching_files = [file for file in os.listdir(path_to_organise) if file.endswith(f'.{ext}')]

                if matching_files:
                    for file in matching_files:
                        source_file_path = os.path.join(path_to_organise, file)
                        target_file_path = os.path.join(organised_dir_path, file)

                        try:
                            # Move the file to the organized directory
                            shutil.move(source_file_path, target_file_path)
                            cc_log(main_log_file_path, f"( SUCCESS ) : {file} moved to {target_file_path}")
                        except FileNotFoundError:
                            # Log an error if the file is not found
                            err_log(error_log_file_path, f"{file} not found at {source_file_path}", "ERROR")
                        except Exception as e:
                            # Log an error for other exceptions during file movement
                            err_log(error_log_file_path, f"Something Went Wrong with {file} - {str(e)}", "ERROR")
                else:
                    # Log a warning if no files are found with the extension
                    err_log(error_log_file_path, f"No files found with the extension - '{ext}' under {path_to_organise} currently. Hence, Skipping...", "WARNING")

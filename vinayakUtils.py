import os

# Directory of the script being run
directory_of_script = os.path.dirname(os.path.abspath(__file__))

print("directory_of_script: ", directory_of_script)


# Current working directory
current_working_directory = os.path.abspath(os.getcwd())

print("current_working_directory: ", current_working_directory)



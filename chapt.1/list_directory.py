import os

def list_directory_contents(directory):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(directory)
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")

# Specify the directory path
directory_path = input("Enter the path of the directory: ")

# List and print the contents of the specified directory
list_directory_contents(directory_path)

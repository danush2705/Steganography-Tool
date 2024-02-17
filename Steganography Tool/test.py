import os

# Get the folder path and filename from the user
folder_path = "G:\Sem 3\Mini Project"
filename = "stego_image.png"

# Function to search for the file in a folder
def find_file_in_folder(folder_path, filename):
    for root, dirs, files in os.walk(folder_path):
        if filename in files:
            return os.path.join(root, filename)

# Search for the file in the specified folder
print( find_file_in_folder(folder_path, filename))

#WRITE A PYTHON PROGRAM TO PRINT THE CONTENTS OF A DIRECTORY USING THE OS MODULE

import os

# Specify the directory path
directory_path = "/"

# List all the files and directories in the specified folder

contents = os.listdir(directory_path)
   
#print each file and directory name

print(contents) 
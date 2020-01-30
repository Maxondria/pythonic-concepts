import os
from datetime import datetime

# current directory
# print(os.getcwd())

# Changes directory
# os.chdir('/Users/maxbigbudget/Work/Projects/')

# List all files and folders in the current working dir
# print(os.listdir())

# make directory
# os.mkdir('Some-Folder')

# make several inner level directories
# os.makedirs('Some/Deep/Level/Folder')

# remove a single directory
# os.rmdir('Some-folder')

# remove several directories
# os.removedirs('Some/Deep/Level/Folder')

# rename a file
# os.rename('original.txt', 'new_name.txt')

# stats about a file

# print(os.stat('strings.py').st_size)
# mod_time = os.stat('strings.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

# traverse a directory using walk()
# This will return a tuple with 3 values every time

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)

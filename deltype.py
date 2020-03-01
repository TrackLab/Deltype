# Author - TrackLab https://github.com/TrackLab
# Requirements - When using the delfiletype.exe, None.
#                When using this source code, send2trash                

import os
from sys import argv
from send2trash import send2trash

def deletefile(filetype):
    for f in os.listdir():
        if f.endswith(filetype):
            send2trash(f)       # Replace with os.remove(f) to use python-only libraries but lose undo-ability
            print('\nDeleted', f)
    print('\nSuccessfully everything with the filetype', filetype)

try:    
    os.chdir(argv[1])
except:
    if input('\nRun in the directory: '+os.getcwd()+'? y/n\n').lower() == 'y':
        pass
    else:
        print('Please specify a directory when running the script...\n')
        quit()
filetype = input('\nWhat filetype should be deleted?\n').lower()
if filetype == '':
    if input('\nA blank filetype will WIPE YOUR DIRECTORY! Are you sure you want to continue? y/n\n').lower() == 'y':
        deletefile(filetype)
    quit()
if filetype.startswith('.'):
    filetype = filetype[1:].lower()
deletefile(filetype)

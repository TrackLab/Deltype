# Author - TrackLab https://github.com/TrackLab
# Contributor - SarenDev https://github.com/SarenDev
# Requirements - When using the delfiletype.exe, None.
#                When using this source code, send2trash                

import os
from sys import argv
from send2trash import send2trash

def help():
    print('\n\nDeltype - A simple and easy to use program to delete all files with a specific filetype inside a directory\n')
    print('Usage: deltype(.py/.exe) [directory, -h]\n')
    print('-h: simply prints this help menu\n')

def deletefile(filetype):
    for f in os.listdir():
        if f.endswith(filetype):
            send2trash(f)       # Replace with os.remove(f) to use built in libraries but lose undo-ability
            print('\nDeleted', f)
    print('\nSuccessfully del-ed everything with the type .', filetype)

try:
    act=argv[1]
except:
    help()
    if input('\nRun in the directory: '+os.getcwd()+'? y/n\n').lower() == 'y':
        pass
    else:
        print('Please specify a directory when running the script or run "-h"...\n')
        quit()
if act in ('-h','h','-H','H'):
    help()
    quit()
try:
    os.chdir(act)
except:
    print('The directory',act,'does not exist\n')
    quit()
filetype = input('\nWhat filetype should be deleted?\n').lower()
if filetype == '':
    if input('\nA blank filetype will WIPE YOUR DIRECTORY! Are you sure you want to continue? y/n\n').lower() == 'y':
        deletefile(filetype)
    quit()
if filetype.startswith('.'):
    filetype = filetype[1:].lower()
deletefile(filetype)

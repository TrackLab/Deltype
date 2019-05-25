# Author - TrackLab https://github.com/TrackLab
# Requirements - When using the delfiletype.exe, None.
#                When using this source code, send2trash                

from os import listdir, remove
from send2trash import send2trash

def deletefile(filetype=None):
    for f in listdir():
        if f.endswith(filetype):
            send2trash(f)       # replace with remove(f) to use python based libraries only
            print('Deleted', f)
    print('Successfully deleted all files with the filetype', filetype)
    
try:
    filetype = input('What filetype should be deleted? ').lower()
    if filetype.startswith('.'):
        filetype = filetype[1:].lower()
    if filetype == 'py':
        inp = input('That will also delete this script file. Are you sure? y/n \n').lower()
        if inp == 'y':
            deletefile(filetype)
    else:
        deletefile(filetype)
except:
    raise ValueError('No filetype to delete has been provided.')
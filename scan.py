from os import listdir
from os.path import isfile, join, isdir
import os
#import sys
#from enum import Enum
# class TYPE(Enum):
#     CRLF2LF = 0
#     LF2CRLF = 1
# type = TYPE.CRLF2LF
#for arg in sys.argv:
#    print(arg)
#    if arg == '-h':
#        print("option \"-l\" : CRLF to LF (default)")
#        print("option \"-c\" : LF to CRLF")
#        pass
#    if arg == '-l':
#        pass
#    if arg == '-c':
#        type = TYPE.LF2CRLF
#        pass
#print("type : " + type)
print("Convert file CRLF to LF")
dir_path = os.path.dirname(os.path.abspath(__file__))
print("Current dir : " + dir_path)
target_files = [dir_path+"/"+f for f in listdir(dir_path) if isfile(join(dir_path, f))]
root_dirs = [f for f in listdir(dir_path) if isdir(join(dir_path, f))]
def search_files(dir_from, dir_paths, out_files):
    for dir in dir_paths :
        fullpath = dir_from + "/" + dir
        under_dirs = [f for f in listdir(fullpath) if isdir(join(fullpath, f))]
        if len(under_dirs) > 0 :
            search_files(fullpath, under_dirs, out_files)
        files = [fullpath+"/"+f for f in listdir(fullpath) if isfile(join(fullpath, f))]
        if len(files) > 0 :
            out_files += files
    pass

search_files(dir_path, root_dirs, target_files)

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

for file_path in target_files :
    print(file_path)
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(file_path, 'wb') as open_file:
        open_file.write(content)
    pass

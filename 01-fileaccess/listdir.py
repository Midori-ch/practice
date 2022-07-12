#!/usr/bin/python3
import os

path = r'/mnt/pg/practice/01-fileaccess'
for dir_path, dir_names, file_names in os.walk(path):
    print('now-path:', dir_path)

    if len(dir_names) != 0:
        print('sub-dir:', dir_names)
    else:
        print('no sub dir inside')

    if len(file_names) != 0:
        print('file:', file_names)
    else:
        print('no file inside')

    for f in file_names:
        print('file path is:', os.path.join(dir_path, f))

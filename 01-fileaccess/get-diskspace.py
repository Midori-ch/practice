#!/usr/bin/python3
# version: v1.0

import shutil
total, used, free = shutil.disk_usage('.')

gb = 2 ** 30

print('Disk space:{:.2f} GB'.format(total / gb))
print('Used space:{:.2f} GB'.format(used / gb))
print('Free space:{:.2f} GB'.format(free / gb))

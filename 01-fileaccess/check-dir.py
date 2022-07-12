#!/usr/bin/python3
# version: v1.0
# copy file from soce to dest
# import shutil
import argparse
from os import path
import sys

parser = argparse.ArgumentParser()
parser.add_argument('src', help="source dir path")
parser.add_argument('dest', help="destnation dir path")

args = parser.parse_args()

if not path.isdir(args.src):
    print('"{}" This is not a directory'.format(args.src))
    sys.exit(2)

if not path.isdir(args.dest):
    print('"{}" This is not a directory'.format(args.dest))
    sys.exit(2)

print('Both dir. checked and exit')
sys.exit()

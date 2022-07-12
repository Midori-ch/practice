#!/usr/bin/python3
# version: v1.0
# copy file from soce to dest
# import shutil
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('src', help="source dir path")
parser.add_argument('dest', help="destnation dir path")

args = parser.parse_args()
print('source path', args.src)
print('destnation path', args.dest)

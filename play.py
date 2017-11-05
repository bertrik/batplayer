#!/usr/bin/env python

import sys
import os

# returns a list of names (with extension, without full path) of all files in folder path
def list_wav_files(path):
    files = []
    for name in os.listdir(path):
        fullpath = os.path.join(path, name)
        if os.path.isfile(fullpath) and name.endswith(".wav"):
            files.append(fullpath)
    return files 
    
def main(argv):
    if len(argv) < 2:
        path = "."
    else:
        path = argv[1];

    files = list_wav_files(path)
    print files

if __name__ == "__main__":
    main(sys.argv)


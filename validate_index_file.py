#!/usr/bin/env python
import os
from files_pb2 import FileList
from utils import get_real_path

def validate_index(f):
    fl = FileList()
    fl.ParseFromString(open(f, 'rb').read())
    for f in fl.files:
        url = get_real_path(f)
        try:
            if os.path.getsize(url)!=f.size:
                print url
        except OSError:
            print url

if __name__ == '__main__':
    import sys
    validate_index(sys.argv[1])

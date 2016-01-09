#!/usr/bin/env python
from files_pb2 import FileList

def parse(f):
    fl = FileList()
    fl.ParseFromString(open(f, 'rb').read())
    return fl

def print_summary(f):
    fl = parse(f)
    print 'version', fl.version
    print 'package version', fl.pkg_version
    print 'platform', fl.platform
    print 'file count', len(fl.files)
    print 'total size', sum(f.size for f in fl.files)

if __name__ == '__main__':
    import sys
    print_summary(sys.argv[1])
    #print parse(sys.argv[1])

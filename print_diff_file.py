#!/usr/bin/env python
from session_pb2 import CheckUpgradeResponse

def print_summary(f):
    fl = CheckUpgradeResponse()
    fl.ParseFromString(open(f, 'rb').read())
    for f in fl.files:print f.size, f.url
    print 'total size', sum(f.size for f in fl.files)

if __name__ == '__main__':
    import sys
    print_summary(sys.argv[1])


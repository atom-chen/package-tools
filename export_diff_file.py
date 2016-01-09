#!/usr/bin/env python
# coding: utf-8
from session_pb2 import CheckUpgradeResponse


import shutil
import os
import sys

def is_valid_file(f):
    if f.endswith('.DS_Store'):
        return False
    if f.endswith('.dll'):
        return False
    if f.endswith('.exe'):
        return False
    return True


def copyto(f, target):
    d = os.path.dirname(target)
    if not os.path.exists(d):
        os.makedirs(d)

    shutil.copyfile(f, target)




def print_summary(f):
    fl = CheckUpgradeResponse()
    fl.ParseFromString(open(f, 'rb').read())
    for f in fl.files:
        print f
        #if f.md5 == '394c3095f155d77bc2f397df53df3961':
        #    print f
        #    print 'is valid file : ', is_valid_file(f.url)

        if not is_valid_file(f.url):
            continue

        file_dir = f.md5[0:2]
        if not os.path.exists(os.path.join('jodo_diff_files',file_dir)):
            os.mkdir(os.path.join('jodo_diff_files',file_dir))

        if f.url.find('.') > 0:
            file_ext = f.url[f.url.rfind('.'):]
        else:
            file_ext = ''
        ipath = os.path.join('assets/',f.md5[0:2] + '/' + f.md5[2:] + file_ext)
        opath = os.path.join('jodo_diff_files/', f.md5[0:2] + '/' + f.md5[2:] + file_ext)

        copyto(ipath, opath)
    #print 'total size', sum(f.size for f in fl.files)

if __name__ == '__main__':
    import sys
    print_summary(sys.argv[1])


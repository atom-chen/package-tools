#!/usr/bin/env python
import os
import shutil
import files_pb2
from utils import file_md5_size, md5_to_path

def version_name(ver):
    return str(ver/100000.0)

def copyto(f, target):
    d = os.path.dirname(target)
    if not os.path.exists(d):
        os.makedirs(d)

    shutil.copyfile(f, target)

def pack(root, odir, version, platform):
    flist = files_pb2.FileList()
    flist.version = version
    flist.platform = platform
    flist.version_name = version_name(version)
    for r, dirs, files in os.walk(root, followlinks=True):
        r = os.path.relpath(r, root)
        if r=='.':
            r = ''
        for f in files:
            url = os.path.join(r, f)
            url = url.replace('\\', '/')
            ipath = os.path.join(root, url)
            md5, size = file_md5_size(ipath)
            opath = os.path.join(odir, md5_to_path(md5, url))
            copyto(ipath, opath)

            finfo = flist.files.add()
            finfo.url = url
            finfo.md5 = md5
            finfo.size = size
            finfo.where = files_pb2.PACKAGE

    s = flist.SerializeToString()
    open(os.path.join(odir, 'filelist'), 'wb').write(s)

if __name__ == '__main__':
    import sys
    pack(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])

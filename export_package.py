#!/usr/bin/env python
# coding: utf-8
import os
import sys
import shutil
from utils import get_real_path, ensure_directory_exists
from files_pb2 import FileList

def export_package(index_file, outdir, unpack=False):
    if os.path.exists(outdir):
        print '目标目录已存在'
        exit(1)

    fl = FileList()
    fl.ParseFromString(open(index_file, 'rb').read())

    assets_dir = os.path.dirname(index_file)

    for f in fl.files:
        p = get_real_path(f)
        print 'copy file', p
        if unpack:
            target = os.path.join(outdir, f.url)
        else:
            target = os.path.join(outdir, p)
        ensure_directory_exists(target)
        shutil.copyfile(os.path.join(assets_dir, p), target)

    shutil.copyfile(os.path.join(index_file), os.path.join(outdir, 'filelist'))

if __name__ == '__main__':
    import sys
    export_package(sys.argv[1], sys.argv[2], '-u' in sys.argv)

#!/usr/bin/env python
# coding: utf-8
import os, os.path
from copyassets import get_platform
import files_pb2


def linkassets(d, target):
    if not os.path.exists(d):
        return
    for f in os.listdir(d):
        p = os.path.relpath(os.path.join(d, f), target)
        os.symlink(p, os.path.join(target, f))


def update_platform(filelist, platform):
    '修改filelist'
    fl = files_pb2.FileList()
    fl.ParseFromString(open(filelist, 'rb').read())
    fl.platform = platform
    if os.path.islink(filelist):
        os.system('rm %s' % filelist)
    open(filelist, 'wb').write(fl.SerializeToString())


if __name__ == '__main__':
    target = 'assets'
    os.system('rm -r %s' % target)
    os.system('mkdir -p %s' % target)
    linkassets('../../assets', target)
    linkassets('extra_assets', target)

    update_platform(os.path.join(target, 'filelist'), get_platform())

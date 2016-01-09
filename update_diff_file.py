#!/usr/bin/env python
import os
import sys
from copy import copy
from files_pb2 import FileList
from session_pb2 import CheckUpgradeResponse
platform = sys.argv[1]

versionset = set()
versions = [] # [(version, valid)]
for f in os.listdir('.'):
    if ('_%s.files'%platform) not in f:
        continue
    version = int(f[:6])
    if version in versionset:
        raise Exception('collide version')
    versionset.add(version)
    if f.endswith('_%s.files'%platform):
        versions.append((version, True))
    elif f.endswith('_%s.files.invalid'%platform):
        versions.append((version, False))
versions.sort()
print 'version list', versions

recent_version = max(v for v, valid in versions if valid)
print 'recent valid version', recent_version

def update_diff_file(v1, valid, v2):
    fl1 = FileList()
    fl1.ParseFromString(open('%s_%s.files%s' % (v1, platform, '' if valid else '.invalid'), 'rb').read())
    fl2 = FileList()
    fl2.ParseFromString(open('%s_%s.files' % (v2, platform), 'rb').read())

    fileset1 = { f.url:(f.md5,f.size) for f in fl1.files }
    fileset2 = { f.url:(f.md5,f.size) for f in fl2.files }
    fileset_all = copy(fileset1)
    fileset_all.update(fileset2)

    bigupgrade = v2/100000 > v1/100000
    print 'bigupgrade', bigupgrade

    rsp = CheckUpgradeResponse(isbigupgrade=False)
    rsp.isbigupgrade = bigupgrade
    rsp.versionId = fl2.version
    rsp.versionName = fl2.version_name
    rsp.config_version = fl2.config_version

    for f in fileset_all:
        if f not in fileset2:
            # deleted
            info = rsp.files.add()
            info.url = f
            info.md5 = fileset1[f][0]
            info.size = 0
            info.new = False
        else:
            if fileset2[f] != fileset1.get(f, ('', 0)):
                info = rsp.files.add()
                info.url = f
                info.md5, info.size = fileset2[f]
                info.new = f not in fileset1

    difffile = '%s_%s.list'%(fl1.version, platform)
    print 'write diff file', difffile
    open(difffile, 'wb').write(rsp.SerializeToString())

for v,valid in versions:
    update_diff_file(v, valid, recent_version)

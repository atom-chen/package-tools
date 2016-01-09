#!/usr/bin/env python
import sys, files_pb2
from session_pb2 import CheckUpgradeResponse

def version_name(ver):
    return str(ver/100000.0)

version, platform = int(sys.argv[1]), sys.argv[2]

#flist = files_pb2.FileList()
#flist.version = version
#flist.platform = platform
#flist.version_name = version_name(version)
#open('%s_%s.list' % (version, platform), 'wb').write(flist.SerializeToString())

flist = CheckUpgradeResponse()
flist.isbigupgrade = False
flist.versionId = version
flist.versionName = version_name(version)
output = '%s_%s.list' % (version, platform)
print 'write to', output
open(output, 'wb').write(flist.SerializeToString())

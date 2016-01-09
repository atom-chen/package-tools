#!/usr/bin/env python
# coding: utf-8
import sys
import os
import shutil
from utils import get_real_path, check_file_exists
from files_pb2 import FileList

import glob

def copy_dir(d, platform=None, isios=False):
    # load filelist
    fl = FileList()
    fl.ParseFromString(open(os.path.join(d, 'filelist'), 'rb').read())
    print 'platform : ', fl.platform
    platform = platform or fl.platform
    #if isios:
    #    target_file = '%s_%s_ios.files'%(fl.version, platform)
    #else:
    #    target_file = '%s_%s.files'%(fl.version, platform)
    target_file = '%s_%s.files'%(fl.version, platform)
    if os.path.exists(target_file):
        print '该版本已存在', target_file
        exit(1)

    # copy assets
    for f in fl.files:
        if not check_file_exists(f):
            p = get_real_path(f)
            print 'copy file', p

            dd = os.path.dirname(p)
            if not os.path.exists(dd):
                os.makedirs(dd)

            shutil.copyfile(os.path.join(d, p), p)

    print 'copy file', target_file
    shutil.copyfile(os.path.join(d, 'filelist'), target_file)

    from print_index_file import print_summary
    print_summary(target_file)

def copy_apk(f):
    # uncompress to temp dir
    print u'解压到临时目录'
    tmpdir = '/tmp/apk_uncompress_temp_dir'
    os.system('rm -r %s' % tmpdir)
    assert os.system('unzip -qq "%s" -d "%s"'%(f, tmpdir))==0, '解压失败'
    copy_dir(os.path.join(tmpdir, 'assets'))

#def copy_ipa(f, platform):
def copy_ipa(f, platform=None):
    # uncompress to temp dir
    print u'解压到临时目录'
    tmpdir = '/tmp/ipa_uncompress_temp_dir'
    os.system('rm -r %s' % tmpdir)
    assert os.system('unzip -qq "%s" -d "%s"'%(f, tmpdir))==0, '解压失败'
    #copy_dir(os.path.join(tmpdir, 'Payload/lszb.app'), platform, True)
    #copy_dir(os.path.join(tmpdir, 'Payload/lszb.app'))
    for cp_dir in glob.glob( "%s/Payload/*.app"%tmpdir ) :
        copy_dir( cp_dir )

if __name__ == '__main__':
    d = sys.argv[1]
    if os.path.isdir(d):
        copy_dir(d)
    elif d.endswith('.apk'):
        copy_apk(d)
    elif d.endswith('.ipa'):
        #copy_ipa(d, sys.argv[2])
        copy_ipa(d)

#!/usr/bin/python
# coding: utf-8
import sys
import os
import re
import shutil
import files_pb2
from xml.dom.minidom import parse
from incrementalConfig_pb2 import incrementResponse
from optparse import OptionParser

boot_assets = set([
    'mc/frames.index',
    'mc/anim.index',

    'config/hzb(2500).ini',

    'config/poem.pb',
    'config/config.pb',

    'main.lua',
    'utils/protobuf.lua',
    'utils/common.lua',
    'utils/userconfig.lua',

    'win/boot.lua',
    'config/GameSettings.lua',
    'utils/enums.lua',
    'utils/curlcodes.lua',
    'ui/controls.lua',
    'ui/floattext.lua',

    'win/error.lua',
    'win/confirm.lua',
    'utils/errcode.lua',

    'mc/login.anim',
    'mc/60058.anim',
    'mc/gameUI.anim',

    'images/default.png.pkm',
    'images/b6.png.pkm',
    'mc/loding.png.pkm',
    'mc/60058.png.pkm',

    'mc/gameUI_1.png',
    'mc/login_2.png',
])

import xxtea
XXTEA_KEY = '+/yUt6mb9FCtnC2C+F'
XXTEA_SIGN = 'YYLUA'

DB_PATH = 'filelist'

mini_version = True

def has_manifest():
    return os.path.exists('AndroidManifest.xml')

def get_version():
    doc = parse(open('AndroidManifest.xml'))
    nd = doc.getElementsByTagName('manifest')[0]
    return int(nd.getAttribute('android:versionCode'))

def get_config_version( assets_dir ):
    config_version = 1

    increment_file_name = os.path.join( assets_dir, 'config/config_inc' )
    print 'increment_file_name', increment_file_name

    try:
        with open( increment_file_name, 'rb' ) as f:
            increment_response = incrementResponse()
            increment_response.ParseFromString( f.read() )
            config_version = increment_response.config_version
    except IOError:
        config_version = 1

    return config_version


def get_metadata(doc):
    d = {}
    for nd in doc.getElementsByTagName('meta-data'):
        d[nd.getAttribute('android:name')] = nd.getAttribute('android:value')
    return d


def get_package_name(doc):
    mt = get_metadata(doc)
    try:
        return mt['YYPackageName']
    except KeyError:
        nd = doc.getElementsByTagName('manifest')[0]
        return nd.getAttribute('package')


def get_platform():
    if has_manifest():
        doc = parse(open('AndroidManifest.xml'))
        return get_package_name(doc).split('.')[-1]
    else:
        return 'dummy'

def file_md5_size(f):
    import md5
    c = open(f, 'rb').read()
    return md5.md5(c).hexdigest(), len(c)

def md5_to_path(md5, url):
    ext = os.path.splitext(url)[1]
    return os.path.join(md5[:2], md5[2:]) + ext

def copyto(f, target):
    d = os.path.dirname(target)
    if not os.path.exists(d):
        os.makedirs(d)

    shutil.copyfile(f, target)

def is_valid_dir(r, platform=None):
    if '.svn' in r:
        return False
    if '.git' in r:
        return False

    if r.startswith('script'):
        return False
    if r.startswith('res'):
        return False
    if r.startswith('fla'):
        return False
    if r.startswith('fonts'):
        return False
    if r.startswith('mc_'):
        return False
    return True


ignore_files = set(['Thumbs.db', 'Thumbs.db:encryptable', 'gmon.out', 'UserDefault.xml', 'main', 'config_inc', 'assets.podspec', ])
ignore_exts = set(['.plist', '.dll', '.exe', '.a', '.fla', '.animxml', '.orig', '.mp4', '.py', '.pyc', '.pyo', '.bat', '.txt', 'xml' ])
png_exts = ['.lh', '.p8']


def is_valid_file(f, r, platform, use_png_ext):
    basename = os.path.basename(f)
    if basename.startswith('.'):
        return False
    if basename in ignore_files:
        return False
    if basename.startswith('callgrind'):
        return False

    ext = os.path.splitext(basename)[-1]
    ignore_exts1 = ignore_exts.copy()
    for e in png_exts:
        if e != use_png_ext:
            ignore_exts1.add(e)

    if ext in ignore_exts1:
        return False

    if f.lower().endswith('.png') and os.path.exists(os.path.join(root, r, f+use_png_ext)):
        return False

    if mini_version and os.path.join(r, f) not in boot_assets:
        return False

    return True


def version_name(ver):
    return '%.5f'%(ver/100000.0)

def replace_game_settings(s):
    return s

def build_assets(root, odir, version, platform, use_png_ext):
    from encrypt_png import encrypt as encrypt_png

    flist = files_pb2.FileList()
    flist.version = version
    flist.platform = platform
    flist.version_name = version_name(version)
    flist.config_version = get_config_version( root )   # 存放的是增量配置的版本号
    print 'config version :', flist.config_version

    for r, dirs, files in os.walk(root, followlinks=True):
        r = os.path.relpath(r, root)
        if r=='.':
            r = ''
        if not is_valid_dir(r, platform):
            continue

        for f in files:
            url = os.path.join(r, f)
            if not is_valid_file(f, r, platform, use_png_ext):
                continue

            url = url.replace('\\', '/')
            ipath = os.path.join(root, url)

            if f.endswith('.lua') and 'GameSettings' not in f:
                signed = XXTEA_SIGN + xxtea.encrypt(open(ipath, 'rb').read(), XXTEA_KEY)
                ipath = '/tmp/temp_compiled.lua'
                f = open(ipath, 'wb')
                f.write(signed)
                f.close()

            if url.endswith('.p8') :
                url = url[:-3]

            # png 加密
            if url.endswith( '.png' ) :
                temp_file_name = '/tmp/temp_encrypt.png'
                copyto( ipath, temp_file_name )

                encrypt_png(temp_file_name)

                ipath = temp_file_name

            md5, size = file_md5_size(ipath)
            opath = os.path.join(odir, md5_to_path(md5, url))

            copyto(ipath, opath)

            finfo = flist.files.add()
            finfo.url = url
            finfo.md5 = md5
            finfo.size = size
            finfo.where = files_pb2.PACKAGE

    s = flist.SerializeToString()
    open(os.path.join(odir, DB_PATH), 'wb').write(s)
    os.system('cp %s/filelist %s/%s_filelist' % (odir, odir, platform))

    if os.name=='nt':
        os.system('mkdir %s\\fonts'%odir)
        os.system('copy %s\\fonts\\YunYueFont.ttf %s\\fonts\\'%(root, odir))
    else:
        os.system('mkdir %s/fonts'%odir)
        os.system('cp %s/fonts/YunYueFont.ttf %s/fonts/'%(root, odir))

# 检查版本号
def check_manifest_version(src_version,target_version):
    # 修改androidmanifest.xml 版本号
    if src_version != target_version: 
        print 'fix manifest version from', src_version, 'to', target_version
        doc = parse(open('AndroidManifest.xml'))
        nd = doc.getElementsByTagName('manifest')[0]

        nd.setAttribute('android:versionCode',str(target_version))
        nd.setAttribute('android:versionName',str(version_name(int(target_version))))

        fileWriter = open('AndroidManifest.xml','w') 
        doc.writexml(fileWriter,'','','','utf-8')
        fileWriter.close()

# 恢复版本号
def restore_manifest_version():
    doc = parse(open('AndroidManifest.xml'))
    nd = doc.getElementsByTagName('manifest')[0]

    nd.setAttribute('android:versionCode','100000')
    nd.setAttribute('android:versionName','1.00000')

    fileWriter = open('AndroidManifest.xml','w') 
    doc.writexml(fileWriter)
    fileWriter.close()

def link_extra_assets(root):
    if os.path.exists(os.path.join(root, 'extra_assets')):
        print 'link extra assets'
        os.chdir(os.path.join(root, 'assets'))
        os.system('ln -s ../extra_assets/* .')


def fix_mc_directory(root, mc_postfix):
    cmd = 'cp -r %s/mc_%s/* %s/mc/ ' % (root, mc_postfix, root)
    print cmd
    assert os.system(cmd) == 0, 'fix mc failed'

    d = os.readlink(os.path.join(root, 'mc'))
    if not os.path.isabs(d):
        d = os.path.join(root, d)

    olddir = os.getcwd()
    os.chdir(os.path.join(d, '../script'))
    print 'gen index...'
    os.system('python genindex.py')
    os.chdir(olddir)


def clean_mc_directory(root):
    d = os.readlink(os.path.join(root, 'mc'))
    if not os.path.isabs(d):
        d = os.path.join(root, d)
    cmd = 'git -C %s clean -d -f' % d
    print cmd
    os.system(cmd)


parser = OptionParser()
#parser.add_option("-f", "--from", dest="root",
#                  help="path to client", metavar="DIR")
#parser.add_option("-t", "--to", dest="target",
#                  help="path to assets", metavar="DIR")
parser.add_option("-v", "--version", dest="version", type="int",
                  help="assets version", metavar="VER")
parser.add_option("--mini", dest="mini", action="store_true",
                  help="mini package", default=False, metavar="VER")
parser.add_option("--ext", dest="use_png_ext", action="store", type="string",
                  help="png compress format", default='.p8', metavar="EXT")
parser.add_option("--mc-postfix", dest="mc_postfix", action="store", type="string",
                  help="alternative mc directory", metavar="MC-POSTFIX")

if __name__ == '__main__':
    options, args = parser.parse_args()
    root, target = args

    print 'copy assets from', root, '===>', target
    mini_version = options.mini

    version = options.version
    if version and has_manifest():
        reload(sys) 
        sys.setdefaultencoding('utf8')
        check_manifest_version(get_version(), sys.argv[2])

    if not version:
        if not has_manifest():
            print '没有manifest文件，必须指定版本号!'
            sys.exit(1)
        else:
            # get version from manifest
            version = get_version()

    os.system('rm -r %s' % target)
    print 'mc postfix', options.mc_postfix
    if options.mc_postfix:
        fix_mc_directory(root, options.mc_postfix)
    try:
        print 'build assets from', root, 'to', target, 'version:', version
        build_assets(root, target, version, get_platform(), options.use_png_ext)
    finally:
        if options.mc_postfix:
            clean_mc_directory(root)
    if has_manifest():
        link_extra_assets(os.path.dirname(target))

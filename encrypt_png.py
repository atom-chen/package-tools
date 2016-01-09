#!/usr/bin/env python
# coding=utf-8

import os
import sys
from ctypes import cdll

module_directory = os.path.dirname(__file__) or '.'
# 编译贴图加密模块
old_dir = os.getcwd()
os.chdir( module_directory )
os.system( 'scons -c' )
os.system( 'scons' )
os.chdir( old_dir )

def encrypt(filename):
    if sys.platform == 'darwin':
        dll = cdll.LoadLibrary(os.path.join(module_directory, 'libtexEncrypt.dylib'))
    else:
        dll = cdll.LoadLibrary(os.path.join(module_directory, 'libtexEncrypt.so'))
    dll.encrypt_file(filename, filename)

if __name__ == '__main__':
    encrypt(sys.argv[1])

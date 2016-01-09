#!/usr/bin/env python
from optparse import OptionParser

usage = "usage: %prog command [options]"
parser = OptionParser(usage=usage)
parser.add_option("-p", "--platform",
                  action="store", type="string", dest="platform",
                  help="only create package for specified platform")
parser.add_option("-c", "--config",
                  action="store", type="string", dest="config",
                  help="spedified config file")


def pack(platform):
    pass


def packall():
    pass


def cmd_init(opt):
    pass


def cmd_list(opt):
    pass


def cmd_pack(opt):
    if 'platform' in opt:
        pack(opt['platform'])
    else:
        packall()


if __name__ == '__main__':
    (options, commands) = parser.parse_args()
    for cmd in commands:
        globals()['cmd_' + cmd](options)

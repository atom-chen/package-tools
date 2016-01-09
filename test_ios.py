#!/usr/bin/env python
# coding: utf-8

import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--labels", dest="labels", type="string",
                  help="platform labels", metavar="LABEL")

if __name__ == '__main__':
    print os.getcwd()

    options, args = parser.parse_args()

    for label in options.labels.split( '|' ):
        os.system( 'rm 120027_%s.list'%label )
        os.system( 'rm 120028_%s.list'%label )
        os.system( 'rm 120029_%s.list'%label )
        os.system( 'rm 120030_%s.list'%label )
        os.system( 'rm 120031_%s.list'%label )
        os.system( 'cp 120027_tb.list 120027_%s.list'%label )
        os.system( 'cp 120028_tb.list 120028_%s.list'%label )
        os.system( 'cp 120029_tb.list 120029_%s.list'%label )
        os.system( 'cp 120030_tb.list 120030_%s.list'%label )
        os.system( 'cp 120031_tb.list 120031_%s.list'%label )



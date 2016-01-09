#!/usr/bin/env python
# coding: utf-8

import os
from optparse import OptionParser
# -- 1 --- 2 --- 3 ---- 4 ---- 5 --- 6 -- 7 --8-- 9 --10-- 11 -- 12 -- 13 -- 14 -- 15 - 16 - 17 - 18 -- 19 -- 20 - 21 - 22 --
# "empty|amigo|huawei|lenovo|xiaomi|oppo|c360|uc|vivo|wdj|youku|baidu|anzhi|haima|cpad|gfan|m4399|kaopu|guopan|mz|yyb|pptv|haomeng|weilan"

proj_types = {
        'pokemon' : {
            'src_sdk' : 'empty',
            'sdk_list' : [ 'am',            # 金立          amigo
                           'huawei',        # 华为          huawei
                           'lenovo',        # 联想          lenovo
                           'mi',            # 小米          xiaomi
                           'oppo',          # oppo          oppo
                           'qh360',         # 360           c360
                           'uc',            # uc            uc
                           'vivo',          # vivo          vivo
                           'wdj',           # 豌豆夹        wdj
                           'youku',         # 优酷          youku
                           'baidu',         # 百度          baidu
                           'anzhi',         # 安智          anzhi
                           'hm',            # 海马-android  haima
                           'cpad',          # cool          pad
                           'gfan',          # 机锋          gfan
                           #'wyx',           # 新浪
                           'm4399',         # 4399          m4399
                           'kaopu',         # 靠谱助手-android
                           #'pptv',
                           'guopan',        # xx 果盘
                           'mz',            # 魅族
                           'yyb',           # 应用宝
                           'pptv',          # pptv
                           'haomeng',       # 好盟
                           'weilan',        # 微蓝
                           ],
            },

    'pokemon_ios' : {
            'src_sdk' : 'tb',
            'sdk_list' : [ 'as',
                           'hmios',
                           'iiapple',
                           'itools',
                           'ky',
                           'pp',
                           'xx',
                           'xy',
                           ],
            },
    }
parser = OptionParser()
parser.add_option("-v", dest="version", type="int", help="version", metavar="VER")
parser.add_option("-t", dest="type", type="string", help="type", metavar="TYPE")

if __name__ == '__main__':
    print os.getcwd()

    options, args = parser.parse_args()

    proj_type = proj_types[options.type]
    for sdk_name in proj_type['sdk_list'] :
        print sdk_name
        os.system( 'rm %d_%s.list'%(options.version, sdk_name) )
        os.system( 'ln -s %d_%s.list %d_%s.list'%(options.version, proj_type['src_sdk'], options.version, sdk_name) )



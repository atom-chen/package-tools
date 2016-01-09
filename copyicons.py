#!/usr/bin/python
import os
import sys
from copyassets import get_platform


def copy_icons(root, platform):
    icon_root = '%s/%s' % (root, platform)
    if not os.path.isdir(icon_root):
        icon_root = root
    for number, directory in [(32, 'ldpi'), (48, 'mdpi'), (72, 'hdpi'), (96, 'xhdpi'), (144, 'xxhdpi')]:
        os.system('mkdir -p res/drawable-%s' % directory)
        os.system('cp %s/%s.png res/drawable-%s/ic_launcher.png' % (icon_root, number, directory))


if __name__ == '__main__':
    copy_icons(sys.argv[1], get_platform())

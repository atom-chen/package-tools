#!/bin/sh
python copy_package.py ~/poem/program/package/android_$1/assets && python update_diff_file.py $1

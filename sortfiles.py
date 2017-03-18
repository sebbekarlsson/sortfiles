#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import glob
import sys
import os
import os.path
import shutil


if len(sys.argv) < 2:
    print('No directory provided')
    quit()

directory = sys.argv[1]
items = glob.glob('{}/*'.format(directory))


for item in items:
    obj = {}
    extension = os.path.splitext(item)[1]

    obj['extension'] = extension
    obj['fullname'] = item
    
    ext_dir = '{}/{}'.format(directory, extension.replace('.', ''))
    
    if not os.path.isdir(item) and not os.path.islink(item):
        if not os.path.isdir(ext_dir):
            os.makedirs(ext_dir)

        try:
            print('moving: {} to {}'.format(item, ext_dir))
            t = shutil.move(item.decode('utf-8'), ext_dir)
        except:
            pass

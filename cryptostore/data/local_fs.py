'''
Copyright (C) 2018-2019  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptostore.engines import StorageEngines
import os
from shutil import copyfile

def tmp_write(bucket, key, data):
    with open(data, 'rb') as fp:
        copyfile(data, os.sep.join([bucket, key, data]))


def tmp_list(bucket, key, limit=None):
    os.listdir(os.sep.join([bucket, key]))


def tmp_read(bucket, key, file_name):
    os.sep.join([bucket, key, file_name])

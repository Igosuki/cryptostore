'''
Copyright (C) 2018-2019  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptostore.engines import StorageEngines
import os
from shutil import copyfile

def tmp_write(bucket, key, data, **kwargs):
    dest = os.sep.join([bucket, key])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(data, 'rb') as fp:
        copyfile(data, dest)


def tmp_list(bucket, key, **kwargs):
    os.listdir(os.sep.join([bucket, key]))


def tmp_read(bucket, key, file_name, **kwargs):
    os.sep.join([bucket, key, file_name])

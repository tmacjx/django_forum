# coding=utf-8

import os
from uuid import uuid4


def file_rename(path):
    """ImageField 上传文件重新命名"""
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper

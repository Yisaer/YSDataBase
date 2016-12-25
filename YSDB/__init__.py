import os

from YSDB.interface import YSDB


__all__ = ['YSDB', 'connect']


def connect(dbname):
    try:
        f = open(dbname, 'r+b')
    except IOError:
        fd = os.open(dbname, os.O_RDWR | os.O_CREAT)
        f = os.fdopen(fd, 'r+b')
    return YSDB(f)

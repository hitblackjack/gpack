#!/usr/local/bin/python2.7
#coding:utf-8

import pdb

try:
    from gevent.monkey import patch_all
    patch_all(subprocess=False, aggressive=False)
    from gevent.pywsgi import WSGIServer
except ImportError:
    print 'You need install gevent manually! System shutdown.'

from config import config
from ghttp import GHTTPServer


def main():
    pdb.set_trace()
    server = WSGIServer(('', 8008), GHTTPServer(config.http_config))
    server.serve_forever()


if __name__ == '__main__':
    main()


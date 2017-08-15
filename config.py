#!/usr/local/bin/python2.7
#coding:utf-8

class Config(object):
    def __init__(self):
        self.http_config= {"upload_pack": True,
                           "receive_pack": True,
                           "git_path": "/usr/bin/git",
                           "project_root": "/db/work/code"}

config = Config()


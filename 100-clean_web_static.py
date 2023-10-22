#!/usr/bin/python3
'''Fabric script that deletes out-of-date archives'''
from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['54.196.43.161', '54.162.51.225']
env.user = 'ubuntu'
env.key_path = '~/.ssh/id_rsa'


def do_clean(number=0):
    '''deletes out-of-date archives'''
    number = 1 if int(number) == 0 else int(number)
    curr_archives = sorted(local('ls -1t versions', capture=True).split('\n'))

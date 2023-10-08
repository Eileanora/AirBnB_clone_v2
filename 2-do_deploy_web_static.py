#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, \
using the function do_deploy"""
from fabric.api import *
from os import path


env.hosts = ['54.196.43.161', '54.162.51.225']
env.user = 'ubuntu'
env.key_path = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    '''function to deploy the archive'''
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        file_name_no_ext = file_name.split('.')[0]
        folder_path = '/data/web_static/releases/'
        run('mkdir -p {}{}/'.format(folder_path, file_name_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, folder_path,
                                                file_name_no_ext))
        run('rm /tmp/{}'.format(file_name))
        # delete symbolic link
        run('rm -rf /data/web_static/current')
        # create new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(folder_path,
                                                           file_name_no_ext))
        return True
    except:
        return False

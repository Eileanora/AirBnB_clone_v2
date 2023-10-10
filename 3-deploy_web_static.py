#!/usr/bin/python3
'''Fabric script that creates and distributes an archive to your web servers,
using the function deploy'''
from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['54.196.43.161', '54.162.51.225']
env.user = 'ubuntu'
env.key_path = '~/.ssh/id_rsa'


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(file))
    if result.failed:
        return None
    else:
        return file


def deploy():
    '''creates archive to web servers'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_deploy(archive_path):
    '''deploy the archive'''
    if not path.exists(archive_path):
        return False

    try:
        # make tmp dir to upload file
        put(archive_path, '/tmp/')
        # set file name and folder path to extract in it
        file_name = archive_path.split('/')[-1]
        file_name_no_ext = file_name.split('.')[0]
        folder_path = '/data/web_static/releases/' + file_name_no_ext + '/'
        # create dir to extract file in it
        run('mkdir -p {}'.format(folder_path))
        # extract file
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, folder_path))
        # delete archive after extract it
        run('rm /tmp/{}'.format(file_name))
        # move all files from web_static to folder_path
        run('mv {}/web_static/* {}'.format(folder_path, folder_path))
        # delete symbolic link
        run('rm -rf /data/web_static/current')
        # create new symbolic link
        run('ln -sf {} /data/web_static/current'.format(folder_path))
        return True
    except Exception:
        return False

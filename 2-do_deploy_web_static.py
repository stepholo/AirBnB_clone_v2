#!/usr/bin/python3
""" Module to distribute an archive to the web server"""

from fabric.api import put, env, task, run
import os

env.user = 'ubuntu'
env.hosts =['54.87.160.173', '54.162.87.193']
env.key_filename = '~/.ssh/school'


@task
def do_deploy(archive_path):
    """Function to distribute an archive to your web servers
        Param:
            archive_path: Path to the archived file
    """
    if os.path.exists(archive_path) == False:
        return False

    f_name = os.path.basename(archive_path)
    basef_name = os.path.splitext(f_name)[0]
    remote_path =  f"/tmp/{f_name}"

    put(archive_path, remote_path)
    run(f'mkdir -p /data/web_static/releases/{basef_name}/')
    run(f'tar -xzf /tmp/{f_name} -C /data/web_static/releases/{basef_name}')
    run(f'rm /tmp/{f_name}')
    run(f'mv /data/web_static/releases/{basef_name}/web_static/* /data/web_static/releases/{basef_name}')
    run(f'rm -rf /data/web_static/releases/{basef_name}/web_static')
    run('rm -rf /data/web_static/current')
    run(f'ln -s /data/web_static/releases/{basef_name} /data/web_static/current')

    print("New version deployed!")
    return True

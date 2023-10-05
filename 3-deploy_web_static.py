#!/usr/bin/python3
"""Module to define a fab file"""

from fabric.api import local, put, env, run
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.87.160.173', '54.162.87.193']
env.key_filename = '~/.ssh/school'

arch_path = []


def do_pack():
    """Function that generates a .tgz archive from the contents
       of the web_static folder of your AirBnB Clone repo, using
       the function do_pack
    """
    t = datetime.now()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
            t.year,
            t.month,
            t.day,
            t.hour,
            t.minute,
            t.second
            )

    name = f"versions/{file_name}"
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -czvf {} web_static".format(name)).failed is True:
        return None
    size = os.path.getsize(name)
    print("web_static packed: {} -> {}Bytes".format(name, size))
    return name


def do_deploy(archive_path):
    """Function to distribute an archive to your web servers
        Param:
            archive_path: Path to the archived file
    """

    if os.path.exists(archive_path) is False:
        return False

    f_name = os.path.basename(archive_path)
    basef_name = os.path.splitext(f_name)[0]
    remote_path = f"/tmp/{f_name}"

    target_d = f"/data/web_static/releases/{basef_name}"
    link = "/data/web_static/current"
    mv = f"/data/web_static/releases/{basef_name}/web_static/*"
    rm = f"/data/web_static/releases/{basef_name}/web_static"

    if put(archive_path, remote_path).failed is True:
        return False
    if run(f'mkdir -p /data/web_static/releases/{basef_name}/').failed is True:
        return False
    if run(f'tar -xzf /tmp/{f_name} -C {target_d}').failed is True:
        return False
    if run(f'rm /tmp/{f_name}').failed is True:
        return False
    if run(f'mv {mv} {target_d}').failed is True:
        return False
    if run(f'rm -rf /{rm}').failed is True:
        return False
    if run(f'rm -rf {link}').failed is True:
        return False
    if run(f'ln -s {target_d} {link}').failed is True:
        return False

    print("New version deployed!")
    return True


def deploy():
    """ Function that creates and distributes an archive to your web servers
    """
    global arch_path
    if not arch_path:
        file = do_pack()
        if file is None:
            return False
        arch_path.append(file)

    return do_deploy(arch_path[0])

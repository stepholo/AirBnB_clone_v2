#!/usr/bin/python3
"""Module to define a fab file"""

from fabric.api import local
from datetime import datetime
import os


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

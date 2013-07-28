#/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for i in ["pmount", "pumount"]:
        os.chmod("/usr/bin/%s" % i, 04755)


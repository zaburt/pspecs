#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    # add TCMALLOC for google-perftools
    autotools.make('DEBUG="" CFLAGS="%s" USE_TCMALLOC=yes all' % get.CFLAGS())

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    pisitools.insinto("/etc", "redis.conf")
    shelltools.chmod("%s/etc/redis.conf" % get.installDIR(), 0644)

    for d in ["lib", "log", "run"]:
        dest = "/var/%s/redis" % d
        pisitools.dodir(dest)
        shelltools.chmod("%s/%s" % (get.installDIR(), dest), 0755)

    pisitools.dodir("/usr/sbin")
    pisitools.domove("/usr/bin/redis-server", "/usr/sbin/")

    # No soup for you
    shelltools.chmod("%s/usr/bin/redis-benchmark" % get.installDIR(), 0750)

    pisitools.dodoc("00-RELEASENOTES", "BUGS", "CONTRIBUTING", "COPYING", "README", "TODO")


#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    autotools.autoconf()
    autotools.configure("--with-jemalloc-prefix=j \
                         --enable-stats \
                         --disable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("ChangeLog", "README*", "COPYING")
    pisitools.dohtml("doc/jemalloc.html")


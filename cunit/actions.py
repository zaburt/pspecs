#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "CUnit-%s.%s-%s" % tuple(get.srcVERSION().split("."))

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-curses")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/doc/CUnit", "%s/%s/html" % (get.docDIR(), get.srcNAME()))
    pisitools.removeDir("/usr/doc")

    # static library is said to be usable
    # pisitools.remove("/usr/lib/libcunit.a")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS", "TODO")


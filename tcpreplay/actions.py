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
    autotools.configure("--enable-dynamic-link \
                         --enable-tcpreplay-edit \
                         --with-testnic=eth0 \
                         --with-testnic2=eth1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib")
    pisitools.dodoc("README", "docs/CHANGELOG", "docs/CREDIT", "docs/HACKING", "docs/LICENSE", "docs/TODO")


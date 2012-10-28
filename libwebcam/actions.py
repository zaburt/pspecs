#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("CMAKE_INCLUDE_PATH", "../common/include")

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")

    pisitools.remove("/usr/lib/*.a")
    pisitools.dodoc("libwebcam/README", "libwebcam/COPYING.LESSER")

    for i in ["README", "COPYING"]:
        pisitools.insinto("/%s/%s/" %(get.docDIR(), get.srcNAME()), "uvcdynctrl/%s" % i, "%s.uvcdynctrl" % i)


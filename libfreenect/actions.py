#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("*/CMakeLists.txt", "^set.*CMAKE_C_FLAGS.*$")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_C_FLAGS='%s'" % get.CFLAGS(), sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make("VERBOSE=1")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")

    pisitools.insinto("/lib/udev/rules.d", "platform/linux/udev/*.rules")
    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("doc/*", "GPL2", "APACHE20", "README*", "HACKING")

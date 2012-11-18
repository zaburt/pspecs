#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Onur Küçük <onur@delipenguen.net>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


libmk = "libmk4.so"
apiver = "2.4"
pylibdir = "/usr/lib/%s/site-packages" % get.curPYTHON()


def setup():
    shelltools.system('CXXFLAGS="%s" unix/configure \
                       --with-tcl=/usr/include,/usr/lib \
                       --prefix="/usr" \
                       --libdir="/usr/lib" \
                       --infodir="/usr/share/info" \
                       --mandir="/usr/share/man"' % get.CXXFLAGS())

def build():
    autotools.make('SHLIB_LD="%s -shared -Wl,-soname,%s.%s"' % (get.CXX(), libmk, apiver.split(".")[0]))
    autotools.make('SHLIB_LD="%s -shared" \
                    pyincludedir="/usr/include/%s" \
                    python' % (get.CXX(), get.curPYTHON()))
                    # PYTHON_LIB="%s" get.curPYTHON() \

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir(pylibdir)
    autotools.rawInstall("DESTDIR=%s pylibdir='%s' install-python" % (get.installDIR(), pylibdir))

    pisitools.rename("/usr/lib/%s" % libmk, "%s.%s" % (libmk, apiver))

    suffixMinor = ""
    for i in apiver.split("."):
        pisitools.dosym("%s.%s" % (libmk, apiver), "/usr/lib/%s%s" % (libmk, suffixMinor))
        suffixMinor += ".%s" % i

    pisitools.dodoc("CHANGES", "README", "NOTES*")
    pisitools.dohtml("Metakit.html")
    pisitools.dohtml("doc/*")


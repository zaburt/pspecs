#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Onur Küçük <onur@delipenguen.net>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

# def setup():
#     autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%(dest)s" \
                          DESTDIR="%(dest)s" \
                          DOCS_DEST="%(dest)s/%(docdir)s/%(pkgname)s" \
                          PAM_USB_DEST="%(dest)s/lib/security"' % {
                              "dest": get.installDIR(),
                              "docdir": get.docDIR(),
                              "pkgname": get.srcNAME()
                          })

    pisitools.dodoc("ChangeLog", "COPYING", "README*")

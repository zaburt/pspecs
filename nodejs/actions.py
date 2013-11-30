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


def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --shared-openssl")

def build():
    autotools.make()

#def check():
#    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING.md", "LICENSE", "README*")
    pisitools.dohtml("doc/api/*")



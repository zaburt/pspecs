#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    for i in ['iptraf', 'rvnamed']:
        pisitools.dosbin("%s-ng" % i)

    pisitools.doman('src/*.8')
    pisitools.dodoc('AUTHORS', 'CHANGES', 'FAQ', 'LICENSE', 'README*', 'RELEASE-NOTES')
    pisitools.dohtml('Documentation/*')

    for i in ['lib', 'log', 'lock']:
        pisitools.dodir("/var/%s/iptraf-ng" % i)


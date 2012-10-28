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
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    autotools.autoreconf("-vfi")
    autotools.configure("--with-gpm \
                         --enable-bittorrent \
                         --enable-finger \
                         --enable-gopher \
                         --enable-html-highlight \
                         --enable-nntp \
                         --enable-smb \
                         --with-gssapi \
                         --with-spidermonkey \
                         --enable-true-color \
                         --enable-256-colors")
                         # --without-x \
                         # --with-nss_compat_ossl \
                         # --with-python \
                         # --with-ruby \

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/share/locale/locale.alias")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README*","SITES", "THANKS", "TODO")

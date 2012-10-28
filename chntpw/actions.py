#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir = "chntpw-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    # autotools.configure()
    autotools.make("clean")

def build():
    autotools.make('CC="%s" \
                    CFLAGS="%s -Wall -DUSEOPENSSL" \
                    LIBS="-lcrypto"' % (get.CC(), get.CFLAGS()))

def install():
    for i in ["chntpw", "cpnt", "reged"]:
        pisitools.dobin(i)

    for i in ["COPYING", "GPL", "HISTORY", "LGPL", "README", "regedit", "syskey", "WinReg"]:
        pisitools.dodoc("%s.txt" % i)


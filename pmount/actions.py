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
    autotools.configure("--enable-hal=no \
                         --with-lock-dir=/var/lock/pmount \
                         --with-whitelist=/etc/pmount.allow")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README*", "NEWS")

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

WorkDir = "tty-clock-master"


def build():
    autotools.make()

def install():
    pisitools.dobin("tty-clock")
    pisitools.doman("tty-clock.1")
    pisitools.dodoc("README*")


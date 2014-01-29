#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Onur Küçük <onur@delipenguen.net>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "PostgreSQL-Temporal"


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/postgresql")
    pisitools.dodoc("Changes", "COPYRIGHT", "LICENSE", "META.json", "README*", "doc/*.*")
    pisitools.dohtml("doc/html/")


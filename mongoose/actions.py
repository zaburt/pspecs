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

import os

WorkDir = "mongoose"

LIBSUFFIX = "3.3"
LIBNAME = "libmongoose.so"
LIBDIR = "/usr/lib"


def fixPerms(base):
    print "working on %s" % base
    for root, dirs, files in os.walk(base):
        for name in dirs:
            os.chmod(os.path.join(root, name), 0755)
        for name in files:
            os.chmod(os.path.join(root, name), 0644)


def build():
    autotools.make('CFLAGS="%s -lssl -lcrypto -DNO_SSL_DL" \
                    MONGOOSE_LIB_SUFFIX=".%s" \
                    linux' % (get.CFLAGS(), LIBSUFFIX))

def install():
    pisitools.dobin('mongoose')
    pisitools.dolib_so("%s.%s" % (LIBNAME, LIBSUFFIX), LIBDIR)

    suffixMinor = ""
    for i in LIBSUFFIX.split("."):
        pisitools.dosym("%s.%s" % (LIBNAME, LIBSUFFIX), "/usr/lib/%s%s" % (LIBNAME, suffixMinor))
        suffixMinor += ".%s" % i

    pisitools.doman('mongoose.1')
    pisitools.dodoc("LICENSE")

    for i in ['bindings', 'examples', 'test']:
        pisitools.insinto("%s/%s/" % (get.docDIR(), get.srcNAME()), i)

    fixPerms("%s/%s" % (get.installDIR(), get.docDIR()))


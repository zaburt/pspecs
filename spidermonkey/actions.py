# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = "js/src"
WorkDir = "js-%s" % get.srcVERSION()

def setup():
    shelltools.cd("js/src")
    # autotools.autoconf()
    autotools.configure("--with-system-nspr \
                         --enable-threadsafe \
                        --enable-readline")

    #autotools.make("-j1 -f Makefile.ref \
    #                JS_THREADSAFE=1 \
    #                CC=%s CCC=%s \
    #                XCFLAGS='%s -fPIC -DJS_C_STRINGS_ARE_UTF8' \
    #                XLDFLAGS='%s' \
    #                BUILD_OPT='1'"
    #                % (get.CC(), get.CXX(),
    #                   get.CFLAGS(), get.LDFLAGS()))

def build():
    shelltools.cd("js")
    autotools.make("-C src")

def install():
    # make is picky about the order of install
    # autotools.make("-f Makefile.ref install DESTDIR=%s" % (get.installDIR()))

    shelltools.cd("js")
    autotools.rawInstall("-C src DESTDIR=%s" % (get.installDIR()))

    pisitools.remove("/usr/bin/js-config")
    for i in ["src/jscpucfg", "src/shell/js"]:
        pisitools.dobin(i)

    pisitools.remove("/usr/lib/*.a")

    # Make versioned *.so and create needed symlinks
    # pisitools.rename("/usr/lib/libjs.so", "libjs.so.1")
    # pisitools.dosym("/usr/lib/libjs.so.1", "/usr/lib/libjs.so")

    pisitools.dosym("libmozjs185.so.1.0", "/usr/lib/libmozjs.so.1")
    pisitools.dosym("libmozjs185.so.1.0", "/usr/lib/libjs.so.1")
    pisitools.dosym("libmozjs185.so", "/usr/lib/libmozjs.so")
    pisitools.dosym("libmozjs185.so", "/usr/lib/libjs.so")

    shelltools.chmod("%s/usr/include/js/*" % get.installDIR(), 0644)

    # pisitools.dodoc("../jsd/README")
    # pisitools.dohtml("README.html")


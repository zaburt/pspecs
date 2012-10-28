#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import grp
import pwd


def hav(method, args):
    try:
        call("baselayout", "User.Manager", method, args)
    except:
        pass

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # build user -> group map for migration
    def deleteGroup(group):
        try:
            gid = grp.getgrnam(group)[2]
            # deleteGroup(gid)
            hav("deleteGroup", (gid))
        except KeyError:
            pass

    def deleteUser(user):
        try:
            uid = pwd.getpwnam(user)[2]
            # deleteUser(uid, delete_files)
            hav("deleteUser", (uid, False))
        except KeyError:
            pass

    # Remove old groups/users
    groups = ["redis"]
    users = ["redis"]

    for group in groups:
        deleteGroup(group)

    for user in users:
        deleteUser(user)

    # addGroup(gid, name)
    hav("addGroup", (301, "redis"))

    # addUser (uid, login, realname, homedir, shell, password, groups, grantedauths, blockedauths)
    hav("addUser", (301, "redis", "Redis Server", "/var/lib/redis", "/bin/false", "", ["redis"], [], []))

    # Give ownership to newly added users
    for d in ["lib", "log", "run"]:
        dest = "/var/%s/redis" % d
        os.chown(dest, 301, 0)
        os.chmod(dest, 0755)



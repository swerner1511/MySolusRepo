#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    pisitools.insinto("/opt/idea-ce", "idea-IC-*/*")
    pisitools.dosym("/opt/idea-ce/bin/idea.sh", "/usr/bin/idea-ce")

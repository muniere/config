"""
Extend package of standard os package
"""

# 1st
import os
import subprocess

# 2nd
from .. import fs

UBUNTU = "ubuntu"
DEBIAN = "debian"
CENTOS = "centos"
AMAZON = "amazon"
DARWIN = "darwin"


def islinux():
    return sysname() in [UBUNTU, DEBIAN, CENTOS, AMAZON]


def isbsd():
    return sysname() in [DARWIN]


def isdebian():
    return sysname() in [UBUNTU, DEBIAN]


def isredhat():
    return sysname() in [CENTOS, AMAZON]


def isdarwin():
    return sysname() in [DARWIN]


def sysname():
    """
    Detect system name

    :return: Detected name
    """
    issue = fs.pilot("/etc/issue")

    if issue.isfile():
        rawname = issue.read().lower()
    else:
        rawname = subprocess.check_output(["uname", "-a"]).strip().lower()

    if "ubuntu" in rawname:
        return UBUNTU

    if "debian" in rawname:
        return DEBIAN

    if "centos" in rawname:
        return CENTOS

    if "amzn" in rawname:
        return AMAZON

    if "darwin" in rawname:
        return DARWIN

    return None

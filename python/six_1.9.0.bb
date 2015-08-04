SUMMARY = "It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions."
AUTHOR = "gutworth"
SECTION = "python/utils"
LICENSE = "MIT"
PR = "r1"

SRC_URI = "https://pypi.python.org/packages/source/s/six/six-1.9.0.tar.gz;protocol=https;name=six"
SRCREV_six = "${AUTOREV}"

SRC_URI[six.md5sum] = "476881ef4012262dfc8adc645ee786c4"
SRC_URI[six.sha256sum] = "e24052411fc4fbd1f672635537c3fc2330d9481b18c0317695b46259512c91d5"


S = "${WORKDIR}/six-${PV}"
LIC_FILES_CHKSUM = "file://${WORKDIR}/six-1.9.0/LICENSE;md5=6f00d4a50713fa859858dd9abaa35b21"

inherit distutils

RDEPENDS_${PN} = "python"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"
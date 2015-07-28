SUMMARY = "It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions."
AUTHOR = "gutworth"
SECTION = "python/utils"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=476881ef4012262dfc8adc645ee786c4"
PR = "r1"

SRC_URI = "https://pypi.python.org/packages/source/s/six/six-1.9.0.tar.gz;protocol=https;name=six"
SRCREV_six = "476881ef4012262dfc8adc645ee786c4"


S = "${WORKDIR}/git"

inherit distutils

SRC_URI[six.md5sum] = "476881ef4012262dfc8adc645ee786c4"
SRC_URI[six.sha256sum] = "e24052411fc4fbd1f672635537c3fc2330d9481b18c0317695b46259512c91d5"

RDEPENDS_${PN} = "python"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"
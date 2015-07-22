SUMMARY = "It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions."
AUTHOR = "gutworth"
SECTION = "python/utils"
LICENSE = "MIT"
LIC_FILES_CHKSUM = ";md5="
PR = "r1"

SRC_URI = "https://pypi.python.org/packages/source/s/six/six-1.9.0.tar.gz#md5=476881ef4012262dfc8adc645ee786c4; protocol=https; name=six"
SRCREV_six = "476881ef4012262dfc8adc645ee786c4"


S = "${WORKDIR}/six-${PV}"

inherit distutils

SRC_URI[md5sum] = "476881ef4012262dfc8adc645ee786c4"
SRC_URI[sha256sum] = "https://pypi.python.org/packages/source/s/six/six-1.9.0.tar.gz#md5=476881ef4012262dfc8adc645ee786c4"

RDEPENDS_${PN} = "python \

"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"
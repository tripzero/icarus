SUMMARY = "A solar-tracking python2.7 package"
AUTHOR = "Kevron Rees / Ryan Kapur"
SECTION = "devel/python"
LICENSE = "GPL v3"
LIC_FILES_CHKSUM = "file://LICENSE;md5=f87832d854acbade6e9f5c601c8b30b1"
PR = "r1"


SRC_URI = "git://github.com/tripzero/icarus; protocol=https; branch=master; name=icarus"
SRCREV_icarus = "4e533bc5cb84dffa944c96dbce20ded6a8961dec"

S = "${WORKDIR}/icarus-${PV}"

inherit distutils

SRC_URI[md5sum] = "https://github.com/tripzero/icarus"
SRC_URI[sha256sum] = "https://github.com/tripzero/icarus"

RDEPENDS_${PN} = "python-datetime \
                  python-distutils \
                  python-twisted \
                  autobahn \
                  pysolar \

"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"
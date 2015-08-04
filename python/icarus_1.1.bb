SUMMARY = "A solar-tracking python2.7 package"
AUTHOR = "Kevron Rees / Ryan Kapur"
SECTION = "devel/python"
LICENSE = "GPL &|() v3"
LIC_FILES_CHKSUM = "file://../LICENSE;md5=25905bd825ed9118dc55c3ba118f6c29"
PR = "r1"


SRC_URI = "git://github.com/tripzero/icarus;protocol=https;branch=master;name=icarus"
SRCREV_icarus = "6f742ac796a2d61c911d970a37701b03965c7156"

S = "${WORKDIR}/git/python"

inherit distutils

SRC_URI[md5sum] = "https://github.com/tripzero/icarus"
SRC_URI[sha256sum] = "https://github.com/tripzero/icarus"

RDEPENDS_${PN} = "python-datetime \
                  python-distutils \
                  autobahn \
                  six \
                  pysolar"
                  
RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"
SUMMARY = "Python libraries simulating irradiation of any point on earth by the sun version 0.6"
AUTHOR = "Brandon Stafford"
SECTION = "devel/python"
LICENSE = "GPL &|() v3"
LIC_FILES_CHKSUM = "file://COPYING;md5=48f95c8895cb8918ef07b761f3a7ee1f"
PR = "r1"

SRC_URI = "git://github.com/pingswept/pysolar;protocol=https;branch=master;name=pysolar"
SRCREV_pysolar = "37fcbf1551ea55216b02c5f99b3e7c579f878e85"

S = "${WORKDIR}/git"
inherit distutils

SRC_URI[md5sum] = "37fcbf1551ea55216b02c5f99b3e7c579f878e85"
SRC_URI[sha256sum] = "https://github.com/pingswept/pysolar"

RDEPENDS_${PN} = "python \
                  python-datetime \
                  python-distutils \
                  python-pytz"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"

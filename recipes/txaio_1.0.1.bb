SUMMARY = "Utilities to support code running unmodified on Twisted + asyncio"
SECTION = "python/utils"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=92f7efe35161605ba200554c84c2b04b"
PR = "r1"

SRC_URI = "git://github.com/tavendo/txaio.git;protocol=https;branch=master;name=txaio"
#SRCREV_txaio = "abb9af9c02055467a553ee05607b8ae00c1b5cdb"
SRCREV_txaio = "${AUTOREV}"

S = "${WORKDIR}/git"

inherit distutils

SRC_URI[txaio.md5sum] = "4fe1681ec20dec538034b0c4cc8a4afd"
SRC_URI[txaio.sha256sum] = "c2ddbaf003c68f64ba1c79c70395555d6ccaee512213405447c06fb2c89f1c8a"


DEPENDS = "six \
           python-distutils \
"

RDEPENDS_${PN} = "python \
                  python-distutils \
                  six \
"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"

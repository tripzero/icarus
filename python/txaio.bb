SUMMARY = "Utilities to support code running unmodified on Twisted + asyncio"
SECTION = "python/utils"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "https://github.com/tavendo/txaio/blob/master/LICENSE;md5="
PR = "r1"

SRC_URI = "https://github.com/tavendo/txaios; protocol=https; branch=master; name=txaio"
SRCREV_txaio = "abb9af9c02055467a553ee05607b8ae00c1b5cdb"
S = "${WORKDIR}/txaio-${PV}"

inherit distutils

SRC_URI[md5sum] = "abb9af9c02055467a553ee05607b8ae00c1b5cdb"
SRC_URI[sha256sum] = "https://github.com/tavendo/txaio"

RDEPENDS_${PN} = "python \
                  python-distutils \
                  six \
                  twisted \

"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"
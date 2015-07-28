SUMMARY = "Utilities to support code running unmodified on Twisted + asyncio"
SECTION = "python/utils"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=2d637a300056bdc81e6263b7075c9150"
PR = "r1"

SRC_URI = "https://github.com/tavendo/txaio;protocol=http;branch=master;name=txaio"
SRCREV_txaio = "abb9af9c02055467a553ee05607b8ae00c1b5cdb"

S = "${WORKDIR}/git"

inherit distutils

SRC_URI[txaio.md5sum] = "2d637a300056bdc81e6263b7075c9150"
SRC_URI[txaio.sha256sum] = "e29f7eb7646b41ae85711da3de8ba966bc6962316353ce1610cb81e375ad47b6"

RDEPENDS_${PN} = "python \
                  python-distutils \
                  six \
                  python-twisted \
"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"

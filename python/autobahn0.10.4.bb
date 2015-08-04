SUMMARY = "Provides open-source implementations of WebSocket Protocol/WAMP"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=92f7efe35161605ba200554c84c2b04b"
PR = "r1"

SRC_URI = "git://github.com/tavendo/AutobahnPython;protocol=https;branch=master;name=autobahn"
SRCREV_autobahn = "${AUTOREV}"

S = "${WORKDIR}/git"

inherit distutils

SRC_URI[md5sum] = "3bcbc00382a9d601fe4565216d4e7dc737d5f65e"
SRC_URI[sha256sum] = "https://github.com/tavendo/AutobahnPython"

RDEPENDS_${PN} = "python \
                  python-datetime \
                  python-distutils \
                  python-twisted \
                  six \
                  txaio \ 
"

RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"

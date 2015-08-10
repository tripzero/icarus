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

DEPENDS = "txaio \
           six \
           python-twisted \
           python-distutils \
          "

RDEPENDS_${PN} = "python \
                  python-datetime \
                  python-distutils \
                  python-twisted \
                  python-twisted-web \
                  six \
                  txaio \ 
"

FILES_${PN} = " \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/__init__.py* \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/util.py* \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn-0.10.5-py2.7.egg/ \
    "

FILES_${PN}-twisted = " \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/twisted/*.py* \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/twisted \
"

FILES_${PN}-wamp = " \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/wamp/*.py* \
    #${libdir}/${PYTHON_DIR}/site-packages/autobahn/wamp \
"

FILES_${PN}-websocket = " \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/websocket/*.py* \
    ${libdir}/${PYTHON_DIR}/site-packages/autobahn/websocket \
"


RDEPENDS_${PN}_class-native = ""

BBCLASSEXTEND = "native nativesdk"

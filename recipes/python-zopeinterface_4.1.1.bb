SUMMARY = "Interface definitions for Zope products"
SECTION = "console/network"

LICENSE = "ZPL-2.1"


SRC_URI = "https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.1.tar.gz;protocol=http;name=zopeinterface"
SRC_URI[zopeinterface.md5sum] = "edcd5f719c5eb2e18894c4d06e29b6c6"
SRC_URI[zopeinterface.sha256sum] = "91cba7b7cd7cb82f6f4e023fe77f94dc3df4ae5287fd55def2148dc232d0c7da"
SRCREV_zopeinterface = "${AUTOREV}"


S = "${WORKDIR}/zope.interface-${PV}"

LIC_FILES_CHKSUM = "file://${WORKDIR}/zope.interface-4.1.1/LICENSE.txt;beginline=8;endline=8;md5=68b329da9893e34099c7d8ad5cb9c940"

inherit setuptools

RPROVIDES_${PN} += "zope-interfaces"
FILES_${PN}-dbg += "${PYTHON_SITEPACKAGES_DIR}/*.egg/*/*/.debug"
FILES_${PN}-dev += "${PYTHON_SITEPACKAGES_DIR}/zope/interface/*.c"
FILES_${PN}-doc += "${PYTHON_SITEPACKAGES_DIR}/zope/interface/*.txt"
FILES_${PN}-tests = " \
        ${PYTHON_SITEPACKAGES_DIR}/zope/interface/tests \
        ${PYTHON_SITEPACKAGES_DIR}/zope/interface/common/tests \
"
DESCRIPTION = "World timezone definitions, modern and historical"
HOMEPAGE = "http://pytz.sourceforge.net"
SECTION = "devel/python"
LICENSE = "MIT"


SRC_URI = "https://pypi.python.org/packages/source/p/pytz/pytz-2015.4.tar.gz;protocol=https;branch=master;name=pytz"
SRCREV_pytz = "${AUTOREV}"

SRC_URI[pytz.md5sum] = "417a47b1c432d90333e42084a605d3d8"
SRC_URI[pytz.sha256sum] = "c4ee70cb407f9284517ac368f121cf0796a7134b961e53d9daf1aaae8f44fb90"


S = "${WORKDIR}/pytz-${PV}"
LIC_FILES_CHKSUM = "file://${WORKDIR}/pytz-${PV}/LICENSE.txt;md5=22b38951eb857cf285a4560a914b7cd6"

inherit setuptools
#
# Copyright OpenEmbedded Contributors
#
# SPDX-License-Identifier: GPL-2.0-only
#

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

BBIMPORTS = ["oe.data", "oe.path", "oe.utils", "oe.types", "oe.package", \
             "oe.packagegroup", "oe.sstatesig", "oe.lsb", "oe.cachedpath", "oe.license", \
             "oe.qa", "oe.reproducible", "oe.rust", "oe.buildcfg"]

# -*- coding: utf-8 -*-
# PyTils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
#
# http://gorod-omsk.ru/blog/pythy/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Unit tests for pytils
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"
__all__ = ["test_numeral", "test_dt", "test_translit", "test_utils"]

import unittest

def get_suite():
    """Return TestSuite for all unit-test of PyTils"""
    suite = unittest.TestSuite()
    for module_name in __all__:
        imported_module = __import__("pytils.test."+module_name,
                                       globals(),
                                       locals(),
                                       ["pytils.test"])
        loader = unittest.defaultTestLoader
        suite.addTest(loader.loadTestsFromModule(imported_module))

    return suite

def run(verbosity=1):
    """Run all unit-test of PyTils"""
    suite = get_suite()
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

if __name__ == '__main__':
    run(2)

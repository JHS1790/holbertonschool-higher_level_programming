"""base_test.py: unit test for module/base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """TestBase: Test the Base class"""

    def test_id(self):
        """test_id: function for testing Base class id assignment"""
        id1 = Base()
        self.assertAlmostEqual(id1.id, 1)
        id2 = Base()
        self.assertAlmostEqual(id2.id, 2)
        id12 = Base(12)
        self.assertAlmostEqual(id12.id, 12)

"""rectangle_test.py: unit test for module/rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangleCreation(unittest.TestCase):
    """TestRectangle: Test the creation of the Rectangle class"""

    def test_id(self):
        """test_id: method for testing Rectangle class id assignment"""
        id1 = Rectangle(1, 1)
        self.assertAlmostEqual(id1.id, 2)
        id2 = Rectangle(2, 2)
        self.assertAlmostEqual(id2.id, 3)
        id12 = Rectangle(3, 3, 3, 3, 12)
        self.assertAlmostEqual(id12.id, 12)

    def test_width(self):
        """test_width: method for testing Rectangle class width assignment"""
        recwidth = Rectangle(3, 4, 1, 2)
        self.assertAlmostEqual(recwidth.width, 3)

    def test_height(self):
        """test_height: method for testing Rectangle class height assignment"""
        recheight = Rectangle(3, 4, 1, 2)
        self.assertAlmostEqual(recheight.height, 4)

    def test_x(self):
        """test_x: method for testing Rectangle class x assignment"""
        recx = Rectangle(3, 4, 1, 2)
        self.assertAlmostEqual(recx.x, 1)

    def test_y(self):
        """test_y: method for testing Rectangle class y assignment"""
        recy = Rectangle(3, 4, 1, 2)
        self.assertAlmostEqual(recy.y, 2)

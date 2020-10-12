"""rectangle_test.py: unit test for module/rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangleCreation(unittest.TestCase):
    """TestRectangleCreation: Test the creation of the Rectangle class"""

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


class TestRectangleFailure(unittest.TestCase):
    """TestRectangleFailure: Test raised exceptions from Rectangle class
    creation
    """

    def test_width_failure(self):
        """test_width_failure: test width exceptions"""
        with self.assertRaises(TypeError): Rectangle("boi", 3)
        with self.assertRaises(ValueError): Rectangle(-5, 2)

    def test_height_failure(self):
        """test_height_failure: test height exceptions"""
        with self.assertRaises(TypeError): Rectangle(2, [])
        with self.assertRaises(ValueError): Rectangle(4, -5)

    def test_x_failure(self):
        """test_x_failure: test x exceptions"""
        with self.assertRaises(TypeError): Rectangle(1, 2, 'blue', 4)
        with self.assertRaises(ValueError): Rectangle(1, 2, -3, 4)

    def test_y_failure(self):
        """test_y_failure: test y exceptions"""
        with self.assertRaises(TypeError): Rectangle(9, 8, 7, {})
        with self.assertRaises(ValueError): Rectangle(4, 5, 6, -7)

class TestRectangleMethods(unittest.TestCase):
    """TestRectangleMethods: Test methods in the Rectangle class"""

    def test_area(self):
        """test_area: test the area method"""
        r1 = Rectangle (2, 2)
        self.assertAlmostEqual(r1.area(), 4)

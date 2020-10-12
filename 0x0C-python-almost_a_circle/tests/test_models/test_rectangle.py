#!/usr/bin/python3
"""rectangle_test.py: unit test for module/rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangleCreation(unittest.TestCase):
    """TestRectangleCreation: Test the creation of the Rectangle class"""

    def test_id(self):
        """test_id: method for testing Rectangle class id assignment"""
        id1 = Rectangle(1, 1)
        self.assertAlmostEqual(id1.id, 4)
        id2 = Rectangle(2, 2)
        self.assertAlmostEqual(id2.id, 5)
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
        with self.assertRaises(TypeError):
            Rectangle("boi", 3)
        with self.assertRaises(ValueError):
            Rectangle(-5, 2)

    def test_height_failure(self):
        """test_height_failure: test height exceptions"""
        with self.assertRaises(TypeError):
            Rectangle(2, [])
        with self.assertRaises(ValueError):
            Rectangle(4, -5)

    def test_x_failure(self):
        """test_x_failure: test x exceptions"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 'blue', 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)

    def test_y_failure(self):
        """test_y_failure: test y exceptions"""
        with self.assertRaises(TypeError):
            Rectangle(9, 8, 7, {})
        with self.assertRaises(ValueError):
            Rectangle(4, 5, 6, -7)


class TestRectangleMethods(unittest.TestCase):
    """TestRectangleMethods: Test methods in the Rectangle class"""

    def test_area(self):
        """test_area: test the area method"""
        r1 = Rectangle(2, 2)
        self.assertAlmostEqual(r1.area(), 4)

    def test_display1(self):
        """test_display1: test the display method"""
        import sys
        from io import StringIO

        recdis = Rectangle(2, 2)
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            recdis.display()
            output = out.getvalue().strip()
            self.assertEqual(output, "##\n##")
        finally:
            sys.stdout = saved_stdout

    def test_display2(self):
        """test_display2: test the display method with x and y"""
        import sys
        from io import StringIO

        recdis = Rectangle(2, 2, 2, 2)
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            recdis.display()
            output = out.getvalue().strip()
            self.assertEqual(output, "##\n  ##")
        finally:
            sys.stdout = saved_stdout

    def test___str__(self):
        """test___str__: tests the __str__ method"""
        recstr = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(recstr), "[Rectangle] (12) 2/1 - 4/6")

    def test_update1(self):
        """test_update1: tests the update method"""
        recup = Rectangle(10, 10, 10, 10)
        recup.update(89, 2, 3, 4, 5)
        self.assertEqual(str(recup), "[Rectangle] (89) 4/5 - 2/3")

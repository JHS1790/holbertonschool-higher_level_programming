#!/usr/bin/python3
"""base_test.py: unit test for module/base.py"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


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

    def test_python2json(self):
        """test_python2json: test the to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            json_dictionary,
            json.JSONEncoder().encode([dictionary])
            )

    def test_json2python(self):
        """test_json2python: test the from_json_string method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

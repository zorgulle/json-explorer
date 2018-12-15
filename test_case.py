import pytest
import unittest
from main import construct

class TestParsingAndDictConstruction(unittest.TestCase):
    def test_simple_dict(self):
        simple_dict = {"name": "Boris"}

        node = construct(simple_dict)
        self.assertDictEqual(node.get_dict(), simple_dict)

    def test_mutiple_type_same_level(self):
        simple_dict = {
            "name": "Boris",
            "nickname": "hardbass"
        }

        node = construct(simple_dict)
        self.assertDictEqual(node.get_dict(), simple_dict)

    def test_dict_with_list_int_value(self):
        simple_dict = {
            "toto": [1, 2, 3]
        }
        node = construct(simple_dict)
        self.assertDictEqual(node.get_dict(), simple_dict)

    def test_dict_with_subdict(self):
        simple_dict = {
            "level1": {
                "level2": "You Win"
            }
        }
        node = construct(simple_dict)
        self.assertListEqual(node.get_value("level2"), ["You Win"])


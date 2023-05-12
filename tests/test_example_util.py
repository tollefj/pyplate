import unittest

from src.utils.example_util import greet


class TestExampleUtil(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("User"), "Hello, User!")
        self.assertNotEqual(greet("Alice"), "Hello, Bob!")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
import unittest
from unittest.mock import patch
import io
import sys

"""Import the parts of the code we want to test"""
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    """Initialize the console for each test"""
    def setUp(self):
        self.console = HBNBCommand()

    """Clean up after each test"""
    def tearDown(self):
        self.console = None

    def test_create_with_valid_syntax(self):
        """Mock user input for testing "create" command"""
        with patch('builtins.input',
                   side_effect=["create State name=\"Carlifornia\"", "EOF"]):
            output = io.StringIO()
            sys.stdout = output
            self.console.cmdloop()
            sys.stdout = sys.__stdout__

        output_str = output.getvalue()
        self.assertIn("New object", output_str)
        self.assertIn("Carlifornia", output_str)

    def test_create_with_invalid_syntax(self):
        """Mock user input for testing invalid "create" command"""
        with patch('builtins.input',
                   side_effect=["create State invalid_syntax", "EOF"]):
            output = io.StringIO()
            sys.stdout = output
            self.console.cmdloop()
            sys.stdout = sys.__stdout__

        output_str = output.getvalue()
        self.assertIn("** attribute name missing **", output_str)


if __name__ == '__main__':
    unittest.main()

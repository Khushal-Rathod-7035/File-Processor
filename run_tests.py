"""
Script to run pytest for testing the application.

This script executes the pytest framework, running
tests located in the 'tests' directory when executed.
"""
import unittest
from tests.test_file_processor import TestFileProcessor

if __name__ == "__main__":
    unittest.main()

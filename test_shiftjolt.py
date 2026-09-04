# test_shiftjolt.py
"""
Tests for ShiftJolt module.
"""

import unittest
from shiftjolt import ShiftJolt

class TestShiftJolt(unittest.TestCase):
    """Test cases for ShiftJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShiftJolt()
        self.assertIsInstance(instance, ShiftJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShiftJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# fp
Turn off PC!
import unittest
from project import tick

class TestMinutes(unittest.TestCase):
    def test_min(self):
        self.assertAlmostEqual(tick(30), 30)
        self.assertAlmostEqual(tick(60), 60)
        self.assertAlmostEqual(tick(120), 120)
        self.assertAlmostEqual(tick(0), 0)
    def test_value(self):
        self.assertRaises(ValueError, tick, -2)

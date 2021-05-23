import unittest
import pytest
import leap
import coverage


class TestCase(unittest.TestCase):
    #pass cases
    def test_pass_1(self):
        self.assertEqual(leap.leap_year(2012), 1)
    def test_pass_2(self):
        self.assertEqual(leap.leap_year(2008), 1)
    def test_pass_3(self):
        self.assertEqual(leap.leap_year(400), 1)
        
    #fail cases
    def test_fail_1(self):
        self.assertEqual(leap.leap_year(1999), 1)
    def test_fail_2(self):
        self.assertEqual(leap.leap_year(2016), 0)
    def test_fail_3(self):
        self.assertEqual(leap.leap_year(401), 1)


if __name__ == '__main__':
    unittest.main()
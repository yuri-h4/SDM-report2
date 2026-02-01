#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))


        def test_valid_min_min(self) :
                self.assertEqual(1, calc(1,1))
        
        def test_valid_min_max(self) :
                self.assertEqual(999, calc(1,999))

        def test_valid_max_min(self) :
                self.assertEqual(999, calc(999,1))

        def test_valid_max_max(self) :
                self.assertEqual(998001, calc(999,999))

        def test_invalid_A_zero(self) :
                self.assertEqual(-1, calc(0,500))
        
        def test_invalid_B_zero(self) :
                self.assertEqual(-1, calc(500,0))

        def test_invalid_A_high(self) :
                self.assertEqual(-1, calc(1000,500))
        
        def test_invalid_B_high(self) :
                self.assertEqual(-1, calc(500,1000))

        def test_invalid_string_A(self) :
                self.assertEqual(-1, calc('abc',500))

        def test_invalid_string_B(self) :
                self.assertEqual(-1, calc(500,'abc'))

        def test_invalid_float_A(self) :
                self.assertEqual(-1, calc(5.5,500))

        def test_invalid_float_B(self) :
                self.assertEqual(-1, calc(500,5.5))

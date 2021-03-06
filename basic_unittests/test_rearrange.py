#!/usr/bin/env python3

from rearrangeNames import rearrange

import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase1="Kristina, Sinkovskaya"
        expected1="Sinkovskaya Kristina"
        self.assertEqual(rearrange(testcase1), expected1)
        self.assertNotEqual(rearrange(testcase1), testcase1)
        testcase2="John, Wick"
        expected2="Wick John"
        self.assertEqual(rearrange(testcase2),expected2)
        self.assertNotEqual(rearrange(testcase2), testcase2)
    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange(testcase), expected)
        self.assertNotEqual(rearrange(testcase), "Ivanka Trump")
    def test_double_name(self):
        testcase="Novakova, Marie M."
        expected="Marie M. Novakova"
        self.assertEqual(rearrange(testcase), expected)
        self.assertNotEqual(rearrange(testcase), testcase)
    def test_one_name(self):
        testcase="Voldemort"
        expected="Voldemort"
        self.assertEqual(rearrange(testcase), expected)
        self.assertNotEqual(rearrange(testcase), sorted(testcase))    
unittest.main()


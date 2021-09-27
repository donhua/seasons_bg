#!/usr/bin/env python3.9
import unittest
from Game import Game

class TestSum(unittest.TestCase):

    def test_list(self):
        result = 1
        etalon = 1
        self.assertEqual(result, etalon)

if __name__ == "__main__":
    unitest.main()

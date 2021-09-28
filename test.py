#!/usr/bin/env python3.9
import unittest
from Game import Game

class TestSum(unittest.TestCase):

    def test_list(self):
        result = Game.j()
        etalon = "int"
        self.assertEqual(type(result), etalon)

if __name__ == "__main__":
    unitest.main()

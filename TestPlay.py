#!/usr/bin/python

import unittest
import CardTypes as ct

class TestPlay(unittest.TestCase):
    def setUp(self):
        self.hand = list()
        self.discard = list()
        self.deck = list()
        self.bench = list()

    def test_EmptyHand(self):
        pass

if __name__ == '__main__':
    unittest.main()


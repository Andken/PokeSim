#!/usr/bin/python

import DeckOperations as do
import BlastoiseFirstTurn as bft
import unittest
from copy import deepcopy
import itertools

class TestCardTypes(unittest.TestCase):
    def setUp(self):
        self.hand = list()
        self.discard = list()
        self.deck = list()
        self.bench = list()

    def test_EmptyHand(self):
        pass

if __name__ == '__main__':
    unittest.main()


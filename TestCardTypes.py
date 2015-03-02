#!/usr/bin/python

import unittest
import CardTypes as ct

class TestCardTypes(unittest.TestCase):
    def setUp(self):
        self.hand = list()
        self.discard = list()
        self.deck = list()
        self.bench = list()

    def test_EmptyHand(self):
        pass

    def test_SingleCard(self):
        card = ct.Card()
        self.assertEqual(card.canPlay(self.hand, self.discard, self.deck, self.bench), False)

if __name__ == '__main__':
    unittest.main()


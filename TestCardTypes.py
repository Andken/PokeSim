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

    def test_AnonymousCard(self):
        card = ct.Card()
        self.assertEqual(card.canPlay(self.hand, self.discard, self.deck, self.bench), False)
        results = card.play(self.hand, self.discard, self.deck, self.bench)
        self.assertEqual(results, [(self.hand, self.discard, self.deck, self.bench)])

    def test_CanPlayVSSeeker(self):
        vss = ct.VSSeeker()
        self.assertEqual(vss.canPlay(self.hand, self.discard, self.deck, self.bench), False)

        self.discard.append(ct.Skyla())

        vss = ct.VSSeeker()
        self.assertEqual(vss.canPlay(self.hand, self.discard, self.deck, self.bench), True)

if __name__ == '__main__':
    unittest.main()


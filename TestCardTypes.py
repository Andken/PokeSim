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
        self.assertEqual(card.canPlay(self.hand, self.discard, self.bench, self.deck), False)
        results = card.play(self.hand, self.discard, self.bench, self.deck)
        self.assertEqual(results, [(self.hand, self.discard, self.bench, self.deck)])

    def test_CanPlayArchie(self):
        self.hand.append(ct.ArchiesAceintheHole())
        self.assertEqual(self.hand[0].canPlay(self.hand, self.discard, self.bench, self.deck), False)

        self.discard.append(ct.Blastoise())

        self.discard = list()

        self.discard.append(ct.Skyla())
        self.discard.append(ct.Skyla())
        self.discard.append(ct.Skyla())
        self.discard.append(ct.Blastoise())
        self.discard.append(ct.Skyla())
        self.discard.append(ct.Skyla())

        self.assertEqual(self.hand[0].canPlay(self.hand, self.discard, self.bench, self.deck), True)

        self.hand.append(ct.ArchiesAceintheHole())

        self.assertEqual(self.hand[0].canPlay(self.hand, self.discard, self.bench, self.deck), False)        

    def test_CanPlayBasic(self):
        keldeo_ex = ct.KeldeoEX()
        self.assertEqual(keldeo_ex.canPlay(self.hand, self.discard, self.bench, self.deck), True)

        self.bench.append(ct.Exeggcute())
        self.bench.append(ct.Exeggcute())
        self.bench.append(ct.Exeggcute())
        self.bench.append(ct.Exeggcute())
        self.bench.append(ct.Exeggcute())

        self.assertEqual(keldeo_ex.canPlay(self.hand, self.discard, self.bench, self.deck), False)

    def test_CanPlayVSSeeker(self):
        vss = ct.VSSeeker()
        self.assertEqual(vss.canPlay(self.hand, self.discard, self.bench, self.deck), False)

        self.discard.append(ct.Skyla())

        vss = ct.VSSeeker()
        self.assertEqual(vss.canPlay(self.hand, self.discard, self.bench, self.deck), True)

if __name__ == '__main__':
    unittest.main()


#!/usr/bin/python

import DeckOperations as do
import unittest

import unittest

class TestDeckOperations(unittest.TestCase):
    def setUp(self):
        self.discard = list()
        self.hand = list()
        self.deck = list()

    def test_SimpleBlastioseFirstTurn1(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(do.BlastioseFirstTurn(self.hand, self.discard, self.deck), True)

    def test_SimpleBlastioseFirstTurn2(self):
        self.hand.append(["VS Seeker","0","Item"])
        self.discard.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(do.BlastioseFirstTurn(self.hand, self.discard, self.deck), True)

    def test_SimpleNoBlastioseFirstTurn(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.assertEqual(do.BlastioseFirstTurn(self.hand, self.discard, self.deck), False)

    def test_BlastioseFirstTurnWithExtraSupporter(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(do.BlastioseFirstTurn(self.hand, self.discard, self.deck), False)

    def test_BlastioseFirstTurnWithExtraItem(self):
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(do.BlastioseFirstTurn(self.hand, self.discard, self.deck), True)

    

if __name__ == '__main__':
    unittest.main()


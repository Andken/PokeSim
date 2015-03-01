#!/usr/bin/python

import DeckOperations as do
import BlastoiseFirstTurn as bft
import unittest
import copy
import itertools

class TestDeckOperations(unittest.TestCase):
    def setUp(self):
        self.discard = list()
        self.hand = list()
        self.deck = list()

    def test_SimpleBlastoiseFirstTurn1(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(bft.BlastoiseFirstTurn(self.hand, self.discard, self.deck), True)

    def test_SimpleBlastoiseFirstTurn2(self):
        self.hand.append(["VS Seeker","0","Item"])
        self.discard.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(bft.BlastoiseFirstTurn(self.hand, self.discard, self.deck), True)

    def test_SimpleNoBlastoiseFirstTurn(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.assertEqual(bft.BlastoiseFirstTurn(self.hand, self.discard, self.deck), False)

    def test_BlastoiseFirstTurnWithExtraSupporter(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        self.assertEqual(bft.BlastoiseFirstTurn(self.hand, self.discard, self.deck), False)

    def test_BlastoiseFirstTurnWithExtraItem(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.discard.append(["Blastoise","2","Evolve"])
        for p in itertools.permutations(self.hand):
            self.assertEqual(bft.BlastoiseFirstTurn(copy.deepcopy(list(p)), self.discard, self.deck), True)    

    def test_BlastoiseFirstTurnWithDiscard(self):
        self.hand.append(["Blastoise","2","Evolve"])
        self.hand.append(["Blastoise","2","Evolve"])
        self.hand.append(["Ultra Ball","0","Item-UnrestrictedDiscard"])
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])

if __name__ == '__main__':
    unittest.main()


#!/usr/bin/python

import DeckOperations as do
import BlastoiseFirstTurn as bft
import unittest
import copy
import itertools

def checkHand(test, expr):
    for p in itertools.permutations(test.hand):
        test.assertEqual(bft.BlastoiseFirstTurn(copy.deepcopy(list(p)), 
                                                copy.deepcopy(test.discard), 
                                                copy.deepcopy(test.deck)), expr)
        

class TestDeckOperations(unittest.TestCase):
    def setUp(self):
        self.hand = list()
        self.discard = list()
        self.deck = list()

    def test_EmptyHand(self):
        checkHand(self, False)

    def test_SimpleSingleVSSeeker(self):
        self.hand.append(["VS Seeker","0","Item"]) 
        checkHand(self, False)

    def test_SimpleSingleVSSeekerAndBlastoise(self):
        self.hand.append(["VS Seeker","0","Item"]) 
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, False)

    def test_SimpleSingleVSSeekerArchieAndBlastoise(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["VS Seeker","0","Item"]) 
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, False)

    def test_SimpleBlastoiseFirstTurn(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, True)

    def test_SimpleBlastoiseFirstTurnVsSeeker(self):
        self.hand.append(["VS Seeker","0","Item"])
        self.discard.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, True)

    def test_SimpleEmptyDiscard(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        checkHand(self, False)

    def test_SimpleNotEnoughCards(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Ultra Ball","0","Item-UnrestrictedDiscard"])
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, False)

    def test_BlastoiseFirstTurnWithExtraSupporter(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, False)

    def test_BlastoiseFirstTurnWithExtraItem(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, True)

    def test_BlastoiseFirstTurnWithExtraItemAndExtraSupporter(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.hand.append(["Battle Compressor","0","Item-Anytime"])
        self.discard.append(["Blastoise","2","Evolve"])
        checkHand(self, False)

    def test_BlastoiseFirstTurnWithDiscard(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Blastoise","2","Evolve"])
        self.hand.append(["Blastoise","2","Evolve"])
        self.hand.append(["Ultra Ball","0","Item-UnrestrictedDiscard"])
        checkHand(self, True)

    def test_BlastoiseFirstTurnWithDiscardAndVSSeeker(self):
        self.hand.append(["Archie's Ace in the Hole","1","Supporter"])
        self.hand.append(["Blastoise","2","Evolve"])
        self.hand.append(["VS Seeker","0","Item"])
        self.hand.append(["Ultra Ball","0","Item-UnrestrictedDiscard"])
        checkHand(self, True)

if __name__ == '__main__':
    unittest.main()


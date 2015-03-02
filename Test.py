#!/usr/bin/python

import DeckOperations as do
import BlastoiseFirstTurn as bft
import unittest
from copy import deepcopy
import itertools

def checkHand(test, expr):
    memoization = dict()
    test.assertEqual(bft.BlastoiseFirstTurn(deepcopy(test.hand), 
                                            deepcopy(test.discard), 
                                            deepcopy(test.deck),
                                            deepcopy(test.bench),
                                            memoization), expr)

class TestDeckOperations(unittest.TestCase):
    def setUp(self):
        self.hand = list()
        self.discard = list()
        self.deck = list()
        self.bench = list()

    def test_EmptyHand(self):
        checkHand(self, False)

    def test_SimpleSingleVSSeeker(self):
        self.hand.append(("VS Seeker","0","Item")) 
        checkHand(self, False)

    def test_SimpleSingleVSSeekerAndBlastoise(self):
        self.hand.append(("VS Seeker","0","Item")) 
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_SimpleSingleVSSeekerArchieAndBlastoise(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("VS Seeker","0","Item")) 
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_SimpleBlastoiseFirstTurn(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_SimpleBlastoiseFirstTurnVsSeeker(self):
        self.hand.append(("VS Seeker","0","Item"))
        self.discard.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_EmptyDiscard(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        checkHand(self, False)

    def test_NotEnoughCards(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_ExtraSupporter(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_BlastoiseFirstTurnWithExtraItem(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ExtraItemAndExtraSupporter(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_Discard(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        checkHand(self, True)

    def test_DiscardAndVSSeeker(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("VS Seeker","0","Item"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        checkHand(self, True)

    def test_MultiDiscard(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        checkHand(self, True)

    def test_MultiDiscardExtraItem(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        checkHand(self, True)

    def test_MultiDiscardManySupporters(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        checkHand(self, False)

    def test_Energy(self):
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_TooMuchEnergy(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_DiscardEnergy(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_DiscardEnergyAndBlastoise(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_Basic(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_MultipleBasics(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_FullBench(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_TooManyBasics(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.hand.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_Exeggcute(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Blastoise","2","Evolve"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.discard.append(("Exeggcute","0","Basic"))
        checkHand(self, True)

    def test_BlastoiseBattleCompressor(self):
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.deck.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ArchieVSSeekerBattleCompressor(self):
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("VS Seeker","0","Item"))
        self.deck.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ArchieAndBlastoiseVSSeekerBattleCompressor(self):
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.hand.append(("VS Seeker","0","Item"))
        self.deck.append(("Archie's Ace in the Hole","1","Supporter"))
        self.deck.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ArchieAndBlastoiseNoVSSeekerBattleCompressor(self):
        self.hand.append(("Battle Compressor","0","Item-Anytime"))
        self.deck.append(("Archie's Ace in the Hole","1","Supporter"))
        self.deck.append(("Blastoise","2","Evolve"))
        checkHand(self, False)

    def test_UltraBallToGetBlastoise(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.deck.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_UltraBallToGetKeldeoEX_1(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.deck.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_UltraBallToGetKeldeoEX_2(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.deck.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_UltraBallToGetKeldeoEX_3(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.deck.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.bench.append(("Keldeo EX","3","Basic"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_UltraBallToGetNothing(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_UltraBallToGetExeggcute(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.discard.append(("Blastoise","2","Evolve"))
        self.deck.append(("Exeggcute","0","Basic"))
        checkHand(self, True)

    def test_ComputerTrainerToGetArchie(self):
        self.hand.append(("Computer Trainer","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.deck.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ComputerTrainerToGetVSSeeker(self):
        self.hand.append(("Computer Trainer","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.deck.append(("VS Seeker","0","Item"))
        self.discard.append(("Archie's Ace in the Hole","1","Supporter"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ComputerTrainerToGetBattleCompressor(self):
        self.hand.append(("Computer Trainer","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("VS Seeker","0","Item"))
        self.deck.append(("Archie's Ace in the Hole","1","Supporter"))
        self.deck.append(("Battle Compressor","0","Item-Anytime"))
        self.deck.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ComputerTrainerToGetWaterEnergy(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Computer Trainer","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Water Energy","0","Energy"))
        self.hand.append(("Water Energy","0","Energy"))
        self.deck.append(("Water Energy","0","Energy"))
        self.discard.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

    def test_ComputerTrainerToGetBlastoise(self):
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Archie's Ace in the Hole","1","Supporter"))
        self.hand.append(("Computer Trainer","0","Item-UnrestrictedDiscard"))
        self.hand.append(("Ultra Ball","0","Item-UnrestrictedDiscard"))
        self.deck.append(("Blastoise","2","Evolve"))
        checkHand(self, True)

if __name__ == '__main__':
    unittest.main()


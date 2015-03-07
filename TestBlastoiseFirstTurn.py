#!/usr/bin/python

import BlastoiseFirstTurn as bft
import unittest
from copy import deepcopy
from PlayerState import PlayerState
import CardTypes as c
import CardFactory as cf

def checkHand(test, p, expr):
    memoization = dict()
    test.assertEqual(bft.BlastoiseFirstTurn(deepcopy(p), 
                                            memoization), expr)

class TestBlastoiseFirstTurn(unittest.TestCase):
    def test_EmptyHand(self):
        checkHand(self, PlayerState(), False)

    def test_SimpleSingleVSSeeker(self):
        checkHand(self, PlayerState(hand=[c.VSSeeker()]), False)

    def test_SimpleSingleVSSeekerAndBlastoise(self):
        p = PlayerState(hand=[c.VSSeeker()],
                        discard=[c.Blastoise()])
        checkHand(self, p, False)

    def test_SimpleSingleVSSeekerArchieAndBlastoise(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("VS Seeker"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_SimpleBlastoiseFirstTurn(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_SimpleBlastoiseFirstTurnVsSeeker(self):
        p = PlayerState()
        p.hand.append(cf.create("VS Seeker"))
        p.discard.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_EmptyDiscard(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        checkHand(self, p, False)

    def test_NotEnoughCards(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_ExtraSupporter(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_BlastoiseFirstTurnWithExtraItem(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ExtraItemAndExtraSupporter(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_Discard(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Ultra Ball"))
        checkHand(self, p, True)

    def test_DiscardAndVSSeeker(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("VS Seeker"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Ultra Ball"))
        checkHand(self, p, True)

    def test_MultiDiscard(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Ultra Ball"))
        checkHand(self, p, True)

    def test_MultiDiscardExtraItem(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Ultra Ball"))
        checkHand(self, p, True)

    def test_MultiDiscardManySupporters(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Ultra Ball"))
        checkHand(self, p, False)

    def test_Energy(self):
        p = PlayerState()
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_TooMuchEnergy(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_DiscardEnergy(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("N"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_DiscardEnergyAndBlastoise(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Blastoise"))
        p.deck.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_Basic(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_MultipleBasics(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_FullBench(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_TooManyBasics(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.hand.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_Exeggcute(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Blastoise"))
        p.hand.append(cf.create("Ultra Ball"))
        p.discard.append(cf.create("Exeggcute"))
        p.deck.append(cf.create("Exeggcute"))
        checkHand(self, p, True)

    def test_BlastoiseBattleCompressor(self):
        p = PlayerState()
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.deck.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ArchieVSSeekerBattleCompressor(self):
        p = PlayerState()
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("VS Seeker"))
        p.deck.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ArchieAndBlastoiseVSSeekerBattleCompressor(self):
        p = PlayerState()
        p.hand.append(cf.create("Battle Compressor"))
        p.hand.append(cf.create("VS Seeker"))
        p.deck.append(cf.create("Archie's Ace in the Hole"))
        p.deck.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ArchieAndBlastoiseNoVSSeekerBattleCompressor(self):
        p = PlayerState()
        p.hand.append(cf.create("Battle Compressor"))
        p.deck.append(cf.create("Archie's Ace in the Hole"))
        p.deck.append(cf.create("Blastoise"))
        checkHand(self, p, False)

    def test_UltraBallToGetBlastoise(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Blastoise"))
        p.deck.append(cf.create("VS Seeker"))
        checkHand(self, p, True)

    def test_UltraBallToGetKeldeoEX_1(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_UltraBallToGetKeldeoEX_2(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_UltraBallToGetKeldeoEX_3(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.bench.append(cf.create("Keldeo EX"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_UltraBallToGetNothing(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.discard.append(cf.create("Blastoise"))
        p.deck.append(cf.create("VS Seeker"))
        checkHand(self, p, True)

    def test_UltraBallToGetExeggcute(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Ultra Ball"))
        p.hand.append(cf.create("Ultra Ball"))
        p.discard.append(cf.create("Blastoise"))
        p.deck.append(cf.create("Exeggcute"))
        p.deck.append(cf.create("Ultra Ball"))
        checkHand(self, p, True)

    def test_ComputerTrainerToGetArchie(self):
        p = PlayerState()
        p.hand.append(cf.create("Computer Trainer"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.deck.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ComputerTrainerToGetVSSeeker(self):
        p = PlayerState()
        p.hand.append(cf.create("Computer Trainer"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.deck.append(cf.create("VS Seeker"))
        p.discard.append(cf.create("Archie's Ace in the Hole"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ComputerTrainerToGetBattleCompressor(self):
        p = PlayerState()
        p.hand.append(cf.create("Computer Trainer"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("VS Seeker"))
        p.deck.append(cf.create("Archie's Ace in the Hole"))
        p.deck.append(cf.create("Battle Compressor"))
        p.deck.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ComputerTrainerToGetWaterEnergy(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Computer Trainer"))
        p.hand.append(cf.create("Water Energy"))
        p.hand.append(cf.create("Water Energy"))
        p.deck.append(cf.create("Water Energy"))
        p.discard.append(cf.create("Blastoise"))
        checkHand(self, p, True)

    def test_ComputerTrainerToGetBlastoise(self):
        p = PlayerState()
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Archie's Ace in the Hole"))
        p.hand.append(cf.create("Computer Trainer"))
        p.hand.append(cf.create("Ultra Ball"))
        p.deck.append(cf.create("Blastoise"))
        checkHand(self, p, True)

if __name__ == '__main__':
    unittest.main(verbosity=2)


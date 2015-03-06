#!/usr/bin/python

import unittest
import CardTypes as ct
from PlayerState import PlayerState

class TestCanPlayTypes(unittest.TestCase):
    def test_CanPlayVSSeeker(self):
        p1 = PlayerState()
        self.assertEqual(ct.VSSeeker().canPlay(p1), False)

        p2 = PlayerState(hand=[ct.VSSeeker()], discard=[ct.WaterEnergy()])
        self.assertEqual(ct.VSSeeker().canPlay(p2), False)

        p3 = PlayerState(hand=[ct.VSSeeker()], discard=[ct.N()])
        self.assertEqual(ct.VSSeeker().canPlay(p3), True)

        p4 = PlayerState(hand=[ct.VSSeeker()])
        self.assertEqual(ct.VSSeeker().canPlay(p4), False)

        p5 = PlayerState(hand=[ct.VSSeeker(), ct.KeldeoEX()],
                         discard=[ct.N(), ct.KeldeoEX()])
        self.assertEqual(ct.VSSeeker().canPlay(p5), True)

        p6 = PlayerState(hand=[ct.VSSeeker(), ct.KeldeoEX()],
                         discard=[ct.KeldeoEX(), ct.N()])
        self.assertEqual(ct.VSSeeker().canPlay(p6), True)

    def test_CanPlayUltraBall(self):
        p1 = PlayerState()
        self.assertEqual(ct.UltraBall().canPlay(p1), False)

        p2 = PlayerState(hand=[ct.UltraBall()], deck=[ct.WaterEnergy()])
        self.assertEqual(ct.UltraBall().canPlay(p2), False)

        p3 = PlayerState(hand=[ct.UltraBall(),
                               ct.KeldeoEX(),
                               ct.KeldeoEX()],
                         deck=[ct.WaterEnergy()])
        self.assertEqual(ct.UltraBall().canPlay(p3), True)

        p4 = PlayerState(hand=[ct.UltraBall(),
                               ct.KeldeoEX(),
                               ct.KeldeoEX()])
        self.assertEqual(ct.UltraBall().canPlay(p4), False)

        p5 = PlayerState(hand=[ct.UltraBall(), ct.KeldeoEX()])
        self.assertEqual(ct.UltraBall().canPlay(p5), False)

    def test_CanPlayComputerTrainer(self):
        p1 = PlayerState()
        self.assertEqual(ct.ComputerTrainer().canPlay(p1), False)

        p2 = PlayerState(hand=[ct.ComputerTrainer()], deck=[ct.WaterEnergy()])
        self.assertEqual(ct.ComputerTrainer().canPlay(p2), False)

        p3 = PlayerState(hand=[ct.ComputerTrainer(),
                               ct.KeldeoEX(),
                               ct.KeldeoEX()],
                         deck=[ct.WaterEnergy()])
        self.assertEqual(ct.ComputerTrainer().canPlay(p3), True)

        p4 = PlayerState(hand=[ct.ComputerTrainer(),
                               ct.KeldeoEX(),
                               ct.KeldeoEX()])
        self.assertEqual(ct.ComputerTrainer().canPlay(p4), False)

        p5 = PlayerState(hand=[ct.ComputerTrainer(), ct.KeldeoEX()])
        self.assertEqual(ct.ComputerTrainer().canPlay(p5), False)

    def test_CanPlayBattleCompressor(self):
        p1 = PlayerState()
        self.assertEqual(ct.BattleCompressor().canPlay(p1), False)

        p2 = PlayerState(hand=[ct.KeldeoEX()], deck=[ct.WaterEnergy()])
        self.assertEqual(ct.BattleCompressor().canPlay(p2), False)

        p3 = PlayerState(hand=[ct.BattleCompressor()], deck=[ct.WaterEnergy()])
        self.assertEqual(ct.BattleCompressor().canPlay(p3), True)

        p4 = PlayerState(hand=[ct.BattleCompressor()])
        self.assertEqual(ct.BattleCompressor().canPlay(p4), False)

    def test_CanPlayBasic(self):
        p = PlayerState(hand=[ct.KeldeoEX()])
        self.assertEqual(ct.KeldeoEX().canPlay(p), True)

        p.bench.append(ct.KeldeoEX())
        p.bench.append(ct.KeldeoEX())
        p.bench.append(ct.KeldeoEX())
        p.bench.append(ct.KeldeoEX())
        self.assertEqual(ct.KeldeoEX().canPlay(p), True)

        p.bench.append(ct.KeldeoEX())
        self.assertEqual(ct.KeldeoEX().canPlay(p), False)

        p.bench.append(ct.KeldeoEX())
        self.assertEqual(ct.KeldeoEX().canPlay(p), False)

    def test_CanPlayArchiesAceintheHole(self):
        p1 = PlayerState()
        self.assertEqual(ct.ArchiesAceintheHole().canPlay(p1), False)

        p2 = PlayerState(hand=[ct.ArchiesAceintheHole()])
        self.assertEqual(ct.ArchiesAceintheHole().canPlay(p2), False)

        p3 = PlayerState(hand=[ct.ArchiesAceintheHole()],
                         discard=[ct.KeldeoEX()])
        self.assertEqual(ct.ArchiesAceintheHole().canPlay(p3), True)

        p4 = PlayerState(hand=[ct.ArchiesAceintheHole(), ct.ArchiesAceintheHole()],
                         discard=[ct.KeldeoEX()])
        self.assertEqual(ct.ArchiesAceintheHole().canPlay(p4), False)

        p5 = PlayerState(hand=[],
                         discard=[ct.KeldeoEX()])
        self.assertEqual(ct.ArchiesAceintheHole().canPlay(p5), False)

        p6 = PlayerState(hand=[ct.ArchiesAceintheHole()],
                         discard=[ct.Exeggcute()])
        self.assertEqual(ct.ArchiesAceintheHole().canPlay(p6), False)

    def test_CanPlayWaterEnergy(self):
        p1 = PlayerState(hand=[ct.WaterEnergy()])
        self.assertEqual(ct.WaterEnergy().canPlay(p1), True)

        p2 = PlayerState(hand=[ct.WaterEnergy()], attached_energy = True)
        self.assertEqual(ct.WaterEnergy().canPlay(p2), False)

#    def test_AnonymousCard(self):
#        card = ct.Card()
#        self.assertEqual(card.canPlay(self.hand, self.discard, self.bench, self.deck), False)
#        results = card.play(self.hand, self.discard, self.bench, self.deck)
#        self.assertEqual(results, [(self.hand, self.discard, self.bench, self.deck)])
#
#    def test_CanPlayArchie(self):
#        self.hand.append(ct.ArchiesAceintheHole())
#        self.assertEqual(self.hand[0].canPlay(self.hand, self.discard, self.bench, self.deck), False)
#
#        self.discard.append(ct.Blastoise())
#
#        self.discard = list()
#
#        self.discard.append(ct.Skyla())
#        self.discard.append(ct.Skyla())
#        self.discard.append(ct.Skyla())
#        self.discard.append(ct.Blastoise())
#        self.discard.append(ct.Skyla())
#        self.discard.append(ct.Skyla())
#
#        self.assertEqual(self.hand[0].canPlay(self.hand, self.discard, self.bench, self.deck), True)
#
#        self.hand.append(ct.ArchiesAceintheHole())
#
#        self.assertEqual(self.hand[0].canPlay(self.hand, self.discard, self.bench, self.deck), False)
#
#    def test_CanPlayBasic(self):
#        self.assertEqual(ct.KeldeoEX().canPlay(self.hand, self.discard, self.bench, self.deck), True)
#        self.assertEqual(ct.Exeggcute().canPlay(self.hand, self.discard, self.bench, self.deck), True)
#        self.assertEqual(ct.Suicune().canPlay(self.hand, self.discard, self.bench, self.deck), True)
#
#        self.bench.append(ct.Exeggcute())
#        self.bench.append(ct.Exeggcute())
#        self.bench.append(ct.Exeggcute())
#        self.bench.append(ct.Exeggcute())
#
#        self.assertEqual(ct.KeldeoEX().canPlay(self.hand, self.discard, self.bench, self.deck), True)
#        self.assertEqual(ct.Exeggcute().canPlay(self.hand, self.discard, self.bench, self.deck), True)
#        self.assertEqual(ct.Suicune().canPlay(self.hand, self.discard, self.bench, self.deck), True)
#
#        self.bench.append(ct.Exeggcute())
#
#        self.assertEqual(ct.KeldeoEX().canPlay(self.hand, self.discard, self.bench, self.deck), False)
#        self.assertEqual(ct.Exeggcute().canPlay(self.hand, self.discard, self.bench, self.deck), False)
#        self.assertEqual(ct.Suicune().canPlay(self.hand, self.discard, self.bench, self.deck), False)
#
#    def test_CanPlayVSSeeker(self):
#        vss = ct.VSSeeker()
#        self.assertEqual(vss.canPlay(self.hand, self.discard, self.bench, self.deck), False)
#
#        self.discard.append(ct.ProfessorJuniper())
#
#        vss = ct.VSSeeker()
#        self.assertEqual(vss.canPlay(self.hand, self.discard, self.bench, self.deck), True)
#
#        self.discard = list()
#        self.bench.append(ct.Exeggcute())
#        self.bench.append(ct.Exeggcute())
#        self.bench.append(ct.Exeggcute())
#
#        vss = ct.VSSeeker()
#        self.assertEqual(vss.canPlay(self.hand, self.discard, self.bench, self.deck), False)
#
#        self.discard.append(ct.Skyla())
#        self.bench.append(ct.Exeggcute())
#        self.bench.append(ct.Exeggcute())
#
#        vss = ct.VSSeeker()
#        self.assertEqual(vss.canPlay(self.hand, self.discard, self.bench, self.deck), True)
#
if __name__ == '__main__':
    unittest.main()


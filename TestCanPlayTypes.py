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

if __name__ == '__main__':
    unittest.main(verbosity=2)


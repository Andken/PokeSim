#!/usr/bin/python

import unittest
import CardTypes as c
from PlayerState import PlayerState

class TestCanPlayTypes(unittest.TestCase):
    def test_CanPlayBicycle(self):
        p1 = PlayerState(nondeterministic = True)
        self.assertEqual(c.Bicycle().canPlay(p1), False)

        p2 = PlayerState(hand=[c.Bicycle()],
                         deck=[c.N(), c.N(), c.N(), c.N()],
                         nondeterministic = True)
        self.assertEqual(c.Bicycle().canPlay(p2), True)

        p2 = PlayerState(hand=[c.Bicycle(), c.N(), c.N()],
                         deck=[c.N(), c.N()],
                         nondeterministic = True)
        self.assertEqual(c.Bicycle().canPlay(p2), True)

        p3 = PlayerState(hand=[c.Bicycle(), c.N(), c.N(), c.N(), c.N()],
                         deck=[c.N(), c.N()],
                         nondeterministic = True)
        self.assertEqual(c.Bicycle().canPlay(p3), False)

        p4 = PlayerState(hand=[c.Bicycle()],
                         deck=[c.N(), c.N()],
                         nondeterministic = True)
        self.assertEqual(c.Bicycle().canPlay(p4), False)

        p5 = PlayerState(hand=[c.Bicycle(), c.N(), c.N()],
                         deck=[c.N(), c.N()])
        self.assertEqual(c.Bicycle().canPlay(p5), False)

    def test_CanPlayMaintenance(self):
        p1 = PlayerState(nondeterministic = True)
        self.assertEqual(c.Maintenance().canPlay(p1), False)

        p2 = PlayerState(hand=[c.Maintenance()],
                         nondeterministic = True)
        self.assertEqual(c.Maintenance().canPlay(p2), False)

        p3 = PlayerState(hand=[c.Maintenance(), c.N(), c.N()],
                         nondeterministic = True)
        self.assertEqual(c.Maintenance().canPlay(p3), True)

        p4 = PlayerState(hand=[c.Maintenance(), c.N(), c.N()])
        self.assertEqual(c.Maintenance().canPlay(p4), False)

    def test_CanPlayVSSeeker(self):
        p1 = PlayerState()
        self.assertEqual(c.VSSeeker().canPlay(p1), False)

        p2 = PlayerState(hand=[c.VSSeeker()], discard=[c.WaterEnergy()])
        self.assertEqual(c.VSSeeker().canPlay(p2), False)

        p3 = PlayerState(hand=[c.VSSeeker()], discard=[c.N()])
        self.assertEqual(c.VSSeeker().canPlay(p3), True)

        p4 = PlayerState(hand=[c.VSSeeker()])
        self.assertEqual(c.VSSeeker().canPlay(p4), False)

        p5 = PlayerState(hand=[c.VSSeeker(), c.KeldeoEX()],
                         discard=[c.N(), c.KeldeoEX()])
        self.assertEqual(c.VSSeeker().canPlay(p5), True)

        p6 = PlayerState(hand=[c.VSSeeker(), c.KeldeoEX()],
                         discard=[c.KeldeoEX(), c.N()])
        self.assertEqual(c.VSSeeker().canPlay(p6), True)

    def test_CanPlayUltraBall(self):
        p1 = PlayerState()
        self.assertEqual(c.UltraBall().canPlay(p1), False)

        p2 = PlayerState(hand=[c.UltraBall()], deck=[c.WaterEnergy()])
        self.assertEqual(c.UltraBall().canPlay(p2), False)

        p3 = PlayerState(hand=[c.UltraBall(),
                               c.KeldeoEX(),
                               c.KeldeoEX()],
                         deck=[c.WaterEnergy()])
        self.assertEqual(c.UltraBall().canPlay(p3), True)

        p4 = PlayerState(hand=[c.UltraBall(),
                               c.KeldeoEX(),
                               c.KeldeoEX()])
        self.assertEqual(c.UltraBall().canPlay(p4), False)

        p5 = PlayerState(hand=[c.UltraBall(), c.KeldeoEX()])
        self.assertEqual(c.UltraBall().canPlay(p5), False)

    def test_CanPlayComputerTrainer(self):
        p1 = PlayerState()
        self.assertEqual(c.ComputerTrainer().canPlay(p1), False)

        p2 = PlayerState(hand=[c.ComputerTrainer()], deck=[c.WaterEnergy()])
        self.assertEqual(c.ComputerTrainer().canPlay(p2), False)

        p3 = PlayerState(hand=[c.ComputerTrainer(),
                               c.KeldeoEX(),
                               c.KeldeoEX()],
                         deck=[c.WaterEnergy()])
        self.assertEqual(c.ComputerTrainer().canPlay(p3), True)

        p4 = PlayerState(hand=[c.ComputerTrainer(),
                               c.KeldeoEX(),
                               c.KeldeoEX()])
        self.assertEqual(c.ComputerTrainer().canPlay(p4), False)

        p5 = PlayerState(hand=[c.ComputerTrainer(), c.KeldeoEX()])
        self.assertEqual(c.ComputerTrainer().canPlay(p5), False)

    def test_CanPlayDowsingMachine(self):
        p1 = PlayerState()
        self.assertEqual(c.DowsingMachine().canPlay(p1), False)

        p2 = PlayerState(hand=[c.DowsingMachine()], discard=[c.WaterEnergy()])
        self.assertEqual(c.DowsingMachine().canPlay(p2), False)

        p3 = PlayerState(hand=[c.DowsingMachine(),
                               c.KeldeoEX(),
                               c.KeldeoEX()],
                         discard=[c.WaterEnergy()])
        self.assertEqual(c.DowsingMachine().canPlay(p3), False)

        p4 = PlayerState(hand=[c.DowsingMachine(),
                               c.KeldeoEX(),
                               c.KeldeoEX()])
        self.assertEqual(c.DowsingMachine().canPlay(p4), False)

        p5 = PlayerState(hand=[c.DowsingMachine(), c.KeldeoEX()])
        self.assertEqual(c.DowsingMachine().canPlay(p5), False)

        p6 = PlayerState(hand=[c.DowsingMachine(),
                               c.KeldeoEX(),
                               c.KeldeoEX()],
                         discard=[c.N()])
        self.assertEqual(c.DowsingMachine().canPlay(p6), True)

    def test_CanPlayBattleCompressor(self):
        p1 = PlayerState()
        self.assertEqual(c.BattleCompressor().canPlay(p1), False)

        p2 = PlayerState(hand=[c.KeldeoEX()], deck=[c.WaterEnergy()])
        self.assertEqual(c.BattleCompressor().canPlay(p2), False)

        p3 = PlayerState(hand=[c.BattleCompressor()], 
                         deck=[c.WaterEnergy(),
                               c.WaterEnergy(),
                               c.WaterEnergy()])
        self.assertEqual(c.BattleCompressor().canPlay(p3), True)

        p4 = PlayerState(hand=[c.BattleCompressor()])
        self.assertEqual(c.BattleCompressor().canPlay(p4), False)

    def test_CanPlayBasic(self):
        p = PlayerState(hand=[c.KeldeoEX()])
        self.assertEqual(c.KeldeoEX().canPlay(p), True)

        p.bench.append(c.KeldeoEX())
        p.bench.append(c.KeldeoEX())
        p.bench.append(c.KeldeoEX())
        p.bench.append(c.KeldeoEX())
        self.assertEqual(c.KeldeoEX().canPlay(p), True)

        p.bench.append(c.KeldeoEX())
        self.assertEqual(c.KeldeoEX().canPlay(p), False)

        p.bench.append(c.KeldeoEX())
        self.assertEqual(c.KeldeoEX().canPlay(p), False)

    def test_CanPlayArchiesAceintheHole(self):
        p1 = PlayerState()
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p1), False)

        p2 = PlayerState(hand=[c.ArchiesAceintheHole()])
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p2), False)

        p3 = PlayerState(hand=[c.ArchiesAceintheHole()],
                         discard=[c.KeldeoEX()],
                         deck=[c.N(),
                               c.N(),
                               c.N(),
                               c.N(),
                               c.N()])
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p3), True)

        p4 = PlayerState(hand=[c.ArchiesAceintheHole(), c.ArchiesAceintheHole()],
                         discard=[c.KeldeoEX()])
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p4), False)

        p5 = PlayerState(hand=[],
                         discard=[c.KeldeoEX()])
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p5), False)

        p6 = PlayerState(hand=[c.ArchiesAceintheHole()],
                         discard=[c.Exeggcute()])
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p6), False)

        p7 = PlayerState(hand=[c.ArchiesAceintheHole()],
                         discard=[c.KeldeoEX()],
                         deck=[c.N(),
                               c.N(),
                               c.N(),
                               c.N(),
                               c.N()],
                         bench=[c.KeldeoEX(),
                                c.KeldeoEX(),
                                c.KeldeoEX(),
                                c.KeldeoEX(),
                                c.KeldeoEX()])
        self.assertEqual(c.ArchiesAceintheHole().canPlay(p7), False)

    def test_CanPlayWaterEnergy(self):
        p1 = PlayerState(hand=[c.WaterEnergy()])
        self.assertEqual(c.WaterEnergy().canPlay(p1), True)

        p2 = PlayerState(hand=[c.WaterEnergy()], attached_energy = True)
        self.assertEqual(c.WaterEnergy().canPlay(p2), False)

if __name__ == '__main__':
    unittest.main()


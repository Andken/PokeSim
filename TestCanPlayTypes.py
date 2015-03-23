#!/usr/bin/python

import unittest
import CardTypes as c
from PlayerState import PlayerState

import ArchiesAceintheHole
import BattleCompressor
import Bicycle
import Blastoise
import ComputerTrainer
import DowsingMachine
import EscapeRope
import Exeggcute
import GrassEnergy
import JirachiEX
import KeldeoEX
import LysandersTrumpCard
import Maintenance
import N
import PrimalKyogreEX
import ProfessorJuniper
import RandomReceiver
import Skyla
import Suicune
import SuperiorEnergyRetriever
import UltraBall
import VSSeeker
import WaterEnergy


class TestCanPlayTypes(unittest.TestCase):
    def test_CanPlayRandomReceiver(self):
        p1 = PlayerState(nondeterministic=True)
        self.assertEqual(RandomReceiver.RandomReceiver().canPlay(p1), False)

        p2 = PlayerState(hand=[RandomReceiver.RandomReceiver()],
                         deck=[WaterEnergy.WaterEnergy()],
                         nondeterministic=True)
        self.assertEqual(RandomReceiver.RandomReceiver().canPlay(p2), True)

        p3 = PlayerState(hand=[RandomReceiver.RandomReceiver()],nondeterministic=True)
        self.assertEqual(RandomReceiver.RandomReceiver().canPlay(p3), False)

        p4 = PlayerState(hand=[RandomReceiver.RandomReceiver()],
                         deck=[WaterEnergy.WaterEnergy()])
        self.assertEqual(RandomReceiver.RandomReceiver().canPlay(p4), False)

    def test_CanPlaySuperiorEnergyRetriever(self):
        p1 = PlayerState()
        self.assertEqual(SuperiorEnergyRetriever.SuperiorEnergyRetriever().canPlay(p1), False)

        p2 = PlayerState(hand=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(), N.N(), N.N()],
                         discard=[WaterEnergy.WaterEnergy()])
        self.assertEqual(SuperiorEnergyRetriever.SuperiorEnergyRetriever().canPlay(p2), True)

        p3 = PlayerState(hand=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(), N.N()],
                         discard=[WaterEnergy.WaterEnergy()])
        self.assertEqual(SuperiorEnergyRetriever.SuperiorEnergyRetriever().canPlay(p3), False)

    def test_CanPlayBicycle(self):
        p1 = PlayerState(nondeterministic = True)
        self.assertEqual(Bicycle.Bicycle().canPlay(p1), False)

        p2 = PlayerState(hand=[Bicycle.Bicycle()],
                         deck=[N.N(), N.N(), N.N(), N.N()],
                         nondeterministic = True)
        self.assertEqual(Bicycle.Bicycle().canPlay(p2), True)

        p2 = PlayerState(hand=[Bicycle.Bicycle(), N.N(), N.N()],
                         deck=[N.N(), N.N()],
                         nondeterministic = True)
        self.assertEqual(Bicycle.Bicycle().canPlay(p2), True)

        p3 = PlayerState(hand=[Bicycle.Bicycle(), N.N(), N.N(), N.N(), N.N()],
                         deck=[N.N(), N.N()],
                         nondeterministic = True)
        self.assertEqual(Bicycle.Bicycle().canPlay(p3), False)

        p4 = PlayerState(hand=[Bicycle.Bicycle()],
                         deck=[N.N(), N.N()],
                         nondeterministic = True)
        self.assertEqual(Bicycle.Bicycle().canPlay(p4), False)

        p5 = PlayerState(hand=[Bicycle.Bicycle(), N.N(), N.N()],
                         deck=[N.N(), N.N()])
        self.assertEqual(Bicycle.Bicycle().canPlay(p5), False)

    def test_CanPlayMaintenance(self):
        p1 = PlayerState(nondeterministic = True)
        self.assertEqual(Maintenance.Maintenance().canPlay(p1), False)

        p2 = PlayerState(hand=[Maintenance.Maintenance()],
                         nondeterministic = True)
        self.assertEqual(Maintenance.Maintenance().canPlay(p2), False)

        p3 = PlayerState(hand=[Maintenance.Maintenance(), N.N(), N.N()],
                         nondeterministic = True)
        self.assertEqual(Maintenance.Maintenance().canPlay(p3), True)

        p4 = PlayerState(hand=[Maintenance.Maintenance(), N.N(), N.N()])
        self.assertEqual(Maintenance.Maintenance().canPlay(p4), False)

    def test_CanPlayVSSeeker(self):
        p1 = PlayerState()
        self.assertEqual(VSSeeker.VSSeeker().canPlay(p1), False)

        p2 = PlayerState(hand=[VSSeeker.VSSeeker()], discard=[WaterEnergy.WaterEnergy()])
        self.assertEqual(VSSeeker.VSSeeker().canPlay(p2), False)

        p3 = PlayerState(hand=[VSSeeker.VSSeeker()], discard=[N.N()])
        self.assertEqual(VSSeeker.VSSeeker().canPlay(p3), True)

        p4 = PlayerState(hand=[VSSeeker.VSSeeker()])
        self.assertEqual(VSSeeker.VSSeeker().canPlay(p4), False)

        p5 = PlayerState(hand=[VSSeeker.VSSeeker(), KeldeoEX.KeldeoEX()],
                         discard=[N.N(), KeldeoEX.KeldeoEX()])
        self.assertEqual(VSSeeker.VSSeeker().canPlay(p5), True)

        p6 = PlayerState(hand=[VSSeeker.VSSeeker(), KeldeoEX.KeldeoEX()],
                         discard=[KeldeoEX.KeldeoEX(), N.N()])
        self.assertEqual(VSSeeker.VSSeeker().canPlay(p6), True)

    def test_CanPlayUltraBall(self):
        p1 = PlayerState()
        self.assertEqual(UltraBall.UltraBall().canPlay(p1), False)

        p2 = PlayerState(hand=[UltraBall.UltraBall()], deck=[WaterEnergy.WaterEnergy()])
        self.assertEqual(UltraBall.UltraBall().canPlay(p2), False)

        p3 = PlayerState(hand=[UltraBall.UltraBall(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()],
                         deck=[WaterEnergy.WaterEnergy()])
        self.assertEqual(UltraBall.UltraBall().canPlay(p3), True)

        p4 = PlayerState(hand=[UltraBall.UltraBall(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()])
        self.assertEqual(UltraBall.UltraBall().canPlay(p4), False)

        p5 = PlayerState(hand=[UltraBall.UltraBall(), KeldeoEX.KeldeoEX()])
        self.assertEqual(UltraBall.UltraBall().canPlay(p5), False)

    def test_CanPlayComputerTrainer(self):
        p1 = PlayerState()
        self.assertEqual(ComputerTrainer.ComputerTrainer().canPlay(p1), False)

        p2 = PlayerState(hand=[ComputerTrainer.ComputerTrainer()], deck=[WaterEnergy.WaterEnergy()])
        self.assertEqual(ComputerTrainer.ComputerTrainer().canPlay(p2), False)

        p3 = PlayerState(hand=[ComputerTrainer.ComputerTrainer(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()],
                         deck=[WaterEnergy.WaterEnergy()])
        self.assertEqual(ComputerTrainer.ComputerTrainer().canPlay(p3), True)

        p4 = PlayerState(hand=[ComputerTrainer.ComputerTrainer(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()])
        self.assertEqual(ComputerTrainer.ComputerTrainer().canPlay(p4), False)

        p5 = PlayerState(hand=[ComputerTrainer.ComputerTrainer(), KeldeoEX.KeldeoEX()])
        self.assertEqual(ComputerTrainer.ComputerTrainer().canPlay(p5), False)

    def test_CanPlayDowsingMachine(self):
        p1 = PlayerState()
        self.assertEqual(DowsingMachine.DowsingMachine().canPlay(p1), False)

        p2 = PlayerState(hand=[DowsingMachine.DowsingMachine()], discard=[WaterEnergy.WaterEnergy()])
        self.assertEqual(DowsingMachine.DowsingMachine().canPlay(p2), False)

        p3 = PlayerState(hand=[DowsingMachine.DowsingMachine(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()],
                         discard=[WaterEnergy.WaterEnergy()])
        self.assertEqual(DowsingMachine.DowsingMachine().canPlay(p3), False)

        p4 = PlayerState(hand=[DowsingMachine.DowsingMachine(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()])
        self.assertEqual(DowsingMachine.DowsingMachine().canPlay(p4), False)

        p5 = PlayerState(hand=[DowsingMachine.DowsingMachine(), KeldeoEX.KeldeoEX()])
        self.assertEqual(DowsingMachine.DowsingMachine().canPlay(p5), False)

        p6 = PlayerState(hand=[DowsingMachine.DowsingMachine(),
                               KeldeoEX.KeldeoEX(),
                               KeldeoEX.KeldeoEX()],
                         discard=[N.N()])
        self.assertEqual(DowsingMachine.DowsingMachine().canPlay(p6), True)

    def test_CanPlayBattleCompressor(self):
        p1 = PlayerState()
        self.assertEqual(BattleCompressor.BattleCompressor().canPlay(p1), False)

        p2 = PlayerState(hand=[KeldeoEX.KeldeoEX()], deck=[WaterEnergy.WaterEnergy()])
        self.assertEqual(BattleCompressor.BattleCompressor().canPlay(p2), False)

        p3 = PlayerState(hand=[BattleCompressor.BattleCompressor()], 
                         deck=[WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy()])
        self.assertEqual(BattleCompressor.BattleCompressor().canPlay(p3), True)

        p4 = PlayerState(hand=[BattleCompressor.BattleCompressor()])
        self.assertEqual(BattleCompressor.BattleCompressor().canPlay(p4), False)

    def test_CanPlayBasic(self):
        p = PlayerState(hand=[KeldeoEX.KeldeoEX()])
        self.assertEqual(KeldeoEX.KeldeoEX().canPlay(p), True)

        p.bench.append(KeldeoEX.KeldeoEX())
        p.bench.append(KeldeoEX.KeldeoEX())
        p.bench.append(KeldeoEX.KeldeoEX())
        p.bench.append(KeldeoEX.KeldeoEX())
        self.assertEqual(KeldeoEX.KeldeoEX().canPlay(p), True)

        p.bench.append(KeldeoEX.KeldeoEX())
        self.assertEqual(KeldeoEX.KeldeoEX().canPlay(p), False)

        p.bench.append(KeldeoEX.KeldeoEX())
        self.assertEqual(KeldeoEX.KeldeoEX().canPlay(p), False)

    def test_CanPlayArchiesAceintheHole(self):
        p1 = PlayerState()
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p1), False)

        p2 = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole()])
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p2), False)

        p3 = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard=[KeldeoEX.KeldeoEX()],
                         deck=[N.N(),
                               N.N(),
                               N.N(),
                               N.N(),
                               N.N()])
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p3), True)

        p4 = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole(), ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard=[KeldeoEX.KeldeoEX()])
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p4), False)

        p5 = PlayerState(hand=[],
                         discard=[KeldeoEX.KeldeoEX()])
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p5), False)

        p6 = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard=[Exeggcute.Exeggcute()])
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p6), False)

        p7 = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard=[KeldeoEX.KeldeoEX()],
                         deck=[N.N(),
                               N.N(),
                               N.N(),
                               N.N(),
                               N.N()],
                         bench=[KeldeoEX.KeldeoEX(),
                                KeldeoEX.KeldeoEX(),
                                KeldeoEX.KeldeoEX(),
                                KeldeoEX.KeldeoEX(),
                                KeldeoEX.KeldeoEX()])
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().canPlay(p7), False)

    def test_CanPlayWaterEnergy(self):
        p1 = PlayerState(hand=[WaterEnergy.WaterEnergy()])
        self.assertEqual(WaterEnergy.WaterEnergy().canPlay(p1), True)

        p2 = PlayerState(hand=[WaterEnergy.WaterEnergy()], attached_energy = True)
        self.assertEqual(WaterEnergy.WaterEnergy().canPlay(p2), False)

if __name__ == '__main__':
    unittest.main()


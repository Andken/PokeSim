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


class TestPlay(unittest.TestCase):
    def test_playRandomReceiver1(self):
        p = PlayerState(hand=[RandomReceiver.RandomReceiver()], 
                        deck=[N.N()], nondeterministic=True)

        possible_states = RandomReceiver.RandomReceiver().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[N.N()],
                         discard=[RandomReceiver.RandomReceiver()], 
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playRandomReceiver2(self):
        p = PlayerState(hand=[RandomReceiver.RandomReceiver()], 
                        deck=[WaterEnergy.WaterEnergy()], nondeterministic=True)

        possible_states = RandomReceiver.RandomReceiver().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(deck=[WaterEnergy.WaterEnergy()],
                         discard=[RandomReceiver.RandomReceiver()], 
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playRandomReceiver3(self):
        p = PlayerState(hand=[RandomReceiver.RandomReceiver()], 
                        deck=[N.N(), N.N()], nondeterministic=True)

        possible_states = RandomReceiver.RandomReceiver().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[N.N()],
                         discard=[RandomReceiver.RandomReceiver()],
                         deck=[N.N()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playRandomReceiver3(self):
        p = PlayerState(hand=[RandomReceiver.RandomReceiver()], 
                        deck=[WaterEnergy.WaterEnergy(), 
                              N.N(), 
                              WaterEnergy.WaterEnergy(), 
                              N.N(), 
                              KeldeoEX.KeldeoEX()], nondeterministic=True)

        possible_states = RandomReceiver.RandomReceiver().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[N.N()],
                         discard=[RandomReceiver.RandomReceiver()],
                         deck=[N.N(),
                               WaterEnergy.WaterEnergy(),
                               KeldeoEX.KeldeoEX(),
                               WaterEnergy.WaterEnergy()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playSuperiorEnergyRetriever1(self):
        p = PlayerState(hand=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(), 
                              N.N(), 
                              N.N()],
                        discard=[WaterEnergy.WaterEnergy()])

        possible_states = SuperiorEnergyRetriever.SuperiorEnergyRetriever().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[WaterEnergy.WaterEnergy()],
                         discard=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(),
                                  N.N(),
                                  N.N()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playSuperiorEnergyRetriever2(self):
        p = PlayerState(hand=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(), 
                              N.N(), 
                              N.N()],
                        discard=[WaterEnergy.WaterEnergy(), 
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy()])

        possible_states = SuperiorEnergyRetriever.SuperiorEnergyRetriever().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy()],
                         discard=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(),
                                  N.N(),
                                  N.N(),
                                  WaterEnergy.WaterEnergy()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playSuperiorEnergyRetriever3(self):
        p = PlayerState(hand=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(), 
                              N.N(), 
                              N.N()],
                        discard=[GrassEnergy.GrassEnergy(), 
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy()])

        possible_states = SuperiorEnergyRetriever.SuperiorEnergyRetriever().play(p)

        self.assertEqual(len(possible_states), 2)

        p1 = PlayerState(hand=[WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy()],
                         discard=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(),
                                  N.N(),
                                  N.N(),
                                  GrassEnergy.GrassEnergy()])

        p2 = PlayerState(hand=[GrassEnergy.GrassEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy()],
                         discard=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(),
                                  N.N(),
                                  N.N(),
                                  WaterEnergy.WaterEnergy()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)
        self.assertEqual(p2 in possible_states, True)


    def test_playSuperiorEnergyRetriever4(self):
        p = PlayerState(hand=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(), 
                              N.N(), 
                              N.N()],
                        discard=[WaterEnergy.WaterEnergy(), 
                                 GrassEnergy.GrassEnergy(),
                                 WaterEnergy.WaterEnergy()])

        possible_states = SuperiorEnergyRetriever.SuperiorEnergyRetriever().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[WaterEnergy.WaterEnergy(),
                               WaterEnergy.WaterEnergy(),
                               GrassEnergy.GrassEnergy()],
                         discard=[SuperiorEnergyRetriever.SuperiorEnergyRetriever(),
                                  N.N(),
                                  N.N()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)


    def test_playBicycle1(self):
        p = PlayerState(hand=[Bicycle.Bicycle(), 
                              N.N(), 
                              N.N()],
                        deck=[N.N(),N.N()],
                        nondeterministic=True)

        possible_states = Bicycle.Bicycle().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[N.N(),N.N(),N.N(),N.N()],
                         discard=[Bicycle.Bicycle()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playBicycle2(self):
        p = PlayerState(hand=[Bicycle.Bicycle(), 
                              N.N(), 
                              N.N()],
                        deck=[N.N(),N.N(),N.N()],
                        nondeterministic=True)

        possible_states = Bicycle.Bicycle().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[N.N(),N.N(),N.N(),N.N()],
                         discard=[Bicycle.Bicycle()],
                         deck=[N.N()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playMaintenance(self):
        p = PlayerState(hand=[Maintenance.Maintenance(), 
                              N.N(), 
                              KeldeoEX.KeldeoEX()], 
                        nondeterministic=True)

        possible_states = Maintenance.Maintenance().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[N.N()],
                         deck=[KeldeoEX.KeldeoEX()],
                         discard=[Maintenance.Maintenance()],
                         nondeterministic=True)

        p2 = PlayerState(hand=[KeldeoEX.KeldeoEX()],
                         deck=[N.N()],
                         discard=[Maintenance.Maintenance()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states or p2 in possible_states, True)

    def test_playJirachiEX1(self):
        p = PlayerState(hand=[JirachiEX.JirachiEX()],
                        deck=[N.N()])

        possible_states = JirachiEX.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 2)

        wo_supporter = PlayerState(bench=[JirachiEX.JirachiEX()],
                                   deck=[N.N()])

        w_supporter = PlayerState(bench=[JirachiEX.JirachiEX()],
                                  hand=[N.N()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(w_supporter in possible_states, True)
        self.assertEqual(wo_supporter in possible_states, True)

    def test_playJirachiEX2(self):
        p = PlayerState(hand=[JirachiEX.JirachiEX()],
                        deck=[N.N(), N.N()])

        possible_states = JirachiEX.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 2)

        wo_supporter = PlayerState(bench=[JirachiEX.JirachiEX()],
                                   deck=[N.N(), N.N()])

        w_supporter = PlayerState(bench=[JirachiEX.JirachiEX()],
                                  hand=[N.N()],
                                  deck=[N.N()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(w_supporter in possible_states, True)
        self.assertEqual(wo_supporter in possible_states, True)

    def test_playJirachiEX3(self):
        p = PlayerState(hand=[JirachiEX.JirachiEX()],
                        deck=[WaterEnergy.WaterEnergy()])

        possible_states = JirachiEX.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(bench=[JirachiEX.JirachiEX()],
                         deck=[WaterEnergy.WaterEnergy()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p2 in possible_states, True)

    def test_playJirachiEX3(self):
        p = PlayerState(hand=[JirachiEX.JirachiEX()])

        possible_states = JirachiEX.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(bench=[JirachiEX.JirachiEX()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p2 in possible_states, True)

    def test_playArchiesAceintheHole1(self):
        p = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole()],
                        deck=[WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy()],
                        discard=[Blastoise.Blastoise()])

        possible_states = ArchiesAceintheHole.ArchiesAceintheHole().play(p)

        self.assertEqual(len(possible_states), 1)
        for state in possible_states:
            self.assertEqual(state.hand == [WaterEnergy.WaterEnergy(),
                                            WaterEnergy.WaterEnergy(),
                                            WaterEnergy.WaterEnergy(),
                                            WaterEnergy.WaterEnergy(),
                                            WaterEnergy.WaterEnergy()], True)
            self.assertEqual(state.discard == [ArchiesAceintheHole.ArchiesAceintheHole()], True)
            self.assertEqual(state.bench == [Blastoise.Blastoise()], True)

    def test_playArchiesAceintheHole2(self):
        p = PlayerState(hand=[ArchiesAceintheHole.ArchiesAceintheHole()],
                        deck=[WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              WaterEnergy.WaterEnergy(),
                              UltraBall.UltraBall()],
                        discard=[Blastoise.Blastoise(), KeldeoEX.KeldeoEX()])

        possible_states = ArchiesAceintheHole.ArchiesAceintheHole().play(p)

        self.assertEqual(len(possible_states), 2)

        p1 = PlayerState(hand = [WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy()],
                         deck = [UltraBall.UltraBall()],
                         discard = [KeldeoEX.KeldeoEX(), ArchiesAceintheHole.ArchiesAceintheHole()],
                         bench = [Blastoise.Blastoise()])
        self.assertEqual(p1 in possible_states, True)

        p2 = PlayerState(hand = [WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy(),
                                 WaterEnergy.WaterEnergy()],
                         deck = [UltraBall.UltraBall()],
                         discard = [Blastoise.Blastoise(), ArchiesAceintheHole.ArchiesAceintheHole()],
                         bench = [KeldeoEX.KeldeoEX()])
        self.assertEqual(p2 in possible_states, True)

        self.assertEqual(p in possible_states, False)

    def test_playWaterEnergy(self):
        p = PlayerState(hand=[WaterEnergy.WaterEnergy()])

        possible_states = WaterEnergy.WaterEnergy().play(p)

        self.assertEqual(len(possible_states), 1)
        for state in possible_states:
            self.assertEqual(state.hand == [], True)
            self.assertEqual(state.attached_energy, True)

    def test_playVSSeeker(self):
        p = PlayerState(hand=[VSSeeker.VSSeeker()],
                        discard=[N.N(), Skyla.Skyla()])

        possible_states = VSSeeker.VSSeeker().play(p)

        self.assertEqual(len(possible_states), 2)
        
        pN = PlayerState(hand=[N.N()],
                         discard=[VSSeeker.VSSeeker(), Skyla.Skyla()])

        pSkyla = PlayerState(hand=[Skyla.Skyla()],
                             discard=[VSSeeker.VSSeeker(), N.N()])
    
        self.assertEqual(pN in possible_states, True)
        self.assertEqual(pSkyla in possible_states, True)
        self.assertEqual(p in possible_states, False)

    def test_playBasic(self):
        p1 = PlayerState()
        keldeo_ex = KeldeoEX.KeldeoEX()
        p1.hand.append(keldeo_ex)
        for p in keldeo_ex.play(p1):
            p2 = PlayerState()
            p2.bench.append(KeldeoEX.KeldeoEX())

            self.assertEquals(p == p2, True)


    def test_playUltraBall1(self):
        p1 = PlayerState(hand = [UltraBall.UltraBall(), 
                                 KeldeoEX.KeldeoEX(),
                                 KeldeoEX.KeldeoEX()],
                         deck = [Blastoise.Blastoise()])

        possible_states = UltraBall.UltraBall().play(p1)
        self.assertEqual(len(possible_states), 2)

        self.assertEqual(PlayerState(hand = [Blastoise.Blastoise()],
                                     discard = [UltraBall.UltraBall(), 
                                                KeldeoEX.KeldeoEX(), 
                                                KeldeoEX.KeldeoEX()]) in
                         possible_states, True)

        self.assertEqual(PlayerState(deck = [Blastoise.Blastoise()],
                                     discard = [UltraBall.UltraBall(), 
                                                KeldeoEX.KeldeoEX(), 
                                                KeldeoEX.KeldeoEX()]) in
                         possible_states, True)

        self.assertEqual(p1 in possible_states, False)


    def test_playUltraBall2(self):
        p1 = PlayerState(hand = [UltraBall.UltraBall(), 
                                 KeldeoEX.KeldeoEX(),
                                 KeldeoEX.KeldeoEX()],
                         deck = [Blastoise.Blastoise(), Bicycle.Bicycle()])

        possible_states = UltraBall.UltraBall().play(p1)
        self.assertEqual(len(possible_states), 2)

        self.assertEqual(PlayerState(hand = [Blastoise.Blastoise()],
                                     deck = [Bicycle.Bicycle()],
                                     discard = [UltraBall.UltraBall(), 
                                                KeldeoEX.KeldeoEX(), 
                                                KeldeoEX.KeldeoEX()]) in
                         possible_states, True)

        self.assertEqual(PlayerState(deck = [Blastoise.Blastoise(), 
                                             Bicycle.Bicycle()],
                                     discard = [UltraBall.UltraBall(), 
                                                KeldeoEX.KeldeoEX(), 
                                                KeldeoEX.KeldeoEX()]) in
                         possible_states, True)
        self.assertEqual(p1 in possible_states, False)


    def test_playComputerTrainer1(self):
        p1 = PlayerState(hand = [ComputerTrainer.ComputerTrainer(), 
                                 KeldeoEX.KeldeoEX(),
                                 KeldeoEX.KeldeoEX()],
                         deck = [Blastoise.Blastoise()])

        possible_states = ComputerTrainer.ComputerTrainer().play(p1)
        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [Blastoise.Blastoise()],
                         discard = [ComputerTrainer.ComputerTrainer(), 
                                    KeldeoEX.KeldeoEX(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playComputerTrainer2(self):
        p1 = PlayerState(hand = [ComputerTrainer.ComputerTrainer(), 
                                 KeldeoEX.KeldeoEX(),
                                 KeldeoEX.KeldeoEX()],
                         deck = [Blastoise.Blastoise(), ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = ComputerTrainer.ComputerTrainer().play(p1)
        self.assertEqual(len(possible_states), 2)

        p2 = PlayerState(hand = [Blastoise.Blastoise()],
                         deck = [ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard = [ComputerTrainer.ComputerTrainer(), 
                                    KeldeoEX.KeldeoEX(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(deck = [Blastoise.Blastoise()],
                         hand = [ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard = [ComputerTrainer.ComputerTrainer(), 
                                    KeldeoEX.KeldeoEX(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p3 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playComputerTrainer3(self):
        p1 = PlayerState(hand = [ComputerTrainer.ComputerTrainer(), 
                                 Exeggcute.Exeggcute(),
                                 WaterEnergy.WaterEnergy(),
                                 KeldeoEX.KeldeoEX()],
                         deck = [ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = ComputerTrainer.ComputerTrainer().play(p1)
        self.assertEqual(len(possible_states), 3)

        p2 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                 Exeggcute.Exeggcute()],
                         discard = [ComputerTrainer.ComputerTrainer(), 
                                    WaterEnergy.WaterEnergy(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                 KeldeoEX.KeldeoEX()],
                         discard = [ComputerTrainer.ComputerTrainer(), 
                                    WaterEnergy.WaterEnergy(), 
                                    Exeggcute.Exeggcute()])

        self.assertEqual(p3 in possible_states, True)

        p4 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                 WaterEnergy.WaterEnergy()],
                         discard = [ComputerTrainer.ComputerTrainer(), 
                                    KeldeoEX.KeldeoEX(), 
                                    Exeggcute.Exeggcute()])

        self.assertEqual(p4 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playComputerTrainer4(self):
        p = PlayerState(hand = [ComputerTrainer.ComputerTrainer(), 
                                Exeggcute.Exeggcute(),
                                WaterEnergy.WaterEnergy(),
                                KeldeoEX.KeldeoEX()],
                        deck = [Blastoise.Blastoise(), ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = ComputerTrainer.ComputerTrainer().play(p)
        self.assertEqual(len(possible_states), 6)

        for ps in possible_states:
            self.assertEqual(ComputerTrainer.ComputerTrainer() in ps.discard, True)
            self.assertEqual(ComputerTrainer.ComputerTrainer() in ps.hand, False)

            self.assertEqual(Blastoise.Blastoise() in ps.hand or
                             ArchiesAceintheHole.ArchiesAceintheHole() in ps.hand, True)
           
            self.assertEqual(len(set(ps.discard) & set([Exeggcute.Exeggcute(), 
                                                        WaterEnergy.WaterEnergy(), 
                                                        KeldeoEX.KeldeoEX()])), 2)
        self.assertEqual(p in possible_states, False)
 
    def test_playDowsingMachine1(self):
        p1 = PlayerState(hand = [DowsingMachine.DowsingMachine(), 
                                 KeldeoEX.KeldeoEX(),
                                 KeldeoEX.KeldeoEX()],
                         discard = [ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = DowsingMachine.DowsingMachine().play(p1)
        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard = [DowsingMachine.DowsingMachine(), 
                                    KeldeoEX.KeldeoEX(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playDowsingMachine2(self):
        p1 = PlayerState(hand = [DowsingMachine.DowsingMachine(), 
                                 KeldeoEX.KeldeoEX(),
                                 KeldeoEX.KeldeoEX()],
                         discard = [VSSeeker.VSSeeker(), ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = DowsingMachine.DowsingMachine().play(p1)
        self.assertEqual(len(possible_states), 2)

        p2 = PlayerState(hand = [VSSeeker.VSSeeker()],
                         discard = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                    DowsingMachine.DowsingMachine(), 
                                    KeldeoEX.KeldeoEX(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole()],
                         discard = [VSSeeker.VSSeeker(),
                                    DowsingMachine.DowsingMachine(), 
                                    KeldeoEX.KeldeoEX(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p3 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playDowsingMachine3(self):
        p1 = PlayerState(hand = [DowsingMachine.DowsingMachine(), 
                                 Exeggcute.Exeggcute(),
                                 WaterEnergy.WaterEnergy(),
                                 KeldeoEX.KeldeoEX()],
                         discard = [ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = DowsingMachine.DowsingMachine().play(p1)
        self.assertEqual(len(possible_states), 3)

        p2 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                 Exeggcute.Exeggcute()],
                         discard = [DowsingMachine.DowsingMachine(), 
                                    WaterEnergy.WaterEnergy(), 
                                    KeldeoEX.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                 KeldeoEX.KeldeoEX()],
                         discard = [DowsingMachine.DowsingMachine(), 
                                    WaterEnergy.WaterEnergy(), 
                                    Exeggcute.Exeggcute()])

        self.assertEqual(p3 in possible_states, True)

        p4 = PlayerState(hand = [ArchiesAceintheHole.ArchiesAceintheHole(),
                                 WaterEnergy.WaterEnergy()],
                         discard = [DowsingMachine.DowsingMachine(), 
                                    KeldeoEX.KeldeoEX(), 
                                    Exeggcute.Exeggcute()])

        self.assertEqual(p4 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playDowsingMachine4(self):
        p = PlayerState(hand = [DowsingMachine.DowsingMachine(), 
                                Exeggcute.Exeggcute(),
                                WaterEnergy.WaterEnergy(),
                                KeldeoEX.KeldeoEX()],
                        discard = [VSSeeker.VSSeeker(), ArchiesAceintheHole.ArchiesAceintheHole()])

        possible_states = DowsingMachine.DowsingMachine().play(p)
        self.assertEqual(len(possible_states), 6)

        for ps in possible_states:
            self.assertEqual(DowsingMachine.DowsingMachine() in ps.discard, True)
            self.assertEqual(DowsingMachine.DowsingMachine() in ps.hand, False)

            self.assertEqual(VSSeeker.VSSeeker() in ps.hand or
                             ArchiesAceintheHole.ArchiesAceintheHole() in ps.hand, True)
           
            self.assertEqual(len(set(ps.discard) & set([Exeggcute.Exeggcute(), 
                                                        WaterEnergy.WaterEnergy(), 
                                                        KeldeoEX.KeldeoEX()])), 2)
        self.assertEqual(p in possible_states, False)
 
    def test_playBattleCompressor1(self):
        p1 = PlayerState()
        battle_compressor = BattleCompressor.BattleCompressor()
        p1.hand.append(battle_compressor)
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(Blastoise.Blastoise())
        
        possible_states = sorted(battle_compressor.play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState()
        p2.discard.append(Blastoise.Blastoise())
        p2.discard.append(BattleCompressor.BattleCompressor())
        p2.deck.append(Blastoise.Blastoise())
        p2.deck.append(Blastoise.Blastoise())

        self.assertEqual(p2 == possible_states[0], True)
        self.assertEqual(p1 in possible_states, False)
        
    def test_playBattleCompressor2(self):
        p1 = PlayerState()
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(ArchiesAceintheHole.ArchiesAceintheHole())
        p1.deck.append(Exeggcute.Exeggcute())
        p1.discard.append(KeldeoEX.KeldeoEX())
        
        possible_states = sorted(BattleCompressor.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState()
        p2.hand.append(BattleCompressor.BattleCompressor())
        p2.discard.append(Blastoise.Blastoise())
        p2.discard.append(ArchiesAceintheHole.ArchiesAceintheHole())
        p2.discard.append(Exeggcute.Exeggcute())
        p2.discard.append(BattleCompressor.BattleCompressor())
        p2.discard.append(KeldeoEX.KeldeoEX())
        p2.deck.append(Blastoise.Blastoise())

        self.assertEqual(p2 == possible_states[0], True)
        self.assertEqual(p1 in possible_states, False)
        
    def test_playBattleCompressor3(self):
        p1 = PlayerState()
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(WaterEnergy.WaterEnergy())
        
        possible_states = sorted(BattleCompressor.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(discard=[WaterEnergy.WaterEnergy(), 
                                  BattleCompressor.BattleCompressor(), 
                                  Blastoise.Blastoise()], 
                         deck=[Blastoise.Blastoise()])

        self.assertEqual(p2 == possible_states[0], True)
        self.assertEqual(p1 in possible_states, False)
        
    def test_playBattleCompressor4(self):
        p1 = PlayerState()
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.hand.append(KeldeoEX.KeldeoEX())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        
        possible_states = sorted(BattleCompressor.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [KeldeoEX.KeldeoEX()],
                         discard=[WaterEnergy.WaterEnergy(), 
                                  BattleCompressor.BattleCompressor(), 
                                  WaterEnergy.WaterEnergy(), 
                                  Blastoise.Blastoise()], 
                         deck=[Blastoise.Blastoise(), WaterEnergy.WaterEnergy(), WaterEnergy.WaterEnergy()])
        
        self.assertEqual(p2 == possible_states[0], True)
        self.assertEqual(p1 in possible_states, False)
        
    def test_playBattleCompressor5(self):
        p1 = PlayerState()
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.deck.append(Exeggcute.Exeggcute())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        
        possible_states = sorted(BattleCompressor.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(discard=[WaterEnergy.WaterEnergy(), 
                                  BattleCompressor.BattleCompressor(), 
                                  Exeggcute.Exeggcute(),
                                  Blastoise.Blastoise()], 
                         deck=[WaterEnergy.WaterEnergy(), WaterEnergy.WaterEnergy(), WaterEnergy.WaterEnergy()])

        self.assertEqual(p2 == possible_states[0], True)
        self.assertEqual(p1 in possible_states, False)
        
    def test_playBattleCompressor6(self):
        p1 = PlayerState()
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.hand.append(BattleCompressor.BattleCompressor())
        p1.deck.append(Exeggcute.Exeggcute())
        p1.deck.append(Blastoise.Blastoise())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(WaterEnergy.WaterEnergy())
        p1.deck.append(ArchiesAceintheHole.ArchiesAceintheHole())
        
        possible_states = sorted(BattleCompressor.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [BattleCompressor.BattleCompressor()],
                         discard=[ArchiesAceintheHole.ArchiesAceintheHole(), 
                                  BattleCompressor.BattleCompressor(), 
                                  Exeggcute.Exeggcute(),
                                  Blastoise.Blastoise()], 
                         deck=[WaterEnergy.WaterEnergy(), WaterEnergy.WaterEnergy()])

        self.assertEqual(p2 == possible_states[0], True)
        
        possible_states = sorted(BattleCompressor.BattleCompressor().play(p2))

        p3 = PlayerState(discard=[ArchiesAceintheHole.ArchiesAceintheHole(), 
                                  BattleCompressor.BattleCompressor(), 
                                  BattleCompressor.BattleCompressor(), 
                                  Exeggcute.Exeggcute(),
                                  Blastoise.Blastoise(),
                                  WaterEnergy.WaterEnergy(),
                                  WaterEnergy.WaterEnergy()], 
                         deck=[])

        self.assertEqual(p3 == possible_states[0], True)
        self.assertEqual(p1 in possible_states, False)
        

if __name__ == '__main__':
    unittest.main()


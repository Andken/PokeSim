#!/usr/bin/python

import unittest
import CardTypes as ct
import PlayerState as ps
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


class TestPlayerState(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(hash(ps.PlayerState()), hash(ps.PlayerState()))

    def test_disaster(self):
        p2 = ps.PlayerState(hand=[Blastoise.Blastoise()])
        self.assertEquals(p2.disaster(Blastoise.Blastoise()), False)

        p4 = ps.PlayerState(deck=[Blastoise.Blastoise()])
        self.assertEquals(p4.disaster(Blastoise.Blastoise()), False)

        p5 = ps.PlayerState()
        self.assertEquals(p5.disaster(Blastoise.Blastoise()), True)

    def test_startingHand(self):
        p1 = ps.PlayerState(hand=[Blastoise.Blastoise(), N.N()])
        self.assertEquals(p1.startingHand(), False)

        p2 = ps.PlayerState(hand=[Blastoise.Blastoise(), N.N(), KeldeoEX.KeldeoEX()])
        self.assertEquals(p2.startingHand(), True)

        p3 = ps.PlayerState(hand=[KeldeoEX.KeldeoEX(), Blastoise.Blastoise(), N.N()])
        self.assertEquals(p3.startingHand(), True)

        p4 = ps.PlayerState(hand=[KeldeoEX.KeldeoEX()])
        self.assertEquals(p4.startingHand(), True)

    def test_placeActive1(self):
        p1 = ps.PlayerState(hand=[Exeggcute.Exeggcute()])
        p1.placeActive()

        p2 = ps.PlayerState(bench=[Exeggcute.Exeggcute()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive2(self):
        p1 = ps.PlayerState(hand=[KeldeoEX.KeldeoEX(), Exeggcute.Exeggcute()])
        p1.placeActive()

        p2 = ps.PlayerState(hand=[Exeggcute.Exeggcute()], bench=[KeldeoEX.KeldeoEX()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive3(self):
        p1 = ps.PlayerState(hand=[Exeggcute.Exeggcute(), KeldeoEX.KeldeoEX()])
        p1.placeActive()

        p2 = ps.PlayerState(hand=[Exeggcute.Exeggcute()], bench=[KeldeoEX.KeldeoEX()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive4(self):
        p1 = ps.PlayerState(hand=[Exeggcute.Exeggcute(), Blastoise.Blastoise()])
        p1.placeActive()

        p2 = ps.PlayerState(hand=[Blastoise.Blastoise()], bench=[Exeggcute.Exeggcute()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive1(self):
        p1 = ps.PlayerState(hand=[KeldeoEX.KeldeoEX()])
        p1.placeActive()

        p2 = ps.PlayerState(bench=[KeldeoEX.KeldeoEX()])
        self.assertEquals(p1 == p2, True)
        
    def test_eq1(self):
        p1 = ps.PlayerState()
        p2 = ps.PlayerState()

        self.assertEqual(p1 == p2, True)
        p1.hand.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p2.hand.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, True)

    def test_eq2(self):
        p1 = ps.PlayerState()
        p2 = ps.PlayerState()

        self.assertEqual(p1 == p2, True)
        p1.hand.append(KeldeoEX.KeldeoEX())
        self.assertNotEqual(p1, p2)
        p2.deck.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p1.deck.append(KeldeoEX.KeldeoEX())
        p2.hand.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, True)

    def test_eq3(self):
        p1 = ps.PlayerState()
        p2 = ps.PlayerState()

        self.assertEqual(p1 == p2, True)
        p1.hand.append(KeldeoEX.KeldeoEX())
        p1.hand.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p2.hand.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p2.hand.append(KeldeoEX.KeldeoEX())
        self.assertEqual(p1 == p2, True)


if __name__ == '__main__':
    unittest.main()


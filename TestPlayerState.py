#!/usr/bin/python

import unittest
import CardTypes as ct
import PlayerState as ps

class TestPlayerState(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(hash(ps.PlayerState()), hash(ps.PlayerState()))

    def test_disaster(self):
        p2 = ps.PlayerState(hand=[ct.Blastoise()])
        self.assertEquals(p2.disaster(ct.Blastoise()), False)

        p4 = ps.PlayerState(deck=[ct.Blastoise()])
        self.assertEquals(p4.disaster(ct.Blastoise()), False)

        p5 = ps.PlayerState()
        self.assertEquals(p5.disaster(ct.Blastoise()), True)

    def test_startingHand(self):
        p1 = ps.PlayerState(hand=[ct.Blastoise(), ct.N()])
        self.assertEquals(p1.startingHand(), False)

        p2 = ps.PlayerState(hand=[ct.Blastoise(), ct.N(), ct.KeldeoEX()])
        self.assertEquals(p2.startingHand(), True)

        p3 = ps.PlayerState(hand=[ct.KeldeoEX(), ct.Blastoise(), ct.N()])
        self.assertEquals(p3.startingHand(), True)

        p4 = ps.PlayerState(hand=[ct.KeldeoEX()])
        self.assertEquals(p4.startingHand(), True)

    def test_placeActive1(self):
        p1 = ps.PlayerState(hand=[ct.Exeggcute()])
        p1.placeActive()

        p2 = ps.PlayerState(bench=[ct.Exeggcute()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive2(self):
        p1 = ps.PlayerState(hand=[ct.KeldeoEX(), ct.Exeggcute()])
        p1.placeActive()

        p2 = ps.PlayerState(hand=[ct.Exeggcute()], bench=[ct.KeldeoEX()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive3(self):
        p1 = ps.PlayerState(hand=[ct.Exeggcute(), ct.KeldeoEX()])
        p1.placeActive()

        p2 = ps.PlayerState(hand=[ct.Exeggcute()], bench=[ct.KeldeoEX()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive4(self):
        p1 = ps.PlayerState(hand=[ct.Exeggcute(), ct.Blastoise()])
        p1.placeActive()

        p2 = ps.PlayerState(hand=[ct.Blastoise()], bench=[ct.Exeggcute()])
        self.assertEquals(p1 == p2, True)
        
    def test_placeActive1(self):
        p1 = ps.PlayerState(hand=[ct.KeldeoEX()])
        p1.placeActive()

        p2 = ps.PlayerState(bench=[ct.KeldeoEX()])
        self.assertEquals(p1 == p2, True)
        
    def test_eq1(self):
        p1 = ps.PlayerState()
        p2 = ps.PlayerState()

        self.assertEqual(p1 == p2, True)
        p1.hand.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p2.hand.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, True)

    def test_eq2(self):
        p1 = ps.PlayerState()
        p2 = ps.PlayerState()

        self.assertEqual(p1 == p2, True)
        p1.hand.append(ct.KeldeoEX())
        self.assertNotEqual(p1, p2)
        p2.deck.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p1.deck.append(ct.KeldeoEX())
        p2.hand.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, True)

    def test_eq3(self):
        p1 = ps.PlayerState()
        p2 = ps.PlayerState()

        self.assertEqual(p1 == p2, True)
        p1.hand.append(ct.KeldeoEX())
        p1.hand.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p2.hand.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, False)
        p2.hand.append(ct.KeldeoEX())
        self.assertEqual(p1 == p2, True)


if __name__ == '__main__':
    unittest.main()


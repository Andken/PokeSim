#!/usr/bin/python

import unittest
import CardTypes as ct
import PlayerState as ps

class TestPlayerState(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(hash(ps.PlayerState()), hash(ps.PlayerState()))

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


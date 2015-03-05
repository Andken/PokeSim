#!/usr/bin/python

import unittest
import CardTypes as c
from PlayerState import PlayerState

class TestPlay(unittest.TestCase):
    def test_playBasic(self):
        p1 = PlayerState()
        keldeo_ex = c.KeldeoEX()
        p1.hand.append(keldeo_ex)
        for p in keldeo_ex.play(p1):
            p2 = PlayerState()
            p2.bench.append(c.KeldeoEX())

            self.assertEquals(p == p2, True)

    def test_playSimpleBattleCompressor(self):
        p1 = PlayerState()
        battle_compressor = c.BattleCompressor()
        p1.hand.append(battle_compressor)
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        
        possible_states = sorted(battle_compressor.play(p1))

        print len(possible_states)


        

if __name__ == '__main__':
    unittest.main()


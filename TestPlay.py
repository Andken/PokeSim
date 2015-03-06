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

    def test_playComputerTrainer1(self):
        p1 = PlayerState(hand = [c.ComputerTrainer(), 
                                 c.KeldeoEX(),
                                 c.KeldeoEX()],
                         deck = [c.Blastoise()])

        possible_states = c.ComputerTrainer().play(p1)
        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [c.Blastoise()],
                         discard = [c.ComputerTrainer(), 
                                    c.KeldeoEX(), 
                                    c.KeldeoEX()])

        self.assertEqual(possible_states[0] == p2, True)

    def test_playComputerTrainer2(self):
        p1 = PlayerState(hand = [c.ComputerTrainer(), 
                                 c.KeldeoEX(),
                                 c.KeldeoEX()],
                         deck = [c.Blastoise(), c.ArchiesAceintheHole()])

        possible_states = c.ComputerTrainer().play(p1)
        self.assertEqual(len(possible_states), 2)

        p2 = PlayerState(hand = [c.Blastoise()],
                         deck = [c.ArchiesAceintheHole()],
                         discard = [c.ComputerTrainer(), 
                                    c.KeldeoEX(), 
                                    c.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(deck = [c.Blastoise()],
                         hand = [c.ArchiesAceintheHole()],
                         discard = [c.ComputerTrainer(), 
                                    c.KeldeoEX(), 
                                    c.KeldeoEX()])

        self.assertEqual(p3 in possible_states, True)

    def test_playComputerTrainer3(self):
        p1 = PlayerState(hand = [c.ComputerTrainer(), 
                                 c.Exeggcute(),
                                 c.WaterEnergy(),
                                 c.KeldeoEX()],
                         deck = [c.ArchiesAceintheHole()])

        possible_states = c.ComputerTrainer().play(p1)
        self.assertEqual(len(possible_states), 3)

        p2 = PlayerState(hand = [c.ArchiesAceintheHole(),
                                 c.Exeggcute()],
                         discard = [c.ComputerTrainer(), 
                                    c.WaterEnergy(), 
                                    c.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(hand = [c.ArchiesAceintheHole(),
                                 c.KeldeoEX()],
                         discard = [c.ComputerTrainer(), 
                                    c.WaterEnergy(), 
                                    c.Exeggcute()])

        self.assertEqual(p3 in possible_states, True)

        p4 = PlayerState(hand = [c.ArchiesAceintheHole(),
                                 c.WaterEnergy()],
                         discard = [c.ComputerTrainer(), 
                                    c.KeldeoEX(), 
                                    c.Exeggcute()])

        self.assertEqual(p4 in possible_states, True)

    def test_playBattleCompressor1(self):
        p1 = PlayerState()
        battle_compressor = c.BattleCompressor()
        p1.hand.append(battle_compressor)
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        
        possible_states = sorted(battle_compressor.play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState()
        p2.discard.append(c.Blastoise())
        p2.discard.append(c.BattleCompressor())
        p2.deck.append(c.Blastoise())
        p2.deck.append(c.Blastoise())

        self.assertEqual(p2 == possible_states[0], True)
        
    def test_playBattleCompressor2(self):
        p1 = PlayerState()
        p1.hand.append(c.BattleCompressor())
        p1.hand.append(c.BattleCompressor())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.ArchiesAceintheHole())
        p1.deck.append(c.Exeggcute())
        p1.discard.append(c.KeldeoEX())
        
        possible_states = sorted(c.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState()
        p2.hand.append(c.BattleCompressor())
        p2.discard.append(c.Blastoise())
        p2.discard.append(c.ArchiesAceintheHole())
        p2.discard.append(c.Exeggcute())
        p2.discard.append(c.BattleCompressor())
        p2.discard.append(c.KeldeoEX())
        p2.deck.append(c.Blastoise())

        self.assertEqual(p2 == possible_states[0], True)
        
    def test_playBattleCompressor3(self):
        p1 = PlayerState()
        p1.hand.append(c.BattleCompressor())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.WaterEnergy())
        
        possible_states = sorted(c.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(discard=[c.WaterEnergy(), 
                                  c.BattleCompressor(), 
                                  c.Blastoise()], 
                         deck=[c.Blastoise()])

        self.assertEqual(p2 == possible_states[0], True)
        
    def test_playBattleCompressor4(self):
        p1 = PlayerState()
        p1.hand.append(c.BattleCompressor())
        p1.hand.append(c.KeldeoEX())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        
        possible_states = sorted(c.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [c.KeldeoEX()],
                         discard=[c.WaterEnergy(), 
                                  c.BattleCompressor(), 
                                  c.WaterEnergy(), 
                                  c.Blastoise()], 
                         deck=[c.Blastoise(), c.WaterEnergy(), c.WaterEnergy()])
        
        self.assertEqual(p2 == possible_states[0], True)
        
    def test_playBattleCompressor5(self):
        p1 = PlayerState()
        p1.hand.append(c.BattleCompressor())
        p1.deck.append(c.Exeggcute())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        
        possible_states = sorted(c.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(discard=[c.WaterEnergy(), 
                                  c.BattleCompressor(), 
                                  c.Exeggcute(),
                                  c.Blastoise()], 
                         deck=[c.WaterEnergy(), c.WaterEnergy(), c.WaterEnergy()])

        self.assertEqual(p2 == possible_states[0], True)
        
    def test_playBattleCompressor6(self):
        p1 = PlayerState()
        p1.hand.append(c.BattleCompressor())
        p1.hand.append(c.BattleCompressor())
        p1.deck.append(c.Exeggcute())
        p1.deck.append(c.Blastoise())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.WaterEnergy())
        p1.deck.append(c.ArchiesAceintheHole())
        
        possible_states = sorted(c.BattleCompressor().play(p1))

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [c.BattleCompressor()],
                         discard=[c.ArchiesAceintheHole(), 
                                  c.BattleCompressor(), 
                                  c.Exeggcute(),
                                  c.Blastoise()], 
                         deck=[c.WaterEnergy(), c.WaterEnergy()])

        self.assertEqual(p2 == possible_states[0], True)
        
        possible_states = sorted(c.BattleCompressor().play(p2))

        p3 = PlayerState(discard=[c.ArchiesAceintheHole(), 
                                  c.BattleCompressor(), 
                                  c.BattleCompressor(), 
                                  c.Exeggcute(),
                                  c.Blastoise(),
                                  c.WaterEnergy(),
                                  c.WaterEnergy()], 
                         deck=[])

        self.assertEqual(p3 == possible_states[0], True)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)


#!/usr/bin/python

import unittest
import CardTypes as c
from PlayerState import PlayerState

class TestPlay(unittest.TestCase):
    def test_playBicycle1(self):
        p = PlayerState(hand=[c.Bicycle(), 
                              c.N(), 
                              c.N()],
                        deck=[c.N(),c.N()],
                        nondeterministic=True)

        possible_states = c.Bicycle().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[c.N(),c.N(),c.N(),c.N()],
                         discard=[c.Bicycle()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playBicycle2(self):
        p = PlayerState(hand=[c.Bicycle(), 
                              c.N(), 
                              c.N()],
                        deck=[c.N(),c.N(),c.N()],
                        nondeterministic=True)

        possible_states = c.Bicycle().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[c.N(),c.N(),c.N(),c.N()],
                         discard=[c.Bicycle()],
                         deck=[c.N()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states, True)

    def test_playMaintenance(self):
        p = PlayerState(hand=[c.Maintenance(), 
                              c.N(), 
                              c.KeldeoEX()], 
                        nondeterministic=True)

        possible_states = c.Maintenance().play(p)

        self.assertEqual(len(possible_states), 1)

        p1 = PlayerState(hand=[c.N()],
                         deck=[c.KeldeoEX()],
                         discard=[c.Maintenance()],
                         nondeterministic=True)

        p2 = PlayerState(hand=[c.KeldeoEX()],
                         deck=[c.N()],
                         discard=[c.Maintenance()],
                         nondeterministic=True)

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p1 in possible_states or p2 in possible_states, True)

    def test_playJirachiEX1(self):
        p = PlayerState(hand=[c.JirachiEX()],
                        deck=[c.N()])

        possible_states = c.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 2)

        wo_supporter = PlayerState(bench=[c.JirachiEX()],
                                   deck=[c.N()])

        w_supporter = PlayerState(bench=[c.JirachiEX()],
                                  hand=[c.N()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(w_supporter in possible_states, True)
        self.assertEqual(wo_supporter in possible_states, True)

    def test_playJirachiEX2(self):
        p = PlayerState(hand=[c.JirachiEX()],
                        deck=[c.N(), c.N()])

        possible_states = c.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 2)

        wo_supporter = PlayerState(bench=[c.JirachiEX()],
                                   deck=[c.N(), c.N()])

        w_supporter = PlayerState(bench=[c.JirachiEX()],
                                  hand=[c.N()],
                                  deck=[c.N()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(w_supporter in possible_states, True)
        self.assertEqual(wo_supporter in possible_states, True)

    def test_playJirachiEX3(self):
        p = PlayerState(hand=[c.JirachiEX()],
                        deck=[c.WaterEnergy()])

        possible_states = c.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(bench=[c.JirachiEX()],
                         deck=[c.WaterEnergy()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p2 in possible_states, True)

    def test_playJirachiEX3(self):
        p = PlayerState(hand=[c.JirachiEX()])

        possible_states = c.JirachiEX().play(p)

        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(bench=[c.JirachiEX()])

        self.assertEqual(p in possible_states, False)
        self.assertEqual(p2 in possible_states, True)

    def test_playArchiesAceintheHole1(self):
        p = PlayerState(hand=[c.ArchiesAceintheHole()],
                        deck=[c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.WaterEnergy()],
                        discard=[c.Blastoise()])

        possible_states = c.ArchiesAceintheHole().play(p)

        self.assertEqual(len(possible_states), 1)
        for state in possible_states:
            self.assertEqual(state.hand == [c.WaterEnergy(),
                                            c.WaterEnergy(),
                                            c.WaterEnergy(),
                                            c.WaterEnergy(),
                                            c.WaterEnergy()], True)
            self.assertEqual(state.discard == [c.ArchiesAceintheHole()], True)
            self.assertEqual(state.bench == [c.Blastoise()], True)

    def test_playArchiesAceintheHole2(self):
        p = PlayerState(hand=[c.ArchiesAceintheHole()],
                        deck=[c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.WaterEnergy(),
                              c.UltraBall()],
                        discard=[c.Blastoise(), c.KeldeoEX()])

        possible_states = c.ArchiesAceintheHole().play(p)

        self.assertEqual(len(possible_states), 2)

        p1 = PlayerState(hand = [c.WaterEnergy(),
                                 c.WaterEnergy(),
                                 c.WaterEnergy(),
                                 c.WaterEnergy(),
                                 c.WaterEnergy()],
                         deck = [c.UltraBall()],
                         discard = [c.KeldeoEX(), c.ArchiesAceintheHole()],
                         bench = [c.Blastoise()])
        self.assertEqual(p1 in possible_states, True)

        p2 = PlayerState(hand = [c.WaterEnergy(),
                                 c.WaterEnergy(),
                                 c.WaterEnergy(),
                                 c.WaterEnergy(),
                                 c.WaterEnergy()],
                         deck = [c.UltraBall()],
                         discard = [c.Blastoise(), c.ArchiesAceintheHole()],
                         bench = [c.KeldeoEX()])
        self.assertEqual(p2 in possible_states, True)

        self.assertEqual(p in possible_states, False)

    def test_playWaterEnergy(self):
        p = PlayerState(hand=[c.WaterEnergy()])

        possible_states = c.WaterEnergy().play(p)

        self.assertEqual(len(possible_states), 1)
        for state in possible_states:
            self.assertEqual(state.hand == [], True)
            self.assertEqual(state.attached_energy, True)

    def test_playVSSeeker(self):
        p = PlayerState(hand=[c.VSSeeker()],
                        discard=[c.N(), c.Skyla()])

        possible_states = c.VSSeeker().play(p)

        self.assertEqual(len(possible_states), 2)
        
        pN = PlayerState(hand=[c.N()],
                         discard=[c.VSSeeker(), c.Skyla()])

        pSkyla = PlayerState(hand=[c.Skyla()],
                             discard=[c.VSSeeker(), c.N()])
    
        self.assertEqual(pN in possible_states, True)
        self.assertEqual(pSkyla in possible_states, True)
        self.assertEqual(p in possible_states, False)

    def test_playBasic(self):
        p1 = PlayerState()
        keldeo_ex = c.KeldeoEX()
        p1.hand.append(keldeo_ex)
        for p in keldeo_ex.play(p1):
            p2 = PlayerState()
            p2.bench.append(c.KeldeoEX())

            self.assertEquals(p == p2, True)


    def test_playUltraBall1(self):
        p1 = PlayerState(hand = [c.UltraBall(), 
                                 c.KeldeoEX(),
                                 c.KeldeoEX()],
                         deck = [c.Blastoise()])

        possible_states = c.UltraBall().play(p1)
        self.assertEqual(len(possible_states), 2)

        self.assertEqual(PlayerState(hand = [c.Blastoise()],
                                     discard = [c.UltraBall(), 
                                                c.KeldeoEX(), 
                                                c.KeldeoEX()]) in
                         possible_states, True)

        self.assertEqual(PlayerState(deck = [c.Blastoise()],
                                     discard = [c.UltraBall(), 
                                                c.KeldeoEX(), 
                                                c.KeldeoEX()]) in
                         possible_states, True)

        self.assertEqual(p1 in possible_states, False)


    def test_playUltraBall2(self):
        p1 = PlayerState(hand = [c.UltraBall(), 
                                 c.KeldeoEX(),
                                 c.KeldeoEX()],
                         deck = [c.Blastoise(), c.Bicycle()])

        possible_states = c.UltraBall().play(p1)
        self.assertEqual(len(possible_states), 2)

        self.assertEqual(PlayerState(hand = [c.Blastoise()],
                                     deck = [c.Bicycle()],
                                     discard = [c.UltraBall(), 
                                                c.KeldeoEX(), 
                                                c.KeldeoEX()]) in
                         possible_states, True)

        self.assertEqual(PlayerState(deck = [c.Blastoise(), 
                                             c.Bicycle()],
                                     discard = [c.UltraBall(), 
                                                c.KeldeoEX(), 
                                                c.KeldeoEX()]) in
                         possible_states, True)
        self.assertEqual(p1 in possible_states, False)


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

        self.assertEqual(p2 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

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
        self.assertEqual(p1 in possible_states, False)

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
        self.assertEqual(p1 in possible_states, False)

    def test_playComputerTrainer4(self):
        p = PlayerState(hand = [c.ComputerTrainer(), 
                                c.Exeggcute(),
                                c.WaterEnergy(),
                                c.KeldeoEX()],
                        deck = [c.Blastoise(), c.ArchiesAceintheHole()])

        possible_states = c.ComputerTrainer().play(p)
        self.assertEqual(len(possible_states), 6)

        for ps in possible_states:
            self.assertEqual(c.ComputerTrainer() in ps.discard, True)
            self.assertEqual(c.ComputerTrainer() in ps.hand, False)

            self.assertEqual(c.Blastoise() in ps.hand or
                             c.ArchiesAceintheHole() in ps.hand, True)
           
            self.assertEqual(len(set(ps.discard) & set([c.Exeggcute(), 
                                                        c.WaterEnergy(), 
                                                        c.KeldeoEX()])), 2)
        self.assertEqual(p in possible_states, False)
 
    def test_playDowsingMachine1(self):
        p1 = PlayerState(hand = [c.DowsingMachine(), 
                                 c.KeldeoEX(),
                                 c.KeldeoEX()],
                         discard = [c.ArchiesAceintheHole()])

        possible_states = c.DowsingMachine().play(p1)
        self.assertEqual(len(possible_states), 1)

        p2 = PlayerState(hand = [c.ArchiesAceintheHole()],
                         discard = [c.DowsingMachine(), 
                                    c.KeldeoEX(), 
                                    c.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playDowsingMachine2(self):
        p1 = PlayerState(hand = [c.DowsingMachine(), 
                                 c.KeldeoEX(),
                                 c.KeldeoEX()],
                         discard = [c.VSSeeker(), c.ArchiesAceintheHole()])

        possible_states = c.DowsingMachine().play(p1)
        self.assertEqual(len(possible_states), 2)

        p2 = PlayerState(hand = [c.VSSeeker()],
                         discard = [c.ArchiesAceintheHole(),
                                    c.DowsingMachine(), 
                                    c.KeldeoEX(), 
                                    c.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(hand = [c.ArchiesAceintheHole()],
                         discard = [c.VSSeeker(),
                                    c.DowsingMachine(), 
                                    c.KeldeoEX(), 
                                    c.KeldeoEX()])

        self.assertEqual(p3 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playDowsingMachine3(self):
        p1 = PlayerState(hand = [c.DowsingMachine(), 
                                 c.Exeggcute(),
                                 c.WaterEnergy(),
                                 c.KeldeoEX()],
                         discard = [c.ArchiesAceintheHole()])

        possible_states = c.DowsingMachine().play(p1)
        self.assertEqual(len(possible_states), 3)

        p2 = PlayerState(hand = [c.ArchiesAceintheHole(),
                                 c.Exeggcute()],
                         discard = [c.DowsingMachine(), 
                                    c.WaterEnergy(), 
                                    c.KeldeoEX()])

        self.assertEqual(p2 in possible_states, True)

        p3 = PlayerState(hand = [c.ArchiesAceintheHole(),
                                 c.KeldeoEX()],
                         discard = [c.DowsingMachine(), 
                                    c.WaterEnergy(), 
                                    c.Exeggcute()])

        self.assertEqual(p3 in possible_states, True)

        p4 = PlayerState(hand = [c.ArchiesAceintheHole(),
                                 c.WaterEnergy()],
                         discard = [c.DowsingMachine(), 
                                    c.KeldeoEX(), 
                                    c.Exeggcute()])

        self.assertEqual(p4 in possible_states, True)
        self.assertEqual(p1 in possible_states, False)

    def test_playDowsingMachine4(self):
        p = PlayerState(hand = [c.DowsingMachine(), 
                                c.Exeggcute(),
                                c.WaterEnergy(),
                                c.KeldeoEX()],
                        discard = [c.VSSeeker(), c.ArchiesAceintheHole()])

        possible_states = c.DowsingMachine().play(p)
        self.assertEqual(len(possible_states), 6)

        for ps in possible_states:
            self.assertEqual(c.DowsingMachine() in ps.discard, True)
            self.assertEqual(c.DowsingMachine() in ps.hand, False)

            self.assertEqual(c.VSSeeker() in ps.hand or
                             c.ArchiesAceintheHole() in ps.hand, True)
           
            self.assertEqual(len(set(ps.discard) & set([c.Exeggcute(), 
                                                        c.WaterEnergy(), 
                                                        c.KeldeoEX()])), 2)
        self.assertEqual(p in possible_states, False)
 
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
        self.assertEqual(p1 in possible_states, False)
        
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
        self.assertEqual(p1 in possible_states, False)
        
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
        self.assertEqual(p1 in possible_states, False)
        
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
        self.assertEqual(p1 in possible_states, False)
        
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
        self.assertEqual(p1 in possible_states, False)
        
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
        self.assertEqual(p1 in possible_states, False)
        

if __name__ == '__main__':
    unittest.main()


#!/usr/bin/python

import unittest
import CardTypes as ct

class TestCardTypes(unittest.TestCase):
    def test_isWaterType(self):
        self.assertEqual(ct.Card().isWaterType(), False)
        self.assertEqual(ct.BasicPokemon().isWaterType(), False)
        self.assertEqual(ct.DiscardType().isWaterType(), False)
        self.assertEqual(ct.Energy().isWaterType(), False)
        self.assertEqual(ct.Supporter().isWaterType(), False)
        self.assertEqual(ct.ArchiesAceintheHole().isWaterType(), False)
        self.assertEqual(ct.Bicycle().isWaterType(), False)
        self.assertEqual(ct.BattleCompressor().isWaterType(), False)
        self.assertEqual(ct.Blastoise().isWaterType(), True)
        self.assertEqual(ct.ComputerTrainer().isWaterType(), False)
        self.assertEqual(ct.EscapeRope().isWaterType(), False)
        self.assertEqual(ct.Exeggcute().isWaterType(), False)
        self.assertEqual(ct.KeldeoEX().isWaterType(), True)
        self.assertEqual(ct.Maintenance().isWaterType(), False)
        self.assertEqual(ct.N().isWaterType(), False)
        self.assertEqual(ct.ProfessorJuniper().isWaterType(), False)
        self.assertEqual(ct.Skyla().isWaterType(), False)
        self.assertEqual(ct.Suicune().isWaterType(), True)
        self.assertEqual(ct.SuperiorEnergyRetriever().isWaterType(), False)
        self.assertEqual(ct.UltraBall().isWaterType(), False)
        self.assertEqual(ct.VSSeeker().isWaterType(), False)
        self.assertEqual(ct.WaterEnergy().isWaterType(), False)

if __name__ == '__main__':
    unittest.main()


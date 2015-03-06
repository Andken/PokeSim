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

    def test_name(self):
        self.assertEqual(ct.ArchiesAceintheHole().name(), "Archie's Ace in the Hole")
        self.assertEqual(ct.Bicycle().name(), "Bicycle")
        self.assertEqual(ct.BattleCompressor().name(), "Battle Compressor")
        self.assertEqual(ct.Blastoise().name(), "Blastoise")
        self.assertEqual(ct.ComputerTrainer().name(), "Computer Trainer")
        self.assertEqual(ct.EscapeRope().name(), "Escape Rope")
        self.assertEqual(ct.Exeggcute().name(), "Exeggcute")
        self.assertEqual(ct.KeldeoEX().name(), "Keldeo EX")
        self.assertEqual(ct.Maintenance().name(), "Maintenance")
        self.assertEqual(ct.N().name(), "N")
        self.assertEqual(ct.ProfessorJuniper().name(), "Professor Juniper")
        self.assertEqual(ct.Skyla().name(), "Skyla")
        self.assertEqual(ct.Suicune().name(), "Suicune")
        self.assertEqual(ct.SuperiorEnergyRetriever().name(), "Superior Energy Retriever")
        self.assertEqual(ct.UltraBall().name(), "Ultra Ball")
        self.assertEqual(ct.VSSeeker().name(), "VS Seeker")
        self.assertEqual(ct.WaterEnergy().name(), "Water Energy")

    def test_hash(self):
        self.assertEqual(hash(ct.KeldeoEX()), hash(ct.KeldeoEX()))

    def test_eq(self):
        c1 = ct.KeldeoEX()
        c2 = ct.KeldeoEX()
        self.assertEqual(c1==c2, True)

    def test_isPokemon(self):
        self.assertEqual(ct.Card().isPokemon(), False)
        self.assertEqual(ct.BasicPokemon().isPokemon(), True)
        self.assertEqual(ct.DiscardType().isPokemon(), False)
        self.assertEqual(ct.Energy().isPokemon(), False)
        self.assertEqual(ct.Supporter().isPokemon(), False)
        self.assertEqual(ct.ArchiesAceintheHole().isPokemon(), False)
        self.assertEqual(ct.Bicycle().isPokemon(), False)
        self.assertEqual(ct.BattleCompressor().isPokemon(), False)
        self.assertEqual(ct.Blastoise().isPokemon(), True)
        self.assertEqual(ct.ComputerTrainer().isPokemon(), False)
        self.assertEqual(ct.EscapeRope().isPokemon(), False)
        self.assertEqual(ct.Exeggcute().isPokemon(), True)
        self.assertEqual(ct.KeldeoEX().isPokemon(), True)
        self.assertEqual(ct.Maintenance().isPokemon(), False)
        self.assertEqual(ct.N().isPokemon(), False)
        self.assertEqual(ct.ProfessorJuniper().isPokemon(), False)
        self.assertEqual(ct.Skyla().isPokemon(), False)
        self.assertEqual(ct.Suicune().isPokemon(), True)
        self.assertEqual(ct.SuperiorEnergyRetriever().isPokemon(), False)
        self.assertEqual(ct.UltraBall().isPokemon(), False)
        self.assertEqual(ct.VSSeeker().isPokemon(), False)
        self.assertEqual(ct.WaterEnergy().isPokemon(), False)


if __name__ == '__main__':
    unittest.main()


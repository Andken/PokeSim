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
        self.assertEqual(ct.DowsingMachine().isWaterType(), False)
        self.assertEqual(ct.EscapeRope().isWaterType(), False)
        self.assertEqual(ct.Exeggcute().isWaterType(), False)
        self.assertEqual(ct.KeldeoEX().isWaterType(), True)
        self.assertEqual(ct.JirachiEX().isWaterType(), False)
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
        self.assertEqual(ct.DowsingMachine().name(), "Dowsing Machine")
        self.assertEqual(ct.EscapeRope().name(), "Escape Rope")
        self.assertEqual(ct.Exeggcute().name(), "Exeggcute")
        self.assertEqual(ct.JirachiEX().name(), "Jirachi EX")
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
        self.assertEqual(isinstance(ct.Card(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.BasicPokemon(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.DiscardType(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Energy(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Supporter(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.ArchiesAceintheHole(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Bicycle(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.BattleCompressor(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Blastoise(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.ComputerTrainer(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.EscapeRope(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Exeggcute(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.KeldeoEX(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.JirachiEX(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.Maintenance(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.N(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.ProfessorJuniper(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Skyla(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Suicune(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.SuperiorEnergyRetriever(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.UltraBall(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.VSSeeker(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.WaterEnergy(), ct.Pokemon), False)

    def test_isTrainer(self):
        self.assertEqual(isinstance(ct.Card(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.BasicPokemon(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.DiscardType(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.Energy(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.Supporter(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.ArchiesAceintheHole(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.Bicycle(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.BattleCompressor(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.Blastoise(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.ComputerTrainer(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.EscapeRope(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.Exeggcute(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.KeldeoEX(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.JirachiEX(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.Maintenance(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.N(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.ProfessorJuniper(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.Skyla(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.Suicune(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.SuperiorEnergyRetriever(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.UltraBall(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.VSSeeker(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.WaterEnergy(), ct.Trainer), False)

    def test_isSupporter(self):
        self.assertEqual(isinstance(ct.Card(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.BasicPokemon(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.DiscardType(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.Energy(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.Supporter(), ct.Supporter), True)
        self.assertEqual(isinstance(ct.ArchiesAceintheHole(), ct.Supporter), True)
        self.assertEqual(isinstance(ct.Bicycle(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.BattleCompressor(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.Blastoise(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.ComputerTrainer(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.EscapeRope(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.Exeggcute(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.KeldeoEX(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.JirachiEX(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.Maintenance(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.N(), ct.Supporter), True)
        self.assertEqual(isinstance(ct.ProfessorJuniper(), ct.Supporter), True)
        self.assertEqual(isinstance(ct.Skyla(), ct.Supporter), True)
        self.assertEqual(isinstance(ct.Suicune(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.SuperiorEnergyRetriever(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.UltraBall(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.VSSeeker(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.WaterEnergy(), ct.Supporter), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)


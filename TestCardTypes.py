#!/usr/bin/python

import unittest
import CardTypes as ct

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

class TestCardTypes(unittest.TestCase):
    def test_isWaterType(self):
        self.assertEqual(ct.Card().isWaterType(), False)
        self.assertEqual(ct.BasicPokemon().isWaterType(), False)
        self.assertEqual(ct.DiscardType().isWaterType(), False)
        self.assertEqual(ct.BasicEnergy().isWaterType(), False)
        self.assertEqual(ct.Supporter().isWaterType(), False)
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().isWaterType(), False)
        self.assertEqual(Bicycle.Bicycle().isWaterType(), False)
        self.assertEqual(BattleCompressor.BattleCompressor().isWaterType(), False)
        self.assertEqual(Blastoise.Blastoise().isWaterType(), True)
        self.assertEqual(ComputerTrainer.ComputerTrainer().isWaterType(), False)
        self.assertEqual(DowsingMachine.DowsingMachine().isWaterType(), False)
        self.assertEqual(EscapeRope.EscapeRope().isWaterType(), False)
        self.assertEqual(Exeggcute.Exeggcute().isWaterType(), False)
        self.assertEqual(KeldeoEX.KeldeoEX().isWaterType(), True)
        self.assertEqual(JirachiEX.JirachiEX().isWaterType(), False)
        self.assertEqual(Maintenance.Maintenance().isWaterType(), False)
        self.assertEqual(N.N().isWaterType(), False)
        self.assertEqual(ProfessorJuniper.ProfessorJuniper().isWaterType(), False)
        self.assertEqual(RandomReceiver.RandomReceiver().isWaterType(), False)
        self.assertEqual(Skyla.Skyla().isWaterType(), False)
        self.assertEqual(Suicune.Suicune().isWaterType(), True)
        self.assertEqual(SuperiorEnergyRetriever.SuperiorEnergyRetriever().isWaterType(), False)
        self.assertEqual(UltraBall.UltraBall().isWaterType(), False)
        self.assertEqual(VSSeeker.VSSeeker().isWaterType(), False)
        self.assertEqual(WaterEnergy.WaterEnergy().isWaterType(), False)

    def test_name(self):
        self.assertEqual(ArchiesAceintheHole.ArchiesAceintheHole().name(), "Archie's Ace in the Hole")
        self.assertEqual(Bicycle.Bicycle().name(), "Bicycle")
        self.assertEqual(BattleCompressor.BattleCompressor().name(), "Battle Compressor")
        self.assertEqual(Blastoise.Blastoise().name(), "Blastoise")
        self.assertEqual(ComputerTrainer.ComputerTrainer().name(), "Computer Trainer")
        self.assertEqual(DowsingMachine.DowsingMachine().name(), "Dowsing Machine")
        self.assertEqual(EscapeRope.EscapeRope().name(), "Escape Rope")
        self.assertEqual(Exeggcute.Exeggcute().name(), "Exeggcute")
        self.assertEqual(JirachiEX.JirachiEX().name(), "Jirachi EX")
        self.assertEqual(KeldeoEX.KeldeoEX().name(), "Keldeo EX")
        self.assertEqual(Maintenance.Maintenance().name(), "Maintenance")
        self.assertEqual(N.N().name(), "N")
        self.assertEqual(ProfessorJuniper.ProfessorJuniper().name(), "Professor Juniper")
        self.assertEqual(RandomReceiver.RandomReceiver().name(), "Random Receiver")
        self.assertEqual(Skyla.Skyla().name(), "Skyla")
        self.assertEqual(Suicune.Suicune().name(), "Suicune")
        self.assertEqual(SuperiorEnergyRetriever.SuperiorEnergyRetriever().name(), "Superior Energy Retriever")
        self.assertEqual(UltraBall.UltraBall().name(), "Ultra Ball")
        self.assertEqual(VSSeeker.VSSeeker().name(), "VS Seeker")
        self.assertEqual(WaterEnergy.WaterEnergy().name(), "Water Energy")

    def test_hash(self):
        self.assertEqual(hash(KeldeoEX.KeldeoEX()), hash(KeldeoEX.KeldeoEX()))

    def test_eq(self):
        c1 = KeldeoEX.KeldeoEX()
        c2 = KeldeoEX.KeldeoEX()
        self.assertEqual(c1==c2, True)

    def test_isPokemon(self):
        self.assertEqual(isinstance(ct.Card(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.BasicPokemon(), ct.Pokemon), True)
        self.assertEqual(isinstance(ct.DiscardType(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.BasicEnergy(), ct.Pokemon), False)
        self.assertEqual(isinstance(ct.Supporter(), ct.Pokemon), False)
        self.assertEqual(isinstance(ArchiesAceintheHole.ArchiesAceintheHole(), ct.Pokemon), False)
        self.assertEqual(isinstance(Bicycle.Bicycle(), ct.Pokemon), False)
        self.assertEqual(isinstance(BattleCompressor.BattleCompressor(), ct.Pokemon), False)
        self.assertEqual(isinstance(Blastoise.Blastoise(), ct.Pokemon), True)
        self.assertEqual(isinstance(ComputerTrainer.ComputerTrainer(), ct.Pokemon), False)
        self.assertEqual(isinstance(EscapeRope.EscapeRope(), ct.Pokemon), False)
        self.assertEqual(isinstance(Exeggcute.Exeggcute(), ct.Pokemon), True)
        self.assertEqual(isinstance(KeldeoEX.KeldeoEX(), ct.Pokemon), True)
        self.assertEqual(isinstance(JirachiEX.JirachiEX(), ct.Pokemon), True)
        self.assertEqual(isinstance(Maintenance.Maintenance(), ct.Pokemon), False)
        self.assertEqual(isinstance(N.N(), ct.Pokemon), False)
        self.assertEqual(isinstance(ProfessorJuniper.ProfessorJuniper(), ct.Pokemon), False)
        self.assertEqual(isinstance(RandomReceiver.RandomReceiver(), ct.Pokemon), False)
        self.assertEqual(isinstance(Skyla.Skyla(), ct.Pokemon), False)
        self.assertEqual(isinstance(Suicune.Suicune(), ct.Pokemon), True)
        self.assertEqual(isinstance(SuperiorEnergyRetriever.SuperiorEnergyRetriever(), ct.Pokemon), False)
        self.assertEqual(isinstance(UltraBall.UltraBall(), ct.Pokemon), False)
        self.assertEqual(isinstance(VSSeeker.VSSeeker(), ct.Pokemon), False)
        self.assertEqual(isinstance(WaterEnergy.WaterEnergy(), ct.Pokemon), False)

    def test_isTrainer(self):
        self.assertEqual(isinstance(ct.Card(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.BasicPokemon(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.DiscardType(), ct.Trainer), True)
        self.assertEqual(isinstance(ct.BasicEnergy(), ct.Trainer), False)
        self.assertEqual(isinstance(ct.Supporter(), ct.Trainer), True)
        self.assertEqual(isinstance(ArchiesAceintheHole.ArchiesAceintheHole(), ct.Trainer), True)
        self.assertEqual(isinstance(Bicycle.Bicycle(), ct.Trainer), True)
        self.assertEqual(isinstance(BattleCompressor.BattleCompressor(), ct.Trainer), True)
        self.assertEqual(isinstance(Blastoise.Blastoise(), ct.Trainer), False)
        self.assertEqual(isinstance(ComputerTrainer.ComputerTrainer(), ct.Trainer), True)
        self.assertEqual(isinstance(EscapeRope.EscapeRope(), ct.Trainer), True)
        self.assertEqual(isinstance(Exeggcute.Exeggcute(), ct.Trainer), False)
        self.assertEqual(isinstance(KeldeoEX.KeldeoEX(), ct.Trainer), False)
        self.assertEqual(isinstance(JirachiEX.JirachiEX(), ct.Trainer), False)
        self.assertEqual(isinstance(Maintenance.Maintenance(), ct.Trainer), True)
        self.assertEqual(isinstance(N.N(), ct.Trainer), True)
        self.assertEqual(isinstance(ProfessorJuniper.ProfessorJuniper(), ct.Trainer), True)
        self.assertEqual(isinstance(RandomReceiver.RandomReceiver(), ct.Trainer), True)
        self.assertEqual(isinstance(Skyla.Skyla(), ct.Trainer), True)
        self.assertEqual(isinstance(Suicune.Suicune(), ct.Trainer), False)
        self.assertEqual(isinstance(SuperiorEnergyRetriever.SuperiorEnergyRetriever(), ct.Trainer), True)
        self.assertEqual(isinstance(UltraBall.UltraBall(), ct.Trainer), True)
        self.assertEqual(isinstance(VSSeeker.VSSeeker(), ct.Trainer), True)
        self.assertEqual(isinstance(WaterEnergy.WaterEnergy(), ct.Trainer), False)

    def test_isSupporter(self):
        self.assertEqual(isinstance(ct.Card(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.BasicPokemon(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.DiscardType(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.BasicEnergy(), ct.Supporter), False)
        self.assertEqual(isinstance(ct.Supporter(), ct.Supporter), True)
        self.assertEqual(isinstance(ArchiesAceintheHole.ArchiesAceintheHole(), ct.Supporter), True)
        self.assertEqual(isinstance(Bicycle.Bicycle(), ct.Supporter), False)
        self.assertEqual(isinstance(BattleCompressor.BattleCompressor(), ct.Supporter), False)
        self.assertEqual(isinstance(Blastoise.Blastoise(), ct.Supporter), False)
        self.assertEqual(isinstance(ComputerTrainer.ComputerTrainer(), ct.Supporter), False)
        self.assertEqual(isinstance(EscapeRope.EscapeRope(), ct.Supporter), False)
        self.assertEqual(isinstance(Exeggcute.Exeggcute(), ct.Supporter), False)
        self.assertEqual(isinstance(KeldeoEX.KeldeoEX(), ct.Supporter), False)
        self.assertEqual(isinstance(JirachiEX.JirachiEX(), ct.Supporter), False)
        self.assertEqual(isinstance(Maintenance.Maintenance(), ct.Supporter), False)
        self.assertEqual(isinstance(N.N(), ct.Supporter), True)
        self.assertEqual(isinstance(ProfessorJuniper.ProfessorJuniper(), ct.Supporter), True)
        self.assertEqual(isinstance(RandomReceiver.RandomReceiver(), ct.Supporter), False)
        self.assertEqual(isinstance(Skyla.Skyla(), ct.Supporter), True)
        self.assertEqual(isinstance(Suicune.Suicune(), ct.Supporter), False)
        self.assertEqual(isinstance(SuperiorEnergyRetriever.SuperiorEnergyRetriever(), ct.Supporter), False)
        self.assertEqual(isinstance(UltraBall.UltraBall(), ct.Supporter), False)
        self.assertEqual(isinstance(VSSeeker.VSSeeker(), ct.Supporter), False)
        self.assertEqual(isinstance(WaterEnergy.WaterEnergy(), ct.Supporter), False)


if __name__ == '__main__':
    unittest.main()


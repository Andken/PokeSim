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
import KyuremPLF
import KyuremLTR
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

def create(name):
    factory = { "Archie's Ace in the Hole"  : ArchiesAceintheHole.ArchiesAceintheHole(),
                "Battle Compressor"         : BattleCompressor.BattleCompressor(),
                "Bicycle"                   : Bicycle.Bicycle(),
                "Blastoise"                 : Blastoise.Blastoise(),
                "Computer Trainer"          : ComputerTrainer.ComputerTrainer(),
                "Dowsing Machine"           : DowsingMachine.DowsingMachine(),
                "Escape Rope"               : EscapeRope.EscapeRope(),
                "Exeggcute"                 : Exeggcute.Exeggcute(),
                "GrassEnergy"               : GrassEnergy.GrassEnergy(),
                "Jirachi EX"                : JirachiEX.JirachiEX(),
                "Keldeo EX"                 : KeldeoEX.KeldeoEX(),
                "Kyurem PLF"                : KyuremPLF.KyuremPLF(),
                "Kyurem LTR"                : KyuremLTR.KyuremLTR(),
                "Lysander's Trump Card"     : LysandersTrumpCard.LysandersTrumpCard(),
                "Maintenance"               : Maintenance.Maintenance(),
                "N"                         : N.N(),
                "Primal Kyogre EX"          : PrimalKyogreEX.PrimalKyogreEX(),
                "Professor Juniper"         : ProfessorJuniper.ProfessorJuniper(),
                "Random Receiver"           : RandomReceiver.RandomReceiver(),
                "Skyla"                     : Skyla.Skyla(),
                "Suicune"                   : Suicune.Suicune(),
                "Superior Energy Retriever" : SuperiorEnergyRetriever.SuperiorEnergyRetriever(),
                "Ultra Ball"                : UltraBall.UltraBall(),
                "VS Seeker"                 : VSSeeker.VSSeeker(),
                "Water Energy"              : WaterEnergy.WaterEnergy()
                }

    return factory[name]


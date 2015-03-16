import CardTypes as ct

def create(name):
    factory = { "Archie's Ace in the Hole"  : ct.ArchiesAceintheHole(),
                "Battle Compressor"         : ct.BattleCompressor(),
                "Bicycle"                   : ct.Bicycle(),
                "Blastoise"                 : ct.Blastoise(),
                "Computer Trainer"          : ct.ComputerTrainer(),
                "Dowsing Machine"           : ct.DowsingMachine(),
                "Escape Rope"               : ct.EscapeRope(),
                "Exeggcute"                 : ct.Exeggcute(),
                "GrassEnergy"               : ct.GrassEnergy(),
                "Jirachi EX"                : ct.JirachiEX(),
                "Keldeo EX"                 : ct.KeldeoEX(),
                "Kyurem PLF"                : ct.KyuremPLF(),
                "Kyurem LTR"                : ct.KyuremLTR(),
                "Lysander's Trump Card"     : ct.LysandersTrumpCard(),
                "Maintenance"               : ct.Maintenance(),
                "N"                         : ct.N(),
                "Primal Kyogre EX"          : ct.PrimalKyogreEX(),
                "Professor Juniper"         : ct.ProfessorJuniper(),
                "Random Receiver"           : ct.RandomReceiver(),
                "Skyla"                     : ct.Skyla(),
                "Suicune"                   : ct.Suicune(),
                "Superior Energy Retriever" : ct.SuperiorEnergyRetriever(),
                "Ultra Ball"                : ct.UltraBall(),
                "VS Seeker"                 : ct.VSSeeker(),
                "Water Energy"              : ct.WaterEnergy()
                }

    return factory[name]


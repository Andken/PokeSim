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
                "Keldeo EX"                 : ct.KeldeoEX(),
                "Maintenance"               : ct.Maintenance(),
                "N"                         : ct.N(),
                "Professor Juniper"         : ct.ProfessorJuniper(),
                "Skyla"                     : ct.Skyla(),
                "Suicune"                   : ct.Suicune(),
                "Superior Energy Retriever" : ct.SuperiorEnergyRetriever(),
                "Ultra Ball"                : ct.UltraBall(),
                "VS Seeker"                 : ct.VSSeeker(),
                "Water Energy"              : ct.WaterEnergy()
                }

    return factory[name]


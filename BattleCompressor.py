import CardTypes
from copy import deepcopy

import Blastoise
import Exeggcute
import ArchiesAceintheHole
import WaterEnergy

class BattleCompressor(CardTypes.Trainer):
    def name(self):
        return "Battle Compressor"

    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.discard.append(self)

        # this might need to be smarter (and only deal with small numbers of card in the deck
        num_discarded_cards = 0
        if Blastoise.Blastoise() in new_p.deck:
            new_p.deck.remove(Blastoise.Blastoise())
            new_p.discard.append(Blastoise.Blastoise())
            num_discarded_cards += 1
        if Exeggcute.Exeggcute() in new_p.deck:
            new_p.deck.remove(Exeggcute.Exeggcute())
            new_p.discard.append(Exeggcute.Exeggcute())
            num_discarded_cards += 1
        if ArchiesAceintheHole.ArchiesAceintheHole() in new_p.deck:
            new_p.deck.remove(ArchiesAceintheHole.ArchiesAceintheHole())
            new_p.discard.append(ArchiesAceintheHole.ArchiesAceintheHole())
            num_discarded_cards += 1
        while num_discarded_cards < 3 and WaterEnergy.WaterEnergy() in new_p.deck:
            new_p.deck.remove(WaterEnergy.WaterEnergy())
            new_p.discard.append(WaterEnergy.WaterEnergy())
            num_discarded_cards += 1            
        
        return set([new_p])

    def canPlay(self, p):
        return (self in p.hand) and (len(p.deck) >= 3)
    

import CardTypes
from copy import deepcopy

import ArchiesAceintheHole
import BattleCompressor
import Blastoise
import Exeggcute
import KeldeoEX
import Suicune
import UltraBall
import VSSeeker
import WaterEnergy


class ComputerTrainer(CardTypes.DiscardType):
    def name(self):
        return "Computer Trainer"

    def play(self, p):
        possible_states = set()

        discards = self.getDiscards(p.hand)

        for possibility in discards:
            assert len(possibility) > 0
            for card in set(p.deck):
                if card in [ArchiesAceintheHole.ArchiesAceintheHole(), 
                            BattleCompressor.BattleCompressor(),
                            Blastoise.Blastoise(),
                            Exeggcute.Exeggcute(),
                            KeldeoEX.KeldeoEX(),
                            Suicune.Suicune(),
                            UltraBall.UltraBall(),
                            VSSeeker.VSSeeker(),
                            WaterEnergy.WaterEnergy()]:
                    new_p = deepcopy(p)
                    new_p.hand.remove(self)
                    new_p.discard.append(self)
                    new_p.hand.remove(possibility[0])
                    new_p.discard.append(possibility[0])
                    new_p.hand.remove(possibility[1])
                    new_p.discard.append(possibility[1])
                    new_p.deck.remove(card)
                    new_p.hand.append(card)
                    possible_states.add(new_p)

        assert len(possible_states) > 0
        return possible_states


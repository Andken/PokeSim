import CardTypes
from copy import deepcopy
import itertools

class SuperiorEnergyRetriever(CardTypes.DiscardType):
    def play(self, p):
        assert "not implemented: " + self.name()

    def canPlay(self, p):
        for card in p.discard:
            if isinstance(card, CardTypes.BasicEnergy):
                return self in p.hand and len(p.hand) - 1 >= 2 
        return False

    def play(self, p):
        possible_states = set()
        discards = self.getDiscards(p.hand)

        for possibility in discards:

            assert len(possibility) > 0

            energies_in_discard = list()
            for card in p.discard:
                if isinstance(card, CardTypes.BasicEnergy):
                    energies_in_discard.append(deepcopy(card))

            assert len(energies_in_discard) > 0
            
            number_of_energies = min(4, len(energies_in_discard))

            energies = set()
            for energies_combo in itertools.combinations(energies_in_discard, 
                                                         number_of_energies):
                energies.add(tuple(sorted(energies_combo)))

            for energies_combo in energies:
                new_p = deepcopy(p)
                new_p.hand.remove(self)
                new_p.discard.append(self)
                new_p.hand.remove(possibility[0])
                new_p.discard.append(possibility[0])
                new_p.hand.remove(possibility[1])
                new_p.discard.append(possibility[1])

                for card in energies_combo:
                    new_p.discard.remove(card)
                    new_p.hand.append(card)

                possible_states.add(new_p)

        return possible_states

    def name(self):
        return "Superior Energy Retriever"


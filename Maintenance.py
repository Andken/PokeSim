import CardTypes
from copy import deepcopy
from random import shuffle

class Maintenance(CardTypes.DiscardType):
    def name(self):
        return "Maintenance"

    def canPlay(self, p):
        return self in p.hand and len(p.hand) - 1 >= 2 and p.nondeterministic

    def play(self, p):
        possible_states = set()

        discards = self.getDiscards(p.hand)

        for possibility in discards:
            assert len(possibility) > 0
            new_p = deepcopy(p)
            new_p.hand.remove(self)
            new_p.discard.append(self)
            new_p.hand.remove(possibility[0])
            new_p.deck.append(possibility[0])
            new_p.hand.remove(possibility[1])
            new_p.deck.append(possibility[1])
            shuffle(new_p.deck)
            new_p.draw(1)
            possible_states.add(new_p)

        assert len(possible_states) > 0
        return possible_states
        


import CardTypes
from copy import deepcopy

class ArchiesAceintheHole(CardTypes.Supporter):
    def play(self, p):
        possible_states = set()
        for card in p.discard:
            if card.isWaterType():
                new_p = deepcopy(p)
                new_p.hand.remove(self)
                new_p.discard.append(self)
                new_p.discard.remove(card)
                new_p.bench.append(card)
                new_p.draw(5)
                possible_states.add(new_p)

        return possible_states

    def name(self):
        return "Archie's Ace in the Hole"

    def canPlay(self, p):
        for card in p.discard:
            if card.isWaterType() and len(p.hand) == 1 and len(p.bench) < 5 and len(p.deck) >= 5:
                return True
        return False


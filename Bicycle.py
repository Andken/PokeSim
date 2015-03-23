import CardTypes
from copy import deepcopy

class Bicycle(CardTypes.Trainer):
    def name(self):
        return "Bicycle"

    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.discard.append(self)
        new_p.draw(4-len(new_p.hand))
        return set([new_p])

    def canPlay(self, p):
        return len(p.hand) < 5 and (len(p.hand) + len(p.deck)) > 4 and self in p.hand and p.nondeterministic


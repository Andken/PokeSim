import CardTypes
from copy import deepcopy

class RandomReceiver(CardTypes.Trainer):
    def name(self):
        return "Random Receiver"

    def canPlay(self, p):
        return self in p.hand and len(p.deck) > 0 and p.nondeterministic

    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.discard.append(self)
        for card in p.deck:
            if isinstance(card, CardTypes.Supporter):
                new_p.deck.remove(card)
                new_p.hand.append(card)
                break

        return set([new_p])


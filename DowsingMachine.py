import CardTypes
from copy import deepcopy

class DowsingMachine(CardTypes.DiscardType):
    def name(self):
        return "Dowsing Machine"

    def canPlay(self, p):
        # -1 because of the Discard Type already in the hand
        for card in p.discard:
            if isinstance(card, CardTypes.Trainer):
                return ((len(p.hand)-1) >= 2)
        return False

    def play(self, p):
        possible_states = set()

        discards = self.getDiscards(p.hand)

        for possibility in discards:
            assert len(possibility) > 0
            for card in set(p.discard):
                if isinstance(card, CardTypes.Trainer):
                    new_p = deepcopy(p)
                    new_p.hand.remove(self)
                    new_p.discard.append(self)
                    new_p.hand.remove(possibility[0])
                    new_p.discard.append(possibility[0])
                    new_p.hand.remove(possibility[1])
                    new_p.discard.append(possibility[1])
                    new_p.discard.remove(card)
                    new_p.hand.append(card)
                    possible_states.add(new_p)

        assert len(possible_states) > 0
        return possible_states


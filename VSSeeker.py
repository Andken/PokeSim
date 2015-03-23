import CardTypes
from copy import deepcopy

class VSSeeker(CardTypes.Trainer):
    def name(self):
        return "VS Seeker"

    def play(self, p):
        possible_states = list()

        for card in p.discard:
            if isinstance(card, CardTypes.Supporter):
                new_p = deepcopy(p)
                new_p.discard.append(self)
                new_p.hand.remove(self)
                new_p.hand.append(card)
                new_p.discard.remove(card)
                possible_states.append(new_p)

        return possible_states

    def canPlay(self, p):
        for card in p.discard:
            if isinstance(card, CardTypes.Supporter):
                return True
        return False    


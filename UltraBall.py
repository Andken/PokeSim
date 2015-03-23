import CardTypes
from copy import deepcopy

class UltraBall(CardTypes.DiscardType):
    def name(self):
        return "Ultra Ball"

    def play(self, p):
        possible_states = list()
        discards = self.getDiscards(p.hand)

        for possibility in discards:
            assert len(possibility) > 0

            new_p = deepcopy(p)
            new_p.hand.remove(self)
            new_p.discard.append(self)
            new_p.hand.remove(possibility[0])
            new_p.discard.append(possibility[0])
            new_p.hand.remove(possibility[1])
            new_p.discard.append(possibility[1])

            # copy this one as it's legal to grab nothing
            possible_states.append(new_p)

            for card_to_get in new_p.deck:
                if isinstance(card_to_get, CardTypes.Pokemon):
                    new_p2 = deepcopy(new_p)
                    new_p2.deck.remove(card_to_get)
                    new_p2.hand.append(card_to_get)
                    possible_states.append(new_p2)

        assert len(possible_states) > 0
        return possible_states


import CardTypes
from copy import deepcopy

class JirachiEX(CardTypes.BasicPokemon):
    def name(self):
        return "Jirachi EX"

    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.bench.append(self)

        possible_states = set()
        possible_states.add(new_p)

        for card in set(new_p.deck):
            if isinstance(card, CardTypes.Supporter):
                new_p_w_supporter = deepcopy(new_p)
                new_p_w_supporter.deck.remove(card)
                new_p_w_supporter.hand.append(card)
                possible_states.add(new_p_w_supporter)

        return possible_states


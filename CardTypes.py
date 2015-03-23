from copy import deepcopy
import itertools
from random import shuffle

#base
class Card:
    def name(self):
        raise "Not implemented"

    def __hash__(self):
        return hash(self.name())

    def __lt__(self, other):
        return self.name() < other.name()

    def __eq__(self, other):
        return self.name() == other.name()

    def play(self):
        assert "play: " + self.name()

    def canPlay(self, p):
        return False

    def isWaterType(self):
        return False

#types of cards
class Pokemon(Card):
    def play(self):
        assert "play: " + self.name()

class Trainer(Card):
    def play(self):
        assert "play: " + self.name()

class BasicPokemon(Pokemon):
    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.bench.append(self)
        return set([new_p])

    def canPlay(self, p):
        return (len(p.bench)) < 5 and (self in p.hand)

class DiscardType(Trainer):
    def play(self):
        assert "play: " + self.name()

    def getDiscards(self, hand):
        new_hand = deepcopy(hand)
        new_hand.remove(self)
        discards = set()
        for discard in itertools.combinations(new_hand, 2):
            discards.add(tuple(sorted(discard)))
        return discards
        
    def canPlay(self, p):
        # -1 because of the Discard Type already in the hand
        return ((len(p.hand)-1) >= 2) and (len(p.deck) >= 1)

class BasicEnergy(Card):
    def play(self, p):
        # do more than just remove it
        new_p = deepcopy(p)
        new_p.attached_energy = True
        new_p.hand.remove(self)
        return set([new_p])

    def canPlay(self, p):
        return self in p.hand and not p.attached_energy

class Supporter(Trainer):
    def play(self):
        assert "play: " + self.name()



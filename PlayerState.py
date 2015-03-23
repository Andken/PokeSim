import CardTypes as ct
from copy import deepcopy
import Exeggcute

class PlayerState:
    def __init__(self, hand=None, 
                 deck=None, 
                 prizes=None, 
                 bench=None, 
                 discard=None, 
                 attached_energy=False,
                 nondeterministic=False):
        if hand is None:
            self.hand = list()
        else:
            self.hand = hand

        if deck is None:
            self.deck = list()
        else:
            self.deck = deck

        if prizes is None:
            self.prizes = list()
        else:
            self.prizes = prizes

        if bench is None:
            self.bench = list()
        else:
            self.bench = bench

        if discard is None:
            self.discard = list()
        else:
            self.discard = discard

        self.attached_energy = attached_energy
        self.nondeterministic = nondeterministic

    def __hash__(self):
        return hash(self.tuplize())

    def __eq__(self, other):
        return self.tuplize() == other.tuplize()

    def __lt__(self, other):
        return self.tuplize() < other.tuplize()

    def tuplize(self):
        return (tuple(sorted(self.hand)),
                tuple(sorted(self.deck)),
                tuple(sorted(self.prizes)),
                tuple(sorted(self.bench)),
                tuple(sorted(self.discard)),
                self.attached_energy,
                self.nondeterministic)

    def draw(self, number_to_draw):
        for i in range(0,number_to_draw):
            self.hand.append(self.deck[0])
            self.deck.remove(self.deck[0])

    def startingHand(self):
        for card in self.hand:
            if isinstance(card, ct.BasicPokemon):
                return True
        return False
            
    def placeActive(self):
        potential = list()
        for card in self.hand:
            if isinstance(card, ct.BasicPokemon):
                potential.append(card)

        assert len(potential) >= 1

        potential_wo_Exeggcute = deepcopy(potential)
        for card in potential_wo_Exeggcute:
            if card == Exeggcute.Exeggcute():
                potential_wo_Exeggcute.remove(card)

        if len(potential_wo_Exeggcute) > 0:
            self.hand.remove(potential_wo_Exeggcute[0])
            self.bench.append(potential_wo_Exeggcute[0])
        else:
            self.hand.remove(Exeggcute.Exeggcute())
            self.bench.append(Exeggcute.Exeggcute())
        
                    
    def setPrizes(self, number_of_prizes):
        for i in range(0,number_of_prizes):
            self.prizes.append(self.deck[0])
            self.deck.remove(self.deck[0])
        
    def disaster(self, card):
        return (card not in self.hand) and (card not in self.deck)

    def printer(self):
        print "hand:"
        for card in self.hand:
            print "\t" + card.name()

        print "deck:"
        for card in self.deck:
            print "\t" + card.name()

        print "prizes:"
        for card in self.prizes:
            print "\t" + card.name()

        print "bench: (attached energy: " + str(self.attached_energy) + ")"
        for card in self.bench:
            print "\t" + card.name()

        print "discard:"
        for card in self.discard:
            print "\t" + card.name()


import CardTypes as ct

class PlayerState:
    def __init__(self, hand=None, deck=None, prizes=None, bench=None, discard=None):
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
                tuple(sorted(self.discard)))

    def draw(self, number_to_draw):
        for i in range(0,number_to_draw):
            hand.append(deepcopy(self.deck[0]))
            del self.deck[0]

    def setPrizes(self, number_of_prizes):
        for i in range(0,number_to_draw):
            prizes.append(deepcopy(self.deck[0]))
            del self.deck[0]
        
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

        print "bench:"
        for card in self.bench:
            print "\t" + card.name()

        print "discard:"
        for card in self.discard:
            print "\t" + card.name()


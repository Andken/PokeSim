from copy import deepcopy
import itertools

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

    def play(self, p):
        return [p]

    def canPlay(self, p):
        return False

    def isWaterType(self):
        return False

#types of cards
class Pokemon(Card):
    pass


class BasicPokemon(Pokemon):
    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.bench.append(self)
        return [new_p]

    def canPlay(self, p):
        return (len(p.bench)) < 5 and (self in p.hand)

class DiscardType(Card):
    def play(self, p):
        return [p]

    def getDiscards(self, hand):
        new_hand = deepcopy(hand)
        new_hand.remove(self)
        return itertools.combinations(new_hand, 2)

    def canPlay(self, p):
        # -1 because of the Discard Type already in the hand
        return ((len(p.hand)-1) >= 2) and (len(p.deck) >= 1)

class Energy(Card):
    def play(self, p):
        # do more than just remove it
        new_p = deepcopy(p)
        new_p.attached_energy = True
        new_p.hand.remove(self)
        return [new_p]

    def canPlay(self, p):
        return self in p.hand and not p.attached_energy

class Supporter(Card):
    pass

# concrete cards
class ArchiesAceintheHole(Supporter):
    def name(self):
        return "Archie's Ace in the Hole"

    def canPlay(self, p):
        for card in p.discard:
            if card.isWaterType():
                return len(p.hand) == 1
        return False

class Bicycle(Card):
    def name(self):
        return "Bicycle"

    def play(self, p):
        assert "not implemented"
        return [p]

    def canPlay(self, p):
        return False

class BattleCompressor(Card):
    def name(self):
        return "Battle Compressor"

    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.discard.append(self)

        # this might need to be smarter (and only deal with small numbers of card in the deck
        num_discarded_cards = 0
        if Blastoise() in new_p.deck:
            new_p.deck.remove(Blastoise())
            new_p.discard.append(Blastoise())
            num_discarded_cards += 1
        if Exeggcute() in new_p.deck:
            new_p.deck.remove(Exeggcute())
            new_p.discard.append(Exeggcute())
            num_discarded_cards += 1
        if ArchiesAceintheHole() in new_p.deck:
            new_p.deck.remove(ArchiesAceintheHole())
            new_p.discard.append(ArchiesAceintheHole())
            num_discarded_cards += 1
        while num_discarded_cards < 3 and WaterEnergy() in new_p.deck:
            new_p.deck.remove(WaterEnergy())
            new_p.discard.append(WaterEnergy())
            num_discarded_cards += 1            
        
        return [new_p]

    def canPlay(self, p):
        return (self in p.hand) and (len(p.deck) >= 1)
    
class Blastoise(Pokemon):
    def name(self):
        return "Blastoise"

    def isWaterType(self):
        return True

class ComputerTrainer(DiscardType):
    def name(self):
        return "Computer Trainer"

    def play(self, p):
        possible_states = set()

        discards = self.getDiscards(p.hand)

        for possibility in discards:
            assert len(possibility) > 0
            for card_to_get in p.deck:
                if card_to_get in [ArchiesAceintheHole(), 
                                   BattleCompressor(),
                                   Blastoise(),
                                   Exeggcute(),
                                   KeldeoEX(),
                                   Suicune(),
                                   UltraBall(),
                                   VSSeeker(),
                                   WaterEnergy()]:
                    new_p = deepcopy(p)
                    new_p.hand.remove(self)
                    new_p.discard.append(self)
                    new_p.hand.remove(possibility[0])
                    new_p.discard.append(possibility[0])
                    new_p.hand.remove(possibility[1])
                    new_p.discard.append(possibility[1])
                    new_p.deck.remove(card_to_get)
                    new_p.hand.append(card_to_get)
                    possible_states.add(new_p)

        assert len(possible_states) > 0
        return possible_states

class EscapeRope(Card):
    def name(self):
        return "Escape Rope"

class Exeggcute(BasicPokemon):
    def name(self):
        return "Exeggcute"

class KeldeoEX(BasicPokemon):
    def name(self):
        return "Keldeo EX"

    def isWaterType(self):
        return True

class Maintenance(Card):
    def name(self):
        return "Maintenance"

class N(Supporter):
    def name(self):
        return "N"

class ProfessorJuniper(Supporter):
    def name(self):
        return "Professor Juniper"

class Skyla(Supporter):
    def name(self):
        return "Skyla"

class Suicune(BasicPokemon):
    def name(self):
        return "Suicune"

    def isWaterType(self):
        return True

class SuperiorEnergyRetriever(Card):
    def name(self):
        return "Superior Energy Retriever"

class UltraBall(DiscardType):
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
                if isinstance(card_to_get, Pokemon):
                    new_p2 = deepcopy(new_p)
                    new_p2.deck.remove(card_to_get)
                    new_p2.hand.append(card_to_get)
                    possible_states.append(new_p2)

        assert len(possible_states) > 0
        return possible_states

class VSSeeker(Card):
    def name(self):
        return "VS Seeker"

    def play(self, p):
        possible_states = list()

        for card in p.discard:
            if isinstance(card, Supporter):
                new_p = deepcopy(p)
                new_p.discard.append(self)
                new_p.hand.remove(self)
                new_p.hand.append(card)
                new_p.discard.remove(card)
                possible_states.append(new_p)

        return possible_states

    def canPlay(self, p):
        for card in p.discard:
            if isinstance(card, Supporter):
                return True
        return False    

class WaterEnergy(Energy):
    def name(self):
        return "Water Energy"



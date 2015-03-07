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

class Energy(Card):
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

# concrete cards
class ArchiesAceintheHole(Supporter):
    def play(self, p):
        possible_states = set()
        for card in p.discard:
            if card.isWaterType():
                new_p = deepcopy(p)
                new_p.hand.remove(self)
                new_p.discard.append(self)
                new_p.discard.remove(card)
                new_p.bench.append(card)
                new_p.draw(5)
                possible_states.add(new_p)

        return possible_states

    def name(self):
        return "Archie's Ace in the Hole"

    def canPlay(self, p):
        for card in p.discard:
            if card.isWaterType() and len(p.hand) == 1 and len(p.bench) < 5 and len(p.deck) >= 5:
                return True
        return False

class Bicycle(Trainer):
    def name(self):
        return "Bicycle"

    def play(self, p):
        assert "not implemented"
        return set([p])

    def canPlay(self, p):
        return False

class BattleCompressor(Trainer):
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
        
        return set([new_p])

    def canPlay(self, p):
        return (self in p.hand) and (len(p.deck) >= 3)
    
class Blastoise(Pokemon):
    def play(self):
        assert "play: " + self.name()

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
            for card in set(p.deck):
                if card in [ArchiesAceintheHole(), 
                            BattleCompressor(),
                            Blastoise(),
                            ComputerTrainer(),
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
                    new_p.deck.remove(card)
                    new_p.hand.append(card)
                    possible_states.add(new_p)

        assert len(possible_states) > 0
        return possible_states

class DowsingMachine(DiscardType):
    def name(self):
        return "Dowsing Machine"

    def canPlay(self, p):
        # -1 because of the Discard Type already in the hand
        for card in p.discard:
            if isinstance(card, Trainer):
                return ((len(p.hand)-1) >= 2)
        return False

    def play(self, p):
        possible_states = set()

        discards = self.getDiscards(p.hand)

        for possibility in discards:
            assert len(possibility) > 0
            for card in set(p.discard):
                if card in [ArchiesAceintheHole(), 
                            BattleCompressor(),
                            Blastoise(),
                            ComputerTrainer(),
                            DowsingMachine(),
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
                    new_p.discard.remove(card)
                    new_p.hand.append(card)
                    possible_states.add(new_p)

        assert len(possible_states) > 0
        return possible_states

class EscapeRope(Trainer):
    def name(self):
        return "Escape Rope"

class Exeggcute(BasicPokemon):
    def name(self):
        return "Exeggcute"

class JirachiEX(BasicPokemon):
    def name(self):
        return "Jirachi EX"

    def play(self, p):
        new_p = deepcopy(p)
        new_p.hand.remove(self)
        new_p.bench.append(self)

        possible_states = set()
        possible_states.add(new_p)

        for card in set(new_p.deck):
            if isinstance(card, Supporter):
                new_p_w_supporter = deepcopy(new_p)
                new_p_w_supporter.deck.remove(card)
                new_p_w_supporter.hand.append(card)
                possible_states.add(new_p_w_supporter)

        return possible_states

class KeldeoEX(BasicPokemon):
    def name(self):
        return "Keldeo EX"

    def isWaterType(self):
        return True

class Maintenance(Trainer):
    def name(self):
        return "Maintenance"

class N(Supporter):
    def name(self):
        return "N"

class PrimalKyogreEX(Pokemon):
    def play(self):
        assert "play: " + self.name()

    def name(self):
        return "Primal Kyogre EX"

    def isWaterType(self):
        return True

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

class SuperiorEnergyRetriever(DiscardType):
    def play(self, p):
        assert "not implemented: " + self.name()

    def canPlay(self, p):
        return False

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

class VSSeeker(Trainer):
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



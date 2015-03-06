import DeckOperations as do
from copy import deepcopy

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
class BasicPokemon(Card):
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

    def getDiscards(hand):
        new_hand = deepcopy(hand)
        new_hand.remove(self)
        return itertools.combinations(new_hand, 2)

    def canPlay(self, p):
        # -1 because of the Dicard Type
        return ((len(p.hand)-1) >= 2) and (len(p.deck) >= 1)

class Energy(Card):
    def play(self, p):
        raise("not implemented")

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

    def play(self, hand, discard, bench, deck):
        return [(hand, discard, bench, deck)]

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
    
class Blastoise(Card):
    def name(self):
        return "Blastoise"

    def isWaterType(self):
        return True

class ComputerTrainer(DiscardType):
    def name(self):
        return "Computer Trainer"

    def play(self, p):
        possible_states = list()

        discards = getDiscards(hand, discard, deck, bench)

        for possibility in discards:
            for new_card_name in ["Archie's Ace in the Hole",
                                  "Battle Compressor",
                                  "Blastoise",
                                  "Exeggcute",
                                  "Keldeo EX",
                                  "VS Seeker"]:
                        new_hand_after_card_added = deepcopy(possibility[0])
                        new_deck = deepcopy(possibility[2])
                        if(do.ContainsName(new_deck, new_card_name)):
                            new_card = do.GetCard(new_deck, new_card_name)
                            do.MoveCard(new_deck, new_hand_after_card_added, new_card)
                        else:
                            # we always have enough water energy
                            new_hand_after_card_added.append(("Water Energy","0","Energy"))

                        possible_states.append(new_hand_after_card_added,
                                               possiblity[1],
                                               new_deck,
                                               possibility[3])

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

    def play(self, hand, discard, deck, bench):
        possible_states = list()

        discards = getDiscards(hand, discard, deck, bench)

        for possibility in discards:
            for new_card_name in ["Blastoise",
                                  "Exeggcute",
                                  "Keldeo EX",
                                  "NOTHING"]:
                        new_hand_after_card_added = deepcopy(possibility[0])
                        new_deck = deepcopy(possibility[2])
                        if(do.ContainsName(new_deck, new_card_name)):
                            new_card = do.GetCard(new_deck, new_card_name)
                            do.MoveCard(new_deck, new_hand_after_card_added, new_card)
                        else:
                            # we always have enough water energy
                            new_hand_after_card_added.append(("Water Energy","0","Energy"))

                        possible_states.append(new_hand_after_card_added,
                                               possiblity[1],
                                               new_deck,
                                               possibility[3])
        return possible_states

class VSSeeker(Card):
    def name(self):
        return "VS Seeker"

    def play(self, hand, discard, deck, bench):
        possible_states = list()

        for card in discard:
            if isinstance(card, Supporter):
                new_hand = deepcopy(hand)
                new_discard = deepcopy(discard)
                do.MoveCard(new_discard, new_hand, card)
                possible_states.append((new_hand, new_discard, deck, bench))

        return possible_states

    def canPlay(self, hand, discard, deck, bench):
        for card in discard:
            if isinstance(card, Supporter):
                return True
        return False    

class WaterEnergy(Energy):
    def name(self):
        return "Water Energy"



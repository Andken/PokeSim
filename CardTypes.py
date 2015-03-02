import DeckOperations as do

class Card:
    def play(self, hand, discard, bench, deck):
        return [(hand, discard, bench, deck)]

    def canPlay(self, hand, discard, bench, deck):
        return False

class Supporter(Card):
    pass

class Energy(Card):
    def play(self, hand, discard, bench, deck):
        new_hand = deepcopy(hand)
        new_bench = deepcopy(bench)
        do.MoveCard(new_hand, new_bench, card)
        return [(new_hand, discard, new_bench, deck)]

    def canPlay(self, hand, discard, bench, deck):
        return not do.ContainsType(bench, "Energy")

class WaterEnergy(Energy):
    pass

class BasicPokemon(Card):
    def play(self, hand, discard, bench, deck):
        new_hand = deepcopy(hand)
        new_bench = deepcopy(bench)
        do.MoveCard(new_hand, new_bench, card)
        return [(new_hand, discard, deck, new_bench)]

    def canPlay(self, hand, discard, bench, deck):
        return len(bench) < 5

class EvolvedPokemon(Card):
    pass

class ItemAnytime(Card):
    def play(self, hand, discard, bench, deck):
        new_hand = deepcopy(hand)
        new_discard = deepcopy(discard)
        new_deck = deepcopy(deck)
        do.MoveCard(new_hand, new_discard, card)
        return [(new_hand, new_discard, bench, deck)]

    def canPlay(self, hand, discard, bench, deck):
        return True

class BattleCompressor(ItemAnytime):
    def play(self, hand, discard, bench, deck):
        new_hand = deepcopy(hand)
        new_discard = deepcopy(discard)
        new_deck = deepcopy(deck)
        do.MoveCard(new_hand, new_discard, card)

        added_cards = 0;
        if (do.ContainsName(new_deck, "Archie's Ace in the Hole")):
            aaith = do.GetCard(new_deck, "Archie's Ace in the Hole")
            do.MoveCard(new_deck, new_discard, aaith)
            added_cards = added_cards + 1
        if (do.ContainsName(new_deck, "Blastoise")):
            blastoise = do.GetCard(new_deck, "Blastoise")
            do.MoveCard(new_deck, new_discard, blastoise)
            added_cards = added_cards + 1
        if (do.ContainsName(new_deck, "Exeggcute")):
            exeggcute = do.GetCard(new_deck, "Exeggcute")
            do.MoveCard(new_deck, new_discard, exeggcute)
            added_cards = added_cards + 1
        for i in range(added_cards, 3):
            new_discard.append(("Water Energy","0","Energy"))
        
        return [(new_hand, new_discard, new_deck, bench)]

# Work here!
class DiscardType(Card):
    def play(self, hand, discard, deck, bench):
        return [(hand, discard, deck, bench)]

    def getDiscards(hand, discard, deck, bench):
        new_hand = deepcopy(hand)
        new_discard = deepcopy(discard)
        do.MoveCard(new_hand, new_discard, card)

        possible_discards = list()
        for subset in itertools.combinations(new_hand, 2):
            new_hand_post_play = deepcopy(new_hand)
            new_discard_post_play = deepcopy(new_discard)
            do.MoveCard(new_hand_post_play, new_discard_post_play, subset[0])
            do.MoveCard(new_hand_post_play, new_discard_post_play, subset[1])
            possible_discards.append((new_hand_post_play, new_discard_post_play, deck, bench))

        return possible_discards

    def canPlay(self, hand, discard, deck, bench):
        return (len(hand)-1) >= 2

class ComputerTrainer(DiscardType):
    def play(self, hand, discard, deck, bench):
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

class UltraBall(DiscardType):
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



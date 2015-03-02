import DeckOperations as do
import itertools
import copy

def BlastoiseFirstTurn(hand, discard, deck, memoization):
    if(len(hand) == 0):
        return False

    if(len(hand) == 1):
        if do.ContainsName(hand, "Archie's Ace in the Hole"):
            return do.ContainsName(discard, "Blastoise")
        if do.ContainsName(hand, "VS Seeker"):
            return (do.ContainsName(discard, "Archie's Ace in the Hole") and do.ContainsName(discard, "Blastoise"))

    # play each card in turn
    for card in hand:
        if(card[2] == "Supporter" or card[2] == "Evolve"):
            continue
        if(card[2] == "Item-Anytime"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            do.PlayCard(new_hand, new_discard, card)
            if(BlastoiseFirstTurn(new_hand, new_discard, deck, memoization)):
                return True
            else:
                continue
        if(card[2] == "Item-UnrestrictedDiscard"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            do.PlayCard(new_hand, new_discard, card)
            if(len(hand) < 2):
                return False
            for subset in itertools.combinations(new_hand, 2):
                new_hand_post_play = copy.deepcopy(new_hand)
                new_discard_post_play = copy.deepcopy(new_discard)
                do.PlayCard(new_hand_post_play, new_discard_post_play, subset[0])
                do.PlayCard(new_hand_post_play, new_discard_post_play, subset[1])
                if(BlastoiseFirstTurn(new_hand_post_play, new_discard_post_play, deck, memoization)):
                    return True
                       
    return False

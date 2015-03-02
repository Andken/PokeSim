import DeckOperations as do
import itertools
import copy

def BlastoiseFirstTurn(hand, discard, deck, memoization):
    hand.sort()
    if(tuple(hand) in memoization):
        return memoization[tuple(hand)]

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
        elif(card[2] == "Item-Anytime"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            do.PlayCard(new_hand, new_discard, card)
            new_hand.sort()
            if(BlastoiseFirstTurn(new_hand, new_discard, deck, memoization)):
                memoization[tuple(new_hand)] = True
                return True
            else:
                memoization[tuple(new_hand)] = False
                continue
        elif(card[2] == "Item-UnrestrictedDiscard"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            do.PlayCard(new_hand, new_discard, card)
            if(len(hand) < 2):
                memoization[tuple(new_hand)] = False
                return False
            for subset in itertools.combinations(new_hand, 2):
                new_hand_post_play = copy.deepcopy(new_hand)
                new_discard_post_play = copy.deepcopy(new_discard)
                do.PlayCard(new_hand_post_play, new_discard_post_play, subset[0])
                do.PlayCard(new_hand_post_play, new_discard_post_play, subset[1])
                new_hand_post_play.sort()
                if(BlastoiseFirstTurn(new_hand_post_play, new_discard_post_play, deck, memoization)):
                    memoization[tuple(new_hand_post_play)] = True
                    return True
                else:
                    memoization[tuple(new_hand_post_play)] = False
                    
    memoization[tuple(hand)] = False
    return False

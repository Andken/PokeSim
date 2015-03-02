import DeckOperations as do
import itertools
import copy

def GetHashableHand(hand, energy_attached):
    return tuple([tuple(hand), energy_attached])

def AlreadyCalculated(hand, energy_attached, memoization):
    return GetHashableHand(hand, energy_attached) in memoization

def PreviousCalculation(hand, energy_attached, memoization):
    return memoization[GetHashableHand(hand, energy_attached)]

def SetCalculation(hand, energy_attached, value, memoization):
    memoization[GetHashableHand(hand, energy_attached)] = value

def BlastoiseFirstTurn(hand, discard, deck, bench, energy_attached, memoization):
    hand.sort()
    if(AlreadyCalculated(hand, energy_attached, memoization)):
        return PreviousCalculation(hand, energy_attached, memoization)
    
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
            if(BlastoiseFirstTurn(new_hand, new_discard, deck, bench, energy_attached, memoization)):
                SetCalculation(new_hand, energy_attached, True, memoization)
                return True
            else:
                SetCalculation(new_hand, energy_attached, False, memoization)
                continue
        elif(card[2] == "Energy"):
            new_hand = copy.deepcopy(hand)
            new_bench = copy.deepcopy(bench)
            do.PlayCard(new_hand, new_bench, card)
            new_hand.sort()
            if(energy_attached):
                continue
            else:
                if(BlastoiseFirstTurn(new_hand, discard, deck, new_bench, True, memoization)):
                    SetCalculation(new_hand, energy_attached, True, memoization)
                    return True
                else:
                    SetCalculation(new_hand, energy_attached, False, memoization)
                    continue
        elif(card[2] == "Item-UnrestrictedDiscard"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            do.PlayCard(new_hand, new_discard, card)
            if(len(hand) < 2):
                SetCalculation(new_hand, energy_attached, False, memoization)
                return False
            for subset in itertools.combinations(new_hand, 2):
                new_hand_post_play = copy.deepcopy(new_hand)
                new_discard_post_play = copy.deepcopy(new_discard)
                do.PlayCard(new_hand_post_play, new_discard_post_play, subset[0])
                do.PlayCard(new_hand_post_play, new_discard_post_play, subset[1])
                new_hand_post_play.sort()
                if(BlastoiseFirstTurn(new_hand_post_play, new_discard_post_play, deck, bench, energy_attached, memoization)):
                    SetCalculation(new_hand_post_play, energy_attached, True, memoization)
                    return True
                else:
                    SetCalculation(new_hand_post_play, energy_attached, False, memoization)
                    
    SetCalculation(hand, energy_attached, False, memoization)
    return False

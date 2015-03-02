def GetHashableHand(hand, discard, deck, bench, energy_attached):
    sorted_hand = sorted(hand)
    sorted_deck = sorted(deck)
    sorted_discard = sorted(discard)
    sorted_bench = sorted(bench)
    return tuple([tuple(sorted_hand), tuple(sorted_deck), tuple(sorted_discard), tuple(sorted_bench), energy_attached])

def AlreadyCalculated(hand, discard, deck, bench, energy_attached, memoization):
    return GetHashableHand(hand, discard, deck, bench, energy_attached) in memoization

def PreviousCalculation(hand, discard, deck, bench, energy_attached, memoization):
    return memoization[GetHashableHand(hand, discard, deck, bench, energy_attached)]

def SetCalculation(hand, discard, deck, bench, energy_attached, value, memoization):
    memoization[GetHashableHand(hand, discard, deck, bench, energy_attached)] = value


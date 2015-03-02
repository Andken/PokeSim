def GetHashableHand(hand, discard, deck, bench):
    sorted_hand = sorted(hand)
    sorted_deck = sorted(deck)
    sorted_discard = sorted(discard)
    sorted_bench = sorted(bench)
    return tuple([tuple(sorted_hand), tuple(sorted_deck), tuple(sorted_discard), tuple(sorted_bench)])

def AlreadyCalculated(hand, discard, deck, bench, memoization):
    return GetHashableHand(hand, discard, deck, bench) in memoization

def PreviousCalculation(hand, discard, deck, bench, memoization):
    return memoization[GetHashableHand(hand, discard, deck, bench)]

def SetCalculation(hand, discard, deck, bench, value, memoization):
    memoization[GetHashableHand(hand, discard, deck, bench)] = value


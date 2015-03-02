def GetHashableHand(hand, energy_attached):
    sorted_hand = sorted(hand)
    return tuple([tuple(sorted_hand), energy_attached])

def AlreadyCalculated(hand, energy_attached, memoization):
    return GetHashableHand(hand, energy_attached) in memoization

def PreviousCalculation(hand, energy_attached, memoization):
    return memoization[GetHashableHand(hand, energy_attached)]

def SetCalculation(hand, energy_attached, value, memoization):
    memoization[GetHashableHand(hand, energy_attached)] = value


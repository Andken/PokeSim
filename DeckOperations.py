def ContainsType(cards, type):
    for card in cards:
        if(card[2] == type):
            return True
    return False

def PlayBasic(hand, bench):
    basic = next(card for card in hand if card[2] == "Basic")
    bench.append(basic)
    hand.remove(basic)

def DrawCard(hand, deck):
    hand.append(deck[0])
    del deck[0]

def PrintCards(label, cards):
    print label
    for card in cards:
        print card[0]

def ContainsName(cards, name):
    for card in cards:
        if(card[0] == name):
            return True
    return False

def BlastioseFirstTurn(hand, discard, deck):
    if(len(hand) == 1):
        return ContainsName(hand, "Archie's Ace in the Hole") and ContainsName(discard, "Blastoise")
    return False


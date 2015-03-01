import DeckOperations as do

def BlastioseFirstTurn(hand, discard, deck):
    if(len(hand) == 1):
        if do.ContainsName(hand, "Archie's Ace in the Hole"):
            return do.ContainsName(discard, "Blastoise")
        if do.ContainsName(hand, "VS Seeker"):
            return (do.ContainsName(discard, "Archie's Ace in the Hole") and do.ContainsName(discard, "Blastoise"))

    # play each card in turn
    for card in hand:
        if(card[2] == "Supporter"):
            continue
        if(card[2] == "Item-Anytime"):
            new_hand = hand
            new_hand.remove(card)
            new_discard = discard
            new_discard.append(card)
            return BlastioseFirstTurn(new_hand, new_discard, deck)

    return False

import DeckOperations as do
import itertools
import copy
import HandHash as hh

def BlastoiseFirstTurn(hand, discard, deck, bench, energy_attached, memoization):
    print "============"
    do.PrintCards("hand==", hand)
    do.PrintCards("discard==", discard)
    do.PrintCards("deck==", deck)
    do.PrintCards("bench==", bench)

    if(hh.AlreadyCalculated(hand, energy_attached, memoization)):
        return hh.PreviousCalculation(hand, energy_attached, memoization)
    
    if(len(hand) == 0):
        return False

    if(len(hand) == 1):
        if do.ContainsName(hand, "Archie's Ace in the Hole"):
            return do.ContainsName(discard, "Blastoise")
        if do.ContainsName(hand, "VS Seeker"):
            return (do.ContainsName(discard, "Archie's Ace in the Hole") and do.ContainsName(discard, "Blastoise"))

    if(do.ContainsName(discard, "Exeggcute")):
        exeggcute = do.GetCard(discard, "Exeggcute")
        new_hand = copy.deepcopy(hand)
        new_discard = copy.deepcopy(discard)
        do.MoveCard(new_discard, new_hand, exeggcute)
        if(BlastoiseFirstTurn(new_hand, new_discard, deck, bench, energy_attached, memoization)):
            hh.SetCalculation(new_hand, energy_attached, True, memoization)
            return True
        else:
            hh.SetCalculation(new_hand, energy_attached, False, memoization)
        
    # play each card in turn
    for card in hand:
        if(card[2] == "Supporter" or card[2] == "Evolve"):
            continue
        elif(card[2] == "Item-Anytime"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            new_deck = copy.deepcopy(deck)
            do.MoveCard(new_hand, new_discard, card)
            # special types of Item-Anytime
            if(card[0] == "Battle Compressor"):
                added_cards = 0
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
                
            if(BlastoiseFirstTurn(new_hand, new_discard, new_deck, bench, energy_attached, memoization)):
                hh.SetCalculation(new_hand, energy_attached, True, memoization)
                return True
            else:
                hh.SetCalculation(new_hand, energy_attached, False, memoization)
                continue
        elif(card[2] == "Basic"):
            if(len(bench) >= 5):
                continue
            new_hand = copy.deepcopy(hand)
            new_bench = copy.deepcopy(bench)
            do.MoveCard(new_hand, new_bench, card)
            if(BlastoiseFirstTurn(new_hand, discard, deck, new_bench, energy_attached, memoization)):
                hh.SetCalculation(new_hand, energy_attached, True, memoization)
                return True
            else:
                hh.SetCalculation(new_hand, energy_attached, False, memoization)
                continue
        elif(card[2] == "Energy"):
            if(energy_attached):
                continue
            else:
                new_hand = copy.deepcopy(hand)
                new_bench = copy.deepcopy(bench)
                do.MoveCard(new_hand, new_bench, card)
                if(BlastoiseFirstTurn(new_hand, discard, deck, new_bench, True, memoization)):
                    hh.SetCalculation(new_hand, energy_attached, True, memoization)
                    return True
                else:
                    hh.SetCalculation(new_hand, energy_attached, False, memoization)
                    continue
        elif(card[2] == "Item-UnrestrictedDiscard"):
            new_hand = copy.deepcopy(hand)
            new_discard = copy.deepcopy(discard)
            do.MoveCard(new_hand, new_discard, card)
            if(len(hand) < 2):                
                continue
            for subset in itertools.combinations(new_hand, 2):
                new_hand_post_play = copy.deepcopy(new_hand)
                new_discard_post_play = copy.deepcopy(new_discard)
                do.MoveCard(new_hand_post_play, new_discard_post_play, subset[0])
                do.MoveCard(new_hand_post_play, new_discard_post_play, subset[1])

                # special types of Item-UnrestrictedDiscard
                if(card[0] == "Computer Trainer"):
                    for new_card_name in ["Archie's Ace in the Hole", 
                                          "Battle Compressor",
                                          "Blastoise",
                                          "Exeggcute",
                                          "Keldeo EX",
                                          "VS Seeker"]:
                        new_hand_after_card_added = copy.deepcopy(new_hand_post_play)
                        new_deck = copy.deepcopy(deck)
                        if(do.ContainsName(new_deck, new_card_name)):
                            new_card = do.GetCard(new_deck, new_card_name)
                            do.MoveCard(new_deck, new_hand_after_card_added, new_card)
                        else:
                            # we always have enough water energy
                            new_hand_after_card_added.append(("Water Energy","0","Energy"))

                        if(BlastoiseFirstTurn(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck, 
                                              bench, energy_attached, memoization)):
                            hh.SetCalculation(new_hand_after_card_added, 
                                              energy_attached, True, memoization)
                            return True
                        else:
                            hh.SetCalculation(new_hand_after_card_added, energy_attached, 
                                              False, memoization)

                else:
                    if(BlastoiseFirstTurn(new_hand_post_play, new_discard_post_play, deck, bench, energy_attached, memoization)):
                        hh.SetCalculation(new_hand_post_play, energy_attached, True, memoization)
                        return True
                    else:
                        hh.SetCalculation(new_hand_post_play, energy_attached, False, memoization)
                    
    hh.SetCalculation(hand, energy_attached, False, memoization)
    return False

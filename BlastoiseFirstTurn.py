import itertools
from copy import deepcopy

def BlastoiseFirstTurn(p, memoization):
    return True
#    print "============"
#    do.PrintCards("hand==", hand)
#    do.PrintCards("discard==", discard)
#    do.PrintCards("deck==", deck)
#    do.PrintCards("bench==", bench)

    if(hh.AlreadyCalculated(hand, discard, deck, bench, memoization)):
        return hh.PreviousCalculation(hand, discard, deck, bench, memoization)
    
    if(len(hand) == 0):
        return False

    if(len(hand) == 1):
        if do.ContainsName(hand, "Archie's Ace in the Hole"):
            return do.ContainsName(discard, "Blastoise")
        if do.ContainsName(hand, "VS Seeker"):
            return (do.ContainsName(discard, "Archie's Ace in the Hole") and do.ContainsName(discard, "Blastoise"))

    if(do.ContainsName(discard, "Exeggcute")):
        exeggcute = do.GetCard(discard, "Exeggcute")
        new_hand = deepcopy(hand)
        new_discard = deepcopy(discard)
        do.MoveCard(new_discard, new_hand, exeggcute)
        if(BlastoiseFirstTurn(new_hand, new_discard, deck, bench, memoization)):
            hh.SetCalculation(new_hand, new_discard, deck, bench, True, memoization)
            return True
        else:
            hh.SetCalculation(new_hand, new_discard, deck, bench, False, memoization)
        
    # play each card in turn
    for card in hand:
        if(card[2] == "Supporter" or card[2] == "Evolve"):
            continue
        elif(card[2] == "Item-Anytime"):
            new_hand = deepcopy(hand)
            new_discard = deepcopy(discard)
            new_deck = deepcopy(deck)
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
                
            if(BlastoiseFirstTurn(new_hand, new_discard, new_deck, bench, memoization)):
                hh.SetCalculation(new_hand, new_discard, new_deck, bench, True, memoization)
                return True
            else:
                hh.SetCalculation(new_hand, new_discard, new_deck, bench, False, memoization)
                continue
        elif(card[2] == "Basic"):
            if(len(bench) >= 5):
                continue
            new_hand = deepcopy(hand)
            new_bench = deepcopy(bench)
            do.MoveCard(new_hand, new_bench, card)
            if(BlastoiseFirstTurn(new_hand, discard, deck, new_bench, memoization)):
                hh.SetCalculation(new_hand, discard, deck, new_bench, True, memoization)
                return True
            else:
                hh.SetCalculation(new_hand, discard, deck, new_bench, False, memoization)
                continue
        elif(card[2] == "Energy"):
            if(do.ContainsName(bench, "Water Energy")):
                continue
            else:
                new_hand = deepcopy(hand)
                new_bench = deepcopy(bench)
                do.MoveCard(new_hand, new_bench, card)
                if(BlastoiseFirstTurn(new_hand, discard, deck, new_bench, memoization)):
                    hh.SetCalculation(new_hand, discard, deck, new_bench, True, memoization)
                    return True
                else:
                    hh.SetCalculation(new_hand, discard, deck, new_bench, False, memoization)
                    continue
        elif(card[2] == "Item-UnrestrictedDiscard"):
            new_hand = deepcopy(hand)
            new_discard = deepcopy(discard)
            do.MoveCard(new_hand, new_discard, card)
            if(len(hand) < 2):                
                continue
            for subset in itertools.combinations(new_hand, 2):
                new_hand_post_play = deepcopy(new_hand)
                new_discard_post_play = deepcopy(new_discard)
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
                        new_hand_after_card_added = deepcopy(new_hand_post_play)
                        new_deck = deepcopy(deck)
                        if(do.ContainsName(new_deck, new_card_name)):
                            new_card = do.GetCard(new_deck, new_card_name)
                            do.MoveCard(new_deck, new_hand_after_card_added, new_card)
                        else:
                            # we always have enough water energy
                            new_hand_after_card_added.append(("Water Energy","0","Energy"))

                        if(BlastoiseFirstTurn(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck, 
                                              bench, memoization)):
                            hh.SetCalculation(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck, 
                                              bench, True, memoization)
                            return True
                        else:
                            hh.SetCalculation(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck,
                                              bench, False, memoization)
                elif(card[0] == "Ultra Ball"):
                    for new_card_name in ["Blastoise",
                                          "Exeggcute",
                                          "Keldeo EX",
                                          "NOTHING"]:
                        new_hand_after_card_added = deepcopy(new_hand_post_play)
                        new_deck = deepcopy(deck)
                        if(do.ContainsName(new_deck, new_card_name)):
                            new_card = do.GetCard(new_deck, new_card_name)
                            do.MoveCard(new_deck, new_hand_after_card_added, new_card)
                        # else do nothing

                        if(BlastoiseFirstTurn(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck, 
                                              bench, memoization)):
                            hh.SetCalculation(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck, 
                                              bench, True, memoization)
                            return True
                        else:
                            hh.SetCalculation(new_hand_after_card_added, 
                                              new_discard_post_play, new_deck,
                                              bench, False, memoization)

                else:
                    if(BlastoiseFirstTurn(new_hand_post_play, new_discard_post_play, deck, 
                                          bench, memoization)):
                        hh.SetCalculation(new_hand_post_play, new_discard_post_play, deck, 
                                          bench, True, memoization)
                        return True
                    else:
                        hh.SetCalculation(new_hand_post_play, new_discard_post_play, deck, 
                                          bench, False, memoization)
                    
    hh.SetCalculation(hand, discard, deck, bench, False, memoization)
    return False

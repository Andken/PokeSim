import DeckOperations as do
import itertools
import copy
import HandHash as hh

def BlastoiseFirstTurn(hand, discard, deck, bench, energy_attached, memoization):
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
            do.MoveCard(new_hand, new_discard, card)
            if(BlastoiseFirstTurn(new_hand, new_discard, deck, bench, energy_attached, memoization)):
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
                if(BlastoiseFirstTurn(new_hand_post_play, new_discard_post_play, deck, bench, energy_attached, memoization)):
                    hh.SetCalculation(new_hand_post_play, energy_attached, True, memoization)
                    return True
                else:
                    hh.SetCalculation(new_hand_post_play, energy_attached, False, memoization)
                    
    hh.SetCalculation(hand, energy_attached, False, memoization)
    return False

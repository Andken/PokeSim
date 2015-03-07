import itertools
from copy import deepcopy
import CardTypes as c

def BlastoiseFirstTurn(p, memoization):
    if(len(p.hand) == 0):
        return False

    if(len(p.hand) == 1):
        return c.ArchiesAceintheHole() in p.hand and c.Blastoise() in p.discard

    if(c.Exeggcute() in p.discard):
        new_p = deepcopy(p)
        new_p.discard.remove(c.Exeggcute())
        new_p.hand.append(c.Exeggcute())
        if(BlastoiseFirstTurn(new_p, memoization)):
            memoization[new_p] = True
            return True
        else:
            memoization[new_p] = False
        
    # play each card in turn
    for card in p.hand:
        if(card.canPlay(p)):
            possibilities = card.play(p)
            
            for possibility in possibilities:
                if(BlastoiseFirstTurn(possibility, memoization)):
                    memoization[possibility] = True
                    return True
                else:
                    memoization[possibility] = False
                       
    memoization[p] = False
    return False

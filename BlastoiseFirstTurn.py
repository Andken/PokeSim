import itertools
from copy import deepcopy

import Blastoise
import Exeggcute

def BlastoiseFirstTurn(p, memoization):
    if p in memoization:
        return memoization[p]

    if Blastoise.Blastoise() in p.bench:
        memoization[p] = True
        return True

    if Exeggcute.Exeggcute() in p.discard:
        new_p = deepcopy(p)
        new_p.discard.remove(Exeggcute.Exeggcute())
        new_p.hand.append(Exeggcute.Exeggcute())
        if(BlastoiseFirstTurn(new_p, memoization)):
            memoization[new_p] = True
            return True
        else:
            memoization[new_p] = False
        
    # play each card in turn
    for card in p.hand:
        if card.canPlay(p):
            possibilities = card.play(p)

            for possibility in possibilities:
                if(BlastoiseFirstTurn(possibility, memoization)):
                    memoization[possibility] = True
                    return True
                else:
                    memoization[possibility] = False
                       
    memoization[p] = False
    return False

#!/usr/bin/python

import sys
from random import shuffle
from PlayerState import PlayerState
import BlastoiseFirstTurn as bft
from copy import deepcopy
import CardFactory as cf
import CardTypes as c

gold_deck = list()
mulligans_by_number = {}
mulligans_by_number[0] = 0
disasters = 0
successes = 0
memoized = {}

sims = int(sys.argv[1])
filename = sys.argv[2]

with open('WaterDeck.txt', 'r+') as f:
    contents = f.readlines()
    for card in contents:
        gold_deck.append(cf.create(card.rstrip()))


for sim_number in range(0,sims):
    print str(sim_number) + ":" + str(sims) + "::" + str(successes)
    p = PlayerState()

    mulligans = 0

    while not p.startingHand():
        p.deck = deepcopy(gold_deck)

        shuffle(p.deck)

        p.hand = list()
        p.draw(7)

        mulligans = mulligans + int(not p.startingHand())

    if(mulligans in mulligans_by_number):
        mulligans_by_number[mulligans] = mulligans_by_number[mulligans] + 1
    else:
        mulligans_by_number[mulligans] = 1

    # prize cards
    p.setPrizes(6)

    disaster = p.disaster(c.Blastoise()) or p.disaster(c.ArchiesAceintheHole())

    p.placeActive()

    disaster = disaster or c.Exeggcute() in p.bench
    disasters = disasters + int(disaster)
    
    p.draw(1)

    if not disaster:
        successes = successes + int(bft.BlastoiseFirstTurn(p, memoized))

print "================================="
print "===Sims:      " + str(sims)
print "===Successes: " + str(successes) + "(" + str(100.0*successes/sims) + "%)"
print "===Disasters: " + str(disasters) + "(" + str(100.0*disasters/sims) + "%)"
print "===Mulligans: "
for key in sorted(mulligans_by_number.iterkeys()):
    print "   " + str(key) + ": " + str(mulligans_by_number[key]) + "(" + str(100.0*mulligans_by_number[key]/sims) + "%)"













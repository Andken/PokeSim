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
bad_news = 0
bad_news_and_success = 0

sims = int(sys.argv[1])
filename = sys.argv[2]

with open(filename, 'r+') as f:
    contents = f.readlines()
    for card in contents:
        gold_deck.append(cf.create(card.rstrip()))


for sim_number in range(1,sims+1):
    print str(sim_number) + ":" + str(sims) + ":: successes: " + str(successes) + " (" + str(100.0*successes/sim_number) + "%) :: disasters: " + str(disasters) + " (" + str(100.0*disasters/sim_number) + "%) :: bad_news: " + str(bad_news) + " (" + str(100.0*bad_news/sim_number) + "%) :: bad_news * success: " + str(bad_news_and_success) + " (" + str(100.0*bad_news_and_success/sim_number) + "%)"

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

    is_bad_news = c.Exeggcute() in p.bench or c.JirachiEX() in p.bench
    bad_news += int(is_bad_news)
    disasters += int(disaster)
    
    p.draw(1)

    if not disaster:
        is_successful = bft.BlastoiseFirstTurn(p, memoized)
        successes += int(is_successful)
        bad_news_and_success += int(is_successful and is_bad_news)

    

print "================================="
print "=====: " + filename
print "===Sims:      " + str(sims)
print "===Successes: " + str(successes) + "(" + str(100.0*successes/sims) + "%)"
print "===Disasters: " + str(disasters) + "(" + str(100.0*disasters/sims) + "%)"
print "===Bad News: " + str(bad_news) + "(" + str(100.0*bad_news/sims) + "%)"
print "===Bad News * Success: " + str(bad_news_and_success) + "(" + str(100.0*bad_news_and_success/sims) + "%)"
print "===Mulligans: "
for key in sorted(mulligans_by_number.iterkeys()):
    print "   " + str(key) + ": " + str(mulligans_by_number[key]) + "(" + str(100.0*mulligans_by_number[key]/sims) + "%)"













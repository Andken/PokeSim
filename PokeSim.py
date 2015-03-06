#!/usr/bin/python

import csv
from random import shuffle
from PlayerState import PlayerState
import BlastoiseFirstTurn as bft
from copy import deepcopy
import CardFactory as cf

sims = 1

gold_deck = list()
mulligans_by_number = {}
mulligans_by_number[0] = 0
disasters = 0
successes = 0
memoized = {}

with open('WaterDeck.txt', 'r+') as f:
    contents = f.readlines()
    for card in contents:
        gold_deck.append(cf.create(card.rstrip()))


print gold_deck
raise "not yet"

for j in range(0,sims):
    print str(j) + ":" + str(sims) + "::" + str(successes)
    p = PlayerState()

    mulligans = 0
    playable_hand = False

    while not playable_hand:
        p.deck = deepcopy(gold_deck)

        shuffle(p.deck)
        p.printer()

        p.hand = list()
        for i in range(0,7):
            p.draw()

        playable_hand = c.BasicPokemon() in p.hand()

        mulligans = mulligans + int(not playable_hand)

    if(mulligans in mulligans_by_number):
        mulligans_by_number[mulligans] = mulligans_by_number[mulligans] + 1
    else:
        mulligans_by_number[mulligans] = 1

    print "mulligans = " + str(mulligans)
    p.printer()

    raise "not done yet"

#    # prize cards
#    prizes = list()
#    for i in range(0,6):
#        do.DrawCard(prizes, deck)
#
#    do.PrintCards("====Prizes===", prizes)
#    disaster = False
#    for card in prizes:
#        # each card has a value...if all card of that value are in the prizes, that's a disaster
#        deck_indices = [i for i, x in enumerate(gold_deck) if x[1] == card[1]]
#        prize_indices = [i for i, x in enumerate(prizes) if x[1] == card[1]]
#
#        disaster = disaster | (len(deck_indices) == len(prize_indices))
#
#    #print "====Disaster: " + str(disaster)
#    disasters = disasters + disaster
#
#    bench = []
#
#    # play a Basic and draw a card
#    if(do.ContainsType(hand, "Basic")):
#        do.PlayBasic(hand, bench)
#
#    do.DrawCard(hand, deck)
#
#    do.PrintCards("==========================New hand=", hand)
#    do.PrintCards("==========================Bench=", bench)
#    do.PrintCards("==========================Deck=", deck)
#
#    successes = successes + int(bft.BlastoiseFirstTurn(hand, discard, deck, bench, memoized))
#
#print "================================="
#print "===Sims:      " + str(sims)
#print "===Successes: " + str(successes) + "(" + str(100.0*successes/sims) + "%)"
#print "===Disasters: " + str(disasters) + "(" + str(100.0*disasters/sims) + "%)"
#print "===Mulligans: "
#for key in sorted(mulligans_by_number.iterkeys()):
#    print "   " + str(key) + ": " + str(mulligans_by_number[key]) + "(" + str(100.0*mulligans_by_number[key]/sims) + "%)"
#
#











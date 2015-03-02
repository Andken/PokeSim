#!/usr/bin/python

import csv
from random import shuffle
import DeckOperations as do
import BlastoiseFirstTurn as bft
from copy import deepcopy

sims = 1

gold_deck = list()
mulligans_by_number = {}
mulligans_by_number[0] = 0
disasters = 0
successes = 0
memoized = {}

with open('WaterDeck.csv', 'rb') as csvfile:
    cards = csv.reader(csvfile, delimiter=',')
    for card in cards:
        gold_deck.append(tuple(card))        


for j in range(0,sims):
    hand = list()
    discard = list()

    mulligans = 0
    playable_hand = False

    while not playable_hand:
        deck = deepcopy(gold_deck)

        shuffle(deck)
        do.PrintCards("============\n=== DECK ===\n============", deck)

        hand = list()
        for i in range(0,7):
            do.DrawCard(hand, deck)

        playable_hand = do.ContainsType(hand, "Basic")

        mulligans = mulligans + int(not playable_hand)

    if(mulligans in mulligans_by_number):
        mulligans_by_number[mulligans] = mulligans_by_number[mulligans] + 1
    else:
        mulligans_by_number[mulligans] = 1

    do.PrintCards("====Actual Hand====", hand)


    # prize cards
    prizes = list()
    for i in range(0,6):
        do.DrawCard(prizes, deck)

    do.PrintCards("====Prizes===", prizes)
    disaster = False
    for card in prizes:
        # each card has a value...if all card of that value are in the prizes, that's a disaster
        deck_indices = [i for i, x in enumerate(gold_deck) if x[1] == card[1]]
        prize_indices = [i for i, x in enumerate(prizes) if x[1] == card[1]]

        disaster = disaster | (len(deck_indices) == len(prize_indices))

    print "====Disaster: " + str(disaster)
    disasters = disasters + disaster

    bench = []

    # play a Basic and draw a card
    if(do.ContainsType(hand, "Basic")):
        do.PlayBasic(hand, bench)

    do.DrawCard(hand, deck)

    do.PrintCards("==========================New hand=", hand)
    do.PrintCards("==========================Bench=", bench)
    do.PrintCards("==========================Deck=", deck)

    successes = successes + int(bft.BlastoiseFirstTurn(hand, discard, deck, bench, memoized))

print "================================="
print "===Sims:      " + str(sims)
print "===Successes: " + str(successes) + "(" + str(100.0*successes/sims) + "%)"
print "===Disasters: " + str(disasters) + "(" + str(100.0*disasters/sims) + "%)"
print "===Mulligans: "
for key in sorted(mulligans_by_number.iterkeys()):
    print "   " + str(key) + ": " + str(mulligans_by_number[key]) + "(" + str(100.0*mulligans_by_number[key]/sims) + "%)"













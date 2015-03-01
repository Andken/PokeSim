#!/usr/bin/python

import csv
from random import shuffle

sims = 1

mulligans_by_number = {}
mulligans_by_number[0] = 0
disasters = 0

for j in range(0,sims):
    with open('WaterDeck.csv', 'rb') as csvfile:
        cards = csv.reader(csvfile, delimiter=',')
        deck = list()


        for card in cards:
            deck.append(card)        

        hand = list()
        mulligans = 0
        playable_hand = False

        while not playable_hand:
            print "========================"
            print "=========DECK==========="
            print "========================"
            shuffle(deck)
            for card in deck:
                print ', '.join(card)

            del hand[:]
            for i in range(0,7):
                hand.append(deck[i])

            print "=========Potential Hand:"
            for card in hand:
                print card[0]

                # the second number is whether it's a basic pokemon to see if a mulligan is needed
                playable_hand = playable_hand or (card[2] == "Basic")

            mulligans = mulligans + int(not playable_hand)
            print "======Playable Hand: " + str(playable_hand)


        if(mulligans in mulligans_by_number):
            mulligans_by_number[mulligans] = mulligans_by_number[mulligans] + 1
        else:
            mulligans_by_number[mulligans] = 1

        print "====Actual Hand==="
        for card in hand:
            print card[0]


        # prize cards
        prizes = list()
        for i in range(7,13):
            prizes.append(deck[i])

        print "====Prizes==="
        disaster = False
        for card in prizes:
            # each card has a value...if all card of that value are in the prizes, that's a disaster
            deck_indices = [i for i, x in enumerate(deck) if x[1] == card[1]]
            prize_indices = [i for i, x in enumerate(prizes) if x[1] == card[1]]

            # print "number of " + card[0] + ": " + str(len(deck_indices)) + " : " + str(len(prize_indices))
            disaster = disaster | (len(deck_indices) == len(prize_indices))

        print "====Disaster: " + str(disaster)
        disasters = disasters + disaster

        # play a Basic and draw a card
        basic = next(card for card in hand if card[2] == "Basic")
        bench = []
        bench.append(basic)
        hand.remove(basic)

        print "==========================New hand="
        for card in hand:
            print card[0]

        print "==========================Bench="
        for card in bench:
            print card[0]


print "================================="
print "===Sims:      " + str(sims)
print "===Disasters: " + str(disasters) + "(" + str(100.0*disasters/sims) + "%)"
print "===Mulligans: "
for key in sorted(mulligans_by_number.iterkeys()):
    print "   " + str(key) + ": " + str(mulligans_by_number[key]) + "(" + str(100.0*mulligans_by_number[key]/sims) + "%)"


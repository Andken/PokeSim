#!/usr/bin/python

import csv
from random import shuffle

with open('WaterDeck.csv', 'rb') as csvfile:
    cards = csv.reader(csvfile, delimiter=',')
    deck = list()


    print "=========DECK==========="
    for card in cards:
        deck.append(card)        

    hand = list()
    mulligans = 0
    playable_hand = False

    while not playable_hand:
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
            playable_hand = playable_hand or (card[2] == "1")

        mulligans = mulligans + playable_hand
        print "======Playable Hand: " + str(playable_hand)

    print "====Actual Hand==="
    for card in hand:
        print card[0]
    

    # prize cards
    prizes = list()
    for i in range(7,13):
        prizes.append(deck[i])

    

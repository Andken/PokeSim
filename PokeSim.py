#!/usr/bin/python

import csv
from random import shuffle

with open('WaterDeck.csv', 'rb') as csvfile:
    cards = csv.reader(csvfile, delimiter=',')
    deck = list()
    for card in cards:
        deck.append(card)        

    shuffle(deck)
    for card in deck:
        print ', '.join(card)

    hand = list()
    for i in range(0,7):
        hand.append(deck[i])

    print "========HAND==========="
    for card in hand:
        print ', '.join(card)
        
    # the second number is whether it's a basic pokemon to see if a mulligan is needed
    

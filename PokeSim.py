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



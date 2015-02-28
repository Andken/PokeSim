#!/usr/bin/python

import csv
with open('WaterDeck.csv', 'rb') as csvfile:
    card = csv.reader(csvfile, delimiter=',')
    for element in card:
        print ', '.join(element)

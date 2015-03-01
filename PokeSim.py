#!/usr/bin/python

import csv
from random import shuffle

def ContainsType(cards, type):
    for card in cards:
        if(card[2] == type):
            return True
    return False

def PlayBasic(hand, bench):
    basic = next(card for card in hand if card[2] == "Basic")
    bench.append(basic)
    hand.remove(basic)

def DrawCard(hand, deck):
    hand.append(deck[0])
    del deck[0]

def PrintCards(label, cards):
    print label
    for card in cards:
        print card[0]

def ContainsName(cards, name):
    for card in cards:
        if(card[0] == name):
            return True
    return False

def BlastioseFirstTurn(hand, discard, deck):
    if(len(hand) == 1):
        return ContainsName(hand, "Archie's Ace in the Hole") and ContainsName(discard, "Blastoise")
    return False

sims = 1

mulligans_by_number = {}
mulligans_by_number[0] = 0
disasters = 0

for j in range(0,sims):
    with open('WaterDeck.csv', 'rb') as csvfile:
        cards = csv.reader(csvfile, delimiter=',')
        deck = list()
        discard = list()

        hand = list()
        mulligans = 0
        playable_hand = False

        while not playable_hand:
            deck = list()
            for card in cards:
                deck.append(card)        

            #shuffle(deck)
            PrintCards("============\n=== DECK ===\n============", deck)
    
            for i in range(0,7):
                DrawCard(hand, deck)

            playable_hand = ContainsType(hand, "Basic")

            mulligans = mulligans + int(not playable_hand)

        if(mulligans in mulligans_by_number):
            mulligans_by_number[mulligans] = mulligans_by_number[mulligans] + 1
        else:
            mulligans_by_number[mulligans] = 1

        PrintCards("====Actual Hand====", hand)


        # prize cards
        prizes = list()
        for i in range(0,6):
            DrawCard(prizes, deck)

        PrintCards("====Prizes===", prizes)
        disaster = False
        for card in prizes:
            # each card has a value...if all card of that value are in the prizes, that's a disaster
            deck_indices = [i for i, x in enumerate(deck) if x[1] == card[1]]
            prize_indices = [i for i, x in enumerate(prizes) if x[1] == card[1]]

            disaster = disaster | (len(deck_indices) == len(prize_indices))

        print "====Disaster: " + str(disaster)
        disasters = disasters + disaster

        bench = []

        # play a Basic and draw a card
        if(ContainsType(hand, "Basic")):
            PlayBasic(hand, bench)

        DrawCard(hand, deck)

        PrintCards("==========================New hand=", hand)
        PrintCards("==========================Bench=", bench)
        PrintCards("==========================Deck=", deck)



print "================================="
print "===Sims:      " + str(sims)
print "===Disasters: " + str(disasters) + "(" + str(100.0*disasters/sims) + "%)"
print "===Mulligans: "
for key in sorted(mulligans_by_number.iterkeys()):
    print "   " + str(key) + ": " + str(mulligans_by_number[key]) + "(" + str(100.0*mulligans_by_number[key]/sims) + "%)"













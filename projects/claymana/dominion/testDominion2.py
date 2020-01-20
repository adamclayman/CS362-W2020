# -*- coding: utf-8 -*-
"""
Last modified on Thu January 16, 2020

Editor: Adam Clayman
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
player_count = len(player_names)
if player_count>2:
    nV=12
else:
    nV=8
nC = -10 + 5 * player_count

#Define box, supply order, supply, and trash
box = testUtility.GetBoxes(nV)
supply_order = testUtility.SupplyOrder()
supply = testUtility.PickSupply(box, nV, nC, player_count)
trash = []

#Costruct the Player objects
players = []
for name in player_names:
    if name[0]=="*":
        players.append(Dominion.ComputerPlayer(name[1:]))
    elif name[0]=="^":
        players.append(Dominion.TablePlayer(name[1:]))
    else:
        players.append(Dominion.Player(name))

#Play the game
turn  = 2   # Changed from turn = 0 for testDominion2.py scenario bug
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)

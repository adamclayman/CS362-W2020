# -*- coding: utf-8 -*-
"""
Last modified on Thu January 16, 2020

Editor: Adam Clayman
"""

#Get players
players = testUtility.GetPlayers()

#number of curses and victory cards
nV = testUtility.GetVictoryCards(players)
nC = testUtility.GetCurses(players)

#Define box, supply order, supply, and trash
box = testUtility.GetBoxes(nV)
supply_order = testUtility.GetSupplyOrder()
supply = testUtility.GetSupply(box, 10, players, nV, nC)
trash = []

#Play the game
turn  = 0
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

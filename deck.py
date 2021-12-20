#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[2]:


import random
import holdem_calc


# # Classes

# In[3]:


class card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print("{}{}".format(self.value, self.suit))
        
# ace_of_clubs = card("clubs", 1)
# ace_of_clubs.show()

class deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ["s", "c", "d", "h"]:
            for v in range(2, 10):
                self.cards.append(card(s, v))
                
        for s in ["s", "c", "d", "h"]:
            for v in ["T", "J", "Q", "K", "A"]:
                self.cards.append(card(s, v))
                
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        random.shuffle(self.cards)
            
    def drawCard(self):
        return self.cards.pop()
            
# deck1 = deck()
# deck1.shuffle()
# deck1.drawCard().show()
# deck1.show()

class player:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
        
    def showHand(self):
        print()
        print("------------------------------------")
        print("{}'s Cards".format(self.name))
        for card in self.hand:
            card.show()
        print("------------------------------------")
        print()
            


# # Create Players and Assign Hands

# In[7]:


deck1 = deck()
deck1.shuffle()
  
numPlayers = 2
# numPlayers = random.randint(1,6)

players = []

for i in range(numPlayers):
    players.append(player("player{}".format(i)))
    players[i].draw(deck1)
    players[i].draw(deck1)
#     players[i].showHand()
    
# print(listPlayers)
    
# player1 = player("clark")
# player1.draw(deck1)
# player1.draw(deck1)
# player2 = player("Tyler")
# player2.draw(deck1)
# player2.draw(deck1)
# player1.showHand()
# player2.showHand()
# players = [player1, player2]
# # deck1.show()
# # print(dir(player1.hand[0]))
# print("{}{}".format(players[0].hand[0].value, players[0].hand[0].suit))


# # Calculate probability Player1 wins

# In[13]:


handsList = []

def probability_win(players):
    for player in players:
        for i in range(len(player.hand)):
            handsList.append("{}{}".format(player.hand[i].value, player.hand[i].suit))
    
#     print(handsList)
    
    return holdem_calc.calculate(None, False, 10000, None, handsList, False)
    
# print(probability_win(players))


#!/usr/bin/env python
# coding: utf-8

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty

import random
import holdem_calc

class card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print("{}{}".format(self.value, self.suit))
        
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
        
deck1 = deck()
deck1.shuffle()
  
numPlayers = 2

players = []

for i in range(numPlayers):
    players.append(player("player{}".format(i)))
    players[i].draw(deck1)
    players[i].draw(deck1)
    
def probability_win(players):
    
    handsList = []
    
    for player in players:
        for i in range(len(player.hand)):
            handsList.append("{}{}".format(player.hand[i].value, player.hand[i].suit))
    
    print(handsList)
    
    return handsList, holdem_calc.calculate(None, False, 10000, None, handsList, False)
  
handsList, odds = probability_win(players)

class BoxLayoutExample(GridLayout):

	card1 = "./images/{}.png".format(handsList[0])
	card2 = "./images/{}.png".format(handsList[1])
	card3 = "./images/{}.png".format(handsList[2])
	card4 = "./images/{}.png".format(handsList[3])
	my_text = StringProperty("Your Cards")
	def on_button_click(self):
		self.my_text = "You clikced"

class thelabApp(App):
    pass


thelabApp().run()


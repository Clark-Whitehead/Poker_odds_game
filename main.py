#!/usr/bin/env python
# coding: utf-8

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ListProperty

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
   

    
    return handsList, holdem_calc.calculate(None, False, 10000, None, handsList, False)
  
handsList, odds = probability_win(players)

print(odds) 
print(odds[1]) 
print(handsList)

oddsMixed = []

for i in range(3):
    oddsMixed.append(random.randint(1,100))

oddsMixed.append(str(round(odds[1]*100)))

random.shuffle(oddsMixed)

class BoxLayoutExample(GridLayout):

	correctOdd = NumericProperty(int(round(odds[1]*100)))

	color1 = StringProperty("1,0,0,1")

	od1 = NumericProperty(oddsMixed[0])
	od2 = NumericProperty(oddsMixed[1])
	od3 = NumericProperty(oddsMixed[2])
	od4 = NumericProperty(oddsMixed[3])

	odd1 = StringProperty("{}%".format(oddsMixed[0]))
	odd2 = StringProperty("{}%".format(oddsMixed[1]))
	odd3 = StringProperty("{}%".format(oddsMixed[2]))
	odd4 = StringProperty("{}%".format(oddsMixed[3]))

	card1 = StringProperty("./images/{}.png".format(handsList[0]))
	card2 = StringProperty("./images/{}.png".format(handsList[1]))
	card3 = StringProperty("./images/{}.png".format(handsList[2]))
	card4 = StringProperty("./images/{}.png".format(handsList[3]))
	

	my_text = StringProperty("Your Cards")
    
	def probability_win(players):
    
		handsList = []
    
		for player in players:
			for i in range(len(player.hand)):
				handsList.append("{}{}".format(player.hand[i].value, player.hand[i].suit))
 

    
		return handsList, holdem_calc.calculate(None, False, 10000, None, handsList, False)
   
	def on_button_click(self):
		pass
 
	def option1(self):
		print(self.correctOdd)
		print(self.od1)
		if self.od1 == self.correctOdd:
			print("true")
		else:
			print("flase")

	def next(self):
		deck1 = deck()
		deck1.shuffle()
        
		numPlayers = 2

		players = []
        
		for i in range(numPlayers):
			players.append(player("player{}".format(i)))
			players[i].draw(deck1)
			players[i].draw(deck1)
            
		handsList, odds = probability_win(players)
       
		self.correctOdd = int(round(odds[1]*100)) 
 
		oddsMixed = []
        
		for i in range(3):
			oddsMixed.append(random.randint(1,100))

		oddsMixed.append(str(round(odds[1]*100)))

		random.shuffle(oddsMixed)
       
		print("odds mixed = {}".format(oddsMixed))
		print(handsList)
		print(odds[1])

		self.od1 = oddsMixed[0]
		self.od2 = oddsMixed[1]
		self.od3 = oddsMixed[2]
		self.od4 = oddsMixed[3]
 
		self.odd1 = "{}%".format(oddsMixed[0])
		self.odd2 = "{}%".format(oddsMixed[1])
		self.odd3 = "{}%".format(oddsMixed[2])
		self.odd4 = "{}%".format(oddsMixed[3])

		print("odd1 = {}".format(self.odd1))

		self.card1 = "./images/{}.png".format(handsList[0])
		self.card2 = "./images/{}.png".format(handsList[1])
		self.card3 = "./images/{}.png".format(handsList[2])
		self.card4 = "./images/{}.png".format(handsList[3])

class thelabApp(App):
    pass


thelabApp().run()


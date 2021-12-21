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
from kivy.properties import ReferenceListProperty
from kivy.graphics import Color

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

oddsTieMixed = []

for i in range(3):
    oddsTieMixed.append(random.randint(1,100))

oddsTieMixed.append(str(round(odds[0]*100)))

random.shuffle(oddsTieMixed)


class BoxLayoutExample(GridLayout):

	correctOdd = NumericProperty(int(round(odds[1]*100)))

	correctTieOdd = NumericProperty(int(round(odds[0]*100)))

	color1 = StringProperty("gray")	
	color2 = StringProperty("gray")
	color3 = StringProperty("gray")	
	color4 = StringProperty("gray")	

	colorTie1 = StringProperty("gray")	
	colorTie2 = StringProperty("gray")
	colorTie3 = StringProperty("gray")	
	colorTie4 = StringProperty("gray")	


	od1 = NumericProperty(oddsMixed[0])
	od2 = NumericProperty(oddsMixed[1])
	od3 = NumericProperty(oddsMixed[2])
	od4 = NumericProperty(oddsMixed[3])

	ti1 = NumericProperty(oddsTieMixed[0])
	ti2 = NumericProperty(oddsTieMixed[1])
	ti3 = NumericProperty(oddsTieMixed[2])
	ti4 = NumericProperty(oddsTieMixed[3]) 

	odd1 = StringProperty("{}%".format(oddsMixed[0]))
	odd2 = StringProperty("{}%".format(oddsMixed[1]))
	odd3 = StringProperty("{}%".format(oddsMixed[2]))
	odd4 = StringProperty("{}%".format(oddsMixed[3]))

	tie1 = StringProperty("{}%".format(oddsTieMixed[0]))
	tie2 = StringProperty("{}%".format(oddsTieMixed[1]))
	tie3 = StringProperty("{}%".format(oddsTieMixed[2]))
	tie4 = StringProperty("{}%".format(oddsTieMixed[3]))


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
		if int(self.od1) == int(self.correctOdd):
			self.color1 = "aqua"
		elif int(self.od2) == int(self.correctOdd):
			self.color2 = "aqua"
			self.color1 = "orange"
		elif int(self.od3) == int(self.correctOdd):
			self.color3 = "aqua"
			self.color1 = "orange"
		else:
			self.color4 = "aqua"
			self.color1 = "orange"

	def option2(self):
		if int(self.od2) == int(self.correctOdd):
			self.color2 = "aqua"
		elif int(self.od1) == int(self.correctOdd):
			self.color1 = "aqua"
			self.color2 = "orange"
		elif int(self.od3) == int(self.correctOdd):
			self.color3 = "aqua"
			self.color2 = "orange"
		else:
			self.color4 = "aqua"
			self.color2 = "orange"

	def option3(self):
		if int(self.od3) == int(self.correctOdd):
			self.color3 = "aqua"
		elif int(self.od1) == int(self.correctOdd):
			self.color1 = "aqua"
			self.color3 = "orange"
		elif int(self.od2) == int(self.correctOdd):
			self.color2 = "aqua"
			self.color3 = "orange"
		else:
			self.color4 = "aqua"
			self.color3 = "orange"

	def option4(self):
		if int(self.od4) == int(self.correctOdd):
			self.color4 = "aqua"
		elif int(self.od1) == int(self.correctOdd):
			self.color1 = "aqua"
			self.color4 = "orange"
		elif int(self.od2) == int(self.correctOdd):
			self.color2 = "aqua"
			self.color4 = "orange"
		else:
			self.color3 = "aqua"
			self.color4 = "orange"

	def optionTie1(self):
		if int(self.ti1) == int(self.correctTieOdd):
			self.colorTie1 = "aqua"
		elif int(self.ti2) == int(self.correctTieOdd):
			self.colorTie2 = "aqua"
			self.colorTie1 = "orange"
		elif int(self.ti3) == int(self.correctTieOdd):
			self.colorTie3 = "aqua"
			self.colorTie1 = "orange"
		else:
			self.colorTie4 = "aqua"
			self.colorTie1 = "orange"

	def optionTie2(self):
		if int(self.ti2) == int(self.correctTieOdd):
			self.colorTie2 = "aqua"
		elif int(self.ti1) == int(self.correctTieOdd):
			self.colorTie1 = "aqua"
			self.colorTie2 = "orange"
		elif int(self.ti3) == int(self.correctTieOdd):
			self.colorTie3 = "aqua"
			self.colorTie2 = "orange"
		else:
			self.colorTie4 = "aqua"
			self.colorTie2 = "orange"

	def optionTie3(self):
		if int(self.ti3) == int(self.correctTieOdd):
			self.colorTie3 = "aqua"
		elif int(self.ti1) == int(self.correctTieOdd):
			self.colorTie1 = "aqua"
			self.colorTie3 = "orange"
		elif int(self.ti2) == int(self.correctTieOdd):
			self.colorTie2 = "aqua"
			self.colorTie3 = "orange"
		else:
			self.colorTie4 = "aqua"
			self.colorTie3 = "orange"

	def optionTie4(self):
		if int(self.ti4) == int(self.correctTieOdd):
			self.colorTie4 = "aqua"
		elif int(self.ti1) == int(self.correctTieOdd):
			self.colorTie1 = "aqua"
			self.colorTie4 = "orange"
		elif int(self.ti2) == int(self.correctTieOdd):
			self.colorTie2 = "aqua"
			self.colorTie4 = "orange"
		else:
			self.colorTie3 = "aqua"
			self.colorTie4 = "orange"


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
 
		self.correctTieOdd = int(round(odds[0]*100))

		oddsMixed = []
        
		for i in range(3):
			oddsMixed.append(random.randint(1,100))

		oddsMixed.append(str(round(odds[1]*100)))

		random.shuffle(oddsMixed)
      
		oddsTieMixed = []

		for i in range(3):
		    oddsTieMixed.append(random.randint(1,100))

		oddsTieMixed.append(str(round(odds[0]*100)))

		random.shuffle(oddsTieMixed)

 
		print("odds mixed = {}".format(oddsMixed))
		print(handsList)
		print(odds[1])

		self.color1 = "gray"
		self.color2 = "gray"
		self.color3 = "gray"
		self.color4 = "gray"

		self.colorTie1 = "gray"
		self.colorTie2 = "gray"
		self.colorTie3 = "gray"
		self.colorTie4 = "gray"


		self.od1 = oddsMixed[0]
		self.od2 = oddsMixed[1]
		self.od3 = oddsMixed[2]
		self.od4 = oddsMixed[3]
 
		self.odd1 = "{}%".format(oddsMixed[0])
		self.odd2 = "{}%".format(oddsMixed[1])
		self.odd3 = "{}%".format(oddsMixed[2])
		self.odd4 = "{}%".format(oddsMixed[3])

		self.ti1 = oddsTieMixed[0]
		self.ti2 = oddsTieMixed[1]
		self.ti3 = oddsTieMixed[2]
		self.ti4 = oddsTieMixed[3]
 
		self.tie1 = "{}%".format(oddsTieMixed[0])
		self.tie2 = "{}%".format(oddsTieMixed[1])
		self.tie3 = "{}%".format(oddsTieMixed[2])
		self.tie4 = "{}%".format(oddsTieMixed[3])


		print("odd1 = {}".format(self.odd1))

		self.card1 = "./images/{}.png".format(handsList[0])
		self.card2 = "./images/{}.png".format(handsList[1])
		self.card3 = "./images/{}.png".format(handsList[2])
		self.card4 = "./images/{}.png".format(handsList[3])

class thelabApp(App):
    pass


thelabApp().run()


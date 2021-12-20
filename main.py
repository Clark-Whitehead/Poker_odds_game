#!/usr/bin/env python
# coding: utf-8

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty


class BoxLayoutExample(GridLayout):
	cards = "./images/3_of_clubs.png"
	my_text = StringProperty("Your Cards")
	def on_button_click(self):
		self.my_text = "You clikced"

class MainWidget(Widget):
    pass


class thelabApp(App):
    pass


thelabApp().run()


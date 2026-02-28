# Ref : youtube.com/watch?v=6gNpSuE01qE

import kivy
from  kivy.app import App # Imports the perant class of an app
from kivy.uix.label import Label # This is to import the lable element 
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('1.9.0')

class Myroot(BoxLayout):
    def __init__(self):
        super(Myroot,self).__init__()

    def RandomPress(self):
        self.random_label.text = str(random.randint(0, 10000))

class RandomNumber(App): # The kv file name has to be the classes name in lower case 
    def build(self):
        return Myroot()
    

randomapp = RandomNumber()
randomapp.run()

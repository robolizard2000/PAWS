# Ref : youtube.com/watch?v=6gNpSuE01qE

import kivy
from  kivy.app import App # Imports the perant class of an app
from kivy.uix.label import Label # This is to import the lable element 

kivy.require('2.3.1')

class RandomNumber(App):
    def build(self):
        return Label(text="RandomNumber")
    

random = RandomNumber()
random.run()

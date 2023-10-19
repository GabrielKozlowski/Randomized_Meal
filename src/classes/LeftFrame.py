from tkinter import *



class LeftFrame:

    def __init__(self):
        print('Helo from init')

  


    def create_left_label(self):    
        self.bottom_left = Frame(self, bg="#cf6f0e")
        self.bottom_left.grid()
        self.bottom_left.columnconfigure(0, minsize=350, weight=1)
        return self.bottom_left




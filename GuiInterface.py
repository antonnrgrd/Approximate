from tkinter import *

class UserMenu(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        #simply creates the top-level menu
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=Menu)

        

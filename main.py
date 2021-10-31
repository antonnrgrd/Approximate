import os
from tkinter import *
from GuiInterface import UserMenu
from menu_constants import *
from selection_handler import *
#from linear_algebra import *



def main():
    '''
    linear_algebra = MatrixOperators(generate_report = True, verbose = False)
    linear_algebra.matrix_mult(np.random.rand(10,10),np.random.rand(10,10))
    '''

    #As far as I can tell,
    root = Tk()
    #Adds title to the file menu
    root.wm_title("Approximate")
    
    ApproximateGreeting = Label(root, text = "Welcome to Approximate! To get started, simply select one of the tasks in one of the categories from their respective dropdown menu")
    ApproximateGreeting.place(relx= .5, rely= 0.145 ,anchor = "center")
   
    #As far as I can tell, there is no tactful way to add a lot of labels and this is the only way possible to do it i.e manually
    LinearAlgebraLabel = Label(root, text = "Linear algebra")
    NPCLabel = Label(root, text = "NPC problems")
    LinearProgrammingLabel = Label(root, text = "Linear Programming")
    DataScienceLabel = Label(root, text = "Data science")
    LinearAlgebraLabel.place(relx = 0.2, rely=.25)
    NPCLabel.place(relx = 0.4,rely=.25)
    LinearProgrammingLabel.place(relx = 0.6,rely=.25)
    DataScienceLabel.place(relx = 0.8,rely=.25)
    ########################################Create dropdown menus
    chosen_option = StringVar(root)
    chosen_option.set(nill_choice)
    linear_algebra_options = OptionMenu(root,chosen_option,*linear_algebra_choices)
    linear_algebra_options.place(relx=0.2, rely = .3)
    npc_options = OptionMenu(root,chosen_option,*npc_choices)
    npc_options.place(relx=0.4, rely = .3)
    
    #We specify the command to be executed to be a lambda, because otherwise it will execute automatically when the window is created
    ReadyButton = Button(root, text = "Continue", command= lambda: value_select_handler[chosen_option.get()]())
    ReadyButton.place(relx= .9, rely= 0.9)
    root.mainloop()
if __name__ == '__main__':
    main()

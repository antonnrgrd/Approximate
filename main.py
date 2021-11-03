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

    
    root = Tk()
    #Adds title to the file menu
    root.wm_title("Approximate")

    initial_frame = tkinter.ttk.Frame(root, width=root.winfo_screenwidth(), height = root.winfo_screenheight())
    initial_frame.grid()
    selected_frame = tkinter.ttk.Frame(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())    
    selected_frame['borderwidth'] = 2
    selected_frame['relief'] = 'sunken'
    selected_frame.grid(column = 0, row = 0, padx=20 ,pady= 5, sticky=(tkinter.W,tkinter.N,tkinter.E))
    init_selection_frame_info(selected_frame, initial_frame)
    selected_frame.grid_remove()
    
    ApproximateGreeting = Label(initial_frame, text = "Welcome to Approximate! To get started, simply select one of the tasks in one of the categories from their respective dropdown menu")
    ApproximateGreeting.place(relx= .5, rely= 0.145 ,anchor = "center")
   
    #As far as I can tell, there is no tactful way to add a lot of labels and this is the only way possible to do it i.e manually
    LinearAlgebraLabel = Label(initial_frame, text = "Linear algebra")
    NPCLabel = Label(initial_frame, text = "NPC problems")
    LinearProgrammingLabel = Label(initial_frame, text = "Linear Programming")
    DataScienceLabel = Label(initial_frame, text = "Data science")
    LinearAlgebraLabel.place(relx = 0.2, rely=.25)
    NPCLabel.place(relx = 0.4,rely=.25)
    LinearProgrammingLabel.place(relx = 0.6,rely=.25)
    DataScienceLabel.place(relx = 0.8,rely=.25)
    ########################################Create dropdown menus
    chosen_option = StringVar(initial_frame)
    chosen_option.set(nill_choice)
    linear_algebra_options = OptionMenu(initial_frame,chosen_option,*linear_algebra_choices)
    linear_algebra_options.place(relx=0.2, rely = .3)
    npc_options = OptionMenu(initial_frame,chosen_option,*npc_choices)
    npc_options.place(relx=0.4, rely = .3)
    
    #We specify the command to be executed to be a lambda, because otherwise it will execute automatically when the window is created
    ReadyButton = Button(initial_frame, text = "Continue", command= lambda: value_select_handler[chosen_option.get()](selected_frame, chosen_option.get(), initial_frame))
    ReadyButton.place(relx= .85, rely= 0.85)
    root.mainloop()
if __name__ == '__main__':
    main()

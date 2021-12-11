import tkinter
import tkinter.ttk
from distutils.spawn import find_executable
from menu_constants import *
#A generic frame initalizer that initalizes information that every window, regardless of the chosen problem will need to have.

def init_selection_frame_info(argframe, pframe, selection = ""):
    generate_report = BooleanVar
    verbose = BooleanVar
    frame = tkinter.ttk.Label(argframe,text = selection)
    report_label = Label(argframe, text = "Enter the name of the report:")
    generate_report_label = Label(argframe, text= "Generate a report of the result?")
    verbose_label = Label(argframe, text= "Make the report verbose?")
    run_button = Button(argframe, text="Run")
    back_button = Button(argframe, text = "Back", command = lambda: [argframe.grid_forget(), pframe.grid()])
    report_name_entry = Entry(argframe)
    select_report = Checkbutton(argframe, variable = generate_report,onvalue=True, offvalue = False)
    select_verbose = Checkbutton(argframe, variable = verbose,onvalue=True, offvalue = False)

    report_label.place(relx=.1, rely=.1)
    
    select_report.place(relx = .27, rely=.2)
    select_verbose.place(relx = .27, rely=.15)
    
    report_name_entry.place(relx=.25, rely=.1)
    
    back_button.place(relx=.08, rely=.85)
    run_button.place(relx= .85, rely= 0.85)

    generate_report_label.place(relx=0.1, rely=.15)
    verbose_label.place(relx=0.1, rely=.2)

'''Basically a class that encapsualtes the GUI interface that Approximate uses, because the increasing complexity meant that 
it no longer sufficed to use ad-hoc solution'''

class ChainedWindows(Frame):
    def __init__(self, root):
        
        '''Because latex might not be installed on the pc in question, we need to check if it is, in order to enable/disable 
        generating reports'''
        if find_executable('latex'):
            self.tex_enabled = True
        else:
            self.tex_enabled = False
        self.value_select_handler = {nill_choice : "err_no_value_chosen_msg"}
        self.root = root
        self.initial_frame = tkinter.ttk.Frame(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())    
        self.initial_frame.grid()
        self.selected_frame = tkinter.ttk.Frame(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())    
        self.selected_frame['borderwidth'] = 2
        self.selected_frame['relief'] = 'sunken'
        self.selected_frame.grid(column = 0, row = 0, padx=20 ,pady= 5, sticky=(tkinter.W,tkinter.N,tkinter.E))
        init_selection_frame_info(self.selected_frame, self.initial_frame)
        self.selected_frame.grid_remove()
    
        ApproximateGreeting = Label(self.initial_frame, text = "Welcome to Approximate! To get started, simply select one of the tasks in one of the categories from their respective dropdown menu")
        ApproximateGreeting.place(relx= .5, rely= 0.145 ,anchor = "center")
   
        #As far as I can tell, there is no tactful way to add a lot of labels and this is the only way possible to do it i.e manually
        LinearAlgebraLabel = Label(self.initial_frame, text = "Linear algebra")
        NPCLabel = Label(self.initial_frame, text = "NPC problems")
        LinearProgrammingLabel = Label(self.initial_frame, text = "Linear Programming")
        DataScienceLabel = Label(self.initial_frame, text = "Data science")
        LinearAlgebraLabel.place(relx = 0.2, rely=.25)
        NPCLabel.place(relx = 0.4,rely=.25)
        LinearProgrammingLabel.place(relx = 0.6,rely=.25)
        DataScienceLabel.place(relx = 0.8,rely=.25)
        ########################################Create dropdown menus
        chosen_option = StringVar(self.initial_frame)
        chosen_option.set(nill_choice)
        linear_algebra_options = OptionMenu(self.initial_frame,chosen_option,*linear_algebra_choices)
        linear_algebra_options.place(relx=0.2, rely = .3)
        npc_options = OptionMenu(self.initial_frame,chosen_option,*npc_choices)
        npc_options.place(relx=0.4, rely = .3)
    
        #We specify the command to be executed to be a lambda, because otherwise it will execute automatically when the window is created
    
        ReadyButton = Button(self.initial_frame, text = "Continue", command= lambda: value_select_handler[chosen_option.get()](selected_frame, chosen_option.get(), self.initial_frame))
        ReadyButton.place(relx= .85, rely= 0.85)
        '''We want to be able to call a particular function, based on '''
        def call_method(self, str_selected_problem):
            return getattr(self, self.value_select_handler[str_selected_problem])(str_selected_problem)
        
        def change_context_menu_npc(self,frame,problem,mainframe):
            mainframe.grid_remove()
            frame.grid()
    
        def err_no_value_chosen_msg(self,frame,problem,mainframe):
            tkinter.messagebox.showerror("No problem chosen","Error: no value has been selected. In order to continue, select a problem from one of the dropdown menus")
    

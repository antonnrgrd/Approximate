from menu_constants import *
import tkinter.messagebox
import tkinter.ttk
from tkinter import *

def change_context_menu_npc(frame,problem,mainframe):
    mainframe.grid_remove()
    frame.grid()
    

def err_no_value_chosen_msg(frame,problem,mainframe):
    tkinter.messagebox.showerror("No problem chosen","Error: no value has been selected. In order to continue, select a problem from one of the dropdown menus")

#A generic frame initalizer that initalizes information that every window, regardless of the chosen problem will need to have.
#
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
    
    select_report.place(relx = .25, rely=.2)
    select_verbose.place(relx = .25, rely=.15)
    
    report_name_entry.place(relx=.25, rely=.1)
    
    back_button.place(relx=.08, rely=.85)
    run_button.place(relx= .85, rely= 0.85)

    generate_report_label.place(relx=0.15, rely=.2)

value_select_handler = {nill_choice : err_no_value_chosen_msg, npc_choices[0] : change_context_menu_npc}



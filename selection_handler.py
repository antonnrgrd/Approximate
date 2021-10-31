from menu_constants import *
import tkinter.messagebox
import tkinter.ttk

def err_no_value_chosen_msg():
    tkinter.messagebox.showerror("No problem chosen","Error: no value has been selected. In order to continue, select a problem from one of the dropdown menus")

def init_frame_info(selection):
    frame = tkinter.ttk.Label(text = selection)
    run_button = Button(frame, text="Run")
    back_button = Button(frame, text = "Back")
    report_name = Entry(frame, text = "Report name")
    
    report_name.place(relx=.5, rely=.1)
    back_button.place(relx=.1, rely=.1)
    run_button.place(relx= .9, rely= 0.9)

value_select_handler = {nill_choice : err_no_value_chosen_msg}

def menu_handler(arg):
   value_select_handler[arg.get()]()

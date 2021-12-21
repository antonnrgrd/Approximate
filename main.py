import os
from tkinter import *
from GuiInterface import UserMenu
from menu_constants import *
from chained_windows import *
import numpy as np
import pandas as pd
from linear_programming import *
#from linear_algebra import *



def main():

    
    data = { 'x1': [2,0,1,1], 'x2':[1,2,1,2], 'x3':[3,1,1,1] , 'ineq': ['na','<=', '=', '>='], 'val': [ np.inf , 2,4,3]}
    frame = pd.DataFrame(data)
    frame = frame.rename(index={0: 'obj'})
    frame.to_csv("example1.csv")

    data = { 'x1': [40,1,1,3], 'x2':[30,2,1,2] , 'ineq': ['na','<=', '<=', '<='], 'val': [ np.inf , 16,9,24]}
    frame = pd.DataFrame(data)
    frame = frame.rename(index={0: 'obj'})
    frame.to_csv("example2.csv")
    pframe = pd.read_csv("example2.csv",index_col=[0])


    data = { 'x1': [5,4,2], 'x2':[4,2,3] , 'ineq': ['na','<=', '<='], 'val': [ np.inf,32,24]}
    frame = pd.DataFrame(data)
    frame = frame.rename(index={0: 'obj'})
    frame.to_csv("example3.csv")
    pframe = pd.read_csv("example3.csv",index_col=[0])
    
    data = { 'x1': [40,1,1], 'x2':[30,2,1] , 'ineq': ['na','<=', '<='], 'val': [ np.inf , 16,9,24]}
    frame = pd.DataFrame(data)
    frame = frame.rename(index={0: 'obj'})
    frame.to_csv("example2.csv")
    pframe = pd.read_csv("example2.csv",index_col=[0])
    
    '''
    pframe = pd.read_csv("example.csv",index_col=[0])
    LP = LinearProgramming(False)
    
    LP.tableau = LP.canonicalize_tableau(pframe)
    print(LP.tableau)
    '''

    '''
    root = Tk()
    #Adds title to the file menu
    chained_window = ChainedWindows(root)
    root.wm_title("Approximate")
    root.mainloop()
    '''
    
    
if __name__ == '__main__':
    main()

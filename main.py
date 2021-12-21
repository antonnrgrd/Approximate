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

    
    data = { 'x1': [2,0,1,1], 'x2':[1,2,1,-2], 'x3':[3,1,1,1] , 'ineq': ['na','<=', '=', '>='], 'val': [ np.inf , 2,4,3]}
    frame = pd.DataFrame(data)
    frame = frame.rename(index={0: 'obj'})
    frame.to_csv("example.csv")
    
    
    pframe = pd.read_csv("example.csv",index_col=[0])
    LP = LinearProgramming(False)
    print('initial frame is:')
    print(pframe)
    LP.tableau = LP.canonicalize_tableau(pframe)
    print('result is now')
    print(LP.tableau)
    

    '''
    root = Tk()
    #Adds title to the file menu
    chained_window = ChainedWindows(root)
    root.wm_title("Approximate")
    root.mainloop()
    '''
    
    
if __name__ == '__main__':
    main()

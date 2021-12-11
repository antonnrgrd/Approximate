import os
from tkinter import *
from GuiInterface import UserMenu
from menu_constants import *
from chained_windows import *
#from linear_algebra import *



def main():
    '''
    linear_algebra = MatrixOperators(generate_report = True, verbose = False)
    linear_algebra.matrix_mult(np.random.rand(10,10),np.random.rand(10,10))
    '''

    
    root = Tk()
    #Adds title to the file menu
    chained_window = ChainedWindows(root)
    root.wm_title("Approximate")
    root.mainloop()
    
    
    
if __name__ == '__main__':
    main()

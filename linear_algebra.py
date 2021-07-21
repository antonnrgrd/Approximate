import numpy as np
from solution import Solution





    
    
    


class MatrixHolder(Solution):
    def __init__(self,matrices):
        super().__init__()
        self.matrices = matrices
    

class MatrixOperators(MatrixHolder):
    def __init__(self):
        super().__init__()
        '''The implementation of the standard matrix-matrix multiplication. For sake of readability and understanding, the most basic
        algorithm is used'''
    def write_contents(self):
    def matrix_mult(self,first_matrix, second_matrix):
        if first_matrix.vectors.shape[1] != second_matrix.vectors.shape[0]:
            self.errornous_computation = True
            if generate_report == True:
                self.error_type = "Error: matrix product is defined only if the number of columns in the first matrix match the number of rows in the second matrix. However, the first given matrix has " + first_matrix.vectors.shape[1] + " and the second given matrix has " + second_matrix.vectors.shape[0] + " columns"
                return
        else:
            '''I must confess I don't how exactly adding n^3 if true checks are, but for the sake of effeciency, I chose only
            to check once if we want to store the solutions and if chosen so, store the computations'''
            if verbose == True:
                for row in matrices[0].shape[0]:
                    for column in self.matrices[1].shape[1]:
            else:
                for row in matrices[0].shape[0]:
                    for column in self.matrices[1].shape[1]:
    
        if generate_report == True:
            self.write_out_solution()
        
                    
            
            
            
            
            
            

    
    
        
    

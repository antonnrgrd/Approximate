import numpy as np
from solution import Solution


    

class MatrixOperators(Solution):
    def __init__(self,generate_report = False, verbose = False):
        super().__init__()
        '''The implementation of the standard matrix-matrix multiplication. For sake of readability and understanding, the most basic
        algorithm is used'''
    def write_contents(self, filename):
        filename.write('The resulting matrice(s) of the computation(s) are \n ')
        for matrix in self.matrices:
            filename.write('\\[ \n')
            filename.write('\\begin{array} \n')
            '''If the size of rows/columns of the resulting matrix is bigger than 10 in dimension, we need to write it out differently as,
        #it is too big to write out conventionally'''
            if soltion.shape[0] > 10 or solution.shape[1] > 10:
                pass
            else:
                for row_index in matrix:
                    for column_index in matrix:
                        print(column_index)
                        #filename.write()
                filename.write('\\end{array} \n')
                filename.write('\\]')
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
                        pass
            else:
                self.solution = np.matmult(first_matrix,second_matrix)
        if generate_report == True:
            self.write_out_solution()
        
                    
            
            
            
            
            
            

    
    
        
    

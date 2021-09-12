import numpy as np
from solution import Solution


    

class MatrixOperators(Solution):
    def __init__(self,generate_report = False, verbose = False):
        super().__init__(generate_report, verbose)
        '''The implementation of the standard matrix-matrix multiplication. For sake of readability and understanding, the most basic
        algorithm is used'''
    def write_matrix(self, matrix, filename):
                filename.write('\\[ \n')
                filename.write('\\begin{bmatrix} \n')
                '''If the size of rows/columns of the resulting matrix is bigger than 10 in dimension, we need to write it out differently as,it is too big to write out conventionally and instead write 10 values of the matrix per line. We use index iteration as this allows us to simultaneously '''
                if matrix.shape[0] > 1 or matrix.shape[1] > 1:
                    numbers_written = 0
                    for i in range(matrix.shape[0]):
                        for j in range(matrix.shape[1]):
                                filename.write(' \\text{ '+ str(i) + ' , ' + str(j) + ' :  ' + str(matrix[i][j]) + '}'  )
                                ''' This is pretty ugly and not very Python-y but other solutions online discuss how various built-in
                                methods for processing n values at a time has some issue or another regarding cases when there are not
                                sufficient values left in a list'''
                                numbers_written = numbers_written +1
                                if numbers_written == 5:
                                    nummbers_written = 0
                                    filename.write('\\\\ \n')
                                else:
                                    filename.write(' & ')
                else:
                    for row in matrix:
                        for value in row:
                            filename.write(str(value) + ' & ')
                        filename.write('\\\\ \n')
                filename.write('\\end{bmatrix} \n')
                filename.write('\\]')
    def write_contents(self, filename):
        print('arguments',self.arguements)
        print('solutionss',self.solutions)
        if self.errornous_computation == True:
            filename.write(self.error_type)
        else:
            filename.write(self.intro_flavor_text + ' \\newline ' )
            for argument in self.arguements:
                self.write_matrix(argument,filename)
            filename.write(self.result_flavor_text + ' \\newline ')
            for solution in self.solutions:
                self.write_matrix(solution, filename)
    def matrix_mult(self,first_matrix, second_matrix):
        self.arguments = []
        if first_matrix.shape[1] != second_matrix.shape[0]:
            self.errornous_computation = True
            if self.generate_report == True:
                self.error_type = "Error: matrix product is defined only if the number of columns in the first matrix match the number of rows in the second matrix. However, the first given matrix has " + str(first_matrix.shape[1]) + " columns and the second given matrix has " + str(second_matrix.shape[0]) + " rows"
        else:
            '''I must confess I don't how exactly adding n^3 if true checks are, but for the sake of effeciency, I chose only
            to check once if we want to store the solutions and if chosen so, store the computations'''
            if self.verbose == True:
                for row in matrices[0].shape[0]:
                    for column in self.matrices[1].shape[1]:
                        pass
            else:
                self.intro_flavor_text = 'The input matrices for the matrix product are'
                self.result_flavor_text = 'And the resulting matrix product is'
                self.arguements.append(first_matrix)
                self.arguements.append(second_matrix)
                self.solutions.append(np.matmul(first_matrix,second_matrix))
        if self.generate_report == True:
            '''We wait appending the matrices to the arguemnt field until we are doen using them b.c  '''
            self.write_out_solution()
    def find_inverse(self, matrix):
        self.arguments = []
        pass
        
                    
            
            
            
            
            
            

    
    
        
    

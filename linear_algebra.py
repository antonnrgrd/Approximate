import numpy as np
from solution import Solution


    

class MatrixOperators(Solution):
    def __init__(self,generate_report = False, verbose = False):
        super().__init__(generate_report, verbose)
        '''The implementation of the standard matrix-matrix multiplication. For sake of readability and understanding, the most basic
        algorithm is used'''
    def write_matrix(self, matrix, filename):
                
                '''If either matrix shape exceeds the size of 5, we need to write it out as several matrices. This is because latex has a limit on how large a single matrix can be when writing it out.'''
                if matrix.shape[0] > 5 or matrix.shape[1] > 5:
                    numbers_written = 0
                    values_written = 0
                    filename.write('\\[ \n')
                    filename.write('\\begin{matrix} \n')
                    for i in range(matrix.shape[0]):
                        for j in range(matrix.shape[1]):
                            '''Because floating point numbers can end up with a lot of digits after the decimal point and thus making writingthem out on '''
                                filename.write(' \\text{ '+ str(i) + ' , ' + str(j) + ' :  ' + str(round(matrix[i][j],3)) + '}'  )
                                ''' This is pretty ugly and not very Python-y but other solutions online discuss how various built-in
                                methods for processing n values at a time has some issue or another regarding cases when there are not
                                sufficient values left in a list'''
                                numbers_written = numbers_written +1
                                values_written = values_written + 1
                                if numbers_written == 5:
                                    nummbers_written = 0
                                    filename.write('\\\\ \n')
                                else:
                                    filename.write(' & ')
                                if values_written == 5:
                                    values_written = 0
                                    filename.write('\\end{matrix} \n')
                                    filename.write('\\]')
                                    filename.write('\\[ \n')
                                    filename.write('\\begin{matrix} \n')
                    filename.write('\\end{matrix} \n')
                    filename.write('\\]')
                    
                else:
                    filename.write('\\[ \n')
                    filename.write('\\begin{bmatrix} \n')
                    for row in matrix:
                        for value in row:
                            filename.write(str(round(value,3)) + ' & ')
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
            if self.verbose == True:
                ''' If we want the report to be verbose, we need to explicitly do all computations '''
                matrix = np.empty(self.matrices[0].shape[0], self.matrices[1].shape[1])
                for i in range (self.matrices[0].shape[0]):
                    for j in range(self.matrices[1].shape[1]):
                        value = 0
                        computation = 'row ' + str(i) + ' column ' + str(j)
                        for k in range(self.matrices[0].shape[1]):
                            value+= self.matrices[0][i][k] + self.matrices[1][k][j]
                        matrix[i][j] = value
                self.intro_flavor_text = 'The input matrices for the matrix product are'
                self.result_flavor_text = 'And the resulting matrix product is'
                self.arguements.append(first_matrix)
                self.arguements.append(second_matrix)
                self.solutions.append(matrix)
                
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
        
                    
            
            
            
            
            
            

    
    
        
    

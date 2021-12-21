import os
from datetime import datetime
from os.path import expanduser
import abc
#We import thread because there will be several attempts at multithreading the various problems
#import thread
'''A class representing a solution. We are deliberately vague about the error types, computations, solutions, etc.
due to the many different shapes there could take '''
class Solution(metaclass=abc.ABCMeta):
    def __init__(self,generate_report = False, verbose = False):
        self.arguements = []
        self.report = None
        self.solutions = []
        self.computations = None
        self.error_type = None
        self.errornous_computation = False
        self.generate_report = generate_report
        self.verbose = verbose
        self.computation_time = None
        self.intro_flavor_text = None
        self.result_flavor_text = None
    ''' The write contents solution method responsbile for writing out the actual input, args comps etc. Since said values have
    such as huge variability depending on what class does the inherting, it will be defined as an interface'''
    def write_out_solution(self):
        '''To avoid overwriting reports, we chose to uniquely represent each
        report by a timestamp + day  '''
        now = datetime.now()
        today = datetime.today()
        current_time = now.strftime("%H-%M-%s")
        date = now.strftime("%d-%B-%Y")
        home = expanduser('~')
        os.chdir(home)
        if not os.path.isdir(home + '/approximate_reports'):
            os.makedirs("approximate_reports")
        file_name = os.getcwd() + ('/approximate_reports/report' + date + current_time + '.tex')
        self.report = file_name
        report = open(file_name, 'w')
        '''An ugly way to write, but afaik there is no really elegant way to make a large write to a file As a side note, using \n is a passable way to write a newline when writing to a file, but an argument broke out in the stackoverflow thread arguing about whther some other technique is superior. For now i will just use \n'''
        report.write('\\documentclass[]{article} \n \\usepackage{amsmath} \n \\usepackage{float} \n \\begin{document} \n \\tableofcontents \n \\section{Summary} \n')
        self.write_contents(report)
        if self.verbose == True:
            self.write_steps()
        report.write('\end{document}')
        report.close()
        os.system('pdflatex ' + file_name)
    def write_csv_solution():
        pass
    def write_latex_arg(matrix):
        ''' Because latex has issues with writing out matrices larger than 10x10 (iirc), we work around this by breaking it up into multiple writes of smaller matrices'''
        if matrix.shape[0] > 5 or (matrix.ndim > 1 or matrix.shape[1] > 5):
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
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass,'write_contents') and
                callable(subclass.write_contents) and
                hasattr(subclass,'write_steps') and
                callable(subclass.write_steps))

    
    

        
        

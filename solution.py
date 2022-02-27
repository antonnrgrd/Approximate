import os
from datetime import datetime
from os.path import expanduser
import abc
import pandas as pd
#We import thread because there will be several attempts at multithreading the various problems
#import thread
'''A class representing a solution. We are deliberately vague about the error types, computations, solutions, etc.
due to the many different shapes there could take '''
class Solution(metaclass=abc.ABCMeta):
    def __init__(self,generate_report = False, verbose = False):
        self.arguements = None
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
        self.expected_shape = None
    def readin_data(self, fpath,expected_shape):
        if fpath != "":
            if os.exsists(fpath):
                if fpath.endswith('.csv'):                 
                    frame = pd.read_csv(fpath)
                    if frame.values.shape == expected_shape:
                        self.arguements.append(frame.values)
                    else:
                        return "Pandas frame has the wrong shape, expected " + str(expected_shape) + " but got frame of shape " + str(frame.values.shape)
                else:
                    return "File was not a csv file. Only csv files are allowed for pandas"
            else:
                "Error, file not found in the provided folder"
    ''' The write contents solution method responsbile for writing out the actual input, args comps etc. Since said values have
    such as huge variability depending on what class does the inherting, it will be defined as an interface'''
    def write_out_solution(self,report_name):
        '''To avoid overwriting reports, we chose to uniquely represent each
        report by a timestamp + day  '''
        now = datetime.now()
        home = expanduser('~')
        os.chdir(home)
        if not os.path.isdir(home + '/approximate_reports'):
            os.makedirs("approximate_reports")
        file_name = os.getcwd() + ('/approximate_reports/report' + report_name + '.tex')
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
    def write_latex_arg(matrix,filewriter):
        ''' Because latex has issues with writing out matrices larger than 10x10 (iirc), we work around this by breaking it up into multiple writes of smaller matrices'''
        if matrix.shape[0] > 5 or (matrix.ndim > 1 or matrix.shape[1] > 5):
                    numbers_written = 0
                    values_written = 0
                    filewriter.write('\\[ \n')
                    filewriter.write('\\begin{matrix} \n')
                    for i in range(matrix.shape[0]):
                        for j in range(matrix.shape[1]):                            
                            '''Because floating point numbers can end up with a lot of digits after the decimal point and thus making writingthem out on '''
                            filewriter.write(' \\text{ '+ str(i) + ' , ' + str(j) + ' :  ' + str(round(matrix[i][j],3)) + '}'  )
                            ''' This is pretty ugly and not very Python-y but other solutions online discuss how various built-in
                            methods for processing n values at a time has some issue or another regarding cases when there are not
                            sufficient values left in a list'''
                            numbers_written = numbers_written +1
                            values_written = values_written + 1
                            if numbers_written == 5:
                                nummbers_written = 0
                                filewriter.write('\\\\ \n')
                            else:
                                filewriter.write(' & ')
                            if values_written == 5:
                                values_written = 0
                                filewriter.write('\\end{matrix} \n')
                                filewriter.write('\\]')
                                filewriter.write('\\[ \n')
                                filewriter.write('\\begin{matrix} \n')
                    filewriter.write('\\end{matrix} \n')
                    filewriter.write('\\]')
                    
        else:
            filewriter.write('\\[ \n')
            filewriter.write('\\begin{bmatrix} \n')
            for row in matrix:
                for value in row:
                    filewriter.write(str(round(value,3)) + ' & ')
                filewriter.write('\\\\ \n')
                filewriter.write('\\end{bmatrix} \n')
                filewriter.write('\\]')
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass,'write_contents') and
                callable(subclass.write_contents) and
                hasattr(subclass,'write_steps') and
                callable(subclass.write_steps) and
                hasattr(subclass,'yield_csv_format') and
                callable(subclass.yield_csv_format))
                 
                   
    

    
    

        
        

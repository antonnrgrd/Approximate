import os
from datetime import datetime
from os.path import expanduser
import abc
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
        report.write('\\documentclass[]{article} \n \\usepackage{amsmath} \n \\usepackage{float} \n \\setcounter{MaxMatrixCols}{100000000000000000000000} \n \\begin{document} \n \\tableofcontents \n \\section{Summary} \n')
        self.write_contents(report)
        if self.verbose == True:
            self.write_steps()
        report.write('\end{document}')
        report.close()
        os.system('pdflatex ' + file_name)
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass,'write_contents') and
                callable(subclass.write_contents) and
                hasattr(subclass,'write_steps') and
                callable(subclass.write_steps))

    
    

        
        

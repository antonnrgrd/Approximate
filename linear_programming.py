from solution import *
import pandas as pd
import numpy as np
class LinearProgramming(Solution):
    def __init__(self,canonical_form = False):
        self.canonical_form = canonical_form
        self.tableau = None
        self.constraints = None
        self.slack_index = None
        self.artifical_var_index = None
        '''We might sometimes have to reverse/flip an inequality. For that we opt to use a dictionary to do this'''
        self.constraint_map = {'>=': '<=', '<=':'>=' }
        '''In order to add slack variables to the canonical tablueau, we basically add slack variables at positions of the tableau at increments of one. 
        The initial slack variable is to be placed at the last position where a 0 occurs'''
    def yield_slack_artvar(self,slack_index,artvar_index, vectorlength, negative_slackvar):
        vector = np.zeros(vectorlength)
        if slack_index != -1:
            ''' We increment the slack/artificial variable indices only if we add them to the intial tableau because it is not guaranteed that we actually need the variable for the constraint in question. i.e We MIGHT need another variable for our tableau or not and the increment of the index indicates the addition of another variable'''
            self.slack_index = self.slack_index +1
            if negative_slackvar == True:
                vector[slack_index] = -1
            else:
                vector[slack_index] = 1
        '''Sometimes, we do not have to add an artifical variable, which is indicated by a negative index. 
        Hence we only add it if the index is non-negative'''
        if artvar_index != -1:
            self.artifical_var_index = self.artifical_var_index +1
            vector[artvar_index] = 1
        return vector
        
            
    def add_constraint(self,constraint,slack_index,artvar_index,tableau,vector_length):
        ''' '''
        if constraint[-1] < 0:
           constraint[0:-2],constraint[-1] = np.negative(constraint[0:-2]), np.negative(constraint[-1])
           constraint[-2] = self.constraint_map[constraint[-2]]
           print(constraint)
        ''' strictly greater or less than are not considered as they are not defined in LP programming '''
        if constraint["ineq"] == '>=':
            '''We cast the values to be lists because Numpy arrays are not intended to be constantly resized, whereas lists are more suited for this '''
            tableau.append(list(constraint[0:-2]) + list(self.yield_slack_artvar(slack_index,artvar_index,vector_length,True)) + list([constraint[-1]]))
        elif constraint["ineq"] == '<=':
            tableau.append(list(constraint[0:-2]) + list(self.yield_slack_artvar(slack_index,-1,vector_length,False)) + list([constraint[-1]]))
        elif constraint["ineq"] == '=':
            tableau.append(list(constraint[0:-2]) + list(self.yield_slack_artvar(-1,artvar_index,vector_length,False)) + list([constraint[-1]]))
        return tableau
        
    def canonicalize_tableau(self,constraints_table):
        goal = constraints_table.loc["obj"]
        initial_tableau = []
        '''The number of artificial and slack variables could potentially be up to # 2*(constraints-1), so we reserve enough space for that. This might possibly waste memory if e.g only equality constraints are present, meaning no slack variables are needed, only artificial variables. However, for now there is only focus on writing a program that works and later on, a more clever solution for allocating space for these variables can be devised. Hence, we compute the size of the slack and artifical variable vector as such'''

        ''' I add the same value twice rather than multiply it by two, because when the value is multiplied by 2, the result is for some reason +1 too many  '''
        slack_artvar_vectorsize = (len(constraints_table[1:].index)-1+len(constraints_table[1:].index)-1)
        '''The first slack variable in the tableau occurs at the index after the last original variable, the first artificial variable one index after the last slack variable, hence
        we define the intial indices for the values as such'''
        self.slack_index, self.artifical_var_index = 0, slack_artvar_vectorsize//2
        '''We skip the first row since it is designated for the objective of the problem
        rather than constraints'''
        for rowindex, constraint in constraints_table[1:].iterrows():
            initial_tableau = self.add_constraint(constraint, self.slack_index,self.artifical_var_index, initial_tableau, slack_artvar_vectorsize)            
        tableau_objective = list(np.negative(goal[0:-2]))
        '''We create the last objective vector to be  slack_artvar_vectorsize+1 to account for the fact that the constraint does not have a rhs'''
        objective_vector = list(np.zeros(slack_artvar_vectorsize+1))
        objective_vector[-2] = 1
        initial_tableau.append(tableau_objective+ objective_vector)
        '''We we work with list in the building of the tableau and convert it to a numpy arrays as numpy arrays are intended/made with resizing in mind'''
        return np.array(initial_tableau)
            
                
    def simplex(self):
        if self.canonical_form == False:
            self.tableau = self.canonicalize_tableau()
        
        
        

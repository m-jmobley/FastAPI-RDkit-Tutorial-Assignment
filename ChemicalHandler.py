# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:00:33 2023
"""
#%% Dependencies

from Reactant import Reactants
from ReactionSmart import ReactionSmarts

#%% ChemicalHandler Class Declaration

class InputHandler():
    
    def __init__(self):
        self.input_dict = {}
         
    def getReactants(self,reactant) -> bool:
        if isinstance(reactant, Reactants):
            self.input_dict['reactants'] = reactant.REACTANT
            return True
        else:
            raise TypeError("Data must be an instance of Reactants.")
            
    def getSMARTS(self,smart) -> bool:
        if isinstance(smart, ReactionSmarts):
            self.input_dict['reaction_smarts'] = smart.SMARTS
            return True
        else:
            raise TypeError("Data must be an instance of ReactionSmarts.")
            

        
        
        
        
        


# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:04:25 2023

"""
#%% Dependencies
from rdkit import Chem
#%% Reactants Class Declaration

class Reactants():
        
    def __init__(self, reactant: str):
        self.REACTANT = reactant
                
    def Verify(self) -> bool: 
        
        checkValid = True if Chem.MolFromSmiles(self.REACTANT) else False            
        return checkValid
    

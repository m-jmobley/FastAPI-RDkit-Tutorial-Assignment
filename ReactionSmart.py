# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:04:39 2023


"""

#%% Dependencies
from rdkit.Chem import AllChem
#%% ReactionSmarts Class Declaration

class ReactionSmarts():
      
    def __init__(self,SMARTS:str):
        self.SMARTS = SMARTS
        
        
    def Verify(self) -> bool:
        
        try:
            AllChem.ReactionFromSmarts(self.SMARTS)
        except ValueError:
            print("Invalid SMARTS string.")
            return False
        else:      
            return True
    
            
        
        


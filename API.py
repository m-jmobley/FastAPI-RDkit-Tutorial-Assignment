# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 00:17:14 2023

@author: M312630
"""
#%% Dependencies

from fastapi import FastAPI
from ChemicalHandler import InputHandler
from rdkit.Chem import AllChem
from rdkit import Chem
import json

#%% API class Declaration

class API:
    
    global app
    app = FastAPI()
    
    def __init_(self):
        
        self.verified_request = {}
         
    def apiInstance(self):
        return app
    
    def setRequest(self,handler_instance):
        if isinstance(handler_instance, InputHandler):
            self.verified_request = handler_instance.input_dict
            print(f"Request {self.verified_request} is now authorized.")
        else:
            raise TypeError("Data must be instance of InputHandler.")
                                       
    @app.get('run_reaction/{SMILE}/{SMART}')
    async def Run_Reaction_SMART(SMILE: str, SMART: str):

        rxn = AllChem.ReactionFromSmarts(SMART)
        reactant = Chem.MolFromSmiles(SMILE)
        products = rxn.RunReactants((reactant, ))
        
        result_mols = []
        for p in products:
            for q in p:
                result_mols.append(Chem.MolToSmiles(q))
        return result_mols
        



# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 00:17:14 2023
"""
#%% Dependencies

from fastapi import FastAPI
from ChemicalHandler import InputHandler
from rdkit.Chem import AllChem
from rdkit import Chem
import json
from pydantic import BaseModel

#%% API class Declaration

class API:
    
    global app
    app = FastAPI()

    
    def __init__(self):
        
        self.verified_request = {}

         
    def apiInstance(self):
        return app
    
    def setRequest(self,handler_instance) -> bool:
        if isinstance(handler_instance, InputHandler):
            self.verified_request = handler_instance.input_dict
            print(f"Request {self.verified_request} is now authorized.")
            return True
        else:
            raise TypeError("Data must be instance of InputHandler.")
                                               



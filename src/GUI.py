 # -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:55:04 2024

@author: M312630
"""

#%% Dependencies

from ChemicalHandler import InputHandler
from Reactant import Reactants
from ReactionSmart import ReactionSmarts
import requests
from api__init__ import api_instance

#%%  

controller_instance = InputHandler()

SMILE: str
SMART: str
SMILE = input("Enter SMILE Identifier: ")
SMART = input("Enter reaction SMART: ")

reactants_instance = Reactants(SMILE)
smart_instance = ReactionSmarts(SMART)

is_smile_valid = reactants_instance.Verify()    
if is_smile_valid:
    controller_instance.getReactants(reactants_instance)
   
is_smart_valid = smart_instance.Verify()
if is_smart_valid:
    controller_instance.getSMARTS(smart_instance)

if is_smile_valid == True and is_smart_valid == True:
    api_instance.setRequest(controller_instance)
    results = requests.get(f"http://127.0.0.1:8000/reaction_return/?SMILE={api_instance.verified_request['reactants']}&SMART={api_instance.verified_request['reaction_smarts']}")
    print(results)
    print(results.json())

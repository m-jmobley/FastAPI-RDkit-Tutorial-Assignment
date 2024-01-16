# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:11:43 2023

"""
#%% Dependencies
from rdkit.Chem import AllChem
from rdkit import Chem
from API import API
#%% Class initializations

api_instance = API()
app = api_instance.apiInstance()

@app.get('/reaction_return/')
def Run_Reaction_SMART(SMILE:str,SMART:str):
    
    print(f"{SMART =} {SMILE =}")
    rxn = AllChem.ReactionFromSmarts(SMART)
    reactant = Chem.MolFromSmiles(SMILE)
    products = rxn.RunReactants((reactant, ))
    result_mols = []
    for p in products:
        for q in p:
            result_mols.append(Chem.MolToSmiles(q))
    return result_mols








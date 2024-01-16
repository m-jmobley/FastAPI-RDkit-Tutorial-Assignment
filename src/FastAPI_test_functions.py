# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:02:03 2024
"""
#%% Testing library dependencies

from ChemicalHandler import InputHandler
from Reactant import Reactants
from ReactionSmart import ReactionSmarts
from api__init__ import app
from fastapi import FastAPI
from  fastapi.testclient import TestClient
from API import API

client = TestClient(app)
#%% Test Functions in InputHandler

def test_getReactants():
    
    input_handler_instance = InputHandler()
    reactants_instance = Reactants('CC1=CC=C(C=C1)C1=CC(=CC=C1C)C1=CC(C)=CC(C)=C1')
    checkValid = input_handler_instance.getReactants(reactants_instance) # testing primary function

    assert checkValid == True
    
def test_getSMARTS():
    
    input_handler_instance = InputHandler()
    reaction_smarts_instance = ReactionSmarts('[c:8]-[c:6]>>[c:8][I:55].[B:99][c:6]')
    checkValid = input_handler_instance.getSMARTS(reaction_smarts_instance)
    
    assert  checkValid == True
    
#%% Verification function test for Reactants and ReactionSmarts Classes

def test_reactant_verify():
    
    reactants_instance = Reactants('CC1=CC=C(C=C1)C1=CC(=CC=C1C)C1=CC(C)=CC(C)=C1')
    assert reactants_instance.Verify() == True
    
def test_reaction_smarts_verify():
    
    reactants_instance = ReactionSmarts('[c:8]-[c:6]>>[c:8][I:55].[B:99][c:6]')
    assert reactants_instance.Verify() == True
    
#%% API class tests
   
def test_api_instance():
    
    #api_instance = API()
    assert type(app) == type(FastAPI())
    
def test_set_request():
    
    api_instance = API()
    input_handler_instance = InputHandler()
    assert api_instance.setRequest(input_handler_instance) == True
    
#def test_api_connection():
#    response = client.get("/")
#    assert response.status_code == 200

def test_run_reaction():
    
    response = client.get("/reaction_return/")
    assert response.status_code == 200
    assert type(response.json()) == list
    
   
    




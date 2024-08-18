#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:31:01 2022

@author: m.daryalal

Instructions:
    1. Assuming that your group number is M, put your codes in a folder called GroupM
    2. Let CurrentPath be the path of the current file. Put GroupM folder in CurrentPath
    3. Instances are read from a folder called Instances. Put Instances folder in CurrentPath

This file reads the following files:
    1. GurobiSolveRWA_GroupM
    2. GurobiSPsSolveRWA_GroupM
    3. HeuristicSolveRWA_GroupM
    
This file tests the correctness of the format of the following functions:
    1. GurobiLinkSolveRWA(filename ,W) from GurobiSolveRWA_GroupM
    2. AllPaths(filename) from GurobiSolveRWA_GroupM
    3. GurobiSPsSolveRWA(filename ,W) from GurobiSolveRWA_GroupM
    4. AllSPs(filename) from GurobiSPsSolveRWA_GroupM
    5. GurobiSPsSolveRWA(filename ,W) from GurobiSPsSolveRWA_GroupM
    6. WA1(SP_sd,request_list,W) from HeuristicSolveRWA_GroupM
    7. H1SolveRWA(filename ,W) from HeuristicSolveRWA_GroupM
    8. WA2(SP_sd,request_list,W) from HeuristicSolveRWA_GroupM
    9. H2SolveRWA(filename ,W) from HeuristicSolveRWA_GroupM
    10. WA3(SP_sd,request_list,W) from HeuristicSolveRWA_GroupM
    11. H3SolveRWA(filename ,W) from HeuristicSolveRWA_GroupM
    12. WA4(SP_sd,request_list,W) from HeuristicSolveRWA_GroupM
    13. H4SolveRWA(filename ,W) from HeuristicSolveRWA_GroupM
    14. WA5(SP_sd,request_list,W) from HeuristicSolveRWA_GroupM
    15. H5SolveRWA(filename ,W) from HeuristicSolveRWA_GroupM

"""

######################################
GroupNo = "11"
W = 5
instance = "2"
######################################

def Test_Paths_Type(P):
    if (not isinstance(P, dict)) or \
       (not isinstance(list(P.keys())[0], tuple)) or \
       (not isinstance(list(P.values())[0], list)) or \
       (not isinstance(list(P.values())[0][0], list)) or \
        not ((isinstance(list(P.values())[0][0][0], tuple)) or (isinstance(list(P.values())[0][0][0], list))):
        print(P)
        print("Your data structure for a storing paths is not correct!")
        print("Correct data structure for the set of all shortest paths:")
        print("A dictionary, where a key is a 2d tuple representing a node pair with traffic, and the value of an entry is a list of paths")
        print("A path is a list of links, and a link is represented by a 3d tuple (or list) of the form (link_index, link_start_node, link_end_node)")
        raise Exception()


import importlib
import pandas as pd
import gurobipy as gp
#gp.setParam('OutputFlag', 0)


filename = "failedInstances/" + instance +".txt"
df = pd.read_csv(filename, header=None, sep="\t")
_, _, _, _, request_list = df[0].apply(eval)

######################################

######### Exact Formulations #########

Module = "Group" + GroupNo + '.' + "GurobiSolveRWA_Group" + GroupNo
solver = importlib.import_module(Module)

print("************************")
print("Testing link formulation...")
try:
    link_obj = int(solver.GurobiLinkSolveRWA(filename ,W))
    print("Link formulation optimal objective value: ", link_obj)
except Exception as e:
    print("GurobiLinkSolveRWA should return the number of fulfilled requests!")
    raise e

print("************************")
print("Testing set of all paths...")
try:
    P_sd = solver.AllPaths(filename)
    print(P_sd)
    Test_Paths_Type(P_sd)
except Exception as e:
    raise e

print("************************")
print("Testing path formulation with all paths...")
try:
    path_obj = int(solver.GurobiPathSolveRWA(filename ,W))
    print("Path formulation optimal objective value: ", path_obj)
except Exception as e:
    print("GurobiPathSolveRWA should return the number of fulfilled requests!")
    raise e

######################################

Module = "Group" + GroupNo + '.' + "GurobiSPsSolveRWA_Group" + GroupNo
solver = importlib.import_module(Module)

print("************************")
print("Testing set of all shortest paths...")
try:
    SPs_sd = solver.AllSPs(filename)
    Test_Paths_Type(SPs_sd)
except Exception as e:
    raise e

print("Testing path formulation with all shortest paths...")
try:
    SPs_obj = int(solver.GurobiSPsSolveRWA(filename ,W))
    print("SPs formulation objective value: ", SPs_obj)
except Exception as e:
    print("GurobiSPsSolveRWA should return the number of fulfilled requests!")
    raise e

#####################################

Module = "Group" + GroupNo + '.' + "HeuristicSolveRWA_Group" + GroupNo
solver = importlib.import_module(Module)


SP_sd = {}
for key in SPs_sd.keys():
        SP_sd[key] = SPs_sd[key][0]

#########

print("************************")
print("Testing Algorithm 1...")

try:
    WA1_obj = int(solver.WA1(SP_sd,request_list,W))
    print("WA1 objective value: ", WA1_obj)
except Exception as e:
    print("WA1 should return the number of fulfilled requests!")
    raise e

try:
    alg1_obj = int(solver.H1SolveRWA(filename ,W))
    print("Algorithm 1 objective value: ", alg1_obj)
except Exception as e:
    print("Algorithm 1 should return the number of fulfilled requests!")
    raise e

#########

print("************************")
print("Testing Algorithm 2...")

try:
    WA2_obj = int(solver.WA2(SP_sd,request_list,W))
    print("WA2 objective value: ", WA2_obj)
except Exception as e:
    print("WA2 should return the number of fulfilled requests!")
    raise e

try:
    alg2_obj = int(solver.H2SolveRWA(filename ,W))
    print("Algorithm 2 objective value: ", alg2_obj)
except Exception as e:
    print("Algorithm 2 should return the number of fulfilled requests!")
    raise e

#########

print("************************")
print("Testing Algorithm 3...")

try:
    WA3_obj = int(solver.WA3(SP_sd,request_list,W))
    print("WA3 objective value: ", WA3_obj)
except Exception as e:
    print("WA3 should return the number of fulfilled requests!")
    raise e

try:
    alg3_obj = int(solver.H3SolveRWA(filename ,W))
    print("Algorithm 3 objective value: ", alg3_obj)
except Exception as e:
    print("Algorithm 3 should return the number of fulfilled requests!")
    raise e

#########

print("************************")
print("Testing Algorithm 4...")

try:
    WA4_obj = int(solver.WA4(SP_sd,request_list,W))
    print("WA4 objective value: ", WA4_obj)
except Exception as e:
    print("WA4 should return the number of fulfilled requests!")
    raise e

try:
    alg4_obj = int(solver.H4SolveRWA(filename ,W))
    print("Algorithm 4 objective value: ", alg4_obj)
except Exception as e:
    print("Algorithm 4 should return the number of fulfilled requests!")
    raise e

#########

print("************************")
print("Testing Algorithm 5...")

try:
    WA5_obj = int(solver.WA5(SP_sd,request_list,W))
    print("WA5 objective value: ", WA5_obj)
except Exception as e:
    print("WA5 should return the number of fulfilled requests!")
    raise e

try:
    alg5_obj = int(solver.H5SolveRWA(filename ,W))
    print("Algorithm 5 objective value: ", alg5_obj)
except Exception as e:
    print("Algorithm 5 should return the number of fulfilled requests!")
    raise e

######################################

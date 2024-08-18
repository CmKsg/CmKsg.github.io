import GurobiSolveRWA as gurobiSolveRWA
import HeuristicSolveRWA as heuristicSolveRWA
import GurobiSPsSolveRWA as gurobiSPsSolveRWA
import time

def SolveRWA(inputfile,method,W):
    if method==1:
        start_time = time.time()
        obj = heuristicSolveRWA.H1SolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2
    elif method==2:
        start_time = time.time()
        obj = heuristicSolveRWA.H2SolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2
    elif method==3:
        start_time = time.time()
        obj = heuristicSolveRWA.H3SolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2
    elif method==4:
        start_time = time.time()
        obj = heuristicSolveRWA.H4SolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2
    elif method==5:
        start_time = time.time()
        obj = heuristicSolveRWA.H5SolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2

    elif method==6:
        start_time = time.time()
        obj = gurobiSolveRWA.GurobiLinkSolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2
    elif method==7:
        start_time = time.time()
        obj = gurobiSolveRWA.GurobiPathSolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2
    elif method==8:
        start_time = time.time()
        obj = gurobiSPsSolveRWA.GurobiSPsSolveRWA(inputfile,W)
        t2 = time.time() - start_time
        return obj,t2

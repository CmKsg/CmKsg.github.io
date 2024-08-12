import GurobiSPsSolveRWA_Group11 as gsolveSP
import GurobiSolveRWA_Group11 as gsolve
import random
import time

def getBinLength(G):
    if not G:
        l = 0
    else:
        l = len(G.keys())
    return l

def createNewBin(G,SP): # find all unique edges in the short path list and add them to a new List
    newid = getBinLength(G)
    G[newid] = []

    for edgeList in SP.values():
        for edge in edgeList:
            if edge not in G[newid]:
                G[newid].append(edge)
    return newid

def pathFitsIntoBin(path,wbin):
    for edge in path:
        if edge not in wbin:
            return False
    return True

def clearPathFromBin(path,wbin):
    for edge in path:
        wbin.remove(edge)


def WA1(SP, T,W):
    maxNumberOfRequests=0
    nV = len(T)
    wavelinksOfLinks={}
    nodepairs = list(SP.keys())
    nodepairs.sort(key=lambda x: x[1] + 1  + x[0]*nV)
    for nodepair in nodepairs:
        path=SP[nodepair]
        requests = T[nodepair[0]][nodepair[1]]
        for r in range(requests):
            usedWaveLengthsForPath=set()
            for link in path:
                if link  in wavelinksOfLinks:
                    for waveLength in wavelinksOfLinks[link]:
                        usedWaveLengthsForPath.add(waveLength)

            totalWaveLengthsSet = set([x for x in range(W)])
            availableWaveLengthsForPath = totalWaveLengthsSet - usedWaveLengthsForPath
            if len(availableWaveLengthsForPath)>0:
                randomWaveLink = random.choice(list(availableWaveLengthsForPath))
                maxNumberOfRequests+=1
                for link in path:
                    if link not in wavelinksOfLinks:
                        wavelinksOfLinks[link]=[randomWaveLink]
                    else:
                        wavelinksOfLinks[link].append(randomWaveLink)
    return maxNumberOfRequests

def WA2(SP, T, W):

    waveLengthsAssigned = {}
    for w in range(W):
        waveLengthsAssigned[w] = []
    G={} #dictionary to hold the wavelengths
    for w in range(W):
        createNewBin(G, SP)

    nV = len(T)
    nodepairs = list(SP.keys())
    nodepairs.sort(key=lambda x: x[1] + 1  + x[0]*nV)
    for nodepair in nodepairs:
        requests = T[nodepair[0]][nodepair[1]]
        path = SP[nodepair]
        for r in range(requests):
            bins = list(G.keys())
            fitted = False
            for wbin in bins:
                #check if path fits into bin
                if pathFitsIntoBin(path,G[wbin]):
                    clearPathFromBin(path, G[wbin])
                    waveLengthsAssigned[wbin].append(nodepair)
                    fitted=True
                    break

    maxNumberOfRequests=0
    for i in range(W):
        maxNumberOfRequests += len(waveLengthsAssigned[i])
    #print(waveLengthsAssigned)
    return maxNumberOfRequests

def commonLink(pathA, pathB): # return true if two paths any links in common
    for link1 in pathA:
        if link1 in pathB:
            return True
    return False

def largestNumberOfNeighbors(Graph) :
    m = -1
    for i in Graph:
        if m<len(Graph[i]):
            m = len(Graph[i])
            index = i
    return index

def getCandidates(S,Graph):
    candList = []
    for g in Graph:
        if g not in S:
            addtoList = True
            for neighbor in Graph[g]:
                if neighbor in S:
                    addtoList = False
                    break
            if addtoList:
                neighborsThatAreAdjacentToS = 0
                for neighbor in Graph[g]:
                    for neighborsNeighbor in Graph[neighbor]:
                        if neighborsNeighbor in S:
                            neighborsThatAreAdjacentToS +=1

                candList.append((g,neighborsThatAreAdjacentToS))
    candList.sort(key = lambda x: x[1], reverse=True )
    return candList


def WA3(SP, T, W):
#construct a graph for the coloring problem
# When the WA problem is formulated as a graph vertex coloring
# problem, nodes correspond to connection requests (which are copies of the paths fixed
# in the first step), and each color represents a distinct wavelength.

    Graph = {}
    nodepairs = list(SP.keys())
    vertices = []
    for nodepair in nodepairs: # for each nodepair create a vertex in the graph
        requests = T[nodepair[0]][nodepair[1]]
        for i in range(requests):
            vertices.append(nodepair)
    for i in range(len(vertices)): # for each nodepair fing all the other vertices that have common links and make them adjacent
        Graph[i] = []
        for j in range(len(vertices)):
            if i!=j:
                if commonLink(SP[vertices[i]], SP[vertices[j]]):
                    Graph[i].append(j)
    BigS = set() #apply the algorithm at https://en.wikipedia.org/wiki/Recursive_largest_first_algorithm
    w=0
    while len(Graph.keys())>0 and w<W:
        S=set()
        first = largestNumberOfNeighbors(Graph)
        S.add(first)
        candidates = getCandidates(S,Graph)
        while (len(candidates)>0):
            S.add(candidates[0][0])
            candidates = getCandidates(S, Graph)
        for s in S:
            del Graph[s]
            for g in Graph:
                if s in Graph[g]:
                    Graph[g].remove(s)
            BigS.add(s)
        w += 1
    print(Graph)
    return len(BigS)



def WA4(SP, T, W): #algorithm for best fit decreasing

    nodepairs = list(SP.keys())
    G={} #dictionary to hold the wavelengths

    waveLengthsAssigned = {}
    for w in range(W):
        waveLengthsAssigned[w] = []

    nodepairs.sort(key=lambda x: len(SP[x])) #sort the node pairs in non decreasing order
    for nodepair in nodepairs:
        requests = T[nodepair[0]][nodepair[1]]
        path = SP[nodepair]
        for r in range(requests):
            #try to find fit into the best (tightest) bin, if not create a new bin
            bins = list(G.keys())
            bins.sort(key=lambda x: len(G[x])) # sort the bins according to their remaining capacity
            fitted = False
            for wbin in bins:
                #check if path fits into bin
                if pathFitsIntoBin(path,G[wbin]):
                    clearPathFromBin(path, G[wbin])
                    waveLengthsAssigned[wbin].append(nodepair)
                    fitted=True
                    break
            if not fitted: #open a new bin
                if getBinLength(G) < W:
                    newid = createNewBin(G, SP)
                    clearPathFromBin(path, G[newid])
                    if newid not in waveLengthsAssigned:
                        waveLengthsAssigned[newid] = []
                    waveLengthsAssigned[newid].append(nodepair)

    maxNumberOfRequests=0
    for i in range(W):
        maxNumberOfRequests += len(waveLengthsAssigned[i])
    #print(waveLengthsAssigned)
    return maxNumberOfRequests



def WA5(SP, T, W):
    nodepairs = list(SP.keys())
    G={} #dictionary to hold the wavelengths

    waveLengthsAssigned = {}
    for w in range(W):
        waveLengthsAssigned[w] = []

    nodepairs.sort(key=lambda x: len(SP[x])) #sort the node pairs in non decreasing order
    for nodepair in nodepairs:
        requests = T[nodepair[0]][nodepair[1]]
        path = SP[nodepair]
        for r in range(requests):
            #try to find fit into the first avilable bin, if not create a new bin
            bins = list(G.keys())
            fitted = False
            for wbin in bins:
                #check if path fits into bin
                if pathFitsIntoBin(path,G[wbin]):
                    clearPathFromBin(path, G[wbin])
                    waveLengthsAssigned[wbin].append(nodepair)
                    fitted=True
                    break
            if not fitted: #open a new bin
                if getBinLength(G) < W:
                    newid = createNewBin(G, SP)
                    clearPathFromBin(path, G[newid])
                    if newid not in waveLengthsAssigned:
                        waveLengthsAssigned[newid] = []
                    waveLengthsAssigned[newid].append(nodepair)

    maxNumberOfRequests=0
    for i in range(W):
        maxNumberOfRequests += len(waveLengthsAssigned[i])
    #print(waveLengthsAssigned)
    return maxNumberOfRequests

def H1SolveRWA(filename, W):
    V, L, T = gsolve.parseFile(filename)
    start_time = time.time()
    SPs_sd = gsolveSP.AllSPs(filename)
    SP_sd = {}
    for key in SPs_sd.keys():
        SP_sd[key] = SPs_sd[key][0]
    t1 = time.time() - start_time
    start_time = time.time()
    m = WA1(SP_sd, T, W)
    t2 = time.time() - start_time
    print("m", m, "time1:", t1, "time2:", t2, "total time:", t1+t2)
    return m

def H2SolveRWA(filename, W):
    V, L, T = gsolve.parseFile(filename)
    start_time = time.time()
    SPs_sd = gsolveSP.AllSPs(filename)
    SP_sd = {}
    for key in SPs_sd.keys():
        SP_sd[key] = SPs_sd[key][0]
    t1 = time.time() - start_time
    start_time = time.time()
    m = WA2(SP_sd, T, W)
    t2 = time.time() - start_time
    print("m", m, "time1:", t1, "time2:", t2, "total time:", t1+t2)
    return m

def H3SolveRWA(filename, W):
    V, L, T = gsolve.parseFile(filename)
    start_time = time.time()
    SPs_sd = gsolveSP.AllSPs(filename)
    SP_sd = {}
    for key in SPs_sd.keys():
        SP_sd[key] = SPs_sd[key][0]
    t1 = time.time() - start_time
    start_time = time.time()
    m = WA3(SP_sd, T, W)
    t2 = time.time() - start_time
    print("m", m, "time1:", t1, "time2:", t2, "total time:", t1+t2)
    return m

def H4SolveRWA(filename, W):
    V, L, T = gsolve.parseFile(filename)
    start_time = time.time()
    SPs_sd = gsolveSP.AllSPs(filename)
    SP_sd = {}
    for key in SPs_sd.keys():
        SP_sd[key] = SPs_sd[key][0]
    t1 = time.time() - start_time
    start_time = time.time()
    m = WA4(SP_sd, T, W)
    t2 = time.time() - start_time
    print("m", m, "time1:", t1, "time2:", t2, "total time:", t1+t2)
    return m

def H5SolveRWA(filename, W):
    V, L, T = gsolve.parseFile(filename)
    start_time = time.time()
    SPs_sd = gsolveSP.AllSPs(filename)
    SP_sd = {}
    for key in SPs_sd.keys():
        SP_sd[key] = SPs_sd[key][0]
    t1 = time.time() - start_time
    start_time = time.time()
    m = WA5(SP_sd, T, W)
    t2 = time.time() - start_time
    print("m", m, "time1:", t1, "time2:", t2, "total time:", t1+t2)
    return m

# print(H1SolveRWA("checkpoint2file.txt",5))
# print(H2SolveRWA("checkpoint2file.txt",5))
#print(H3SolveRWA("checkpoint2file.txt",5))
# print(H4SolveRWA("checkpoint2file.txt",5))
# print(H5SolveRWA("checkpoint2file.txt",5))
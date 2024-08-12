import GurobiSolveRWA_Group11 as gsolve
import math
from gurobipy import *


def GurobiSPsSolveRWA(filename, W):
    ## This would be the input .txt file
    node_list, link_list , traffic_matrix = gsolve.parseFile(filename)
    link_num = len(link_list )
    request_list = traffic_matrix
    # W
    wavelength_num = W

    ## Solving Link formulation using Gurobi solver
    # SD
    request_pair = []
    request_dict = {}
    for source in node_list:
        for destination in node_list:
            if request_list[source][destination] > 0:
                request_dict[(source, destination)] = request_list[source][destination]
                request_pair.append((source, destination))

    request_num = len(request_dict)

    def listdic(LL, NL):
        LD = {}
        for i in range(len(NL)):
            childs = []
            for j in LL:
                if i == j[0]:
                    childs.append(j[1])
                LD[i] = childs
        return LD

    def SDenum(T):
        SDlist = []
        for i in range(len(T)):
            for j in range(len(T[i])):
                SD = []
                if T[i][j] > 0:
                    SD.append(i)
                    SD.append(j)
                    SDlist.append(SD)
        return SDlist



    def findLink(link_list, s, d):
        if [s, d] in link_list:
            return link_list.index([s, d])
        else:
            return link_list.index([int(s), int(d)])





    SP = AllSPsH(filename)

    listdic(link_list, node_list)
    SDenum(request_list)
    #allPaths = findallpaths(SDs, LD)
    allPaths = gsolve.AllPathsNodes(filename)
    pathSD = {}

    
    for sd in allPaths.keys():
        indexno = 0
        pathSD[sd] = []
        for psd in allPaths[sd]:
            pathSD[sd].append(indexno)
            indexno += 1

    Gamma = []
    
    for p in SP:
        g = [0 for x in link_list]
        for i in SP[p]:
            g[i] = 1
#        for i in range(len(p) - 1):
#            index = findLink(link_list, p[i], p[i + 1])
#            g[index] = 1
        Gamma.append(g)

    path_num = len(SP)


    Omega = list(range(5))

    # Create optimization model
    m = Model('RWA')
    # Create variables
    x = m.addVars(wavelength_num, path_num, vtype=GRB.BINARY, name="x")

    m.Params.LogToConsole = 0

    m.setObjective((quicksum(x[i, j] for i in range(wavelength_num) for j in range(path_num))), GRB.MAXIMIZE)

    m.addConstrs((quicksum(x[i, j] * Gamma[j][k] for j in range(path_num)) <= 1 for i in range(wavelength_num) for k in
                  range(link_num)), name="Wavelength conflict")

    m.addConstrs((quicksum(x[j, k] for j in range(wavelength_num) for k in pathSD[request_pair[i]]) <= request_dict[
        request_pair[i]] for i in range(request_num)), name="Demand")

    m.optimize()
#    for v in m.getVars():
#        print('%s %g' % (v.VarName, v.X))
#        print('Obj: %g' % m.ObjVal)
    return m.ObjVal

def heap_pop(heap): # given a heap, sets the first index to be the last index, deletes the last heap index and returns the initial first index
    p = heap[0]
    heap[0] = heap[len(heap)-1]
    del(heap[len(heap)-1])
    return p

def heap_swimup(heap,index): # swims the item in a heap upwards, swapping it until there is no larger value in that heap
    parent = int((index-1)/2)
    while parent>=0:
        if heap[parent][0]>heap[index][0]:
            heap[index],heap[parent] = heap[parent],heap[index]
            index=parent
            parent = int((index - 1) / 2)
        else:
            break

def heap_sinkdown(heap,index): # sinks the item in a heap downwards, similar to how mergesort works
    while index < len(heap): # while the index given is less than the total length of the heap, it keeps going
        leftchild = 2 * index + 1 # the left child is 2*index+1
        rightchild = 2 * index + 2 # the right child is 2*index+2
        if heap[index][0]>heap[leftchild][0]: # if the 0th member of the index is greater than the 0th member of the left child, it will set a tuple (index,leftchild) and a tuple (leftchild,index)
            heap[index],heap[leftchild] = heap[leftchild],heap[index]
            index=leftchild # sets the index as the left child
        elif heap[index][0]>heap[rightchild][0]: # if the 0th member of the index is greater than the 0th member of the right child, given that it's not greater than the 0th member of the left child, it will set the same tuples as for leftchild
            heap[index],heap[rightchild] = heap[rightchild],heap[index]
            index=rightchild
        else:
            break

def heap_insert(heap,value): # main aspect of the heap function. basically sorts an array based on prioritization using swimup and sinkdown.
    if len(heap)==0:
        heap.append(value)
        return
    for i in range(len(heap)):
        if heap[i][1]==value[1]:
            oldvalue = heap[i][0]
            heap[i][0] = value[0]
            if oldvalue>value[0]:
                heap_swimup(heap,i)
            elif oldvalue<value[0]:
                heap_sinkdown(heap,i)
            return

    heap.append(value)
    heap_swimup(heap,len(heap)-1)

def getAdjacencyList(V,L): # takes in link list [[0,1],[1,2],[2,5],[5,4],[4,3],[3,0],[3,2],[2,5],[1,0],[2,1],[5,2],[4,5],[3,4],[0,3],[2,3],[5,2]]
    adjList={}
    for v in V:
        adjList[v] = set()
    for s,d in L:
        adjList[s].add(d)
    for v in V:
        adjList[v] = list(adjList[v])
    return adjList # creates a list of all of the adjacent nodes, for example for node 0, it is adjacent to 1 and 3 so it would be {0: [1,3]}


def shortestPath(V,L,s,adjacenyList): # Takes in link list, the adjacency list, node list and S (which is the index of the node that the shortest path is from, for example, for node 3 it finds the shortest path, which could be [3,0] or [3,6])
    dist={}
    prev={}
    for v in V:
        dist[v] = math.inf # the infinity implies distance, if the distance is infinity it won't be chosen compared to any other distance
        prev[v] = -1 # -1 for the prev node means that there is no path from the previous node
    dist[s] = 0
    heap=[]
    heap_insert(heap, [0,s])
    while len(heap)>0:
        p=heap_pop(heap)[1]
        for neighbor in adjacenyList[p]:
            distance = dist[p] +1
            if distance<dist[neighbor]:
                dist[neighbor]=distance
                prev[neighbor]=p
                heap_insert(heap,[distance,neighbor])
    sPs = {}
    for v in V:
        if prev[v]!=-1:
            sPs[v]=[]
            to_node = v
            from_node=prev[to_node]
            while from_node!=-1:
                linkid = L.index([from_node,to_node])
                sPs[v].insert(0,linkid)
                to_node = from_node
                from_node = prev[to_node]
    return sPs

def SDList(T ):
    SDlist = [] # SD is the set of all node pairs that have a connection request
    for i in range(len(T)):
        for j in range(len(T[i])):
            SD = []
            if T[i][j] > 0: # if the traffic is bigger than 0, it will create a connection request in the SDlist
                SD.append(i)
                SD.append(j)
                SDlist.append(SD)
    return SDlist # creates a list of all the pending requests, given that a request is greater than 0 example: [[0,1], [0,2], [0,3], [0,4]] means that there is a request to go from node 0 to 1, 0 to 2, 0 to 3 and 0 to 4.


def AllSPsH(filename):
    V, L, T = gsolve.parseFile(filename)
    SDs = SDList(T )
    ShortestPaths={}
    SP={}
    adjacenyList =getAdjacencyList(V,L)
    for sd in SDs:
        from_node,to_node = sd # from 0 to 1
        if from_node in ShortestPaths: # if 0 is in shortest paths
            SP[(from_node,to_node)] = ShortestPaths[from_node][to_node]
        else: # if 0 is not in the shortest paths
            ShortestPaths[from_node] = shortestPath(V,L,from_node,adjacenyList)
            SP[(from_node, to_node)] = ShortestPaths[from_node][to_node]
    return SP
def AllSPs(filename):
    V, L, T = gsolve.parseFile(filename)
    SDs = SDList(T )
    ShortestPaths={}
    SP={}
    adjacenyList =getAdjacencyList(V,L)
    for sd in SDs:
        from_node,to_node = sd # from 0 to 1
        if from_node not in ShortestPaths: # if 0 is in shortest paths
            ShortestPaths[from_node] = shortestPath(V,L,from_node,adjacenyList)
        if to_node in ShortestPaths[from_node]:
            SP[(from_node, to_node)] = ShortestPaths[from_node][to_node]
    for i in SP:
        newlist = []
        for linkid in SP[i]:
            newlist .append((linkid, L[linkid][0],L[linkid][1 ]))
        SP[i] = [newlist]
    return SP
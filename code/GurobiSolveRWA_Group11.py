
import json
from gurobipy import *

def GurobiLinkSolveRWA(filename, W):
    node_list, link_list , traffic_matrix = parseFile(filename)
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

    # Generate delta values

    deltaplus = {}
    deltaminus = {}
    for link_id, link in enumerate(link_list):
        if link[0] in deltaplus:
            deltaplus[link[0]].add(link_id)
        else:
            deltaplus[link[0]] = set([link_id])
        if link[1] in deltaminus:
            deltaminus[link[1]].add(link_id)
        else:
            deltaminus[link[1]] = set([link_id])

    # Build Model & variables

    model = Model("RWA")
    x = model.addVars(request_num, link_num, wavelength_num, vtype=GRB.BINARY, name="x")
    model.Params.LogToConsole = 0

    # Objective function (1.a): Maximize the number of granted requests

    model.setObjective((quicksum(
        x[i, j, k] for i in range(request_num) for j in deltaplus[request_pair[i][0]] for k in range(wavelength_num))),
                       GRB.MAXIMIZE)

    # Constraints

    # Constraint (1.b): Avoid wavelength conflict
    model.addConstrs(
        (quicksum(x[i, j, k] for i in range(request_num)) <= 1 for j in range(link_num) for k in range(wavelength_num)),
        name="Wavelength conflict")

    # Constraint (1.c): Wavelength continuity
    model.addConstrs(
        ((quicksum(x[i, j, k] for j in deltaplus[v]) - quicksum(x[i, j, k] for j in deltaminus[v])) == 0 for k in
         range(wavelength_num) for i in range(request_num) for v in
         (node_list - set([request_pair[i][0], request_pair[i][1]]))), name="wavelength_continuity")

    # Constraint (1.d): No loop
    model.addConstrs(
        (quicksum(x[i, j, k] for j in deltaminus[request_pair[i][0]] for k in range(wavelength_num)) == 0 for i in
         range(request_num)), name="No_loop1")
    model.addConstrs(
        (quicksum(x[i, j, k] for j in deltaplus[request_pair[i][1]] for k in range(wavelength_num)) == 0 for i in
         range(request_num)), name="No_loop2")

    # Constraint (1.e): Demand
    model.addConstrs((quicksum(x[i, j, k] for j in deltaplus[request_pair[i][0]] for k in range(wavelength_num)) <=
                      request_dict[request_pair[i]] for i in range(request_num)), name="Demand")

    # Solve the model
    model.optimize()
#    for i in range(request_num):
#        for j in range(link_num):
#            for k in range(wavelength_num):
#                if x[i, j, k].x > 0:
#                    print(x[i, j, k].varName)

    return model.ObjVal

def GurobiPathSolveRWA(filename, W):
    node_list, link_list , traffic_matrix = parseFile(filename)
    link_num = len(link_list )
    request_list = traffic_matrix

    # W
    wavelength_num = W

    # Solving path formulation of provided instance with Gurobi Solver

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


    listdic(link_list, node_list)
    SDenum(request_list)
    #allPaths = findallpaths(SDs, LD)
    allPaths = AllPathsNodes(filename)
    P = []
    pathSD = {}
    #print(allPaths)
    indexno = 0
    for sd in allPaths.keys():
        pathSD[sd] = []
        for psd in allPaths[sd]:
            pathSD[sd].append(indexno)
            indexno += 1
            P.append(psd)
    #print(P)
    #print(pathSD)
    Gamma = []
    for p in P:
        g = [0 for x in link_list]
        for i in range(len(p) - 1):
            index = findLink(link_list, p[i], p[i + 1])
            g[index] = 1
        Gamma.append(g)
    #print(Gamma)

    path_num = len(P)

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
    return m.ObjVal

def parseFile(filename):
    file1 = open(filename)
    count = 0
    for line in file1.readlines():
        count += 1
        if count == 1:
            node_num = int(line.strip())
        elif count == 2:
            link_num = int(line.strip())
        elif count == 3:
            a = line.strip()
            V = set(json.loads(a))
        elif count == 4:
            a = line.strip()
            L = json.loads(a)
        elif count == 5:
            a = line.strip()
            T =json.loads(a)
    file1.close()
    return V,L,T


def getAdjacencyList(V,L): # takes in link list [[0,1],[1,2],[2,5],[5,4],[4,3],[3,0],[3,2],[2,5],[1,0],[2,1],[5,2],[4,5],[3,4],[0,3],[2,3],[5,2]]
    adjList={}
    for v in V:
        adjList[v] = set()
    for s,d in L:
        adjList[s].add(d)
    for v in V:
        adjList[v] = list(adjList[v])
    return adjList # creates a list of all of the adjacent nodes, for example for node 0, it is adjacent to 1 and 3 so it would be {0: [1,3]}


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


def AllPathsNodes(filename):
    _,n = AllPathsH(filename)
    return n

def AllPaths(filename):
    l,_ = AllPathsH(filename)
    return l

#this function returns the outgoing links as a list from a node (from_node)
def findOutgoingLinksFromNode(from_node,L):
    outGoingLinks=[]
    linkIndex=0
    for source,destination in L:
        if source==from_node:
            outGoingLinks.append(linkIndex)
        linkIndex+=1
    return outGoingLinks

#function finds all paths from the source node to the destination node, given a list of links
#uses the DFS logic to traverse the graph
def AllPathsSourcetoDestination(source,destination,L):

    #the list to store the paths in terms of links
    #path of links have this structure:  [ [linkindex, source of link, destination of link ] , [linkindex, source of link, destination of link ], ..  ]
    pathsSourcetoDestinationLinks=[]

    # the list to store the paths in terms of nodes
    #path of nodex have this structure:  [ nodenumber, nodenumber,nodenumber, ... ]
    pathsSourcetoDestinationNodes = []

    outgoingLinksFromSource = findOutgoingLinksFromNode(source,L)


    #linkStack is a list of lists where
    # each inner list has the form of : [link index to be processed, path of links , path of nodes]
    linkStack = []

    # for every outgoing link from the inital source node
    # append to the linkStack as   [link index to be processed, path of links , path of nodes]

    for linkIndex in outgoingLinksFromSource:
        s,d = L[linkIndex]
        linkStack.append([linkIndex,[linkIndex],[s,d]])

    #continue as long as there are remaining links in the linkStack to be processed
    while len(linkStack)>0:
        #Pop a link from the stack
        linkIndex,linkpath,nodepath = linkStack.pop(0)
        #linkDestination is the destination node of the link
        _,linkDestination = L[linkIndex]

        # if destination is reached update the path lists (pathsSourcetoDestinationLinks, pathsSourcetoDestinationNodes)
        if destination==linkDestination:
            mlinkpath=[]
            #convert linkpath in to this form [ [linkindex, source of link, destination of link ] , [linkindex, source of link, destination of link ], ..  ]
            for ll in linkpath:
                mlinkpath.append([ll,L[ll][0],L[ll][1]])
            pathsSourcetoDestinationLinks.append(mlinkpath)
            pathsSourcetoDestinationNodes.append(list(nodepath))
        else:
            outgoingLinksFromDestination = findOutgoingLinksFromNode(linkDestination, L)
            #for every outgoing link from the current destination node
            for linkIndex in outgoingLinksFromDestination:
                s,d = L[linkIndex]
                #if the links end node has not been visited yet add this link to the linkStack
                if d not in nodepath:
                    linkpathCopy = list(linkpath)
                    linkpathCopy.append(linkIndex)
                    nodepathCopy = list(nodepath)
                    nodepathCopy.append(d)
                    linkStack.append([linkIndex, linkpathCopy,nodepathCopy])

    return pathsSourcetoDestinationLinks, pathsSourcetoDestinationNodes


def AllPathsH(filename):

    V, L, T = parseFile(filename)
    SDs = SDList(T )
    Links={}
    Nodes = {}
    #calculate path for every node pair in SDs
    for sd in SDs:
        from_node,to_node = sd # from 0 to 1
        l,n = AllPathsSourcetoDestination(from_node,to_node,L)
        Links[(from_node,to_node)] = l
        Nodes[(from_node, to_node)] = n


    return Links,Nodes
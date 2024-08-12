import time
import numpy as np
from numpy import random
import GurobiSolveRWA_Group11 as gsolve
import HeuristicSolveRWA_Group11 as genericsolve
import matplotlib.pyplot as plt

def generateInstance_Group11(filename, lamb, omega, i): # generates an instance based on a basefile that is provided
    with open(filename) as f: # opens filename
        content = f.readlines()
        print(content)
        content = [x.strip() for x in content]

    def clean(network): # cleans the file to just be the requests and nodes
        data = []
        n = 0
        m = 0
        for i in network:
            if '<node' in i[0]:
                data.append(i[0])
                n += 1
            elif '<edge' in i[0]:
                data.append(i[0])
                m += 1
        cleaned = [e.split("\"") for e in data]
        return cleaned

    def gatherdetails(cleanednetwork): # assigns variables
        V = []
        L = []
        for i in cleanednetwork:
            if "node" in i[0]:
                V.append(int(i[1]))
            else:
                L.append([int(i[1]), int(i[3])])
                L.append([int(i[3]), int(i[1])])
        n = len(V)
        m = len(L)
        return n, m, V, L

    all_content = [c.split(',') for c in content]

    def genTraffic(n, m, V, L, lam, seed): # generates an nxn traffic matrix
        np.random.seed(seed)
        W = round(random.uniform(2, omega)) # generates a W using a uniform distribution
        randT = random.poisson(lam=lam, size=n * n) # generates a randomized traffic matrix based off of the lambda given
        T = []
        for i in range(n + 1):
            t = []
            for j in range(n):
                t.append(randT[i * j])
            T.append(t)
        T.pop(0)
        return [n, m, V, L, T] # returns n, m, V, L and T

    def instanceTxt(instance, id): # writes a txt file to be used in the following plots
        f = open("instance" + str(id) + ".txt", "w")
        for i in instance:
            f.write(str(i) + "\n")
        f.close

    n, m, V, L = gatherdetails(clean(all_content))

    instance = genTraffic(n, m, V, L, lamb, 63587)
    instanceTxt(instance, i)


def compLinkPath_Group11(filename, W): # computes time and objective values for parts 2, 3 and 4, specifically for the gurobi implementations
    timeInit = time.time()
    gsolve.GurobiPathSolveRWA(filename, W)
    timePath = time.time()-timeInit
    timeInit = time.time()
    gsolve.GurobiLinkSolveRWA(filename, W)
    timeLink = time.time()-timeInit
    return timeLink, timePath

def compGeneric_Group11(filename, W): # computes time and objective values for parts 2, 3 and 4, specifically for the WA1-5 algorithms used
    zexact = gsolve.GurobiPathSolveRWA(filename, W)
    timeInit = time.time()
    h1z = genericsolve.H1SolveRWA(filename, W)
    time1 = time.time()-timeInit
    timeInit = time.time()
    h2z = genericsolve.H2SolveRWA(filename, W)
    time2 = time.time()-timeInit
    timeInit = time.time()
    h3z = genericsolve.H3SolveRWA(filename, W)
    time3 = time.time()-timeInit
    timeInit = time.time()
    h4z = genericsolve.H4SolveRWA(filename, W)
    time4 = time.time()-timeInit
    timeInit = time.time()
    h5z = genericsolve.H5SolveRWA(filename, W)
    time5 = time.time()-timeInit
    dObj1 = (zexact - h1z) / zexact
    dObj2 = (zexact - h2z) / zexact
    dObj3 = (zexact - h3z) / zexact
    dObj4 = (zexact - h4z) / zexact
    dObj5 = (zexact - h5z) / zexact
    return [time1, time2, time3, time4, time5, dObj1, dObj2, dObj3, dObj4, dObj5]

def plot_2_G11(listLam, timePath, timeLink, i): # plots the graph for part 2
    strTemp = "Instance " + str(i + 1) + " Gurobi Function Running Time Comparisons"
    fig, ax = plt.subplots()
    plt.plot(listLam, timePath, label = "Path Solve")
    plt.plot(listLam, timeLink, label = "Link Solve")
    plt.xlabel("Lambda"), plt.ylabel("Running Time")
    ax.set_title(strTemp) # used for labelling and the legend
    plt.legend()
    plt.show()

def plot_3_G11(listLam, timePath, timeLink, timeList1, timeList2, timeList3, timeList4, timeList5, objList1, objList2, objList3, objList4, objList5, i): # plots the graph for part 3
    strTemp = "Instance " + str(i+1) + " Running Time Comparisons"
    fig, ax = plt.subplots()
    plt.plot(listLam, timePath, label="Path Solve")
    plt.plot(listLam, timeLink, label="Link Solve")
    plt.plot(listLam, timeList1, label="WA1")
    plt.plot(listLam, timeList2, label="WA2")
    plt.plot(listLam, timeList3, label="WA3")
    plt.plot(listLam, timeList4, label="WA4")
    plt.plot(listLam, timeList5, label="WA5")
    plt.xlabel("Lambda"), plt.ylabel("Running Time") # used for labelling and the legend
    ax.set_title(strTemp)
    plt.legend()
    plt.show()

    strTemp = "Instance " + str(i + 1) + "Objective Comparisons"
    plt.plot(listLam, objList1, label="WA1")
    plt.plot(listLam, objList2, label="WA2")
    plt.plot(listLam, objList3, label="WA3")
    plt.plot(listLam, objList4, label="WA4")
    plt.plot(listLam, objList5, label="WA5")
    plt.xlabel("Lambda"), plt.ylabel("Objective Difference") # used for labelling and the legend
    ax.set_title(strTemp)
    plt.legend()
    plt.show()

def plot_4_G11(listLam, timeDif1, timeDif2, timeDif3, timeDif4, timeDif5, objDif1, objDif2, objDif3, objDif4, objDif5, i): # plots the graph for part 4
    strTemp = "Instance " + str(i + 1) + " Running Time Comparisons"
    fig, ax = plt.subplots()
    plt.plot(listLam, timeDif1, label="WA1")
    plt.plot(listLam, timeDif2, label="WA2")
    plt.plot(listLam, timeDif3, label="WA3")
    plt.plot(listLam, timeDif4, label="WA4")
    plt.plot(listLam, timeDif5, label="WA5")
    plt.xlabel("Lambda"), plt.ylabel("Running Time Difference") # used for labelling and the legend
    ax.set_title(strTemp)
    plt.legend()
    plt.show()

    strTemp = "Instance " + str(i + 1) + "Objective Comparisons"
    plt.plot(listLam, objDif1, label="WA1")
    plt.plot(listLam, objDif2, label="WA2")
    plt.plot(listLam, objDif3, label="WA3")
    plt.plot(listLam, objDif4, label="WA4")
    plt.plot(listLam, objDif5, label="WA5")
    plt.xlabel("Lambda"), plt.ylabel("Objective Difference") # used for labelling and the legend
    ax.set_title(strTemp)
    plt.legend()
    plt.show()

def plotComparisons(): # plots all of the comparisons for the 6 instances used (they're arranged in increasing "complexity" as the number of nodes, and the size of the matrix increases)
    for i in range(1):
        listLam = []
        timePath, timeLink, timeList1, timeList2, timeList3, timeList4, timeList5, objList1, objList2, objList3, objList4, objList5, timeDif1, timeDif2, timeDif3, timeDif4, timeDif5, objDif1, objDif2, objDif3, objDif4, objDif5 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        for j in range(2, 101): # gets the objectives and time with the input variable being W (the number of wavelengths per node)
            listLam.append(j)
            strTemp = str(i) + ".txt"
            tempList = compLinkPath_Group11(strTemp, j)
            timePath.append(tempList[0]), timeLink.append(tempList[1])
            tempList = compGeneric_Group11(strTemp, j)
            timeList1.append(tempList[0]), timeList2.append(tempList[1]), timeList3.append(tempList[2]), timeList4.append(tempList[3]), timeList5.append(tempList[4]), objList1.append(tempList[5]), objList2.append(tempList[6]), objList3.append(tempList[7]), objList4.append(tempList[8]), objList5.append(tempList[9])
            timeMin = min(tempList[0:4])
            objMax = max(tempList[5:9])
            if timeMin != tempList[0]: # so that there isn't a zero error (division by 0)
                timeDif1.append((tempList[0]-timeMin)/(timeMin))
            else:
                timeDif1.append(1)
            if timeMin != tempList[1]:
                timeDif2.append((tempList[1]-timeMin)/(timeMin))
            else:
                timeDif2.append(1)
            if timeMin != tempList[2]:
                timeDif3.append((tempList[2]-timeMin)/(timeMin))
            else:
                timeDif3.append(1)
            if timeMin != tempList[3]:
                timeDif4.append((tempList[3]-timeMin)/(timeMin))
            else:
                timeDif4.append(1)
            if timeMin != tempList[4]:
                timeDif5.append((tempList[4]-timeMin)/(timeMin))
            else:
                timeDif5.append(1)
            objDif1.append((objMax-tempList[5])/(objMax+0.1)), objDif2.append((objMax-tempList[6])/(objMax+0.1)), objDif3.append((objMax-tempList[7])/(objMax+0.1)), objDif4.append((objMax-tempList[8])/(objMax+0.1)), objDif5.append((objMax-tempList[9])/(objMax+0.1))
        plot_2_G11(listLam, timePath, timeLink, i)
        plot_3_G11(listLam, timePath, timeLink, timeList1, timeList2, timeList3, timeList4, timeList5, objList1, objList2, objList3, objList4, objList5, i)
        plot_4_G11(listLam, timeDif1, timeDif2, timeDif3, timeDif4, timeDif5, objDif1, objDif2, objDif3, objDif4, objDif5, i)

plotComparisons()
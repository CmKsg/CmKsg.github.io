import random

import numpy as np
from bs4 import BeautifulSoup
from scipy.stats import poisson
import os


def squeeze_an_instance(fileName,sn,sl,filename):

    with open(fileName, 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "xml")
    b_nodes = Bs_data.find_all('node')

    nodes_dict = {}
    nodes_id = 0
    for node in b_nodes:
        id = node.get('id')
        nodes_dict[id] = nodes_id
        nodes_id += 1

    V = list(nodes_dict.values())
    L = []
    b_links = Bs_data.find_all('link')
    for link in b_links:
        linkid = link.get('id')
        source = link.find('source').text
        target = link.find('target').text
        additional_modules = link.find_all('addModule')
        for module in additional_modules:
            L.append([nodes_dict[source], nodes_dict[target]])
            L.append([nodes_dict[target], nodes_dict[source]])

    n = len(V)
    m = len(L)


    if n>sn and sn!=-1:

        for i in range(n-sn):
            vremoved = V.pop()
            L = list(filter(lambda x: x[0] != vremoved and x[1] != vremoved , L))

    n = len(V)
    m = len(L)

    if m>sl and sl!=-1:

        for i in range(m-sl):
            L.pop(random.randint(0,len(L)-1))

    n = len(V)
    m = len(L)



    Ttotal = poisson.rvs(mu=100 * n ** 2, size=1)[0]
    T = [[0 for x in range(n)] for x in range(n)]

    # we need to unifromly distribute Tbar over T matrix
    # there are n**2 - n  node pairs to make the distribution

    N = n ** 2 - n
    random_numbers_list = [np.random.rand() for i in range(N - 1)]
    random_numbers_list.append(0)
    random_numbers_list.append(1)
    random_numbers_list.sort()
    # print(len(random_numbers_list))

    index = 1
    for i in range(n):
        for j in range(n):
            if i != j:
                T[i][j] = int((random_numbers_list[index] - random_numbers_list[index - 1]) * Ttotal)
                index += 1


    f = open(filename + ".inout", "w")
    f.write(str(n) + "\n")
    f.write(str(m) + "\n")
    f.write(str(V) + "\n")
    f.write(str(L) + "\n")
    f.write(str(T) + "\n")

    f.close()

def generate_instances():
    rootdir = 'base-instances-xml'
    seed = 48151
    np.random.seed(seed)

    for subdir, dirs, files in os.walk(rootdir):
         for file in files:
              fileName =  os.path.join(subdir, file)

              with open(fileName, 'r') as f:
                  data = f.read()

              Bs_data = BeautifulSoup(data, "xml")
              b_nodes = Bs_data.find_all('node')

              nodes_dict = {}
              nodes_id = 0
              for node in b_nodes:
                  id = node.get('id')
                  nodes_dict[id] =nodes_id
                  nodes_id+=1

              V = list(nodes_dict.values())
              L=[]
              b_links = Bs_data.find_all('link')
              for link in b_links:
                  linkid = link.get('id')
                  source = link.find('source').text
                  target = link.find('target').text
                  additional_modules = link.find_all('addModule')
                  for module in additional_modules:
                      L.append([nodes_dict[source], nodes_dict[target]])
                      L.append([nodes_dict[target], nodes_dict[source]])

              n = len(V)
              m = len(L)


              Ttotal = poisson.rvs(mu=100*n**2, size=1)[0]
              T = [[0 for x in range(n)] for x in range(n)]

              # we need to unifromly distribute Tbar over T matrix
              # there are n**2 - n  node pairs to make the distribution

              N= n**2 - n
              random_numbers_list =[np.random.rand() for i in range(N-1)]
              random_numbers_list .append(0)
              random_numbers_list .append(1)
              random_numbers_list.sort()
              #print(len(random_numbers_list))

              index=1
              for i in range(n):
                  for j in range(n):
                      if i!=j:
                          T[i][j]=int((random_numbers_list[index] -random_numbers_list[index-1])*Ttotal)
                          index+=1

              basename = os.path.basename(fileName)

              f = open("generated-instances/"+basename+".inout", "w")
              f.write(str(n)+"\n")
              f.write(str(m)+"\n")
              f.write(str(V)+"\n")
              f.write(str(L)+"\n")
              f.write(str(T)+"\n")


              f.close()

for v in range(10,160,5):
    squeeze_an_instance("base-instances-xml/brain/brain.xml",v,70,"V-files/"+str(v))

for l in range(100,1600,100):
    squeeze_an_instance("base-instances-xml/brain/brain.xml",150,l,"L-files/"+str(l))

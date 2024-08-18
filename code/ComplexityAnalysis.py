import SolveRWA as solveRWA
import os
import matplotlib.pyplot as plt


algorithm_no=2
#
# #for Algorithm 5, fix w=10 and L=70 , these are the files under V-files directory
rootdir = 'V-files'
V_x =[]
V_y = []
w=1

for subdir, dirs, files in os.walk(rootdir):
     for file in files:
          fileName =  os.path.join(subdir, file)
          with open(fileName, 'r') as f:
              V = int(f.readline())
              L = int(f.readline())
          f.close()
          V_x.append(V)

          m,t = solveRWA.SolveRWA(fileName,algorithm_no,w)
          V_y.append(t)

plt.figure()
plt.scatter(V_x,V_y)
plt.xlabel("|V|")
plt.ylabel("Computation Time (s)")
plt.title("Computation Time vs |V| (|L| fixed at 5, |omega| fixed at 1))")
plt.show()
#
#
#for Algorithm 5, fix w=10 and V=150 , these are the files under V-files directory
rootdir = 'L-files'
L_x =[]
L_y = []
w=10

for subdir, dirs, files in os.walk(rootdir):
     for file in files:
          fileName =  os.path.join(subdir, file)
          with open(fileName, 'r') as f:
              V = int(f.readline())
              L = int(f.readline())
          f.close()
          L_x.append(L)

          m,t = solveRWA.SolveRWA(fileName,algorithm_no,w)
          L_y.append(t)

plt.figure()
plt.xlabel("|L|")
plt.ylabel("Computation Time (s)")
plt.title("Computation Time vs |L| (|V| fixed at 150, |omega| fixed at 10)")
plt.scatter(L_x,L_y)
plt.show()

# for Algorithm 5,  use brain.xml.inout under generated-instances directory v= 161 and l=1328
W_x =[]
W_y = []
for w in range(1,30):
    W_x .append(w)
    m, t = solveRWA.SolveRWA("generated-instances/brain.xml.inout", algorithm_no, w)
    W_y.append(t)

plt.figure()
plt.xlabel("|omega|")
plt.ylabel("Computation Time (s)")
plt.title("Computation Time vs |omega| (|V| fixed at 161, |L| fixed at 1328)")
plt.scatter(W_x,W_y)
plt.show()


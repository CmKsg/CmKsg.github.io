---
title: "RWA Analysis of Fiber Network"
excerpt: "An algorithm design and numerical methods project, where several algorithms were developed and tested on various fiber networks to optimize fiber traffic. <br/>"
collection: portfolio
---
## Summary
For this project, the routing wavelength problem was tackled, which is the optimization of assignment of lightpaths to a set of connection requests in an optic network. This analysis was done through the use of two traditional integer programs and several heuristic algorithms.

## Methodology
- The first method, which is the link-formulation integer program (IP), was generated. This IP maximizes the number of granted requests in the network, while ensuring that no constraints regarding transmission are violated and no loops are created.
- The second method, which is the path-formulation IP, was generated. This IP is similar to link-formulation, however first finds the set of all possible paths before the IP is run. The IP therefore maximizes the number of granted requests in the network, while only ensuring that no transmission constraints are violated.
The heuristic methods included:
1) The Two-Phase Method
2) First-Fit Algorithm
3) First-Fit Decreasing Algorithm
4) Best-Fit Algorithm
5) Best-Fit Decreasing Algorithm
6) Recursive Largest First
- These algorithms were evaluated against one-another based on the criteria of maximum number of connections granted and runtime. First-fit decreasing was deemed as the optimal algorithm for use.

# Details

## Deterministic Influence Diagram

The RWA problem refers to the assignment of lightpaths to a set of connection requests in an optical network. The purpose of this report is to determine the efficiency of several heuristic algorithms with their solution time of the RWA problem as well as their optimal values.

The variables considered in the RWA problem look at the different aspects of an optical network, such as; the nodes, the links, availability of wavelengths, traffic within the network and the set of nodes that are included in that traffic. A more formal definition of these variables is:

<br/><img src="/images/Portfolio3/RWAVariables&Constraints.png">

For the model to be complete, the decision variables used have to meet the following primary conditions to have a feasible solution:

• _Wavelength Continuity Condition_ - A lightpath uses the same wavelength from its source through to its destination.
• _No Wavelength Conflict_ - No two wavelengths with a common link on their path share the same wavelength.

Using the constraints and variables defined, an optimal provisioning plan is generated. The optimal provision plan would be a feasible plan that has the optimal number of connection requests granted in the network that is defined.

## Link Formulation

Link formulation approaches the problem from sets of incoming and outgoing links of node v. It is defined as an integer programming problem, which maximizes the number of granted requests in the network with the binary variable x.

**Integer Program**
<br/><img src="/images/Portfolio3/LinkFormulation.png">

## Path Formulation

Path formulation approaches the problems with a different perspective. It initially runs an algorithm that defines all possible paths that can be found for the optical network, and then the link formulation IP is solved.

**All paths**:
**Input**: SDs
<pre>
  for sd in SDs:
    if sd has outgoing and incoming links:
      find pathTaken (sourceToDestination (link) list sourceToDestination (node)list)
        pathTaken has the links and nodes taken in the specific path
      append pathTaken to allPaths (source to destination link, source to destination node)
return allPaths
</pre>

**Integer Program**

<br/><img src="/images/Portfolio3/PathFormulation.png">

### Shortest Path Algorithm (Depth-First Search: Heap Queue)

In order to run the heuristic algorithms to be presented later, a shortest path algorithm had to be run. To find these shortest paths, a modified version of the heap-queue algorithm was implemented. The heap-queue algorithm uses a heap-queue, which is a type of tree structure where the parent node has a lower value than its child node.

Since the parent nodes always have lower values than their child node, the heap at the top of the tree, will always be the shortest path possible. The shortest path is found by using a method similar to heap-sort, where higher values are sunk-down in the tree and lower values swim-up. The bottom value is removed from the heap until there are no possible higher values left and the remainder is determined to be the shortest path. This method was implemented due to its efficiency in terms of running time. The algorithm’s theoretical complexity is O(logN), therefore even as the number of paths increases, the algorithm continues to run efficiently.

**ShortestPath:**
<pre>
  Insert a node into the heap (binary tree) from the SDs
  Searches for another node that has a shorter path
  Swaps the node with the node that has the shorter path
    Swimup: Does this through divide and conquer
      Divides the index by 2 of the parent node until there is no longer a larger path in the heap
    Sinkdown: Does this through divide and conquer
      Multiplies the index by 2 for the left child and the right child until there is no shorter path in the heap
    Pop: Removes the last member on the heap, as it has the longest path
  Repeats until there is one member in the heap
  Returns the shortest path of the node
</pre> 

While the Depth-First search is built on the process detailed above, the variance in this algorithm starts with the use of the pop function to remove items from the stack, as opposed to the heapsink and heapswim functions used earlier. As paths are explored, the pop function is used to remove the node from the stack. If a destination is not already on the path, it is appended to the stack to ensure no loops are created within the network.

The function designed to find all paths takes the set of all node pairs that have a connection request as well as LD, to determine all paths in the network which satisfy the four above-noted constraints set forth. The output of the function returns a list of all paths in the network.

## Heuristic Methods

Heuristic methods are algorithms that produce a feasible solution to the problem. They allow for a lower running time, but may result in less than the actual optimal value.

### Two-Phase Method

The Two-phase method solves a linear programming problem with artificial variables in standard form with the input of a linear program in standard inequality form. In general, the output of the two-phase method can result in one of the following 3 options:

1. Production of an optimal solution of the linear program.
2. Production of a parametric solution of the linear program, supporting that the program is unbounded. The value of the objective function can tend to +∞.
3. Confirmation that the linear program is infeasible as the constraints cannot be satisfied simultaneously.

The initial phase of the method seeks to eliminate the artificial variables from the basis by assigning values of 0 to the original variables and values of -1 to the artificial variables. The output of the first phase is a basic feasible solution used for the second phase. The latter phase introduces the original objective function and works with the simplex algorithm to determine the optimal solution.

### Random Wavelength Assignment

The random wavelength assignment algorithm is a greedy algorithm that assigns the shortest paths randomly.

**Pseudocode**:
**Inputs**: shortestPaths list (generated with R), traffic matrix, wavelength requests
<pre>
Greedy
  Iterates through each request in the traffic matrix for each nodepair (sorted in accordance to the 2 ∗ (assignednodenumber) + 1
  Assigns each link in a greedy manner to the wavelengths available
  Randomly assigns these links
</pre> 

### First-Fit Algorithm

The First-Fit algorithm is a greedy algorithm which operates on the notion of packing items into the first bin which can accommodate the item in question. It is greedy, as it only takes into account the immediate gain of packing an item, rather than the future gain of allocating a minimum number of bins.

New bins are created in the event that an item does not fit in the bins previously scanned. While this algorithm proves to improve computing and processing times due to its simplicity, it unfortunately sacrifices significant memory allocation which may create deficiencies of memory available for other required processes.

**Pseudocode**:
**Inputs**: shortestPaths list (generated with R), traffic matrix, wavelength requests
<pre>
Greedy
  Iterates through each request in the traffic matrix for each nodepair (sorted in accordance to the 2 ∗ (assignednodenumber) + 1
  Assigns each link in a greedy manner to the wavelengths available
  Assign these links in order
</pre> 
  

### First-Fit Decrease Algorithm

A greedy algorithm, very similar to the first-fit algorithm that initially sorts all items in decreasing order, and then runs the first-fit algorithm.

**Pseudocode**:
**Inputs:** shortestPaths list (generated with R), traffic matrix, wavelength requests
<pre>
Greedy
 Sorts the node pairs in non-decreasing order
 Creates a new bin
 Assigns a request into the bin with the least remaining capacity
   If no bins with enough remaining capacity, creates a new bin
   Remove path from the request list
 Returns the number of requests
</pre>

### Best-Fit Decreasing

A greedy algorithm, similar to the first-fit algorithm that sorts all items using the best fitting path bins, and optimizing the capacity of those bins.

**Pseudocode**:
**Inputs:** shortestPaths list (generated with R), traffic matrix, wavelength requests
<pre>
 Greedy
 Sorts the node pairs in non-decreasing order
 Creates a new bin
 Assigns a request into the bin with the least remaining capacity
  If no bins with enough remaining capacity, creates a new bin
  Remove path from the request list
 Returns the number of requests
</pre>

### Recursive Largest First

The Recursive Largest-First method follows a greedy approach in solving the NP-hard problem of coloring the vertices one at a time, while sequentially building color classes. Vertices and nodes can be used interchangeably to define the basis of network graph formation (RWA network). Specifically, they refer to locations within the network at which data transmissions can travel to or from.

As vertices within the network are traveled to/from, the vertices are coloured to indicate they have been selected in the routing. Subsequent independent sets of vertices not included in the initially determined routing are then construct a new color class to differentiate the route within the network. Within the created color class, the first vertex added is the one with the greatest number of uncoloured neighbors. Subsequent vertices are added to the class to ensure that they have a sufficient number of uncoloured neighbors such that they cannot be added to the created color class.

**Pseudocode**:
**Inputs**: shortestPaths list (generated with R), traffic matrix, wavelength requests
<pre>
 Constructs a graph with each nodepair representing a vertex in the graph
 Generates a partition of the vertices that represents a feasible coloring of the graph
 Adds vertices to the set
   The vertex with the highest number of neighboring vertices is added to the set
   Remove the vertex
   Repeat until no vertices are left
 Remove the set of vertices from the graph, if the graph still contains vertices, repeat step 2 and 3
 Returns the size of the set of vertices
</pre>

### Criteria Used for Comparison

The efficiency and performance of the algorithms used for this specific RWA problem rely on two primary analyses:

1. The number of connections granted by the algorithm
2. The runtime measured to produce the output of connections granted

The primary objective in the presented RWA problem is to maximize the number of granted connection requests. This was deemed the primary objective as maximizing the capacity of the telecommunications network by optimizing the number of connection requests granted will drive profits for the company in question. A greater number of connection requests granted directly translates into a higher number of customers who can be serviced on the network.

Network capacity alone does not provide the telecommunication company an accurate depiction of their industry competitiveness. To further evaluate the performance of each algorithm created the runtime will be measured as a key performance indicator of the algorithm designed. Throughout various stages of the algorithm use, comparing the runtime of each of the algorithms will allow a holistic and equitable comparison of the processing time required for the algorithm to produce its deemed optimal solution. Faster algorithms will allow the network to make back-end decisions and processes quicker, thus increasing the speed of services provided to the consumer. The combination of maximizing network capacity and optimizing runtimes will provide a vast and fast network thus providing an overall optimized network experience.

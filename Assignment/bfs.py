from Graph import *
import numpy
import matplotlib.pyplot as plt


from graph_reader import *
import time
""" BFS.
*this graph takes a graph and explore every node  starting 
from the current node provided as a 2nd argument. 
it basically traverse the nodes layer by layer."""

def BFS(graph,curr,target):
    path = []   
    
    visited=set()
    
    Q = []    
    Q.append(curr)
    visited.add(curr)
    
    while Q and curr!=target:
        
        curr = Q.pop(0)
        path.append(curr)

        for i in graph.verticies[curr]._nbrs:
            if i[0].name not in visited:                
                Q.append(i[0].name)
                visited.add(i[0].name)
                
                if i[0].name == target:
                    break
                
    return path   


# test BFS:

nodes = []
for v in g.verticies:
    nodes.append(v)

path_sum = 0

# take starting time
start_time = time.time()
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i !=j:
           path = BFS(g,nodes[i],nodes[j])
           path_sum += len(path)

# take ending time
end_time=time.time()

total_combination = (len(nodes)-1)*len(nodes)

print("\tAverage solution length = ",path_sum/total_combination)
print("\taverage time = ",(end_time-start_time)/total_combination)

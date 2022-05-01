import time
# from bonus import *

import matplotlib.pyplot as plt
from matplotlib import *
from Graph import *
from graph_reader import *
from queue import  PriorityQueue
"""Dijkstra function explores each node starting from the current given node  
   and return a tuple of 2 dictionaries.
             1. distance dictionary (to get optimal distance of every node)
             2. parent dictionary (to track the path)
     """
def Dijkstra(graph,curr,target):
    
    dist={}       
    parent= {}
    parent[curr]=None
    G = set()          
    explored=set()    
        
    for iv, (name, node) in enumerate(graph.verticies.items()):
        dist[name]=float('inf')
        G.add(node.name)
        
    # set initial node Distance to 0.
    dist[curr]=0     
    # queue
    Q = PriorityQueue()    
    Q.put((0,curr)) 
    
    while G and curr !=target: 
        
        curr = Q.get() 
        curr=curr[1]
                
        explored.add(curr) 
        if curr in G:
            G.remove(curr)        
          
        for tupl in graph.verticies[curr]._nbrs:
            if tupl[0].name not in explored: 
                if (dist[tupl[0].name]) > dist[curr] + float(tupl[1]):
                    dist[tupl[0].name] = dist[curr] + float(tupl[1])
                    parent[tupl[0].name]=curr
                    Q.put((dist[tupl[0].name],tupl[0].name))
           
    path = []
    
    while curr:
        path.append(curr)   
        curr=parent[curr]
        
    path=list(reversed(path))  
   
    return (path,dist)
    
   
    # test
    
nodes = []
for v in g.verticies:
    nodes.append(v)
path_sum=0

# starting time
start_time = time.time()
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i!=j:
            
            path = Dijkstra(g,nodes[j],nodes[i])
            path_sum += len(path)            # 

# ending time
end_time=time.time()

total_combination = (len(nodes)-1)*len(nodes)
print("\tAverage solution length = ",path_sum/total_combination)
print("\taverage time = ",(end_time-start_time)/total_combination)
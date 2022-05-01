# from bonus import *
from math import *
import time
from Graph import *
from graph_reader import *
from queue import  PriorityQueue
import time
import matplotlib.pyplot as plt
from matplotlib import *
from Graph import *
from graph_reader import *
from queue import  PriorityQueue

position = {}
f = open("huristic.txt","r")
lines = f.readlines()
for l in lines:
        ls=l.split(" ") 
        position[ls[0]]=(float(ls[1]),float(ls[2])) 
f.close()

def heuristic(a, b):
    
    #Degree to Corresponding radian.
    lon1 = radians(a[1])
    lon2 = radians(b[1])
    lat1 = radians(a[0])
    lat2 = radians(b[0])
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    d = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(d))    
    # Radius of earth (Km).
    r = 6371
      
    # calculate the result
    return(c * r)    


"""
    a_Star function explores each node starting from the current given node  
    and return a tuple of 2 dictionaries.
             1. distance dictionary (to get optimal distance of every node)
             2. parent dictionary (to track the path)
     """
     
def a_Star(g,curr,tatget):
    dist={}       
    parent= {}
    parent[curr]=None
    G = set()          
    explored=set()    
        
    for iter, (name, node) in enumerate(g.verticies.items()):
        dist[name]=float('inf')
        G.add(node.name)
    dist[curr]=0    
    Q = PriorityQueue()    
    Q.put((0,curr)) 
     
    
    while G and curr != tatget: 
        
        
        curr = Q.get() 
        curr=curr[1]
                
        explored.add(curr) 
        if curr in G:
            G.remove(curr)            
        
        for tupl in g.verticies[curr]._nbrs:
            if tupl[0].name not in explored: 
                h = heuristic(position[curr],position[tupl[0].name])
                if dist[tupl[0].name] > dist[curr] + float(tupl[1])+h:
                    dist[tupl[0].name] = dist[curr] + float(tupl[1])+h
                    parent[tupl[0].name]=curr
                    Q.put((dist[curr] + float(tupl[1])+h,tupl[0].name)) 
              
        
    path = []
    while curr:
        path.append(curr)   
        curr=parent[curr]
    path=list(reversed(path))
   
    return (path,dist)
      
        
nodes = []
for v in g.verticies:
    nodes.append(v)
path_sum = 0

# take starting time
start_time = time.time()
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i!=j:
            
            path = a_Star(g,nodes[j],nodes[i])
            path_sum += len(path)
# take ending time
end_time=time.time()

total_combination = (len(nodes)-1)*len(nodes)

print("\tAverage solution length = ",path_sum/total_combination)
print("\taverage time = ",(end_time-start_time)/total_combination)
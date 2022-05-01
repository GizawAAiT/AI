from Graph import *
from Dijkstra import *
from graph_reader import *
from a_star import *

# g=Graph

def degree(g,n):
    G=[]
    for iv,(key,val) in enumerate(g.verticies.items()):
        G.append(key)
    connects = len(g.verticies[n]._nbrs)
    return (connects/(len(G)-1))

def closeness(g,n):
    G=[]
    
    sum = 0.0
    for iv,(key,val) in enumerate(g.verticies.items()):
        G.append(key)
    G.remove(n)
    N_Minus_One = len(G)
    while G:

        dij = Dijkstra(g,n,G.pop())
        path = dij[0]
        for p in path:
           sum += dij[1][p]
    return N_Minus_One/sum

def betweenness(g,n):
    G=set()
    for iv,(key,val) in enumerate(g.verticies.items()):
        G.add(key)
    G.remove(n)
    
    bridge = 0
    road = 0
        
    while G:
        
        initial = G.pop()
        other_nodes = G
        for final in other_nodes:
            dij = a_Star(g,initial,final)
            path = set(dij[0])
            
            if  n in path:
              bridge +=1
            road +=1
    return bridge/road
                
   
   
#  testing the centrality measures.  
G=[]    
for iv,(key,val) in enumerate(g.verticies.items()):
    G.append(key)

print("Node","\t", "degree" ,"\t\t", "closeness" ,"\t\t","betweenness")
for i in G:    
    print(i,"\t", degree(g,i),"\t",closeness(g,i),"\t",betweenness(g,i))



A = 0
bridge=""
closest = ""
high_degree = ""

A = 0
bridge=""
for i in G:    
    b = betweenness(g,i)
    if b > A:
        A=b
        bridge=i
print(bridge ," has the highest betweenness.")

closest = ""
B=0
for i in G:    
    b = closeness(g,i)
    if b > B:
        B=b
        closest=i
print(closest ," is closest node")

C=0
deg = []
for i in G:    
    c = degree(g,i)
    if c >= C:
        C = c
        deg.append(i)
        
print(deg ," has the highest degree")



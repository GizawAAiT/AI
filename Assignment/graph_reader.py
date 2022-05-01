# import Graph
from Graph import *

# instantiate a graph instance
g=Graph()

def loadGraph(file_source):
    
    file=open(file_source,"r")
    lines = file.readlines()
    
    for l in lines:
        list=l.split(" ")   
            
        if list[0] in g.verticies:
            list[0]=g.verticies[list[0]]
        else:
            list[0]=Node(list[0])
            
        if list[2] in g.verticies:
            list[2]=g.verticies[list[2]]
        else:        
            list[2]=Node(list[2])
    
        g.add_edge(list[0], list[2],list[1])     
   
    file.close     
    
loadGraph("edge.txt")

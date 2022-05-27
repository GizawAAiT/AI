from Graph import *
from graph_reader import *



def BFS(g,curr):
    
    vstd=set()
    q = []
    
    q.append(curr)
    vstd.add(curr)
    
    while q:
        curr = q.pop(0)
        
        for i in g.verticies[curr]._nbrs:
            print(i[0].name)
            if i[0].name not in vstd:
                q.append(i[0].name)
                vstd.add(i[0].name)
    print("visited",vstd,len(vstd))
        
BFS(g,"Oradea")        
    

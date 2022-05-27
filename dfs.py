from Graph import *
from graph_reader import *



def DFS(g,curr):
    
    vstd=set()
    st = []    
    st.append(curr)    
    
    while len(st)>0:
        
        curr = st.pop()
        # print(curr)
        
        if (curr not in vstd):
            vstd.add(curr)
            for node in g.verticies[curr]._nbrs:
                if node[0].name not in vstd:
                    st.append(node[0].name)    
        
DFS(g,"Oradea")        
    

import time
from bonus import *

from Graph import *
from graph_reader import *

""" DFS.
*Depth First Search(DFS) function takes a graph and explore every node  starting 
from the current  node provided as a 2nd argument.
It start from curr and goes Deeper and Deeper till it reaches the target
node or a node with no child."""

def DFS(g,curr,target):
    
    path = []
    vstd=set()
    st = []    
    st.append(curr)    
    
    while st and curr!=target:
        
        curr = st.pop()
        # print(curr)
        path.append(curr)
        if (curr not in vstd):
            vstd.add(curr)
            for node in g.verticies[curr]._nbrs:
                if node[0].name not in vstd:
                    st.append(node[0].name)    
    return path   
nodes = []
for v in g.verticies:
    nodes.append(v)
path_sum = 0

# take starting time
end_time=time.time()
start_time = time.time()
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i !=j:
           path = DFS(g,nodes[i],nodes[j])
           path_sum += len(path)

# take starting time
end_time=time.time()
total_combination = (len(nodes)-1)*len(nodes)

print("\tAverage solution length = ",path_sum/total_combination)
print("\taverage time = ",(end_time-start_time)/total_combination)



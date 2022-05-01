from Graph import *
from graph_reader import *
import time

import random

# get the current verticies of the graph
G=set()
for iv ,(key,val)  in enumerate(g.verticies.items()):
    G.add(key)

""" 
*  generate 20*n random and identical numbers.
*  where n is fold of the first (original) graph size
*  create nodes to each of these numbers
*  add these nodes to the original graph
*  by connecting each of them to one or more 
*  nodes in the graph g.
   """

def randNode(l_bound,u_bound,size):
    R_N = set()  
    # file = open("huristic.txt","a+")  
    for i in range(size*20):
        n = str(random.randint(l_bound,u_bound))
        
        while n in R_N:
            n = str(random.randint(l_bound,u_bound))
        
        R_N.add((n))
        
  

        # the following block of file writing is 
        # for the heuristic puprose of any added data.

        # file.write("\n")
        # file.write(n)
        # file.write(" ")
        # file.write(str(random.uniform(30.05, 150.05)))
        # file.write(" ")
        # file.write(str(random.uniform(30.05, 150.05)))
    # file.close()    
    return R_N

"""
  this function will connect a given node 
  as an edge to the first graph
   """
def newConnection(gr,nd1,nd2,w):
    if nd1 in G:
        nd1=g.verticies[nd1]
    else:
        nd1=Node(nd1)
        
    if nd2 in G:
        nd2=g.verticies[nd2]
    else:        
        nd2=Node(nd2)

    gr.add_edge(nd1,nd2,w) 



"""# test :
Here we are going to generate 4 additional 
graphs to the original one and make these graphs ready 
to the test for the algorisms(bfs, dfs, Dijkstra's and A*).
"""

sizes = [1,2,3,4] #times the size (20) .
graphes = ["G1","G2","G3","G4"]


"""
  test 1 when size = 1.
  test 2 when size = 2.
  test 3 when size = 3.
  test 4 when size = 4.
  so Here I am going to use the same code 
  by changing the inputs for the above tests(1-4).
  
"""

R_N = randNode(10,130,sizes[3])
while R_N:        # print(n1 ," is add",len(G),len(R_N))

    ed_no=random.randint(1,7) 
    host = random.sample(G,ed_no)
    n1 = R_N.pop()  
    for i in range(ed_no):        
        n2 = host.pop()
        w = random.uniform(30.5, 200.5)
        newConnection(g,n1,n2,w)    
    G.add(n1)
    
    

















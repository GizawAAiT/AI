# from queue import PriorityQueue

from Graph import *
from graph_reader import *
# def nearest(g,node,explored_list):
#     minimum = 999999
#     pq=[next(iter(g.verticies[node]._nbrs))]
    
#     for tupl in g.verticies[node]._nbrs:
#         if tupl[0].name not in explored_list and float(tupl[1]) < float(minimum):
#             print(minimum,"new weight",tupl[1])
#             minimum = int(tupl[1])
#             pq.pop()
#             pq.append(tupl)
#             print(tupl[0].name," = ", tupl[1])
    # return pq


def Dijkstra(g,curr):
    dist={}       
    parent= {}
    G = set()          
    explored=set()    
    # explored.add(curr)     
        
    for iter, (name, node) in enumerate(g.verticies.items()):
        dist[name]=float('inf')
        G.add(node.name)
        print("mynode",node.name)
    dist[curr]=0    
     
    print("\n\n\n\nG:",G,"\n",len(G),"\n\n\n\n")
    
    while len(G)>0: 
        min_dist=9999999999999 
        succesor=curr  
        for tupl in g.verticies[curr]._nbrs:
            if tupl[0].name not in explored: 
                if dist[tupl[0].name] > dist[curr] + int(tupl[1]):
                    dist[tupl[0].name] = dist[curr] + int(tupl[1])
                    parent[tupl[0].name]=curr
        
        G.remove(curr)
        for i in G:        
            if dist[i] < int(min_dist):
                min_dist=dist[i]
                succesor = i
                    
        explored.add(curr)
        print(curr,dist[curr])
        
        print("G Length:",len(G))
        curr = succesor
        print("succesor :" ,succesor)
        
    return (dist,parent)   
        
Dijkstra(g,"Neamt")      
   
        
        
        
        
        
        
        
        # Q 
   
        # if Q:
        #     opt_wei[Q[0].name] = opt_wei[curr] + Q[1]
            
        #     explored.add(Q[0].name)
        #     G.remove(curr)
        #     curr=Q[0].name
    # print("answer",opt_wei[curr])
    # 
    # backTrackDict = {curr:curr}
    # while destiny not in explored :
    #     next=nextNearest(g,curr,explored)
    #     if next:
    #         backTrackDict[next[0].name] = curr
    #         opt_wei[next[0]]=opt_wei[curr]+next[1]
            
    #         curr = next[0].name
    #         explored.add(curr)
    
    # print("visited",explored,len(explored))
    # # reconstruct the optimum path  
    # path=[]
    # opt_wei=opt_wei[curr]
    # while curr in backTrackDict:
    #     path.append(curr)
    #     curr=backTrackDict[curr]
    # path=reversed(path)
    # return (opt_wei,path)
# Dijkstra(g,"Oradea","Fagaras")    
      
    

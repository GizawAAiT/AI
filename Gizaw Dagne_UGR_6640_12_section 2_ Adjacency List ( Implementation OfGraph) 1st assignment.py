
""" First Lab Assignment.
Adjacency list implementation of Graph."""

class Node:
    """Node hould have to handle the id( Name) of the vertice and the list of other vertiv=ces connected through an edge."""
    def __init__(self, name=None):
        self.id = name
        self.list_connected_nodes=[]
    def updateListConnects(self,destine,weight=1):
        self.list_connected_nodes.append((destine, weight))
        
class Edge:
    """Edge has 2 optional fields(e.i. 1. weight: by default, eny edge considered as unweighted
                                       2. directed(boolean.) by default undirected(bi-directional))"""
    def __init__(self,i,f,weight=1,directed=False):
        self.initial=i
        self.final=f
        self.weight=weight
        self.directed=directed

class Graph:
    """Graph handles the list of nodes, edges and the methodes to connect nodes through edges."""
    def __init__(self):
        self.list_node=[]

    def addNode(self,node):
        nd=Node(node)
        self.list_node.append(nd)

    def addEdge(self,i,f,w=1,d=False):
        initial=final=0
        i_exist=f_exist=False
        for iter in range(len(self.list_node)):
            if self.list_node[iter].id==i:
                i_exist=True
            if self.list_node[iter].id==f:
                f_exist=True

        try:
            if not f_exist or not i_exist:
                raise ValueError
        except ValueError:
            print(f" Node {i} or {f} doesn't exist.")
            return

        # iterate through the node list to track the connecting terminals(Nodes).
        for iterator in self.list_node:
            if iterator.id==i:
                initial=self.list_node.index(iterator)
            if iterator.id ==f:
                final=self.list_node.index(iterator)

        try:
            for atuple in self.list_node[initial].list_connected_nodes:
                if atuple[0]==self.list_node[final].id:
                    raise ValueError
        except ValueError:
            print(f"Edge {self.list_node[initial].id}-{self.list_node[final].id} already there.")
            return

        self.list_node[initial].updateListConnects(self.list_node[final].id,w)

        # if the direction is undetermined(Bi-directional), it should connect in the reverse direction.
        if d==False and initial!=final:
            self.list_node[final].updateListConnects(self.list_node[initial].id,w)





# check out! ( I used some critical test cases).

# gr=Graph()
# gr.addNode("A")
# gr.addNode("E")
# gr.addNode("G")
# gr.addEdge("E","G",6,True)
# gr.addEdge("G","E",1,True)
# gr.addNode("H")
# gr.addEdge("L", "B", 5, True)
# gr.addEdge(1, 'B', 5, True)
# gr.addEdge('B', 1)
# gr.addEdge("A", "H")
# gr.addEdge(1, 'j', 7)
# gr.addEdge(1, 1)
# gr.addNode(1)
# gr.addEdge(1, 1)
# gr.addEdge(1, 1)
#
#
# gr.addEdge("A", "H")
#
# for i in gr.list_node:
#     print(i.id,i.list_connected_nodes)




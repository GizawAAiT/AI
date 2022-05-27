from unicodedata import name


class Node:

    def __init__(self, name):
        self.name = name
        self._nbrs =set()
        
    def connect(self, node):        
        self._nbrs.add(node) 
        
class Edge:

    def __init__(self, left, right, weight=1):
        self.left = left
        self.right = right
        self.weight = weight
        

class Graph:
    
    def __init__(self):
        self.verticies = {}
        self.edges = {}

    def add_node(self, node):
        self.verticies[node.name] = node
        
    def add_edge(self, left, right, weight=1):        
        
        if left.name not in self.verticies:            
            self.verticies[left.name] = left
            
        if right.name not in self.verticies:
            self.verticies[right.name] = right
           
        e = Edge(left, right, weight)

        key = (left.name, right.name)
        self.edges[key] = e  
       
        left.connect((right,weight))
        right.connect((left,weight))
      
    def search(self, a, b):
        pass

    def to_aj_matrix(self):
        pass


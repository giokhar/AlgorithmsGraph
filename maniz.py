
# coding: utf-8

# In[14]:

import re

"""Abstract Data Type Edge"""

class edge:
    def __init__(self, source, destination, nexts = None):
        self._source = source
        self._destination = destination
        self._next = nexts
    
    def getDest(self):
        return self._destination

    def getSource(self):
        return self._source
    
    def getNext(self):
        return self._next  
    
"""Abstract Data Type Node"""

class node:
    
    counter = 0
    
    def __init__(self,key):
        self._id = key
        self._head = None
        self._index = node.counter
        node.counter += 1
        
    def getId(self):
        return self._id
    
    def modNode(self, new_key):
        self._id = new_key
        
    def addFirst(self, source, destination):
        self._head = edge(source, destination)
        self.position = self._head
    
    def addEdge(self, source, destination):
        self.element = edge(source, destination)
        self.position._next = self.element
        self.position = self.element
    
    def firstEdge(self):
        return self._head
    
    def getIndex(self):
        return self._index
"""Abstract Data Type Graph implementing Node and Edge"""

class graph:
    
    def __init__(self):
        self._vertices = {}
        self.vertexNum = 0
        self.edgeNum = 0
    
    # Method of insert node in the graph
    def insert_node(self, key):
        self.vertexNum += 1
        self._vertices[key] = node(key)
        return self._vertices[key]
    
    # Return this list of nodes in the graph 
    # self.vertice = {(Name: Node)}
    def get_vertices(self):
        return self._vertices
    
    # Method of search city and return the index of the node
    def searchCity(self, city):
        if city in self._vertices:
            return self._vertices[city].getIndex()
        else:
            return self.insert_node(city).getIndex()
    
    # Method to insert edge
    # Source and destination can be string representing name of the source and destination
    # Source and destination can be object of source and destination
    # sourcename and destination name not the objects
    
    def insert_edge(self, source, destination):
        self.edgeNum += 1
        if source in self._vertices:
            source = self._vertices[source]
        else:
            source = self.insert_node(source)
            
        if destination in self._vertices:
            destination = self._vertices[destination]
        else:
            destination = self.insert_node(destination)
        
        if source._head == None:
            source.addFirst(source, destination)
        else:
            source.addEdge(source, destination)
       
    # support method for cyclic
    def cyclic_test(self, v, parent):
        if v.getDest() not in self.visited:
            self.visited.append(v.getDest())
            return self.cyclic_test(v.getDest().firstEdge(),v)
                
        next_edge = v.getNext()
        if next_edge != None:
            if parent != next_edge.getDest():
                return True
            return self.cyclic_test(next_edge, v)
        return False
    
    def myFunc(self):

        print("source, destination")
        for u in self._vertices.values():
            print(u.getId())
            print(u.firstEdge().getSource().getId(),"-",u.firstEdge().getDest().getId())


    # method to find cycle in graph, return ture if cyclic
    def cyclic(self):
        self.visited = []
        for u in self._vertices.values():
            if u not in self.visited:
                self.visited.append(u)
                v = u.firstEdge()
                cycle = self.cyclic_test(v, u)
        return cycle    
    
if __name__ == "__main__":
    
#---------------------------------------BUILDING GRAPH------------------------
    """Reading file and building graph"""
    while True:
        filename = input("Enter Filename: ")         
        try:
            with open(filename) as file:
                data1 = file.read().rstrip()           
                data2 = re.split(r'[\n ' ' -]',data1) # parsing the input data file
                break
        except Exception:
            print ('This file does not exist. Try Again.')
    print ()
    
    g = graph() ## object g 
    
    for i in range (0,len(data2) - 1,2):
        g.insert_edge(data2[i],data2[i+1]) # call insert_edge to create edge

    g.myFunc()
    

#--------------------------------------Connected Components-------------------------------------

# DFS graph method ... generic type for adjacency list graph
def dfs(v):
    
    if v.getDest() not in visited:
        connected[connected_component].append(v.getDest().getId()) # adding the vertex to component
        visited.append(v.getDest())
        dfs(v.getDest().firstEdge())
    v = v.getNext()
    if v != None:
        dfs(v)

visited = []
connected = {}         
connected_component = 0
# keeping track of connected components by implementing DFS
for u in g.get_vertices().values():
    if u not in visited:
        connected_component += 1 # component number
        connected[connected_component] = [u.getId()] # component list
        visited.append(u) 
        dfs(u.firstEdge())
        
# ----------------------------OUTPUT-------------------------------------------------------        

print("Read", g.vertexNum, "cities", int(g.edgeNum/2), "edges")   
print()
print("Number of connected components:", connected_component)  
print()
for key, value in connected.items():
    print("Connected Component",key,":")
    for j in value:
        print(j)
    print()

        


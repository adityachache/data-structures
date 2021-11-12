class Graph():
    
    def __init__(self):
        self.numberofnodes = 0 
        self.adjacentlist = {}
        

    def addvertex(self,node):
        """add a vertex in the graph"""
        self.adjacentlist[node] = []
        self.numberofnodes += 1
            
    def addedge(self,node1,node2):
        """add an edge to a vertex"""
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
        
    
    def showconnections(self):
        """shows the connection between the vertices"""
        for node in self.adjacentlist:
            print(f'{node} -->> {" ".join(map(str,self.adjacentlist[node]))}')
            #print(f'{node} -->> {" ".join(self.adjacentlist[node])}')


my_graph = Graph()
my_graph.addvertex(1)
my_graph.addvertex(2)
my_graph.addvertex(3)
my_graph.addedge(1,2)
my_graph.addedge(1,3)
my_graph.addedge(2,3)
my_graph.showconnections()
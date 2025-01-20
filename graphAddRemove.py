class Graph():
    def __init__(self):
        self.adj_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for other in self.adj_list[vertex]:
                self.adj_list[other].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
    def print_graph(self):
        v_list=[]
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v,' : ',self.adj_list[v])


my_graph=Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_edge(1,2)
my_graph.add_edge(1,4)
my_graph.add_edge(1,3)
my_graph.add_edge(2,3)
my_graph.add_edge(3,4)
my_graph.print_graph()

print("removing edge betwen 3 and 4")
my_graph.remove_edge(4,3)
my_graph.print_graph()

print("removing vertex 1")
my_graph.remove_vertex(1)
my_graph.print_graph()
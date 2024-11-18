class DirectedGraph:
    def __init__(self) -> None:
        self.adjacency_list = {}
        
    def add_vertex(self,vertex):
        """Add a new vertex to the adjaceny list"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        
    def add_edge(self, start, end):
        """Add a directed edge from ‘start‘ to ‘end‘ """
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        
        if end not in self.adjacency_list:
            self.adjacency_list[end] = []
            
        self.adjacency_list[start].append(end)
        
    def display(self):
        """Display the graph."""
        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")
            
    def in_degree(self):
        """Calculate the in-degree of each vertex."""
        in_degrees = {vertex: 0 for vertex in self.adjacency_list}
        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                in_degrees[neighbor] += 1
        return in_degrees

    def out_degree(self):
        """Calculate the out-degree of each vertex."""
        out_degrees = {vertex: len(neighbors) for vertex, neighbors in self.adjacency_list.items()}
        return out_degrees
    
    
# Create a directed graph
graph = DirectedGraph()

# Add vertices and directed edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("D", "E")

# Display the directed graph
print("Directed Graph (Adjacency List):")
graph.display()

# Calculate and display in-degree and out-degree
print("\nIn-Degree of vertices:", graph.in_degree())
print("Out-Degree of vertices:", graph.out_degree())
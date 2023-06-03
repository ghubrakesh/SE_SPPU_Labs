class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {node: [] for node in nodes}
        
    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
        
    def dfs(self, start_node):
        visited = set()
        self._dfs_helper(start_node, visited)
        
    def _dfs_helper(self, curr_node, visited):
        visited.add(curr_node)
        print(curr_node, end=' -> ')
        
        for neighbor in self.adj_list[curr_node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)
    
    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        visited.add(start_node)
        
        while queue:
            curr_node = queue.pop(0)
            print(curr_node, end=' -> ')
            
            for neighbor in self.adj_list[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
               
    
# Example usage:
nodes = ["Library", "Science-Building", "Student-Center", "Canteen", "Recreation-Center"]
g = Graph(nodes)
g.add_edge("Library", "Science-Building")
g.add_edge("Science-Building", "Student-Center")
g.add_edge("Student-Center", "Canteen")
g.add_edge("Canteen", "Recreation-Center")
g.add_edge("Recreation-Center", "Student-Center")
g.add_edge("Recreation-Center", "Library")

print()
print("DFS traversal:")
g.dfs("Library")
print()
print("\nBFS traversal:")
g.bfs("Library")
print()

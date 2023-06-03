class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        parent = []
        rank = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while e < self.vertices - 1:
            src, dest, weight = self.graph[i]
            i += 1
            x = self.find(parent, src)
            y = self.find(parent, dest)

            if x != y:
                e += 1
                result.append((src, dest, weight))
                self.union(parent, rank, x, y)

        return result


# Example usage
g = Graph(4)
g.add_edge(0, 1, 4)
g.add_edge(0, 3, 8)
g.add_edge(1, 2, 6)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 3)

mst = g.kruskal_mst()

# Print the minimum spanning tree
for src, dest, weight in mst:
    print(f"Office {src} connected to Office {dest} with a cost of {weight}")

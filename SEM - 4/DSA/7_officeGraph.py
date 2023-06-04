import heapq

def prim(graph):
    priority_queue = []
    heapq.heapify(priority_queue)

    start_office = list(graph.keys())[0]
    visited = set([start_office])

    mst = []
    total_cost = 0

    for neighbor, cost in graph[start_office]:
        heapq.heappush(priority_queue, (cost, start_office, neighbor))

    while len(priority_queue) :
        cost, office1, office2 = heapq.heappop(priority_queue)

        # Check for a cycle
        if office2 not in visited:
            visited.add(office2)
            mst.append((office1, office2, cost))
            total_cost += cost

            # Add the edges of the newly visited office to the priority queue
            for neighbor, cost in graph[office2]:
                heapq.heappush(priority_queue, (cost, office2, neighbor))

    return mst, total_cost

# Example usage
graph = {
    'Office1': [('Office2', 5), ('Office3', 10)],
    'Office2': [('Office1', 5), ('Office3', 8), ('Office4', 6)],
    'Office3': [('Office1', 10), ('Office2', 8), ('Office4', 3)],
    'Office4': [('Office2', 6), ('Office3', 3)]
}

mst, total_cost = prim(graph)

# Print the minimum spanning tree and total cost
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total Cost:", total_cost)

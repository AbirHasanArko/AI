import heapq

def best_first_search(graph, start, goal, heuristic, algorithm="astar"):

    pq = [(0, start)]
    visited = set()
    parent = {start: None}
    cost = {start: 0}

    while pq:

        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        print("Visiting:", current)

        if current == goal:
            break

        for neighbor, weight in graph[current]:

            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:

                cost[neighbor] = new_cost
                parent[neighbor] = current

                if algorithm == "gbfs":
                    f = heuristic[neighbor]

                else:  # A*
                    f = new_cost + heuristic[neighbor]

                heapq.heappush(pq, (f, neighbor))

    if goal not in parent:
        print("No path found")
        return

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Path:", path)
    print("Cost:", cost[goal])


# Weighted graph: (neighbor, edge_cost)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'G': []
}

# Estimated distance from each node to goal G
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 2,
    'G': 0
}

start = 'A'
goal = 'G'

# Choose algorithm:
best_first_search(graph, start, goal, heuristic, "gbfs")

# best_first_search(graph, start, goal, heuristic, "astar")
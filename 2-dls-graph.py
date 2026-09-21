def dls(graph, node, goal, blocked, limit, visited, parents, depth):
    if node in blocked:
        return False

    visited.add(node)

    if node == goal:
        return True

    if depth == limit:
        return False

    for neighbour in graph[node]:
        if neighbour not in visited and neighbour not in blocked:
            parents[neighbour] = node
            if dls(graph, neighbour, goal, blocked, limit, visited, parents, depth + 1):
                return True

    return False

def DLS(graph, start, goal, blocked, limit):
    visited = set()
    parents = {}

    found = dls(graph, start, goal, blocked, limit, visited, parents, 0)

    if not found:
        print("not found")
        return

    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = parents[cur]
    path.append(start)
    path.reverse()

    print("Path", "->".join(path))


graph = {
    'A' : ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

blocked = {"E"}

DLS(graph, 'A', 'G', blocked, 4)
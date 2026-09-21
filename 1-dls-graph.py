def dfs(graph, start, goal, blocked):
    stack = [start]
    visited = set()
    parent = {}

    while stack:
        node = stack.pop()

        if node in visited or node in blocked:
            continue

        visited.add(node)

        if node == goal:
            break

        for neig in graph[node]:
            if neig not in visited or neig not in blocked:
                parent[neig] = node
                stack.append(neig)

    if goal not in visited:
        print("Goal not found")
        return

    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)

    path.reverse()

    print("Path:", " -> ".join(path))


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

blocked = {"E"}

dfs(graph, 'A', 'G', blocked)


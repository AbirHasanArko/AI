def dfs(graph, node, goal, blocked, limit, visited, parents, depth):
    if node in blocked:
        return False

    visited.add(node)

    if node == goal:
        return True

    if depth == limit:
        return False

    for neighbor in graph[node]:
        if neighbor not in blocked and neighbor not in visited:
            parents[neighbor] = node

            if dfs(graph, neighbor, goal, blocked, limit, visited, parents, depth + 1):
                return True

    return False


def iddfs(graph, start, goal, blocked, maxdepth):
    for limit in range (maxdepth + 1):
        print(f"at limit {limit}")
        visited = set()
        parents = {}

        found = dfs(graph, start, goal, blocked, limit, visited, parents, 0)

        if not found:
            print("not found")
            continue

        path = []
        cur = goal
        while cur != start:
            path.append(cur)
            cur = parents[cur]
        path.append(start)
        path.reverse()
        
        print("Path", "->".join(path))

        return

    print("stopped")


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

iddfs(graph, 'A', 'G', blocked, 4)

        
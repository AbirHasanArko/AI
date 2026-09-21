from collections import deque

def bi(graph, start, goal, blocked):
    if start in blocked or goal in blocked:
        print("start or goal is blocked")
        return

    if start == goal:
        print("start is goal")
        return

    fwd_q = deque([start])
    bwd_q = deque([goal])

    fwd_visited = {start}
    bwd_visited = {goal}

    fwd_parent = {}
    bwd_parent = {}

    meeting_node = None

    while fwd_q and bwd_q:
        node = fwd_q.popleft()

        for neig in graph[node]:
            if neig in blocked:
                continue

            if neig not in blocked and neig not in fwd_visited:
                fwd_parent[neig] = node
                fwd_visited.add(neig)
                fwd_q.append(neig)

                if neig in bwd_visited:
                    meeting_node = neig
                    break

        if meeting_node:
            break

        node = bwd_q.popleft()
        
        for neig in graph[node]:
            if neig in blocked:
                continue

            if neig not in blocked and neig not in bwd_visited:
                bwd_parent[neig] = node
                bwd_visited.add(neig)
                bwd_q.append(neig)

                if neig in fwd_visited:
                    meeting_node = neig
                    break

        if meeting_node:
            break

    if meeting_node is None:
        print("no path")
        return

    path1 = []
    cur = meeting_node
    while cur != start:
        path1.append(cur)
        cur = fwd_parent[cur]
    path1.append(start)
    path1.reverse()

    path2 = []
    cur = bwd_parent[meeting_node]
    while cur != goal:
        path2.append(cur)
        cur = bwd_parent[cur]
    path2.append(goal)

    path = path1 + path2

    print("path: ","->".join(path))


graph = {
    'A' : ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','G'],
    'F': ['C','G'],
    'G': ['E', 'F']
}

blocked = {"E"}

bi(graph, 'A', 'G', blocked)

    
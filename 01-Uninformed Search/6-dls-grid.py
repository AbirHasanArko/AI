def dls(grid, current, goal, limit, depth, visited, parent):

    rows = len(grid)
    cols = len(grid[0])

    # Goal found
    if current == goal:
        return True

    # Cannot go deeper
    if depth == limit:
        return False

    visited.add(current)

    r, c = current

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        # Outside grid
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            continue

        # Blocked
        if grid[nr][nc] == '#':
            continue

        neighbor = (nr, nc)

        # Already visited
        if neighbor in visited:
            continue

        # Save parent
        parent[neighbor] = current

        # Recursively search deeper
        if dls(
            grid,
            neighbor,
            goal,
            limit,
            depth + 1,
            visited,
            parent
        ):
            return True

    return False


def depth_limited_search(grid, start, goal, limit):

    visited = set()
    parent = {}

    found = dls(
        grid,
        start,
        goal,
        limit,
        0,
        visited,
        parent
    )

    if not found:
        print("Goal not found within depth limit.")
        return

    # Construct path
    path = []

    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    print("DLS Path:")
    print(path)

    print("Path length:", len(path) - 1)
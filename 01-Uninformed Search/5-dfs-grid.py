def dfs(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    # DFS uses a stack
    stack = [start]

    # Keep track of visited cells
    visited = set()

    # Used to reconstruct the final path
    parent = {}

    # Up, Down, Left, Right
    directions = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    while stack:

        # Take the last inserted cell
        current = stack.pop()

        # Don't process twice
        if current in visited:
            continue

        r, c = current

        # Don't enter blocked cell
        if grid[r][c] == '#':
            continue

        visited.add(current)

        print("Visiting:", current)

        # Goal test
        if current == goal:
            break

        # Generate neighbors
        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            # Outside grid
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            # Blocked cell
            if grid[nr][nc] == '#':
                continue

            neighbor = (nr, nc)

            # Already visited
            if neighbor in visited:
                continue

            # Save parent
            if neighbor not in parent:
                parent[neighbor] = current

            # Add to stack
            stack.append(neighbor)

    # Goal not reached
    if goal not in visited:
        print("No path found")
        return

    # -------------------------
    # Construct path
    # -------------------------

    path = []

    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)

    # Reverse: goal -> start becomes start -> goal
    path.reverse()

    print("\nPath:")
    print(path)

    print("\nPath length:", len(path) - 1)

grid = [
    ['S', '.', '.', '#', '.'],
    ['#', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', 'G']
]

start = (0, 0)
goal = (4, 4)

dfs(grid, start, goal)
from collections import deque


def bidirectional_search(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    # Start search
    forward_queue = deque([start])

    # Goal search
    backward_queue = deque([goal])

    # Visited sets
    visited_forward = {start}
    visited_backward = {goal}

    # Parent dictionaries
    parent_forward = {}
    parent_backward = {}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    meeting = None

    while forward_queue and backward_queue:

        # =================================
        # FORWARD SEARCH
        # =================================

        current = forward_queue.popleft()

        r, c = current

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

            if neighbor not in visited_forward:

                visited_forward.add(neighbor)

                parent_forward[neighbor] = current

                forward_queue.append(neighbor)

                # Did the two searches meet?
                if neighbor in visited_backward:
                    meeting = neighbor
                    break

        if meeting is not None:
            break

        # =================================
        # BACKWARD SEARCH
        # =================================

        current = backward_queue.popleft()

        r, c = current

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            if grid[nr][nc] == '#':
                continue

            neighbor = (nr, nc)

            if neighbor not in visited_backward:

                visited_backward.add(neighbor)

                parent_backward[neighbor] = current

                backward_queue.append(neighbor)

                # Did the two searches meet?
                if neighbor in visited_forward:
                    meeting = neighbor
                    break

        if meeting is not None:
            break

    # =================================
    # No meeting
    # =================================

    if meeting is None:
        print("No path found.")
        return

    # =================================
    # Start → Meeting
    # =================================

    path1 = []

    current = meeting

    while current != start:

        path1.append(current)

        current = parent_forward[current]

    path1.append(start)

    path1.reverse()

    # =================================
    # Meeting → Goal
    # =================================

    path2 = []

    current = meeting

    while current != goal:

        current = parent_backward[current]

        path2.append(current)

    # Combine
    path = path1 + path2

    print("Meeting point:", meeting)
    print("Path:", path)
    print("Path length:", len(path) - 1)
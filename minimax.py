import math
import copy

# Determine whose turn
def player(state):
    x = sum(row.count('X') for row in state)
    o = sum(row.count('O') for row in state)

    return 'X' if x == o else 'O'


# Get available moves
def actions(state):
    moves = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                moves.append((i, j))

    return moves


# Generate new state
def result(state, action):
    new_state = copy.deepcopy(state)
    i, j = action
    new_state[i][j] = player(state)

    return new_state


# Check game over
def terminal(state):

    lines = []

    lines.extend(state)

    for j in range(3):
        lines.append([state[i][j] for i in range(3)])

    lines.append([state[i][i] for i in range(3)])
    lines.append([state[i][2-i] for i in range(3)])

    for line in lines:
        if line == ['X'] * 3 or line == ['O'] * 3:
            return True

    return len(actions(state)) == 0


# Evaluate game state
def utility(state):

    lines = list(state)

    for j in range(3):
        lines.append([state[i][j] for i in range(3)])

    lines.append([state[i][i] for i in range(3)])
    lines.append([state[i][2-i] for i in range(3)])

    for line in lines:
        if line == ['X'] * 3:
            return 1

        if line == ['O'] * 3:
            return -1

    return 0


# MAX player (X)
def max_value(state):

    if terminal(state):
        return utility(state)

    value = -math.inf

    for action in actions(state):
        value = max(value, min_value(result(state, action)))

    return value


# MIN player (O)
def min_value(state):

    if terminal(state):
        return utility(state)

    value = math.inf

    for action in actions(state):
        value = min(value, max_value(result(state, action)))

    return value


# Find best move
def minimax(state):

    best_action = None

    if player(state) == 'X':

        best_value = -math.inf

        for action in actions(state):
            value = min_value(result(state, action))

            if value > best_value:
                best_value = value
                best_action = action

    else:

        best_value = math.inf

        for action in actions(state):
            value = max_value(result(state, action))

            if value < best_value:
                best_value = value
                best_action = action

    return best_action


# Main function
state = [
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
    [' ', ' ', 'O']
]

move = minimax(state)

print("Best move:", move)
print("Player:", player(state))
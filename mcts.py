import math
import copy
import random


# Determine current player
def player(state):
    x = sum(row.count('X') for row in state)
    o = sum(row.count('O') for row in state)

    return 'X' if x == o else 'O'


# Find available moves
def actions(state):
    moves = []

    for i in range(3):
        for j in range(3):
            if state[i][j] == ' ':
                moves.append((i, j))

    return moves


# Generate next state
def result(state, action):
    new_state = copy.deepcopy(state)
    i, j = action
    new_state[i][j] = player(state)

    return new_state


# Check terminal state
def terminal(state):

    lines = list(state)

    for j in range(3):
        lines.append([state[i][j] for i in range(3)])

    lines.append([state[i][i] for i in range(3)])
    lines.append([state[i][2-i] for i in range(3)])

    for line in lines:
        if line == ['X'] * 3 or line == ['O'] * 3:
            return True

    return len(actions(state)) == 0


# Evaluate result
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


# MCTS Node
class MCTSNode:

    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

        self.children = []
        self.visits = 0
        self.total_value = 0

        self.untried_actions = actions(state)


# UCB1 formula
def ucb1(node, C=1.41):

    if node.visits == 0:
        return math.inf

    exploitation = node.total_value / node.visits

    exploration = C * math.sqrt(
        math.log(node.parent.visits) / node.visits
    )

    return exploitation + exploration


# 1. Selection
def selection(node):

    while not terminal(node.state):

        if node.untried_actions:
            return node

        node = max(node.children, key=ucb1)

    return node


# 2. Expansion
def expansion(node):

    if terminal(node.state):
        return node

    action = random.choice(node.untried_actions)
    node.untried_actions.remove(action)

    new_state = result(node.state, action)

    child = MCTSNode(new_state, node, action)
    node.children.append(child)

    return child


# 3. Simulation (Random rollout)
def simulation(node):

    state = copy.deepcopy(node.state)

    while not terminal(state):

        action = random.choice(actions(state))
        state = result(state, action)

    return utility(state)


# 4. Backpropagation
def backpropagation(node, result_value):

    while node is not None:

        node.visits += 1
        node.total_value += result_value

        node = node.parent


# Main MCTS
def mcts(state, iterations=1000):

    root = MCTSNode(state)

    for _ in range(iterations):

        node = selection(root)
        node = expansion(node)

        result_value = simulation(node)

        backpropagation(node, result_value)

    best_child = max(root.children, key=lambda child: child.visits)

    return best_child.action


# Main program
state = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

print("Initial Board:")
for row in state:
    print(row)

move = mcts(state, iterations=1000)

print("\nBest AI Move:", move)
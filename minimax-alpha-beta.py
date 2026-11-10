import math

board = [
    ["X", "O", "X"],
    ["O", "X", " "],
    [" ", " ", "O"]
]

def player(board):
    x = sum(row.count("X") for row in board)
    o = sum(row.count("O") for row in board)
    return "X" if x == o else "O"


def actions(board):
    return [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] == " "
    ]


def result(board, action, p):
    new_board = [row[:] for row in board]
    r, c = action
    new_board[r][c] = p
    return new_board


def utility(board):
    lines = (
        board +
        [[board[r][c] for r in range(3)] for c in range(3)] +
        [[board[i][i] for i in range(3)],
         [board[i][2-i] for i in range(3)]]
    )

    for line in lines:
        if line.count("X") == 3:
            return 1
        if line.count("O") == 3:
            return -1

    return 0


def terminal(board):
    return utility(board) != 0 or not actions(board)


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(
            result(board, action, "X"), alpha, beta
        ))

        alpha = max(alpha, v)

        if alpha >= beta:
            break  # Prune

    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(
            result(board, action, "O"), alpha, beta
        ))

        beta = min(beta, v)

        if beta <= alpha:
            break  # Prune

    return v


def minimax(board):
    best_action = None
    alpha = -math.inf
    beta = math.inf

    for action in actions(board):
        value = min_value(
            result(board, action, "X"), alpha, beta
        )

        if value > alpha:
            alpha = value
            best_action = action

    return best_action


print("Best move:", minimax(board))
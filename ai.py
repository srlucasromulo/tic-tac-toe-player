import random


def winning(board):

    # check lines
    for line in range(3):
        count_1 = 0
        count_2 = 0
        target = None

        for column in range(3):
            if board[line, column] == 0:
                target = (line, column)
            elif board[line, column] == 1:
                count_1 += 1
            elif board[line, column] == 2:
                count_2 += 1

        if (count_1 == 2 or count_2 == 2) and target is not None:
            return target

    # check columns
    for column in range(3):
        count_1 = 0
        count_2 = 0
        target = None

        for line in range(3):
            if board[line, column] == 0:
                target = (line, column)
            elif board[line, column] == 1:
                count_1 += 1
            elif board[line, column] == 2:
                count_2 += 1

        if (count_1 == 2 or count_2 == 2) and target is not None:
            return target

    # check diag 1
    count_1 = 0
    count_2 = 0
    target = None
    for i in range(3):

        if board[i, i] == 0:
            target = (i, i)
        elif board[i, i] == 1:
            count_1 += 1
        elif board[i, i] == 2:
            count_2 += 1

        if (count_1 == 2 or count_2 == 2) and target is not None:
            return target

    # check diag 2
    count_1 = 0
    count_2 = 0
    target = None
    column = 2
    for line in range(3):
        if board[line, column] == 0:
            target = (line, column)
        elif board[line, column] == 1:
            count_1 += 1
        elif board[line, column] == 2:
            count_2 += 1
        column -= 1

        if (count_1 == 2 or count_2 == 2) and target is not None:
            return target

    return None


def random_position(board):
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x, y] == 0:
            return x, y


def play(board):
    position = winning(board)
    print(f'position to play: {position}')
    if position is not None:
        return position
    else:
        return random_position(board)

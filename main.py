import random


def dead_state(width: int, height: int):
    board_holder = []
    for i in range(height):
        row_holder = []
        for j in range(width):
            row_holder.append(0)
        board_holder.append(row_holder)
    return board_holder


def random_state(width: int, height: int):
    board_holder = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            board_holder[i][j] = random.randint(0, 1)
    return board_holder


def render(board):
    height = len(board)
    width = len(board[0])

    for i in range(height):
        for j in range(width):
            if j == 0:
                print(" ", end="")
                print(board[i][j], end="  ")
            elif 0 < j < width - 1:
                print(board[i][j], end="  ")
            else:
                print(board[i][j], end="")
                print(" ", end="")
        print()


board = random_state(4, 4)

render(board)

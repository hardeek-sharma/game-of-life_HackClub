import random
import time
from time import sleep


Dead_num = 0
Dead_sym = "`"

Alive_num = 1
Alive_sym = "X"


def dead_state(width: int, height: int):
    board_holder = []
    for i in range(height):
        row_holder = []
        for j in range(width):
            row_holder.append(Dead_num)
        board_holder.append(row_holder)
    return board_holder


def random_state(width: int, height: int):
    board_holder = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            board_holder[i][j] = random.choice([Dead_num, Alive_num])
    return board_holder


def render(board_holder):
    height = len(board_holder)
    width = len(board_holder[0])

    print("-" * (width * 3 + 2))

    for i in range(height):
        for j in range(width):
            if j == 0:
                print("| ", end="")
                if board_holder[i][j] == Dead_num:
                    print(Dead_sym, end="  ")
                else:
                    print(Alive_sym, end="  ")
            elif 0 < j < width - 1:
                if board_holder[i][j] == Dead_num:
                    print(Dead_sym, end="  ")
                else:
                    print(Alive_sym, end="  ")
            else:
                if board_holder[i][j] == Dead_num:
                    print(f"{Dead_sym} |", end="")
                else:
                    print(f"{Alive_sym} |", end="")
                print(" ", end="")
        print()

    print("-" * (width * 3 + 2))


def next_board_state(init_board):
    height = len(init_board)
    width = len(init_board[0])

    next_board = []
    for i in range(height):
        next_row = []
        for j in range(width):
            live_neighbors = 0

            if i == 0 and j == 0: # Top Left
                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1

                if init_board[i + 1][j + 1] == Alive_num:  # SE
                    live_neighbors += 1

                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1
            elif i == 0 and j != 0 and j != width-1: # Top
                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1

                if init_board[i + 1][j + 1] == Alive_num:  # SE
                    live_neighbors += 1

                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1

                if init_board[i + 1][j - 1] == Alive_num:  # SW
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
                    live_neighbors += 1
            elif i == 0 and j == width-1: # Top Right
                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1

                if init_board[i + 1][j - 1] == Alive_num:  # SW
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
                    live_neighbors += 1
            elif i != 0 and i != height-1 and j == 0: # Left
                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i - 1][j + 1] == Alive_num:  # NE
                    live_neighbors += 1

                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1

                if init_board[i + 1][j + 1] == Alive_num:  # SE
                    live_neighbors += 1

                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1
            elif i != 0 and i != height-1 and j != 0 and j != width-1: # Center
                if init_board[i-1][j-1] == Alive_num: # NW
                    live_neighbors += 1

                if init_board[i-1][j] == Alive_num: # N
                    live_neighbors += 1

                if init_board[i-1][j+1] == Alive_num: # NE
                    live_neighbors += 1

                if init_board[i][j+1] == Alive_num: # E
                    live_neighbors += 1

                if init_board[i+1][j+1] == Alive_num: # SE
                    live_neighbors += 1

                if init_board[i+1][j] == Alive_num: # S
                    live_neighbors += 1

                if init_board[i+1][j-1] == Alive_num: # SW
                    live_neighbors += 1

                if init_board[i][j-1] == Alive_num: # W
                    live_neighbors += 1
            elif i != 0 and i != height-1 and j == width-1: # Right
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i+1][j] == Alive_num: # S
                    live_neighbors += 1

                if init_board[i+1][j-1] == Alive_num: # SW
                    live_neighbors += 1

                if init_board[i][j-1] == Alive_num: # W
                    live_neighbors += 1
            elif i == height-1 and j == 0: # Bottom Left
                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i - 1][j + 1] == Alive_num:  # NE
                    live_neighbors += 1

                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1
            elif i == height-1 and j != 0 and j != width-1: # Bottom
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i - 1][j + 1] == Alive_num:  # NE
                    live_neighbors += 1

                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1

                if init_board[i][j-1] == Alive_num: # W
                    live_neighbors += 1
            elif i == height-1 and j == width-1: # Bottom Right
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i][j-1] == Alive_num: # W
                    live_neighbors += 1

            if live_neighbors <= 1 and init_board[i][j] == Alive_num:
                next_row.append(Dead_num)
            elif 2 <= live_neighbors <= 3 and init_board[i][j] == Alive_num:
                next_row.append(Alive_num)
            elif live_neighbors > 3 and init_board[i][j] == Alive_num:
                next_row.append(Dead_num)
            elif live_neighbors == 3 and init_board[i][j] == Dead_num:
                next_row.append(Alive_num)
            else:
                next_row.append(Dead_num)

        next_board.append(next_row)
    return next_board


def run_forever(new_board):
    while True:
        render(new_board)
        old_board = new_board
        new_board = next_board_state(new_board)
        sleep(0.5)

        if new_board == old_board:
            render(new_board)
            break



if __name__ == '__main__':
    board = random_state(10, 10)

    run_forever(board)
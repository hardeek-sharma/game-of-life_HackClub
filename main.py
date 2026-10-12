import random
from enum import Enum


class Dead(Enum):
    num = 0
    symbol = "`"


class Alive(Enum):
    num = 1
    symbol = "X"


def dead_state(width: int, height: int):
    board_holder = []
    for i in range(height):
        row_holder = []
        for j in range(width):
            row_holder.append(Dead.num)
        board_holder.append(row_holder)
    return board_holder


def random_state(width: int, height: int):
    board_holder = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            board_holder[i][j] = random.choice([Dead.num, Alive.num])
    return board_holder


def render(board_holder):
    height = len(board_holder)
    width = len(board_holder[0])

    print("-" * (width * 3 + 2))

    for i in range(height):
        for j in range(width):
            if j == 0:
                print("| ", end="")
                if board_holder[i][j] == Dead.num:
                    print(Dead.symbol.value, end="  ")
                else:
                    print(Alive.symbol.value, end="  ")
            elif 0 < j < width - 1:
                if board_holder[i][j] == Dead.num:
                    print(Dead.symbol.value, end="  ")
                else:
                    print(Alive.symbol.value, end="  ")
            else:
                if board_holder[i][j] == Dead.num:
                    print(f"{Dead.symbol.value} |", end="")
                else:
                    print(f"{Alive.symbol.value} |", end="")
                print(" ", end="")
        print()

    print("-" * (width * 3 + 2))


board = random_state(60, 13)

render(board)

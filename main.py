import random
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

            if i == 0 and j == 0:  # Top Left
                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1

                if init_board[i + 1][j + 1] == Alive_num:  # SE
                    live_neighbors += 1

                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1
            elif i == 0 and j != 0 and j != width - 1:  # Top
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
            elif i == 0 and j == width - 1:  # Top Right
                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1

                if init_board[i + 1][j - 1] == Alive_num:  # SW
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
                    live_neighbors += 1
            elif i != 0 and i != height - 1 and j == 0:  # Left
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
            elif i != 0 and i != height - 1 and j != 0 and j != width - 1:  # Center
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

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

                if init_board[i + 1][j - 1] == Alive_num:  # SW
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
                    live_neighbors += 1
            elif i != 0 and i != height - 1 and j == width - 1:  # Right
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i + 1][j] == Alive_num:  # S
                    live_neighbors += 1

                if init_board[i + 1][j - 1] == Alive_num:  # SW
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
                    live_neighbors += 1
            elif i == height - 1 and j == 0:  # Bottom Left
                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i - 1][j + 1] == Alive_num:  # NE
                    live_neighbors += 1

                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1
            elif i == height - 1 and j != 0 and j != width - 1:  # Bottom
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i - 1][j + 1] == Alive_num:  # NE
                    live_neighbors += 1

                if init_board[i][j + 1] == Alive_num:  # E
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
                    live_neighbors += 1
            elif i == height - 1 and j == width - 1:  # Bottom Right
                if init_board[i - 1][j - 1] == Alive_num:  # NW
                    live_neighbors += 1

                if init_board[i - 1][j] == Alive_num:  # N
                    live_neighbors += 1

                if init_board[i][j - 1] == Alive_num:  # W
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


def get_file_path():
    while True:
        try:
            file_path = input("Enter an absolute file path: ")
            with open(file_path, "r") as file:
                contents = file.readline()
        except FileNotFoundError:
            print("\033[31m That file was not found (make sure to use an absolute path) \033[0m")
        except PermissionError:
            print("\033[31m File exists, but you do not have permission to access it \033[0m")
        else:
            break

    return file_path


def get_board_from_file():
    file_path = get_file_path()

    with open(file_path, "r") as file:
        file_list = file.read().split("\n")

        file_matrix = []
        for row in file_list:
            file_matrix.append(list(row))

        height = len(file_matrix)
        length = len(file_matrix[0])

        for i in range(height):
            for j in range(length):
                file_matrix[i][j] = int(file_matrix[i][j])

    return file_matrix


def get_board_mode():
    print("(1. Random Soup 2. Import From File)")
    while True:
        try:
            board_mode = int(input("How would you get a life: "))
        except ValueError:
            print("\033[31m Enter a NUMBER (1 or 2) \033[0m")
        else:
            if board_mode < 1 or board_mode > 2:
                print("\033[31m Enter 1 or 2 \033[0m")
            else:
                return board_mode


def get_width():
    while True:
        try:
            width = int(input("How wide do you want your board to be: "))
        except ValueError:
            print("\033[31m Enter a NUMBER \033[0m")
        else:
            if width <= 1:
                print("\033[31m Width cannot be less than 2 \033[0m")
            else:
                return width


def get_height():
    while True:
        try:
            height = int(input("How tall do you want your board to be: "))
        except ValueError:
            print("\033[31m Enter a NUMBER \033[0m")
        else:
            if height <= 1:
                print("\033[31m Height cannot be less than 2 \033[0m")
            else:
                return height


def run_life():
    board = None
    mode = get_board_mode()
    if mode == 1:
        board = random_state(get_width(), get_height())
    elif mode == 2:
        board = get_board_from_file()

    run_forever(board)


if __name__ == '__main__':
    run_life()

import sys
from collections import deque
from io import StringIO

input_1 = """4 5
.....
.....
.B...
...P.
LLLLLLLL"""

sys.stdin = StringIO(input_1)


def matrix_dimension_input() -> list:
    matrix = []
    matrix_rows, matrix_column = input().split()
    matrix_rows = int(matrix_rows)
    matrix_column = int(matrix_column)
    [matrix.append(input()) for row in range(matrix_rows)]
    matrix = [matrix[y][x] for y in range(len(matrix)) for x in range(len(matrix[0]))]
    matrix = [matrix[x:x + matrix_column] for x in range(0, len(matrix), matrix_column)]
    return matrix


def player_movement_commands() -> deque:
    return deque(input())


def player_location(matrix: list) -> tuple:
    row_player, column_player = 0, 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == "P":
                row_player, column_player = row, column
    return row_player, column_player


def bunnies_movement(matrix: list) -> ():
    row_bunny = 0
    column_bunny = 0
    list_with_bunnies = deque()
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == "B":
                row_bunny, column_bunny = row, column
                list_with_bunnies.append([row_bunny, column_bunny])
    while list_with_bunnies:
        current_bunny_location = list_with_bunnies.popleft()
        row_bunny, column_bunny = current_bunny_location
        if 'P' in matrix[row_bunny - 1:row_bunny + 2] or "P" in matrix[column_bunny - 1:column_bunny + 2]:
            return matrix, True
        if column_bunny - 1 in range(len(matrix[0])):
            matrix[row_bunny][column_bunny - 1] = "B"
        if column_bunny + 1 in range(len(matrix[0])):
            matrix[row_bunny][column_bunny + 1] = "B"
        if row_bunny - 1 in range(len(matrix)):
            matrix[row_bunny - 1][column_bunny] = "B"
        if row_bunny + 1 in range(len(matrix)):
            matrix[row_bunny + 1][column_bunny] = "B"


    return matrix, False


matrix = matrix_dimension_input()
player_moves = player_movement_commands()
row_current_position_player, column_current_position_player = player_location(matrix)

is_won = False
is_dead = False
while player_moves:
    next_move = player_moves.popleft()
    if next_move == "U":
        if row_current_position_player - 1 == "B":
            is_dead = True

        elif row_current_position_player - 1 == ".":
            row_current_position_player -= 1
        elif not row_current_position_player - 1 in range(len(matrix)):
            is_won = True

    elif next_move == "D":
        if row_current_position_player + 1 == "B":
            is_dead = True

        elif row_current_position_player + 1 == ".":
            row_current_position_player += 1
        elif not row_current_position_player + 1 in range(len(matrix)):
            is_won = True

    elif next_move == "L":
        if column_current_position_player - 1 == "B":
            is_dead = True

        elif column_current_position_player - 1 == ".":
            row_current_position_player -= 1
        elif not column_current_position_player - 1 in range(len(matrix[0])):
            is_won = True

    elif next_move == "D":
        if column_current_position_player + 1 == "B":
            is_dead = True

        elif column_current_position_player + 1 == ".":
            row_current_position_player += 1
        elif not column_current_position_player + 1 in range(len(matrix[0])):
            is_won = True
    matrix, player_died = bunnies_movement(matrix)
    if any((player_died, is_won, is_dead)):
        break
matrix[row_current_position_player][column_current_position_player] = "."
[print(*x) for x in matrix]

if is_won:
    print(f"won: {row_current_position_player} {column_current_position_player}")
    exit()
if is_dead:
    print(f"dead: {row_current_position_player} {column_current_position_player}")
    exit()

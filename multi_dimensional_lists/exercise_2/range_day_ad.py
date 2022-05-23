import sys
from io import StringIO

input_1 = """. . . . . 
. . . . x
x . x . .
A . x . x 
x . x . . 
4
move up 2
shoot up
move up 2
shoot right"""

#sys.stdin = StringIO(input_1)


def initial_location(matrix: list, position_search_of: str) -> [int, int]:
    position_coordinates = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == position_search_of:
                position_coordinates.append([r, c])
    return position_coordinates


def is_in_matrix_boundaries(next_row: int, next_col: int, matrix):
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        return True
    return False


direction = {
    "up": lambda row, col, step: (row - step, col),
    "down": lambda row, col, step: (row + step, col),
    "right": lambda row, col, step: (row, col + step),
    "left": lambda row, col, step: (row, col - step),
}

#input data
matrix = []
for _ in range(5):
    matrix.append(input().split())

shooter_row, shooter_col = initial_location(matrix, "A")[0]

number_of_commands = int(input())


# main()
target_shooted = 0
_no_more_targets = False
_last_target_coordinates = []
for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        next_row, next_col = direction[command[1]](shooter_row, shooter_col, int(command[2])) # desired move coordinates
        if is_in_matrix_boundaries(next_row, next_col, matrix) and matrix[next_row][next_col] == ".":
                shooter_row, shooter_col = next_row, next_col

    elif command[0] == "shoot":
        next_row_shooter, next_col_shooter = direction[command[1]](shooter_row, shooter_col, 1)
        while is_in_matrix_boundaries(next_row_shooter, next_col_shooter, matrix):
            if matrix[next_row_shooter][next_col_shooter] == "x":
                target_shooted += 1
                matrix[next_row_shooter][next_col_shooter] = "."
                _last_target_coordinates.append([next_row_shooter, next_col_shooter])
                break
            next_row_shooter, next_col_shooter = direction[command[1]](next_row_shooter, next_col_shooter, 1)

    if len(initial_location(matrix, "x")) == 0: # check whether there are any other targets left
        _no_more_targets = True
        break

#print results
if _no_more_targets:
    print(f"Training completed! All {target_shooted} targets hit.")
number_of_targets_left = len(initial_location(matrix, "x"))
if number_of_targets_left > 0:
    print(f"Training not completed! {number_of_targets_left} targets left.")
[print(x) for x in _last_target_coordinates]

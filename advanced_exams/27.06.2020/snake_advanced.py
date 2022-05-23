import sys
from io import StringIO

input_1 = """6
-----S
----B-
------
------
--B---
--*---
left
down
down
down
left"""

#sys.stdin = StringIO(input_1)


def number_rows() -> int:
    return int(input())


def matrix_size(number: int) -> list:
    matrix = []
    for _ in range(number):
        matrix.append([x for x in input()])
    return matrix


def snake_position(matrix: list) -> [int, int]:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "S":
                return row, col


def burrow_position(matrix: list) -> list:
    burrow = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "B":
                burrow.append([row, col])
                if len(burrow) == 2:
                    break
    return burrow if burrow else (None, None)


def is_in_matrix_boundaries(next_row: int, next_col: int, matrix: list) -> bool:
    return True if next_row in range(len(matrix)) and next_col in range(len(matrix[0])) else False


direction = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),

}
# input data
rows_of_matrix = number_rows()
matrix = matrix_size(rows_of_matrix)
row_snake, col_snake = snake_position(matrix)
first_burrow, second_burrow = burrow_position(matrix)
command = input()

is_out_of_matrix = False
is_food_enough = False
food_counter = 0
current_row, current_col = row_snake, col_snake
# main()
while command:


    matrix[current_row][current_col] = "."
    next_row, next_col = direction[command](current_row, current_col)
    if is_in_matrix_boundaries(next_row, next_col, matrix):
        current_row, current_col = next_row, next_col
        if matrix[current_row][current_col] == "*":
            food_counter += 1
            if food_counter == 10:
                is_food_enough = True
        elif [current_row, current_col] == first_burrow:
            matrix[current_row][current_col] = "."
            current_row, current_col = second_burrow
        elif [current_row, current_col] == second_burrow:
            matrix[current_row][current_col] = "."
            current_row, current_col = first_burrow
        matrix[current_row][current_col] = "."
    else:
        is_out_of_matrix = True
    matrix[current_row][current_col] = "S"

    if is_out_of_matrix :
        matrix[current_row][current_col] = "."
        break
    if is_food_enough:
        break

    command = input()

if is_out_of_matrix:
    print("Game over!")
elif is_food_enough:
    print(f'You won! You fed the snake.')

print(f'Food eaten: {food_counter}')
[print("".join(x)) for x in matrix]

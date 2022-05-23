import sys
from io import StringIO

input_1 = """7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right"""

#sys.stdin = StringIO(input_1)


def size_of_matrix():
    return int(input())


def matrix_square(number: int) -> list:
    matrix = []
    for num in range(number):
        matrix.append(input().split())
    return matrix


def alice_position(matrix: list) -> [int, int]:
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "A":
                matrix[row][col] = "*"
                return row, col


def is_in_matrix_boundaries(next_row: int, next_col: int, matrix: list) -> bool:
    return True if next_row in range(len(matrix)) and next_col in range(len(matrix[0])) else False


direction = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

rows_in_matrix = size_of_matrix()
matrix = matrix_square(rows_in_matrix)
alice_row, alice_col = alice_position(matrix)


was_tea_collected = False
is_end = False
tea_bags_counter = 0
command = input()
current_row, current_col = alice_row, alice_col
while command:

    next_row, next_col = direction[command](current_row, current_col)
    if is_in_matrix_boundaries(next_row, next_col, matrix):
        current_row, current_col = next_row, next_col
        if matrix[current_row][current_col] == "R":
            is_end = True
            matrix[current_row][current_col] = "*"
            break
        if matrix[current_row][current_col].isdigit():
            tea_bags_counter += int(matrix[current_row][current_col])
            if tea_bags_counter >= 10:
                was_tea_collected = True
                matrix[current_row][current_col] = "*"
                break

    else:
        is_end = True
        matrix[current_row][current_col] = "*"
        break
    matrix[current_row][current_col] = "*"
    command = input()

if is_end:
    print("Alice didn't make it to the tea party.")
if was_tea_collected:
    print("She did it! She went to the party.")

[print(" ".join(x)) for x in matrix]

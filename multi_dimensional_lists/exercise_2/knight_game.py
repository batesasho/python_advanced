import sys
from collections import deque
from io import StringIO






def number_of_rows():
    return int(input())


def matrix_size(num: int) -> list:
    matrix = []
    for n in range(num):
        matrix.append([x for x in input()])

    return matrix


def is_in_matrix_boundaries(next_row: int, next_col: int, matrix: list) -> bool:
    return True if next_row in range(len(matrix)) and next_col in range(len(matrix[0])) else False

input_1 = """5 
0K0K0
K000K
00K00
K000K
0K0K0"""
#sys.stdin = StringIO(input_1)

horse_moves = {
    "left_one": lambda r, c: (r - 2, c - 1),
    "right_one": lambda r, c: (r - 2, c + 1),
    "left_up": lambda r, c: (r - 1, c - 2),
    "right_up": lambda r, c: (r - 1, c + 2),
    "left_down": lambda r, c: (r + 1, c - 2),
    "right_down": lambda r, c: (r + 1, c + 2),
    "left_two": lambda r, c: (r + 2, c - 1),
    "right_two": lambda r, c: (r + 2, c + 1),
}

matrix_rows = number_of_rows()
matrix = matrix_size(matrix_rows)


count = 0
while True:

    sorted_points = []
    points = deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if matrix[row][col] == "K":
                total_horse_attacked = 0
                for direction, step in horse_moves.items():
                    next_row, next_col = row, col
                    next_row, next_col = step(next_row, next_col)
                    if is_in_matrix_boundaries(next_row, next_col, matrix) and matrix[next_row][next_col] == "K":
                        total_horse_attacked += 1
                points.append([total_horse_attacked, row, col])
    sorted_points = sorted(points, key = lambda x: -x[0])

    if sorted_points[0][0] == 0:
        break
    else:
        matrix[sorted_points[0][1]][sorted_points[0][2]] = "0"
        count += 1


print(count)
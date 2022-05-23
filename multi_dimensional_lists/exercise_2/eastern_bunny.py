import sys
from io import StringIO
from collections import namedtuple

input_1 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 1 27 56 37
1 35 25 37 252 340 56 1
35 X 1 45 4 B 37 63
1005 X 1 2 12 43 5 19
X 19 35 20 32 27 42 4
73 88 1 32 37 52 X 22"""

sys.stdin = StringIO(input_1)


def number_rows():
    return int(input())

def matrix(number: int) -> list:
    matrix = []
    for _ in range(number):
        matrix.append([x if not x.isdigit() else int(x) for x in input().split()])
    return matrix


def bunny_location(matrix: list) -> tuple:
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == "B":
                return row, column


def calculation_sum_of_eggs(matrix, bunny_position: tuple) -> tuple:
    row_bunny, column_bunny = bunny_position

    right_sum = sum([n if not n == "B" else 0 for n in matrix[row_bunny][column_bunny+1 if column_bunny != len(matrix[0]) else 0:None if "X" not in matrix[row_bunny][column_bunny+1:] else matrix[row_bunny].index("X")]])
    right_list_length = len([n if not n == "B" else 0 for n in matrix[row_bunny][column_bunny+1 if column_bunny != len(matrix[0]) else 0:None if "X" not in matrix[row_bunny][column_bunny+1:] else matrix[row_bunny].index("X")]])
    right_coordinates = [[row_bunny,column_move] if not right_list_length == 1 else None for column_move in range(1, right_list_length + 1)]

    left_sum = sum([n if not n == "B" else 0 for n in matrix[row_bunny][column_bunny-1 if column_bunny != 0 else 0:None if "X" not in matrix[row_bunny][:column_bunny] else matrix[row_bunny][:column_bunny].index("X"):-1]])
    left_list_length = len([n if not n == "B" else 0 for n in matrix[row_bunny][column_bunny-1 if column_bunny != 0 else 0:None if "X" not in matrix[row_bunny][:column_bunny] else matrix[row_bunny][:column_bunny].index("X"):-1]])
    left_coordinates = [[row_bunny, column_move] if not left_list_length == 1 else None for column_move in range(1, left_list_length + 1)]

    up_list = [matrix[row][column_bunny] for row in range(len(matrix[:row_bunny]))]
    up_sum = sum(n if not n == "B" else 0 for n in up_list[-1:None if "X" not in up_list else up_list.index("X"):-1])
    up_list_length = len([n if not n == "B" else 0 for n in up_list[-1:None if "X" not in up_list else up_list.index("X"):-1]])
    up_coordinates = [[row_bunny - row_move, column_bunny]for row_move in range(up_list_length, 0, -1)]

    down_list = [matrix[row_bunny+row + 1][column_bunny] for row in range(len(matrix[row_bunny+1:]))]
    down_sum = sum(n if not n == "B" else 0 for n in down_list[:None if "X" not in down_list else down_list.index("X")])
    down_list_length = len([n if not n == "B" else 0 for n in down_list[:None if "X" not in down_list else down_list.index("X")]])
    down_coordinates = [[row_bunny+row_move, column_bunny] for row_move in range(1, down_list_length + 1)]

    max_direction = [up_sum, down_sum, right_sum, left_sum]
    max_coordinates = [up_coordinates, down_coordinates, right_coordinates, left_coordinates]

    Direction = namedtuple("Direction", "left right up down")
    direction = Direction(left_sum, right_sum, up_sum, down_sum)

    return max(max_direction), max_coordinates[max_direction.index(max(max_direction))], direction._fields[direction.index(max(direction))]


def print_result(max_value:int, coordinates: list, diretion:str) -> print:
    print(diretion)
    print(*coordinates, sep = "\n")
    print(max_value)

matrix_size = number_rows()
matrix = matrix(matrix_size)
bunny_location = bunny_location(matrix)
max_value, coordinates, direction = calculation_sum_of_eggs(matrix, bunny_location)
print_result(max_value, coordinates, direction)

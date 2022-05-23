import sys
from collections import namedtuple
from io import StringIO

input_1 = """8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK"""

sys.stdin = StringIO(input_1)


def matrix_input() -> list:
    matrix_ = []
    matrix_rows = int(input())
    for _ in range(matrix_rows):
        matrix_.append([x for x in input()])
    return matrix_


def check_horse_possible_positions(matrix: list) -> int:

    max_count = 0
    Rows_positions, Column_positions = namedtuple("Rows_positions", "x"), namedtuple("Column_positions", "y")
    rows_positions, column_positions = Rows_positions([2, 2, -2, -2, -1, -1, 1, 1]), \
                                       Column_positions([1, -1, 1, -1, -2, 2, 2, -2])
    removed_counter = 0
    row_column_indecies = []
    while True:
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                count = 0
                if matrix[row][column] == "K":
                    for index_horse_options in range(len(rows_positions.x)):
                        row_option = rows_positions.x[index_horse_options]
                        column_option = column_positions.y[index_horse_options]
                        if row + row_option in range(len(matrix)) and column + column_option in range(len(matrix[0])):
                            if matrix[row + row_option][column + column_option] == "K":
                                count += 1
                if max_count < count:
                    max_count = count
                    row_column_indecies = [row, column]

        if row_column_indecies:
            matrix[row_column_indecies[0]][row_column_indecies[1]] = "0"
            row_column_indecies =[]

            removed_counter += 1

        else:
            break
    return removed_counter



matrix = matrix_input()
count_attacker_dict = check_horse_possible_positions(matrix)
print(count_attacker_dict)

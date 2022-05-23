import sys
from io import StringIO

input_1 = """3
4
- X - -
S C V -
- V - -
- - - -
right
Christmas morning"""


#sys.stdin = StringIO(input_1)

def number_of_presents_value():
    return int(input())


def size_of_rows_matrix():
    return int(input())


def santa_location(matrix: list) -> [int, int]:
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "S":
                return row, col


def is_in_matrix_boundaries(next_row, next_col, matrix):
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        return True
    return False


def is_nice_kids_left(matrix: list) -> int:
    nice_kids_list = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "V":
                nice_kids_list += 1

    return nice_kids_list


def matrix_size(rows: int) -> list:
    matrix = []

    for i in range(size_of_matrix):
        matrix.append([x for x in input().split()])
    return matrix


def print_results(matrix: list, is_run_out_of_presents: bool, good_kids_received_presents_counter: int) -> print:
    any_kids_left = is_nice_kids_left(matrix)
    if is_run_out_of_presents and any_kids_left > 0:
        print("Santa ran out of presents!")

    [print(" ".join(x)) for x in matrix]

    if any_kids_left == 0:
        print(f'Good job, Santa! {good_kids_received_presents_counter} happy nice kid/s.')
    else:
        print(f"No presents for {any_kids_left} nice kid/s.")


# input data
number_presents = number_of_presents_value()
size_of_matrix = size_of_rows_matrix()
matrix = matrix_size(size_of_matrix)

# initial location of santa'
santa_row, santa_col = santa_location(matrix)

# 4 directions movement allowed by definition.
direction = {
    "up": lambda row, col: (row - 1, col),
    "down": lambda row, col: (row + 1, col),
    "right": lambda row, col: (row, col + 1),
    "left": lambda row, col: (row, col - 1),
}

# main ()
command = input()

good_kids_received_presents_counter = 0
is_run_out_of_presents = False
while command:
    if command == "Christmas morning":
        break
    matrix[santa_row][santa_col] = "-"  # position of Santa replaced by "-"
    next_row, next_col = direction[command](santa_row, santa_col)
    if is_in_matrix_boundaries(next_row, next_col, matrix):
        santa_row, santa_col = next_row, next_col
        if matrix[santa_row][santa_col] == "V":
            number_presents -= 1
            good_kids_received_presents_counter += 1
        elif matrix[santa_row][santa_col] == "C":
            for move, step in direction.items():  # check all directions for children
                next_row_check, next_col_check = step(santa_row, santa_col)
                if is_in_matrix_boundaries(next_row_check, next_col_check, matrix): # check "C" is on border row/col cell
                    if matrix[next_row_check][next_col_check] == "V" or \
                            matrix[next_row_check][next_col_check] == "X":
                        number_presents -= 1
                        good_kids_received_presents_counter += 1 if matrix[next_row_check][next_col_check] == "V" else 0
                    if not matrix[next_row_check][next_col_check] == "C":
                        matrix[next_row_check][next_col_check] = "-" # replaces all children found who received presents with "-"
        matrix[santa_row][santa_col] = "S"  # final location of santa marked with "S"

    if number_presents <= 0:
        is_run_out_of_presents = True
        break
    try:
        command = input()
    except:
        break
print_results(matrix, is_run_out_of_presents, good_kids_received_presents_counter)

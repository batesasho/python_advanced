import sys
from io import StringIO

input_1 = """3 2"""

sys.stdin = StringIO(input_1)


def matrix_size_input() -> tuple:
    rows, column = list(map(int, input().split()))
    return rows, column


def matrix_not_palindrome(row: int, column: int) -> list:
    matrix = []
    number_of_letters = 3  # pre-defined value
    [matrix.append(chr(97 + r) * number_of_letters) for r in range(row) for c in range(column)]
    matrix = [matrix[x:x + column] for x in range(0, len(matrix), column)]
    return matrix


def palindrome_matrix(matrix: list, row: int, column: int) -> list:
    palindrome_matrix_list = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            temporarily_list_ = []
            temporarily_list_.extend(matrix[row][column])
            temporarily_list_[1] = chr(ord(temporarily_list_[1]) + column)
            palindrome_matrix_list.append("".join(temporarily_list_))

    return palindrome_matrix_list


def print_result(matrix: list,  column: int) -> "printing result":
    [print(*matrix[x:x+column]) for x in range(0, len(matrix), column)]


matrix_row, matrix_column = matrix_size_input()
matrix_created_not_palindrome = matrix_not_palindrome(matrix_row, matrix_column)
matrix_palindrome = palindrome_matrix(matrix_created_not_palindrome, matrix_row, matrix_column)
print_result(matrix_palindrome, matrix_column)

import sys
from io import StringIO

input_1 = """1| 4 5 6 7  |  8 9"""

#sys.stdin = StringIO(input_1)


def matrix_input() -> list:
    matrix = input().split("|")
    matrix = [matrix[x].split() for x in range(len(matrix))][::-1]
    return matrix


def flatten_matrix(matrix: list) -> list:
    matrix = [matrix[x][y] for x in range(len(matrix)) for y in range(len(matrix[x]))]
    return matrix


def printing_result(matrix: str) -> "printing results - flatten matrix separate by space":
    print(*[x for x in matrix], sep = " ")


matrix = matrix_input()
flatten_matrix_list = flatten_matrix(matrix)
printing_result(flatten_matrix_list)

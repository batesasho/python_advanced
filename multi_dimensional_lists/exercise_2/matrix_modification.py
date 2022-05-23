import sys
from io import StringIO

input_1 = """4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END"""

#sys.stdin = StringIO(input_1)


def matrix_input(number) -> list:
    matrix = []
    for _ in range(number):
        matrix.append(input())
    matrix = [matrix[row].split() for row in range(len(matrix))]
    matrix = [int(matrix[row][col]) for row in range(len(matrix)) for col in range(len(matrix[0]))]
    matrix = [matrix[x:x + number] for x in range(0, len(matrix), number)]
    return matrix


def invalid_coordinates() -> print:
    print('Invalid coordinates')


def printing_result(matrix: list) -> print:
    [print(*x) for x in matrix]


number = int(input())
matrix_size = matrix_input(number)

command = input()

while not command == "END":
    modification, row, column, value = command.split()
    row = int(row)
    column = int(column)
    value = int(value)
    if row in range(len(matrix_size)) and column in range(len(matrix_size[row])):
        if modification == "Add":
            matrix_size[row][column] += value
        elif modification == "Subtract":
            matrix_size[row][column] -= value
    else:
        invalid_coordinates()

    command = input()
else:
    printing_result(matrix_size)

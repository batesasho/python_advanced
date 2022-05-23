def matrix_size(num: int) -> list:
    matrix = []
    for row in range(num):
        matrix.append([x for x in input().split(", ")])
    return matrix


def row_of_matrix() -> int:
    return int(input())


def player(matrix: list, row = 0, col = 0):
    row, col = input("Please choose a column:")
    return matrix[row][col]


rows_of_matrix = row_of_matrix()
matrix = matrix_size(rows_of_matrix)

while True:

    player_one =

    player_one, player_two = player_two, player_one

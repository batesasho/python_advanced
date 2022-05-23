def matrix_size(number: int) -> list:
    matrix = []
    for num in range(number):
        matrix.append([x for x in input()])
    return matrix


def player_location(matrix: list) -> tuple:
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "P":
                return row, col


def is_in_matrix_boundaries(matrix: list, next_row: int, next_column: int) -> bool:
    if next_row in range(len(matrix)) and next_column in range(len(matrix)):
        return True
    return False

def is_alpha_check(matrix, row, column, string):
    if matrix[row_player_position][column_player_position].isalpha():
        string += matrix[row_player_position][column_player_position]
        matrix[row_player_position][column_player_position] = "-"
    return matrix, row, column, string


string = input()
number_rows_matrix = int(input())
matrix = matrix_size(number_rows_matrix)
number_of_commands = int(input())
row_player_position, column_player_position = player_location(matrix)
matrix[row_player_position][column_player_position] = "-"
for num in range(number_of_commands):
    command = input()
    if command == "up":
        if is_in_matrix_boundaries(matrix, row_player_position - 1, column_player_position):
            row_player_position -= 1
            matrix, row_player_position, column_player_position, string = is_alpha_check(matrix, row_player_position, column_player_position, string)
        else:
            string = string[:-1]
    elif command == "down":
        if is_in_matrix_boundaries(matrix, row_player_position + 1, column_player_position):
            row_player_position += 1
            matrix, row_player_position, column_player_position, string = is_alpha_check(matrix, row_player_position,
                                                                                         column_player_position, string)
        else:
            string = string[:-1]
    elif command == "right":
        if is_in_matrix_boundaries(matrix, row_player_position, column_player_position + 1):
            column_player_position += 1
            matrix, row_player_position, column_player_position, string = is_alpha_check(matrix, row_player_position, column_player_position, string)
        else:
            string = string[:-1]
    elif command == "left":
        if is_in_matrix_boundaries(matrix, row_player_position, column_player_position - 1):
            column_player_position -= 1
            matrix, row_player_position, column_player_position, string = is_alpha_check(matrix, row_player_position, column_player_position, string)
        else:
            string = string[:-1]
    if num == number_of_commands - 1:
        matrix[row_player_position][column_player_position] = "P"
print(string)
[print("".join(map(str, x))) for x in matrix]

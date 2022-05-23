import sys
from collections import deque
from io import StringIO

input_1 = """5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *"""

#sys.stdin = StringIO(input_1)


def matrix_size_input_() -> int:
    return int(input())


def movements() -> deque:
    return deque(input().split())


def matrix_square(number: int) -> list:
    matrix_square = []
    for _ in range(number):
        matrix_square.append(input().split())
    return matrix_square


def start_position(matrix: list) -> tuple:
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 's':
                return row, column


def count_coal_in_matrix(matrix: list) -> int:
    count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 'c':
                count += 1
    return count


def check_found_coal_substitute_with_asterisk(matrix: list, next_move_row, next_move_column, count_coal: int) -> tuple:
    if matrix[next_move_row][next_move_column] == "c":
        count_coal += 1
        matrix[next_move_row][next_move_column] = "*"
        if count_coal == check_all_coals_in_matrix:
            print(f"You collected all coal! ({next_move_row}, {next_move_column})")
            exit()
    return matrix, count_coal


def check_end_of_miner_path(matrix: list, next_move_row, next_move_column):
    if matrix[next_move_row][next_move_column] == "e":
        print(f"Game over! ({next_move_row}, {next_move_column})")
        exit()
    return


def miner_movement(matrix: list, initial_position: tuple, movement_commands: deque,
                   total_coal_in_matrix: int) -> None:
    initial_row, initial_column = initial_position
    next_move_row, next_move_column = initial_row, initial_column
    matrix_boundary = len(matrix)
    count_coal = 0
    current_move = ''
    while movement_commands:
        current_move = movement_commands.popleft()
        if current_move == "up":
            if next_move_row - 1 in range(matrix_boundary):
                next_move_row -= 1
                matrix, count_coal = check_found_coal_substitute_with_asterisk(matrix, next_move_row, next_move_column,
                                                                               count_coal)
                check_end_of_miner_path(matrix, next_move_row, next_move_column)
        elif current_move == "down":
            if next_move_row + 1 in range(matrix_boundary):
                next_move_row += 1
                matrix, count_coal = check_found_coal_substitute_with_asterisk(matrix, next_move_row, next_move_column,
                                                                               count_coal)
                check_end_of_miner_path(matrix, next_move_row, next_move_column)
        elif current_move == "left":
            if next_move_column - 1 in range(matrix_boundary):
                next_move_column -= 1
                matrix, count_coal = check_found_coal_substitute_with_asterisk(matrix, next_move_row, next_move_column,
                                                                               count_coal)
                check_end_of_miner_path(matrix, next_move_row, next_move_column)
        elif current_move == "right":
            if next_move_column + 1 in range(matrix_boundary):
                next_move_column += 1
                matrix, count_coal = check_found_coal_substitute_with_asterisk(matrix, next_move_row, next_move_column,
                                                                               count_coal)
                check_end_of_miner_path(matrix, next_move_row, next_move_column)
    else:
        number_of_remaining_coal = total_coal_in_matrix - count_coal
        print(f"{number_of_remaining_coal} pieces of coal left. ({next_move_row}, {next_move_column})")


size_of_matrix = matrix_size_input_()
movement = movements()
matrix = matrix_square(size_of_matrix)
miner_initial_position = start_position(matrix)
check_all_coals_in_matrix = count_coal_in_matrix(matrix)
miner_movement(matrix, miner_initial_position, movement, check_all_coals_in_matrix )

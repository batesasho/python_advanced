def matrix_size_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            [1, 2, 3],
            [4, 5, 6],
        ]
    else:
        matrix_ = []
        row_matrix, column_matrix = input().split()
        row_matrix = int(row_matrix)
        for row_elements in range(row_matrix):
            matrix_.append(input().split())
    return matrix_


def commands(is_judge = True):
    matrix_commands = []
    if is_judge == False:
        matrix_commands = [
            ['swap', 0, 0, 1, 1],
            ['swap', 10, 9, 8, 7],
            ['swap', 0, 1, 1, 0],
        ]
    else:
        command = input()
        while not command == "END":
            matrix_commands.append(command.split())
            command = input()

    return matrix_commands


def valid_input_check(command_matrix: list, matrix: list):
    if not command_matrix[0] == 'swap' or not len(command_matrix[1:]) == 4 or not int(command_matrix[1]) in range(
            len(matrix)) or not int(command_matrix[3]) in range(len(matrix)) or not int(command_matrix[2]) in range(len(matrix[0])) or not int(command_matrix[4]) in range(len(matrix[0])):
        return False
    return True


def coordinates_matrix_input(command_matrix_entered: list):
    row1, col1, row2, col2 = [command_matrix_entered[x] for x in range(1, 5)]
    return int(row1), int(col1), int(row2), int(col2)


def swap_change(matrix: list, row_one: int, column_one: int, row_two: int, column_two: int):
    matrix[row_one][column_one], matrix[row_two][column_two] = matrix[row_two][column_two], matrix[row_one][column_one]
    return matrix


def print_result_after_ok_validation(swapped_matrix_: list):
    [print(*rows) for rows in swapped_matrix_]

matrix_size = matrix_size_input()
matrix_commands = commands()

for number_of_swaps in range(len(matrix_commands)):
    matrix_commands_input_validation = valid_input_check(matrix_commands[number_of_swaps],
                                                         matrix_size)
    if matrix_commands_input_validation:
        matrix_coordinates_export = coordinates_matrix_input(matrix_commands[number_of_swaps])
        swapped_matrix = swap_change(matrix_size, *matrix_coordinates_export)
        print_result_after_ok_validation(swapped_matrix)
    else:
        print('Invalid input!')

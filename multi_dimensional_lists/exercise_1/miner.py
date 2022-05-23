def matrix_input(is_judge=True):
    if is_judge == False:
        matrix_ = [
            ["*", "*", "*", "c", "*"],
            ["*", "*", "*", "e", "*"],
            ["*", "*", "c", "*", "*"],
            ["s", "*", "*", "c", "*"],
            ["*", "*", "c", "*", "*"],
        ]
    else:
        matrix_ = []
        row_matrix = int(input())

        for row_elements in range(row_matrix):
            matrix_.append(input().split())
    return matrix_


def commands_for_matrix_manipulation(is_judge=True):
    if not is_judge:
        return ["up", "right", "right", "up", "right"]
    return input().split()


def find_initial_location(matrix: list):
    row_initial_location = 0
    column_initial_location = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == "s":
                row_initial_location = row
                column_initial_location = column
    return [row_initial_location, column_initial_location]


def miner_movement(matrix: list, starting_location: list, different_commands: list):
    row_current_location, column_current_location = starting_location
    current_location = matrix[row_current_location][column_current_location]
    miner_path = current_location
    try:
        for command in different_commands:
            if command == "left":
                column_current_location -= 1
                current_location = matrix[row_current_location][column_current_location]
            elif command == "right":
                column_current_location += 1
                current_location = matrix[row_current_location][column_current_location]
            elif command == "up":
                row_current_location -= 1
                current_location = matrix[row_current_location][column_current_location]
            elif command == "down":
                row_current_location += 1
                current_location = matrix[row_current_location][column_current_location]
            miner_path += current_location

            if miner_path[-1] == "e":
                pass  # return current_location, miner_path
            elif miner_path[-1] == "c":
                matrix[row_current_location][column_current_location] = "*"
    except:
        pass

    return matrix, miner_path


def calculation_of_harvested_coal(miner_path: str):
    return miner_path.count("c")


matrix_size = matrix_input(is_judge=False)
matrix_command = commands_for_matrix_manipulation(is_judge=False)
initial_location = find_initial_location(matrix_size)
matrix_miner_move, miner_path = miner_movement(
    matrix_size, initial_location, matrix_command
)
number_of_harvested_coal = calculation_of_harvested_coal(miner_path)

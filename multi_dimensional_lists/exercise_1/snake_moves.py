def matrix_size_input(is_judge = True):
    if is_judge == False:
        row_matrix, column_matrix = [
            5, 6
        ]
    else:
        row_matrix, column_matrix = input().split()
        row_matrix = int(row_matrix)
        column_matrix = int(column_matrix)
    return row_matrix, column_matrix


def snake_string(is_judge = True):
    if is_judge == False:
        return "SoftUni"
    return input()


def snake_movement_slicing(snake: str, matrix_row: int, matrix_column: int):
    snake_move = snake * matrix_row * matrix_column
    new = [snake_move[x: x + matrix_column] for x in range(0, len(snake_move), matrix_column)]
    return new[:matrix_row]


def snake_move():
    snake_move_matrix = snake_movement_slicing(snake_string, row_matrix, column_matrix)
    return [snake_move_matrix[x][::-1] if not x % 2 == 0 else snake_move_matrix[x] for x in
            range(len(snake_move_matrix))]


def print_result(snake_movement_matrix: list):
    [print(x) for x in snake_movement_matrix]


row_matrix, column_matrix = matrix_size_input()
snake_string = snake_string()
snake_moves_matrix = snake_move()
print_result(snake_moves_matrix)

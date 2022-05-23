def matrix_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            [8, 3, 2, 5],
            [6, 4, 7, 9],
            [9, 9, 3, 6],
            [6, 8, 1, 2],
        ]
    else:
        matrix_ = []
        row_matrix = int(input())

        for row_elements in range(row_matrix):
            matrix_.append(list(map(int, input().split())))

    return matrix_


def coordinates_of_bombs(is_judge = True):
    if is_judge == False:
        coordinates = [
            [1, 2],
            [2, 1],
            [2, 0],
        ]
    else:
        coordinates = (input().split())
        coordinates_integer = [coordinates[y].split(",") for y in range(len(coordinates))]
        coordinates_integer = [int(x) for y in coordinates_integer for x in y]

    return [coordinates_integer[x:x + 2] for x in range(0, len(coordinates_integer), 2)]


def detonation_bomb(matrix: list, coordinates_bomb: list):
    row_bomb = coordinates_bomb[0]
    column_bomb = coordinates_bomb[1]
    number_bomb = matrix[row_bomb][column_bomb]
    if number_bomb <= 0:
        return matrix
    try:
        for row_index in range(row_bomb - 1, row_bomb + 2):
            if row_index < 0:
                continue
            for column_index in range(len(matrix[row_index])):
                if column_index in range(column_bomb - 1, column_bomb + 2):
                    if column_index < 0:
                        continue
                    if row_index == row_bomb and column_index == column_bomb:
                        continue
                    else:
                        if not matrix[row_index][column_index] <= 0:
                            matrix[row_index][column_index] -= number_bomb
    except:
        pass
    matrix[row_bomb][column_bomb] = 0

    return matrix

    # # adding Zeroes around the matrix
    # for row in range(len(matrix)):
    #     matrix[row].insert(0, 0)
    #     matrix[row].append(0)
    # matrix.insert(0, [0] * (len(matrix[0])))
    # matrix.append([0] * (len(matrix[0])))


def remain_cells_sum_value(matrix_detonated: list):
    alive_cells_count = 0
    sum_values_alive_cells = 0
    filtered_list = [x for y in matrix_detonated for x in y if x > 0]
    alive_cells_count = len(filtered_list)
    sum_values_alive_cells = sum(filtered_list)

    return (alive_cells_count, sum_values_alive_cells)


def print_result(matrix_modified):
    alive_cells, sum_values = remain_cells_sum_value(matrix_size)
    print(f'Alive cells: {alive_cells}')
    print(f'Sum: {sum_values}')
    [print(*x) for x in matrix_modified]


matrix_size = matrix_input()
bomb_coordinates = coordinates_of_bombs()
for coordinates in bomb_coordinates:
    matrix_size = detonation_bomb(matrix_size, coordinates)

print_result(matrix_size)

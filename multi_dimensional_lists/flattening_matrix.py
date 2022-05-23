def matrix_input(is_judge = True):
    if is_judge == False:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
        ]
    else:
        matrix = []
        row_matrix = int(input())

        for row_elements in range(row_matrix):
            matrix.append(list(map(int, input().split(', '))))
    return matrix


def combine_elements_of_matrix(matrix: list):
    flattening_matrix = []
    for rows in range(len(matrix)):
        for column in matrix[rows]:
            flattening_matrix.append(column)
    return flattening_matrix


def print_result(combined_matrix: list):
    print(combined_matrix)


matrix_size = matrix_input()
flattening_matrix = combine_elements_of_matrix(matrix_size)
print_result(flattening_matrix)




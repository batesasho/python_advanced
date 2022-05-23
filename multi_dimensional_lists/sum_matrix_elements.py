def matrix_input(is_judge = True):
    if is_judge == False:
        matrix = [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        matrix = []
        row_matrix, column_matrix = input().split(', ')
        row_matrix = int(row_matrix)
        column_matrix = int(column_matrix)
        for row_elements in range(row_matrix):
            matrix.append(list(map(int,input().split(', '))))
    return matrix


def sum_all_elements_matrix(matrix: list):
    sum_value = 0
    for row in matrix:
        for elements in row:
            sum_value += elements
    return sum_value


def print_result(matrix: list, total_sum_elements: int):
    print(total_sum_elements)
    print(matrix)


matrix = matrix_input()
sum_of_matrix_elements = sum_all_elements_matrix(matrix)
print_result(matrix, sum_of_matrix_elements)


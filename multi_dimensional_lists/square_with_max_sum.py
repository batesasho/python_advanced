from sys import maxsize


def matrix_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        matrix_ = []
        row_matrix, column_matrix = input().split(', ')
        row_matrix = int(row_matrix)
        column_matrix = int(column_matrix)
        for row_elements in range(row_matrix):
            matrix_.append(list(map(int, input().split(', '))))

    return matrix_


def sum_of_2x2_matrix(matrix_list: list):
    sum_2x2 = 0
    max_sum = -maxsize
    list_elements = []
    for row in range(len(matrix_list) - 1):
        for column in range(len(matrix_list[row]) - 1):
            sum_2x2 = matrix_list[row][column] + matrix_list[row][column + 1] + matrix_list[row + 1][column] + \
                      matrix_list[row + 1][column + 1]
            if sum_2x2 > max_sum:
                max_sum = sum_2x2
                list_elements = [matrix_list[row][column], matrix_list[row][column + 1]], [matrix_list[row + 1][column],
                                                                                           matrix_list[row + 1][
                                                                                               column + 1]]
    return (list_elements, max_sum)


def print_result(matrix_max_elements: list, sum_of_max_elements: int):
    [print(*(map(str,x))) for x in matrix_max_elements]
    print(sum_of_max_elements)


matrix = matrix_input()
matrix_max_elements, sum_value = sum_of_2x2_matrix(matrix)
print_result(matrix_max_elements, sum_value)

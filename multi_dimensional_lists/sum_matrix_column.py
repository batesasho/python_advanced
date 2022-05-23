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
            matrix.append(list(map(int, input().split())))

    return matrix


def sum_all_elements_per_column(list_elements_in_matrix: list):
    summed_elements_list = []
    for column in range(len(list_elements_in_matrix[0])):
        sum_elements_in_each_column = 0
        for row in range(len(list_elements_in_matrix)):
            sum_elements_in_each_column += list_elements_in_matrix[row][column]
        summed_elements_list.append(sum_elements_in_each_column)
    return summed_elements_list


def print_result(list_with_results: list):
    print(*list_with_results, sep = "\n")


matrix = matrix_input()
sum_all_el_in_columns = sum_all_elements_per_column(matrix)
print_result(sum_all_el_in_columns)

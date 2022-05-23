def matrix_input(is_judge = True):
    if is_judge == False:
        matrix = [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, - 12],

        ]
    else:
        matrix = []
        row_matrix = int(input())
        for row_elements in range(row_matrix):
            matrix.append(list(map(int, input().split())))
    return matrix


def sum_primary_diagonal(matrix_elements: list):
    sum_primary_diagonal = 0
    for column in range(len(matrix_elements)):
        sum_primary_diagonal += matrix_elements[column][column]
    return sum_primary_diagonal


def print_result(summed_value_primary_diagonal: int):
    print(summed_value_primary_diagonal)


matrix_elements = matrix_input()
sum_elements_in_primary_diagonal = sum_primary_diagonal(matrix_elements)
print_result(sum_elements_in_primary_diagonal)


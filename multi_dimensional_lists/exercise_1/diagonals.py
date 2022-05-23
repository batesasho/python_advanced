def matrix_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, - 12],

        ]
    else:
        matrix_ = []
        row_matrix = int(input())

        for row_elements in range(row_matrix):
            matrix_.append(list(map(int, input().split(', '))))

    return matrix_


def primary_diagonal_elements_sum(matrix: list):
    sum_primary_diagonal = 0
    primary_diagonal_list = []
    for row in range(len(matrix)):
        sum_primary_diagonal += matrix[row][row]
        primary_diagonal_list.append(matrix[row][row])
    return primary_diagonal_list, sum_primary_diagonal


def secondary_diagonal_elements_sum(matrix: list):
    sum_secondary_diagonal = 0
    secondary_diagonal_list= []
    for row in range(len(matrix)):
        sum_secondary_diagonal += matrix[row][-1-row]
        secondary_diagonal_list.append(matrix[row][-1-row])
    return secondary_diagonal_list, sum_secondary_diagonal


def print_result(primary_list: list, primary_sum: int, secondary_list: list, secondary_sum: int):
    print(f'Primary diagonal: {", ".join(map(str,primary_list))}. Sum: {primary_sum}')
    print(f'Secondary diagonal: {", ".join(map(str,secondary_list))}. Sum: {secondary_sum}')




matrix_elements = matrix_input()
print_result(*primary_diagonal_elements_sum(matrix_elements), *secondary_diagonal_elements_sum(matrix_elements))








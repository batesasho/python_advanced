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
            matrix_.append(list(map(int, input().split())))

    return matrix_


def primary_diagonal_elements_sum(matrix: list):
    sum_primary_diagonal = 0
    for row in range(len(matrix)):
        sum_primary_diagonal += matrix[row][row]
    return sum_primary_diagonal

def secondary_diagonal_elements_sum(matrix: list):
    sum_secondary_diagonal = 0
    for row in range(len(matrix)):
        sum_secondary_diagonal += matrix[row][-1-row]
    return sum_secondary_diagonal


def calc_difference_both_diagonals(primary_diagonal, secondary_diagonal):
    return abs(primary_diagonal - secondary_diagonal)


def print_result(difference_diagonals):
    print(difference_diagonals)


matrix_elements = matrix_input()
matrix_primary_diagonal = primary_diagonal_elements_sum(matrix_elements)
matrix_secondary_diagonal = secondary_diagonal_elements_sum(matrix_elements)
matrix_difference_calc = calc_difference_both_diagonals(matrix_primary_diagonal, matrix_secondary_diagonal)
print_result(matrix_difference_calc )

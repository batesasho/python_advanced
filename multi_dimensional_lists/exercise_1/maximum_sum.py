from sys import maxsize


def matrix_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4],

        ]
    else:
        matrix_ = []
        row_matrix = int(input().split()[0])

        for row_elements in range(row_matrix):
            matrix_.append(list(map(int, input().split())))
    return matrix_


def max_value_sum_3x3_size(matrix: list):
    max_summed_value = - maxsize
    for row in range(len(matrix) - 2):
        for column in range(len(matrix[row]) - 2):
            summed_value_3x3_size = []
            sum_sub_matrix = 0
            summed_value_3x3_size = [matrix[row+x][column+y] for x in range(3) for y in range(3)]
            summed_value_3x3_size = [summed_value_3x3_size[x:x+3] for x in range(0, len(summed_value_3x3_size), 3)]
            sum_sub_matrix = sum(sum(x) for x in summed_value_3x3_size)
            if sum_sub_matrix > max_summed_value:
                max_summed_value = sum_sub_matrix
                max_summed_value_3x3_size = summed_value_3x3_size
    return max_summed_value_3x3_size, max_summed_value

def print_result(summed_value: list, total_sum_elements_max: int):
    print(f'Sum = {total_sum_elements_max}')
    [print(*x) for x in summed_value]


matrix = matrix_input()
max_summed_value_3x3_size, total_sum = max_value_sum_3x3_size(matrix)
print_result(max_summed_value_3x3_size, total_sum)

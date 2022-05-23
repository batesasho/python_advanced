def matrix_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            ["A", "B", "B", "D"],
            ["E", "B", "B", "B"],
            ["I", "J", "B", "B"],

        ]
    else:
        matrix_ = []
        row_matrix = int(input().split()[0])
        for row_elements in range(row_matrix):
            matrix_.append(input().split())

    return matrix_


def count_number_of_chars_2x2(matrix: list):
    count = 0
    for row in range(len(matrix)-1):
        for column in range(len(matrix[row])-1):
            if matrix[row][column] == matrix[row][column+1] == matrix[row+1][column+1] == matrix[row+1][column]:
                count += 1
    return count


def print_result(number_of_equal_chars):
    print(number_of_equal_chars)


matrix = matrix_input()
print_result(count_number_of_chars_2x2(matrix))
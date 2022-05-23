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


def even_elements_matrix(matrix: list):
    even_elements_matrix = []
    for row in range(len(matrix)):
        even_elements_matrix.append(list(filter(lambda x: x % 2 == 0 , matrix[row])))
        # even_elements_matrix.append([])
        # for element in matrix[row]:
        #     if element %2 == 0:
        #         even_elements_matrix[row].append(element)
    return even_elements_matrix


def print_result(even_matrix: list):
    print(even_matrix)


matrix = matrix_input()
filter_even_elements = even_elements_matrix(matrix)
print_result(filter_even_elements)

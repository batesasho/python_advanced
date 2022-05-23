def matrix_input(is_judge = True):
    if is_judge == False:
        matrix_ = [
            'ABC',
            'DEF',
            'X!@',
        ]
    else:
        matrix_ = []
        row_matrix = int(input())
        for row_elements in range(row_matrix):
            matrix_.append(input())
    return matrix_


def find_special_symbol_index(matrix: list, special_symbol: str):
    special_sym_row = 0
    special_sym_column = 0
    is_found = False
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == special_symbol:
                special_sym_column = column
                special_sym_row = row
                is_found = True
                break
        if is_found:
            break
    return (special_sym_row, special_sym_column)


def print_result(spec_row, spec_col, special_symbol):
    if spec_row:
        print(f"({spec_row}, {spec_col})")
    else:
        print(f"{special_symbol} does not occur in the matrix")



matrix = matrix_input()
search_symbol = input()
print_result(*find_special_symbol_index(matrix, search_symbol), search_symbol)



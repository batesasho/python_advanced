import sys
from io import StringIO

input_1 = """UL . . U . . UR .
. UL . U . UR . .
. . UL U UR . . .
L L L Q R R R R
Q . DL D Q . . .
. Q . D . UL . .
K . . D . . Q .
. Q . Q . . . UL"""
sys.stdin = StringIO(input_1)

matrix = [input().split() for _ in range(8)]

directions = {"right": lambda r, c: (r, c + 1),
              "left": lambda r, c: (r, c - 1),
              "up": lambda r, c: (r - 1, c),
              "down": lambda r, c: (r + 1, c),
              "left_up_diagonal": lambda r, c: (r - 1, c - 1),
              "right_up_diagonal": lambda r, c: (r - 1, c + 1),
              "left_down_diagonal": lambda r, c: (r + 1, c - 1),
              "right_down_diagonal": lambda r, c: (r + 1, c + 1),
              }


def is_in_board_boundaries(row, col, matrix):
    return row in range(len(matrix)) and col in range(len(matrix))


queen_positions_list = []
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "Q":
            for direction, step in directions.items():
                current_row, current_col = row, col
            # right_checkmate = [x for x in matrix[row][col + 1:]]
            # left_checkmate = [x for x in matrix[row][col - 1::-1]]
            # up_checkmate = [matrix[row_][col_] for row_ in range(row - 1, -1, -1) for col_ in range(col, col+1)]
            # down_checkmate = [matrix[row_][col_] for row_ in range(row + 1, len(matrix)) for col_ in
            #                   range(col, col + 1)]
            # up_left_diagonal_checkmate = [matrix[row_][col_] for row_ in range(row - 1, - 1, -1) for col_ in range(col ,col + 1)]
            # up_right_diagonal_checkmate = [matrix[row_][col_] for row_ in range(row - 1, - 1, -1) for col_ in
            #                               range(len(matrix) - row - 1, len(matrix) - row)]
            # down_right_diagonal_checkmate = [matrix[row_][col_] for row_ in range(row + 1, len(matrix)) for col_ in range(row, row + 1)]
            # down_left_diagonal_checkmate = [matrix[row_][col_] for row_ in range(row + 1, len(matrix)) for col_ in
            #                                  range(row, row + 1)]

            while True:
                current_row, current_col = step(current_row, current_col)
                if is_in_board_boundaries(current_row, current_col, matrix):
                    if matrix[current_row][current_col] == "Q":
                        break
                    elif matrix[current_row][current_col] == "K":
                        queen_positions_list.append([row, col])
                        break
                else:
                    break
if queen_positions_list:
    [print(x) for x in queen_positions_list]
else:
    print('The king is safe!')

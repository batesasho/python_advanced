input_1 = """4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)"""


# sys.stdin = StringIO(input_1)


def in_matrix_boundaries(row, col, matrix):
    if row in range(len(matrix)) and col in range(len(matrix)):
        return True
    return False


matrix_size = int(input())
matrix = []
[matrix.append(matrix_size * ["."]) for x in range(matrix_size)]
number_of_bombs = int(input())
for bombs in range(number_of_bombs):
    row_bomb, col_bomb = list(map(int, input().replace("(", "").replace(")", "").split(", ")))
    if row_bomb in range(len(matrix)) and col_bomb in range(len(matrix)):
        matrix[row_bomb][col_bomb] = "*"
direction = {"right": lambda r, c: (r, c + 1),
             "left": lambda r, c: (r, c - 1),
             "up": lambda r, c: (r - 1, c),
             "down": lambda r, c: (r + 1, c),
             "up_left_diagonal": lambda r, c: (r - 1, c - 1),
             "up_right_diagonal": lambda r, c: (r - 1, c + 1),
             "down_left_diagonal": lambda r, c: (r + 1, c - 1),
             "down_right_diagonal": lambda r, c: (r + 1, c + 1)
             }

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == ".":
            count = 0
            for key, step in direction.items():
                current_row, current_col = row, col
                current_row, current_col = step(current_row, current_col)
                if in_matrix_boundaries(current_row, current_col, matrix):
                    if matrix[current_row][current_col] == "*":
                        count += 1
            matrix[row][col] = count
[print(*x) for x in matrix]

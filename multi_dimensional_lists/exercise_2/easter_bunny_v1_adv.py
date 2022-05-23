input_1 = """5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0"""


# sys.stdin = StringIO(input_1)


def number_of_rows() -> int:
    return int(input())


def matrix_size(number: int) -> list:
    matrix = []
    for row in range(number):
        matrix.append(list(int(x) if x.isdigit() else x for x in input().split()))
    return matrix


def bunny_location(matrix: list) -> [int, int]:
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == "B":
                return r, c


def is_in_matrix_boundaries(next_row: int, next_col: int, matrix):
    return True if next_row in range(len(matrix)) and next_col in range(len(matrix)) else False


# input data
number_of_matrix_rows = number_of_rows()
matrix = matrix_size(number_of_matrix_rows)
bunny_row, bunny_col = bunny_location(matrix)

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

# main ()
bunny_path = {}
sum_eggs = {}

for direction, step in directions.items():
    next_row, next_col = bunny_row, bunny_col
    while True:
        next_row, next_col = step(next_row, next_col)
        if is_in_matrix_boundaries(next_row, next_col, matrix):
            if isinstance(matrix[next_row][next_col], int):
                sum_eggs.setdefault(direction, 0)
                sum_eggs[direction] += matrix[next_row][next_col]

                bunny_path.setdefault(direction, [])
                bunny_path[direction].append([next_row, next_col])
            else:
                break
        else:
            break

# print result
direction, value = [(d, v) for (d, v) in sum_eggs.items() if v == max(sum_eggs.values())][0]
print(direction)
[print(*value, sep = "\n") for key, value in bunny_path.items() if key == direction]
print(value)

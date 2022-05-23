import sys
from io import StringIO

input_1 = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down"""
#sys.stdin = StringIO(input_1)


def matrix_dimension():
    number = int(input())
    matrix = []
    for num in range(number):
        matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    return matrix


def player_position(matrix: list) -> tuple:
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "P":
                return row, col


def is_in_matrix_boundary(matrix, next_row, next_column) -> bool:
    if next_column in range(len(matrix)) and next_row in range(len(matrix)):
        if not matrix[next_row][next_column] == "X":
            return True
    return False


matrix = matrix_dimension()
row_player, col_player = player_position(matrix)

command = input()
coins_collected = 0
is_lost_the_game = False
is_win_the_game = False
path_player = []
while command:
    if command == "up":
        if is_in_matrix_boundary(matrix, row_player - 1, col_player):
            row_player -= 1
            coins_collected += matrix[row_player][col_player]
        else:
            is_lost_the_game = True
            break
    elif command == "down":
        if is_in_matrix_boundary(matrix, row_player + 1, col_player):
            row_player += 1
            coins_collected += matrix[row_player][col_player]
        else:
            is_lost_the_game = True
            break
    elif command == "right":
        if is_in_matrix_boundary(matrix, row_player, col_player + 1):
            col_player += 1
            coins_collected += matrix[row_player][col_player]
        else:
            is_lost_the_game = True
            break
    elif command == "left":
        if is_in_matrix_boundary(matrix, row_player, col_player - 1):
            col_player -= 1
            coins_collected += matrix[row_player][col_player]
        else:
            is_lost_the_game = True
            break
    path_player.append([row_player, col_player])
    if coins_collected >= 100:
        is_win_the_game = True
        break
    command = input()
if is_lost_the_game:
    coins_collected //= 2
    print(f"Game over! You've collected {coins_collected} coins.")

if is_win_the_game:
    print(f"You won! You've collected {coins_collected // 1} coins.")

print('Your path:')
[print(x) for x in path_player]

def matrix_dimension():
    matrix = []
    for _ in range(7):
        matrix.append([int(x) if x.isdigit() else x for x in input().split()])
    return matrix


def is_inside_the_darts(matrix, row, col):
    if row in range(len(matrix)) and col in range(len(matrix)):
        return True
    return False


name_player_one, name_player_two = input().split(", ")
matrix = matrix_dimension()
player_one_points = 501
player_two_points = 501
command = list(map(int, input().replace("(", "").replace(")", "").split(", ")))
deduced_points = 0
turns = 1
is_win_the_game = False
is_player_one_win = False
is_player_two_win = False
while command:
    row_shoot, column_shoot = command

    if is_inside_the_darts(matrix, row_shoot, column_shoot):
        if isinstance(matrix[row_shoot][column_shoot], int):
            deduced_points = matrix[row_shoot][column_shoot]
        elif matrix[row_shoot][column_shoot] == "D":
            deduced_points = (matrix[0][column_shoot] + matrix[6][column_shoot] + matrix[row_shoot][0] +
                              matrix[row_shoot][6]) * 2
        elif matrix[row_shoot][column_shoot] == "T":
            deduced_points = (matrix[0][column_shoot] + matrix[6][column_shoot] + matrix[row_shoot][0] +
                              matrix[row_shoot][6]) * 3
        elif matrix[row_shoot][column_shoot] == "B":
            is_win_the_game = True

    if turns % 2 == 0:
        turns += 1
        player_one_points -= deduced_points
        if player_one_points <= 0 or is_win_the_game:
            is_player_one_win = True
            break
    else:
        player_two_points -= deduced_points
        turns += 1
        if player_two_points <= 0 or is_win_the_game:
            is_player_two_win = True
            break

    command = list(map(int, input().replace("(", "").replace(")", "").split(", ")))

print(f"{name_player_one if is_player_two_win else name_player_two} won the game with {(turns // 2)} throws!")

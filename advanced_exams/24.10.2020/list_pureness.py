from collections import deque
from sys import maxsize


def best_list_pureness(sequence: list, number_iteractions: int):
    sequence = deque(sequence)
    sum_value = 0
    max_value = - maxsize

    for numb in range(number_iteractions + 1):
        sum_value = sum([(number * index) for number, index in enumerate(sequence)])
        if sum_value > max_value:
            max_value = sum_value
            number_iteraction = numb
        sequence.appendleft(sequence.pop())
    return f'Best pureness {max_value} after {number_iteraction} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

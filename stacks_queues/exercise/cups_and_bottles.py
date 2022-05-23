import sys
from collections import deque
from io import StringIO

input_1 = """10 20 30 40 50
20 11"""
#sys.stdin = StringIO(input_1)


def number_of_cups_input() -> deque:
    return deque(map(int, input().split()))


def number_of_bottles_input() -> deque:
    return deque(map(int, input().split()))


cups_number_list = number_of_cups_input()
bottles_number_list = number_of_bottles_input()
wasted_water = deque()
used_bottles = deque()
is_bottles_empty = False
while cups_number_list:
    if bottles_number_list:
        if bottles_number_list[-1] >= cups_number_list[0]:
            bottles_number_list[-1] -= cups_number_list[0]
            cups_number_list.popleft()
            wasted_water.append(bottles_number_list.pop())
        else:
            cups_number_list[0] -= bottles_number_list[-1]
            bottles_number_list.pop()
    else:
        is_bottles_empty = True
        break
else:
    print(f"Bottles: {' '.join(map(str, bottles_number_list))}", sep = " ")
    print(f"Wasted litters of water: {sum(wasted_water)}")

if is_bottles_empty:
    print(f"Cups: {' '.join(map(str, cups_number_list))}", sep = " ")
    print(f"Wasted litters of water: {sum(wasted_water)}")

import sys
from collections import deque
from io import StringIO

input_1 = """4, 10, 10, 6, 2, 99
2"""

#sys.stdin = StringIO(input_1)

sequence = deque([int(x) for x in input().split(", ")])
index = int(input())

number = sequence[index]
count = 0
while sequence:
    evaluation_number = sequence.pop()
    if evaluation_number <= number:
        count += evaluation_number
print(count)

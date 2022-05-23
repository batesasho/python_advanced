import sys
from collections import deque
from io import StringIO

input_1 = """50
2
11 10 5 11 10 20
15 13 16
1500"""

#sys.stdin = StringIO(input_1)

price_bullet = int(input())
size_gun_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

shoots_count = 0
current_size_barrel = size_gun_barrel
while bullets and locks:
    current_bullet = bullets.pop()
    current_size_barrel -= 1
    shoots_count += 1
    value_of_intelligence -= price_bullet

    if current_bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if current_size_barrel == 0 and bullets:
        print("Reloading!")
        current_size_barrel = size_gun_barrel
if not locks:
    print(f'{len(bullets)} bullets left. Earned ${value_of_intelligence }')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
